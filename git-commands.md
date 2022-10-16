## Cloning

- git clone <github url> --> it copies a repository to the local computer from github/gitlab

## Branching

- git branch --> it lists all branches on local machine
- git branch -a --> it lists all branches on local and remote
- git branch <branch name> --> creates a new branch locally, copies all files from parent branch
- git branch -D <branch name> --> deletes a branch, command cannot delete currently active branch
- git checkout <branch name> --> move from current branch to branch provided
- git checkout -b <branch name> --> creates a new branch and moves from current branch to new branch

## Add

- git add <file name> --> stages a file that is new or has been modified, only staged files can be commited to git

## Commit

- git commit -m "any message here" --> commits files to the current branch, this creates a record in git in the form of a commit id
- git commit --amend -m "some message here" --> updates the last commit, with new changes that were staged. this is used to update commits that have some mistakes without creating a new commit. this 'rewrites' git history, as the last commit id is gone and replaced with a new commit id
- git commit --amend --no-edit --> same as last command, but the commit message from old commit will be reused

## Push

git push --> pushes current branch to remote, this syncs local repository with remote repository

## Pull

git pull --> updates local branch from changes in the remote branch

## Status

- git status --> shows the state (unstaged changes and staged changes) of the current git repository

## Log

- git log --> shows the commit history of the branch
- git log --oneline --> same as last command but more concise logs
