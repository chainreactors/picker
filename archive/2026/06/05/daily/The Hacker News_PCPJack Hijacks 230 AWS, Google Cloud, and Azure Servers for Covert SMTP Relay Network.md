---
title: PCPJack Hijacks 230 AWS, Google Cloud, and Azure Servers for Covert SMTP Relay Network
url: https://thehackernews.com/2026/06/pcpjack-hijacks-230-aws-google-cloud.html
source: The Hacker News
date: 2026-06-05
fetch_date: 2026-06-06T05:51:39.049355
---

# PCPJack Hijacks 230 AWS, Google Cloud, and Azure Servers for Covert SMTP Relay Network

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [PCPJack Hijacks 230 AWS, Google Cloud, and Azure Servers for Covert SMTP Relay Network](https://thehackernews.com/2026/06/pcpjack-hijacks-230-aws-google-cloud.html)

**Ravie Lakshmanan**Jun 05, 2026Threat Intelligence / Cloud Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEibu0mX9Tusu3siXFJzPskfA1ZYZ2OdRJTegsJFkffBc9cBBPGWguTUAI3PPAaFy-WIjziA9PIrMrZNVuFVNmbFhOSPLv6mMBPvjWnR-WQGBD2fvGFTJT358yWFFTxeFSS87aQ_fj30G2VdsGlBjy2KJiby4CS-k3X9FjjpyTGxljOo373cUaZKhdBvWZ_a/s1700-e365/cloud-emails.jpg)

The threat actor known as **PCPJack** has hijacked cloud servers associated with Amazon Web Services (AWS), Google Cloud, and Microsoft Azure to create a covert SMTP email relay network.

"Compromised business servers across the U.S., Europe, and Asia were quietly converted into SMTP proxies, verified for mail relay capability, and synced to a downstream consumer every five minutes," Hunt.io said in a statement. "The infrastructure was still running when we found it."

The threat intelligence company [said](https://hunt.io/blog/pcpjack-230-cloud-servers-smtp-proxy-network-sliver-chisel) it found source code, compiled binaries, deployment state logs, internet scanners, exploitation tooling, and a live Sliver configuration after the threat actor behind the operation left two open directories on a command-and-control (C2) server ("213.136.80[.]73") without any authentication.

PCPJack was [first discovered](https://thehackernews.com/2026/05/pcpjack-credential-stealer-exploits-5.html) by SentinelOne in April 2026 after it identified a credential theft framework that specifically targets cloud services, while taking steps to terminate and remove processes or artifacts associated with [TeamPCP](https://thehackernews.com/2026/06/miasma-supply-chain-attack-compromises.html), another notorious hacking group that has attracted attention in recent months for its software supply chain attacks.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Staged in one of the open directories [Sliver](https://sliver.sh/)-integrated SMTP proxy deployment toolkit, along with Chisel tunneling and proxy binaries for most Linux CPU architectures, such as AMD64, ARM64, and x86. On the victim side, the binary is dropped as a hidden dot-prefixed file and persisted at "/var/tmp/.xs."

Also found in the directories are deployer scripts designed to load the Sliver C2 client configuration and filter for Linux beacons that have checked in within the last ten minutes. Beacons are implants that periodically phone home to the C2 server at regular intervals to check in and retrieve commands.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDFM4oDWYAO7JKcLxS6IQC1lqi41moPuJEQX-yvb7vS6s-kRbcAe4Nwj2nKUKGU0XSD-VeRXaq0r42YXlRC9i1KFmSKIVmRilbLhhgbUU8Qn5EKZwKMgSZ3PfNULHup7-ljxLF5RXEyzq8hR3Q18lWRj7MpqEg3bsMUPAc88JkhTopQySSo2K6ZX2Zp9Ff/s1700-e365/proxy.png)

"Each beacon receives a SOCKS5 proxy port derived deterministically from an MD5 hash of its Sliver UUID, mapped into the range 10000-14999," Hunt.io noted. "The same beacon always maps to the same port across runs, eliminating the need for a shared port registry."

The script is also capable of running an SMTP quality gate that probes for outbound access to smtp.gmail[.]com:587. Hosts that fail this check are skipped with an exit code of zero.

"This gate defines the operation's purpose: hosts that cannot relay email have no value to this pipeline," the cybersecurity company added. "Beacons are processed in batches of 50, with a 25-minute wait after uploads and 15 minutes after execution commands, to accommodate slow-interval beacon check-ins."

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh9DG5ikWSDkde35T3pz2leiwevefWIUy_OKnwWFfNHjvCegHbawZR6jM5kF4s2CoOtgOL3wSBq70QrcAUIai7fnilxDecZQXQodzSluboMGI9-HwR1Q-8ABs8TkTStnZ_esPGwLGs1aAH_lIO1kKMT_Ue053m2tBhG7BoEo_vWoHhqMvzLNzCkPimLYLfv/s1700-e365/proxy-1.png)

Subsequent iterations of the deployer scripts have been found to remove the SMTP gate and the batching logic. Also present is a diagnostic script that selects five active beacons and tasks them each a shell command that checks for the following -

* Presence of Chisel binaries at known drop paths
* A Chisel process is running
* Disk space
* Reachability of port 9000 on the C2, and
* Presence of persistence artifacts, such as the cron entry or systemd service

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

In addition, the C2 server runs a Python script named "chisel\_verifier.py" as a persistent background daemon, which enumerates active Chisel tunnel ports via ss -tlnp every 60 seconds, tests each new port for SMTP capability, and removes failed or dropped tunnels from the active pool.

Verified proxies are enriched with exit IP address, country, and ASN via services like api.ipify[.]org and ip-api[.]com. The proxy lists are then synced every five minutes via the Secure Copy Protocol (SCP) to a separate downstream server at 38.242.204[.]245. The server is currently not accessible. The end goal of the operation remains unclear at this stage.

"The 230-node outcome is the observable result. Whether this progression reflects a single operator iterating or multiple actors sharing the same infrastructure cannot be determined from the recovered files," Hunt.io said, describing it as an opportunistic campaign.

"The verified proxy list is being synced every five minutes to that server, and someone is consuming it. Whether for spam, phishing, or something else, the infrastructure to deliver at scale was clearly running."

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read ...