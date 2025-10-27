---
title: Using Linux grep and Windows findstr to Manipulate Files, (Fri, Mar 31st)
url: https://isc.sans.edu/diary/rss/29696
source: SANS Internet Storm Center, InfoCON: green
date: 2023-04-02
fetch_date: 2025-10-04T11:28:08.106159
---

# Using Linux grep and Windows findstr to Manipulate Files, (Fri, Mar 31st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29692)
* [next](/diary/29698)

# [Using Linux grep and Windows findstr to Manipulate Files](/forums/diary/Using%2BLinux%2Bgrep%2Band%2BWindows%2Bfindstr%2Bto%2BManipulate%2BFiles/29696/)

**Published**: 2023-03-31. **Last Updated**: 2023-04-01 14:24:24 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Using%2BLinux%2Bgrep%2Band%2BWindows%2Bfindstr%2Bto%2BManipulate%2BFiles/29696/#comments)

Over the years I have found grep to be very versatile. The most common use of grep is to find if the logs have a string that match an IP address, a domain, a service or protocol, some application was logged, etc.

Years ago, when I initially built my first DNS Sinkhole [[1](https://www.sans.org/white-papers/33523/)], I used several combination of grep to parse and compare files to build the bind lists of domains to sinkhole. I now use Pi-Hole [[2](https://pi-hole.net/)] which uses the same principals which is now managed via its interface.

My early sinkhole used a series of grep commands to compare two files. The following example use a wildcard list of country codes that were already blocked by the sinkhole against a list of known bad domains published on various websites [[3](https://raw.githubusercontent.com/jonschipp/mal-dnssearch/master/mandiant_apt1.dns)]. To demonstrate how to use a list to compare and remove the blocked domains, I will use my pi-hole domain list.

First step is to create the file the filter list called; toremove, which contains the following blocked top-level domains that are already blocked (it could be as many as the organization need). Another list could be applied for domains already blocked (i.e. google.com, sans.isc):

.\*\.bazar
.\*\.biz
.\*\xyz

Before we start, lest get a count of how may lines we have the file list.2.pihole.xxxx.ca.domains with wc -l to establish a baseline:

![](https://isc.sans.edu/diaryimages/images/grep_baseline.PNG)

This picture shows there is *505196* records in this file. The options use with grep are as follow:

* w - Select only those lines containing matches that form whole words.
* h - Suppress the prefixing of file names on output.
* v - Invert the sense of matching, to select non-matching lines.
* f - Obtain patterns from FILE, one per line.

The next step is to compare the top-level domain list against a downloaded domain list:

*grep -whvf* /root/toremove list.2.pihole.xxxx.ca.domains

![](https://isc.sans.edu/diaryimages/images/grep_firstrun.PNG)

This picture shows when grep was first run with the result above the command. Re-run of the same command and this time grepping for any domains ending with .xyz$ have been removed from the list. The $ at the end of xyz is to indicate the 'end of the line'.

Let’s recheck what we have left after removing the 3 top-domains from the list:

![](https://isc.sans.edu/diaryimages/images/grep_result.PNG)

We now have *375686* domains left in the list. The command removed 129510 records.

**Windows findstr**

It is possible to repeat the same search using Windows findstr. Lest list the options used to filter the file:

* /v                - Prints only lines that don't contain a match.
* /g:filename - Gets search strings from the specified file.

This is how to do it:

*findstr /v /g:*toremove list.2.pihole.xxxx.ca.domains | findstr .xyz$

![](https://isc.sans.edu/diaryimages/images/findstr_firstrun.PNG)

This is the options used with find (find /?) to count the number of lines left:

* /V - Displays all lines NOT containing the specified string.
* /C - Displays only the count of lines containing the string.
* "" - Specifies the text string to find.

Let’s recheck to confirm that findstr (findstr /?) remove the 3 top-domains from the list:

*findstr /v /g:*toremove list.2.pihole.xxxx.ca.domains | find /v /c ""

![](https://isc.sans.edu/diaryimages/images/findstr_final_count.PNG)

This output the same result as grep: *375686* domains left in the list. The command removed 129510 records.

This highlight the versality of both of these tools to work through large amout of data quickly and still obtain the same result. This is another example of Living Off the Land Binaries ([LOLBins](https://isc.sans.edu/diary/Linux%2BLOLBins%2BApplications%2BAvailable%2Bin%2BWindows/29296)).

[1] https://www.sans.org/white-papers/33523/
[2] https://pi-hole.net/
[3] https://raw.githubusercontent.com/jonschipp/mal-dnssearch/master/mandiant\_apt1.dns
[4] https://isc.sans.edu/diary/Linux+LOLBins+Applications+Available+in+Windows/29296

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Filtering](/tag.html?tag=Filtering) [findstr](/tag.html?tag=findstr) [grep](/tag.html?tag=grep) [LOLBins](/tag.html?tag=LOLBins) [Regex](/tag.html?tag=Regex) [Removing Records](/tag.html?tag=Removing Records)

[0 comment(s)](/diary/Using%2BLinux%2Bgrep%2Band%2BWindows%2Bfindstr%2Bto%2BManipulate%2BFiles/29696/#comments)

* [previous](/diary/29692)
* [next](/diary/29698)

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