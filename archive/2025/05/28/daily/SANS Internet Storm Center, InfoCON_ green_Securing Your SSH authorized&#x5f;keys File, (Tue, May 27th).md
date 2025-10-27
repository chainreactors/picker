---
title: Securing Your SSH authorized&#x5f;keys File, (Tue, May 27th)
url: https://isc.sans.edu/diary/rss/31986
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-28
fetch_date: 2025-10-06T22:29:15.778327
---

# Securing Your SSH authorized&#x5f;keys File, (Tue, May 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31980)
* [next](/diary/31990)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

# [Securing Your SSH authorized\_keys File](/forums/diary/Securing%2BYour%2BSSH%2Bauthorizedkeys%2BFile/31986/)

**Published**: 2025-05-27. **Last Updated**: 2025-05-27 15:44:43 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Securing%2BYour%2BSSH%2Bauthorizedkeys%2BFile/31986/#comments)

This is nothing "amazingly new", but more of a reminder to secure your "authorized\_keys" file for SSH. One of the first things I see even simple bots do to obtain persistent access to a UNIX system is to add a key to the authorized\_keys file of whatever account they are compromising.

So here are a few things you can do to make your "authorized\_keys" file more secure:

### authorized\_keys file location

The default location is .ssh/authorized\_keys and .ssh/authorized\_keys2. Make sure to specify a location (default is fine, but more later). One file is fine. the "authorized\_keys2" file was used back in the day to retain backward compatibility with older SSH versions. Most importantly, you want to control the location of the file, and for the later discussion, we are going to assume the default location.

### File Permissions

This is probably the easiest change you can make. By default, most systems set the permissions to "0600" and make the file owned by the user. This looks "ok" at first as only the user has read/write access. But in this case, we try to prevent someone who compromised the user's credentials from modifying the file. A better option is to make sure the file is owned by the root and set to read-only (0444). The user must still be able to read the file, so 0400 will not work if the file is owned by root. Next, you may also set the "immutable" flag. It does not offer a ton of extra security, as the attacker has to be root anyway, but it offers some more detection capabilities.

### Central Management

Even small "IoT" style systems can often be managed with tools like Ansible. This opens up more possibilities to better manage authorized\_keys files. First of all, you do not have to store the key files in the user's home directory. You could set up a central location for all the key files. Something like /etc/ssh/authorized\_keys. In this directory, you may not maintain individual files for each user. The sshd configuration file accepts "tokens" as part of the filename. You now use

AuthorizedKeysFile /etc/ssh/authorized\_keys/%U

The token "%U" is replaced with the numeric userid. Or you can use "%u" for the username (this may be easier to keep consistent across different systems).

There is also the possibility to use a command to retrieve the key on demand using the "AuthorizedKeysCommand". This way, the keys are not exposed on the system, but personally I am a bit afraid of any denial of service issues with this setup. But there are a lot of options to further secure SSH keys by, for example, constantly rotating them or integrating them with other centrally managed access systems.

### File Monitoring

Changes to authorized\_keys files should be monitored using systems like Aide, Wazuh/OSSEC, or Tripwire. This may not always be an option on minimum Linux systems (IoT). Some homegrown solutions may work well enough in these cases (Ansible could easily alert you of changes). Do not allow "perfect" to get in the way of "good enough".

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [authorizedkeys](/tag.html?tag=authorizedkeys) [ssh](/tag.html?tag=ssh)

[0 comment(s)](/diary/Securing%2BYour%2BSSH%2Bauthorizedkeys%2BFile/31986/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/dallas-2025/course/application-security-securing-web-apps-api-microservices) | Dallas | Dec 1st - Dec 6th 2025 |

* [previous](/diary/31980)
* [next](/diary/31990)

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