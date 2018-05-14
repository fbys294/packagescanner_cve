#import os
#from pprint import pprint
import glob, subprocess, vulners, re, json
import urllib.request as urllib2

VULNERS_LINKS = {'pkgChecker':'https://vulners.com/api/v3/audit/audit/',
                 'bulletin':'https://vulners.com/api/v3/search/id/?id=%s'}
#Download Official CPE Dictionary v2.3, zip
#https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.zip
#package_info = {}
vulners_api = vulners.Vulners()
name = ""
version = ""
package_list = []




for files in glob.iglob("/home/pobe/Workspace/crunchy-on-demand/crunchy-postgres-bosh-new/blobs/*/*", recursive=True):
    #package_info = str(os.system("dpkg --info " + files))
    if "deb" in files:
        package_info = subprocess.check_output("dpkg --info " + files, shell=True)
        package_info2 = package_info.decode("utf-8")
        #Debug with print below.
        #print(package_info2)
        package_info3 = package_info2.splitlines()
        for lines in package_info3:
            if "Package:" in lines:
                name = lines
                print(name)
            elif "Version:" in lines:
                version = lines
                version2 = re.sub('[.]C(.+)', '', version, flags=re.IGNORECASE)
                print(version)
            elif "Architecture:" in lines:
                arctech = (lines.split())[1]
                name_only = (name.split())[1]
                version2_only = (version2.split())[1]
                dpkg_line = (name_only +" "+version2_only+" "+arctech)
                print("---------------------------Exploit-------------------------------")
                #print(name_only, version2_only)
                #package_exploits = vulners_api.searchExploit(name_only + " " + version2_only)
                #print(package_exploits)
                print("----------------------------Vulner-----------------------------")
                #results = vulners_api.softwareVulnerabilities("\"name_only\"", "\"version2_only\"")
                #exploit_list = results.get('exploit')
                #vulnerabilities_list = [results.get(key) for key in results if key not in ['info', 'blog', 'bugbounty']]
                print("----------------------------END--------------------------------")

                #print(exploit_list)
                #print(vulnerabilities_list)

            # aline:
               #print(line)
               #print("This is a test -----------------------------------------------------------------")
               #print(aline)
    package_list.append(dpkg_line)

print(package_list)
print("Total provided packages: %s" % len(package_list))
payload = {'os': 'ubuntu',
           'version': '14.04',
           'package': package_list}
req = urllib2.Request(VULNERS_LINKS.get('pkgChecker'))
req.add_header('Content-Type', 'application/json')
response = urllib2.urlopen(req, json.dumps(payload).encode('utf-8'))
responseData = response.read()
if isinstance(responseData, bytes):
    responseData = responseData.decode('utf8')
responseData = json.loads(responseData)
resultCode = responseData.get("result")
if resultCode == "OK":
    print(json.dumps(responseData, indent=4))
    print("Vulnerabilities:\n%s" % "\n".join(responseData.get('data').get('vulnerabilities')))
else:
    print("Error - %s" % responseData.get('data').get('error'))
