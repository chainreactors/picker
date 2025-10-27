---
title: PE32 Ransomware: A New Telegram-Based Threat on the Rise
url: https://any.run/cybersecurity-blog/pe32-ransomware-analysis/
source: Over Security - Cybersecurity news aggregator
date: 2025-04-23
fetch_date: 2025-10-06T22:08:46.144095
---

# PE32 Ransomware: A New Telegram-Based Threat on the Rise

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

![PE32 Ransomware: A New Telegram-Based Threat on the Rise ](/cybersecurity-blog/wp-content/uploads/2025/04/PE32_blog.jpg)

[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

# PE32 Ransomware: A New Telegram-Based Threat on the Rise

April 22, 2025

[Add comment](#comments-12987)
25593 views
9 min read

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

PE32 Ransomware: A New Telegram-Based Threat on the Rise

#### Recent posts

* [![](/cybersecurity-blog/wp-content/uploads/2025/09/Release-notes-1024x497.png)

  #### Release Notes: Palo Alto Networks, Microsoft, IBM Connectors and 2,300+ Suricata Rules

  1587
  0](/cybersecurity-blog/release-notes-september-2025/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/10/FunkLocker_blog-1024x497.jpg)

  #### FunkSec’s FunkLocker: How AI Is Powering the Next Wave of Ransomware

  3153
  0](/cybersecurity-blog/funklocker-malware-analysis/)
* [![](/cybersecurity-blog/wp-content/uploads/2025/09/defender_blog-1024x497.jpg)

  #### ANY.RUN & MS Defender: Enrich Alerts Faster, Stop Attacks Early

  3162
  0](/cybersecurity-blog/ms-defender-connectors/)

[Home](/cybersecurity-blog/)[Malware Analysis](/cybersecurity-blog/category/malware-analysis/)

PE32 Ransomware: A New Telegram-Based Threat on the Rise

***Editor’s note:****The current article is authored by Mauro Eldritch, offensive security expert and threat intelligence analyst. You can*[*find Mauro on X*](https://x.com/MauroEldritch)*.*

There’s no shortage of [ransomware](https://any.run/malware-trends/ransomware) these days. It’s everywhere, lurking in email attachments, hiding in cracked software, and making headlines almost daily. While some ransomware groups vanish or rebrand, new names step in to take their place, keeping security teams in a constant state of alert.

One of the latest strains making the rounds is **PE32 Ransomware,** a newcomer that’s quickly gaining attention online, including on Twitter. Despite its amateur execution, it manages to [encrypt files](https://any.run/cybersecurity-blog/encryption-algorithms-in-malware/), communicate over Telegram, and cause real damage.

## PE32: Key Takeaways

![](/cybersecurity-blog/wp-content/uploads/2025/04/pe32main-1024x582.png)

In this report, **[Mauro Eldritch](https://any.run/cybersecurity-blog/authors/mauro-eldritch/)** takes a closer look at [how PE32 works](https://app.any.run/tasks/58b336b0-baec-48bb-9675-b2f3d352b63c/?utm_source=anyrunblog&utm_medium=article&utm_campaign=pe32_analysis&utm_term=220425&utm_content=linktoservice), how it communicates, and why its chaotic behavior still poses a real threat.

* **Fast** **encryption**: Starts encryption after a simple prompt; targets visible folders like Desktop.

* **Unique ransom setup**: Two payment tiers: one to unlock files, another to stop data leaks.

* **Telegram C2**: Communicates entirely via Telegram Bot API; bot token is exposed in the code.

* **Easy to analyze**: [ANY.RUN makes it simple to extract bot data and monitor activity](https://app.any.run/tasks/58b336b0-baec-48bb-9675-b2f3d352b63c/?utm_source=anyrunblog&utm_medium=article&utm_campaign=pe32_analysis&utm_term=220425&utm_content=linktoservice).

* **Messy & loud**: Drops marker files, triggers disk repair, and encrypts even useless files.

* **No stealth**: No obfuscation or evasion tricks; relies on basic Windows libraries.

* **Immature but active**: Still evolving, but already a threat due to poor security hygiene.

## Execution Flow and Initial Behavior

![](/cybersecurity-blog/wp-content/uploads/2025/04/1-1024x542.jpg)

When executed, the sample waits for the operator’s input to determine whether it should encrypt only the folder where it was dropped or the entire system (see Image 2).

[View sandbox analysis](https://app.any.run/tasks/58b336b0-baec-48bb-9675-b2f3d352b63c/?utm_source=anyrunblog&utm_medium=article&utm_campaign=pe32_analysis&utm_term=220425&utm_content=linktoservice)

![](/cybersecurity-blog/wp-content/uploads/2025/04/2-1024x538.jpg)

However, regardless of this selection, it immediately starts noisily encrypting the most visible locations, such as the desktop, appending the .pe32s extension (see Image 3).

### Encrypted Desktop files with .pe32s extension

Instead of dropping a ransom note directly onto the Desktop (as most ransomware does), PE32 creates a folder named PE32-KEY in the root of the C:\ drive. This folder contains several internal files used during execution:

* context.pe32c, lock.pe32, pe32lockfile.lock – for internal tracking and state

![](/cybersecurity-blog/wp-content/uploads/2025/04/3-1024x541.jpg)

* ID – stores the victim’s unique identifier

* README.txt – the actual ransom note

Speed up and simplify analysis of malware and phishing threats with ANY.RUN’s Interactive Sandbox

[Sign up with business email](https://app.any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=pe32_analysis&utm_term=220425&utm_content=linktoregistration#register/)

### PE32 ransom note

The ransom note stands out for its two-tiered payment model: one fee to unlock encrypted files, and another to prevent stolen data from being leaked. This approach differs from most ransomware strains, which typically bundle both into a single payme...