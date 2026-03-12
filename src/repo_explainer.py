from repo_scan import build_tree,find_entry_points,read_readme
from llm_client import ask_llm

def build_repo_prompt(tree, entry_points, readme):

    prompt = f"""
You are a senior software engineer analyzing a GitHub repository.

Repository structure:

{"\n".join(tree)}

Entry points:

{"\n".join(entry_points)}

README (project documentation):

{readme}

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
3. If the information is directly supported by README text, choose README.
4. If the information is inferred from file names or directory structure, choose Structure.
5. If it is a reasonable guess not directly supported by the inputs, choose Inference.
6. Do not invent facts that are not supported by the repository information.        
        """

    return prompt


def explain_repo(tree, entry_points):

    prompt = build_repo_prompt(tree, entry_points)

    response = ask_llm(prompt)

    return response


if __name__ == "__main__":

    repo_path = "repos/requests"

    tree = build_tree(repo_path)

    print("Directory Tree:\n")

    print("\n".join(tree))

    print("\nPossible entry points:\n")

    entry_points = find_entry_points(repo_path)
    print("\n got entry_points:\n")

    readme = read_readme(repo_path)

    promt = build_repo_prompt(tree=tree, entry_points=entry_points, readme=readme)

    print("\n promt:\n")
    print(promt)

    explain = ask_llm(prompt=promt)
    print("\nHere is the explaination from Gemnini\n")
    print(explain)