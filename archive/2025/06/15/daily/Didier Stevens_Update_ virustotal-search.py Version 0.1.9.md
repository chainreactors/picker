---
title: Update: virustotal-search.py Version 0.1.9
url: https://blog.didierstevens.com/2025/06/14/update-virustotal-search-py-version-0-1-9/
source: Didier Stevens
date: 2025-06-15
fetch_date: 2025-10-06T22:52:46.794619
---

# Update: virustotal-search.py Version 0.1.9

# [Didier Stevens](https://blog.didierstevens.com/)

## Saturday 14 June 2025

### Update: virustotal-search.py Version 0.1.9

Filed under: [My Software](https://blog.didierstevens.com/category/my-software/),[Update](https://blog.didierstevens.com/category/update/) — Didier Stevens @ 0:00

I added a quota feature to virustotal-search.py’s -l (–limitrequests) option.

-l is an option to limit the number of requests: you specify the maximum number of requests to make, and virustotal-search.py will stop once that maximum is reached. Remark that virustotal-search.py does 4 hash lookups per requests, thus if your remaining quota for the day is 1000, you can use -l 250 to perform a maximum of requests without exceeding your total quota (250 = 1000 / 4).

With this new version, you can also instruct virustotal-search.py to calculate (via the API) how much remaining quota you have, and use that to decide how much queries to perform. This is done with keyword quota:. The syntax is: -l quota:groupid,maximum,reserve.

groupid is the group ID your account belongs to. For example sans\_isc.

maximum is your daily API quota: how many lookups can you do in one day.

And reserve is the number of lookups you want to save: how many lookups should remain when virustotal-search.py has finished.

Let’s try an example: assume you want virustotal-search.py to do as much queries as possible, but leave a reserve of 100 lookups. Option -l will look like this: -l quota:sans\_isc,10000,100.

sans\_isc is your group ID, 10000 is the daily API quota, 100 is the reserve.

If you want virustotal-search.py to query your remaining quota, without doing any lookups, use string query as reserve. Like this: l quota:sans\_isc,10000,query.

![](https://blog.didierstevens.com/wp-content/uploads/2025/06/image.png)

In this example, 3896 lookups have been consumed, and that gives 10000 – 3896 = 6104 remaining lookups. To lookup file hashes, that means there are 6104 / 4 = 1526 remaining queries.

Thus in this case, starting virustotal-search.py with option -l quota:sans\_isc,10000,0 would be the same as -l 1526. The difference is that in the first case, you don’t have to calculate the value 1526, virustotal-search does this for you.

You can combine this feature with option –sleep to have virustotal-search.py use the remaining lookups at the end of the day.

For example, virustotal-search.py –sleep 01:45:00 -l quota:sans\_isc,10000,10 will have virustotal-search.py wait until it’s 01:45:00 (15 minutes before UTC midnight in CEST), then query the amount of remaining lookups, and do the lookups so as not to exceed the quota and to leave 10 lookups available.

[virustotal-search\_V0\_1\_9.zip](https://didierstevens.com/files/software/virustotal-search_V0_1_9.zip) ([http](http://didierstevens.com/files/software/virustotal-search_V0_1_9.zip))
MD5: 8A8D8C47A02D07AAA36FAB5A8667BC54
SHA256: A6062F7C3D910E8B090DF77C81BBF3A0ADE504A4F0F504325C009D9FC792B266

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2025/06/14/update-virustotal-search-py-version-0-1-9/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2025/06/14/update-virustotal-search-py-version-0-1-9/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2025/06/14/update-virustotal-search-py-version-0-1-9/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2025/06/14/update-virustotal-search-py-version-0-1-9/feed/) [TrackBack URI](https://blog.didierstevens.com/2025/06/14/update-virustotal-search-py-version-0-1-9/trackback/)

### Leave a Reply (comments are moderated)

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

* ## Pages

  + [About](https://blog.didierstevens.com/about/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
  + [Links](https://blog.didierstevens.com/links/)
  + [My Python Templates](https://blog.didierstevens.com/my-python-templates/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Professional](https://blog.didierstevens.com/professional/)
  + [Programs](https://blog.didierstevens.com/programs/)
    - [Ariad](https://blog.didierstevens.com/programs/ariad/)
    - [Authenticode Tools](https://blog.didierstevens.com/programs/authenticode-tools/)
    - [Binary Tools](https://blog.didierstevens.com/programs/binary-tools/)
    - [CASToggle](https://blog.didierstevens.com/programs/castoggle/)
    - [Cobalt Strike Tools](https://blog.didierstevens.com/programs/cobalt-strike-tools/)
    - [Disitool](https://blog.didierstevens.com/programs/disitool/)
    - [EICARgen](https://blog.didierstevens.com/programs/eicargen/)
    - [ExtractScripts](https://blog.didierstevens.com/programs/extractscripts/)
    - [FileGen](https://blog.didierstevens.com/programs/filegen/)
    - [FileScanner](https://blog.didierstevens.com/programs/filescanner/)
    - [HeapLocker](https://blog.didierstevens.com/programs/heaplocker/)
    - [MyJSON Tools](https://blog.didierstevens.com/programs/myjson-tools/)
    - [Network Appliance Forensic Toolkit](https://blog.didierstevens.com/programs/network-appliance-forensic-toolkit/)
    - [Nokia Time Lapse Photography](https://blog.didierstevens.com/programs/nokia-time-lapse-photography/)
    - [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
    - [OllyStepNSearch](https://blog.didierstevens.com/programs/ollystepnsearch/)
    - [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
    - [Shellcode](https://blog.didierstevens.com/programs/shellcode/)
    - [SpiderMonkey](https://blog.didierstevens.com/programs/spidermonkey/)
    - [Translate](https://blog.didierstevens.com/programs/translate/)
    - [USBVirusScan](https://blog.didierstevens.com/programs/usbvirusscan/)
    - [UserAssist](https://blog.didierstevens.com/programs/userassist/)
    - [VirusTotal Tools](https://blog.didierstevens.com/programs/virustotal-tools/)
    - [XORSearch & XORStrings](https://blog.didierstevens.com/programs/xorsearch/)
    - [YARA Rules](https://blog.didierstevens.com/programs/yara-rules/)
    - [ZIPEncryptFTP](https://blog.didierstevens.com/programs/zipencryptftp/)
  + [Public Drafts](https://blog.didierstevens.com/public-drafts/)
    - [Cisco Tricks](https://blog.didierstevens.com/public-drafts/cisco-tricks/)
  + [Screencasts & Videos](https://blog.didierstevens.com/screencasts-videos/)
* Search for:
* ## Top Posts

  + [PDF Tools](https://blog.didierstevens.com/programs/pdf-tools/)
  + [oledump.py](https://blog.didierstevens.com/programs/oledump-py/)
  + [My Software](https://blog.didierstevens.com/my-software/)
  + [Decrypting TLS Streams With Wireshark: Part 1](https://blog.didierstevens.com/2020/12/14/decrypting-tls-streams-with-wireshark-part-1/)
  + [WebDAV Traffic To Malicious Sites](https://blog.didierstevens.com/2017/11/13/webdav-traffic-to-malicious-sites/)
* ## Categories

  + [.NET](https://blog.didierstevens.com/category/net/)
  + [010 Editor](https://blog.didierstevens.com/category/010-editor/)
  + [Announcement](https://blog.didierstevens.com/category/announcement/)
  + [Arduino](https://blog.didierstevens.com/category/arduino/)
  + [Bash Bunny](https://blog.didierstevens.com/category/bash-bunny/)
  + [Beta](https://blog.didierstevens.com/category/beta/)
  + [bpmtk](https://blog.didierstevens.com/category/bpmtk/)
  + [Certification](https://blog.didierstevens.com/category/certification/)
  + [Didier Stevens Labs](https://blog.didierstevens.com/category/didier-stevens-labs/)
  + [Eee PC](https://blog.didierstevens.com/category/eee-pc/)
  + [Elec](https://blog.didierstevens.com/category/elec/)
  + [Encryption](https://blog.didierstevens.com/category/encryption/)
  + [Entertainment](https://blog.didierstevens.com/category/entertainment/)
  + [Fello...