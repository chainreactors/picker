---
title: New OS Telemetry Guide
url: https://inteltechniques.com/blog/index.html#telemetry-guide-content
source: IntelTechniques by Michael Bazzell
date: 2026-08-18
fetch_date: 2026-08-19T02:57:31.518872
---

# New OS Telemetry Guide

[# IntelTechniques](../index.html)

* [Training](../training.html)
* [Services](../services.html)
* [Resources](../links.html)
* [Tools](../tools/index.html)
* [Blog](../blog/)
* [Magazine](https://unredactedmagazine.com)
* [Books](../books.html)
* [Contact](../contact.html)

#### IntelTechniques Blog

---

## New OS Telemetry Guide

August 18, 2026

+

In [Extreme Privacy, 5th Edition](https://inteltechniques.com/book7) I explained how I use a software firewall to prevent my computers from sending out details about my usage to the companies which create the applications and operating systems powering them. In [Issue 011 of UNREDACTED Magazine](https://payhip.com/b/6teIq), I explained how the Apple operating system now bypasses the software firewall to send data about your actions back to their servers without any notification. This generated a lot of feedback. Some wanted to know exactly what they should block for their own macOS machines while others wanted an updated list for Microsoft. Others were curious if this would apply to Windows virtual machines (yes, it does).

The purpose of this guide is to allow you to create a DNS filtering block list which can be used without a software firewall to prevent all telemetry from being sent to either Apple or Microsoft (or both if using a VM). You will need a free [NextDNS](https://nextdns.io/NextDNS) account and your host operating system must be using this specific account for it all to work, as explained in [Extreme Privacy, 5th Edition](https://inteltechniques.com/book7). Once you have that working, the following block lists block all telemetry by placing each option in the "denylist" within your NextDNS profile.

![](../img/nextdns.png)

#### Apple Block List

---

apple.com
icloud.com
itunes.com
apple-dns.net
apple.news
apple-relay.cloudflare.com
apple-relay.fastly-edge.com
cdn-apple.com
aaplimg.com
akadns.net
dsce9.akamaiedge.net
sentry.io
demdex.net
mgr.gcsp.cddbp.net
safebrowsing.googleapis.com
ohttp-relay1.fastly-edge.com

#### Microsoft Block List

---

microsoft.com
microsoft.net
windows.com
windowsupdate.com
bing.com
live.com
msedge.net
office.com
skype.com
msn.com
office.net
xboxservices.com
cloud.microsoft
msftconnecttest.com
msftncsi.com
nelreports.net
t.ssl.ak.dynamic.tiles.virtualearth.net
img-s-msn-com.akamaized.net
edge-consumer-static.azureedge.net
prod-video-cms-amp-microsoft-com.akamaized.net
sentry.io
demdex.net
safebrowsing.googleapis.com

Once these are applied and activated, your system can no longer send data about your usage back to the motherships. However, that also means your systems can no longer receive updates or scan files and programs for suspicious behavior. This can be a serious risk for those who need that protection. I would never recommend this for a non-tech-savvy user. I also insist that I disable the DNS filtering at least once a week to download and apply system updates. During this time, I have no other apps open and I re-apply the DNS filtering upon a reboot.

I believe macOS users should still use a software firewall such as Little Snitch or Lulu in order to block telemetry of software applications (unless you want to constantly modify your denylist in NextDNS with their domains). It is also vital to change your time server to a nuetral provider (not Apple or Microsoft), as explained in the book. This keeps your time synchronized without allowing Apple or Microsoft to suck up everything else about your usage.

**Overall, please do not apply any of this unless you understand the risks and benefits.**

#### Results

---

Within a few seconds of booting my Apple computer, the following is only a partial output of the connections being blocked. This was without opening a single application.

![](../img/apple.png)

Within a few seconds of booting my Windows computer, the following is only a partial output of the connections being blocked. Notice that a connection to Proton was allowed since it was not on the denylist. Also notice that a connection to Apple popped in because many people with Windows systems may also use Apple-related applications. There is no harm in applying both block lists to any computer. The unused domains won't harm anything.

![](../img/windows.png)

I want to say one last time that you should use caution when blocking system connections. In theory, it sounds great. You are preventing your host from snooping on you and documenting a lot about your activity, including your IP address, machine identifiers, accounts, programs you use, and when (and how) you use them. You are also preventing your system from protecting you. Only you can decide if you need their protection. If you have good digital hygiene, understand how cyber threats come into systems, and have the discipline to manually apply updates, you should be fine. If you are prone to viruses, this is not for you. Always understand how to reverse your DNS provider before making the switch. See [Extreme Privacy, 5th Edition](https://inteltechniques.com/book7) for more details.

## The New Blog

August 15, 2026

+

I have hosted a WordPress blog on this site for almost 20 years. I don't any more.

WordPress was great. Type what you want to say; click a few buttons; and poof, your post is available to the world while your RSS feed is auto generated. It was so easy. It also brought a lot of trouble.

Even though we self-hosted the blog, WordPress continued to add various tracking capabilities. We would remove them as they emerged, but tracking was still possible. We try to prevent us from knowing the IP addresses of our visitors whenever possible. This gives you more privacy and us deniability if we were to receive a court order for traffic. The feds were not knocking down our door, but we like to practice what we preach.

We use Cloudflare as our CDN and full caching prevented our web host from receiving the requests for pages. This eliminated both our host and us from seeing your specific traffic and IP address. However, searches on the blog would generate a direct hit to the host and bypass the protection. We disabled search but that did not stop all logging when an un-cached page was accessed.

My main beef with having WordPress on our site was the attacks. Thousands of bots brute-force and scrape WordPress installations looking for content and vulnerabilities. This can result in hundreds of thousands of page loads every day, sometimes millions. Our CDN stops some of it, but most gets by.

I also just don’t like having a large amount of code and a database on my site just to deliver text content and a few images. WordPress is very excessive for our needs. So we killed it. Doing this left us with an entire site existing of only HTML and JS. This allowed us to stop using our web host (Namecheap) and simply cache the static pages on a Cloudflare worker. The entire site is under 100 MB and our old host is no longer logging your activity. Cloudflare is now the only server which can see the data and traffic, and they do not share IP address or traffic logs with us, outside of temporary security logs when attacked. That is not to say THEY don't store the data, but they could do that as our CDN anyway. We have just eliminated one of two middle-men (Namecheap). We updated our Privacy Policy to reflect these new benefits at <https://inteltechniques.com/privacy>.

Today, we offer a pure HTML with Javacript Blog at <https://inteltechniques.com/blog/>. There is no database and all of the content is on a single HTML page. Images only load if you expand a post in order to keep bandwidth down for you and us. We created an RSS feed to continue supplying updates to those who rely on RSS readers for content. We even forward the old feed to the new so that your existing configurations should just work.

We have already posted new content and pruned the old and outdated material so be sure to take a look and subscribe to the RSS feed. We have many big things planned.

## New Firewall Guide

August 15, 20...