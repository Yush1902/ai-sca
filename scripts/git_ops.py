import subprocess
import os

branch = "fix/sca-patch"

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

run('git config --global user.email "github-actions[bot]@users.noreply.github.com"')
run('git config --global user.name "github-actions[bot]"')

token = os.environ.get("GH_PAT")

run(f"git checkout -b {branch}")
run("mv requirements_fixed.txt requirements.txt")
run("git add requirements.txt")
run('git commit -m "chore: AI fix for SCA vulnerabilities"')
run(f"git push origin {branch}")
print("Pushed fix branch.")
