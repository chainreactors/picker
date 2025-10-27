---
title: PyLangGhost RAT: Rising Data Stealer from Lazarus Group Targeting Finance and Technology
url: https://any.run/cybersecurity-blog/pylangghost-malware-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-07
fetch_date: 2025-10-07T00:49:56.069318
---

# PyLangGhost RAT: Rising Data Stealer from Lazarus Group Targeting Finance and Technology

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2020/07/Logo-1.png)](/cybersecurity-blog/)

* [Register for free](https://app.any.run/#register)
* [Guides and Tutorials](/cybersecurity-blog/guides/)
* [Research](/cybersecurity-blog/research/)
* Featured posts
  + [Malware Analysis in ANY.RUN:
    The Ultimate Guide](/cybersecurity-blog/malware-analysis-in-a-sandbox/)
  + [Raccoon Stealer 2.0 Malware analysis](/cybersecurity-blog/raccoon-stealer-v2-malware-analysis/)
  + [How to Get Free Malware Samples and Reports](/cybersecurity-blog/free-malware-samples-reports/)
* Categories
  + [Analyst Training](/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](/cybersecurity-blog/category/instructions/)
  + [Interviews](/cybersecurity-blog/category/interviews/)
  + [Malicious History](/cybersecurity-blog/category/history/)
  + [Malware Analysis](/cybersecurity-blog/category/malware-analysis/)
  + [News](/cybersecurity-blog/category/news/)
  + [Service Updates](/cybersecurity-blog/category/service-updates/)
* [Write for us](/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/#register)

* + Search

[![ANY.RUN's Cybersecurity Blog](/cybersecurity-blog/wp-content/uploads/2022/10/mini-logo.png)](/cybersecurity-blog/)

* + Search

![PyLangGhost RAT: Rising Stealer from Lazarus Group Striking Finance and Technology ](/cybersecurity-blog/wp-content/uploads/2025/08/PyLangGhost_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# PyLangGhost RAT: Rising Stealer from Lazarus Group Striking Finance and Technology

August 6, 2025

[Add comment](#comments-15287)
9823 views
14 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

PyLangGhost RAT: Rising Stealer from Lazarus Group Striking Finance and Technology

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1970
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3195
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3303
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

PyLangGhost RAT: Rising Stealer from Lazarus Group Striking Finance and Technology

*Editor’s note:****The current article is authored by Mauro Eldritch, offensive security expert and threat intelligence analyst. You can***[***find Mauro on X***](https://x.com/MauroEldritch)***.***

North Korean state-sponsored groups, such as Lazarus, continue to target the financial and cryptocurrency sectors with a variety of custom malware families. In previous research, we examined strains like [InvisibleFerret, Beavertail](https://any.run/cybersecurity-blog/invisibleferret-malware-analysis/), and [OtterCookie](https://any.run/cybersecurity-blog/ottercookie-malware-analysis/), often deployed through fake developer job interviews or staged business calls with executives. While these have been the usual suspects, a newer Lazarus subgroup, **Famous Chollima**, has recently introduced a fresh threat: **PyLangGhost RAT**, a Python-based evolution of GoLangGhostRAT.

Unlike common malware that spreads through pirated software or infected USB drives, PyLangGhost RAT is delivered via highly targeted social engineering campaigns aimed at the technology, finance, and crypto industries, with developers and executives as prime victims. In these attacks, adversaries stage fake job interviews and trick their targets into believing that their browser is blocking access to the camera or microphone. The “solution” they offer is to run a script that supposedly grants permission. In reality, the script hands over full remote access to a North Korean operator.

This sample was obtained from fellow researcher Heiner García Pérez of BlockOSINT, who encountered it during a fake job recruitment attempt and documented his findings in an advisory.

Let’s break it down.

![](/cybersecurity-blog/wp-content/uploads/2025/08/1.png)

## Key Takeaways

* **Attribution:** PyLangGhost RAT is linked to the North Korean Lazarus subgroup *Famous Chollima*, known for using highly targeted and creative intrusion methods.

* **Delivery Method:** Distributed through “ClickFix” social engineering, where victims are tricked into running malicious commands to supposedly fix a fake camera or microphone error during staged job interviews.

* **Core Components:** The malware’s main loader (nvidia.py) relies on multiple modules (config.py, api.py, command.py, util.py, auto.py) for persistence, C2 communication, command execution, data compression, and credential theft.

* **Credential & Wallet Theft:** Targets browser-stored credentials and cryptocurrency wallet data from extensions like MetaMask, BitKeep, Coinbase Wallet, and Phantom, using privilege escalation and Chrome encryption key decryption (including bypasses for Chrome v20+).

* **C2 Communication:** Communicates over raw IP addresses with no TLS, using weak RC4/MD5 encryption, but remains stealthy with very low initial detection rates (0–3 detections on VirusTotal).

* **Detection & Analysis:** [Identified as 100/100 malicious by ANY.RUN](https://app.any.run/tasks/275e3573-0b3e-4e77-afaf-fe99b935c510/?utm_source=anyrunblog&utm_medium=article&utm_campaign=pylangghost_rat&utm_term=060825&utm_content=linktoservice), with telltale signs including the default python-requests User-Agent and multiple rapid requests to C2 infrastructure.

* **Code Origin:** Appears to be a full Python reimplementation of GoLangGhost RAT, likely aided by AI, as indicated by Go-like logic patterns, unusual code structure, and large commented-out sections.

## The Fake Job Offer Trap

In the past, DPRK operators have resorted to creative methods to distribute malware, from staging fake job interviews and sharing bogus coding challenges (some laced with malware, others seemingly clean but invoking malicious dependencies at runtime), to posing as VCs in business calls, pretending not to hear the victim, and prompting them to download a fake Zoom fix or update.

This case is a bit different. It falls in...