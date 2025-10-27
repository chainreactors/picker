---
title: Microsoft PlayReady Complete Client Identity Compromise
url: https://cxsecurity.com/issue/WLB-2024050033
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-13
fetch_date: 2025-10-06T17:13:36.706458
---

# Microsoft PlayReady Complete Client Identity Compromise

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
|  |  | |  | | --- | | **Microsoft PlayReady Complete Client Identity Compromise** **2024.05.12**  Credit:  **[Adam Gowdiak](https://cxsecurity.com/author/Adam%2BGowdiak/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Hello All,
We have come up with two attack scenarios that make it possible to
extract private ECC keys used by a PlayReady client (Windows SW DRM
scenario) for the communication with a license server and identity
purposes.
More specifically, we successfully demonstrated the extraction of the
following keys:
- private signing key used to digitally sign license requests issued
by PlayReady client,
- private encryption key used to decrypt license responses received by
the client (decrypt license blobs carrying encrypted content keys).
A proof for the above (which Microsoft should be able to confirm) is
available at this link:
https://security-explorations.com/samples/wbpmp\_id\_compromise\_proof.txt
While PlayReady security is primary about security of content keys,
ECC keys that make up client identity are even more important. Upon
compromise, these keys can be used to mimic a PlayReady client outside
of a Protected Media Path environment and regardless of the imposed
security restrictions.
In that context, extraction of ECC keys used as part of a PlayReady
client identity constitute an ultimate compromise of a PlayReady
client on Windows ("escape" of the PMP environment, ability to request
licenses and decrypt content keys).
Content key extraction from Protected Media Path process (through XOR
key or white-box crypto data structures) in a combination with this
latest identity compromise attack means that there is nothing left to
break when it comes to Windows SW DRM implementation.
Let this serve as a reminder that PlayReady content protection
implemented in software and on a client side has little chances of a
“survival” (understood as a state of not being successfully reverse
engineered and compromised). In that context, this is vendor’s
responsibility to constantly increase the bar and with the use of all
available technological means.
Thank you.
Best Regards,
Adam Gowdiak
----------------------------------
Security Explorations -
AG Security Research Lab
https://security-explorations.com
----------------------------------
Packet Storm Editor Note - below is wbpmp\_id\_compromise\_proof.txt
c:\\_MNT\PROJECTS\WBPMP\code\toolkit>shell
# MS Play Ready / Canal+ VOD toolkit
# (c) Security Explorations 2016-2019 Poland
# (c) AG Security Research 2019-2022 Poland
loaded cdn [CDN helper]
loaded mspr [MS Play Ready toolkit]
loaded vod [CANALP VOD toolkit]
loaded cgaweb [CANALP CGAWeb toolkit]
msprcp> set CDM\_DIR cdm\w10
msprcp> identity
0C86330B0E98CD7C586F336088DAFA0E
4F72F3CBDC81C849F635AE556A73679F
902B255736B6E891F3AF30F98B0A5DBA
D9A5C7A90F8DEA029AA8FB1C95887BE3
E82DFAE7A9DB21FC1ECF33C1DADC54B7
msprcp> identity 0C86330B0E98CD7C586F336088DAFA0E -v
[0C86330B0E98CD7C586F336088DAFA0E]
PRKF
version: 3
attr: 100c Unknown
data
0000: 00 04 00 00 ....
attr: 1000 Unknown
data
0000: 00 01 10 01 00 00 00 2c 00 02 00 80 00 01 00 00 .......,........
0010: ea 3c 67 da 4e 43 de e0 00 00 00 10 30 e1 4c db .<g.NC......0.L.
0020: 9d 23 9e 97 f7 1d ac 03 13 c2 2b 69 00 01 10 02 .#........+i....
0030: 00 00 00 7c 00 01 01 00 00 00 00 40 cb 27 6f 9f ...|.......@.'o.
0040: 9f 76 46 64 54 23 19 ef 9c c7 69 0f 9c 3b e3 75 .vFdT#....i..;.u
0050: 8b d3 78 2a 8d 03 fb a8 bf 9e 1c 6d f7 10 1c 69 ..x\*.......m...i
0060: 94 2c 4d 07 d9 68 8b 61 09 85 bb d3 4e e8 58 20 .,M..h.a....N.X.
0070: e2 0c c9 bc a9 a8 1e b7 f6 59 65 7d 00 62 e4 7a .........Ye}.b.z
0080: 4a 93 87 21 00 00 00 20 93 de eb 4b ab b4 b2 c1 J..!.......K....
0090: 71 9b 3c fc cf a8 b9 7e f2 a9 4f e1 07 39 17 fd q.<.......O..9..
00a0: 23 10 72 8a 29 95 bf d8 00 01 10 11 00 00 00 3c #.r.)..........<
00b0: 00 02 00 80 2d 82 c1 90 50 2c e7 55 00 00 00 10 ....-...P,.U....
00c0: 8f 03 13 45 06 c3 b4 3e fb 7f 1d 77 e8 ca 2d 07 ...E...>...w..-.
00d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
00e0: 00 00 00 00 ....
attr: 1009 Identities
IdentityInfo
pubkey
0000: f0 34 a0 f4 28 79 dc a4 73 88 c8 fa a6 46 40 94 .4..(y..s....F@.
0010: ef 10 f7 4b f4 42 5e 2e 51 c1 08 67 9d 9a 4b 2e ...K.B^.Q..g..K.
0020: af 2b ed 89 8e dd bb eb 1b ad 68 df 9c 33 d2 8b .+........h..3..
0030: 1d f3 a5 77 1a d2 a0 a3 b9 4d 83 6d 24 a4 2a 03 ...w.....M.m$.\*.
prvkey
0000: 31 d5 b7 ab dd 28 44 52 3b 8a ac 6c e2 c5 4e 34 1....(DR;..l..N4
0010: 61 1d 97 8f e1 4f 63 e9 c0 14 8a 83 6c 5f 3f cc a....Oc.....l\_?.
IdentityInfo
pubkey
0000: 42 b2 a0 ff 38 1c 34 cc 67 06 3b 50 e1 2e 0d de B...8.4.g.;P....
0010: 74 49 55 29 38 ef 66 0c 60 5c 90 9f 8c b0 49 43 tIU)8.f.......IC
0020: 0f e7 a8 1f 2f 67 5a b2 90 5c 3e 2e 99 62 19 b4 ..../gZ...>..b..
0030: 4a 39 8b 23 64 5e 4c d7 cc 95 38 bd 3c d3 2b f7 J9.#d^L...8.<.+.
prvkey
0000: d7 60 5c 71 57 a0 01 7c 58 e2 e7 79 a8 b1 12 55 ...qW..|X..y...U
0010: 1d 72 14 f0 d9 2c ef 04 6c cc 57 c1 2e 9b e3 b4 .r...,..l.W.....
IdentityInfo
pubkey
0000: cb 27 6f 9f 9f 76 46 64 54 23 19 ef 9c c7 69 0f .'o..vFdT#....i.
0010: 9c 3b e3 75 8b d3 78 2a 8d 03 fb a8 bf 9e 1c 6d .;.u..x\*.......m
0020: f7 10 1c 69 94 2c 4d 07 d9 68 8b 61 09 85 bb d3 ...i.,M..h.a....
0030: 4e e8 58 20 e2 0c c9 bc a9 a8 1e b7 f6 59 65 7d N.X..........Ye}
prvkey
0000: 4c 33 c6 8e 0e f1 b6 f1 0c d5 31 6b 40 94 aa 68 L3........1k@..h
0010: 32 cc 68 1b 00 3b fc 65 8b c4 3c e3 cb 62 de fc 2.h..;.e..<..b..
0020: 11 ef 51 7b 92 73 a1 84 24 ac 71 33 cf 76 d3 05 ..Q{.s..$.q3.v..
0030: 44 2d 4e 12 79 3f 3f 09 7a 4e 4d 51 ac 78 a7 3c D-N.y??.zNMQ.x.<
0040: 6b k
IdentityCertChain
CERT CHAIN:
### CERT
- random
0000: 07 80 59 24 9a b6 7e 48 c3 7f 6d 38 30 af f0 b6 ..Y$...H..m80...
- seclevel 2000
- uniqueid
0000: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 ................
- pubkey\_sign
0000: 42 b2 a0 ff 38 1c 34 cc 67 06 3b 50 e1 2e 0d de B...8.4.g.;P....
0010: 74 49 55 29 38 ef 66 0c 60 5c 90 9f 8c b0 49 43 tIU)8.f.......IC
0020: 0f e7 a8 1f 2f 67 5a b2 90 5c 3e 2e 99 62 19 b4 ..../gZ...>..b..
0030: 4a 39 8b 23 64 5e 4c d7 cc 95 38 bd 3c...