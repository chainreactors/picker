---
title: WordPress Skimmers Evade Detection by Injecting Themselves into Database Tables
url: https://thehackernews.com/2025/01/wordpress-skimmers-evade-detection-by.html
source: The Hacker News
date: 2025-01-14
fetch_date: 2025-10-06T20:14:15.021695
---

# WordPress Skimmers Evade Detection by Injecting Themselves into Database Tables

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

# [WordPress Skimmers Evade Detection by Injecting Themselves into Database Tables](https://thehackernews.com/2025/01/wordpress-skimmers-evade-detection-by.html)

**Jan 13, 2025**Ravie Lakshmanan Payment Security / Web Security

[![WordPress Skimmers](data:image/png;base64... "WordPress Skimmers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjD_FWlRzjuW54hBslJkGN716FFQw3SgYOf7N9gPh8ctwGy7Ggf3CcjjR5E0f_VuSGQ0zidC7SofZ7YL4W5Q5qqub-QTJh-YX9qVqcNkAORnY4W4wnqqFLW9mS08F7sgB442UroQ2MMzUcWHhE4SYPt7U9Vl-60XmBytci_48b0vZ4813P0F1x1SiIRbc_6/s790-rw-e365/wordpress.png)

Cybersecurity researchers are warning of a new stealthy [credit card skimmer campaign](https://thehackernews.com/2024/06/new-credit-card-skimmer-targets.html) that targets WordPress e-commerce checkout pages by inserting malicious JavaScript code into a database table associated with the content management system (CMS).

"This credit card skimmer malware targeting WordPress websites silently injects malicious JavaScript into database entries to steal sensitive payment details," Sucuri researcher Puja Srivastava [said](https://blog.sucuri.net/2025/01/stealthy-credit-card-skimmer-targets-wordpress-checkout-pages-via-database-injection.html) in a new analysis.

"The malware activates specifically on checkout pages, either by hijacking existing payment fields or injecting a fake credit card form."

The GoDaddy-owned website security company said it discovered the malware embedded into the WordPress [wp\_options table](https://codex.wordpress.org/Database_Description#Table:_wp_options) with the option "widget\_block," thus allowing it to avoid detection by scanning tools and persist on compromised sites without attracting attention.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

In doing so, the idea is to insert the malicious JavaScript into an HTML block widget through the WordPress admin panel (wp-admin > widgets).

The JavaScript code works by checking if the current page is a checkout page and ensures that it springs into action only after the site visitor is about to enter their payment details, at which point the it dynamically creates a bogus payment screen that mimics legitimate payment processors like Stripe.

The form is designed to capture users' credit card numbers, expiration dates, CVV numbers, and billing information. Alternately, the rogue script is also capable of capturing data entered on legitimate payment screens in real-time to maximize compatibility.

The stolen data is subsequently Base64-encoded and combined with AES-CBC encryption to make it appear harmless and resist analysis attempts. In the final stage, it's transmitted to an attacker-controlled server ("valhafather[.]xyz" or "fqbe23[.]xyz").

The development comes more than a month after Sucuri [highlighted](https://blog.sucuri.net/2024/11/credit-card-skimmer-malware-targeting-magento-checkout-pages.html) a similar campaign that leveraged JavaScript malware to dynamically create fake credit card forms or extract data entered in payment fields on checkout pages.

The harvested information is then subjected to three layers of obfuscation by encoding it first as JSON, XOR-encrypting it with the key "script," and finally using Base64-encoding, prior to exfiltration to a remote server ("staticfonts[.]com").

"The script is designed to extract sensitive credit card information from specific fields on the checkout page," Srivastava noted. "Then the malware collects additional user data through Magento's APIs, including the user's name, address, email, phone number, and other billing information. This data is retrieved via Magento's customer-data and quote models."

The disclosure also follows the discovery of a financially-motivated phishing email campaign that tricks recipients into clicking on PayPal login pages under the guise of an outstanding payment request to the tune of nearly $2,200.

"The scammer appears to have simply registered an Microsoft 365 test domain, which is free for three months, and then created a distribution list (Billingdepartments1[@]gkjyryfjy876.onmicrosoft.com) containing victim emails," Fortinet FortiGuard Labs' Carl Windsor [said](https://www.fortinet.com/blog/threat-research/phish-free-paypal-phishing). "On the PayPal web portal, they simply request the money and add the distribution list as the address."

What makes the campaign sneaky is the fact that the messages originate from a legitimate PayPal address (service@paypal.com) and contain a genuine sign in URL, which allows the emails to slip past security tools.

To make matters worse, as soon as the victim attempts to login to their PayPal account about the payment request, their account is automatically linked to the email address of the distribution list, permitting the threat actor to hijack control of the account.

In recent weeks, malicious actors have also been observed leveraging a novel technique called transaction simulation spoofing to steal cryptocurrency from victim wallets.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"Modern Web3 wallets incorporate transaction simulation as a user-friendly feature," Scam Sniffer [said](https://drops.scamsniffer.io/transaction-simulation-spoofing-a-new-threat-in-web3/). "This capability allows users to preview the expected outcome of their transactions before signing them. While designed to enhance transparency and user experience, attackers have found ways to exploit this mechanism."

[![WordPress Skimmers](data:image/png;base64... "WordPress Skimmers")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQ-seLGm5YgVFyMPZOK9ag64yLrAQKt02L9SVn-BtCiWlhHquyj7aozd7cHIhW_T3jVJzVsLez5RDBmLCZ-_RkqETb0ZgOBH6yIRp_D-TdLKR23misn4m4HTt0RTQiU5XRs_X-GI_S51JokG_eB-2F8g6BAwmzC8zvQQR4c829GnuN0uBAK-3wYs827mEQ/s790-rw-e365/scam.png)

The infection chains involve taking advantage of the time gap between transaction simulation and execution, permitting attackers to set up fak...