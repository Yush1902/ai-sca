import openai
import os

openai.api_key = os.getenv("API_KEY")

def get_fixes_from_ai(vuln_summary: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a security bot that fixes dependency vulnerabilities."},
            {"role": "user", "content": f"Here is a list of vulnerabilities:\n{vuln_summary}\nFix the issues and output a secure requirements.txt."}
        ]
    )
    return response['choices'][0]['message']['content']
