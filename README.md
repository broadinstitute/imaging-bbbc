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
    pyenv local bbbc
    pip2 install jinja2
    

## Adding a new dataset

1. Create an issue to add the new dataset
1. `git checkout -b issues/XX` to checkout a new branch. Replace `XX` with the issue number.
1. `git push -u origin issues/XX` 
1. Add new entry in `IMAGE_SETS` in `make.py` corresponding to this dataset
1. Add new template html file in `templates`
1. Run `./make.py` to create the `index.html` for the dataset page in `htdocs` programmatically
1. The `index.html` page will get created under `htdocs/BBBC<NEW-DATASET>/`. 
1. Copy files related to this dataset, such as the images and ground truth csv files, to  `/imaging/web/BBBC/high_throughput_images` (located on `neon` server). Then, in htdocs, for each file, create symbolic link to the file in `/imaging/web/BBBC/high_throughput_images`. E.g. if you want to add a file called `images.zip` to the dataset `BBBC999`, first copy `images.zip` to `/imaging/web/BBBC/high_throughput_images/BBBC999/`, then in your repo, cd to `htdocs/BBBC999/` and create a softlink to that file by running `ln -s /imaging/web/BBBC/high_throughput_images/BBBC999/images.zip .`. 
1. Run `git status` to see what files have changed or have been added. Check to make sure that you want to add all the new or changed files that show up. Delete any untracked files that you don't want to commit. 
1. Once you've verified the files in the previous step, do `git add .` to stage all the changed / untracked files for a commit.
1. Run `git commit -m "Added new dataset BBBC<NEW-DATASET>"` 
1. Run `git push -u origin issues/XX`. Replace `XX` with the issue number.
1. Create a PR from this branch and have someone review it.
1. Once accepted, merge the PR
1. Run `./publish.sh` to upload the files to the web server.

