# packagescanner_cve
Run and tested with python3.6

##### jobstopackage.py #####
Prints job to package mapping

git clone {repo}
Expected working directory path ~/workspace/crunchy-postgres-bosh
python modules needed:
pip install nested_lookup simplejson vulners

Run Example:
  
python jobstopackage.py

#### localscanner.py ####
Prints out Vulnerabilities for depedent packages based on manifest.

Expected working directory path: ~/workspace/crunchy-postgres-bosh/
Uses boshjsontemp.json
python modules needed:
pip install vulners 

Run Example:
python localscanner.py

