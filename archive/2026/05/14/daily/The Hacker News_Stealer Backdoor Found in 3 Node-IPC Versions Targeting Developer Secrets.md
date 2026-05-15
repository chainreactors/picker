---
title: Stealer Backdoor Found in 3 Node-IPC Versions Targeting Developer Secrets
url: https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html
source: The Hacker News
date: 2026-05-14
fetch_date: 2026-05-15T05:53:27.647024
---

# Stealer Backdoor Found in 3 Node-IPC Versions Targeting Developer Secrets

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

# [Stealer Backdoor Found in 3 Node-IPC Versions Targeting Developer Secrets](https://thehackernews.com/2026/05/stealer-backdoor-found-in-3-node-ipc.html)

**Ravie Lakshmanan**May 14, 2026Developer Security / Supply Chain Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhTj2m9-HHmDEDzKIsalsJ_HJcwcUsIFajvcpTLP9QMyqS9F_JroTH7lXeOGZFuO6j6F-RzbIo1kBIQ0udSFQGzjN2hxO8ZfyFeHM5557BPI1sjiJ7cEMJJE62t11e07Wt1CsmAntpLHSM0XbnQDvVYNBfNdAOsob9kN6G6-mQjKX68fEE1nzy_Bn4TvxyK/s1700-e365/node.jpg)

Cybersecurity researchers are sounding the alarm about what has been described as "malicious activity" in newly published versions of node-ipc.

According to [Socket](https://socket.dev/blog/node-ipc-package-compromised) and [StepSecurity](https://www.stepsecurity.io/blog/node-ipc-npm-supply-chain-attack), three different versions of the npm package have been [confirmed](https://socket.dev/supply-chain-attacks/node-ipc) as malicious -

* node-ipc@9.1.6
* node-ipc@9.2.3
* node-ipc@12.0.1

"Early analysis indicates that node-ipc@9.1.6, node-ipc@9.2.3, and node-ipc@12.0.1 contain obfuscated stealer/backdoor behavior," Socket said.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/threatlabz-vpn-risk-2026-d)

"The malware appears to fingerprint the host environment, enumerate and read local files, compress and chunk collected data, wrap the payload in a cryptographic envelope, and attempt exfiltration through a network endpoint selected via DNS/address logic."

StepSecurity said the heavily obfuscated payload is triggered when the package is required at runtime, and attempts to exfiltrate a broad set of developer and cloud secrets to an external command-and-control (C2) server.

This includes 90 categories of credentials, including Amazon Web Services, Google Cloud, Microsoft Azure, SSH keys, Kubernetes tokens, GitHub CLI configs, Claude AI and Kiro IDE settings, Terraform state, database passwords, shell history, and more. The harvested data is then compressed into a GZIP archive and transmitted to the "sh.azurestaticprovider[.]net" domain.

The three versions were published by an account named "atiertant," which has no connection to the package's original author, "riaevangelist." Although "atiertant" appears in the maintainer list, the account has no prior publish history in connection with the node-ipc package. The previous update to the package was in August 2024.

The fact that the dormant, high-download package was compromised after a 21-month gap indicates that either the "atiertant" credentials were newly compromised, or the account was specifically added as a maintainer to publish the malicious versions.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhp05lNxaTERDFeGVPrSYe7Q7FEASNwPhlfBhLBPC81Wq_QowfGeao1GQ1Le2DYub9GTYGcjTqxH7swDfmiTcTrle4HCAC1wXfVv1N2NSpXBVXBHmgw28T9wS9WJ2D4GXhl2uOJj49fG6Tde1KmtMHIKYGXrGBxgoqvULUZHQ4KQmyweFCBBG7Pr3rS7oIo/s1700-e365/chains.jpg)

What's notable about the activity is that it does not rely on any npm lifecycle hooks such as preinstall, install, or postinstall scripts, instead appending the malicious payload as an Immediately Invoked Function Expression ([IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)) to the end of "node-ipc.cjs." This, in turn, causes the malware to fire unconditionally on every require('node-ipc').

The oddity doesn't end there, for the payload performs a SHA-256 fingerprint check and compares it against a hard-coded hash assembled from eight obfuscated table fragments embedded in the code, before proceeding with system enumeration and comprehensive credential harvesting.

"This means 12.0.1 is entirely inert on any machine whose primary module path does not hash to the target value," StepSecurity researcher Sai Likhith said. "The attacker knows exactly which project or developer is being targeted and pre-computed the hash of their entry point before publishing. The 9.x versions do not have this gate and will execute the full payload on any system that loads them."

The malware also incorporates a second exfiltration channel besides issuing an HTTPS POST to the fake Azure domain containing the compressed stolen data. This involves encoding chunks of the archive as a DNS TXT record after overriding the system's DNS resolver with Google Public DNS to sidestep local DNS-based security controls.

"It first resolves sh.azurestaticprovider.net using 1.1.1.1 (primary) or 8.8.8.8 (fallback) to obtain the C2 IP," StepSecurity said. "Then it re-targets the resolver directly at the C2 IP for all exfiltration queries."

"The direct-to-C2 DNS sink is a notable anti-detection technique. Because the exfiltration queries never touch public DNS resolvers, there is no observable bt.node.js activity in public DNS logs. Organizations relying solely on DNS logging through corporate resolvers would not see this traffic."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Lastly, the [malware](https://www.ox.security/blog/node-ipc-npm-package-infostealer-malware/) also [attempts](https://www.upwind.io/feed/malicious-node-ipc-npm-package-credential-theft) to continue execution independently of the original Node.js process by forking itself into a detached background child processes, allowing exfiltration activity to continue silently after the parent application is terminated.

"This campaign reflects how software supply chain attacks are evolving beyond simple malicious packages into infrastructure-aware credential harvesting operations," Avital Harel, security research lead at Upwind, said in a statement. "Attackers are increasingly targeting the identities and automation systems powering modern software delivery pipelines while designing malware specifically to blend into normal developer and application behavior."

This is not the first time the npm package has incorporated malicious functionality. In March 2022, the maintainer of the ...