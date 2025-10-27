---
title: ISPs Hijack Cloudflare/Google DNS Requests, Ending Site-Blocking Workarounds
url: https://torrentfreak.com/isps-hijack-cloudflare-google-dns-requests-ending-site-blocking-workarounds-240807/
source: TorrentFreak
date: 2024-08-08
fetch_date: 2025-10-06T18:08:11.732320
---

# ISPs Hijack Cloudflare/Google DNS Requests, Ending Site-Blocking Workarounds

[![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/search.svg)

* News ▼
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/x.svg)

# ISPs Hijack Cloudflare/Google DNS Requests, Ending Site-Blocking Workarounds

August 7, 2024 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

When ISPs are instructed to block pirate sites, tampering with their own DNS records is often the weapon of choice. This type of blocking can be circumvented by switching to public DNS offered by companies including Cloudflare and Google. Tests carried on several ISPs in Malaysia this week reveal that requests to Cloudflare and Google public DNS servers are being hijacked and diverted to local ISP DNS servers.

[![dns-liar](https://torrentfreak.com/images/dns-liar.png)](https://torrentfreak.com/images/dns-liar.png)To the average internet user, DNS translates a domain into an IP address to make browsing as simple and unintrusive as possible. Under the hood, DNS does just that and for the majority of people online, that’s good enough.

For those who work with DNS and understand how incredibly important (and beautiful) it is, the idea that DNS is something to be tampered with, so that the system effectively tells lies, steps over the line. Yet, thanks to the global site-blocking drive, DNS servers all around the world, in dozens of countries, constantly lie to those who use them.

Site-blocking programs dictate that, when ISP-operated DNS servers are asked to return the IP addresses for tens of thousands of ‘pirate’ domains, the IP addresses returned by those DNS servers (if any IP addresses are returned at all) will not be the correct ones. This means that the user cannot access the domain; not by this route at least.

## Public DNS – Mostly Tamper-Free

Since most blocking measures are implemented by consumer ISPs that operate their own DNS servers, users who switch to public DNS servers operated by Cloudflare, Google, Quad9, and many others, can usually avoid ISP blocking altogether. There are some exceptions depending on country, and since all three of the above have been ordered to [block](https://torrentfreak.com/cloudflare-dns-has-to-block-pirate-sites-italian-court-confirms-230403/) a [small number](https://torrentfreak.com/google-cloudflare-cisco-will-poison-dns-to-stop-piracy-block-circumvention-240613/) of [domains](https://torrentfreak.com/dns-resolver-quad9-wins-pirate-site-blocking-appeal-against-sony-231208/), switching to their DNS servers won’t unblock *every* domain, just the overwhelming majority.

Pressure from the Motion Picture Association (MPA) to introduce pirate site blocking in Malaysia, led to its implementation under Section 263 of the Communications and Multimedia Act 1998. Requests to block sites are processed by the Malaysian Communications and Multimedia Commission (MCMC), which instructs local ISPs to prevent their systems “from being used in, or in relation to, the commission of any offense,” including copyright infringement.

MPA reports on Malaysia’s site-blocking program have painted a regular picture of success but, in common with other schemes reliant on DNS tampering at ISPs, users eventually discovered that switching to public DNS restores connectivity.

Reports emerging from Malaysia this week, affecting both Cloudflare and Google DNS, are much more concerning than ISP blocking or even blocking measures imposed on public DNS providers.

## Public DNS Under Threat and Reportedly Hijacked in Malaysia

The Internet Monitoring Action Project (iMAP) monitors internet interference and restrictions impacting freedom of expression online in Cambodia, Hong Kong (China), India, Indonesia, Malaysia, Myanmar, Philippines, Thailand, Timor-Leste and Vietnam. The group uses the detection and reporting systems of the Open Observatory Network Interference ([OONI](https://ooni.org/)) and this week reported a significant shift in Malaysia’s site-blocking program.

“It was detected through automated and manual testing on 5th August, that transparent DNS proxy redirecting of DNS queries to Google and Cloudflare public DNS servers has been implemented by two Malaysian ISPs Maxis and Time,” [iMAP reports](https://imap.sinarproject.org/news/internet-censorship-update-transparent-dns-proxy-implemented-by-malaysian-isps-on-cloudflare-and-google-public-dns-servers).

“Users that have configured their Internet settings to use alternative DNS servers, would have found that they are now unable to access websites officially blocked by MCMC and [are now] getting a connection timeout error.”

A brief technical summary from iMAP reveals what happens when users attempt to access sites using Cloudflare and Google DNS.

> *• On Maxis, DNS queries to Google Public DNS (8.8.8.8) servers are being automatically redirected to Maxis ISP DNS Servers;*
>
> • On Time, DNS queries to both Google Public DNS (8.8.8.8) and Cloudflare Public DNS (1.1.1.1) are being automatically redirected to Time ISP DNS servers.

“Instead of the intended Google and Cloudflare servers, users are being served results from ISP DNS servers. In addition to MCMC blocked websites, other addresses returned from ISP DNS servers can also differ from those returned by Google and Cloudflare,” iMAP warns.

## Technical Problems, Technical Solutions

It’s worth highlighting the seriousness of these claims. Requests destined for Google and Cloudflare DNS are being rerouted to local ISPs, in a manner that indicates those companies are responsible for users ending up at the Malaysian Communications and Multimedia Commission’s IP address (175.139.142.25), rather than the website they requested.

In a nutshell, internet users cannot rely on their ISPs’ DNS servers to respond accurately, and can no longer rely on third-party DNS to respond accurately either.

But if there’s one good thing about such aggressive blocking it’s this: like almost all efforts that rely on a technical solution to impose blocking, there is a technical solution to neutralize it.

[Details are available from iMAP](https://imap.sinarproject.org/news/internet-censorship-update-transparent-dns-proxy-implemented-by-malaysian-isps-on-cloudflare-and-google-public-dns-servers) and apply to anyone wishing to improve their online privacy and security in general, not just those wishing to avoid their DNS requests being hijacked.

“Users that are affected, can configure their browser settings to enable DNS over HTTPS to secure their DNS lookups by using direct encrypted connection to private or public trusted DNS servers. This will also bypass transparent DNS proxy interference and provide warning of interference,” iMAP concludes.

## Tacit Acceptance of ■■■■■■■■■■

Finally, it’s worth mentioning that Malaysia is no stranger to censorship and controlling access to information. Under the Printing Presses and Publications Act 1984, unlicensed use or possession of a printing press is still a crime. [Site-blocking measures](https://monitor.civicus.org/explore/malaysia-blocking-of-websites-use-of-sedition-law-and-harassment-of-protesters-undermines-funda...