# Function to be called to stage and push a single commit.

# Import the subprocess module so we can use Popen.
import os
import sys
from subprocess import Popen

# Make some constants to make our typing life a litte easier.
REPO_EXT = ".git"
GIT = "git"
ADD = "add"
COMMIT = "commit"
PUSH = "push"
PULL = "pull"
ORIGIN = "origin"


def get_local_repo_paths():
    pass


def stge_cmt_and_psh_w_subproc(branch_name, repo_path, commit_desc):
    """This will stage, commit, and push branch_name to
    repo_path with commit_desc.

    Arguments:
        branch_name -- Name of the branch we're working with.
        repo_path   -- Path to the git repo we're working with.
        commit_desc -- A description for the commit.
    """
    print("Staging all changes...")
    args = [GIT, ADD, "-A"]
    Popen(args, cwd=repo_path)

    print("Committing staged changes...")
    args = [GIT, COMMIT, "-a", "-m", commit_desc]
    Popen(args, cwd=repo_path)

    print("Pushing to origin...")
    args = [GIT, PUSH, ORIGIN, branch_name]
    Popen(args, cwd=repo_path)

    print("Done!")


def stge_cmt_and_psh_all(branch_names, path_list, commit_desc):
    """This will stage, commit, and push multiple repos to their
    origins.

    Arguments:
        branch_names -- List of branch names.
        path_list    -- List of repo paths.
        commit_desc  -- Commit description. Will be used for all repos.
    """
    print("Beginning repo iteration...")
    for i, (branch, path) in enumerate(zip(branch_names, path_list)):
        i_mod = ""
        cur_pass = i + 1

        if cur_pass == 1:
            i_mod = "st"
        elif cur_pass == 2:
            i_mod = "nd"
        elif cur_pass == 3:
            i_mod = "rd"
        else:
            i_mod = "th"

        i_str = f"{i+1}{i_mod}"

        print(f"Staging all changes for the {i_str} repo...")
        args = [GIT, ADD, "-A"]
        Popen(args, cwd=path)

        print(f"Committing staged changes for the {i_str} repo...")
        args = [GIT, COMMIT, "-a", "-m", commit_desc]
        Popen(args, cwd=path)

        print(f"Pushing the {i_str} repo to origin...")
        args = [GIT, PUSH, ORIGIN, branch]
        Popen(args, cwd=path)
    else:
        print("All repos have been staged, committed, and pushed!")


if __name__ == "__main__":
    cmd = sys.argv
    if len(cmd) >= 1:
        print("No arguments given.")
        exit()

    if len(cmd) > 4:
        print("Too many arguments given.")
        exit()

    stge_cmt_and_psh_w_subproc(cmd[1], cmd[2], cmd[3])
