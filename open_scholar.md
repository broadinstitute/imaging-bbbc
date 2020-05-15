# Depositing images for OpenScholar BBBC

Copy files to server
1. Use Finder to create a directory `/imaging/web/BBBC/high_throughput_images/BBBC999/`
1. Use Finder to copy data files to that directory

Make files available via HTTP

1. Use Finder to create a directory `/imaging/web/BBBC/htdocs/BBBC999/`
1. Log in to a Broad server
1. `cd /imaging/web/BBBC/htdocs/BBBC999`
1. For each data file, e.g. `images.zip`, do this `ln -s /imaging/web/BBBC/high_throughput_images/BBBC999/images.zip .`
1. `images.zip` is now available at https://data.broadinstitute.org/bbbc/BBBC999/images.zip

