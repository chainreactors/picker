---
title: Scanning s3 buckets, (Mon, Mar 6th)
url: https://isc.sans.edu/diary/rss/29606
source: SANS Internet Storm Center, InfoCON: green
date: 2023-03-07
fetch_date: 2025-10-04T08:51:37.352320
---

# Scanning s3 buckets, (Mon, Mar 6th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29598)
* [next](/diary/29610)

# [Scanning s3 buckets](/forums/diary/Scanning%2Bs3%2Bbuckets/29606/)

**Published**: 2023-03-06. **Last Updated**: 2023-03-08 01:51:57 UTC
**by** [Manuel Humberto Santander Pelaez](/handler_list.html#manuel-humberto-santander-pelaez) (Version: 1)

[0 comment(s)](/diary/Scanning%2Bs3%2Bbuckets/29606/#comments)

We frequently see news of information leaks that occur in different companies due to having information in the cloud with the wrong permissions, allowing anyone access to potentially confidential information.

Why do people remove restrictions and allow a bucket to be public? Regardless of its intention, on many occasions it corresponds to inappropriate devops practices where objects are created from development without security measures and make their transition to production in the same way.

In this diary we will look at how to scan S3 buckets on AWS with incorrect public access permissions. For this we will use the s3scanner tool, which you can get from https://github.com/sa7mon/S3Scanner It requires the creation of a file containing the names of all buckets to be enumerated. For this case, I proceeded to create a bucket with a hackable name and it will be the only name that contains the file:

![](https://isc.sans.edu/diaryimages/images/bucketnames.png)

After this, we proceed with the execution of the tool. It is important to note that we are doing an enumeration exercise that does not involve configuring AWS credentials, which is why we will get a warning that still does not interfere with the result we seek to obtain:

![](https://isc.sans.edu/diaryimages/images/bucketscan2.png)

Let's see what files are present using AWS Cli:

![](https://isc.sans.edu/diaryimages/images/awsbucket2.png)

And, of course, AWS console shows a mayor warning as publicly accesible with this bucket:

![](https://isc.sans.edu/diaryimages/images/warnings3.png)

Changing permissions on cloud artifacts can easily go unnoticed. To manage problems like these, it is necessary to have a control that performs the automated review of the security posture in the cloud, in such a way that it alerts when this kind of permission change occurs and thus the corresponding actions can be taken. We will review this in a future diary.

**Manuel Humberto Santander Peláez**
**SANS Internet Storm Center - Handler**
**Twitter:** [@manuelsantander](https://twitter.com/manuelsantander)
**Mastodon:**[[email protected]](https://infosec.exchange/%40manuelsantander)
**email:**[[email protected]](/cdn-cgi/l/email-protection#e9849a88879d88878da9809a8ac79a88879ac7869b8e)

Keywords:

[0 comment(s)](/diary/Scanning%2Bs3%2Bbuckets/29606/#comments)

* [previous](/diary/29598)
* [next](/diary/29610)

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