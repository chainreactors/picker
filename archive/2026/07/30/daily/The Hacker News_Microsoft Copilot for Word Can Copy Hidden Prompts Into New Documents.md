---
title: Microsoft Copilot for Word Can Copy Hidden Prompts Into New Documents
url: https://thehackernews.com/2026/07/microsoft-copilot-for-word-can-copy.html
source: The Hacker News
date: 2026-07-30
fetch_date: 2026-07-31T05:31:17.379334
---

# Microsoft Copilot for Word Can Copy Hidden Prompts Into New Documents

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [Microsoft Copilot for Word Can Copy Hidden Prompts Into New Documents](https://thehackernews.com/2026/07/microsoft-copilot-for-word-can-copy.html)

**Swati Khandelwal**Jul 30, 2026Vulnerability / AI Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-BgxoTGLqXYzQh4HW0TUm-hbX0ApFizzFtFkKe5mb3fKS_yn6Zzpj_Uvivxi7VCwEUOuJx3Bg1XHpHWq9tbZh5xBrAHT4gBG2DYyqvFkVKmWIRiF_zCpXIG5bTs7HfsV1pjM2EsTm-e7WttN-iB57p0n4ki2Vs7vXyB6rTF9mSqlwPu3h7KHocg0mWcI/s1700-e365/copilot-word.jpg)

Hidden instructions in a Word document can make Microsoft 365 Copilot rewrite figures in a report, then copy the same instructions into the finished file. Håkon Måløy [disclosed the technique](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) on July 28, 144 days after reporting it to Microsoft.

In his proof of concept, the internally generated file triggered the same behavior when it was used in a second Copilot drafting session.

Måløy's timeline says Microsoft confirmed the reported behavior on March 31 and deployed two mitigations. The first blocked the original prompt wording; the second upgraded the underlying model to GPT-5.5.

He said the full chain worked with modified instructions on GPT-5.6 the next day, and the attack class still reproduced on July 28. "The vulnerability class therefore remains exploitable at the time of publication," Måløy said.

The attack is not zero-click and does not execute conventional malware. It requires a Copilot drafting or editing operation, and the malicious document must enter the model's context as an attachment or as a OneDrive source selected by Work IQ, the intelligence engine behind Microsoft 365 Copilot.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

The disclosure does not report exploitation in the wild, and Måløy withheld the complete payload. He recommends treating external documents as untrusted, reviewing attached documents before starting a generation or edit, and checking Copilot-generated or edited files before reuse or sharing.

The chain runs through document text and Copilot's own drafting behavior. Copilot reads source files to decide what belongs in a draft and can mistake [instructions inside them](https://thehackernews.com/2024/08/microsoft-fixes-ascii-smuggling-flaw.html) for part of the user's request. In the proof of concept, it halved every financial figure, copied the full prompt into the output in white, eight-point text, and disclosed neither change.

Måløy said Word strips colour and font size before sending document text to the large language model, leaving white-on-white instructions legible to the model. One part of the payload altered the document; the other told Copilot to copy and conceal the instructions, framing those commands as source-tracking and readability requirements.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4VeSC7woPhgO8VA54BbstSNtcKABtl5JyaMyZNL7RfGtrfzhzyPDUE0Dsj3CuMMl63A3RTlpxSd5XW9CsZSmUBJk8xZvqcWQ6dCvovMc0wqlzWRYcn0Wm6L1qIdCcJRVhk3orrGPcaMpxJRk44lGRfXWKaixQTkS3Pjk9Gk2cPlIHbn1eXa7vynz8HZg/s1700-e365/co.png)

Microsoft says Word can [ground a draft on up to 20 files](https://support.microsoft.com/en-us/word/copilot/draft-and-add-content-with-copilot-in-word), emails, or meetings, and [Edit with Copilot](https://support.microsoft.com/en-us/word/edit-with-copilot-in-word) can use Work IQ. Edit with Copilot is still rolling out worldwide to users with eligible licences. In Måløy's test, Copilot searched OneDrive for a quarterly report, found the malicious market analysis outside the folder containing the other sources, and included it. Work IQ still had to judge the file relevant.

With the original malicious document absent and only the infected Q1 report attached, Copilot halved the figures in a Q2 draft and appended the prompt again. The new carrier was an ordinary internally generated document. The chain does not propagate on its own: each hop requires another Copilot drafting or editing operation in which the carrier enters the model's context.

The hidden formatting is only the entry point. Once Copilot copies the instructions into an internally generated document, the original source is no longer present when that file enters the next session. Måløy argues that this break in the provenance trail makes the manipulation harder to trace.

[![Cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnP2BIJTKZ31v-Y_pyvFqC1s6LD-Bo8UNy3UHgqojpVezgaGWw5-sPe5uRK0dfSm3gmDvoKCdHoJnGx1BiTP6Y0qit7D7TCZU_LckTDpdu9eeyuelmJKndEkOxZP6oNPwzguLBCTkAnNkIEvSYaWamKLqYLrJPjnea1V_lz7UcfQkavBo2g3OEGoLyz7mD/s728-e100/sygnia-d-4.png)](https://thn.news/sygnia-webinar)

As of publication, The Hacker News found no public CVE or standalone Microsoft advisory for the Word finding in searches of NVD, CVE.org, and Microsoft's [Security Update Guide](https://msrc.microsoft.com/update-guide/). Microsoft says jailbreak and cross-prompt injection attack (XPIA) classifiers help block high-risk prompts, although they may not be available in every Copilot scenario.

[Defender for Office 365](https://learn.microsoft.com/en-us/defender-office-365/step-by-step-guides/prompt-injection-protection-defender-for-office-365) adds mail-flow inspection for inbound email. Microsoft describes Copilot's runtime safeguards as covering injected instructions from grounded content. Neither Microsoft nor Måløy says whether this exact payload is detected at either layer.

No customer-side remediation fully addresses the issue, according to Måløy. His argument is that payload-specific blocks do not reach the class: a model must process attacker-controlled content to decide whether it is malicious, so "the content being inspected participates in the act of inspection."

Microsoft made a related point in a June post about AI memory, writing that "Prompting alone is not a reliable security boundary" and that [...