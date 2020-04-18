## Rename a branch
1. If you are in same branch which you want to rename then run `git branch -m <new_branch_name>`.
2. If you are in different different branch then run `git branch -m <old_branch_name> <new_branch_name>`.
3. If you want to delete the old branch and push with new name then run `git push origin :<old_branch_name> <new_branch_name>`.
4. To update the upstream run `git push origin -u <new_branch_name>`.
5. If you don't want to delete the old branch name and update the upstream by new branch name run `git push origin HEAD` (make sure that you are in new branch).


## Switching back to previous commit/Deleting the commits
- `git reset --hard <commit_id>` For moving Head to specific commit. After runnning this command Head is pointing to that specfic commit.
- `git push origin/<branch_name>` You can run this command for deleting all the above commit lies above the pointing Head. And applied to your repo.


## For viewing the graph of commits
- `git log --graph`
- `git log --graph --all`


## Squash multiple Commits into 1 commit
- `git log --pretty=oneline --abbrev-commit` This git command is useful for logging commits with it's abbrevation.
- `git rebase -i HEAD~n` This git command is used for rebasing. Here n refers to before n Head. Suppose you want to combine last 4 commits then here n will be 4.
After running this command an interactive shell will be open. Change last commits except first from pick -> s. save and exits. After this another interactive shell will be open for commiting message. Here commit whatever you want to to message commit. save and exit.
- `git push origin/<branch_name> --force` for pushing this to repo.
- `git rebase --abort` for aborting the rebasing.
- `git rebase --edit` for editing the rebasing.
- `git rebase --continue` If found something conflicting issue on the above process, then first resolve the conflict and commit it.

