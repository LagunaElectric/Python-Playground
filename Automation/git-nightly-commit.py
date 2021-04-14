# Function to be called to push a single commit

import subprocess

G = "git"
PSH = "push"
PL = "pull"
OR = "origin"
A = "add"


def push_to_remote(branch_name, repo_path):
    args = [G, A, "-A"]
    subprocess.Popen(cwd=repo_path, args)
