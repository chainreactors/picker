---
title: Live Linux IR with UAC, (Thu, Jan 26th)
url: https://isc.sans.edu/diary/rss/29480
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-27
fetch_date: 2025-10-04T05:00:30.823145
---

# Live Linux IR with UAC, (Thu, Jan 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29472)
* [next](/diary/29484)

# [Live Linux IR with UAC](/forums/diary/Live%2BLinux%2BIR%2Bwith%2BUAC/29480/)

**Published**: 2023-01-26. **Last Updated**: 2023-01-26 23:07:32 UTC
**by** [Tom Webb](/handler_list.html#tom-webb) (Version: 1)

[1 comment(s)](/diary/Live%2BLinux%2BIR%2Bwith%2BUAC/29480/#comments)

The other day, I was looking for Linux IR scripts and ran across the tool Unix-like Artifacts Collector or UAC(1) created by Thiago Lahr.  As you would expect, it gathers most live stats but also collects Virtual box and Docker info and other data on the system. It can dump results files to SFTP, Azure, S3, and IBM storage natively.

With any tool, you should always test to understand how it affects your system. I ran a simple file timeline collection before and after to see what changes were made.

#git clone <https://github.com/tclahr/uac.git>

#mac-robber / >before

#uac -a live\_response ../

#mac-robber / > after

As expected, files on the system have their access time updated when the tool reads files. Some tools do reset the access times back, but this one does not. It would be best if you collected file times before running the rest of the script. You can specify this via the command line

#uac -a bodyfile/bodyfile.yaml, live\_response/\\*. .

The results are a tar.gz file; when extracted, they have artifacts in the below folder structure.

![](https://isc.sans.edu/diaryimages/images/livedir.JPG)

To see what commands it uses to gather data, you can drop into one of the folders under live response and look at at the yml files.

#cd /tmp/usb/uac/artifacts/live\_response/containers

#grep 'command:' docker.yaml

![](https://isc.sans.edu/diaryimages/images/cmd-yaml.JPG)

You can also create a super timeline with the data that it collected with a Plaso docker(2). If you do a full collection, it also grabs copies of files in the "Root" dir and the file system line in the bodyfile dir.

![](https://isc.sans.edu/diaryimages/images/body-dir.JPG)

UAC can also dump memory

#./uac -a memory\_dump/avml.yaml

Its a potent tool that acts as an IR collection "swiss army knife". You can create a collection profile and customize lots of things. Before you add it to your bag of tools, you should test it in many situations and understand its limitations and usage. After more testing and comfort with it, I plan on adding it to my group of collection tools.

Are you using another IR script that you like? Have you rolled your own? Let me know in the comments.

(1) https://github.com/tclahr/uac

(2) https://tclahr.github.io/uac-docs/super\_timeline/

--

Tom Webb

@[[email protected]](/cdn-cgi/l/email-protection)

Keywords: [DFIR](/tag.html?tag=DFIR) [forensics](/tag.html?tag=forensics) [incident response](/tag.html?tag=incident response) [linux](/tag.html?tag=linux)

[1 comment(s)](/diary/Live%2BLinux%2BIR%2Bwith%2BUAC/29480/#comments)

* [previous](/diary/29472)
* [next](/diary/29484)

### Comments

Hi Tom,

I am glad that you are testing and considering adding UAC to your bag of tools. Please let me know if you have any features or artifacts that you would like to see in future releases.

Tip: if you want to collect everything (using the 'full' profile), but need to collect the bodyfile first, you can use: ./uac -a bodyfile/bodyfile.yaml -p full /destination

Although 'bodyfile/bodyfile.yaml' is part of the 'full' profile, it will not be collected twice.

Regards.

#### Thiago Lahr

#### Jan 28th 2023 2 years ago

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