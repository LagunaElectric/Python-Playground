# Function to be called to stage and push a single commit.

# Import the subprocess module so we can use Popen.
import sys
from subprocess import Popen

# Make some constants to make our typing life a litte easier.
G = "git"
A = "add"
C = "commit"
PSH = "push"
PL = "pull"
OR = "origin"

# This particular method is using the subprocess module.


# This will stage, commit, and push branch_name to repo_path with commit_desc.
def stage_commit_and_push_with_subproc(branch_name, repo_path, commit_desc):
    args = [G, A, "-A"]
    Popen(args, cwd=repo_path)

    args = [G, C, "-a", "-m", commit_desc]
    Popen(args, cwd=repo_path)

    args = [G, PSH, OR, branch_name]
    Popen(args, cwd=repo_path)


if __name__ == "__main__":
    args = sys.argv
    if len(args) >= 1:
        print("No arguments given.")
        exit()
    if len(args) > 4:
        print("Too many arguments given.")
        exit()
    stage_commit_and_push_with_subproc()
