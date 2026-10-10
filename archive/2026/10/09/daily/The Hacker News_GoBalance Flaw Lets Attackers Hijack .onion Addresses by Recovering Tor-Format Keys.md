---
title: GoBalance Flaw Lets Attackers Hijack .onion Addresses by Recovering Tor-Format Keys
url: https://thehackernews.com/2026/10/gobalance-flaw-lets-attackers-hijack.html
source: The Hacker News
date: 2026-10-09
fetch_date: 2026-10-10T07:58:22.475904
---

# GoBalance Flaw Lets Attackers Hijack .onion Addresses by Recovering Tor-Format Keys

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2IlqZRz59oSh813xvx6J6LZwp36zTJVBxQ-PeUsJRUAsFcG59ozpg3_EkL6lxZPOdBGD_o8YVUq2CVyutLmT7SgKt513yyCnRmX1J8e5b358cLIneCtSSp46pMvfQ-md9-VagqDnUxxJPuU1CFx7hjpZv75B2E77SI400cPs5PKE4H0uWsGfvEwg_lfzn/s728-nu-rw-lo-l85-e365/prompt-injection-response-d.png)](https://thehackernews.uk/prompt-injection-response-d)

# [GoBalance Flaw Lets Attackers Hijack .onion Addresses by Recovering Tor-Format Keys](https://thehackernews.com/2026/10/gobalance-flaw-lets-attackers-hijack.html)

**Swati Khandelwal**Oct 09, 2026Vulnerability / Dark Web

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjUJ8xcgqF85kQru4JEuCv6OipwHlff6IEp3r1zhFOY9tYpbwEeWYSqzPTILX4uqM97Cc9ZfNfb3HB4lZbecN48fqKgKryAL60KqqZU4HmdfTMsRYaDcFjNL7aE8vk7G0D_-mqY_B2Jk_3kXMsx2ABpgbWixg1GHZ2l7V0MSzqtEWnYZ_ymkOTf0j8yq2c/s1700-nu-rw-lo-l85-e365/onion.jpg)

A bug in **GoBalance**, a tool many dark-web sites use to stay reachable during attacks, lets anyone work out the secret key that controls a site's .onion address using only public information, and then take that address over.

Searchlight Cyber, which [disclosed the flaw](https://www.slcyber.io/research/leaking-the-keys-to-the-kingdom-how-a-single-slip-handed-over-a-darknet-empire) on October 8, says an attacker who recovers the key can redirect the site's visitors to a copy of the site they control. Taking over the address does not grant the attacker access to the site's servers, database, or stored user data.

### How the Flaw Works

An .onion address is really [a public key](https://spec.torproject.org/address-spec.html), so whoever holds the matching private key controls the address. To stay reachable, a site publishes a signed record, called a descriptor, that anyone on the Tor network can fetch, and GoBalance signs that record.

The flaw is in the signing step. A Tor private key is [64 bytes](https://pkg.go.dev/crypto/ed25519) long, but GoBalance passed only the first 32 bytes to the signer and dropped the rest. The dropped half is the part that keeps each signature's secret value hidden.

Without that half, the secret value becomes a fixed number anyone can compute. A single published descriptor then carries enough to recover the site's private key, with no access to its servers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

Because the exposed key is the site's long-term master key, not a short-lived one, a recovered key can sign valid records for the address far into the future.

### Which Sites Are at Risk

GoBalance is a version of Tor's Onionbalance load balancer rewritten in Go, and it ships with EndGame, a widely used toolkit that keeps dark web sites online during denial-of-service attacks. The flaw is in the rewrite.

Searchlight says the original Onionbalance and Tor itself are not affected.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjesPi86S9SgS_AUsCm_WQIeGk01-AFLncifE_Z8hLygE4vmiqyjMYVZ0wpdXqQFgyUio8YHO7Cx9A2fY_5Amj3_Xddvf_3Z3tRRDM1er9ZPHiI390uEwDInVfqmGRvHEQOP5cjyiablQ04UzAgH5nja6qtWspJnd9555J1tEXbiUVGtDfC-3cmWmnhL78/s1700-nu-rw-lo-l85-e365/hacked.png)

It also affects only sites whose master key is stored in Tor's own key format. GoBalance's setup tool writes keys in a safer format that is not at risk, so not every site running GoBalance is exposed.

### The Dread Takeover

The flaw came to light through Dread, one of the dark web's biggest forums, run by administrators who go by HugBunter and Paris. Between October 5 and 7, both of Dread's .onion addresses were taken over and pointed at a rival site, Conclave.

Dread's operators first blamed their own mistake. On October 5, Paris [said](https://monero.observer/dread-main-onion-private-key-exposed/) he had "stupidly uploaded dread's main onion private key into a gobalance update."

Two days later the second address, a backup kept for premium members, was taken over as well. A backup is harder to explain as a slip, and HugBunter then said the attacker had used a GoBalance flaw against several dark-web services. Searchlight takes the same view, calling the second takeover the stronger sign the flaw was used, while still treating the first address as a separate key leak.

Dread has since moved to a new address and told users to change their passwords. In a [signed message](https://tor.watch/service/dread) on October 7, the operators said the forum had "migrated, permanently, following onion private key exposure due to a vulnerability in third-party software," and that "other hidden services may be affected." They say Dread's servers were not broken into.

### Who Else Is Affected

How many other sites are affected is not clear. HugBunter said several dark-web markets had their addresses taken over, including some that had already shut down, but did not name them or give a number.

At least one other site has confirmed it publicly. Omega, a dark-web market, said in a [signed note](https://tor.watch/service/omega) on October 8 that it took its old address offline "due to an issue caused by the GoBalance bug" and moved to a new one.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

### No Official Fix Yet

There is no official fix. On October 9, The Hacker News found no CVE identifier for the flaw in the US National Vulnerability Database and no public advisory from the Tor Project or GoBalance's maintainer. Dread has said it plans to release a patched version of GoBalance and help affected sites move across.

An independent researcher has published [a patch and a working proof-of-concept](https://github.com/kolmteistov/gobalance-patch) that recovers a master key from a single public descriptor. The researcher says the demonstration used only keys made for the test and that no real service was targeted. The Hacker News has not run the code, and it is not an official release.

### What Operators and Users Should Do

For site operators, a patch alone does not undo the exposure. Once a descriptor has been published, the key it leaks cannot be pulled back, so a site that ran a vulnerable version has to create a new .onion address and move to it, as Dread and Omega have done.

For users of a site that may be affected, Dread's advice wa...