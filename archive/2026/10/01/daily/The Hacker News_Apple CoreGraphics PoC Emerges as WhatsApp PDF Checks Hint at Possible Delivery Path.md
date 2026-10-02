---
title: Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path
url: https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html
source: The Hacker News
date: 2026-10-01
fetch_date: 2026-10-02T07:49:38.484029
---

# Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path

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

# [Apple CoreGraphics PoC Emerges as WhatsApp PDF Checks Hint at Possible Delivery Path](https://thehackernews.com/2026/10/apple-coregraphics-poc-emerges-as.html)

**Swati Khandelwal**Oct 01, 2026Vulnerability / Mobile Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5u07cHr0A83x9aQdJE-_Emw6K1GzjR2eybdv9Rq_qi43Oi-M2U4eWqCkjvH5fUhw5wKSa-rvQ81gePKLYCqJXyrZpWHXOehEFq_QaTdYpy0O3LLUQGGYn1pxlUGUXwplloAHT3ZP7oMcF6al9A7q9XfnYNUhtBD0qw-GOWuKiyZl8zbrudyjWtEzHXC0/s1700-nu-rw-lo-l85-e365/apple-whatsapp.jpg)

Security researchers have published the first public proof-of-concept for **CVE-2026-86950**, an Apple CoreGraphics flaw Apple says may have been used in attacks against specific targeted individuals.

The trigger is a malicious PDF with a crafted embedded font that crashes unpatched iPhones and Macs. The code causes a crash, not an execution error. Turning the memory corruption into a working exploit is separate work the analysis does not demonstrate.

Apple patched the flaw on [September 28](https://thehackernews.com/2026/09/apple-patches-coregraphics-flaw.html), crediting Meta Product Security with the discovery and noting it may have been used in an "extremely sophisticated attack against specific targeted individuals on versions of iOS before iOS 27."

The U.S. Cybersecurity and Infrastructure Security Agency [added the flaw](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-86950) to its Known Exploited Vulnerabilities catalog the following day, requiring federal agencies to apply the fix by October 2.

Apple has not listed iOS 27 or macOS Golden Gate 27 as affected in the September 28 advisories. No workaround has been described for systems that cannot update immediately.

### What the Researchers Found

The analysis was published September 30 by Dion Blazakis, Josh Maine, and Anna Groza of [Calif](https://calif.io/research/the-great-glyph-grift), a firm known for research into [zero-click attack surfaces](https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html) in messaging apps. They started from a publicly available binary comparison of iOS 26.7 and 26.7.1.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/growth-ai-control-d)

CoreGraphics is the Apple framework for 2D drawing, image rendering, and PDF processing. It was the only library changed in 26.7.1, with the same fix applied more than 20 times across eight rasterizer functions.

The patched code converts a glyph coordinate from floating-point to a 32-bit fixed-point value. Before the patch, two of the eight functions handled out-of-range values differently: one saturated the result, the other truncated it.

That difference caused the calculated bounding box for a glyph to be too narrow. CoreGraphics then allocated a working buffer smaller than the edges it needed to draw, and wrote outside it.

To trigger the bug, the researchers built a TrueType font with coordinates large enough to force the overflow. Embedding it in a PDF with a text matrix and nested composite-glyph scaling pushes those coordinates past the limit. They published the generation scripts and a sample PDF in a [public GitHub repository](https://github.com/califio/publications/tree/main/MADBugs/CVE-2026-86950).

The harness calls the same ImageIO thumbnail path an app uses when previewing a received attachment. The researchers say the crash occurs on both macOS and iOS.

The macOS result includes a full debugger call stack. The iOS claim is Calif's, with no separate trace published.

The crash exposes a controlled out-of-bounds write that affects two adjacent 16-bit values in a buffer that the attacker can control, allowing writes to the stack or heap. Calif says converting that primitive into working code execution is separate work. Calif did not obtain the in-the-wild sample and cannot say how the attacker completed the chain.

### The WhatsApp Question

Calif examined WhatsApp because Meta Product Security was credited with finding the flaw. The firm compared two recent WhatsApp versions, 26.37.73 and 26.38.74, and found new code in WhatsApp's [Kaleidoscope](https://engineering.fb.com/2026/01/27/security/rust-at-scale-security-whatsapp/) attachment scanner.

The newer version reads PDF files for embedded font streams and flags suspicious ones with three defect tags: MalformedFontProgram, UndecodableFontProgram, and UnverifiedFontProgram. Any such tag returns a high-risk score to WhatsApp's attachment checker, which then stops automatic parsing of the flagged file.

Calif described those changes as circumstantial evidence pointing toward WhatsApp as a possible delivery vector. The firm's post describes its research as covering a possible WhatsApp zero-click path.

The published analysis does not describe or test a WhatsApp delivery path. The initial version did: it said the researchers' analysis suggested WhatsApp could deliver a PDF that triggers the flaw when a victim opens a chat from a trusted contact with automatic media downloads on.

That sentence was removed 85 minutes after publication in a commit by Calif CEO Thai Duong, who described the change as removing the WhatsApp speculation.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The analysis closes with a question: whether the flaw "was combined with additional vulnerabilities in WhatsApp to reach parsing with less user interaction." That phrasing suggests the path Calif studied would require user action or further WhatsApp vulnerabilities in the chain.

WhatsApp has published no advisory linking this flaw to its products. Its 2026 advisory page lists two unrelated vulnerabilities.

The Hacker News asked Meta whether WhatsApp was involved in the reported attacks. Meta did not respond before publication.

An earlier case makes the hypothesis plausible. In August 2025, WhatsApp assessed that a flaw in its linked-de...