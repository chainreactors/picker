---
title: Fooling a Voice Authentication System with an AI-Generated Voice
url: https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-ai-generated-voice.html
source: Schneier on Security
date: 2023-03-02
fetch_date: 2025-10-04T08:29:26.302896
---

# Fooling a Voice Authentication System with an AI-Generated Voice

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Fooling a Voice Authentication System with an AI-Generated Voice

A reporter used an AI synthesis of his own voice to [fool the voice authentication system](https://www.vice.com/en/article/dy7axa/how-i-broke-into-a-bank-account-with-an-ai-generated-voice) for Lloyd’s Bank.

Tags: [AI](https://www.schneier.com/tag/ai/), [authentication](https://www.schneier.com/tag/authentication/), [banking](https://www.schneier.com/tag/banking/), [biometrics](https://www.schneier.com/tag/biometrics/), [deepfake](https://www.schneier.com/tag/deepfake/), [fraud](https://www.schneier.com/tag/fraud/), [identification](https://www.schneier.com/tag/identification/), [spoofing](https://www.schneier.com/tag/spoofing/), [voice recognition](https://www.schneier.com/tag/voice-recognition/)

[Posted on March 1, 2023 at 7:06 AM](https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-ai-generated-voice.html) •
[20 Comments](https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-ai-generated-voice.html#comments)

### Comments

Winter •
[March 1, 2023 8:43 AM](https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-ai-generated-voice.html/#comment-418708)

That is a very active field of research:

> Concerns regarding the vulnerability of automatic speaker verification (ASV) technology against spoofing can undermine confidence in its reliability and form a barrier to exploitation. The absence of competitive evaluations and the lack of common datasets has hampered progress in developing effective spoofing countermeasures. This paper describes the ASV Spoofing and Countermeasures (ASVspoof) initiative, which aims to fill this void. Through the provision of a common dataset, protocols, and metrics, ASVspoof promotes a sound research methodology and fosters technological progress. This paper also describes the ASVspoof 2015 dataset, evaluation, and results with detailed analyses. A review of postevaluation studies conducted using the same dataset illustrates the rapid progress stemming from ASVspoof and outlines the need for further investigation.

Winter •
[March 1, 2023 9:57 AM](https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-ai-generated-voice.html/#comment-418713)

The 2021 ASVspoof challenge was about deep fakes:

‘https://www.isca-speech.org/archive/pdfs/asvspoof\_2021/yamagishi21\_asvspoof.pdf/yamagishi21\_asvspoof.pdf

> ASVspoof 2021 is the forth edition in the series of bi-annual challenges which aim to promote the study of spoofing and the design of countermeasures to protect automatic speaker verification systems from manipulation. In addition to a continued focus upon logical and physical access tasks in which there are a number of advances compared to previous editions, ASVspoof 2021 introduces a new task involving deepfake speech detection. This paper describes all three tasks, the new databases for each of them, the evaluation metrics, four challenge baselines, the evaluation platform and a summary of challenge results. Despite the introduction of channel and compression variability which compound the difficulty, results for the logical access and deepfake tasks are close to those from previous ASVspoof editions. Results for the physical access task show the difficulty in detecting attacks in real, variable physical spaces. With ASVspoof 2021 being the first edition for which participants were not provided with any matched training or development data and with this reflecting real conditions in which the nature of spoofed and deepfake speech can never be predicated with confidence, the results are extremely encouraging and demonstrate the substantial progress made in the field in recent years.

Basically, the lesson seems to be that what AI can fake, AI can detect.

Papa Loves U •
[March 1, 2023 10:26 AM](https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-ai-generated-voice.html/#comment-418714)

Just like one should treat an/any endpoint; reduce/minimize/eliminate(where possible) bells & whistles or the “attack surface” – those purdy, shiny thingies you CAN live without. Time to begin treating your automated home like an endpoint because that’s what’s become with all IoT being all over the place. Just like one of the regulars here (Clive Robinson) keeps repeating himself right here on this blog – year after year, by giving you the best advice you can possibly get (for free, mind you) – compare the risks vs. benefits (trade-offs), among other things, and go from there. Communism too works wonders in theory and on the paper…

Vesselin Bontchev •
[March 1, 2023 10:52 AM](https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-ai-generated-voice.html/#comment-418716)

Hi, this is your bank.

Your voice has been compromised, please change it. Make sure you use both high- and low-pitched sounds and at least 7 vowels.

lurker •
[March 1, 2023 12:44 PM](https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-ai-generated-voice.html/#comment-418718)

@Bruce

> A reporter used an AI synthesis of his own voice to fool the voice authentication system for Lloyd’s Bank.

A reporter used a rubber cast of his own fingerprint to fool his company’s biometric door lock.

A publicly accessible piece of biometrics was duplicated sufficiently accurately to fool a system that had not considered this a risk. What’s new here?

Security is a balance of risks and rewards. Good security is hard to do.

TimH •
[March 1, 2023 1:23 PM](https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-ai-generated-voice.html/#comment-418719)

@lurker

> What’s new here?

What isn’t new is that banks will refuse to accept a voice-validated fraud incident. Prof. Ross Anderson has published papers (and been expert witness) on banks refusing to acknowledge security flaws, and insisting against plain evidence that it were the customer wot dun it, not fraud and their responsibility.

lurker •
[March 1, 2023 3:27 PM](https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-ai-generated-voice.html/#comment-418720)

@TimH

What’s also new is that banks have abandoned centuries of insistence on face to face meetings and ink on paper documents, and are falling over themselves in a rush to be swallowed by new-fangled technology. Most are now making it impossible for a customer to present themself at an office of the bank, complete with identifying instruments, to conduct banking business. This refusal to engage with their customers must invite fraud, and transfer some of the blame onto the banks.

TimH •
[March 1, 2023 4:22 PM](https://www.schneier.com/blog/archives/2023/03/fooling-a-voice-authentication-system-with-an-...