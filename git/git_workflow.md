# Baseline git notes;


## 1. Fork or clone the repository;
- If repo doesn't belong to you, or don't have write access you need to fork it into your own GH account
- After forking, you can clone to your local machine:

git clone [URL_of_forked/SSH]

### 1.a. Keeping the forked-main up to date with its upstream.
- original source is often called "upstream" repository, this can be added to your forked-main with this command:

git remote add upstream https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git

- Then doublecheck the upstream repository
git remove -v

- Keep things up to date with the upstream
For merging upstream

git fetch upstream
git checkout main
git merge upstream/main
OR
git pull upstream main

For merging if you are directly accessing the main repository
git pull origin main




## 2. Create a new branch and begin working on it
### 2.a. Creathing and moving to your branch
- Create or go to your branch. Use prefixes like "feature", "hotfix", "refactor" etc... for organization

git checkout -b feature/new-feature
OR
git checkout feature/new-feature

### 2.b. Keeping your branch up to date as you develop and before you merge
- First make sure your branch is up to date as you are working and before making any PRs to make sure your branch itself is up to date.
- Before merging your branch back into main or making a pull request its good to make sure your branch is up to date.
- If there are merge conflicts, Git will let you know and you can resolve them on the branch;
- If you've forked something, make sure your fork-main is up to date with the upstream (1.a.)


git checkout main
git pull origin main
git checkout feature/new-feature-name
git merge main


### 2.c. making commits
- Then make the changes, and commit them.

git add .
git commit -m "PREFIX: message" -m "message 2"


## 3. Merging into main, or creating a pull request
Repeat 2.b. before merging or creating a Pull Request

### 3.a. Pushing your branch and creating a Pull Request
This is the workflow for collaborative workflows where you are not the maintainer;

git push origin feature/new-feature-name

- Go to the GitHub page of your forked repository (or the original repository if that's where you pushed).
- You'll likely see a message about your recently pushed branch. Click on "Compare & pull request".
- If you don't see the above message, switch to your branch using the 'branch' dropdown and then click the "New pull request" button.
- Ensure that the base fork/repository is the original repository you want to merge your changes into, and the head fork/repository is your fork with your changes.
- Fill out the pull request template with a title, description, and any other necessary details.
- Click "Create pull request".

#### 3.a.i. Address Review Feedback (if applicable):
- Once your pull request is created, maintainers of the original repository will review your changes. They might provide feedback or ask for changes.
- If changes are needed, simply make them on your local branch, commit them, and push the branch again. The pull request will automatically update with your new commits.

#### 3.a.ii. Merge (by maintainers):
- Once the maintainers are satisfied with the changes, they'll merge your pull request into the target branch of the original repository.
- The exact process might vary depending on the contributing guidelines of the particular project you're contributing to. Always read any CONTRIBUTING.md or similar documentation provided in the repository.

### 3.b. Merging into main and pushing to repo
This will merge your changes from your branch into main. Do this if you have write access / or its your own repository

git checkout main
git merge feature/new-feature
git push origin main


## 4. Deleting the branch
- After successfully merging your branch, you might want to delete the local and remote feature branches to keep your repository clean:

git branch -d feature/new-feature-name
git push origin --delete feature/new-feature-name












