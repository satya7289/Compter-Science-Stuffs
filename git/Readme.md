

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

