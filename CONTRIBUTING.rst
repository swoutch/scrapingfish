How to contribute to scrapingfish
#################################

Thank you for considering contributing to scrapingfish!


First time setup
****************

-   Fork scrapingfish to your GitHub account by clicking the `Fork`_ button.
-   `Clone`_ the main repository locally.

    .. code-block:: text

        $ git clone https://github.com/swoutch/scrapingfish
        $ cd scrapingfish

-   Add your fork as a remote to push your work to. Replace
    ``{username}`` with your username. This names the remote "fork", the
    default remote is "origin".

    .. code-block:: text

        $ git remote add fork https://github.com/{username}/scrapingfish

-   Create a virtualenv.

    .. code-block:: text

        $ python3 -m venv .venv
        $ . .venv/bin/activate

    On Windows, activating is different.

    .. code-block:: text

        > .venv\Scripts\activate

-   Install the development dependencies, then install scrapingfish in
    editable mode.

    .. code-block:: text

        $ pip install -r requirements/dev.txt && pip install -e .

.. _Fork: https://github.com/swoutch/scrapingfish/fork
.. _Clone: https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#step-2-create-a-local-clone-of-your-fork


Start coding
************

-   Create a branch to identify the issue you would like to work on. Branch off
    of the "main" branch.

    .. code-block:: text

        $ git fetch origin
        $ git checkout -b your-branch-name origin/main

-   Using your favorite editor, make your changes, committing as you go.
-   Include tests that cover any code changes you make. Make sure the
    test fails without your patch. Run the tests as described below.
-   Push your commits to your fork on GitHub and
    `create a pull request`_.

    .. code-block:: text

        $ git push --set-upstream fork your-branch-name

.. _create a pull request: https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request


For maintainers only
********************

Build
=====
[ -d "./dist/" ] && find ./dist/ -mindepth 1 -delete; python -m tasks.build


Lock
=====
python -m tasks.lock
