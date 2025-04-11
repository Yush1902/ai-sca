import json
from utils import parser, openai_helper

# Load SCA scan result
with open("snyk_results.json") as f:
    scan_data = json.load(f)

# Extract vulnerability summary
summary = parser.extract_vulnerable_packages(scan_data)

# Call OpenAI to generate fixes
fixed_requirements = openai_helper.get_fixes_from_ai(summary)

# Write fixed dependencies
with open("requirements_fixed.txt", "w") as f:
    f.write(fixed_requirements)

print("✅ Fixed requirements written.")
