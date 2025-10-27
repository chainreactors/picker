---
title: Prowler v3: AWS &#x26; Azure security assessments, (Thu, Jan 12th)
url: https://isc.sans.edu/diary/rss/29430
source: SANS Internet Storm Center, InfoCON: green
date: 2023-01-13
fetch_date: 2025-10-04T03:46:39.719290
---

# Prowler v3: AWS &#x26; Azure security assessments, (Thu, Jan 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29426)
* [next](/diary/29434)

# [Prowler v3: AWS & Azure security assessments](/forums/diary/Prowler%2Bv3%2BAWS%2BAzure%2Bsecurity%2Bassessments/29430/)

**Published**: 2023-01-12. **Last Updated**: 2023-01-12 08:52:45 UTC
**by** [Russ McRee](/handler_list.html#russ-mcree) (Version: 1)

[2 comment(s)](/diary/Prowler%2Bv3%2BAWS%2BAzure%2Bsecurity%2Bassessments/29430/#comments)

As a current Google Cloud Platform defender, and former Microsoft Azure defender, I appreciate any tool or capability intended to provide multi-cloud protection. As noted via LinkedIn, [Toni](https://www.linkedin.com/posts/toniblyx_prowler-v3-piece-of-mind-activity-7011369522175598593-n1UA) announced the release of [Prowler v3](https://github.com/prowler-cloud/prowler) just before Christmas. Prowler v3 is a complete overhaul of Prowler, fully rewritten it in Python. **[Prowler](https://docs.prowler.cloud/en/latest/) is an open source security tool to perform AWS and Azure security best practices assessments, audits, incident response, continuous monitoring, hardening and forensics readiness.** Prowler v3 is now multi-cloud with Azure added as the second supported cloud provider. Prowler is significantly faster as well, now able to scan an entire AWS account across all regions 37 times faster than before.
Prowler v3 change log:

* **Python:** No more bash, now all in Python. 'pip install prowler-cloud' then run 'prowler'
* **Performance improvements:** an account that took 2.5 hours to scan in v2 now only takes 4 minutes to scan in v3
* **Developers and Community:** easier to contribute with new checks and new compliance frameworks, as well as unit tests and native logging features
* **Multi-cloud:** Currently AWS and Azure, the team plans to include GCP and OCI soon and would appreciate contributors
* **Checks and Groups:** all checks are now more comprehensive and we provide resolution actions in most of them
* **Compliance:** full support for CIS 1.4, CIS 1.5 and the new Spanish ENS in this release, more to come soon!
* **Consolidated output formats:** now both CSV and JSON reports come with the same attributes. HTML, CSV and JSON are created every time you run `prowler`
* **Quick Inventory:** fine tuned the Quick Inventory feature to get a list of all resources in your AWS accounts within seconds
* **Document site:** https://docs.prowler.cloud

To test Prowler, I installed, configured, and ran it against my AWS account with ease from my Mac mini running Python 3.9.12, as follows:

* pip install prowler-cloud
* prowler -v to confirm success and installed version
* ulimit -n 1000 to avoid [file descriptor](https://docs.prowler.cloud/en/latest/troubleshooting/) limits, macOS Ventura's default value for file descriptors is 256
* aws configure to use AWS IAM security credentials properly. This requires  AWS CLI, which, if you did the [2022 SANS Holiday Hack Challenge](https://2022.kringlecon.com/) over the holidays, you should be quite familiar with. Yes, I recovered the Cloud Ring ;-)
  + ![](https://isc.sans.edu/diaryimages/images/CloudRing.png)
* prowler aws

Results are produced in CSV, HTML, and JSON, as well as a results table to the terminal. As you can see below, my results are terrible, and I have some attention to pay to my rarely used AWS account, current billing = .87 cents a month ;-).

![Prowler](https://isc.sans.edu/diaryimages/images/Prowler.png)

May I be the first to recommend you read all the Prowler resources, and immediately audit accounts and subscriptions in your care. I have in, my many years of cloud defense, seen the worst of the worst in cloud compromise, customer runaway spend, and cloud abuse, often the result of easily prevented misconfigurations and weak permissions. Go do! I look forward to the GCP version.

Cheers…until next time.

[Russ McRee](https://holisticinfosec.io/) | [@holisticinfosec](http://twitter.com/holisticinfosec) | [infosec.exchange/@holisticinfosec](https://infosec.exchange/%40holisticinfosec) | [LinkedIn.com/in/russmcree](https://www.linkedin.com/in/russmcree/)

Keywords: [cloud](/tag.html?tag=cloud) [Prowler](/tag.html?tag=Prowler) [Azure](/tag.html?tag=Azure) [AWS](/tag.html?tag=AWS) [GCP](/tag.html?tag=GCP) [OCI](/tag.html?tag=OCI)

[2 comment(s)](/diary/Prowler%2Bv3%2BAWS%2BAzure%2Bsecurity%2Bassessments/29430/#comments)

* [previous](/diary/29426)
* [next](/diary/29434)

### Comments

Thanks for posting this, @Russ

I'm finding that the Azure support is not nearly as mature as the AWS feature set.
Is that what you find too?

I'm not sure what this gets me in the Azure space that's better than the Azure Security Center, HAWK [ https://github.com/T0pCyber/hawk ], Sparrow [ https://github.com/cisagov/Sparrow ], or the CRT [ https://github.com/CrowdStrike/CRT ].

What am I missing?

#### MrCarney

#### Jan 17th 2023 2 years ago

Sorry for the long delay, MrCarney. Concur and agreed, less than optimal for Azure as of my testing. Hopefully future improvements may achieve parity.

#### Russ McRee

#### May 6th 2023 2 years ago

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