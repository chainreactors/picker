---
title: The Top 10 Not So Common SSH Usernames and Passwords, (Wed, Oct 16th)
url: https://isc.sans.edu/diary/rss/31360
source: SANS Internet Storm Center, InfoCON: green
date: 2024-10-17
fetch_date: 2025-10-06T18:59:21.379694
---

# The Top 10 Not So Common SSH Usernames and Passwords, (Wed, Oct 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31356)
* [next](/diary/31362)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [The Top 10 Not So Common SSH Usernames and Passwords](/forums/diary/The%2BTop%2B10%2BNot%2BSo%2BCommon%2BSSH%2BUsernames%2Band%2BPasswords/31360/)

**Published**: 2024-10-16. **Last Updated**: 2024-10-16 17:26:49 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/The%2BTop%2B10%2BNot%2BSo%2BCommon%2BSSH%2BUsernames%2Band%2BPasswords/31360/#comments)

Our list of "Top" ssh usernames and password is pretty static. Well known defaults, like "root" and "admin" are at the top of the list. But there are always some usernames and password in the list that are not as well known, or only showed up more recently. I will focus in this diary on these "second tier" credentials.

**345gs5662d34**

Used by Polycom CX600 IP phones, this password often shows up in the username field (as other passwords do) if sloppy bots do enter it into the wrong field.

**zyfwp**

A backdoor account in Zyxel equipment. It was found by Rapid 7 (and later removed by Zyxel) in 2020.

**yhtcAdmin**

Used in "Youhua PT939G" fiber routers.

**vadmin**

The default username for the web hosting platform LiteSpeed. Can be used via SSH or HTTP.

**telecomadmin**

The username used by Huawei ONT HG8245H5 fiber termination kit.

**chenzilong**

Not sure. But it may be a popular Chinese character. Maybe anybody reading this knows?

**7ujMko0admin**

Some Dahua network NVRs use this telnet/ssh password. They are pretending the string "7ujMko0" to the web password, which by default is "admin".

**a1sev5y7c39k**

The default password for some unspecified routers using the Realtek chipset.

**Xpon@Olt9417#**

V\*SOL GPON OLT default password

**ve0RbANG**

used with the "YhtcAdmin" username for Youhua PT939G optical network termination equipment. The same device also uses Admin/1234 and Admin/Telecom\_1234. .

You can look at our top password list here:

<https://isc.sans.edu/data/ssh.html>

I will add some of the details about our username and password pages as you look up a particular password. For example:

<https://isc.sans.edu/ssh_usernames.html?username=345gs5662d34>

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [password](/tag.html?tag=password) [ssh](/tag.html?tag=ssh) [telnet](/tag.html?tag=telnet) [username](/tag.html?tag=username)

[1 comment(s)](/diary/The%2BTop%2B10%2BNot%2BSo%2BCommon%2BSSH%2BUsernames%2Band%2BPasswords/31360/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31356)
* [next](/diary/31362)

### Comments

Do you have a list of top 1000 passwords? I need it to comply with https://csf.tools/reference/nist-sp-800-53/r5/ia/ia-5/ia-5-1/ points a and b.

I'm currently using https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000.txt

That list was last updated 6 years ago. I know there isn't much movement in the top most common passwords, but my control states I'm supposed to update my list.

#### Egamma

#### Oct 17th 2024 11 months ago

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