triggers:
- headless
---

The user wants necessary documentation for this pull request.

You should add documentation when these situations
- There are changes of directory structure
- New python packages was added
- New Domain Model or DB TABLE was added

All documentation should be in README.md

use following steps to apply necessary documentation

1. Fetch Pull Request Differences:
Use GitHub CLI to get the list of changed files and the diff content for the target pull request.
Example commands:
gh pr diff <PULL_REQUEST_NUMBER> --name-status (to get file statuses like A, M, D, R)
gh pr diff <PULL_REQUEST_NUMBER> (to get the actual content diff)

2. Analyze Changes to Identify Documentation Needs:
Directory Structure Changes:
From the files obtained in step 1, identify if any files were moved (e.g., R status), or if new directories were added (e.g., A status files in a new path) or removed (e.g., D status files leading to an empty directory).
Pay attention to changes in primary source directories, module locations, or significant restructuring.
New Python Packages:
Inspect diffs for changes in dependency files such as requirements.txt, pyproject.toml (e.g., under [tool.poetry.dependencies]), or setup.py.
List any newly added package names.
New Domain Models or DB Tables:
Inspect diffs for changes in model definition files (e.g., models.py, schemas.py) or database migration files.
Identify newly defined classes (for domain models) or SQL CREATE TABLE statements (for DB tables).

3. Read the Existing README.md:
Load the content of the README.md file from the root of the repository.

4. Generate Documentation Content and Append to README.md:
Based on the identified changes, create concise documentation.
Append the new documentation to relevant sections in README.md (e.g., "Project Structure," "Dependencies," "Data Models"). If a relevant section doesn't exist, create one.

5. Save the Modified README.md File.

6. Commit and Push the Changes (Recommended):
Stage the README.md file: git add README.md
Commit the changes with a descriptive message: git commit -m "docs: Update README.md for PR #<PULL_REQUEST_NUMBER>"
Push the commit to the pull request branch: git push

