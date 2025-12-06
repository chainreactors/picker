---
title: Windows Links and Usable Security
url: https://shostack.org/blog/windows-links-and-usable-security/
source: Shostack & Friends Blog
date: 2025-12-05
fetch_date: 2025-12-06T03:10:58.643282
---

# Windows Links and Usable Security

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. Windows Links and Usable Security

Shostack + Friends Blog

# Windows Links and Usable Security

Some dialogs can harm the viewer
![A Windows dialog, discussed at length in the post](/images/blog/img/2025/windows-lnk-bug-1600w.png)

Eric Lawrence concludes a recent [blog post](https://textslashplain.com/2025/12/03/security-surfaces/) “Ultimately the guidance
in the Security Warning prompt is the right advice: ‘If you do not
trust the source, do not open.’”

Unusually, Eric is wrong. First and foremost, the prompt does not
show a source, and so it's not giving actionable advice. It shows four fields: Name, Publisher, Type and
From. I can make a good argument that at least From and Publisher
are the “source,” but I can make a better argument that the source
information is literally not shown there. Since it's an internet
zone file, it has “Mark of
the Web” information, but that’s not presented, and its existence
is not even hinted at by the Warning prompt.

There’s a mnemonic, SPRUCE, which is quite useful in analyzing this
dialog. SPRUCE stands for:

* Source (of the dialog)
* Process (what should the human do?)
* Risk (what can go wrong)
* Unique information the user is bringing
* Choice
* Evidence that the user should evaluate

So looking at the dialog:

* Source: What popped that dialog? I’d bet its the Windows shell,
  but maybe it’s outlook or IE.
* Process: What do I check as I make a decision? Again, the
  dialog refers to a field that’s missing. What difference does it
  make that it’s an ‘unknown publisher’? The fact that information
  bubbles out seems important, but how do I use it? Do I care that
  it’s in Downloads? Does it bypass anti-malware?
* Risk: In what way can this harm your computer? Does it run code?
  Open an arbitrary file with arbitrary commands? Take advantage of
  a vulnerability? There’s certainly an argument that this could
  tip into jargon, but a more information link would be better than
  treating the reader like an child, incapable of using more information.
* Unique information: Why is the user being asked at all? (In this
  case, I can think of scant reasons for there to be a link in
  downloads which points out of downloads
* Choice: What choices can I make? Is there something I might do,
  like use the file explorer to learn more?
* Evaluation:
  Where does the file come from? (And here, what’s the
  relationship between “name” and “from?”

For more about SPRUCE, please see [Helping Engineers Design NEAT
Security Warnings](https://shostack.org/files/papers/ReederEtAl_NEATatMicrosoft.pdf).

Originally published by Adam on 05 Dec 2025

Categories:
  [usability](/blog/category/usability)
  [security](/blog/category/security)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling/)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder/)

[Other Star Wars blog posts](/blog/category/star-wars/)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives/)

[Doing science with near misses](/blog/doing-science-with-near-misses/)

[Posts about Adam’s “Threats” book](/blog/category/threats-book/)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book/)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school/)

[About this blog](/blog/about/)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read/).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact/) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![A Windows dialog, discussed at length in the post](/images/blog/img/2025/windows-lnk-bug-175w.png)](/blog/windows-links-and-usable-security/)

### [Windows Links and Usable Security](/blog/windows-links-and-usable-security/)

05 Dec 2025

Some dialogs can harm the viewer

[![a photograph of a robot, sitting in a library, working on a jigsaw puzzle. The robot holds up the jigsaw puzzle, and snow is falling inside the library](/images/blog/img/2025/appsec-roundup-winter-175w.png)](/blog/appsec-roundup-nov-2025/)

### [Secure By Design roundup - November 2025](/blog/appsec-roundup-nov-2025/)

30 Nov 2025

Perspective on CISOs as facilitators, a deep dive into the types of diagrams for medical devices, poetry, Chinese LLMs, Chinese drones and Chinese routers. Do any of them contain secrets?

[![A computer with a refreshable braille display.](/images/blog/img/2025/S+A_Accessibility-Hero-1200x500-175w.jpeg)](/blog/website-accessibility-improvements-2025/)

### [Recent accessibility improvements for the Shostack + Associates website](/blog/website-accessibility-improvements-2025/)

25 Nov 2025

Accessibility is an ongoing process. Learn about some recent updates to the Shostack + Associates website that increase accessibility and usability.

[![Open Web Application Security Project graphic](/images/blog/img/2025/owasp-reboot-175w.jpeg)](/blog/owasp-threat-model-reboot/)

### [OWASP Threat Modeling Reboot](/blog/owasp-threat-model-reboot/)

17 Nov 2025

Get in, we’re rebooting the OWASP Threat Modeling project!

## Popular Blog Topics

[Threat Model Thursday](/blog/category/threat-model-thursday/),
exploring specific published threat models

[Threat Modeling](/blog/category/threat-modeling/) (general topic)

[Application Security](/blog/category/application-security/)

[Software Engineering](/blog/category/software-engineering/)

[Cloud Security](/blog/category/cloud-security/)

[Compliance](/blog/category/compliance/)

[AI](/blog/category/ai/) + [ChatGPT](/blog/category/chatgpt/)

[Privacy](/blog/category/privacy/) + [Personal Security](/blog/category/personal-security/)

[Research](/blog/category/research-papers/) + [Reports](/blog/category/reports-and-data/)

[Book Reviews](/blog/category/book-reviews/)

[News](/blog/category/news/)

[Podcasts](/blog/category/podcasts/), [Videos](/blog/category/videos/) + [Webinars](/blog/category/webinars/)

Our site works best with Javascript enabled, however we have done our best to minimize any negative impacts to your experience without it.

* [Shostack on LinkedIn](https://www.linkedin.com/in/shostack/)
* [Shostack on Github](https://github.com/adamshostack/)
* [Stostack Videos on YouTube](https://youtube.com/c/shostack)
* © 2021-2025 Shostack + Associates  |  [Privacy Policy](/privacy-policy/)
* [Contact Shostack and Associates](/contact/)
* Call +1 866-APP-SECURE
* [Sitemap](/sitemap/)