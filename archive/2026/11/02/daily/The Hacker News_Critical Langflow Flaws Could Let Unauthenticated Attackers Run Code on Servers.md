---
title: Critical Langflow Flaws Could Let Unauthenticated Attackers Run Code on Servers
url: https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html
source: The Hacker News
date: 2026-11-02
fetch_date: 2026-11-03T08:51:45.033350
---

# Critical Langflow Flaws Could Let Unauthenticated Attackers Run Code on Servers

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

# [Critical Langflow Flaws Could Let Unauthenticated Attackers Run Code on Servers](https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html)

**Swati Khandelwal**Nov 02, 2026Vulnerability / Artificial Intelligence

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_FF2_yXQrxnB1ymo-GsohY6t0INslV7mps2DVMnYa_dD_RpZu7uz9HwNrux1gxieMF4hnc_84KMpOyhroj0EDx0Vwv0QljdhTehvJINIsr-Sjyw4CaMiLO3fFWGl-8LhLWgOtC4DRU2X5e46s3Rxghu3KLUMsyHfpxFyKogIs34Q2fm2RYpAMI_Jt_9A/s1700-nu-rw-lo-l85-e365/langflow-rce.jpg)

Two critical flaws in Langflow could let a remote attacker with no account bypass authentication or run arbitrary code, [IBM said last week](https://www.ibm.com/support/pages/security-bulletin-langflow-oss-affected-multiple-vulnerabilities-2).

Langflow is an open-source tool for building AI agents and workflows, and its vulnerability reports go to IBM. Every release from 1.0.0 through 1.12.8 has the flaws, and the only fix is version 1.13.0.

Neither flaw is in CISA's Known Exploited Vulnerabilities catalog, as of the catalog's October 30 update. Six other Langflow flaws are listed there, most recently CVE-2026-9198, which was [added in August](https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html).

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

The four Langflow flaws in IBM's bulletin, first published on October 28 and updated the next day, are:

| CVE | CVSS score (IBM) | Account needed | What IBM says it could allow |
| --- | --- | --- | --- |
| CVE-2026-93680 | 9.8 (Critical) | No | Bypassing security restrictions, because of improper authentication |
| CVE-2026-110186 | 9.8 (Critical) | No | Running arbitrary code, because of improper control of code generation |
| CVE-2026-110193 | 8.8 (High) | Yes, a low-privileged account | Making the Agentic Assistant generate or submit component code that runs operating system commands on the server |
| CVE-2026-110192 | 6.5 (Medium) | Yes | Getting sensitive information from insufficiently protected credentials |

One of the flaws is "unauthenticated remote code execution exploitable through model context protocol tool enumeration," according to IBM. Through the Model Context Protocol (MCP), Langflow can offer its flows as tools to AI apps that support MCP.

A [module in the public Metasploit Framework](https://github.com/rapid7/metasploit-framework/blob/master/modules/auxiliary/gather/langflow_auth_bypass_cve_2026_93680.rb) already cites CVE-2026-93680, the authentication bypass. It connects to a Langflow server's MCP endpoint without credentials, starts a session, and lists the tools the server offers. It does not run code or commands on the server.

Its author lists Langflow 1.5.0 through 1.11.4 as affected, a narrower range than IBM's.

When automatic login is enabled, Langflow logs users in as superusers without prompting them to sign in. The setting LANGFLOW\_AUTO\_LOGIN is enabled by default in [Langflow 1.12.8](https://github.com/langflow-ai/langflow/blob/v1.12.8/src/lfx/src/lfx/services/settings/auth.py). Its code description warns that it "bypasses authentication and should only be used in development environments."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

The module was tested on Langflow 1.8.4 with automatic login turned on. Another of the four flaws is "an incomplete remediation of an auto-login security control," according to IBM. The bulletin does not say whether servers with automatic login turned off are vulnerable.

### Upgrading to 1.13.0

[Langflow 1.13.0](https://github.com/langflow-ai/langflow/releases/tag/v1.13.0) came out on October 22. Version 1.12.8, released the same day, still has the flaws, and PyPI lists no later 1.12 release as of November 2. IBM offers no workaround for servers that cannot upgrade yet.

Langflow 1.13 turns automatic login off by default. To upgrade:

1. Back up the database, the secret key and uploaded files.
2. If the server uses automatic login, prepare the existing account for password sign-in, as [Langflow's upgrade guidance](https://docs.langflow.org/get-started-installation) describes.
3. Upgrade the Python package with pip install --upgrade "langflow==1.13.0". For Docker, move to the langflowai/langflow:1.13.0 image and keep the deployment's persistent data.
4. If you cannot sign in after upgrading, follow the recovery steps that the same guidance links to. Do not delete or reinstall Langflow to get access back, because Langflow's documentation warns this can permanently remove your flows.

On October 29, IBM also published CVE records for 29 other Langflow flaws and named versions [1.12.4](https://www.ibm.com/support/pages/node/7293015) and [1.12.5](https://www.ibm.com/support/pages/node/7293016) as their fixes. One of them, CVE-2026-104339, could also let an attacker with no account run arbitrary code, and IBM rates it 9.8. None of the 33 records, these four included, lists 1.13.0 as affected.

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

[API Security](https://thehackernews.com/search/label/API%20Security), [Application Security](...