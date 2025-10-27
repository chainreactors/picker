---
title: Defense in depth -- the Microsoft way (part 81): enabling	UTF-8 support breaks existing code
url: https://seclists.org/fulldisclosure/2023/Feb/8
source: Full Disclosure
date: 2023-02-15
fetch_date: 2025-10-04T06:41:56.700660
---

# Defense in depth -- the Microsoft way (part 81): enabling	UTF-8 support breaks existing code

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

![](/shared/images/nst-icons.svg#search)

# Defense in depth -- the Microsoft way (part 81): enabling UTF-8 support breaks existing code

---

*From*: "Stefan Kanthak" <stefan.kanthak () nexgo de>
*Date*: Fri, 10 Feb 2023 14:22:42 +0100

---

```
Hi @ll,

almost 4 years ago, with Windows 10 1903, after more than a year
beta-testing in insider previews, Microsoft finally released UTF-8
support for the -A interfaces of the Windows API.

0) <https://docs.microsoft.com/en-us/windows/uwp/design/globalizing/use-utf8-code-page#activeCodePage>

   | If the ANSI code page is configured for UTF-8, -A APIs typically
   | operate in UTF-8. This model has the benefit of supporting
   | existing code built with -A APIs without any code changes.

   The last claim is but a bloody DANGEROUS lie!
   As shown hereafter, it must read instead:
   "This model has the malefit of causing buffer overruns in existing
    code!"

1) For 30 years, the documentation of the -A interfaces for file and
   directory management of the Win32 API states:
   "The maximum path name length is 260 characters."

   See <https://msdn.microsoft.com/en-us/library/aa363855.aspx>
   "CreateDirectoryA function" for example:

   | For the ANSI version of this function, there is a default string
   | size limit for paths of 248 characters (MAX_PATH - enough room
   | for a 8.3 filename). ...
   ...
   | The 255 character limit per path segment still applies.

   This constitutes a contractual GUARANTEE for the product behaviour!

2) The documentation for the file systems supported by Windows says
   too "The maximum length of a file name segment is 255 characters."
   See <https://msdn.microsoft.com/en-us/library/ee681827.aspx>
   "File System Functionality Comparison"

3) With these 2 contractually GUARANTEED preconditions, the following
   code is safe, i.e. not susceptible to a buffer overrun:
   CreateDirectoryA() fails as soon as szPath exceeds the documented
   limit which is less than the buffer size of 260 characters.

   CHAR szANSI[] = "€"; // or one of the following other 122 characters
                        // from ANSI code page 1252:
                        // ‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂ
                        // ÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ
   CHAR szPath[MAX_PATH] = "";
   do
      strcat(szPath, szANSI);
   while (CreateDirectoryA(szPath));

4) With UTF-8 support enabled, the same code now suffers from a
   buffer overrun:

   CHAR szUTF8[] = u"€"; // or "\xE2\x82\xAC"
   CHAR szPath[MAX_PATH] = "";
   do
      strcat(szPath, szUTF8);
   while (CreateDirectoryA(szPath), NULL);

   STRIKE 1!

5) Given the 2 guarantees from 1) and 2), the following code is
   also safe and not susceptible to a buffer overrun: see
   <https://msdn.microsoft.com/en-us/library/aa365740.aspx>
   "WIN32_FIND_DATAA structure" and "FindFirstFile function"
   <https://msdn.microsoft.com/en-us/library/aa364418.aspx>

   wfd.cFileName can NEVER receive a file/directory name longer
   than 255 characters, so the concatenation of C: or .\ (as
   well as C:\ and ..\ too) and wfd.cFileName NEVER overruns a
   buffer of MAX_PATH!

   #define PATTERN "C:*" // or "C:\\*" or ".\\*" or "..\\*"

   WIN32_FIND_DATAA wfd;
   CHAR szPath[MAX_PATH] = PATTERN;
   HANDLE hFind = FindFirstFileA(szPath, &wfd);
   if (hFind != INVALID_HANDLE_VALUE) {
      do {
         strcat(szPath + strlen(PATTERN) - 1, wfd.cFileName);
         GetFileAttributesA(szPath); // do something with the
         ...                         // found file system objects
      } while (FindNextFile(hFind, &wfd));
      FindClose(hFind);
   }

6) With UTF-8 support enabled and a file or directory named
   €€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€
   (or other 86 characters from the above 123) present in the
   CWD of drive C:, FindFirstFileA() (and FindNextFileA() too)
   return a string of 86 * 3 = 258 characters in wfd.cFileName
   which causes a buffer overrun in previously safe code!

   STRIKE 2!

7) The following code enumerates ALL file system objects in a
   (root) directory or network share:

   WIN32_FIND_DATAA wfd;
   HANDLE hFind = FindFirstFileA("\\\\host\\share\\*", &wfd);
   if (hFind != INVALID_HANDLE_VALUE) {
      do { // code to process wfd.cFileName omitted
      } while (FindNextFile(hFind, &wfd));
      FindClose(hFind);
   }

8) With UTF-8 support enabled and a directory or file named
   €€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€
   (i.e. 87 or more of the 123 characters from above) present,
   both FindFirstFile() and FindNextFile() FAIL with the
   previously impossible, NEVER encountered Win32 error code
   234 alias ERROR_MORE_DATA: wfd.cFileName is to short for
   UTF-8 encoded file/directory segment names!

   STRIKE 3!

stay tuned, and far away from UTF-8 in Windows
Stefan Kanthak

PS: for the full story of Microsoft's EPIC failures with UTF-8
    in Windows, see
    <https://skanthak.homepage.t-online.de/quirks.html#quirk33>
    <https://skanthak.homepage.t-online.de/quirks.html#quirk32>
    <https://skanthak.homepage.t-online.de/quirks.html#quirk31>

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#8)
[![Next](/images/right-icon-16x16.png)](9)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#8)
[![Next](/images/right-icon-16x16.png)](9)

### Current thread:

* **Defense in depth -- the Microsoft way (part 81): enabling UTF-8 support breaks existing code** *Stefan Kanthak (Feb 14)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.c...