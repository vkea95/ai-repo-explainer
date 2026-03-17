from llm_client import ask_llm
from repo_scan import build_tree, find_entry_points, read_readme, find_key_files, read_key_file_snippets

def build_repo_prompt(tree, entry_points, readme,snippets):

    prompt = f"""
You are a senior software engineer analyzing a GitHub repository.

Repository structure:

{"\n".join(tree)}

Entry points:

{"\n".join(entry_points)}

README (project documentation):

{readme}

Key code snippets:
{snippets}

Your task is to analyze the repository.

Return your answer in the following format.

---

## Project Purpose
Answer:
Source: README / Structure / Inference

## Main Modules
Answer:
Source: README / Structure / Inference

## Entry Points
Answer:
Source: README / Structure / Inference

## Reading Guide
Answer:
Source: README / Structure / Inference

---

Rules:

1. Choose exactly ONE source for each section.
2. Source must be one of: README, Structure, Inference.
3. If directly supported by README text, choose README.
4. If inferred from file names, code snippets, or directory structure, choose Structure.
5. If it is a reasonable guess, choose Inference.
6. Do not invent unsupported facts.       
7. If the answer is not explicitly stated in README, DO NOT label it as README.
8. If the answer is derived from file names or code, prefer Structure over README.
9. Only use README as the source if the answer is explicitly stated or directly demonstrated in the README.
10. If the answer combines README information with code structure reasoning, choose Inference instead of README.
11. If README only demonstrates example usage, but the answer identifies runtime or code-level entry points, choose Inference.
12. If the answer depends on both README examples and repository structure, choose Inference instead of README.
13. If the answer identifies where functions are defined or how they are exposed in code, choose Inference instead of README, even if README shows usage examples.
14. README examples do not define code structure. If structure or file paths are mentioned, do not use README as the source.

When identifying entry points:
- Prefer runtime entry points (e.g., main execution flow, API entry functions)
- Do NOT list build tools like setup.py, tox.ini unless no runtime entry exists

When describing modules:
- Explain relationships between modules (who calls who)
- Do not just list file names

        """

    return prompt


def explain_repo(repo_path):

    repo_path = "repos/requests"

    tree = build_tree(repo_path)

    print("Directory Tree:\n")

    print("\n".join(tree))

    print("\nPossible entry points:\n")

    entry_points = find_entry_points(repo_path)
    print("\n got entry_points:\n")

    readme = read_readme(repo_path)

    key_files = find_key_files(repo_path)
    snippets = read_key_file_snippets(repo_path, key_files)

    promt = build_repo_prompt(tree=tree, entry_points=entry_points, readme=readme, snippets=snippets)

    print("\n promt:\n")
    print(promt)

    explain = ask_llm(prompt=promt)
    print("\nHere is the explaination from Gemnini\n")
    print(explain)


if __name__ == "__main__":

    repo_path = "repos/requests"

    explain_repo(repo_path)