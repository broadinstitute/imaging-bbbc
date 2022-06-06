# Repo to manage the Broad Bioimage Benchmark Collection

https://bbbc.broadinstitute.org/

## Website updates
As of 2020, the BBBC website is managed via the OpenScholar platform rather than Github. Instructions for depositing images on the Broad server are below. Active issues related to previously held BBBC image sets should be completed then closed. No new issues should be created here. 

## Depositing images for OpenScholar BBBC

Copy files to server. Use Finder to do these steps:
1. Create a directory `/imaging/web/BBBC/high_throughput_images/BBBC999/`
1. Copy data files (e.g. `images.zip`) to that directory
1. Create a directory `/imaging/web/BBBC/htdocs/BBBC999/`
1. Copy example images (e.g. `example.jpg`) to that directory. Note that tif images do not work (use png, gif, or jpeg).

Make files available via HTTP

`example.jpg` is already available at https://data.broadinstitute.org/bbbc/BBBC999/example.jpg, but `images.zip` needs more steps

1. Log in to a Broad server
1. `cd /imaging/web/BBBC/htdocs/BBBC999`
1. For each data file, e.g. `images.zip`, do this `ln -s /imaging/web/BBBC/high_throughput_images/BBBC999/images.zip .`
1. `images.zip` is now available at https://data.broadinstitute.org/bbbc/BBBC999/images.zip
