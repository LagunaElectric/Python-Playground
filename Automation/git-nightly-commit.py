# Function to be called to stage and push a single commit.

import os
import sys
import subprocess

# Make some constants to make our typing life a litte easier.
REPO_EXT = ".git"
GIT = "git"
ADD = "add"
COMMIT = "commit"
PUSH = "push"
PULL = "pull"
ORIGIN = "origin"


def get_immediate_sub_dirs(path):
    return next(os.walk(path))[1]


def get_local_repo_paths():
    paths = get_immediate_sub_dirs(os.getcwd())
    repo_paths = []

    for path in paths:
        sub_paths = get_immediate_sub_dirs(path)

        for sub_path in sub_paths:
            if sub_path == REPO_EXT:
                repo_paths.append(f"{os.getcwd()}\\{path}")

    return repo_paths


def call_git_command(print_message, git_args, path):
    print()
    print(print_message)
    args = [GIT]
    args += git_args
    subprocess.call(args, cwd=path)


def build_index_string(i):
    i_mod = ""
    if i == 1:
        i_mod = "st"
    elif i == 2:
        i_mod = "nd"
    elif i == 3:
        i_mod = "rd"
    else:
        i_mod = "th"
    i_str = f"{i}{i_mod}"
    return i_str


def stage_commit_push(commit_desc, branch, path, i_str=0):
    stge_msg = ""
    cmt_msg = ""
    psh_msg = ""
    fin_msg = ""

    if (i_str == 0):
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

    args = [COMMIT, "-a", "-m", commit_desc]
    call_git_command(cmt_msg, args, path)

    args = [PUSH, ORIGIN, branch]
    call_git_command(psh_msg, args, path)

    print(fin_msg)


def push_multiple_repos(branch_names, path_list, commit_desc):
    print()
    print(f"Commit Description: {commit_desc}")
    for i, (branch, path) in enumerate(zip(branch_names, path_list), start=1):
        index_string = build_index_string(i)

        print("Beginning repo iteration...")
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
