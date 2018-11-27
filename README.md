# packagescanner_cve
Run and tested with python3.6

## jobstopackage.py ##
Print jobs to package mapping

git clone git@github.com:fbys294/packagescanner_cve.git

Expected working directory path ~/workspace/crunchy-postgres-bosh

python modules needed:

 - pip install nested_lookup simplejson vulners

__Run Example:__
  
python jobstopackage.py

## localscanner.py ##
Print out Vulnerabilities for depedent packages based on manifest.

Expected working directory path: ~/workspace/crunchy-postgres-bosh/

Uses boshjsontemp.json

python modules needed:

 - pip install vulners 

__Run Example:__

python localscanner.py

