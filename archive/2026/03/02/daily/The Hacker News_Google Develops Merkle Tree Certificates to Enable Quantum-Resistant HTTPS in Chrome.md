---
title: Google Develops Merkle Tree Certificates to Enable Quantum-Resistant HTTPS in Chrome
url: https://thehackernews.com/2026/03/google-develops-merkle-tree.html
source: The Hacker News
date: 2026-03-02
fetch_date: 2026-03-03T04:13:44.816968
---

# Google Develops Merkle Tree Certificates to Enable Quantum-Resistant HTTPS in Chrome

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguiZ85S7494GyqhFt9uP48C8ggEnb3bp9Qmsdv4LOYjNWfa98MKx17Dk7o1nJrEV3ai3edIGIgwt6oO5iJMmYLcyu6PojcvJnO4IfLhVK2dzGKFyEroFjKQhnp2hd5Cc6G4CynJRfb55aclnGwj7rse9jMncn_vu_tFqQZtHZH3Sb5dMXwRKN-kSVYUMzD/s1700-e365/ai-d.png)](https://thehackernews.uk/wiz-ai-security-d)

# [Google Develops Merkle Tree Certificates to Enable Quantum-Resistant HTTPS in Chrome](https://thehackernews.com/2026/03/google-develops-merkle-tree.html)

**Ravie Lakshmanan**Mar 02, 2026Cryptography / Browser Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjI7UWgA_nVAo80v0LRW4e9HTMYUIiEebPJv-EX7ssG1EVxwD-_hlvqqVzQ7Eb4mA9FWWW1U2WYmA8JPnPhyphenhyphenBWaCgFcyeEzcr0QhDRoUsPYgMqB7Ddt2_vEzEYMJj0w9Q9lb2nf12s_FoXDpql2BbxlpCo1oplXSzGjLFmqAsoW_Ix7CufTx5LiWrepwal8/s1700-e365/chrome.jpg)

Google has announced a new program in its Chrome browser to ensure that HTTPS certificates are secure against the [future risk](https://thehackernews.com/2026/01/threatsday-bulletin-new-rces-darknet.html#post-quantum-shift-accelerates) posed by [quantum computers](https://thehackernews.com/2025/02/google-cloud-kms-adds-quantum-safe.html).

"To ensure the scalability and efficiency of the ecosystem, Chrome has no immediate plan to add traditional [X.509 certificates](https://en.wikipedia.org/wiki/X.509) containing post-quantum cryptography to the [Chrome Root Store](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/root_store.md)," the Chrome Secure Web and Networking Team [said](https://security.googleblog.com/2026/02/cultivating-robust-and-efficient.html).

"Instead, Chrome, in collaboration with other partners, is developing an [evolution](https://drive.google.com/file/d/1KQXAGBHXR4S_prwFrZlyfA6DrpvfJwuJ/view) of HTTPS certificates based on [Merkle Tree Certificates](https://datatracker.ietf.org/doc/draft-ietf-plants-merkle-tree-certs/) (MTCs), currently in development in the PLANTS working group."

As Cloudflare explains, MTC is a [proposal](https://blog.cloudflare.com/bootstrap-mtc/) for the next generation of the Public Key Infrastructure (PKI) used to secure the internet that aims to reduce the number of public keys and signatures in the TLS handshake to the bare minimum required.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/xm-cyber-comm-d)

Under this model, a Certification Authority (CA) signs a single 'Tree Head' representing potentially millions of certificates, and the 'certificate' sent to the browser is a lightweight proof of inclusion in that tree, Google said.

In other words, MTCs facilitate the adoption of post-quantum algorithms without having to incur additional bandwidth associated with classical X.509 certificate chains. The approach, the company added, decouples the security strength of the corresponding cryptographic algorithm from the size of the data transmitted to the user.

"By shrinking the authentication data in a TLS handshake to the absolute minimum, MTCs aim to keep the post-quantum web as fast and seamless as today's internet, maintaining high performance even as we adopt stronger security," Google said.

The tech giant said it's already experimenting with MTCs with real internet traffic and that it plans to gradually expand the rollout in three distinct phases by the third quarter of 2027 -

* **Phase 1** (In progress) - Google is conducting a feasibility study in collaboration with Cloudflare to evaluate the performance and security of TLS connections relying on MTCs.
* **Phase 2** (Q1 2027) - Google plans to invite Certificate Transparency (CT) [Log](https://certificate.transparency.dev/logs/) operators with at least one "[usable](https://googlechrome.github.io/CertificateTransparency/log_states.html)" log in Chrome before February 1, 2026, to participate in the initial bootstrapping of public MTCs.
* **Phase 3** (Q3 2027) - Google will finalize the requirements for onboarding additional CAs into the new Chrome Quantum-resistant Root Store (CQRS) and corresponding Root Program that only supports MTCs.

"We view the adoption of MTCs and a quantum-resistant root store as a critical opportunity to ensure the robustness of the foundation of today's ecosystem," Google said. By designing for the specific demands of a modern, agile, internet, we can accelerate the adoption of post-quantum resilience for all web users.

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

[browser security](https://thehackernews.com/search/label/browser%20security), [Certificate Authority](https://thehackernews.com/search/label/Certificate%20Authority), [CloudFlare](https://thehackernews.com/search/label/CloudFlare), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Google Chrome](https://thehackernews.com/search/label/Google%20Chrome), [HTTPS](https://thehackernews.com/search/label/HTTPS), [Internet Security](https://thehackernews.com/search/label/Internet%20Security), [Post-Quantum Cryptography](https://thehackernews.com/search/label/Post-Quantum%20Cryptography), [TLS](https://thehackernews.com/search/label/TLS)

Trending News

[![Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies](data:image/svg+xml;base64... "Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies")

Researchers Show Copilot and Grok Can Be Abused as Malware C2 Proxies](https://thehackernews.com/2026/02/researchers-show-copilot-and-grok-can.html)

[![⚡ Weekly ...