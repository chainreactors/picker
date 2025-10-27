---
title: Smart Searching with GoogleDorking
url: https://exposingtheinvisible.org/en/guides/google-dorking/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-03
fetch_date: 2025-10-04T02:55:30.279728
---

# Smart Searching with GoogleDorking

* [## Read

  Articles & Databases](/en/read)
* [## Watch

  Films](/en/watch)
* [## Listen

  Podcasts](/en/listen)
* [## Learn

  Guides & Workshops](/en/learn)

[![](https://cdn.ttc.io/i/fit/1088/0/sm/0/plain/exposingtheinvisible.org/kit-banner.jpg)

Investigative Techniques and Tools

### The Kit

kit.exposingtheinvisible.org](https://kit.exposingtheinvisible.org)

![red geometric shapes with honeycomb background](https://cdn.ttc.io/i/fit/1200/0/sm/0/plain/exposingtheinvisible.org/media20/guide/hero-guide-dork.jpg)

Access to information

# Smart Searching with GoogleDorking

#### Table of contents:

* History
* To dork or not to dork
* How it works
* Dorking for Dummies
* Dork It Yourself
* Defensive dorking

Using search engines to their full capacity to expose the unfindable.

“googleDorking,” also known as “Google hacking”, is a technique used by newsrooms, investigative organisations, security auditors as well as tech savvy criminals to query various search engines for information hidden on public websites and vulnerabilities exposed by public servers. Dorking is a way of using search engines to their full capacity to penetrate web-based services to depths that are not necessarily visible at first.

All you need to carry out a googleDork is a computer, an internet
connection and knowledge of the appropriate search syntax.

This guide will describe what googleDorking is and how it works
across different search engines, provide tips on how to protect yourself
while googleDorking and suggest ways to protect your websites and
servers from those who would use these techniques for malicious
purposes.

## History

googleDorking has been in documented use since the early 2000s. Like
many of the most successful hacks, googleDorking is not technically
sophisticated. It simply requires that you use certain *operators* —
special key words supported by a given search engine — correctly and
sometimes creatively. Johnny Long, aka j0hnnyhax, was a pioneer of
googleDorking. Johnny first posted his definition of the newly coined
term in 2002:

![](https://cdn.ttc.io/i/fit/1035/0/sm/0/plain/exposingtheinvisible.org/ckeditor_assets/pictures/595/content_googledork.jpg)

*Johnny Long's 2002 definition of a googleDork.*

In an
2011 [interview](http://www.techrepublic.com/blog/it-security/google-hacking-its-all-about-the-dorks/),
Johnny Long said, “In the years I've spent as a professional hacker,
I've learned that the simplest approach is usually the best. As hackers,
we tend to get down into the weeds, focusing on technology, not
realizing there may be non-technical methods at our disposal that work
as well or better than their high-tech counterparts. I always kept an
eye out for the simplest solution to advanced challenges.”

Rather than an ordinary type of search query that focuses on a semantic
way of asking questions, either directly through writing the whole
question or selected key words, googleDorking is based on reverse
engineering the way machines scan and index web content.

In this context, googleDorking uses search functions beyond
their semantic role, which not only changes how we typically imagine
using search engines, but also vastly expands the capacity of the tool
in the hands of people searching for a way of exploring content and
access to various services.

Such access might lead to the discovery of information that can be used
for fraud or terrorism, finding information on yourself or your
institution, as well as information that assists in the investigation of
governments, corporations or powerful individuals.  These results,
rather than being characteristic of the tool or method itself, instead
rely on the intentions of those using googleDorking, the questions they
are asking, and what they do with the results.

Dorking exposes vulnerabilities and also unleashes the unintended, often
powerful, consequences of searching search engines.

## To dork or not to dork

If you are thinking about using googleDorking as an investigative
technique, there are several precautions to take. Although you are free
to search at-will on search engines, accessing certain webpages or
downloading files from them can be a prosecutable offense, especially in
the United States in accordance with the extremely vague and
overreaching [Computer Fraud and Abuse Act
(CFAA)](https://en.wikipedia.org/wiki/Computer_Fraud_and_Abuse_Act).
Moreover, if you're dorking in a country with heavy internet
surveillance (i.e. any country), it's possible that your searches could
be recorded and used against you in the future.

As protection, we recommend using [the Tor
Browser](https://www.torproject.org/projects/torbrowser.html.en) or
[Tails](https://tails.boum.org) when googleDorking on any search engine.
Tor masks your internet traffic, divorcing your computer's identifying
information from the webpages that you are accessing. Security-in-a-Box
includes detailed guides on how to use the Tor Browser on
[Linux](https://securityinabox.org/en/guide/torbrowser/linux) and on
[Windows](https://securityinabox.org/en/guide/torbrowser/windows). Using
Tor will often make your searches more difficult. Google and other
search engines might ask you to solve captchas to prove you're human. If
your Tor exit node has recently been overrun with bots, search engines
might block your searches entirely. In this case, you should refresh
your Tor circuit until you connect to an exit node that's not
blacklisted. To do so, click the onion icon in the upper-left hand
corner of the browser and select “New Tor Circuit for this Site,” as
shown below.

![](https://cdn.ttc.io/i/fit/1035/0/sm/0/plain/exposingtheinvisible.org/ckeditor_assets/pictures/617/content_torcircuits.jpg)

Please note that, depending on what country you are in, using Tor might
flag your online activity as suspicious. This is a risk you must be
wiling to take when using Tor, though you can mitigate that risk to some
extent by using a [Tor
Bridge](https://www.torproject.org/docs/bridges.html.en) with an
[obfuscated pluggable
transport](https://www.torproject.org/docs/bridges.html.en#PluggableTransports).
Unless your are specifically targeted by an advanced attack, however,
the Tor Browser is quite good at preventing anyone from associating your
online identity with the websites you visit or the search terms you
enter. If you can not use Tor, you might want to find a VPN provider
that you trust and use it with a privacy-aware search engine, such as
DuckDuckGo.

If you decide to proceed with an investigation that involves
googleDorking, the remainder of this guide will help you get started and
provide a comparison of supported dorks across search engines as of
March 2017.

## How it works

Dorking can be employed across various search engines, not just on
Google. In everyday use, search engines like Google, Bing, Yahoo, and
DuckDuckGo accept a search term, or a string of search terms and return
matching results. But search engines are also programmed to accept more
advanced operators that refine those search terms. An operator is a key
word or phrase that has particular meaning for the search engine.
Operators include things like “inurl”, “intext”, “site”, “feed”,
“language”, and so on. Each operator is followed by a colon which is
followed by the relevant term or terms (with no space before or after
the colon).

A googleDork is just a search that uses one or more of these advanced
techniques to reveal something interesting.

These operators allow a search to target more specific information, such
as certain strings of text in the body of a website or files hosted on a
given url. Among other things, a googleDorker can locate hidden login
pages, error messages that give away too much information and files that
a website administrator might not realise are publicly accessible.

Not all advanced search techniques rely on operators. For example,
including quotation marks around text prompts the engine to search for
only the exact phrase in quotes....