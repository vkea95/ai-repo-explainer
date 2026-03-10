import subprocess
import os

REPO_DIR = "repos"


def clone_repo(repo_url):

    repo_name = repo_url.split("/")[-1].replace(".git", "")

    repo_path = os.path.join(REPO_DIR, repo_name)

    if os.path.exists(repo_path):
        print("Repo already exists")
        return repo_name, repo_path

    subprocess.run(["git", "clone", repo_url, repo_path])

    return repo_name, repo_path


if __name__ == "__main__":

    repo_url = "https://github.com/psf/requests"

    repo_name, repo_path = clone_repo(repo_url)

    print("Repo:", repo_name)
    print("Path:", repo_path)
