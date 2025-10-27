---
title: GitHub accidentally exposes RSA SSH key
url: https://www.malwarebytes.com/blog/news/2023/03/github-changes-its-compromised-ssh-key
source: Over Security - Cybersecurity news aggregator
date: 2023-03-29
fetch_date: 2025-10-04T11:03:07.698842
---

# GitHub accidentally exposes RSA SSH key

[ ]

[![ThreatDown Powered by Malwarebytes](https://www.threatdown.com/wp-content/themes/mbc/images/logo-header-threatdown-horizontal.svg)](https://www.threatdown.com/)

SUPPORT

* [Nebula support](https://support.threatdown.com/hc/en-us/)
* [OneView support](https://support.threatdown.com/hc/en-us/p/oneview)

SIGN IN

* [Nebula sign in](https://cloud.threatdown.com/auth/login)
* [OneView sign in](https://oneview.threatdown.com/)
* [Partner Portal sign in](https://partners.malwarebytes.com/English/)

[ ]

## Products

< Products

* ## Products
* [Endpoint Detection & Response (EDR)](/products/endpoint-detection-and-response/)
* [Endpoint Protection](/products/endpoint-protection/)
* [Vulnerability Assessment](/products/vulnerability-assessment/)
* [Patch Management](/products/patch-management/)
* [Application Block](/products/application-block/)
* [DNS Filtering](/products/dns-filtering/)
* [Mobile Security](/products/mobile-security/)
* [Email Security](/products/email-security/)

* ## Services
* [Managed Detection & Response (MDR)](/products/managed-detection-and-response/)
* [Managed Threat Hunting](/products/managed-threat-hunting/)
* [Premium Support](/products/premium-support/)

* ## Features
* [Browser Phishing Protection](/products/browser-phishing-protection/)
* [Firewall Management](/products/firewall-management/)
* [Security Advisor](/products/security-advisor/)

* ## Platforms
* [Nebula](/products/nebula/)
* Manage your organization’s endpoint security in a single-tenant console

  [Nebula customer sign in >](https://cloud.threatdown.com/auth/login)
* [OneView](/products/oneview/)
* Provides MSPs centralized visibility and management capabilities across customer sites

  [OneView customer sign in >](https://oneview.threatdown.com/auth/login)

[ ]

## Partners

< Partners

* [Explore Partnerships](/partner-program/)
* Review program benefits, innovative technology, channel first mentality
* [Managed Service Providers](/partner-program/msp/)
* Everything MSPs need to run their business seamlessly

* [Technology Partners](/technology-integrations/)
* Explore our technology integrations
* [Resellers](/partner-program/partner-reseller/)
* Build growth, profitability, and customer loyalty

* ![](https://www.threatdown.com/wp-content/uploads/2023/11/px-center.png?w=356)
* Retain and grow your business with tools, education, and support in the partner experience center.

  [Sign in to PXC >](https://partners.threatdown.com/English/%20)

[ ]

## Resources

< Resources

* [Threat Center](/threat-center/)
* Learn about the latest threat news
* [Reports](/threat-center/reports/)
* [Threat Detections](/threat-detections/)
* [Executive POV](/threat-center/executive-pov/)
* [Glossary](/glossary/)
* [Blog](/blog/)

* [Resource Center](/resources/)
* Learn more about ThreatDown
* [ThreatDown News](/press/)
* [Case Studies](/resources/categories/case-studies/)
* [Reviews](/resources/categories/products/)
* [Cybersecurity Tips & Tricks](/resources/categories/cybersecurity-tips-tricks/)
* [Webinars](/resources/categories/webinars/)
* [About Us](/about-us/)

* ![2025 State of Ransomware: Inside a record-breaking year of ransomware attacks](https://www.threatdown.com/wp-content/uploads/2025/08/2025-state-of-ransomware.png?w=1246)
* Discover a record-breaking year of attacks where ransomware became decentralized and unpredictable, spreading further than ever before.

  [Download now >](https://www.threatdown.com/dl-state-of-ransomware-2025/)

[Pricing](/pricing/)

[ ]

## Why ThreatDown

< Why ThreatDown

* ## Why ThreatDown
* [About Us](/about-us/)
* [ThreatDown vs. Competition](/vs/)
* [Case Studies](/resources/categories/case-studies/)

* ![](https://www.threatdown.com/wp-content/uploads/2025/04/product-of-the-year-nav.png?w=712)
* ThreatDown named Product of the Year by MRG Effitas.

  [Learn more >](https://www.threatdown.com/blog/product-of-the-year/)

[Get a quote](/custom-quote/)

[Buy now](/pricing/)

[Home](/)
>
[Blog](/blog/)

![GitHub logo](https://www.threatdown.com/wp-content/uploads/2024/04/github_accidentally_exposes_rsa_resized.png?w=1024)

[Threat Intelligence](https://www.threatdown.com/blog/category/threat-intelligence/)

# GitHub accidentally exposes RSA SSH key

March 27, 2023

[Pieter Arntz](https://www.threatdown.com/blog/author/parntzmalwarebytes-com/)

Late last week, GitHub tweeted that it had replaced its RSA SSH “out of an abundance of caution,” after accidentally exposing the key on a publicly accessible repository.

![](https://www.threatdown.com/wp-content/uploads/2024/05/easset_upload_file65262_262604_e.webp)

How the accidental exposure managed to happen is unknown, but it means that anyone that happened to notice it and was able to copy the key could impersonate GitHub or eavesdrop on Git operations over SSH.

SSH (Secure Shell) keys are access credentials that are used in the SSH protocol and they are instrumental for the safe use of platforms such as GitHub, which is used for storing, tracking, and collaborating on software projects. The SSH protocol is widely used to login remotely from one system into another, and its strong encryption makes it ideal to carry out tasks such as issuing remote commands and remotely managing network infrastructure and other vital system components.

An RSA key pair includes a private and a public key. The RSA private key is used to generate digital signatures, and the RSA public key is used to verify digital signatures. GitHub.com’s RSA SSH private key was the one that was, briefly, exposed in a public GitHub repository.

## What do GitHub users need to do?

If you are using GitHub’s [ECDSA or Ed25519 keys](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints), you won’t notice any change and no action is required. If you receive a warning that starts by saying that the remote host identification has changed, you’ll need to remove the old key by running this command:

`$ ssh-keygen -R github.com`

Then, you can manually add the following line to add the new RSA SSH public key entry to your `~/.ssh/known_hosts` file:

`github.com ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCj7ndNxQowgcQnjshcLrqPEiiphnt+VTTvDP6mHBL9j1aNUkY4Ue1gvwnGLVlOhGeYrnZaMgRK6+PKCUXaDbC7qtbW8gIkhL7aGCsOr/C56SJMy/BCZfxd1nWzAOxSDPgVsmerOBYfNqltV9/hWCqBywINIR+5dIg6JTJ72pcEpEjcYgXkE2YEFXV1JHnsKgbLWNlhScqb2UmyRkQyytRLtL+38TGxkxCflmO+5Z8CSSNY7GidjMIZ7Q4zMjA2n1nGrlTDkzwDCsw+wqFPGQA179cnfGWOWRVruj16z6XyvxvjJwbz0wQZ75XK5tKSb7FNyeIEs4TT4jk+S4dhPeAUC5y+bDYirYgM4GC7uEnztnZyaVWQ7B381AK4Qdrwt51ZqExKbQpTUNn+EjqoTwvqNj4kqx5QUCI0ThS/YkOxJCXmPUWZbhjpCg56i+2aB6CmK2JGhn57K5mj0MNdBXA4/WnwH6XoPWJzK5Nyu2zB3nAZp+S5hpQs+p1vN1/wsjk=`

Alternatively you can automatically update GitHub.com’s RSA SSH key in your `~/.ssh/known_hosts`, by running the following in your terminal:

`$ ssh-keygen -R github.com`

`$ curl -L https://api.github.com/meta | jq -r '.ssh_keys | .[]' | sed -e 's/^/github.com /' >> ~/.ssh/known_hosts`

You can verify that your hosts are connecting via our new RSA SSH key by confirming that you see the following fingerprint:

`SHA256:uNiVztksCsDhcc0u9e8BujQXVUpKZIDTMczCvj3tD2s`

For more information, please visit the official [documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints) on GitHub’s SSH public key fingerprints, or follow the more elaborate instructions in the [article about the update](https://github.blog/2023-03-23-we-updated-our-rsa-ssh-host-key/).

## Categories

[Breaches](https://www.threatdown.com/blog/category/breaches/)[Product News](https://www.threatdown.com/blog/category/product-news/)[Ransomware](https://www.threatdown.com/blog/category/ransomware/)[Threat Intelligence](https://www.threatdown.com/blog/category/threat-intelligence/)[Vulnerabilities](https://www.threatdown.com/blog/category/vulnerabilities/)

[![X (formerly Twitter)](https://www.threatdown.com/wp-content/themes/mbc/images/x-logo....