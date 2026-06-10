---
title: Hades PyPI Attack: 19 Packages Poisoned to Auto-Run Bun Credential Stealer
url: https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html
source: The Hacker News
date: 2026-06-09
fetch_date: 2026-06-10T06:17:16.514384
---

# Hades PyPI Attack: 19 Packages Poisoned to Auto-Run Bun Credential Stealer

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

# [Hades PyPI Attack: 19 Packages Poisoned to Auto-Run Bun Credential Stealer](https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html)

**Ravie Lakshmanan**Jun 09, 2026Supply Chain Attack / Malware

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEimsh1r7uS0J7o39IjoPTuHOzh-EiqtvAat_29YiejSgsn0oTvwmlklYrtu0VqUU05z-THGSE__CFshF8lpSdkRbx-b7Ez0uvlBnWcNQntBPcjv08iKy_hqq5W6NrLSUFek3FfLN5Z6ookVi6zqFE_uQhF56Nu_uyorkUuHOlYxm-cpfFsDwMUhWNRB9Mxi/s1700-e365/python-worm.png)

The [Miasma](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html) supply chain campaign has sparked a fresh attack wave called **Hades**, this time involving 37 malicious wheel artifacts across 19 packages in the Python Package Index (PyPI) registry, as the Mini Shai-Hulud-style attacks continue to be refined and splintered to target specific ecosystems.

"The compromised releases shipped a \*-setup.pth file that attempts to execute automatically during Python startup, download the Bun JavaScript runtime, and run an obfuscated JavaScript payload named \_index.js," Socket [said](https://socket.dev/blog/shai-hulud-descends-to-hades-miasma-pypi-wave) in a new analysis.

The list of identified packages is below -

* bramin 0.0.2, 0.0.3, 0.0.4
* cmd2func 0.2.2, 0.2.3
* coolbox 0.4.1, 0.4.2
* dynamo-release 1.5.4
* executor-engine 0.3.4, 0.3.5
* executor-http 0.1.3, 0.1.4
* funcdesc 0.2.2, 0.2.3
* magique 0.6.8, 0.6.9
* magique-ai 0.4.4, 0.4.5
* mrbios 0.1.1, 0.1.2
* napari-ufish 0.0.2, 0.0.3
* nucbox 0.1.2, 0.1.3
* okite 0.0.7, 0.0.8
* pantheon-agents 0.6.1, 0.6.2
* pantheon-toolsets 0.5.5, 0.5.6
* spateo-release 1.1.2
* synago 0.1.1, 0.1.2
* ufish 0.1.2, 0.1.3
* uprobe 0.1.3, 0.1.4

Like in the previous Shai-Hulud and Miasma campaigns, the malicious payload downloads and installs the Bun JavaScript runtime, which is then used to launch a heavily obfuscated JavaScript stealer that can harvest a wide range of data from developer systems.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

This includes secrets associated with GitHub, npm, PyPI, RubyGems, JFrog, CircleCI, Anthropic, AWS, GCP, Azure, and Kubernetes, along with Docker configurations, Vault tokens, SSH keys, shell histories, .env files, .npmrc files, .pypirc files, Claude/MCP configurations, and other local or runner-accessible credentials.

What's changed this time around is the campaign marker. While previous iterations exported the harvested data to a public GitHub repository with the description "Miasma: The Spreading Blight," "Miasma: The Spreading Blight," and "Miasma - The Spreading Blight," the latest wave [includes](https://github.com/search?q=%22Hades+The+End+for+the+Damned%22&type=repositories) the repository descriptions -

* Hades - The End for the Damned
* Hades \* The End for the Damned

"That makes Hades best understood as a PyPI branch of the same Mini Shai-Hulud / Miasma lineage, not a standalone Python malware incident," the application security company said. "The core playbook remains the same: abuse trusted package channels, execute before normal package use, stage a Bun-powered JavaScript payload, steal developer and CI/CD credentials, and use GitHub-centric exfiltration and propagation logic."

What has changed this time around is the use of a \*-setup.pth file that's processed by Python's "site" module during interpreter startup, resulting in the execution of the malicious payload after installation without requiring the victim to import the poisoned package. The payload, in turn, downloads and runs Bun from GitHub and runs the stealer, but not before checking if the system corresponds to the Russian locale.

"This is the Python equivalent of the npm install-hook problem that Shai-Hulud and Miasma repeatedly exploit," Socket explained. "The syntax is different, but the security consequence is the same: dependency installation creates an execution edge before application code is reviewed or invoked."

### Hades Cluster Attempts to Mislead AI Security Scanners

Also compromised as part of the Hades campaign are a number of packages related to the computational biology, bioinformatics, and genotype-phenotype analysis ecosystem -

* embiggen 0.11.97
* ensmallen 0.8.101
* gpsea 0.9.14
* mflux-streamlit 0.0.3, 0.0.4
* nhmpy 2.4.7
* ppkt2synergy 0.1.1
* pyphetools 0.9.120

Interestingly, this cluster employs a different approach in that the entry point is embedded inside the package's "\_\_init\_\_.py" file as an obfuscated single-line import hook. However, the outcome is the same: Downloading and running the Bun runtime, followed by the execution of the JavaScript payload.

"The use of the Bun runtime remains a consistent theme," StepSecurity [said](https://www.stepsecurity.io/blog/the-hades-campaign-pypi-packages). "Downloading Bun as a standalone ZIP file allows the malware to run complex JavaScript tasks in environments that lack a Node.js installation, bypassing traditional package manager controls and network proxy logs."

In what has been characterized as a novel artificial intelligence (AI) defense evasion technique, the malware also incorporates a plain-text prompt injection that attempts to deceive Large Language Model (LLM)-based package analysis tools to instruct the model to classify the package as safe.

On top of that, the malware queries GitHub commits for the keyword "TheBeautifulSnadsOfTime" to extract a Base64-encoded string containing a JavaScript payload. It also polls GitHub for commits matching the keyword "firedalazer" so as to fetch a Python-based dropper and execute it.

Some of the important features built into the Hades malware are listed below -

* Replicate and spread laterally across developer networks via SSH or SCP, push trojanized versions of PyPI packages from compromised systems by exploiting the developers' OpenID Connect (OIDC) trust configurations.
* Target GitHub repositories to extract organization secrets u...