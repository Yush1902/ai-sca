from utils import openai_helper
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

# Read the plain text Snyk results
with open("snyk_results.txt") as f:
    snyk_output = f.read()

print("📋 Raw Snyk output:")
print(snyk_output[:500])  # Preview first 500 chars

# Send to OpenAI for fix suggestions
fixed_requirements = openai_helper.get_fixes_from_ai(snyk_output)

# Save the updated requirements file
with open("requirements_fixed.txt", "w") as f:
    f.write(fixed_requirements)

print("✅ Fixed requirements written.")
