# How to contribute to scrapingfish

Thank you for considering contributing to scrapingfish!


## First time setup

- Fork scrapingfish to your GitHub account by clicking the
  [Fork](https://github.com/swoutch/scrapingfish/fork) button.
- [Clone](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#step-2-create-a-local-clone-of-your-fork)
  the main repository locally.
  ```shell
  git clone https://github.com/swoutch/scrapingfish
  cd scrapingfish
  ```
- Add your fork as a remote to push your work to. Replace `{USERNAME}` with
  your username. This names the remote "fork", the default remote is "origin".
  ```shell
  git remote add fork https://github.com/{USERNAME}/scrapingfish
  ```
- Create a virtualenv.
  ```shell
  python3 -m venv .venv
  . .venv/bin/activate
  ```
  On Windows, activating is different.
  ```powershell
  .venv\Scripts\activate
  ```
- Install the development dependencies, then install scrapingfish in editable mode.
  ```shell
  pip install -r requirements/dev.txt && pip install -e .
  ```

## Each time you enter the directory
Activate the virtualenv:
```shell
python3 -m venv .venv
. .venv/bin/activate
```
Or on Windows:
```powershell
.venv\Scripts\activate
```


## Start coding

- Create a branch to identify the issue you would like to work on. Branch off
  of the "main" branch.
  ```shell
  git fetch origin
  git checkout -b your-branch-name origin/main
  ```
- Using your favorite editor, make your changes, committing as you go.
- Include tests that cover any code changes you make. Make sure the
  test fails without your patch. Run the tests as described below.
- Push your commits to your fork on GitHub and
  [create a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
  ```shell
  git push --set-upstream fork your-branch-name
  ```


## For maintainers only

### Build
```shell
python3 -m build
```

### Lock
```shell
pip-compile-multi
```
