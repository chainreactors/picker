---
title: LiteLLM Compromised in Supply Chain Attack Delivering Credential Stealer and Backdoor
url: https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html
source: The Hacker News
date: 2026-10-21
fetch_date: 2026-10-22T06:46:42.801592
---

# LiteLLM Compromised in Supply Chain Attack Delivering Credential Stealer and Backdoor

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgpv5Y6QePil1MjgPiKuj9qVcOEzN1QdpjV55lFLD7Nyll1Wy1-rDkPzUxoUxZBjyhD74ycWms55yNl3nOcVfzpirEVdQnc0bfulwnXhfb5IAO5oii05bR8bzttfawsmnOSBqpuNre7TO6eDyDJn4FhPAsISdesN9Nsfq-7UgOE6XMHMH5tSwffhl-qhK9h/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/ai-threat-guide-d)

# [LiteLLM Compromised in Supply Chain Attack Delivering Credential Stealer and Backdoor](https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html)

**Ravie Lakshmanan**Oct 21, 2026Malware / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg-f1TsJE93kcT5Cp1wvKlnR-bCWFP9ZUZofd0PXryxRBt0B1q0-t0BaHnEJcNhy3IhRZq2fBU9fmILshSvlY-qk28TOO-f1JoBcGSRtwiC3MIV4gDxdXYzTS_ZMirtPka7UaG9Shie7kgWKzauZOwKgPvk8hHXUTFly2YXpzBuxUD20MdxBfKeXrRsIG-W/s1700-nu-rw-lo-l85-e365/litellm-hack.jpg)

The popular LiteLLM Python package has been compromised as part of a software supply chain attack that delivered a credential stealer and a backdoor, according to reports from [SafeDep](https://safedep.io/litellm-pypi-compromise-credential-stealer-backdoor/#payload-2-the-backdoor-in-sitecustomizepy), [Socket](https://socket.dev/blog/litellm-compromise), [StepSecurity](https://www.stepsecurity.io/blog/litellm-1-107-0-compromised-pypi-backdoored-wheels-credential-stealer), and [Upwind](https://www.upwind.io/feed/litellm-1-107-0-supply-chain-attack-malicious-code-found-in-pypi-package).

The compromise affects LiteLLM 1.107.0, distributed through PyPI wheels and Docker images. The Python package has since been [quarantined](https://pypi.org/project/litellm/#history) on Python Package Index (PyPI), and the malicious Docker images have been removed.

Oliver Jensen, director of security at LiteLLM, said an investigation into the incident is ongoing, and that it's still working to trace the original attack vector by which the threat actor published the malicious release.

"We have identified that the malicious actions were taken through three engineers' GitHub accounts, appearing to be by way of stolen GitHub CLI OAuth tokens," Jensen [said](https://github.com/BerriAI/litellm/issues/47826). "The threat actor used one user's account to trigger the project-releaser run, and another user's account to approve it. All tokens which were involved in this attack have been revoked."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

"We have not yet identified the mechanism by which the threat actor acquired the relevant tokens, so cannot yet assert that no further access to these GitHub accounts. As a temporary mitigation, we have removed all but one (unaffected) user from our GitHub organization."

Separately, LiteLLM said it has updated the public registries to remove any trusted links to its GitHub organization so as to prevent further publication of malicious packages.

Analysis of the malicious version shows that it's equipped to collect cloud credentials, private keys, browser data, and authentication files for AI development tools. The following wheels are affected -

* litellm-1.107.0-cp310-abi3-macosx\_10\_12\_x86\_64.whl
* litellm-1.107.0-cp310-abi3-macosx\_11\_0\_arm64.whl
* litellm-1.107.0-cp310-abi3-manylinux\_2\_28\_aarch64.whl
* litellm-1.107.0-cp310-abi3-manylinux\_2\_28\_x86\_64.whl
* litellm-1.107.0-cp310-abi3-musllinux\_1\_2\_aarch64.whl
* litellm-1.107.0-cp310-abi3-musllinux\_1\_2\_x86\_64.whl
* litellm-1.107.0-cp310-abi3-win\_amd64.whl
* litellm-1.107.0.tar.gz (No payload files, but has the tampered pyproject.toml)

"The first payload is a credential stealer that calls itself privcollect," StepSecurity said. "The second payload forks a background daemon that checks a GitHub dead drop every hour and runs whatever Python the attacker serves."

The malware is launched by Python even before LiteLLM is imported through a path file ("cook.pth"), which is designed to automatically execute code when the interpreter starts. It's worth noting that the same behavior was observed in the LiteLLM compromise that took place as part of the [TeamPCP supply chain attacks](https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html) [earlier](https://thehackernews.com/2026/08/malicious-litellm-releases-tied-to.html) this [March](https://futuresearch.ai/blog/litellm-pypi-supply-chain-attack/).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-d)

The "cook.pth" file contains a single line, "import cook," which, in turn, launches the credential collector payload. This includes harvesting cloud tokens, developer accounts and private keys, AI tooling credential JSON files, browser data associated with Chromium and Firefox, and environment variables.

The malware is also capable of targeting LiteLLM deployments with an aim to extract the proxy's saved credentials and model configuration. The collected data is packaged into a GZIP-compressed TAR archive and sent to "litellm[.]dev/healthcheck" by means of an HTTP POST request.

In addition, the malware is designed to read the contents of a text file ("domain.txt") located within a GitHub repository ("github[.]com/letters9813"), check if it holds a domain and, if so, run the same stealer, and finally run an HTTP GET request against "<domain>/codepy" and execute the response. The GitHub repository currently returns a 404 error.

Users who have downloaded the malicious version are advised to revoke and replace exposed credentials from a clean environment and pin version 1.106.2 by digest.

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
[![Facebook Messenger](...