# from llm_client import ask_llm
from repo_scan import build_tree,find_entry_points


def build_repo_prompt(tree, entry_points):

    prompt = f"""
You are a senior software engineer analyzing a GitHub repository.

Repository structure:

{"\n".join(tree)}

Entry points:

{"\n".join(entry_points)}

Explain briefly:
1. What this project likely does
2. What the main modules are
3. Where execution probably starts
        
        """

    return prompt


# def explain_repo(tree, entry_points):

#     prompt = build_repo_prompt(tree, entry_points)

#     response = ask_llm(prompt)

#     return response


if __name__ == "__main__":

    repo_path = "repos/requests"

    tree = build_tree(repo_path)

    print("Directory Tree:\n")

    print("\n".join(tree))

    print("\nPossible entry points:\n")

    entry_points = find_entry_points(repo_path)
    print("\n got entry_points:\n")


    promt = build_repo_prompt(tree=tree, entry_points=entry_points)

    print("\n promt:\n")
    print(promt)
