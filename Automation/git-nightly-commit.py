# Function to be called to stage and push a single commit.

# Import the subprocess module so we can use Popen.
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


def stage_commit_and_push_with_subproc(branch_name, repo_path, commit_desc):
    """This will stage, commit, and push branch_name to
    repo_path with commit_desc.

    Arguments:
        branch_name -- Name of the branch we're working with.
        repo_path   -- Path to the git repo we're working with.
        commit_desc -- A description for the commit.
    """
    args = [GIT, ADD, "-A"]
    Popen(args, cwd=repo_path)

    args = [GIT, COMMIT, "-a", "-m", commit_desc]
    Popen(args, cwd=repo_path)

    args = [GIT, PUSH, ORIGIN, branch_name]
    Popen(args, cwd=repo_path)


if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 1:
        print("No arguments given.")
        exit()

    if len(args) > 4:
        print("Too many arguments given.")
        exit()

    stage_commit_and_push_with_subproc(args[1], args[2], args[3])
