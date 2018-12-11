# imaging-bbbc
Freely Downloadable Microscopy Image Sets

## Set up environment to run scripts in this repo
    brew update 
    brew install pyenv pyenv-virtualenv
    pyenv install 2.7.14
    pyenv virtualenv 2.7.14 bbbc
    git clone git@github.com:broadinstitute/imaging-bbbc.git
    # if you've already cloned, cd to the imaging-bbbc directory and git pull, then skip the next line (no need to cd in) 
    cd imaging-bbbc
    eval "$(pyenv init -)"
    pyenv shell bbbc
    pip2 install jinja2
    

## Adding a new dataset

1. Create an issue to add the new dataset (or update existing).
1. `git checkout -b issues/XX` to checkout a new branch. Replace `XX` with the issue number.
1. `git push -u origin issues/XX` 
1. Add new entry in `IMAGE_SETS` in `make.py` corresponding to this dataset. Be sure to [prefix the string](https://docs.python.org/2/tutorial/introduction.html#unicode-strings) with a `u` e.g. `u'Kaggle 2018 Data Science Bowl'`. 
1. Add new (or updates existing) template html file in `templates`. Be sure to edit the timestamp ("This page last updated YYYY-MM-DD") manually because this is no longer autogenerated for the `index.html` of the image sets.
1. Add new entry as a row under the appropriate category(s) on the image sets page.
1. You may need to do `eval "$(pyenv init -)"` followed by `pyenv shell bbbc` in order to invoke the appropriate python virtual environment.
1. Run `./make.py` to create (or update) the `index.html` for the dataset page in `htdocs` programmatically.
1. The `index.html` page will get created under `htdocs/BBBC<NEW-DATASET>/`. 
1. Copy files related to this dataset, such as the images and ground truth csv files, to  `/imaging/web/BBBC/high_throughput_images` (located on `neon` server). Then, in htdocs, for each file, create symbolic link to the file in `/imaging/web/BBBC/high_throughput_images`. E.g. if you want to add a file called `images.zip` to the dataset `BBBC999`, first copy `images.zip` to `/imaging/web/BBBC/high_throughput_images/BBBC999/`, then in your repo, cd to `htdocs/BBBC999/` and create a softlink to that file by running `ln -s /imaging/web/BBBC/high_throughput_images/BBBC999/images.zip .`. Example images can just be stored directly in the corresponding htdocs directory, but note that tif images do not work (use png, gif, or jpeg)
1. Run `git status` to see what files have changed or have been added. Check to make sure that you want to add all the new or changed files that show up. 
1. Once you've verified the files in the previous step, do `git add .` (Or, if you do not want to add all, add them individually using `git add <file>` to stage all the changed / untracked files for a commit. 
1. Delete any untracked files that you don't want to commit by `git checkout -- .` to remove the remaining unstaged files. (This often occurs due to the timestamp feature that makes it seem as though every file is being changed; you do not need to include those in the next commit, so we discard these changes from the working directory.)
1. Run `git commit -m "Added new dataset BBBC<NEW-DATASET>"` 
1. Run `git push -u origin issues/XX`. Replace `XX` with the issue number.
1. Create a PR from this branch and have someone review it, if necessary.
1. Once accepted, merge (squash and merge) the PR. Then, delete the (remote) branch. 
1. `git checkout master`
1. `git fetch origin`
1. `git pull origin master`
1. Run `./publish.sh` to upload the files to the web server.
1. `git remote prune origin` (can do `git remote prune origin --dry-run` to check first). This will clean up (prune) the origin branch.
1. `git branch -d issues/XX` to delete the local branch.

## Versioning
1. If we update a BBBC entry's data, we need to update the version (going forward as of Oct 18, 2018). To do so, duplicate the template page of the current entry, and use it to create a new BBBC page following instructions above, which will keep the old version's info, and should be clearly marked in red at the top "OUTDATED, please see latest version (here)". 
1. The main BBBC page should be edited to reflect the next version, and should now include a link to [Version 1]. And, at the bottom of the newer version, we should have a section called "Version History" followed by a line entry that includes the date, the version, and changes from the previous verion (see BBBC019 for example).
1. On the newer version page, be sure to update the version number in the citation as well.
