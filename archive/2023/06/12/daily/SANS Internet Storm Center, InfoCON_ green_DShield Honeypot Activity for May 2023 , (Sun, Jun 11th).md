---
title: DShield Honeypot Activity for May 2023 , (Sun, Jun 11th)
url: https://isc.sans.edu/diary/rss/29932
source: SANS Internet Storm Center, InfoCON: green
date: 2023-06-12
fetch_date: 2025-10-04T11:46:58.364999
---

# DShield Honeypot Activity for May 2023 , (Sun, Jun 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29930)
* [next](/diary/29936)

# [DShield Honeypot Activity for May 2023](/forums/diary/DShield%2BHoneypot%2BActivity%2Bfor%2BMay%2B2023/29932/)

**Published**: 2023-06-11. **Last Updated**: 2023-06-11 15:39:48 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/DShield%2BHoneypot%2BActivity%2Bfor%2BMay%2B2023/29932/#comments)

It is always interesting to review what my DShield honeypot has stored the previous month, what is also interesting is how the activity vary from week to week. Beside the graph, it is the Top 10 IPs for May.

![](https://isc.sans.edu/diaryimages/images/May2023_Honeypot_Activity.PNG)![](https://isc.sans.edu/diaryimages/images/May2023_Honeypot_Top10.PNG)

This is the month of May Top 15 commands.

![](https://isc.sans.edu/diaryimages/images/May2023_Top15_command.PNG)

The first command in this list is to check what kind of system they have access too using uname -a. This command gives the actor all the information about the system including the OS, name of system, uptime, etc.

The next command delete the .ssh directory, recreate it and add its own SSH public key to .ssh in authorized\_keys to allow access to the system. According to this article [[1](https://yoroi.company/research/outlaw-is-back-a-new-crypto-botnet-targets-european-organizations/)], this apparently belong to the "Outlaw Hacking Group" which was first identified by TrendMicro in 2018.

cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized\_keys && chmod -R go= ~/.ssh && cd ~

What is interesting about this series of Linux command, it was seen only for the first 18 days of May. The activty was seen again on the 7 June.

![](https://isc.sans.edu/diaryimages/images/May2023_SSH.PNG)

The next group of commands chattr and lockr to remove any attribute that can prevent the overwriting the the .ssh hidden file. These commands aren't part of the DShield honeypot. This next command cat /proc/cpuinfo | grep name | wc -l list the number of processors. This last one is looking at the memory on this system: free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}'

This is the Top 5 script and executable uploaded for the month of May. The first two are binaries and the last three are scripts which are well known and listed in Virustotal. The first three are related the Mirai and the last 2 are IRCbot and downloader.

**May 2023 Indicator of Compromised**

The number of the right is the number of times the file was uploaded to the honeypot:

e4cc9a566e92fd87c00dfe2398f93b7badd2110cb712145e344e20aa0ddc6457 - [326](https://www.virustotal.com/gui/file/e4cc9a566e92fd87c00dfe2398f93b7badd2110cb712145e344e20aa0ddc6457)
a2c2a58995a8d79c4af92a7117d9c3ba5eb2e3b0600a5871b81558fcd7aeb97b - [34](https://www.virustotal.com/gui/file/a2c2a58995a8d79c4af92a7117d9c3ba5eb2e3b0600a5871b81558fcd7aeb97b)
818675ba09b4883e57790aff9a79669275dfe088d02dc5f5cf459b16375d17db - [13](https://www.virustotal.com/gui/file/818675ba09b4883e57790aff9a79669275dfe088d02dc5f5cf459b16375d17db)
595a0565461528e335b8a4c3e93f305bec04089c04a641c233e28a26ffca40d6 - [4](https://www.virustotal.com/gui/file/595a0565461528e335b8a4c3e93f305bec04089c04a641c233e28a26ffca40d6)
7aae334219ed0d7af2eaff729050ae2fc1bdf2c286fdc8a00be39c8f4907ff19 - [4](https://www.virustotal.com/gui/file/7aae334219ed0d7af2eaff729050ae2fc1bdf2c286fdc8a00be39c8f4907ff19)

[1] https://yoroi.company/research/outlaw-is-back-a-new-crypto-botnet-targets-european-organizations/
[2] https://otx.alienvault.com/indicator/file/b2469af4217d99b16a4b708aa29af0a60edeec3242078f42fa03b8eaf285d657
[3] https://www.geeksforgeeks.org/chattr-command-in-linux-with-examples/

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Activity](/tag.html?tag=Activity) [Commands](/tag.html?tag=Commands) [DShield](/tag.html?tag=DShield) [Honeypot](/tag.html?tag=Honeypot) [IP Activity](/tag.html?tag=IP Activity) [Statistics](/tag.html?tag=Statistics)

[0 comment(s)](/diary/DShield%2BHoneypot%2BActivity%2Bfor%2BMay%2B2023/29932/#comments)

* [previous](/diary/29930)
* [next](/diary/29936)

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