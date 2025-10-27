---
title: The Watermarking Paradox
url: https://www.hackerfactor.com/blog/index.php?%2Farchives%2F1042-The-Watermarking-Paradox.html=
source: Instapaper: Unread
date: 2024-09-11
fetch_date: 2025-10-06T18:30:49.055944
---

# The Watermarking Paradox

![Hacker Factor Logo](/images/hf-lock-banner.png)

[The Hacker Factor Blog](/blog/)

**Work without a net**

[Home](/)
[Blog](/blog/)
[Swag](https://www.zazzle.com/hackerfactor/?rf=238307745558769988)

### About

[Dr. Neal Krawetz](/about.php) writes The Hacker Factor Blog. Follow him on [Mastodon](https://noc.social/%40hackerfactor).

### Tools

• [FotoForensics](https://fotoforensics.com/): Test your own photos.

### Links

**Security**

### Calendar

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| [«](https://hackerfactor.com/blog/index.php?/archives/2025/09.html "View posts for previous month") | October '25 | | | | | [»](https://hackerfactor.com/blog/index.php?/archives/2025/11.html "View posts for previous month") |
| S | M | T | W | T | F | S |
|  |  |  | 1 | 2 | 3 | 4 |
| 5 | 6 | 7 | 8 | 9 | 10 | 11 |
| 12 | 13 | 14 | 15 | 16 | 17 | 18 |
| 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| 26 | 27 | 28 | 29 | 30 | 31 |  |

### Archives

* [October 2025](/blog/index.php?/archives/2025/10.html "October 2025")
* [September 2025](/blog/index.php?/archives/2025/09.html "September 2025")
* [August 2025](/blog/index.php?/archives/2025/08.html "August 2025")
* [Recent...](/blog/index.php?frontpage)
* [Older...](https://hackerfactor.com/blog/index.php?/archive)

### Feeds

* [![XML](/blog/templates/nealk/img/xml.gif)](/blog/index.php?/feeds/index.rss1)
  [RSS 1.0 feed](/blog/index.php?/feeds/index.rss1)
* [![XML](/blog/templates/nealk/img/xml.gif)](/blog/index.php?/feeds/index.rss2)
  [RSS 2.0 feed](/blog/index.php?/feeds/index.rss2)

### Categories

* [Conferences](/blog/index.php?/categories/7-Conferences "Been there, done that, took notes")
* [Copyright](/blog/index.php?/categories/16-Copyright "Copyrights, Patents, and Concerns")
* [Financial](/blog/index.php?/categories/8-Financial "Money Matters")
* [Forensics](/blog/index.php?/categories/14-Forensics "Computer and Digital Forensics")
* [Authentication](/blog/index.php?/categories/23-Authentication)
* [FotoForensics](/blog/index.php?/categories/17-FotoForensics "http://fotoforensics.com/")
* [Image Analysis](/blog/index.php?/categories/1-Image-Analysis "A Picture's Worth")
* [IoT](/blog/index.php?/categories/22-IoT "Internet of Things")
* [Mass Media](/blog/index.php?/categories/6-Mass-Media "Volume Does Not Imply Brightness")
* [Music](/blog/index.php?/categories/24-Music)
* [Network](/blog/index.php?/categories/3-Network "A Series of Tubes")
* [Honeypot](/blog/index.php?/categories/21-Honeypot "This is my other computer")
* [Tor](/blog/index.php?/categories/19-Tor "The Onion Router")
* [Phones](/blog/index.php?/categories/18-Phones "Telemarketers, Cold Calls, and Scams")
* [Politics](/blog/index.php?/categories/13-Politics "Fear, Uncertaity, Doubt, and that bad aftertaste")
* [Privacy](/blog/index.php?/categories/9-Privacy "You Have The Right")
* [Programming](/blog/index.php?/categories/5-Programming "Code Monkey's Unite!")
* [AI](/blog/index.php?/categories/20-AI "AI and Machine Learning")
* [Security](/blog/index.php?/categories/4-Security "Attack and Defend")
* [Terrorists](/blog/index.php?/categories/2-Terrorists "Terrorism Research")
* [Travel](/blog/index.php?/categories/15-Travel "Enjoy life! Eat out more often!")
* [Unfiction](/blog/index.php?/categories/12-Unfiction "I can't make this up...")
* [[Other]](/blog/index.php?/categories/11-Other "Catch-all category")

[All categories](/blog/index.php?frontpage "All categories")

# [The Watermarking Paradox](/blog/index.php?/archives/1042-The-Watermarking-Paradox.html)

## Sunday, 8 September 2024

Lately there has been a huge push to include watermarks in pictures in order to identify AI-generated content. For example:

* Adobe, Microsoft, and OpenAI (C2PA's steering committee members) have recently thrown their support behind a [California bill](https://digitaldemocracy.calmatters.org/bills/ca_202320240ab3211) to require watermarking all AI images.

* US House bill [H.R.7766](https://www.congress.gov/bill/118th-congress/house-bill/7766/text/ih) is the "Protecting Consumers from Deceptive AI Act", wants to require watermarking AI-generated images.

* US Senate bill [S. 2765](https://www.congress.gov/bill/118th-congress/senate-bill/2765/text) is the "Advisory for AI-Generated Content Act" which also wants to require watermarking of AI images.

* Another Senate bill called the [Content Origin Protection and Integrity from Edited and Deepfaked Media Act (COPIED Act)](https://mashable.com/article/senate-introduces-ai-bill-to-protect-artists-creatives) would make it illegal to remove watermarks from AI-generated images, with no exceptions for unintentional removals due to post-processing and editing by creators. (See the [bill's text](https://www.commerce.senate.gov/services/files/3012CB20-193B-4FC6-8476-DDE421F3DB7A), Section 6(b)(1).) This bill is supported by [Microsoft](https://www.techspot.com/news/104043-microsoft-urges-congress-enact-laws-against-deepfake-misuse.html), [Google](https://decrypt.co/242814/google-ai-deepfake-demote-search-results), and other C2PA steering committee members.

It appears that Microsoft, Adobe, and other members of C2PA are trying to codify the faulty C2PA approach into law.

In my opinion, this is a massively flawed application of watermarking technology. I've mentioned some of these problems in [previous](/blog/index.php?/archives/1031-C2PA-from-the-Attackers-Perspective.html) [entries](/blog/index.php?/archives/1024-IEEE,-BBC,-and-C2PA.html>blog</a> <a href=), but none of them really dove deep into the technical problems. (They basically said, at a high level, that the watermarking approach is "[flimsy at best](https://spectrum.ieee.org/meta-ai-watermarks)".) This blog entry is a technical review of watermarking technologies and how C2PA supports this flawed usage.

### Types of Watermarks

There are two types of watermarks: visible and invisible. A visible watermark is just an overlay on the image (or video or other media). They can be easily added using common graphics editors. However, they are not very robust; whether it is cropping or subtle editing, these overlays are trivial to remove.

For example, back in 2013, a developer at Getty Images uploaded two pictures to the public FotoForensics service. The first picture shows Rupert Grint (he played Harry Potter's [unappreciated sidekick](https://www.reddit.com/r/HarryPotterMemes/comments/o9i8gk/books_by_ron_weasley/), Ron Weasley) and includes a visible watermark in the center of the image.

[![](https://fotoforensics.com/analysis.php?id=7fd8766ae80c0006d5f6e8089acbd53fc5f32aea.152782&fmt=orig&size=600)](https://fotoforensics.com/analysis.php?id=7fd8766ae80c0006d5f6e8089acbd53fc5f32aea.152782)

The second picture, titled "My\_watermark\_removal\_166042229.jpg", shows the same image but with the visible watermark removed:

[![](https://fotoforensics.com/analysis.php?id=ba9888fe8041f7e11220a8e9e2c91c4d6aa64e5c.151153&fmt=orig&size=600)](https://fotoforensics.com/analysis.php?id=ba9888fe8041f7e11220a8e9e2c91c4d6aa64e5c.151153)

And keep in mind, this was 11 years ago and before we had lots of AI tools to help remove visible watermarks. According to the metadata, this change was made using Paint.NET.

Personally, I have no problems with visible watermarks. They provide a superficial way to tag images and attribute ownership. Because the watermark is written into the visual content, it is a little more robust than writing a copyright statement in some metadata field. The visible watermark shows the intent of the owner to retain their intellectual property. While the presence can mitigate image theft, it's far from a perfect solution. The watermarks can be easily removed or intentionally added for false attribution. As attribution methods go, visible watermarks are often a "good enough" solution.

### Invisible Watermarks

Invisible watermarks are encoded in the image (or video stream, audio stream, etc.). They exist, but you probably can't see them...