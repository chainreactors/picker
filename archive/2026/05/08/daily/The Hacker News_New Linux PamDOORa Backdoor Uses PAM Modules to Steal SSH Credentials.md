---
title: New Linux PamDOORa Backdoor Uses PAM Modules to Steal SSH Credentials
url: https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html
source: The Hacker News
date: 2026-05-08
fetch_date: 2026-05-09T05:09:02.746605
---

# New Linux PamDOORa Backdoor Uses PAM Modules to Steal SSH Credentials

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyqUz0-ifa8jE9rCzud3wzxmhcuzTp1VOWFEvGMoZXDYfaB_4459fPyvyQw7wvAnzjzDL09PkyJM83QGheO69fC3esg1WA7WnJ89i_t_q3K8DxYmgV__QujU8RWRnCK4MpbKqu8nwuMFfLaiRVHy_ov7IZ16hoKI3rIu-5BcISmqXPjlQU7N0sa4lWI-n-/s728-e100/wiz-d.png)](https://thehackernews.uk/wiz-ai-state-d)

# [New Linux PamDOORa Backdoor Uses PAM Modules to Steal SSH Credentials](https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html)

**Ravie Lakshmanan**May 08, 2026Malware / Threat Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixNgyNI9ObZi3Il87CVXhEWyWgcK-O1IKhQKRs7NPrNVqTMBZRw7AZpmbk5RdsPxNPmO9IyXaq6QzYBN691HBgfE8HpwnyJuE4-vaCAwHPpb6UfeSRcrMI-GRjcX53cELs31s7ps6YkGx5bAAB67w4m9GQ7ZVWjSdnaPOFczjHlsS3967ZvBh-4ZvTBWEJ/s1700-e365/linux-pam.jpg)

Cybersecurity researchers have disclosed details of a new Linux backdoor named **PamDOORa** that's being advertised on the Rehub Russian cybercrime forum for $1,600 by a threat actor called "darkworm."

The backdoor is designed as a Pluggable Authentication Module ([PAM](https://www.redhat.com/en/blog/pluggable-authentication-modules-pam))-based post-exploitation toolkit that enables persistent SSH access by means of a magic password and specific TCP port combination. It's also capable of harvesting credentials from all legitimate users who authenticate through the compromised system.

"The tool, called PamDOORa, is a new PAM-based backdoor, designed to serve as a post-exploitation backdoor, enabling authentication to servers via OpenSSH," Flare.io researcher Assaf Morag [said](https://flare.io/learn/resources/blog/pamdoora-new-linux-pam-based-backdoor-sale-dark-web) in a technical report. "Allegedly this would remain persistent on Linux systems (x86\_64)."

PamDOORa is the second Linux backdoor targeting the PAM stack after [Plague](https://thehackernews.com/2025/08/new-plague-pam-backdoor-exposes.html). PAM is a security framework in Unix/Linux operating systems that grants system administrators the ability to incorporate multiple authentication mechanisms or update them (e.g., switching from passwords to biometrics) into an existing system through the use of pluggable modules without the need for rewriting existing applications.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

Because PAM modules typically run with [root privileges](https://www.cyberark.com/resources/endpoint-privilege-security/plague-malware-exploits-pluggable-authentication-module-to-breach-linux-systems), a compromised, misconfigured, or malicious module can introduce significant security risks and open the door to credential harvesting and unauthorized access.

"Despite its strengths, the Pluggable Authentication Module's (PAM) modularity introduces risks, as malicious modifications to PAM modules can create backdoors or steal user credentials, especially since PAM does not store passwords but transmits values in plaintext," Group-IB [noted](https://www.group-ib.com/blog/pluggable-authentication-module/) in September 2024.

"The pam\_exec module, which allows the execution of external commands, can be exploited by attackers to gain unauthorized access or establish persistent control by injecting malicious scripts into PAM configuration files."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5BOXKdu5522ta-1c7W3cJ_fo1y2eyvW_sZdnM3GAmK-aMGxsjl9SOc0qet7jxLeHrKzTjdSx2XdKlANomTIJhyphenhyphenpdHs91SusWt67CV4zAGpLfhH6GfdfQEPUZ7FoRTA3tAaYWKwq91gB93hbL77oQqr0buFJnljy9Q901n1cdiQMQRH7yQhM4ujk4ahKB4/s1700-e365/pam.jpeg)

The Singaporean security vendor also detailed how it's possible to manipulate PAM configuration for SSH authentication to execute a script via pam\_exec, effectively allowing a bad actor to obtain a privileged shell on a host and facilitate stealthy persistence.

The latest findings from Flare.io show that PamDOORa, besides enabling credential theft, incorporates anti-forensic capabilities to methodically tamper with authentication logs to erase traces of malicious activity.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Although there is no evidence that the malware has been put to use in real-world attacks, infection chains distributing the malware are likely to involve the adversary first obtaining root access to the host through some other means and deploying the PamDOORa PAM module to capture credentials and establish persistent access over SSH.

After an initial asking price of $1,600 on March 17, 2026, the "darkworm" persona has since reduced it by almost 50% to $900 as of April 9, indicating either a lack of buyer interest or an intent to accelerate a sale.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEihDVYXue_Q5wypjsWxqc5xrBRNMKtSy-yjNlfoSIDroScODB7xn3XNMWj5-OJgkBKiixywyupxpotgwylU2iqkTJf7nE72vyDQnyDTQPwtJFQf9SVCBRXw4e3F0iF4fPYCAoPYEo4KE7rr5jUTacm2RLA890S1pb3IwRSBIJt-hvIkurGcmFFhNg9_8k_I/s1700-e365/pam-1.png)

"PamDOORa represents an evolution over existing open-source PAM backdoors," Morag explained. "While the individual techniques (PAM hooks, credential capture, log tampering) are well-documented, the integration into a cohesive, modular implant with anti-debugging, network-aware triggers, and a builder pipeline places it closer to operator-grade tooling than the crude proof-of-concept scripts found in most public repositories."

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
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share...