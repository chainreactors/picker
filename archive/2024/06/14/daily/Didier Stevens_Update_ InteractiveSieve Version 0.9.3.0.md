---
title: Update: InteractiveSieve Version 0.9.3.0
url: https://blog.didierstevens.com/2024/06/13/update-interactivesieve-version-0-9-3-0/
source: Didier Stevens
date: 2024-06-14
fetch_date: 2025-10-06T16:56:03.666196
---

# Update: InteractiveSieve Version 0.9.3.0

# [Didier Stevens](https://blog.didierstevens.com/)

## Thursday 13 June 2024

### Update: InteractiveSieve Version 0.9.3.0

Filed under: [Uncategorized](https://blog.didierstevens.com/category/uncategorized/) — Didier Stevens @ 0:00

New features in this version of InteractiveSieve are:

Load and Split

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-163441.png)

With Load and Split; you can load a CSV file and split rows that have a field that contains more than one value, separated by a separator character.

Take this example:

```
IP,Count,Methods
10.0.0.220,5,GET
10.0.0.45,13554,GET|POST
10.0.0.135,54302,GET|HEAD|POST
```

Fields in column Methods can have more than one value: GET, POST and/or HEAD. These values are separated by a pipe | character.

Simply loading this CSV file in InteractiveSieve gives this:

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-164041.png)

While using Load and Split with separator | for column 3 (Methods) gives this:

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-164135-1.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-164148-1.png)

Ignore Comments

The Options dialog has now a field “Ignore comments”:

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-164451-1.png)

This can be used to ignore each line that starts with the given line-comment character.

Take this CSV file for example:

```
#Produced 2024/06/01
IP,Count,Methods
10.0.0.220,5,GET
10.0.0.45,13554,GET|POST
#Extra comment
10.0.0.135,54302,GET|HEAD|POST
```

When loaded in InteractiveSieve without “Ignore comments” character, the result is this:

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-165045-1.png)

And providing line-comment character # gives this:

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-165133.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-165153.png)

Show

The Show command in the right-click menu for a row gives this dialog:

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-165519.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-165604.png)

Sum

The Sum command in the right-click menu for a cell can be used to sum the numerical values of that column. There is no need to convert the text to numbers first.

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-165831.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-165858.png)

Group

And finally, there’s the Group command in the right-click menu for a column.

This is a bit the opposite of Load and Split.

Take this CSV file for example:

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-170404.png)

Let’s say I want to group Methods by IP address. First I specify that column IP is the index:

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-170516.png)

Next I select column Methods to Group:

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-170731.png)

And then I specify the separator (~ in this example):

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-170848.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-170909.png)

The original values can be restored with Restore from group:

![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-171129.png)
![](https://blog.didierstevens.com/wp-content/uploads/2024/06/20240601-171143.png)
[InteractiveSieve\_V\_0\_9\_3\_0.zip](https://didierstevens.com/files/software/InteractiveSieve_V_0_9_3_0.zip) ([http](http://didierstevens.com/files/software/InteractiveSieve_V_0_9_3_0.zip))
MD5: 09FE2F374A789EDA8B9BC2A9DFE9E732
SHA256: A3AA9790772466953A3C37785C7F18E0B0201BC1CABEB8D12F674E0BDBF0FDA2

### Share this:

* [Click to share on Facebook (Opens in new window)
  Facebook](https://blog.didierstevens.com/2024/06/13/update-interactivesieve-version-0-9-3-0/?share=facebook)
* [Click to share on X (Opens in new window)
  X](https://blog.didierstevens.com/2024/06/13/update-interactivesieve-version-0-9-3-0/?share=x)

### *Related*

[Leave a Comment](https://blog.didierstevens.com/2024/06/13/update-interactivesieve-version-0-9-3-0/#respond)

## Leave a Comment [»](#postcomment "Leave a comment")

No comments yet.

[RSS feed for comments on this post.](https://blog.didierstevens.com/2024/06/13/update-interactivesieve-version-0-9-3-0/feed/) [TrackBack URI](https://blog.didierstevens.com/2024/06/13/update-interactivesieve-version-0-9-3-0/trackback/)

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
  + [Quickpost: No Escape From PDF](https://blog.didierstevens.com/2010/06/29/quickpost-no-escape-from-pdf/)
  + [Escape From PDF](https://blog.didierstevens.com/2010/03/29/escape-from-pdf/)
  + [Didier Stevens Suite](https://blog.didierstevens.com/didier-stevens-suite/)
* ## Categories

  + [.NET](https://blog.didierst...