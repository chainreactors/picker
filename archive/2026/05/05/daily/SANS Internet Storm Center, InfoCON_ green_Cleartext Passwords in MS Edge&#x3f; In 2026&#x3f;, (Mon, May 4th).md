---
title: Cleartext Passwords in MS Edge&#x3f; In 2026&#x3f;, (Mon, May 4th)
url: https://isc.sans.edu/diary/rss/32954
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-05
fetch_date: 2026-05-06T05:09:39.970502
---

# Cleartext Passwords in MS Edge&#x3f; In 2026&#x3f;, (Mon, May 4th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Rob VandenBrink](/handler_list.html#rob-vandenbrink "Rob VandenBrink")

Threat Level: [green](/infocon.html)

* [previous](/diary/32950)
* [next](/diary/32956)

Click HERE to learn more about classes Rob is teaching for SANS

# [Cleartext Passwords in MS Edge? In 2026?](/forums/diary/Cleartext%2BPasswords%2Bin%2BMS%2BEdge%2BIn%2B2026/32954/)

**Published**: 2026-05-04. **Last Updated**: 2026-05-05 14:37:01 UTC
**by** [Rob VandenBrink](/handler_list.html#rob-vandenbrink) (Version: 1)

[0 comment(s)](/diary/Cleartext%2BPasswords%2Bin%2BMS%2BEdge%2BIn%2B2026/32954/#comments)

Yup, that is for real.

For me, this started with a post in X at hxxps://x.com/intcyberdigest/status/2051406295828250963?s=61 , which highlighted research by [@L1v1ng0ffTh3L4N](https://x.com/L1v1ng0ffTh3L4N) that found exactly this issue.  Edge stores all of your browser passwords in clear text, even if you haven't used them in this session, y'know, just in case.

I figured, it couldn't be that easy, right?  But like so many things, yes, yes it was.

To reproduce this

* Open Edge.  Don't browse anywhere, just open it
* Flip out to Task Manager, search for Edge, then expand that task
* Highlight the "browser" sub-task, right click, and choose "Create Memory Dump"

![](https://isc.sans.edu/diaryimages/images/dump_mem_from_process.png)

Navigate to where the DMP file is stored.

If you haven't used strings before, you're in for a treat.  Strings is of course just part of most Linux distros, but you can easily get a copy for Windows as part of MS Sysinternals, at https://learn.microsoft.com/en-us/sysinternals/downloads/strings

Now let's look for passwords!  You could use strings and look for known credentials, just search for a known password and you will certainly find it.  Or you can take advantage of the format of the saved data:

<url of the site><protocol>< ><userid>< >password>

So, searching for "<tld><protocol>", which in most cases is "comhttps" (no spaces) will find most of them, and they'll all be in one nicely formatted group no less.  The command for that will be:

strings -n 8 msedge.DMP | find "comhttps"

looking a bit down in the output (since comhttps does match more stuff in the memory dump than just the credential list), I see:

![](https://isc.sans.edu/diaryimages/images/password_dump.png)

As you can see, Edge isn't  my primary browser, but I do use it a fair bit for Azure work.  And yes, this is a real session, so I cropped/blurred out sensitive accounts and of course passwords.

It really is that easy.

And the ironic thing?  To view these same credentials in the browser, there's a whole security theatre process where Edge wants your biometrics as proof before disclosing even the userid and site names - you know, "for security".  All the while, the whole shot is in clear text, free for the looking ..

Also as noted in the X post, Microsoft classifies this as "intended behaviour".  I'm not sure what manager or lawyer decided that, hopefully it wasn't anyone in their security team.

Anyway, if the intent of this is to get me to use Firefox or Chrome, it's working!!

Have you seen a similar "strong front door / open window" security example in your forensics, please share in the comments (keeping any NDA's etc in mind of course)

=================

**Update:**

Tom Jøran Sønstebyseter Rønning (@L1v1ng0ffTh3L4N) just posted with more detail on his research at: x.com/l1v1ng0ffth3l4n/status/2051308329880719730  (follow the comment thread for all the info)

The main thrust of it remains the same.  The logged in Windows user can dump all of their stored Edge credentials with no additional rights.  Which means that the malware that user executes also has those credentials for the asking

===============
Rob VandenBrink
[[email protected]](/cdn-cgi/l/email-protection)

Keywords: [browser](/tag.html?tag=browser) [credential harvesting](/tag.html?tag=credential harvesting) [Microsoft](/tag.html?tag=Microsoft) [password](/tag.html?tag=password)

[0 comment(s)](/diary/Cleartext%2BPasswords%2Bin%2BMS%2BEdge%2BIn%2B2026/32954/#comments)

Click HERE to learn more about classes Rob is teaching for SANS

* [previous](/diary/32950)
* [next](/diary/32956)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)