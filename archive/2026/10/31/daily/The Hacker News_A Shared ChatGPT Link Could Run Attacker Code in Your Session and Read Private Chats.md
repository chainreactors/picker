---
title: A Shared ChatGPT Link Could Run Attacker Code in Your Session and Read Private Chats
url: https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html
source: The Hacker News
date: 2026-10-31
fetch_date: 2026-11-01T08:21:37.848948
---

# A Shared ChatGPT Link Could Run Attacker Code in Your Session and Read Private Chats

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [A Shared ChatGPT Link Could Run Attacker Code in Your Session and Read Private Chats](https://thehackernews.com/2026/10/a-shared-chatgpt-link-could-run.html)

**Swati Khandelwal**Oct 31, 2026Vulnerability / Web Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhEplEzMjNIg5IBNIX4uz_WyVhtJqqbKICvvpW5LbwPEsQVd4ypSQC1ISnXoR0pMLlQEF4erNUIf-5-ELvBXIE8VH2Iv7dCPCuaZAFVeS9VIITs_5e_77DwtIvo3ExUcfJC_aT4x3FDD3AmTKeQFKnOrufXorlbiHOJNO-pUhwzBNwL98r-2JSW2CWiTBs/s1700-nu-rw-lo-l85-e365/chatgpt.jpg)

A malicious ChatGPT share link could run an attacker's code in the logged-in session of anyone who opened it, allowing them to read their private conversations, researchers at the security firm Parameter showed.

The researchers reported the flaw through [OpenAI's bug bounty program](https://bugcrowd.com/engagements/openai) on October 18, and OpenAI fixed it eight days later and rated it P1, its most serious category.

The trap was an ordinary ChatGPT conversation shared via its public link. It could be sent the same way as any real shared chat: by email, as a chat message, as a support ticket, or as a social post.

The victim did not have to install anything, join a workspace, or sign in through the attacker. In the most reliable version of the attack, they opened the link and clicked ChatGPT's Preview button once. In a later version, Parameter set the page to open Preview on its own, so opening the link was the only step.

### What the Attacker Could Do

Once the link opened, the attacker's code ran inside the victim's signed-in session with the same access as the real ChatGPT site. It listed the victim's recent conversations, opened a private chat that had never been shared with the attacker, and sent a small portion of it to a server controlled by the researchers.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The code called ChatGPT's own signed-in APIs directly, rather than copying what happened to be on the screen. Because it ran with the victim's full web access, its reach was not limited to those chats. "Essentially, we could perform any action on behalf of the victim's ChatGPT account," the researchers [wrote](https://www.parameter.ai/labs/we-found-a-gap-at-openai).

The work was a controlled test. Parameter does not report any real-world use of the flaw, and ran its private-chat proof between separate accounts rather than against real users.

### How the Link Broke Out of Its Sandbox

Here is how the chain worked, according to Parameter. ChatGPT can turn a block of HTML in a chat into a small web page through a feature called Preview. Because that page can hold any code, ChatGPT runs it in a locked-down frame on a separate web address, where it cannot read the main ChatGPT page around it.

That sandbox held. The way in came from a second feature in the same conversation.

The shared chat also contained an interactive graph, and drawing it loaded a math library called MathLive into the main ChatGPT page. Loading MathLive left a listener running there that accepted messages about its on-screen keyboard.

A message passed between browser frames is safe only if the receiver checks who sent it. Parameter found that this listener accepted a keyboard message from any sender, and that the message was allowed to carry raw HTML. The Preview could then reach across the boundary and hand attacker HTML to the trusted main page.

That HTML built a new frame that the browser treated as part of chatgpt.com. A script loaded from YouTube then supplied the code that ran inside it.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEikYB9KX234zytCTLW_X4nluEXNf8q3e5kjOGQO5Fm07RpGvsrvFlpKmXp9H-gm4e0apQJNA-ADrDAdG0bVaxqyJ7ff3QxYtvjNgdM8xyLYS_iuAY-K1fh-jZPq1-8_pIiMWAFniMSXreU5Q-txcFeQH_Rrcwg37Vka97a2ApYagAzpoAsMvgG-EDV19zM/s1700-nu-rw-lo-l85-e365/ch.png)

ChatGPT's content security policy limits where a page's scripts may come from. It blocked inline code but allowed scripts from YouTube, which is why that step worked.

### What OpenAI Fixed, and What Users Should Do

Parameter said OpenAI reproduced both the code execution and the private-chat proof, raised the severity from P2 to P1, and rolled a fix across two versions of ChatGPT's web frontend. By October 26, both versions rejected the messages the attack relied on.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The researchers traced the problem to three design choices that lined up:

1. MathLive acted on a message that changed its settings without checking which frame had sent it.
2. That message was allowed to carry raw HTML as keyboard-layout data.
3. The HTML could create a frame that was not sandboxed and inherited the chatgpt.com identity.

The YouTube step was only the final workaround, not the cause. Blocking it alone would still leave an untrusted Preview able to push HTML into the main site.

ChatGPT users do not need to do anything. The fix is on OpenAI's side, with nothing to install or reset.

Parameter published its writeup on October 28, after the fix. OpenAI paid a total of $5,000 for the report.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messen...