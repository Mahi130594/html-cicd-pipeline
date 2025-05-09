import requests
import os

# GitHub repo info
repo = "Mahi130594/html-cicd-pipeline"
branch = "main"
url = f"https://api.github.com/repos/{repo}/commits/{branch}"

# File to save the last known commit SHA
sha_file = "last_commit.txt"

def get_latest_commit_sha():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["sha"]
    else:
        print("Error fetching data from GitHub")
        return None

def read_saved_sha():
    if os.path.exists(sha_file):
        with open(sha_file, "r") as file:
            return file.read().strip()
    return ""

def save_new_sha(sha):
    with open(sha_file, "w") as file:
        file.write(sha)

def main():
    latest_sha = get_latest_commit_sha()
    saved_sha = read_saved_sha()

    if latest_sha and latest_sha != saved_sha:
        print("New commit found! Running deployment...")
        os.system("bash deploy.sh")
        save_new_sha(latest_sha)
    else:
        print("No new commits.")

if __name__ == "__main__":
    main()
