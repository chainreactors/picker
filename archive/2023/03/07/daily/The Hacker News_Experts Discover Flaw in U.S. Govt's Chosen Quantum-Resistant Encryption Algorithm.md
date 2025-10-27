---
title: Experts Discover Flaw in U.S. Govt's Chosen Quantum-Resistant Encryption Algorithm
url: https://thehackernews.com/2023/03/experts-discover-flaw-in-us-govts.html
source: The Hacker News
date: 2023-03-07
fetch_date: 2025-10-04T08:52:10.184573
---

# Experts Discover Flaw in U.S. Govt's Chosen Quantum-Resistant Encryption Algorithm

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

# [Experts Discover Flaw in U.S. Govt's Chosen Quantum-Resistant Encryption Algorithm](https://thehackernews.com/2023/03/experts-discover-flaw-in-us-govts.html)

**Mar 06, 2023**Ravie LakshmananEncryption / Cybersecurity

[![Quantum-Resistant Encryption Algorithm](data:image/png;base64... "Quantum-Resistant Encryption Algorithm")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTeVs-6hkK26bO0mqaxPJASPH1R_C6SmrsYmz578cb9UAPQ6MsQ1Rs-QbFs_VYj2NxwwQRYH3uBEtIqShtv-knncuDInHQZm2mRzt6Xh_lmanP35XI0vYAVrmHgvc8ID4itvh0xc66rYY4k94JEt_x0wrN0uv0BF3Bno-E9Sj1simME-zXPO24n5Sc9g/s790-rw-e365/keys.png)

A group of researchers has revealed what it says is a vulnerability in a specific implementation of **CRYSTALS-Kyber**, one of the encryption algorithms chosen by the U.S. government as quantum-resistant last year.

The exploit relates to "side-channel attacks on up to the fifth-order masked implementations of CRYSTALS-Kyber in ARM Cortex-M4 CPU," Elena Dubrova, Kalle Ngo, and Joel Gärtner of KTH Royal Institute of Technology [said](https://eprint.iacr.org/2022/1713) in a paper.

CRYSTALS-Kyber is one of four post-quantum algorithms [selected](https://thehackernews.com/2022/07/nist-announces-first-four-quantum.html) by the U.S. National Institute of Standards and Technology (NIST) after a rigorous multi-year effort to identify a set of next-generation encryption standards that can withstand huge leaps in computing power.

A side-channel attack, as the name implies, involves extracting secrets from a cryptosystem through measurement and analysis of physical parameters. Some examples of such parameters include supply current, execution time, and electromagnetic emission.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The underlying idea is that the physical effects introduced as a result of a cryptographic implementation can be used to decode and deduce sensitive information, such as ciphertext and encryption keys.

One of the popular countermeasures to harden cryptographic implementations against physical attacks is [masking](https://www.iacr.org/archive/eurocrypt2013/78810139/78810139.pdf), which [randomizes](https://eprint.iacr.org/2015/359) the computation and detaches the side-channel information from the secret-dependent cryptographic variables.

"The basic principle of masking is to split each sensitive intermediate variable of the cryptographic algorithm into multiple shares using secret sharing, and to perform computations on these shares," another group of researchers [explained](https://www.iacr.org/archive/ches2016/98130170/98130170.pdf) in 2016.

"From the moment that the input is split until the shared output of the cryptographic algorithm is released, shares of the sensitive intermediate variables are never combined in a way that these variables are unmasked, i.e. the unshared sensitive variables are never revealed. Only after the calculation has finished, the shared output is reconstructed to disclose its unmasked value."

The attack method devised by the researchers involves a neural network training method called recursive learning to help recover message bits with a high probability of success.

"Deep learning-based side-channel attacks can overcome conventional countermeasures such as masking, shuffling, random delays insertion, constant-weight encoding, code polymorphism, and randomized clock," the researchers said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The researchers also developed a new message recovery method called cyclic rotation that manipulates ciphertexts to increase the leakage of message bits, thereby boosting the success rate and making it possible to extract the session key.

"Such a method allows us to train neural networks that can recover a message bit with the probability above 99% from high-order masked implementations," they added.

When reached for comment, NIST told The Hacker News that the approach does not break the algorithm itself and that the findings don't affect the standardization process of CRYSTALS-Kyber.

"Side-channel work was part of the evaluation, and will continue to be studied going forward," NIST's Dustin Moody was [quoted](https://www.insidequantumtechnology.com/news-archive/moody-researchers-didnt-break-crystals-kyber-algorithm-standards-course-unchanged/) as saying to Inside Quantum Technology (IQT) News. "It highlights the need to have protected implementations."

"There exist papers that attack pretty much every cryptographic algorithm using side-channels. Countermeasures are developed, and many of the attacks aren't realistic or practical in real-world scenarios."

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
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[encryption](https://thehackernews.com/search/label/encryption)[NIST](https://thehackernews.com/search/label/NIST)[Privacy](https://thehackernews.com/search/label/Privacy)[Quantum Computing](https://thehackernews.com/search/label/Quantum%20Computing)

[![c](data:image/svg+xml;base64...)](https://thehackernews.uk/cloud-defense)

Trending News

[![SolarWinds Releases Hotfix for Critical CVE-2025-26399 Remote Code Execution Flaw](data:image/svg+xml;base64... "SolarWi...