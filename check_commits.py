# check_commit.py
import requests
import json
import os
token = os.environ.get('GITHUB_TOKEN')

REPO = "yourusername/html-ci-project"
BRANCH = "master"
TOKEN = "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"  # created a personal access token with repo access
LAST_COMMIT_FILE = "/home/mahi/HTML-Project/last_commit.txt"

headers = {"Authorization": f"token {TOKEN}"}
url = f"https://api.github.com/repos/{REPO}/commits/{BRANCH}"

response = requests.get(url, headers=headers)
commit_sha = response.json()["sha"]

# Load previous SHA
if os.path.exists(LAST_COMMIT_FILE):
    with open(LAST_COMMIT_FILE, "r") as f:
        last_sha = f.read().strip()
else:
    last_sha = ""

# If there's a new commit
if commit_sha != last_sha:
    print("New commit found. Deploying...")
    os.system("/home/mahi/HTML-Project/deploy.sh")  # path to your deploy script
    with open(LAST_COMMIT_FILE, "w") as f:
        f.write(commit_sha)
else:
    print("No new commits found.")
