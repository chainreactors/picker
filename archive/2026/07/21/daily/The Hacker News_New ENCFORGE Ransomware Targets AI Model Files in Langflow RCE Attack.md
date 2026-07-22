---
title: New ENCFORGE Ransomware Targets AI Model Files in Langflow RCE Attack
url: https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html
source: The Hacker News
date: 2026-07-21
fetch_date: 2026-07-22T05:04:27.458425
---

# New ENCFORGE Ransomware Targets AI Model Files in Langflow RCE Attack

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrKWHErc__Wn0forfQ5eJ5sIR1hVKCHCTeNQOaAX4lbygJ8S1Xpemx6JXl78dpwiT65DDBGURp48A3EemKzmli-jXPI3v1928MnJm-1j2ZPUaFXCvuySFhyphenhyphenKR-Li6fAinFT2bhLgsqUSNUR_ggMAnOHi3jD1qYWHXvueX8WdtxAd6GYety9cBGYABo18hX/s728-e100/tt-d.jpg)](https://thehackernews.uk/ai-zero-trust-h-d)

# [New ENCFORGE Ransomware Targets AI Model Files in Langflow RCE Attack](https://thehackernews.com/2026/07/new-encforge-ransomware-targets-ai.html)

**Swati Khandelwal**Jul 21, 2026Threat Intelligence / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjDTNXJkg3w9ziG7euHnlaoQkTjogtjIhtwE-ZudPv_9wOpJUCUNVc-i_BtBkDTCflKzRSfUOEp5xHyRWAOcQWv18pf2kv9-yuI75SOM52X3akV3VrguZf6GDH9MZejxFG7FoJGMIgARuiWyncCOmNznSofFT8Fn9Zu2ZGmk0V_Ni3niha2I9qAO59VKHw/s1700-e365/ransomware-ai.jpg)

Researchers at Sysdig have linked a second attack on the same Langflow server to [JADEPUFFER](https://thehackernews.com/2026/07/ai-agent-exploits-langflow-rce-to.html), the AI-agent-driven operator it first documented earlier this month.

The same operator has now been spotted deploying **ENCFORGE**, a new compiled Go ransomware designed to encrypt model weights, vector indexes, training datasets, and other AI infrastructure files across the host filesystem.

The entry point did not change. [Langflow versions before 1.3.0](https://github.com/langflow-ai/langflow/security/advisories/GHSA-rvqx-wpfh-mfx7) expose the `/api/v1/validate/code` endpoint without authentication, allowing any remote attacker to execute arbitrary Python on the server. The flaw, [`CVE-2025-3248`](https://nvd.nist.gov/vuln/detail/CVE-2025-3248), carries a CVSS score of 9.8 and has been in CISA's Known Exploited Vulnerabilities [catalog](https://www.cisa.gov/news-events/alerts/2025/05/05/cisa-adds-one-known-exploited-vulnerability-catalog) since May 5, 2025.

As The Hacker News reported earlier this month, the prior operation used throwaway Python code and MySQL's `AES_ENCRYPT()` function to encrypt and destroy data in Nacos (Alibaba's configuration server) and production databases.

The new [ENCFORGE payload](https://www.sysdig.com/blog/jadepuffer-evolves-the-agentic-threat-actor-deploys-ransomware-built-to-destroy-ai-models) replaces those improvised scripts with compiled tooling aimed at the model stores, vector databases, and training pipelines the first campaign swept for credentials.

## The ENCFORGE Payload

Researchers retrieved the binary from the attacker's command-and-control server, where it was hidden as `/.lockd`; a direct request to `/lockd` returns 404, and the leading dot keeps it off a plain directory listing. The file is a UPX 5.20-packed static Go 1.22.12 ELF.

Threat intelligence platforms returned no detections on either the packed or unpacked hash at the time of Sysdig's analysis. The internal project name is `encfile`; the binary's error text references a companion keygen tool named `keyforge`. Both strings survive recompilation of the same codebase and serve as stable detection anchors.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-vuln-protection-d)

Its default extension list covers PyTorch and TensorFlow checkpoints, Hugging Face SafeTensors, ONNX interchange format, GGUF (the current standard for locally deployed LLMs) and its predecessor GGML, FAISS vector indexes, Parquet and Arrow training datasets, NumPy arrays, and TensorFlow records.

An `--include` flag lets the operator append additional file globs; the built-in help text uses LoRA fine-tuning adapters and legacy GGML weights as examples. The full list runs to approximately 180 extensions. Those examples point directly at AI environments; a generic file locker would have little reason to name LoRA adapters or legacy GGML weights. Researchers read the choice as deliberate targeting, not incidental coverage.

ENCFORGE uses AES-256-CTR for file data, with the per-run symmetric key wrapped under an embedded RSA-2048 public key compiled into this build. Rather than encrypting whole files, it encrypts selected regions, the same speed optimization LockBit and BlackCat-class lockers use.

Each processed file is renamed with a `.locked` extension. The binary kills processes holding files open before encrypting, handles restarts without re-encrypting completed files, drops ransom notes as `README`, `HOW_TO_DECRYPT`, and `README_DECRYPT`, and deletes itself after running.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjEoToP8gvd4Gql8-JT2fVhJBZGEhAyDRNr9XinJAeyJiZUDiYqW-x0Ex3d4I4z9ZUDogmzvkcgkJOfsGfAKHzz_Gp5sDku-AwjP4snmY33DIgoCP06_xpI-8oULy-Cz-cyNizjPoOKll7Fw1fIMFatCB7anNVSKpmPMDX-ynR3c-91cu104jbO8QIk8HQ/s1700-e365/files.jpg)

The recovered ENCFORGE binary has no exfiltration capability. It carries no networking code, cloud storage client, or staging mechanism, and researchers found no evidence of data exfiltration, a leak site, or a Tor payment portal during the session it observed. Its only leverage is the encrypted data.

The extortion contact embedded in the ransom notes is `e78393397@proton.me`, the same Proton Mail address used in the prior campaign. Sysdig describes this as the strongest attribution link between the two operations.

Researchers disclosed one observed session, did not name the organization, and provided no victim count or evidence of another ENCFORGE deployment.

## From Langflow to the Host

After confirming code execution, JADEPUFFER swept the container for credentials and found the Docker socket at `/var/run/docker.sock`. Its first attempt to pull ENCFORGE from the GCP command-and-control server failed. Rather than stopping, it adapted.

Over five minutes and 24 seconds, the operator created and revised six Python scripts through the same Langflow RCE channel until it had a working path to the host. The first script was built one line at a time, keeping any single request inert for signature-based inspection.

Starting with the second, the operator encoded each full script in base64 and decoded it inside an `exec()` call, avoiding shell-level searches for commands such as `base64 -d`. The final version used the Docker API to spin up a privileged container with the host PID namespace and root filesystem mounted, located the target proc...