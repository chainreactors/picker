---
title: Targeted supply chain attack against Chrome browser extensions
url: https://blog.sekoia.io/targeted-supply-chain-attack-against-chrome-browser-extensions/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-23
fetch_date: 2025-10-06T20:13:21.200555
---

# Targeted supply chain attack against Chrome browser extensions

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Targeted supply chain attack against Chrome browser extensions

On 26 December 2024, the data security company Cyberhaven informed its users about a compromise of their Chrome browser extension. The attacker exploited the extension developer's permissions, which had been previously gained through a...

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/04/logo-sekoia-symbol-6.png)](#molongui-disabled-link)

[Quentin Bourgue and Sekoia TDR](#molongui-disabled-link)
January 22 2025

0

18 minutes reading

## Table of contents

* [Context](#h-context)
* [Supply chain attack overview](#h-supply-chain-attack-overview)
  + [Targeted phishing attacks against the extension developers](#h-targeted-phishing-attacks-against-the-extension-developers)
  + [Compromised extensions](#h-compromised-extensions)
  + [Extensions’ malicious code](#h-extensions-malicious-code)
* [Adversary’s infrastructure](#h-adversary-s-infrastructure)
  + [Phishing domains for initial access](#h-phishing-domains-for-initial-access)
  + [Command & Control infrastructure](#h-command-amp-control-infrastructure)
  + [Attacker’s domain names](#h-attacker-s-domain-names)
* [Conclusion](#h-conclusion)
* [Remediation](#h-remediation)
* [IoCs & Technical details](#h-iocs-amp-technical-details)
* [MITRE ATT&CK](#h-mitre-att-amp-ck)
* [External references](#h-external-references)

## Context

On 26 December 2024, the data security company Cyberhaven informed its users about a compromise of their Chrome browser extension. The **attacker exploited the extension developer’s permissions**, which had been previously **gained through a targeted phishing attack, to upload a malicious version of Cyberhaven to the Chrome Web Store**.

Investigations into the adversary’s infrastructure revealed that during December 2024, the threat actor **compromised a dozen Chrome extensions, potentially affecting hundreds of thousands of end users**. The malicious code injected into these **compromised extensions aimed to harvest sensitive data from users’ web browsers**. The targeted data include API keys, session cookies, and other authentication tokens from websites such as **ChatGPT and Facebook for Business**.

After reporting this supply chain attack to the developers of the compromised extensions, Sekoia analysts were able to retrieve the initial phishing emails. This enabled us to **understand the entire attack and uncover an infrastructure used by the attacker** since at least 2023, and possibly even earlier.

This blog post provides an overview of the supply chain attack, detailing the targeted phishing attacks and the malicious code added to the compromised extensions. Additionally, it shares insights into the adversary’s infrastructure, as well as recommendations for remediation and Indicator of Compromise (IoCs).

*This blog post was originally sent to our clients on 10 January 2025.*

## Supply chain attack overview

The following analysis focuses on the two parts of the uncovered supply chain campaign:

* The spearphishing emails targeting Chrome extension developers, successfully compromising dozens of them since mid-November 2024.

* The compromise of approximately a dozen Chrome extensions since early December 2024, allegedly infecting hundreds of thousands of extensions’ users.

Sekoia analysts assess with high confidence that during 2023 and 2024, the threat actor conducted additional campaigns targeting Chrome extensions, using similar techniques, along with additional ones. The section below provides an analysis of the most recent campaign, which was active until 30 December 2024.

### Targeted phishing attacks against the extension developers

To gain the necessary permissions to publish new versions of legitimate extensions on the Chrome Web Store, the threat actor sent phishing emails to the developers, attempting to persuade them to authorise access to a malicious OAuth Google application.

![Phishing email about a fake violation related to the Chrome extension.](data:image/svg+xml...)![Phishing email about a fake violation related to the Chrome extension.](https://lh7-qw.googleusercontent.com/docsz/AD_4nXetdRLQU7QfRtSk3pWce5aSNIkDPmMlMIXydj1wecVOnJEyCwmubc23byIsTigitHVeu-nLEaJyzQfvfFIIoElY29XNzFvDaFueH1q3wU9HfXMh73mi03IiFEQ9SEAVxf4clvx1?key=o2TctMSFqDAnMJuTcehnkkuS)

*Figure 1.* *Phishing email claiming a fake violation related to a Chrome extension, targeted at the extension developers (source: Sekoia)*

The phishing emails had the following characteristics:

* **Email subjects**:
  + *Action Request: <EXTENSION NAME> requires the use of a developer account to accept the Chrome Web Store policy*
  + *Action Required: <EXTENSION NAME> Requires Changes to Comply with Chrome Web Store Policy*

* **Sender email addresses**:
  + *chromewebstore-noreply[@]chromeforextension[.]com*
  + *chromewebstore-noreply[@]supportchromestore[.]com*

* **Display name**:
  + *Webstore Extension*

Of note, it is highly likely that the attacker gathered the developers’ email addresses from the extension pages on the Chrome Web Store, as this information is publicly available.

Clicking on the “*Go To Policy*” button redirects to the adversary’s infrastructure, for example:

* *hxxps://app.checkpolicy[.]site/extension-privacy-policy?e=victime[@]example[.]com*
* *hxxps://app.checkpolicy[.]site/accept-terms-policy?e=victim[@]example[.]com*

These URLs redirect to a legitimate Google Accounts webpage, where victims are asked to allow the malicious OAuth application access to their Google account.

![Malicious OAuth application “Privacy Policy Extension” requesting access to update the Chrome Web Store extensions (Source: Cyberhaven).](data:image/svg+xml...)![Malicious OAuth application “Privacy Policy Extension” requesting access to update the Chrome Web Store extensions (Source: Cyberhaven).](https://lh7-qw.googleusercontent.com...