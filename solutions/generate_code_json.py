import re
import json
import ast
from typing import Callable, Optional

STOPWORDS = {
    "write",
    "a",
    "an",
    "the",
    "function",
    "that",
    "which",
    "to",
    "create",
    "make",
    "implement",
    "please",
    "program",
    "code",
    "for",
}


class ConformanceError(ValueError):
    pass


class Solution:

    def derive_function_name(self, prompt: str) -> str:
        words = re.findall(r"[a-z0-9]+", prompt.lower())
        kept = [word for word in words if word not in STOPWORDS]
        name = "_".join(kept[:4])
        return "fn_" + name if name[0].isdigit() else name

    def get_default_value(self, key: str, prompt: str) -> str:
        name = self.derive_function_name(prompt)

        if key in ("function_name", "name"):
            return name
        if key in ("code", "source", "source_code"):
            return f"def {name} (*args, **kwargs):\n pass"
        if key in ("language"):
            return "python"
        if key in ("description", "docstring", "summary"):
            return prompt.strip()

    def default_generator(self, prompt: str, required_keys: list) -> str:
        return {k: self.get_default_value(k, prompt) for k in required_keys}

    def validate(self, raw: str, required_keys: list) -> tuple:
        try:
            data = json.loads(raw)
        except (json.JSONDecodeError, TypeError) as e:
            return False, None, [f"not valid JSON {e}"]
        if not isinstance(data, dict):
            return False, None, ["Top-Level json is an object"]

        problems = []
        for k in required_keys:
            if k not in data:
                problems.append(f"missing key : {k}")
            elif not isinstance(data[k], str):
                problems.append(f"key {k} is not string")
            elif not data[k].strip():
                problems.append(f"key {k} is empty")

        return not problems, data, problems

    def _extract_object(self, raw: str) -> Optional[dict]:
        """Best-effort, deterministic parse of a messy draft into a dict."""
        if not isinstance(raw, str):
            return None
        text = re.sub(r"```(?:json)?", "", raw).strip()

        start, end = text.find("{"), text.find("}")

        if start == -1 or end <= start:
            return None

        text = text[start : end + 1]

        candidates = [text, re.sub(r",\s*([}\]])", r"\1", text)]

        for c in candidates:
            try:
                obj = json.loads(c)
                if isinstance(obj, dict):
                    return obj
            except json.JSONDecodeError:
                pass

            try:
                obj = ast.literal_eval(c)
                if isinstance(obj, dict):
                    return obj
            except (ValueError, json.JSONDecodeError):
                pass

            return None

    def correct(self, raw: str, prompt: str, required_keys: list) -> str:
        salvaged = self._extract_object(raw) or {}

        fixed = {}
        for k in required_keys:
            v = salvaged.get(k)
            if v is not None and not isinstance(v, str):
                v = json.dumps(v) if isinstance(v, (dict, list)) else str(v)

            if not v or not v.strip():
                v = self.get_default_value(k, prompt)
            fixed[k] = v

        # keep any extra keys the draft had (after the required ones)
        for key, value in salvaged.items():
            if key not in fixed:
                fixed[key] = value

        return json.dumps(fixed)

    def generate_code_json(
        self, prompt: str, required_keys: list, generator: Callable = None
    ) -> str:
        if not required_keys:
            raise ValueError("required_keys must not be empty")

        if not generator:
            generator = self.default_generator

        draft = generator(prompt, required_keys)
        print("draft--", draft)
        ok, _, _ = self.validate(draft, required_keys)
        if ok:
            return draft

        fixed = self.correct(draft, prompt, required_keys)
        ok, _, problems = self.validate(fixed, required_keys)

        if ok:
            return fixed
        else:
            raise ConformanceError(f"could not conform after correction: {problems}")


if __name__ == "__main__":
    prompt = "Reverse a string"
    required_keys = ["function_name", "code", "language"]
    solution = Solution()
    solution.generate_code_json(prompt, required_keys)
