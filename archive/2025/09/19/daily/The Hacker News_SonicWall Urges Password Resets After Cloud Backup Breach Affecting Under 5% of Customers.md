---
title: SonicWall Urges Password Resets After Cloud Backup Breach Affecting Under 5% of Customers
url: https://thehackernews.com/2025/09/sonicwall-urges-password-resets-after.html
source: The Hacker News
date: 2025-09-19
fetch_date: 2025-10-02T20:23:41.790082
---

# SonicWall Urges Password Resets After Cloud Backup Breach Affecting Under 5% of Customers

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

# [SonicWall Urges Password Resets After Cloud Backup Breach Affecting Under 5% of Customers](https://thehackernews.com/2025/09/sonicwall-urges-password-resets-after.html)

**Sep 18, 2025**Ravie LakshmananData Breach / Network Security

[![SonicWall Urges Password Resets](data:image/png;base64... "SonicWall Urges Password Resets")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi6DuAOeSPPKaTtfFkphJnx31HWv2K4Y1c_lE-JaYDRAKekoUTLLYiAh-A38ZTiRmpFisp_R39ajqwFpGc_27G_wnR-YQ09FpJ2CJSGc4sI_0ruO3l_BCHJqzFjAeOimCWFp8nUTVbjurA3Ip8Xnff68KE7sH2McLp66iAcOsvOQwe2rZaopi0iNn4IYCgv/s790-rw-e365/sonicwall.jpg)

SonicWall is urging customers to reset credentials after their firewall configuration backup files were exposed in a security breach impacting MySonicWall accounts.

The company said it recently detected suspicious activity targeting the cloud backup service for firewalls, and that unknown threat actors accessed backup firewall preference files stored in the cloud for less than 5% of its customers.

"While credentials within the files were encrypted, the files also included information that could make it easier for attackers to potentially exploit the related firewall," the company [said](https://www.sonicwall.com/support/knowledge-base/mysonicwall-cloud-backup-file-incident/250915160910330).

The network security company said it's not aware of any of these files being leaked online by the threat actors, adding it was not a ransomware event targeting its network.

"Rather this was a series of brute-force attacks aimed at gaining access to the preference files stored in backup for potential further use by threat actors," it noted. It's currently not known who is responsible for the attack.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

As a result of the incident, the company is [urging](https://www.sonicwall.com/support/knowledge-base/essential-credential-reset/250909151701590) customers to follow the steps below -

* Login to MySonicWall.com and verify if cloud backups are enabled
* Verify if affected serial numbers have been flagged in the accounts
* Initiate containment and remediation procedures by limiting access to services from WAN, turning off access to HTTP/HTTPS/SSH Management, disabling access to SSL VPN and IPSec VPN, reset passwords and TOTPs saved on the firewall, and review logs and recent configuration changes for unusual activity

In addition, affected customers have also been [recommended](https://www.sonicwall.com/support/knowledge-base/remediation-through-updated-preferences-file/250916134841513) to import fresh preferences files provided by SonicWall into the firewalls. The new preferences file includes the following changes -

* Randomized password for all local users
* Reset TOTP binding, if enabled
* Randomized IPSec VPN keys

"The modified preferences file provided by SonicWall was created from the latest preferences file found in cloud storage," it said. "If the latest preferences file does not represent your desired settings, please do not use the file."

The disclosure comes as threat actors affiliated with the Akira ransomware group have [continued](https://thehackernews.com/2025/09/sonicwall-ssl-vpn-flaw-and.html) to target unpatched SonicWall devices for obtaining initial access to target networks by exploiting a year-old security flaw (CVE-2024-40766, CVSS score: 9.3).

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Earlier this week, cybersecurity company Huntress detailed an [Akira ransomware incident](https://thehackernews.com/2025/08/sonicwall-investigating-potential-ssl.html) involving the exploitation of SonicWall VPNs in which the threat actors leveraged a plaintext file containing recovery codes of its security software to bypass multi-factor authentication (MFA), suppress incident visibility, and attempt to remove endpoint protections.

"In this incident, the attacker used exposed Huntress recovery codes to log into the Huntress portal, close active alerts, and initiate the uninstallation of Huntress EDR agents, effectively attempting to blind the organization's defenses and leave it vulnerable to follow-on attacks," researchers Michael Elford and Chad Hudson [said](https://www.huntress.com/blog/dangers-of-storing-unencrypted-passwords).

"This level of access can be weaponized to disable defenses, manipulate detection tools, and execute further malicious actions. Organizations should treat recovery codes with the same sensitivity as privileged account passwords."

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

[Cloud security](https://thehackernews.com/search/label/Cloud%20security)[cybersecurity](https://thehackernews.com/search/label/cybersecurity)[data breach](https://thehackernews.com/search/label/data%20breach)[Firewall Security](https://thehackernews.com/search/label/Firewall%20Security)[Huntress](https://thehackernews.com/search/label/Huntress)[network security](https://thehackernews.com/search/label/network%20security)[ransomware](https://thehackernews.com/search/label/ransomware)[Sonicwall](https://thehackernews.com/search/label/Sonicwall)[VPN Security](https://thehackernews.com/search...