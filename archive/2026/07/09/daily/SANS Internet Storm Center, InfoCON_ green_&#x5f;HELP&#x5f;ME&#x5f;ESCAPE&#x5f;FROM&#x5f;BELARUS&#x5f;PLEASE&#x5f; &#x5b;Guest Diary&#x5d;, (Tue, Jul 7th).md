---
title: &#x5f;HELP&#x5f;ME&#x5f;ESCAPE&#x5f;FROM&#x5f;BELARUS&#x5f;PLEASE&#x5f; &#x5b;Guest Diary&#x5d;, (Tue, Jul 7th)
url: https://isc.sans.edu/diary/rss/33130
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-09
fetch_date: 2026-07-10T06:00:00.069272
---

# &#x5f;HELP&#x5f;ME&#x5f;ESCAPE&#x5f;FROM&#x5f;BELARUS&#x5f;PLEASE&#x5f; &#x5b;Guest Diary&#x5d;, (Tue, Jul 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/33128)
* [next](/diary/33138)

Click HERE to learn more about classes Guy is teaching for SANS

# [\_HELP\_ME\_ESCAPE\_FROM\_BELARUS\_PLEASE\_ [Guest Diary]](/forums/diary/HELPMEESCAPEFROMBELARUSPLEASE%2BGuest%2BDiary/33130/)

**Published**: 2026-07-07. **Last Updated**: 2026-07-09 01:20:02 UTC
**by** [Jason Callahan, SANS.edu BACS Student](/handler_list.html#jason-callahan,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/HELPMEESCAPEFROMBELARUSPLEASE%2BGuest%2BDiary/33130/#comments)

[This is a Guest Diary by Jason Callahan, an ISC intern as part of the [SANS.edu](https://www.sans.edu/cyber-security-programs/bachelors-degree/) BACS program]

Every so often a honeypot hit comes along that is less about the exploit and more about the intent behind it. While reviewing DShield logs I ran into a scanning bot that caught my eye: a URI string that appeared to be a plea for help.

On 2026-06-06 my DShield honeypot logged back-to-back HTTP requests from the same source IP hitting two different ports with both carrying an identical, oddly formatted request path:

![](https://isc.sans.edu/diaryimages/images/Jason_Callahan_pic1(1).png)

The request path itself /?\_HELP\_ME\_ESCAPE\_FROM\_BELARUS\_PLEASE\_ is not a known exploit path, it appeared to be a plain-text message in the URL. Searching my logs for that particular string returned around a dozen similar HTTP requests over a 2 months period. These came from various IPs from around the globe with no discernible pattern which pointed to a self-propagating bot rather than a single attacker.

Further research showed that this bot was first reported to ISC in May 2026. The number of reports peaked shortly after the first report before a sharp drop and has remained steady since. [[1](https://isc.sans.edu/weblogs/urlhistory.html?url=Lz9fSEVMUF9NRV9FU0NBUEVfRlJPTV9CRUxBUlVTX1BMRUFTRV8=)]

![](https://isc.sans.edu/diaryimages/images/Jason_Callahan_pic2.png)

I was unable to locate much more information about this bot other than a reddit thread on [r/selfhosted](https://www.reddit.com/r/selfhosted/comments/1tbrkcv/found_some_strange_get_requests_in_my_traefik/) describing the same requests hitting a Traefik reverse proxy. According to that thread, the user emailed the address embedded in the User-Agent and received a reply pointing to a page on a free web-hosting service. The page is a static HTML document with no scripts and it lays out what the bot is & why it exists.

The author, who identifies himself only as “Alex,” claims to be based in Belarus and writes that the bot is intentionally limited: no exploits, no command-and-control, no persistence. In his words, paraphrased and summarized from the page:

• The bot scans random IP addresses for open HTTP ports (80, 8000, 8080) and SSH ports (22, 2222).
• If it finds an open HTTP port it sends a single request (GET, CONNECT, or HEAD)
• If it finds an open SSH port it attempts a brute force with a small, fixed list of default credential pairs (admin:admin, root:root, etc.)
• It runs fully autonomously with no C2 channel; discovered IP/credential pairs are reported back to a loader only.
• It does not establish persistence, typically running from /tmp, and it is designed to self-terminate roughly six months after release.
• The stated purpose is to draw attention to conditions in Belarus. They describe it as a “performance piece,” saying they are not seeking funding and only asking for non-financial help leaving the country (job leads, advice, connections).

Disregarding the origin and supposed intent of the bot, this is a straightforward scan-and-brute-force bot and it should be treated like any other hitting a honeypot. The HTTP request is reconnaissance/fingerprinting that tells the operator a host is alive and reachable on that port. The risk is on the SSH side: any host reachable on TCP 22/2222 that still uses a default or weak credential pair is exposed, regardless of the creator’s stated intentions.

I want to give some healthy skepticism here rather than take the linked page at face value. I have no way to verify the age, location, or motive claimed on that page, whether the page itself is the full extent of the bot's behavior, or whether the “self-terminate after six months” and “no persistence” claims hold up under closer reverse engineering. Sob stories and appeals to sympathy are also a known social-engineering lever, and a URI designed to make analysts pause and read a web page rather than immediately blocklist an IP is an effective way to buy a scanner some goodwill. None of that changes the defensive posture: treat it as an untrusted, credential-guessing scanner.

[1] https://isc.sans.edu/weblogs/urlhistory.html?url=Lz9fSEVMUF9NRV9FU0NBUEVfRlJPTV9CRUxBUlVTX1BMRUFTRV8=
[2] https://isc.sans.edu/honeypot.html
[3] https://www.sans.edu/cyber-security-programs/bachelors-degree/

Disclosure: Claude was used for grammar and polish checks. No further use of generative A.I. was used in the creation of this post.

-----------
Guy Bruneau [IPSS Inc.](http://www.ipss.ca/)
[My GitHub Page](https://github.com/bruneaug/)
Twitter: [GuyBruneau](https://twitter.com/guybruneau)
gbruneau at isc dot sans dot edu

Keywords: [Analysis](/tag.html?tag=Analysis) [DShield sensor](/tag.html?tag=DShield sensor) [Research](/tag.html?tag=Research) [Webhoneypot](/tag.html?tag=Webhoneypot)

[0 comment(s)](/diary/HELPMEESCAPEFROMBELARUSPLEASE%2BGuest%2BDiary/33130/#comments)

Click HERE to learn more about classes Guy is teaching for SANS

* [previous](/diary/33128)
* [next](/diary/33138)

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