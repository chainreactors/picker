---
title: Microsoft PlayReady Cryptography Weakness
url: https://cxsecurity.com/issue/WLB-2024050011
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-05-05
fetch_date: 2025-10-06T17:13:51.195118
---

# Microsoft PlayReady Cryptography Weakness

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
|  |  | |  | | --- | | **Microsoft PlayReady Cryptography Weakness** **2024.05.04**  Credit:  **[Adam Gowdiak](https://cxsecurity.com/author/Adam%2BGowdiak/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **N/A**  CWE: **N/A** | |

Hello All,
There is yet another attack possible against Protected Media Path
process beyond the one involving two global XOR keys [1]. The new
attack may also result in the extraction of a plaintext content key
value.
The attack has its origin in a white-box crypto [2] implementation.
More specifically, one can devise plaintext content key from white-box
crypto data structures of which goal is to make such a reconstruction
difficult / not possible. This alone breaks one of the main security
objective of white-box cryptography which is to protect the secret key
(unbreakability) [3].
Contrary to the initial (XOR key) attack, the white-box crypto attack
is not limited to the given narrow time window (white-box data
structures need to be present for the time of a movie decryption /
playback). Fixing it might require a completely new approach /
implementation (current one is obviously flawed).
In that context, white-box crypto attack seems to be more severe than
the XOR key one.
Additionally, a cryptographic check proving that extracted key values
correspond to real keys has been conducted for Canal+ Online, Netflix,
HBO Max, Amazon Prime Video and Sky Showtime.
The check relies on a digital cryptographic signature verification.
Such a signature is appended at the end of each license issued by
PlayReady license server.
The crypto check works as following:
- plaintext value of a digital signature key encrypted through ECC is
extracted from a Protected Media Path process
- the extracted signature key is used to calculate the AES-CMAC value
of a binary licence XMR blob
- the calculated signature value is checked against the signature
appended at the end of the issued license
- correct AES-CMAC value implicates correct signature key (and correct
content key)
The above mechanism is also used by Microsoft to verify the
correctness of decrypted content keys received from a license server.
It relies on the fact that signature key is part of the same encrypted
license blob as content key. Thus, successful extraction of a
signature key implicates successful extraction of a content key.
In the context of no confirmation / denial [4] from the platforms
indicated above as being affected, the crypto check should constitute
sufficient proof to support that claim alone.
Thank you.
Best Regards,
Adam Gowdiak
----------------------------------
Security Explorations -
AG Security Research Lab
https://security-explorations.com
----------------------------------
References:
[1] Microsoft Warbird and PMP security research
https://security-explorations.com/microsoft-warbird-pmp.html
[2] White-box cryptography, Wikipedia
https://en.wikipedia.org/wiki/White-box\_cryptography
[3] White-Box Security Notions for Symmetric Encryption Schemes
https://eprint.iacr.org/2013/523.pdf
[4] Microsoft DRM Hack Could Allow Movie Downloads From Popular
Streaming Services
https://www.securityweek.com/microsoft-drm-hacking-could-allow-movie-downloads-from-popular-streaming-services/

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024050011)

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