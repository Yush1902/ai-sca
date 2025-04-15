import json
from utils import parser, openai_helper

with open("snyk_results.json") as f:
    scan_data = json.load(f)

summary = parser.extract_vulnerable_packages(scan_data)

fixed_requirements = openai_helper.get_fixes_from_ai(summary)

with open("requirements_fixed.txt", "w") as f:
    f.write(fixed_requirements)

print("Fixed requirements written.")
