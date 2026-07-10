---
title: I Wrote a New Book for Corelight
url: https://taosecurity.blogspot.com/2026/07/i-wrote-new-book-for-corelight.html
source: TaoSecurity Blog
date: 2026-07-09
fetch_date: 2026-07-10T06:00:09.502938
---

# I Wrote a New Book for Corelight

[Skip to main content](#main)

### Search This Blog

# [TaoSecurity Blog](https://taosecurity.blogspot.com/)

Richard Bejtlich's blog on digital security, strategic thought, and military history.

### I Wrote a New Book for Corelight

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

[July 09, 2026](https://taosecurity.blogspot.com/2026/07/i-wrote-new-book-for-corelight.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLD7qvOGj-vysW1oKnpVauXypgCv8nGDkAJ3-ku3GFDTwH2ud2n6fOVAkjfyQlqkWtiuloQi86jC36SFQ6q8RtciyqVGS0J1eJkJNc2_3L1-uiETD82IB7P0py3Xf3ggvbiBGi8rtIVZttdqk8vz1svXuVyt1YYZXCG1sO5VtHwTDEJgkNjCj3/w426-h640/cover.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjLD7qvOGj-vysW1oKnpVauXypgCv8nGDkAJ3-ku3GFDTwH2ud2n6fOVAkjfyQlqkWtiuloQi86jC36SFQ6q8RtciyqVGS0J1eJkJNc2_3L1-uiETD82IB7P0py3Xf3ggvbiBGi8rtIVZttdqk8vz1svXuVyt1YYZXCG1sO5VtHwTDEJgkNjCj3/s864/cover.png)

TLDR: I wrote a new book for Corelight called [NDR Essentials](https://corelight.com/cp/ndr-essentials). It's free at that link. This is the 10th book that I've authored or co-authored. The rest are all posted at [taosecurity.com](https://www.taosecurity.com/).

Why?

It was time.

That’s what I thought when I heard that Corelight wanted to
update its 2021 book on network detection and response (NDR). Tamara
Crawford, who owned the project, scheduled a meeting with me and asked
if I might be interested in helping, depending on who might write the
text.

I volunteered immediately to write the whole book, but I had a
few conditions. The text had to be at least 100 pages long, because 100
pages is my personal dividing line between “book” and “white paper.” I
needed the freedom to cover the topics I wanted to address, and to not
be told what to write. I wanted to show the four network security
monitoring (NSM) data types working in a vendor-neutral manner, with
technical details. Finally, I knew this project would take several
months to research, write, lay out, proofread, and complete. Once
Corelight agreed, I was ready to begin.

My goal for the book was to show how high-fidelity [network evidence](https://corelight.com/resources/glossary/network-evidence)
can power successful incident detection and response operations. For
decades, digital security relied on the flawed premise that the “right”
security controls could stop malicious activity. History, however, has
repeatedly shown that prevention eventually fails. Victory belongs to
the defender who accepts that intrusions are inevitable and who
implements aggressive post-compromise interdiction and containment.

Security teams have the best chance to stop an adversary before
they accomplish their mission when they leverage network security
monitoring data and the latest [AI and automation assistants](https://corelight.com/resources/glossary/ai-driven-soc). Therefore, this book equips practitioners with the tools and mindsets necessary to hunt through network evidence and diminish [attacker dwell time](https://corelight.com/resources/glossary/attacker-dwell-time).

**The book begins** with a chapter
that defines risk, threat, vulnerability, and asset value in the context
of cybersecurity. It explains seven risk management strategies, NDR’s
role in the security cycle, four sources of situational awareness, the
importance of time and how to measure it, and a variety of NDR-specific
topics like where and how to monitor, costs vs. benefits, and the
difference between [NSM](https://corelight.com/resources/glossary/network-security-monitoring-nsm) and [NDR](https://corelight.com/resources/glossary/ndr-network-detection-and-response).

**Chapter 2** is all about the four
types of NSM data. I show examples of full content data via terminal and
graphical interfaces, and what it can do for analysts. I briefly
demonstrate how to obtain and analyze extracted content, then show how
transaction data can answer many of the key questions asked by security
analysts. The chapter concludes with alert data, which has become more
significant in an age of smarter and more precise AI capabilities.

**Chapter 3** is the first of two
chapters demonstrating workflows for security investigators. This
chapter examines how alert data from a sufficiently capable NDR can
identify suspicious and malicious activity. It includes four cases,
showing how lateral movement, expired SSL certificates, outbound
reconnaissance, and malicious remote desktop protocol behavior manifest
in alerts.

**Chapter 4** presents the other side of investigative workflows, relying on [threat hunting](https://corelight.com/resources/glossary/threat-hunting)
to reveal adversary activity. Properly collected, rendered, and
displayed NSM data is crucial, because you can’t really hunt without
high-quality evidence. The chapter includes six cases, showing how file
name mismatches, unusual downloads, large data transfers, coordinated
exfiltration, lateral movement, and certificates appear when exposed via
threat hunting.

**Chapter 5** explores how artificial
intelligence and automation technologies are bringing powerful new
capabilities to security teams. I start by discussing the generation of
alerts at the edge and at the center, then I share how AI can help with
investigating suspicious and malicious activity. I conclude
with advice on the best use of agentic triage and how AI will integrate
with tools while enabling new capabilities.

If you’re a security leader, such as a CISO or director, you’ll
probably be most interested in Chapters 1 and 5. You should ensure your
teams have the data described in Chapters 2-4. If you’re a security
analyst, you’ll probably be most interested in Chapters 2-4, although
you should be familiar with the concepts and strategies in Chapters 1
and 5. If you’re familiar with my previous works, you will be happy to
see that this book has a certain amount of “future-proofing” embedded. I
did not explain how to install any specific tools, nor did the tools I
use rely on strict display technologies. All of the examples in Chapter 2
use open source tools with stable outputs, such as Tshark, Wireshark®, Zeek®, and Suricata®.

I hope readers find the book relevant to their security work
and a decent introduction to adding NSM data from capable NDRs to their
investigations. This book is only the beginning of what can be done once
teams have access to high-fidelity network evidence. If you’d like to
know more about the book, Vince Stoffer interviewed me for the [Corelight podcast](https://corelight.com/podcasts),
and that episode will be available on YouTube, Spotify, and Apple
Podcasts. As I say at the end of every episode, “we will see you on the
network.” Read [*NDR Essentials*](https://corelight.com/cp/ndr-essentials) to learn how high-fidelity network evidence can strengthen your security program!

[books](https://taosecurity.blogspot.com/search/label/books)
[nsm](https://taosecurity.blogspot.com/search/label/nsm)
[writing](https://taosecurity.blogspot.com/search/label/writing)

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

### Comments

[Post a Comment](https://www.blogger.com/comment/fullpage/post/4088979/5309444058770321302)

### Popular posts from this blog

### [Zeek in Action Videos](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html)

[July 29, 2021](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html "permanent link")

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhcWFyS3aGQrT6UiiiBbLkOiUs5W_Y9cYMLeH2Z7KkzzqINSWjFIEG8inSUNbYNGTjF7dcEUOOOkK7DzHQXcNMY3Nhl1PIFsdZZeJOH7bzRzpQMUdez5M7_g3t_xyygra49FBKK/w640-h360/capture_001_29072021_143006.jpg)](https://taosecurity.blogspot.com/2021/07/zeek-in-action-videos.html)

This is a quick note to point blog readers to my Zeek in Action YouTube video series for the Zeek network security monitoring project .  Each video addresses a topic that I think might be of interest to people trying to understand their ...