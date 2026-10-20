---
title: Training AIs to Solve CAPTCHAs
url: https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html
source: Schneier on Security
date: 2026-10-19
fetch_date: 2026-10-20T06:53:43.082174
---

# Training AIs to Solve CAPTCHAs

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

## Training AIs to Solve CAPTCHAs

Interesting [research](https://arxiv.org/abs/2609.02393):

> **Abstract**: Vision-language models (VLMs) can solve visual CAPTCHAs without task-specific training, but the agents built on them approach every challenge from scratch. For such an agent, the hundredth instance of a familiar puzzle costs as much time and compute as the first. Specialized detectors invert the trade-off, answering in milliseconds but only for categories they were trained on. Neither improves with exposure. We study what changes when a solver improves with use. Our system pairs a fine-tuned YOLOv8 detector with an open-weight VLM behind a confidence-based router, and runs entirely from screenshots and operating-system input events, with no browser automation or DOM access. It reaches 85.4% overall and 84.2% macro accuracy across 16 classes, exceeding either component alone. Every answer VLM produces also serves as a training label, so the detector absorbs categories it was never trained for, typically after one or two encounters and without human annotation. The same loop also repairs it. A CAPTCHA operator can perturb images against the publicly released detector and drive its accuracy to 0%, but the perturbations leave VLM untouched, and its labels let the detector recover. Under a year-long simulated arms race in which the CAPTCHA operator re-crafts its perturbations each month, the solver recovers every round, and a cheap ~70%-accurate open-weight teacher hardens it as effectively as a perfect oracle. Visual CAPTCHA defenses that assume a failing bot stays failing therefore understate how quickly an adaptive solver returns.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [captchas](https://www.schneier.com/tag/captchas/)

[Posted on October 19, 2026 at 7:07 AM](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html) •
[5 Comments](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html#comments)

### Comments

Clive Robinson •
[October 19, 2026 9:49 AM](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html/#comment-459106)

@ ALL,

Training a Current LLM AI to solve a CAPTCHA should be well within it’s capabilities…

But what price the LLM usage cost compared to some 1$/Day person or a bowl of rice and beans captive in a slave compound just the right side of a totalitarian national boarder?

Also the humans tend to learn from each and every CAPTCHA that they solve. So there is a degree of equality in the arms race.

definitely a human •
[October 19, 2026 11:13 AM](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html/#comment-459108)

wait. are you saying those CAPTCHAs are actually being used to filter out bots from humans? i thought the filtering was being done beforehand with subtle metrics and the like, and that tasks like “click on all squares that contain a ukrainian gas station” were being used to compel the known humans to train vision systems.

Clive Robinson •
[October 19, 2026 1:35 PM](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html/#comment-459110)

@ Bruce,

A couple of thoughts for you, on the notion of,

“Are Current legally mandated and corporate surveillance Systems the final nail in the coffin of CAPTCHAs?”

To see why consider,

**Firstly**, will the increasingly legally required “age verification checks” remove the need for CAPTCHAs entirely?

On the assumption that the documentation for age verification would not be legally available to Current AI Systems[1]. That is the required documentation would be,

“Only for persons ‘natural’ not persons ‘legal’.”

**Secondly**, or,

“Will CAPTCHAs evolve in some way?”

Perhaps following the reasoning of the old saying,

“To err is human”

Make the CAPTCHA larger say 5×5 and have three types of photo,

1, With the requested object.
2, Without the requested object.
3, With an ambiguous object.

The VLM when full trained would only pick Type 1 pictures and get all of them in the CAPTCHA frame.

The human would check maybe a Type 2 and if designed correctly some Type 3 pictures.

The backend to the CAPTCHA system looks for a small percentage of error Type 2 and Type 3 pictures. On the assumption that too many are a bot just randomly selecting rather than a human erring.

To reduce random type AI system probing, upset the user by having three or four CAPTCHA frames in series and each gets “submitted” and then all get checked together as a group rather than “verified individually”.

Such a system could be “sold to humans” as a new anti-cybercrime “security check” rather than a “challenge to personhood”

[1] If age “verification documentation” became available to AI systems, then the whole point of age verification would fail. Further unless “officially supplied” the AI system owners and operators would clearly be guilty of some kind of fraud. I gather “US Wire Fraud” is considered as almost a piece of “no defence possible” legislation, much like “US Conspiracy” legislation.

Further if “officially supplied” documentation was made available this would be a route for “age verification” avoidance. In that a chain of Current AI systems that communicate as happens with agentic use would be able to “access and pass back” age restricted content (this can already be seen by the way Search Engines have been used to bypass “great firewalls” designed to block access to “prn” via URL examination).

Jon •
[October 19, 2026 6:14 PM](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html/#comment-459112)

Many years ago it was thought that the difference between men and machines was that human beings could write poetry, paint beautiful pictures, make lovely sculptures and all that sort of thing that wasn’t mere mass mathematics.

Nowadays, what really makes us human is the ability to identify every square that does not contain a bicycle.

And even that is being chewed away. J.

anon •
[October 19, 2026 10:18 PM](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html/#comment-459113)

That’t not important. The end result of AI being able to instantly solve CAPTCHA, RECAPTCHA, FUTURECAPTCHA, IMPOSSIBLECAPTCHA, ad nauseum is that ip addresses will end up on block lists never to be removed. At the same time, bot-writers will devise more and more feindish ways to emulate my grandmother with rheumatoid arthritis using a touch pad. At that point, it will be quicker, easier, and less expensive to call 1-800-4HITMEN, and give them the ip address.

What disgusts me is that every ISP on the planet, and off-planet, knows precisely which customers’ machines are infected, with which malware, and where it originated; however, in order to prevent their headquarters buildings and all of thei...