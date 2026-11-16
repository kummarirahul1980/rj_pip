#!/usr/bin/bash
python <<'EOF'
from rj_core.helpers import jsonify

passed = 0
failed = 0

def test(name, actual, expected):
    global passed, failed
    if actual == expected:
        passed += 1
        print(f"✅ PASS: {name}")
    else:
        failed += 1
        print(f"❌ FAIL: {name}")
        print(f"   Expected: {expected!r}")
        print(f"   Actual:   {actual!r}")

# 1. Basic keyword arguments
test("Basic kwargs",
     jsonify(name="Rahul", age=19),
     {"name": "Rahul", "age": 19})

# 2. Positional dictionary - merge mode
test("Dictionary merge mode",
     jsonify({"name": "Rahul"}, __positional_dict_args__=False),
     {"name": "Rahul" })

# 3. Positional dictionary - separate mode
test("Dictionary separate mode",
     jsonify({"name": "Rahul"}, __positional_dict_args__=True),
     {"args": [{"name": "Rahul"}]})

# 4. Multiple dictionaries - merge mode
test("Multiple dictionaries merge",
     jsonify({"x": 1}, {"y": 2}, __positional_dict_args__=True),
     {"x": 1, "y": 2})

# 5. Duplicate dictionary keys - last wins
test("Dictionary First Priority Safe TEst",
     jsonify({"message": "OK"}, {"message": "Not okay"},
             __positional_dict_args__=True),
     {"message": "OK"})

# 6. Positional non-dictionary arguments
test("Positional arguments",
     jsonify("hello", 123),
     {"args": ["hello", 123]})

# 7. Mixed positional arguments - separate mode
test("Mixed arguments separate mode",
     jsonify("hello", {"name": "Rahul"}, age=19),
     {"args": ["hello", {"name": "Rahul"}], "age": 19})

# 8. Mixed positional arguments - merge mode
test("Mixed arguments merge mode",
     jsonify("hello", {"name": "Rahul"},
             __positional_dict_args__=True, age=19),
     {"args": ["hello"], "name": "Rahul", "age": 19})

# 9. Empty values filtered
test("Empty filtering",
     jsonify(name=None, city="", items=[], age=19),
     {"age": 19})

# 10. Empty values included
test("Include empty values",
     jsonify(name=None, city="", items=[],
             ___ignore_empty__=True),
     {"name": None, "city": "", "items": []})

# 11. Keyword arguments override positional dictionaries
test("Keyword precedence",
     jsonify({"message": "OK"},
             __positional_dict_args__=True,
             message="Updated"),
     {"message": "Updated", "args": []})

# 12. No input mutation
source = {"name": "Rahul", "age": None}
jsonify(source, __positional_dict_args__=True)
test("No input mutation", source, {"name": "Rahul", "age": None})

# 13. No arguments
test("No arguments", jsonify(), {})

# 14. Empty positional dictionary
test("Empty dictionary filtered",
     jsonify({}, __positional_dict_args__=True),
     {"args": []})

# 15. Nested dictionaries
test("Nested dictionary preserved",
     jsonify({"user": {"name": "Rahul"}},
             __positional_dict_args__=True),
     {"user": {"name": "Rahul"}, "args": []})

print("\n" + "=" * 40)
print(f"RESULT: {passed} PASSED | {failed} FAILED")
print("=" * 40)
EOF
