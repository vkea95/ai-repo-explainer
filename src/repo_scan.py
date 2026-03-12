import os
# define the directories to be ignored
IGNORE_DIRS = {
    ".git",
    ".github",
    "__pycache__",
    "node_modules",
    "dist",
    "build",
    "target",
    ".venv",
    "venv",
    "docs",
    "tests",
    "test",
    "assets",
    "images",
    "static",
}

ENTRY_FILES = {
    "main.py",
    "app.py",
    "run.py",
    "cli.py",
    "__main__.py",
    "server.py",
    "manage.py",
    "setup.py",
    "main.rs",
    "lib.rs",
    "Main.java",
    "Application.java"
}

README_FILES = {
    "README.md",
    "README.rst",
    "README.txt"
}

def read_readme(root_path):
    for name in README_FILES:
        path = os.path.join(root_path,name)
        if os.path.exists(path):
            print("reading the readme file: {path}")
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                return f.read()[:3000]
    print("there is no readme file inside the project")
    return ""


def build_tree(root_path, max_depth=2, prefix="", current_depth=0):
    if current_depth > max_depth:
        return []

    lines = []

    try:
        entries = sorted(os.listdir(root_path))
    except Exception:
        return lines

    for entry in entries:

        full_path = os.path.join(root_path, entry)

        if os.path.isdir(full_path) and entry in IGNORE_DIRS:
            continue

        lines.append(prefix + entry)

        if os.path.isdir(full_path):
            lines.extend(
                build_tree(
                    full_path,
                    max_depth,
                    prefix + "    ",
                    current_depth + 1
                )
            )

    return lines

def find_entry_points(root_path):
    entry_points = []
    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for f in files:
            if f in ENTRY_FILES:
                entry_points.append(os.path.join(root, f))

    return entry_points


if __name__ == "__main__":

    repo_path = "repos/requests"

    tree = build_tree(repo_path)

    print("Directory Tree:\n")

    print("\n".join(tree))

    print("\nPossible entry points:\n")

    entry_points = find_entry_points(repo_path)

    for ep in entry_points:
        print(ep)
