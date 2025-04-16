import subprocess
import os
import sys

def run(cmd):
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

token = os.environ.get("GIT_PAT")
if not token:
    print("ERROR: GIT_PAT environment variable is not set.")
    sys.exit(1)

run('git config --global user.email "github-actions[bot]@users.noreply.github.com"')
run('git config --global user.name "github-actions[bot]"')


run(f'git remote set-url origin https://x-access-token:{token}@github.com/Yush1902/ai-sca.git')

branch = "fix/sca-patch"
try:
    run(f"git checkout -b {branch}")
except subprocess.CalledProcessError:
    print(f"⚠️ Branch {branch} may already exist. Trying to switch...")
    run(f"git checkout {branch}")

run("mv requirements_fixed.txt requirements.txt")

run("git add requirements.txt")
run('git commit -m "chore: AI fix for SCA vulnerabilities"')

run(f"git push origin {branch}")
print("Fix branch pushed successfully.")
