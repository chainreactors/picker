---
title: Formbook from Possible ModiLoader (DBatLoader) , (Sat, Jun 17th)
url: https://isc.sans.edu/diary/rss/29958
source: SANS Internet Storm Center, InfoCON: green
date: 2023-06-18
fetch_date: 2025-10-04T11:47:33.125226
---

# Formbook from Possible ModiLoader (DBatLoader) , (Sat, Jun 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29956)
* [next](/diary/29960)

# [Formbook from Possible ModiLoader (DBatLoader)](/forums/diary/Formbook%2Bfrom%2BPossible%2BModiLoader%2BDBatLoader/29958/)

**Published**: 2023-06-17. **Last Updated**: 2023-06-17 05:07:01 UTC
**by** [Brad Duncan](/handler_list.html#brad-duncan) (Version: 1)

[0 comment(s)](/diary/Formbook%2Bfrom%2BPossible%2BModiLoader%2BDBatLoader/29958/#comments)

***Introduction***

I'm currently doing a "30 days of Formbook" collection effort, generating infection traffic from recent Formbook samples and posting the results to my [blog](https://www.malware-traffic-analysis.net/).  On Friday 2023-06-16, I ran across an example that kicks off with an Excel file exploiting CVE-2017-11882 to use what seems like [ModiLoader](https://malpedia.caad.fkie.fraunhofer.de/details/win.dbatloader) (also known as DBatLoader).

I previously wrote about ModiLoader for Remcos RAT in [an ISC diary last month](https://isc.sans.edu/diary/Malspam%2Bpushes%2BModiLoader%2BDBatLoader%2Binfection%2Bfor%2BRemcos%2BRAT/29896).  In today's diary, I'll review an infection that I think is ModiLoader Formbook from my infection run yesterday (Friday, 2023-06-16).

[![](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-01a.jpg)](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-01.jpg)
*Shown above:  Flow chart for my Formbook infection from possible ModiLoader.*

***The Initial Lure***

The [initial lure](https://www.virustotal.com/gui/file/4f6e9a66f50f443d07676ef43a7f2349fc713c96522058c1c4d425da7be4a4bf) was a file created with Excel to exploit an old vulnerability for [CVE-2017-11882](https://nvd.nist.gov/vuln/detail/cve-2017-11882).  I used a Windows 7 host with Office 2007 as a vulnerable system in my lab to test the sample.

[![](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-02a.jpg)](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-02.jpg)
*Shown above:  The initial lure opened in Office 2007 Excel.*

After opening the initial lure, the file retrieved a loader-style EXE, and that loader-style EXE retrieved base64 text over HTTPS from qu[.]ax as shown below.  Approximately one minute later, the Formbook C2 traffic started.

[![](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-03a.jpg)](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-03.jpg)
*Shown above:  Traffic from the infection run filtered in Wireshark.*

Checking the [loader EXE in a sandbox](https://app.any.run/tasks/072fe147-47d3-4bf3-ad01-8b4ca632f81e) revealed the loader retrieved a base64 text file from hxxps://qu[.]ax/NNAs.wav.  The base64 text represents a malicious DLL file in reverse byte order.  Fortunately [CyberChef](https://cyberchef.io/) can easily decode the text and return the binary.

[![](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-04a.jpg)](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-04.jpg)
*Shown above:  Downloading the loader EXE's payload from hxxps://qu[.]ax/NNAs.wav in a web browser.*

*[![](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-05a.jpg)](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-05.jpg)
Shown above:  Checking the downloaded file to find it's base64 text.*

*[![](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-06a.jpg)](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-06.jpg)
Shown above:  Decoding the base64 text file in CyberChef to reveals a malicious EXE or DLL.*

[![](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-07a.jpg)](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-07.jpg)
*Shown above:  Checking the converted file and discovering it's a DLL.*

***Post-infection Forensics***

Examining my infected lab host revealed the loader EXE was made persistent through the Windows registry.  My investigation also found a copy of MSBuild.exe (a legitimate file for the Microsoft Build Engine) made persistent in the same manner I usually see for Formbook.  I've done similar, undocumented infection runs with confirmed ModiLoader samples for Formbook, and each of those also had some sort of non-Formbook, legitimate file where I would normally see a Formbook EXE.  This seems common for ModiLoader Formbook infections.

[![](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-08a.jpg)](https://isc.sans.edu/diaryimages/images/2023-06-16-isc-diary-image-08.jpg)
*Shown above:  Artifacts from my infection run.*

***Indicators of Compromise (IOCs)***

The following are malware/artifacts from this infection run.

Malware/artifacts from the infection run:

SHA256 hash: [4f6e9a66f50f443d07676ef43a7f2349fc713c96522058c1c4d425da7be4a4bf](https://www.virustotal.com/gui/file/4f6e9a66f50f443d07676ef43a7f2349fc713c96522058c1c4d425da7be4a4bf)

File size: 1,821,184 bytes
File name: DC293\_payment.xls
File type: Composite Document File V2 Document (created with Excel)
File description: File exploiting CVE-2017-11882 in vulnerable versions of Microsoft Excel

SHA256 hash: [8566d2bf58fe371e646076c60874a8fbb50de2fbf9b950c457804d316a3de89f](https://www.virustotal.com/gui/file/8566d2bf58fe371e646076c60874a8fbb50de2fbf9b950c457804d316a3de89f)

File size: 94,208 bytes
File location: htxxp://23.94.144[.]13/555/vbc.exe
File location: C:\Users\Public\cleanmgr\_rse.exe
Persistent file location: C:\Users\[username]\AppData\Roaming\bestm.exe
File type: PE32 executable (GUI) Intel 80386 Mono/.Net assembly, for MS Windows
File description: possible ModiLoader (DBatLoader) EXE for Formbook version 4.1

SHA256 hash: [16c7760898572422cac97f705e9076c35610a07fbc40aaa91b5663af923cdca7](https://www.virustotal.com/gui/file/16c7760898572422cac97f705e9076c35610a07fbc40aaa91b5663af923cdca7)

File size: 1,036,972 bytes
File location: hxxps://qu[.]ax/NNAs.wav
File type: ASCII text, with very long lines (65536), with no line terminators
File description: Base64 text retrieved by ModiLoader for Formbook
Note: File is decords to a Windows DLL in reverse byte order

SHA256 hash: [cfc4f6c4931fc8df03919d96181178a903a6ccd39eb5268ac00b3a223c027b5b](https://www.virustotal.com/gui/file/cfc4f6c4931fc8df03919d96181178a903a6ccd39eb5268ac00b3a223c027b5b)

File size: 777,728 bytes
File type: PE32 executable (DLL) (console) Intel 80386 Mono/.Net assembly, for MS Windows
File description: Windows DLL converted from the above Base64 text
Run method: unknown

SHA256 hash: [d94e9ea7dce3dd4760f48356f14a986ea1fc8f1c84864105bf815a32284296ab](https://www.virustotal.com/gui/file/d94e9ea7dce3dd4760f48356f14a986ea1fc8f1c84864105bf815a32284296ab)

File size: 261,688 bytes
File location: C:\Program Files (x86)\W2d0\k6qlvnu84nj0.exe
File type: PE32 executable (DLL) (console) Intel 80386 Mono/.Net assembly, for MS Windows
File description: Copy of legitimate Microsoft file msbuild.exe (not inherently malicious)

Windows Registry key: HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

Value 0

name: bestm
type: REG\_SZ
data: "C:\Users\[username]\AppData\Roaming\bestm.exe"

Value 1

name: YDD0P4187
type: REG\_SZ
data: C:\Program Files (x86)\W2d0\k6qlvnu84nj0.exe

HTTP GET and POST requests:

GET /tfgp/?*[string of alphanumeric characters with the following mixed in:* = \_ + *and* /*]*
POST /tfgp/

Domains used for Formbook C2 traffic:

DNS query for ***www.valleyofbreath[.]com*** - no response from DNS server
DNS query for ***www.website-dolap[.]com*** - no response from DNS server
DNS query for ***www.cloudzon[.]world*** - response: No such name
DNS query for ***www.eperq[.]buzz*** - response: No such name
DNS query for ***www.nolinkoti[.]biz*** - response: No such name
DNS query for ***www.simplepay[.]kitchen*** - response: No such n...