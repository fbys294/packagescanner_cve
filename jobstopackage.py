import simplejson as json
import glob, yaml, os, re
from nested_lookup import nested_lookup

job_spec_list = []
package_spec_list = []
package_final_list = []
job_to_package = {}
package_to_files = {}
workplace_dir = "/home/pobe/Workspace/crunchy-on-demand/crunchy-postgres-bosh-new/"
#---- Yaml to Json import
'''
yamlfile = open('/tmp/bosh.yaml', 'r')
jtoy = yaml.load(yamlfile)
print (json.dumps(jtoy))

values2 = (nested_lookup('jobs', jtoy))
job_name_list = (nested_lookup('name', values2))
print("\nList of jobs")
print(job_name_list)
'''
#---
#----Function defined--------
def getpackage (pacakges):
    #packages2 = re.sub('[','', packages)
    package_list = []
    package_only = []
    # Next Work --------------------------------------------------------

    for package2 in pacakges.split(', '):
        package_dir = re.sub("/.+", "", package2)
        if os.path.isdir(workplace_dir+ "blobs/"+ package_dir):
            for files in glob.iglob(workplace_dir+ "blobs/" + package2):
                #while loop to run as many times as values in list
                package_only.append(os.path.split(files)[1])
                package_list.append(files)
        elif os.path.isdir(workplace_dir+ "src/"+ package_dir):
            for files in glob.iglob(workplace_dir + "src/" + package2):
                package_only.append(os.path.split(files)[1])
                package_list.append(files)
    return package_only

#----------------------------

'Loading file as json'
jsonFile = open('/tmp/boshjsontemp.json', 'r')
values = json.load(jsonFile)
jsonFile.close()

values2 = (nested_lookup('jobs', values))
job_name_list = (nested_lookup('name', values2))
print("\nList of jobs")
print(job_name_list)


# Find all files called spec and insert them into job_spec_list.
for specs in glob.glob("/home/pobe/Workspace/crunchy-on-demand/crunchy-postgres-bosh-new/jobs/*/spec", recursive=True ):
    job_spec_list.append(specs)

# Find all files called spec and insert them into a packages_spec_list.
for specs2 in glob.glob("/home/pobe/Workspace/crunchy-on-demand/crunchy-postgres-bosh-new/packages/*/spec", recursive=True ):
    package_spec_list.append(specs2)

print("\nPackage to files list")
print(package_spec_list)

for filename2 in package_spec_list:
    with open(filename2, 'r') as ymlfile2:
        spec_package_file = yaml.load(ymlfile2)
        #print(spec_package_file["files"])
        package_name = spec_package_file['name']
        files_name = spec_package_file['files']
        #print(spec_yaml_file['name'],spec_yaml_file['packages'])
        package_to_files[ package_name ]= files_name
print("\nPackage spec file list")
print(package_to_files)
'''
for value in package_to_files.values():
    package_final_list.append(value)
#print(package_final_list)
'''
for filename in job_spec_list:
    with open(filename, 'r') as ymlfile:
        spec_yaml_file = yaml.load(ymlfile)
        #print(section)
        name_job = spec_yaml_file['name']
        package_job = spec_yaml_file['packages']
        #print(spec_yaml_file['name'],spec_yaml_file['packages'])
        job_to_package[ name_job ] = package_job
print("\nJobs to package dict")
print(job_to_package)

#print(job_to_package)
full_list = []

'''
for folder in package_final_list():
    path = '/home/pobe/Workspace/crunchy-on-demand/crunchy-postgres-bosh-new/blob/%s' % (folder)
    for filename in os.listdir(path):
        print (path, filename)
'''

# Find all files called spec and insert them into job_spec_list.
#for specs3 in glob.glob("/home/pobe/Workspace/crunchy-on-demand/crunchy-postgres-bosh-new/blob/*/**", recursive=True )


#json_data = json.dumps(job_to_package)
#print(json_data)
#json_data[0]['haproxy'] = 'testing'
#job_to_package.update([0]['haproxy']['stop'] )
#print (job_to_package['haproxy'])
#print("Testing")
#print(job_to_package)

#The following iterates job_to_package dictionary, Prints the key, Uses the value to finds the matching' \
#key to value in the packages_to_files dictonary. While loop to only go over as many inputs in the value[list']'
print("------------------------------------------------------------")
for key, value in job_to_package.items():
    key1 = key
    value1 = value
    print(" - " + key)
    i = 0
    while (len(value) > i):
        print("   - " + value[i])
        #print("     - " + str(package_to_files.get(value[i])))
        print ("     - " + ', '.join(package_to_files.get(value[i])))
        send_value = (', '.join(package_to_files.get(value[i])))
        print("       - " + str(', '.join(getpackage(send_value))))
        i = i+1

    #for value1 in package_to_files.items():
     #   print(value1)
