---
triggers:
- fix_ci
---

The user wants to pass CI which is failed now.

TODO
1. check which CI is failed on this branch
2. check the LOG to identify what is happening and what is the reason why it fails.
3. solve problem by editing source code

TIPS
1. You can check which CI is failed on the branch like this.
`gh run list --status="failure" --branch="<BRANCH_NAME>"`
You can know RUN_ID with this result.

2. You can see detailed log like this.
`gh run view <RUN_ID>`
