---
title: Detecting Multi-Stage Infection Chains Madness
url: https://blog.sekoia.io/detecting-multi-stage-infection-chains-madness/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-23
fetch_date: 2025-10-06T22:08:56.112444
---

# Detecting Multi-Stage Infection Chains Madness

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

[![logo sekoia.io blog light](data:image/svg+xml...)![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

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

[Detection Engineering](https://blog.sekoia.io/category/detection-engineering/ "Detection Engineering")
[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Detecting Multi-Stage Infection Chains Madness

[![](data:image/svg+xml...)![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/04/TDR-badge.png)](#molongui-disabled-link)

[Sekoia TDR and Erwan Chevalier](#molongui-disabled-link)
April 22 2025

0

10 minutes reading

During our daily tracking and analysis routine at **Sekoia** **TDR** team (Threat Detection & Research), we have been monitoring an attacker infrastructure internally called **“Cloudflare tunnel infrastructure to deliver multiple RATs”**.  This infrastructure is used by several actors to host malicious files and deliver remote access trojans (RAT). Several security vendors ([Forcepoint](https://www.forcepoint.com/es/blog/x-labs/asyncrat-python-trycloudflare-malware), [Fortinet](https://www.fortinet.com/blog/threat-research/purehvnc-deployed-via-python-multi-stage-loader),  [Orange](https://x.com/CERTCyberdef/status/1894733146114904465), [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/threat-actor-abuses-cloudflare-tunnels-deliver-rats)) have reported that the mentioned infrastructure  has been operational since at least February 2024, illustrating its resilience. The related infection chains relying upon that infrastructure is particularly complex, with multiple steps involved (as explained in the schema below) and some variations observed from one campaign to another.

The objectives of these campaigns require analysis by examining the entire malware chain. This analysis will not be detailed here, but the data theft objective remains probable, and consistent with most active cybercriminals intrusion sets.

This report describes one of the latest observed infection chains (delivering AsyncRAT) relying on the Cloudflare tunnel infrastructure and the attacker’s tactics, techniques and procedures (TTPs), with a principal **focus on detection opportunities**. We will illustrate how the **Sekoia** **Defend** platform detects the different steps with several detection rules that will be shared in the technical details part.

![](data:image/svg+xml...)![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXd6rxezi1jCA43dOyTMxUtBr__mqfrz1RjI5qCQT4oHPqrsAf6qNLQ7PoU3oIVLJGyua01e8uhjnXj4r_BdfXeAKuMv-NipuJI5eZbWJOnauk8Qw6BWxmiQj0IcyZ1RfFGmYYh8?key=pC8JM2yo9LhuIjRYzFYXE6Hg)

*Figure 1. Infection chains distributing AsyncRAT*

# Initial Access (email -> windows-library)

The usual initial access vector used in that campaign (and still the most prevalent when targeting employees) is a **phishing email**, often disguised as an invoice or order, attempting to deceive the recipient into opening a malicious attachment under a false sense of urgency. Some of these emails may employ a deceptive tactic by including a fabricated conversation thread with a forged reply.

![](data:image/svg+xml...)![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXemvaAkN4veNmpGN-41iasMJht1U4JOBCn5sftPebf7TpyA8A-GypMU589sEPCK1MbODO4U3DG7BXf0uAHt5B3Dz43kv1Jf2O3xRWQGhjoCL1HXfLTyFDwTKYF6lL37zt_SvkeoUw?key=pC8JM2yo9LhuIjRYzFYXE6Hg)

*Figure 2. Phishing email sample*

The attachment contained in the phishing email is an old “**application/windows-library+xml**” file type. and in the year 2025, it is not the primary method to access files over the network (we will explain why below). While this type of file is sometimes blocked at an email gateway, it is not always the case as it may be considered as a safe file format compared to binary ones.

It is possible to block this kind of malicious email using a simple Sigma rule “[Suspicious Email Attachment Received](https://github.com/SEKOIA-IO/Community/blob/main/sigma_rules/network/email_suspicious_attachment_received.yml)”. It allows us to detect this suspicious attachment. This kind of rule is trivial as we only want to detect a list of given suspicious extensions in any events related to an email and a file. Most of our telemetry hits are either true positives or false positives easy to filter out in a given customer context (mostly IT actions). As we did not initially have the “.ms-library” extension, the rule was updated following that investigation.

![](data:image/svg+xml...)![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXeuJGVMKH0nvWxoFOIV1-AQkyvPXWwn2-ZMOWpm0RNa9k344xlDde4aWRX4hqXC5KTvL-Pa8LHeFxBSwu50y-stclTccp3F8Yh4FPEeKPzqEpz53pzeyWxdchZltNa4JLobdf4bEw?key=pC8JM2yo9LhuIjRYzFYXE6Hg)

*Figure 3. Suspicious ms-library file sample*

If we look into that file content, the remote **WebDav** resource is clearly displayed and the file format is easy to detect and block eventually.

![](data:image/svg+xml...)![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXdlKAudZsDSlDsPhfOwkknsinWphp_tKXAn2LC-CjrAz729paXerMD9EjXGXt3YyQJn10z9rt6A6KtciSbY0ZG8juZfju5KvlG5Gt0bktSdZNUwlppa8qwyznC65EWnOIxQ7-QPnQ?key=pC8JM2yo9LhuIjRYzFYXE6Hg)

*Figure 4. Suspicious ms-library file sample*

Opening that file will open a warning pop-up for the user, and upon validation, it will create a network connection to the WebDav remote resource mentioned in the “url” entry, displaying the remote file.

![](data:image/svg+xml...)![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXf1xnoqobeqNwfSMeQ1ZFG2CWw0jekzNnRZFjiaDzhlXTOvaM-XO9-ubNKfVytzG3iat5S2DuCQme-cXuVgayAO0LXjE-obvuSQ6ZAidynHhDO0SkiALV4aPQS-qsfKZUizrNchxQ?key=pC8JM2yo9LhuIjRYzFYXE6Hg)

*Figure 5. Explorer Window displaying the malicious remote file*

# Execution (LNK -> HTA -> BAT -> Python)

In the first step of the execution, the deceptive tactic employed involves a **LNK file disguised as a shortcut to a PDF file**, which makes it relevant to the phishing email’s theme. LNK files are commonly used in Windows systems to create shortcuts to other files or directories. The direct download of a LNK f...