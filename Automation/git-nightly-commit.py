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


def get_local_repo_paths():
    # Grab a list of subdirs immediately inside the current working dir.
    paths = next(os.walk(os.getcwd()))[1]
    repo_paths = []

    for path in paths:
        # Grab a list of subdirectories immediately inside the given path.
        sub_paths = next(os.walk(path))[1]
        for sub_path in sub_paths:
            if sub_path == ".git":
                # This will find all dirs that contain .git folders
                # and add them to the repo_paths list.
                repo_paths.append(f"{os.getcwd()}\\{path}")

    return repo_paths


def stage_commit_push(commit_desc, branch, path, i_str=0):
    """This will stage, commit, and push branch_name in
    repo_path to it's origin with commit_desc.

    Arguments:
        branch_name -- Name of the branch we're working with.
        repo_path   -- Path to the git repo we're working with.
        commit_desc -- A description for the commit.
    """
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

    print()
    print(stge_msg)
    args = [GIT, ADD, "-A"]
    subprocess.call(args, cwd=path)
    print()
    print(cmt_msg)
    args = [GIT, COMMIT, "-a", "-m", commit_desc]
    subprocess.call(args, cwd=path)
    print()
    print(psh_msg)
    args = [GIT, PUSH, ORIGIN, branch]
    subprocess.call(args, cwd=path)
    print(fin_msg)


def push_repos(branch_names, path_list, commit_desc):
    """This will stage, commit, and push multiple repos to their
    origins.

    Arguments:
        branch_names -- List of branch names.
        path_list    -- List of repo paths.
        commit_desc  -- Commit description. Will be used for all repos.
    """
    print()
    print(f"Commit Description: {commit_desc}")
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

        print("Beginning repo iteration...")
        stage_commit_push(commit_desc, branch, path, i_str)
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
        push_repos(branch_names, repo_paths, "Test Message")
