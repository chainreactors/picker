---
title: India’s Aadhar card source code disclosure via exposed .svn/wc.db
url: https://infosecwriteups.com/indias-aadhar-card-source-code-disclosure-via-exposed-svn-wc-db-c05519ea7761?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-16
fetch_date: 2025-10-04T03:59:32.385113
---

# India’s Aadhar card source code disclosure via exposed .svn/wc.db

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fc05519ea7761&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Findias-aadhar-card-source-code-disclosure-via-exposed-svn-wc-db-c05519ea7761&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Findias-aadhar-card-source-code-disclosure-via-exposed-svn-wc-db-c05519ea7761&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-c05519ea7761---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-c05519ea7761---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# India’s Aadhar card source code disclosure via exposed .svn/wc.db

[![0xLittleSpidy](https://miro.medium.com/v2/resize:fill:64:64/1*TiAuVDlZlWEv4rbB9uckRQ.jpeg)](https://0xlittlespidy.medium.com/?source=post_page---byline--c05519ea7761---------------------------------------)

[0xLittleSpidy](https://0xlittlespidy.medium.com/?source=post_page---byline--c05519ea7761---------------------------------------)

3 min read

·

Jan 2, 2023

--

2

Listen

Share

Press enter or click to view image in full size

![]()

Hi Guys, I recently found a .svn/wc.db folder exposed on a [resident.uidai.gov.in](https://resident.uidai.gov.in), and used it to reconstruct the Web app’s source code. I cannot find any article about svn, So this will be very useful for those who find svn on a website.

> what is .svn/wc.db?

The .svn/wc.db file is a database file used by Subversion, a version control system and it contains information about the state of the working copy, including the revision numbers of the files, the dates and times when they were last updated, and any local modifications that have been made. It is used by Subversion to track changes to the files in the working copy and to manage the process of merging changes from the repository into the working copy.

> what is the Difference between .svn/wc.db and .git ?

.svn/wc.db is a database file used by Subversion, a centralized VCS

.git, on the other hand, is a database file used by Git, a distributed VCS

**Note: I haven’t used any directory or file brute-forcing. I used a chrome extension called** [**DotGit**](https://chrome.google.com/webstore/detail/dotgit/pampamgoihgcedonnphgehgondkhikel?hl=en) **which automatically finds .git and .svn in a website while surfing.**

Let's Look at How I downloaded all the source codes of an Aadhar website

I just appended .svn/wc.db to <https://resident.uidai.gov.in> and downloaded the database file

```
wget https://resident.uidai.gov.in/.svn/wc.db
```

when I opened the database file with SQLite browser. I came occurs a lot of tables.

```
sqlitebrowser wc.db
```

Press enter or click to view image in full size

![]()

The nodes table contains many columns but 2 important columns are “local\_relpath” and “checksum”

local\_relpath →It contains the path of a web app

checksum → It contains a checksum value of the path

**For Example:**

local\_relpath = /Bio-Lock-Enable.php

checksum = $sha1$c7fb9f76455733203cb734de0c6016366d729458

I know that SVN keeps a backup copy of all files in a one location

```
.svn/pristine/<XX>/<CHECKSUM>.svn-base
```

1. CHECKSUM is Sha1 sum of the file (remove $sha1$)
2. XX is the first two characters of CHECKSUM.

```
https://resident.uidai.gov.in/.svn/pristine/c7/c7fb9f76455732203cb734de0c6016366d729428.svn-base
```

It is easy to download a single file with wget command. but I have more than 500 paths.so I wrote a simple script to download all the source code.

link to the below code ↓

<https://gist.github.com/0xLittleSpidy/d57446737071f119f452d5bc95721864>

script to download all the source code

Press enter or click to view image in full size

![]()

Downloaded source code

Finally, I got the complete source code of the Aadhar website.

The Indian government has fixed the issue and I encourage ethical hacking practices.

Here are some more good resources:

[## GitHub - anantshri/svn-extractor: a simple script to extract all web resources by means of.SVN…

### Many a times web application pen-testers are encountered with the presence of .svn folders. For those not aware .svn…

github.com](https://github.com/anantshri/svn-extractor?source=post_page-----c05519ea7761---------------------------------------)

[## Hacking the .SVN directory (Archive)

### This comes from a blog post I wrote on 01/26/2009. I see people are still searching for it and landing at my old site…

www.adamgotterer.com](https://www.adamgotterer.com/post/28125474053/hacking-the-svn-directory-archive?source=post_page-----c05519ea7761---------------------------------------)

Special thanks to [Dinesh Kumar](https://www.linkedin.com/in/dhina016/) for guiding me.

Thanks for taking the time to read my write-up.

### Want to Connect? Please consider following me on [Medium](https://0xlittlespidy.medium.com/), and [Twitter](https://twitter.com/0xLittleSpidy), connecting with me on [LinkedIn](https://www.linkedin.com/in/pradeep21801/), or [buying me a coffee](https://www.buymeacoffee.com/0xLittleSpidy)!

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----c05519ea7761---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----c05519ea7761---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----c05519ea7761---------------------------------------)

[Web Application Security](https://medium.com/tag/web-application-security?source=post_page-----c05519ea7761---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----c05519ea7761---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c05519ea7761---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--c05519ea7761---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--c05519ea7761---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--c05519ea7761---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-p...