#!/bin/bash

base=`dirname "$0"`
broad_server='login01'
umask 002
rsync -crl --exclude=.git --exclude=.gitignore --exclude=.DS_Store --exclude=foo --verbose --delete --chmod=ugo=rwX $base/htdocs/ ${broad_server}:/imaging/web/BBBC/htdocs/
