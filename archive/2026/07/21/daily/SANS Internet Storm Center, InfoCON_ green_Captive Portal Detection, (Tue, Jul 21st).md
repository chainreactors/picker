---
title: Captive Portal Detection, (Tue, Jul 21st)
url: https://isc.sans.edu/diary/rss/33172
source: SANS Internet Storm Center, InfoCON: green
date: 2026-07-21
fetch_date: 2026-07-22T05:04:22.411666
---

# Captive Portal Detection, (Tue, Jul 21st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/33168)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

# [Captive Portal Detection](/forums/diary/Captive%2BPortal%2BDetection/33172/)

**Published**: 2026-07-21. **Last Updated**: 2026-07-21 13:44:56 UTC
**by** [Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author) (Version: 1)

[1 comment(s)](/diary/Captive%2BPortal%2BDetection/33172/#comments)

Not everything our honeypots detect is an attack. Sometimes it is just "odd traffic", and this is one example: Our "First Seen" list currently includes "http://detectportal.firefox.co
m/success.txt" as one of the new URLs detected by our honeypots. The hostname "detectportal" kind of gives away what is happening here.

If you have ever tried to connect to a public WiFi network, you probably ran into some type of "captive portal". A splash screen that will ask you to acknowledge some kind of user agreement or require you to log in. Of course, each implementation looks a bit different, and browsers and operating systems attempt to detect these captive portals. Typically, the operating system will automatically direct you to the correct portal page.

It used to be easier to deal with captive portals. Back in the "old days" (not necessarily "good old days"), users often had a non-TLS page configured as their homepage. The captive portal was able to intercept this connection and direct the user to the captive portal's login page. These days, however, most websites use TLS, and browsers default to TLS for many sites and refuse to switch to a non-TLS site. This made using WiFi networks a lot safer, but it gets in the way of directing users to a captive portal.

In response, operating systems and browsers implemented features to detect captive portals. The system will attempt to pull up a specific http URL to detect if it receives a redirect response. If so, it will open the redirect URL in a browser. You will see these URLs as systems join your network, or if the browser is started. The URL does provide some intelligence as to what operating system or browser is being used. Here is a quick summary of what URLs different operating systems use:

Windows: http://www.msftconnecttest.com/connecttest.txt . This is part of the Windows Network Connectivity Status Indicator, which was introduced in Windows 8. Windows 10 and later will attempt to access the URL and check for a valid response. The response should be "Microsoft Connect Test". In addition, it will do a DNS lookup for dns.msftncsi.com. [1]

Apple: Recent versions of MacOS and iOS use http://captive.apple.com/hotspot-detect.html as a test. The expected response is "Success". If the system can not connect, Apple's Captive Network Assistant starts to assist the user in logging in.

Android: http://connectivitycheck.android.com/generate\_204. The result page is empty, and uses a status code of 204 (No Content).

Chrome: http://www.gstatic.com/generate\_204. Slightly different URL than Chrome, but works the same way expecting a "204 No Content" response. Chromium implements the same system with http://clients3.google.com/generate\_204 [3]

Firefox: http://detectportal.firefox.com/canonical.html. This page returns a 200 status code. The body of the page includes a META tag to redirect users to a page explaining how Firefox deals with captive portals (I like this.. as an analyst, it is neat to have the page explain what it does) [4]

All these URLs use HTTP so the captive portal can redirect the request. This is necessary for the client to discover the captive portals' "splash screen". If you are ever "stuck" and can't find the captive portal for a network, opening any of the URLs above in your browser may redirect you to the sign-in page.

[1] https://learn.microsoft.com/en-us/troubleshoot/windows-client/networking/internet-explorer-edge-open-connect-corporate-public-network#ncsi-active-probes-and-the-network-status-alert

[2] https://grpugh.wordpress.com/2014/10/29/an-undocumented-change-to-captive-network-assistant-settings-in-os-x-10-10-yosemite/

[3] https://www.chromium.org/chromium-os/chromiumos-design-docs/network-portal-detection/

[4] https://support.mozilla.org/en-US/kb/captive-portal

--
Johannes B. Ullrich, Ph.D. , Dean of Research, [SANS.edu](https://sans.edu)
[Twitter](https://jbu.me/164)|

Keywords: [captive portal](/tag.html?tag=captive portal) [wifi](/tag.html?tag=wifi)

[1 comment(s)](/diary/Captive%2BPortal%2BDetection/33172/#comments)

Click [HERE](https://www.sans.org/profiles/dr-johannes-ullrich) to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33168)

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