---
title: Protected OOXML Spreadsheets, (Mon, Jul 15th)
url: https://isc.sans.edu/diary/rss/31070
source: SANS Internet Storm Center, InfoCON: green
date: 2024-07-16
fetch_date: 2025-10-06T17:45:13.359030
---

# Protected OOXML Spreadsheets, (Mon, Jul 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31068)
* [next](/diary/31072)

# [Protected OOXML Spreadsheets](/forums/diary/Protected%2BOOXML%2BSpreadsheets/31070/)

**Published**: 2024-07-15. **Last Updated**: 2024-07-15 04:54:57 UTC
**by** [Didier Stevens](/handler_list.html#didier-stevens) (Version: 1)

[0 comment(s)](/diary/Protected%2BOOXML%2BSpreadsheets/31070/#comments)

I was asked a question about the protection of an .xlsm spreadsheet. I've written before on the protection of .xls spreadsheets, for example in diary entries "[Unprotecting Malicious Documents For Inspection](https://isc.sans.edu/diary/Unprotecting%2BMalicious%2BDocuments%2BFor%2BInspection/27126)" and "[16-bit Hash Collisions in .xls Spreadsheets](https://isc.sans.edu/diary/16-bit%20Hash%20Collisions%20in%20.xls%20Spreadsheets/31066)"; and blog post "[Quickpost: oledump.py plugin\_biff.py: Remove Sheet Protection From Spreadsheets](https://blog.didierstevens.com/2021/02/12/quickpost-oledump-py-plugin_biff-py-remove-sheet-protection-from-spreadsheets/)".

.xlsm spreadsheats (and .xlsx) are [OOXML](https://en.wikipedia.org/wiki/Office_Open_XML) files, and are thus ZIP files containing mostly XML files:

![](https://isc.sans.edu/diaryimages/images/20240711-232852.png)

The spreadsheet I'm taking as an example here, has a protected sheet. Let's take a look at the XML file for this sheet by piping [zipdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/zipdump.py)'s output into [xmldump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/xmldump.py):

![](https://isc.sans.edu/diaryimages/images/20240711-232951.png)

XML element sheetProtection protects this sheet. If you remove this element, the sheet becomes unprotected.

The password used to protect this sheet, is hashed and the hashvalue is stored as an attribute of element sheetProtection.

Let's print out each attribute on a different line:

![](https://isc.sans.edu/diaryimages/images/20240711-233138.png)

The password is hashed hundred thousand times (attribute spinCount) with SHA-512 (attribute algorithmName) together with a salt (attribute saltValue, base64 encoded). This result is stored in attribute hashValue (base64 encoded).

Here is the algorithm in Python:

```

def CalculateHash(password, salt):
    passwordBytes = password.encode('utf16')[2:]
    buffer = salt + passwordBytes
    hash = hashlib.sha512(buffer).digest()
    for iter in range(100000):
        buffer = hash + struct.pack('<I', iter)
        hash = hashlib.sha512(buffer).digest()
    return hash

def Verify(password, salt, hash):
    hashBytes = binascii.a2b_base64(hash)
    return hashBytes == CalculateHash(password, binascii.a2b_base64(salt))
```

Spreadsheet protected-all.xlsx is a spreadsheet I created with 3 types of protections: modification protection, workbook protection and sheet protection:

![](https://isc.sans.edu/diaryimages/images/20240711-233227.png)

I released a new version of [xmldump.py](http://github.com/DidierStevens/DidierStevensSuite/blob/master/xmldump.py) to extract these hashes and format them for hashcat:

![](https://isc.sans.edu/diaryimages/images/20240711-233245.png)

For each extracted hash, the lines are:

1. the name of the containing file
2. the name of the protecting element (which can be removed should you want to disable that particular protection)
3. the hashcat compatibel hash (hash mode 25300)
4. a hashcat command to crack this hash with a wordlist

You can imagine that cracking these hashes with hashcat is rather slow, because 100,000 SHA-256 hash operations need to be executed for each candidate password. On a desktop with a NVIDIA GeForce RTX 3080 GPU, I got around 24,000 hashes per second.

Didier Stevens
Senior handler
[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/Protected%2BOOXML%2BSpreadsheets/31070/#comments)

* [previous](/diary/31068)
* [next](/diary/31072)

### Comments

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)