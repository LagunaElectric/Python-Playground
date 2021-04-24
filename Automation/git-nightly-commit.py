# Function to be called to stage and push a single commit.

import os
import sys
import subprocess
from typing import Optional

# Make some constants to make our typing life a litte easier.
REPO_EXT = ".git"
GIT = "git"
ADD = "add"
COMMIT = "commit"
PUSH = "push"
PULL = "pull"
ORIGIN = "origin"


def get_immediate_sub_dirs(path: str) -> list[str]:
    return next(os.walk(path))[1]


def get_local_repo_paths() -> list[str]:
    paths = get_immediate_sub_dirs(os.getcwd())
    sub_paths = [get_immediate_sub_dirs(path) for path in paths]
    repo_paths = [f"{os.getcwd()}\\{path}" for path in sub_paths if path == REPO_EXT]
    return repo_paths


def call_git_command(print_message: str, git_args: list[str], path: str):
    print()
    print(print_message)
    args = [GIT, git_args]
    subprocess.call(args, cwd=path)


def build_index_string(i: int) -> str:
    switch = {1: "st", 2: "nd", 3: "rd", None: "th"}
    i_mod = switch.get(i) or switch[None]
    return f"{i}{i_mod}"


def stage_commit_push(
    commit_desc: str, branch: str, path: str, i_str: Optional[str] = None
):
    if i_str == None:
        stge_msg = "Staging all changes..."
        cmt_msg = "Committing staged changes..."
        psh_msg = "Pushing to origin..."
        fin_msg = "Done!"
    else:
        stge_msg = f"Staging all changes for the {i_str} repo..."
        cmt_msg = f"Committing staged changes for the {i_str} repo..."
        psh_msg = f"Pushing the {i_str} repo to origin..."
        fin_msg = f"Done with {i_str} repo!"

    args = [ADD, "-A"]
    call_git_command(stge_msg, args, path)

    args = [COMMIT, "-m", commit_desc]
    call_git_command(cmt_msg, args, path)

    args = [PUSH, ORIGIN, branch]
    call_git_command(psh_msg, args, path)

    print(fin_msg)


def push_multiple_repos(
    branch_names: list[str], path_list: list[str], commit_desc: str
):
    print()
    print(f"Commit Description: {commit_desc}")

    print("Beginning repo iteration...")
    for i, (branch, path) in enumerate(zip(branch_names, path_list), start=1):
        index_string = build_index_string(i)
        stage_commit_push(commit_desc, branch, path, index_string)
    else:
        print()
        print("All repos have been staged, committed, and pushed!")


if __name__ == "__main__":
    cmd = sys.argv

    if len(cmd) > 1:
        if len(cmd) < 5:
            stage_commit_push(cmd[1], os.path.normcase(cmd[2]), cmd[3])
        else:
            print("Too many args. Expected: 3 args")
    else:
        repo_paths = get_local_repo_paths()

        # For testing, assume all branch names will be "master"
        branch_names = ["master"] * len(repo_paths)

        print(branch_names, repo_paths)
        push_multiple_repos(branch_names, repo_paths, "Test Message")
