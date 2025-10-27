---
title: Apple Opens PCC Source Code for Researchers to Identify Bugs in Cloud AI Security
url: https://thehackernews.com/2024/10/apple-opens-pcc-source-code-for.html
source: The Hacker News
date: 2024-10-26
fetch_date: 2025-10-06T18:56:50.797366
---

# Apple Opens PCC Source Code for Researchers to Identify Bugs in Cloud AI Security

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
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

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Apple Opens PCC Source Code for Researchers to Identify Bugs in Cloud AI Security](https://thehackernews.com/2024/10/apple-opens-pcc-source-code-for.html)

**Oct 25, 2024**Ravie LakshmananCloud Security / Artificial Intelligence

[![Cloud AI Security](data:image/png;base64... "Cloud AI Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8cEyTUk5tvIVjDP-mtuOK5vSR7s3-zmo7-Vs7Cg1tGl0VnBgwrXQK36sFvxL5kCJUm9nwGbdtXsN14BZ52WTEJta1GV_iWK61s3wjfQ5ezuciiiI_xUTDSPU2iYhR3aGFfyHDr6r9RSQBwsD2oTuiTZCp2BpVdU9VCHkKXjnYE3bNOxCLTba4w3u_Clii/s790-rw-e365/apple.png)

Apple has publicly made available its Private Cloud Compute (PCC) Virtual Research Environment (VRE), allowing the research community to inspect and verify the privacy and security guarantees of its offering.

PCC, which Apple [unveiled](https://thehackernews.com/2024/06/apple-integrates-openais-chatgpt-into.html) earlier this June, has been marketed as the "most advanced security architecture ever deployed for cloud AI compute at scale." With the new technology, the idea is to offload computationally complex Apple Intelligence requests to the cloud in a manner that doesn't sacrifice user privacy.

Apple [said](https://security.apple.com/blog/pcc-security-research/) it's inviting "all security and privacy researchers — or anyone with interest and a technical curiosity — to learn more about PCC and perform their own independent verification of our claims."

To further incentivize research, the iPhone maker said it's expanding the Apple Security Bounty program to include PCC by offering monetary payouts ranging from $50,000 to $1,000,000 for security vulnerabilities identified in it.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

This includes flaws that could allow execution of malicious code on the server, as well as exploits capable of extracting users' sensitive data, or information about the user's requests.

The VRE aims to offer a suite of tools to help researchers carry out their analysis of PCC from the Mac. It comes with a virtual Secure Enclave Processor (SEP) and leverages built-in macOS support for paravirtualized graphics to enable inference.

Apple also said it's making the source code associated with some components of PCC [accessible via GitHub](https://github.com/apple/security-pcc) to facilitate a deeper analysis. This includes CloudAttestation, Thimble, splunkloggingd, and srd\_tools.

"We designed Private Cloud Compute as part of Apple Intelligence to take an extraordinary step forward for privacy in AI," the Cupertino-based company said. "This includes providing verifiable transparency – a unique property that sets it apart from other server-based AI approaches."

The development comes as broader research into generative artificial intelligence (AI) continues to uncover novel ways to jailbreak large language models (LLMs) and produce unintended output.

[![Cloud AI Security](data:image/png;base64... "Cloud AI Security")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgtrMtmUduNfnPe2JsBIBPru-JZi_YM6dW8lW0JTTroN262cdcRU0AlGnSw0ouxSH_XNroisg2NmSxh4vMu2jTxJBL-8Kwfm4sKd0rMGOq4R7bvxz5kEM-svVAaNfciPlBA3HTDHexaWaQrMAQ49bWq2GUUoDbEqls1UuwytaY0Q5m1QCWXaYyBJO8sphZP/s790-rw-e365/apple.png)

Earlier this week, Palo Alto Networks detailed a technique called [Deceptive Delight](https://thehackernews.com/2024/10/researchers-reveal-deceptive-delight.html) that involves mixing malicious and benign queries together to trick AI chatbots into bypassing their guardrails by taking advantage of their limited "attention span."

The attack requires a minimum of two interactions, and works by first asking the chatbot to logically connect several events – including a restricted topic (e.g., how to make a bomb) – and then asking it to elaborate on the details of each event.

Researchers have also demonstrated what's called a ConfusedPilot attack, which targets Retrieval-Augmented Generation ([RAG](https://aws.amazon.com/what-is/retrieval-augmented-generation/)) based AI systems like Microsoft 365 Copilot by poisoning the data environment with a seemingly innocuous document containing specifically crafted strings.

"This attack allows manipulation of AI responses simply by adding malicious content to any documents the AI system might reference, potentially leading to widespread misinformation and compromised decision-making processes within the organization," Symmetry Systems [said](https://www.symmetry-systems.com/blog/confused-pilot-attack/).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Separately, it has been found that it's possible to tamper with a machine learning model's [computational graph](https://pytorch.org/blog/computational-graphs-constructed-in-pytorch/) to plant "codeless, surreptitious" backdoors in pre-trained models like ResNet, YOLO, and Phi-3, a technique codenamed ShadowLogic.

"Backdoors created using this technique will persist through fine-tuning, meaning foundation models can be hijacked to trigger attacker-defined behavior in any downstream application when a trigger input is received, making this attack technique a high-impact AI supply chain risk," HiddenLayer researchers Eoin Wickens, Kasimir Schulz, and Tom Bonner [said](https://hiddenlayer.com/research/shadowlogic/).

"Unlike standard software backdoors that rely on executing malicious code, these backdoors are embedded within the very structure of the model, making them more challenging to detect and mitigate."

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
[**...