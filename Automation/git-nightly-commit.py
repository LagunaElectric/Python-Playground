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


def push_repo(branch_name, repo_path, commit_desc):
    """This will stage, commit, and push branch_name in
    repo_path to it's origin with commit_desc.

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


def push_repos(branch_names, path_list, commit_desc):
    """This will stage, commit, and push multiple repos to their
    origins.

    Arguments:
        branch_names -- List of branch names.
        path_list    -- List of repo paths.
        commit_desc  -- Commit description. Will be used for all repos.
    """
    print(f"Commit Description: {commit_desc}")
    print("Beginning repo iteration...")
    for i, (branch, path) in enumerate(zip(branch_names, path_list), start=1):
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
        out_str = f"{i_str} Repo | Branch Name: '{branch}' | Path: '{path}'."

        print(out_str)
        """ print(f"Staging all changes for the {i_str} repo...")
        args = [GIT, ADD, "-A"]
        Popen(args, cwd=path)

        print(f"Committing staged changes for the {i_str} repo...")
        args = [GIT, COMMIT, "-a", "-m", commit_desc]
        Popen(args, cwd=path)

        print(f"Pushing the {i_str} repo to origin...")
        args = [GIT, PUSH, ORIGIN, branch]
        Popen(args, cwd=path) """
    else:
        # print("All repos have been staged, committed, and pushed!")
        print("Iteration complete.")


if __name__ == "__main__":
    # Testing push_repos
    """ branch_names = ["master"] * 5
    repo_paths = [os.path.normcase(os.getcwd())] * 5

    # print(branch_names, repo_paths)
    stge_cmt_and_psh_all(branch_names, repo_paths, "Test Message") """

    # Original code
    cmd = sys.argv
    if len(cmd) <= 1:
        print("No arguments given.")
        exit()

    if len(cmd) > 4:
        print("Too many arguments given.")
        exit()

    push_repo(cmd[1], os.path.normcase(cmd[2]), cmd[3])
