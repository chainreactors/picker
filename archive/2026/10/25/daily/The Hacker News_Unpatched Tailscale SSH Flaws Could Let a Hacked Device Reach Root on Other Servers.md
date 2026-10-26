---
title: Unpatched Tailscale SSH Flaws Could Let a Hacked Device Reach Root on Other Servers
url: https://thehackernews.com/2026/10/unpatched-tailscale-ssh-flaws-could-let.html
source: The Hacker News
date: 2026-10-25
fetch_date: 2026-10-26T07:19:09.095604
---

# Unpatched Tailscale SSH Flaws Could Let a Hacked Device Reach Root on Other Servers

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

# [Unpatched Tailscale SSH Flaws Could Let a Hacked Device Reach Root on Other Servers](https://thehackernews.com/2026/10/unpatched-tailscale-ssh-flaws-could-let.html)

**Swati Khandelwal**Oct 25, 2026Vulnerability / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbGR63RmXInXPwCVFZlGJSiGv5WQfLTWymToOPIYbKXfXniB7X4YDbTVK-28G4r3WfdelCr_2TRzhoYrIogcG_C9WjXEHaLhURIh_v5RyO5sBY8UKwQWbKUBrv_H5n5K7N4mz2WG3d5dldw_re-M5CgDDbVi_EhTqvB9P87fZJlODojj8ivvj-RwLUhpg/s1700-nu-rw-lo-l85-e365/tailscale.jpg)

A single hacked device on a Tailscale network can be used to gain root access to other servers it can reach, according to a security researcher who published the findings this week.

The attack requires two things: Tailscale SSH set up to allow port forwarding, and an attacker who already controls one device that the network's access rules permit to connect to the target.

The findings were published on October 25 in a report called [Tailworm](https://tailworm.com/) by Erica Windisch of Cyberdione Labs. Windisch tested Tailscale version 1.104.2 and headscale version 0.29.5, the self-hosted server some networks use to run Tailscale instead of the company's hosted service, over three days in a lab.

The report describes tests on that software, not attacks against real networks. As of publication, Tailscale had issued no [security bulletin](https://tailscale.com/security-bulletins), no CVE identifier, and no fixed version.

Tailscale has responded in public. Mike Shaver, the company's vice president of engineering, [wrote on Reddit](https://www.reddit.com/r/Tailscale/comments/1xeoj1l/recent_tailscale_vulnerability_reports/) that Tailscale had received the report, had already been looking at the same areas with outside security specialists, and had found issues it is working to fix. Shaver said the company is still working out which setups are affected, and that it is "not recommending that everyone disable Tailscale SSH."

Tailscale SSH does not work like a normal SSH server. Rather than checking a connecting user's password or key, it identifies the device, and a single access rule decides whether that device may open an SSH session to a target.

Because of this, the attack needs no stolen passwords or keys. It needs a foothold on one device first, which the report says an attacker can get the usual ways: a vulnerable web application, a poisoned software package, phishing, or stolen login details. Tailscale does not create that first foothold.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-agent-methods-d)

How much an administrator can do about it depends on where the network is run. On Tailscale's hosted service, forwarding can be switched off per rule. On headscale version 0.29.5, forwarding cannot be turned off at all. The report says every SSH grant there should therefore be treated as giving root on the target.

In the lab, Windisch showed the problem in stages. Using standard SSH port forwarding, an ordinary session caused the root-level Tailscale process to connect to a system socket that only root should access, and the test gained root and read the system password file almost immediately, without administrator rights.

A second method replaced a root-owned socket with the attacker's, allowing direct root command execution against certain services.

A third method defeated a safety check meant to limit which files forwarding can access by racing the system between when it checks a file path and when it uses it. That chain went further in the lab, the report says: it captured a key used to enroll new devices and used the key to join an attacker's own machine to the network as a trusted server.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0Dt1js1YNd3wtQTOsbkw_5h8-jZyHiPuH92LFA9XMRrXMezC9VUstIywzQA3fhrVIxxV-jyojfPfURik57Gk0CRJuHTf8r9sg0eJk652Rin6gZSA_2kbtHq7Q3VXveYgytFc5BGK8PKht7UHJsrEYO1vxl9srRXNIWIRz2DalRuxo2TmNaPjmG0tLP30/s1700-nu-rw-lo-l85-e365/tailsworm.jpg)

That last step worked from start to finish only on networks where Tailscale's Tailnet Lock feature was not enabled. On networks that do, the needed secrets were captured in transit, but the final step was not completed.

Windisch describes the overall result as "wormable." In the lab, one compromised device could spread to every device that the access rules allow, with no passwords, no stolen keys, and no user action, in under a second per step.

In the report's words, "the mesh converts one ordinary foothold into fleet-wide privileged access at machine speed." That spread was measured in a lab, not seen on real networks.

The report names two things that held it back: access rules written as single source-to-destination pairs, which stopped the spread on their own, and device keys tied to hardware such as a TPM or Secure Enclave.

Some researchers who read the report have publicly questioned the "wormable" description, while others have called the root-access finding serious.

The SSH problem is one of 11 findings in the report, which also covers Tailscale's app connectors, its serve feature, the DERP relay used between devices, and headscale. Windisch told The Hacker News that the SSH privilege escalation "is worrying," but that the app connector finding "may be more impactful to some organizations." The app connector finding, in an experimental feature called conn25, lets a permitted user send traffic to destinations the security team never approved, including a cloud provider's metadata service, which can hand out server credentials.

All of the findings rest on Windisch's report alone. No other researcher has publicly reproduced them, and Tailscale has not confirmed the specific technical claims. Windisch said the proof-of-concept code behind the findings is not public, and that she provided it only to Tailscale's security contact.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/net...