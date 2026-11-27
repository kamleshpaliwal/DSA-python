import re
import json

OPERATIONS = [
    (("add", "sum", "plus"), "+"),
    (("subtract", "minus", "difference"), "-"),
    (("multiply", "product", "times"), "*"),
    (("divide", "quotient"), "/"),
]
DEFAULTS = {
    "name": "unnamed_function",
    "parameters": [],
    "docstring": "No description provided.",
}


class Solution:
    def is_empty(self, v):
        return v is None or (isinstance(v, str)) and not v.strip()

    def fix(self, obj, required):
        if isinstance(obj, dict):
            for k in required:
                if k not in obj or self.is_empty(obj[k]):
                    obj[k] = DEFAULTS.get(k, "NA")
            obj["parameters"] = [
                {"name": p.get("name") or f"arg{i}", "type": p.get("type") or "Any"}
                for i, p in enumerate(obj.get("parameters"))
            ]
            obj["code"] = self.generate_code(obj)
            return obj

    def validate(self, obj, required):
        missing = [k for k in required if k not in obj or self.is_empty(obj.get(k))]
        for i, p in enumerate(obj.get("parameters", [])):
            for key in ("name", "type"):
                if self.is_empty(p.get(key)):
                    missing.append(f"parameters[{i}].{key}")
        return len(missing) > 0

    def infer_body(self, name, doc, params):
        # print("kkk", f"{name} {doc}")
        words = set(re.findall(r"[a-z]+", f"{name} {doc}".lower()))
        arg_names = [p.get("name") for p in params]
        # print("arg_names", arg_names)
        # print("words", words)
        # print("words & set(keywords)", words & set(["add", "sum", "plus"]))
        for keywords, op in OPERATIONS:
            # print("words & set(keywords)", words & set(keywords), len(arg_names))
            if words & set(keywords) and len(arg_names) >= 2:
                body = "return " + f" {op} ".join(arg_names)
                # print("body", body)
                return body

        return "stub body"

    def generate_code(self, obj):
        params = obj.get("parameters")
        args = ",".join(f'{p["name"]}:{p["type"]}' for p in params)

        body = self.infer_body(obj.get("name"), obj.get("docstring"), params)
        # print("body", body)
        code = (
            f"def {obj.get("name")}({args}): \n"
            f' """{obj.get("docstring")} """ \n'
            f"{body}\n"
        )
        if re.search(r"\bAny\b", args):
            code = "from typing import Any \n" + code
        return code

    def build(self, spec):
        parameters = [dict(p) for p in spec.get("parameters", [])]
        obj = {
            "name": spec.get("name"),
            "parameters": parameters,
            "docstring": spec.get("docstring"),
        }
        code = self.generate_code(obj)
        obj["code"] = code
        return obj

    def describe_func(self, spec, required):
        obj = self.build(spec)
        ok = self.validate(obj, required)
        if ok:
            return obj
        fixed = self.fix(obj, required)
        ok = self.validate(obj, required)
        return fixed


if __name__ == "__main__":
    solution = Solution()
    spec = {
        "name": "add",
        "parameters": [{"name": "a", "type": "int"}, {"name": "b", "type": "int"}],
        "docstring": "Add two numbers",
    }
    required = ["name", "parameters", "docstring", "code"]
    result = solution.describe_func(spec, required)
    print("result", result["code"])
    # ns = {}
    # exec(json.loads(result)["code"], ns)
    # print(ns["add"](2, 3))
