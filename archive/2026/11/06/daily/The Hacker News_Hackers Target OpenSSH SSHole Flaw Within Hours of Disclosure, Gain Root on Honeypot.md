---
title: Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot
url: https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html
source: The Hacker News
date: 2026-11-06
fetch_date: 2026-11-07T08:02:13.599925
---

# Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Hackers Target OpenSSH SSHole Flaw Within Hours of Disclosure, Gain Root on Honeypot](https://thehackernews.com/2026/11/hackers-exploited-openssh-sshole-flaw.html)

**Ravie Lakshmanan**Nov 06, 2026Vulnerability / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjHbl1TAGj_ZHZDF3oQ8AfebRDiovg_d8Wk4huY5VJkSa0csE45G7k5jwdG1De-W-7l2RjnyH_ZvT3vcioykVeOooifwvViM8RiuTu0gSt2t-XgOefyYKyM5_zbsI5WFNubkIT0hOUr4inPIQMvXs6GDTLa6j7XWL3etRJYvOcDLJxa3IDXv-KtuCma5JsG/s1700-nu-rw-lo-l85-e365/ssh.jpg)

Threat actors are attempting to exploit a [recently disclosed security flaw](https://thehackernews.com/2026/11/openssh-issues-emergency-fix-for-flaw.html) impacting OpenSSH that can enable sign-ins to accounts that have no password set, according to [Previdian](https://previdian.com/CVE-2026-123158#telemetry).

The vulnerability, tracked as **[CVE-2026-123158](https://nvd.nist.gov/vuln/detail/cve-2026-123158)** (CVSS score: 8.1) and codenamed SSHole (or \*sshole), impacts Linux systems that run OpenSSH on the musl C library with Pluggable Authentication Modules (PAM) disabled, including Alpine Linux's default OpenSSH server configuration.

An [unauthenticated attacker](https://www.ox.security/blog/openssh-authentication-bypass-cve-2026-123158/) can supply an oversized password to access accounts that are deliberately configured without usable passwords, without having to steal credentials or SSH keys. The issue, [discovered](https://sshhole.com/) by security researcher Ozgun Kultekin, has been addressed in [OpenSSH 10.6p2](https://www.openssh.org/releasenotes.html#10.6p2).

The underlying issue dates back to a patch introduced in 2016 to fix a username enumeration vulnerability tracked as [CVE-2016-6210](https://seclists.org/fulldisclosure/2016/Jul/51). Under specific conditions, the password-handling behavior in OpenSSH mistakenly interprets a failed password-hashing operation as successful authentication by producing the same value ("\*") used to indicate that an account with password disabled at the system level.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

An attacker can trigger the vulnerability to authenticate to certain password-disabled accounts using an arbitrary password between 257 and 1,024 bytes long, causing the hash attempt to fail and returning an asterisk. The sshd daemon then compares with the asterisk stored in the account's password field, leading to a successful login.

To be clear, successful exploitation requires at least one account with an asterisk (\*) as its password hash. It does not allow attackers to bypass passwords on accounts with valid password hashes.

"A successful SSHole attack grants access with the compromised account's existing permissions," Safe Security [said](https://safe.security/resources/blog/sshole-high-severity-openssh-vulnerability-turns-disabled-passwords-into-unauthorized-access/). "For enterprise, the consequences of SSHole depend on the privileges of the compromised account."

"While unauthorized SSH access is the immediate impact, attackers may also gain access to deployment credentials, application secrets, and connected infrastructure, potentially enabling lateral movement or service disruption."

|  |
| --- |
| [![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjnG6pBiv0H00uhTTHwD3JHT9Ydeo-S8dKg1VhX4a7q5Nk3Yz6DwVOCwsvhRaMygTXYG2ezH4GSKL9NNImsT5MbI5X7xBiQ2FJG0yShZsVlztKzXrVin5JEKmK4el243T13b4HhzJ5UsNh6PG8voWTrzW4ONKjSECRZq5Po-3mkDqTwGC_8muuekPOOG14r/s1700-nu-rw-lo-l85-e365/safe.jpg) |
| Image Source: Safe Security |

It's worth noting that the vulnerability [does not affect](https://socradar.io/blog/sshole-openssh-password-bypass-alpine/) Dropbear, glibc-based Linux distributions, non-Linux systems, and systems that check passwords through PAM.

Threat intelligence firm Previdian said it observed the first exploitation attempt less than nine hours after the CVE publication, adding it has confirmed successful root access on a honeypot running Alpine Linux and OpenSSH. Telemetry data shows a total of eight exploitation attempts from an IP address geolocated to Japan.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

"The observed source IP, 89.116.89[.]18, used oversized passwords to bypass authentication and ran reconnaissance commands including id, uname and hostname through non-interactive SSH sessions," Ryan Dewhurst, founder and CEO of Previdian, said in a statement shared with The Hacker News.

Affected users are advised to install OpenSSH 10.6p2 or their distribution's patched package, and then restart sshd. Alpine is also recommending that users investigate "Accepted password for" log entries involving accounts that should not accept password logins.

"Look in /var/log/messages for sshd lines reading Accepted password for an account that has no password (alpine, root, or any key-only user)," Alpine [said](https://alpinelinux.org/posts/2026-11-05-openssh-password-authentication-bypass/). "Review doas use and recently created users, files and authorized keys on exposed machines. If you cannot rule out a login, treat the machine as compromised."

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
[![Facebook Messeng...