---
title: SANS ISC Internship Setup: AWS DShield Sensor &#x2b; DShield SIEM &#x5b;Guest Diary&#x5d;, (Tue, Nov 26th)
url: https://isc.sans.edu/diary/rss/31480
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-29
fetch_date: 2025-10-06T19:19:17.327922
---

# SANS ISC Internship Setup: AWS DShield Sensor &#x2b; DShield SIEM &#x5b;Guest Diary&#x5d;, (Tue, Nov 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31476)
* [next](/diary/31484)

# [SANS ISC Internship Setup: AWS DShield Sensor + DShield SIEM [Guest Diary]](/forums/diary/SANS%2BISC%2BInternship%2BSetup%2BAWS%2BDShield%2BSensor%2BDShield%2BSIEM%2BGuest%2BDiary/31480/)

**Published**: 2024-11-26. **Last Updated**: 2024-11-28 01:52:48 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/SANS%2BISC%2BInternship%2BSetup%2BAWS%2BDShield%2BSensor%2BDShield%2BSIEM%2BGuest%2BDiary/31480/#comments)

[This is a Guest Diary by John Paul Zaguirre , an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

**Introduction**

This is a blog post documentation on how to set up the DShield Sensor in AWS, DShield SIEM locally, and connecting them both. I initially setup a Raspberry Pi5 to use as a DShield Sensor, but ultimately switched to AWS after a while. I then added a DShield SIEM hosted locally on my network and connected the AWS sensor into it to utilize for my attack observations. This walkthrough is based on multiple documentations that have been compiled into one, and I have linked their GitHub pages under the “References and Resources” section. You can find the full walkthrough on this page – <https://github.com/15HzMonitor/Internship-Blog-Post>

**Requirements - Hardware, Software, and Accounts**

**Hardware**
1.    A machine to host your DShield SIEM. This can be a laptop, a desktop, or a virtual machine running on your desktop. If you're planning to run the SIEM 24/7, I suggest using something different than your daily production machine. In my case, I reused an old desktop to use as my SIEM so that it can run 24/7. Below are the minimum specs required to run the SIEM based on Guy's documentation for the Ubuntu Setup [[1](https://github.com/bruneaug/DShield-SIEM#ubuntu-setup)]:
    o    Minimum 8+ GB RAM
        -    If the amount of RAM assigned to each container (see below) is more than 2GB, consider increasing the server RAM capacity.
    o    4-8 Cores
    o    Add 2 partitions, one for the OS, the other for docker
    o    Minimum 300 GB partition assigned to /var/lib/docker (I used a 1TB SATA drive)
2.    USB flash drive(s) to put your Ubuntu ISO to be installed to your repurposed machine. Have at least 16GB, and it must be clear of any data since you will be using Rufus, and it will format the USB stick when creating a boot drive.

**Software**
1.    Ubuntu 22.04 LTS Live Server 64-bit for your DShield SIEM. You can download the ISO on the Ubuntu Server Page [[2](https://ubuntu.com/download/server)].
2.    Rufus Software to put your Ubuntu ISO into a bootable USB. You can find the latest Rufus version on the Rufus downloads page [[3](https://rufus.ie/downloads/)].
3.    (Optional) a software such as Parted Magic or DBAN to wipe the machine you will be using.
4.    Your router's software to create a static IP for your SIEM and do port forwarding.

**Accounts**
1.    A SANS Internet Storm Center (ISC) Account for your API key to enter in your sensor. You can sign up on the ISC sign up page [[4](https://isc.sans.edu/register.html)].
2.    An AWS Account to deploy your DShield Sensor using the Free Tier offer.
If you don't have one yet, you can sign up on the AWS sign up page [[5](https://signin.aws.amazon.com/signup?request_type=register)].
3.    An AlienVault OTX account for generating the API code to link to your DShield SIEM. You can sign up on the AlienVault OTX sign up page [[6](https://otx.alienvault.com/)].

**Setup Process**

1. **Setup your DShield Sensor.**

1. Sign up for an AWS Account.
2. Setup EC2 Instance
3. Install & setup DShield Sensor
4. Configure EC2 Security

2. **Setup your DShield SIEM.**

1. Install Ubuntu Server to a physical machine.
2. (Option) Install Ubuntu Server virtually through VMWare.
3. Build a Docker Partition.
4. Install Docker.
5. Install and Configure DShield ELK.
   * An optional setup for using Raspberry Pi as a SIEM has been written by another SANS Student and can be found on their GitHub page [[7](http://Installing DShield SIEM on a Raspberry Pi 5 - 8 GB RAM)].

3. **Configure Filebeat and connect your DShield Sensor to DShield SIEM.**

1. Install and configure Filebeat on your DShield sensor and connect it to your ELK.
2. Troubleshoot and test Filebeat.
3. Start Filebeat, Elastic-agent, and Softflowd.
4. Check the status of Filebeat, Elastic-agent, and Softflowd.
5. Accessing your dashboards and logs.

4. **Harden your DShield SIEM.**

1. Adding non-root user(s), Install updates, Unattended upgrades, Locking down OpenSSH, Fail2ban.
2. 10 Tips for Hardening your Linux Servers.

[1] https://github.com/bruneaug/DShield-SIEM#ubuntu-setup
[2] https://ubuntu.com/download/server
[3] https://rufus.ie/downloads/
[4] https://isc.sans.edu/register.html
[5] https://signin.aws.amazon.com/signup?request\_type=register
[6] https://otx.alienvault.com/
[7] Installing DShield SIEM on a Raspberry Pi 5 - 8 GB RAM
[8] https://www.sans.edu/cyber-security-programs/bachelors-degree/

Special thanks to the writers of these GitHub documents:

[dshield: DShield Raspberry Pi Sensor](https://github.com/DShield-ISC/dshield)
I[nstalling DShield SIEM on a Raspberry Pi 5 - 8 GB RAM](https://github.com/amelete11235/homelab/blob/main/Installing%20DShield%20SIEM%20on%20a%20Raspberry%20Pi%205%20-%208%20GB%20RAM/Installing%20DShield%20SIEM%20on%20a%20Raspberry%20Pi%205%20-%208%20GB%20RAM.md)
[DShield-SIEM: DShield Sensor Log Collection with ELK](https://github.com/bruneaug/DShield-SIEM/tree/main)
[Dshield-ELK](https://github.com/fkadriver/Dshield-ELK)

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My Handler Page](https://handlers.sans.org/gbruneau/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [AWS](/tag.html?tag=AWS) [BACS](/tag.html?tag=BACS) [DShield](/tag.html?tag=DShield) [DShield Sensor](/tag.html?tag=DShield Sensor) [ELK](/tag.html?tag=ELK)

[0 comment(s)](/diary/SANS%2BISC%2BInternship%2BSetup%2BAWS%2BDShield%2BSensor%2BDShield%2BSIEM%2BGuest%2BDiary/31480/#comments)

* [previous](/diary/31476)
* [next](/diary/31484)

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
* [Pr...