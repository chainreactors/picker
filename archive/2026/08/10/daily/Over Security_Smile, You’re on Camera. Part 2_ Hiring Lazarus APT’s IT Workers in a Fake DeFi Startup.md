---
title: Smile, You’re on Camera. Part 2: Hiring Lazarus APT’s IT Workers in a Fake DeFi Startup
url: https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation-part-two/
source: Over Security
date: 2026-08-10
fetch_date: 2026-08-11T03:31:33.637836
---

# Smile, You’re on Camera. Part 2: Hiring Lazarus APT’s IT Workers in a Fake DeFi Startup

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* [Guides and tutorials](https://any.run/cybersecurity-blog/guides/)
* [Research](https://any.run/cybersecurity-blog/research/)
* Categories
  + [Analyst Training](https://any.run/cybersecurity-blog/category/training/)
  + [Cybersecurity Lifehacks](https://any.run/cybersecurity-blog/category/lifehacks/)
  + [Instructions on ANY.RUN](https://any.run/cybersecurity-blog/category/instructions/)
  + [Interviews](https://any.run/cybersecurity-blog/category/interviews/)
  + [Malicious History](https://any.run/cybersecurity-blog/category/history/)
  + [Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)
  + [News](https://any.run/cybersecurity-blog/category/news/)
  + [Service Updates](https://any.run/cybersecurity-blog/category/service-updates/)
* [Write for us](https://any.run/cybersecurity-blog/write-for-us/)
* [Go to service](https://app.any.run/)
* [Register for free](https://app.any.run/?register)
* [Register for free](https://app.any.run/?register)

* + Search

[![ANY.RUN's Cybersecurity Blog](https://any.run/cybersecurity-blog/wp-content/uploads/2026/02/anyrun-logo.svg)](https://any.run)
/
[BLOG](https://any.run/cybersecurity-blog/)

* + Search

![Smile, You’re on Camera. Part 2: Hiring Lazarus APT’s IT Workers in a Fake DeFi Startup](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Hiring-Lazarus-APT-Remote-Workers-scaled.png)

[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

# Smile, You’re on Camera. Part 2: Hiring Lazarus APT’s IT Workers in a Fake DeFi Startup

August 10, 2026

[Add comment](#comments-22466)
10815 views
23 min read

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

Smile, You’re on Camera. Part 2: Hiring Lazarus APT’s IT Workers in a Fake DeFi Startup

#### Recent posts

* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Hiring-Lazarus-APT-Remote-Workers-1024x497.png)

  #### Smile, You're on Camera. Part 2: Hiring Lazarus APT's IT Workers in a Fake DeFi Startup

  10815
  0](https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation-part-two/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/ChongLuaDao-1024x497.png)

  #### Safeguarding 200M Users: How ChongLuaDao Scales Threat Validation with ANY.RUN

  7113
  0](https://any.run/cybersecurity-blog/chongluadao-success-story/)
* [![](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Major-Cyber-Attacks-in-July-2026-1024x497.png)

  #### Major Cyber Attacks in July 2026: US and EU Organizations Hit by Phishing, RATs, and Stealers

  11504
  0](https://any.run/cybersecurity-blog/major-cyber-attacks-july-2026/)

[Home](https://any.run/cybersecurity-blog/)[Malware Analysis](https://any.run/cybersecurity-blog/category/malware-analysis/)

Smile, You’re on Camera. Part 2: Hiring Lazarus APT’s IT Workers in a Fake DeFi Startup

*Editor’s note: This work is a collaboration between Mauro Eldritch from BCA LTD, a company dedicated to threat intelligence and hunting, Heiner García from NorthScan, a threat intelligence initiative uncovering North Korean IT worker infiltration, and* [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=lazarus-group-it-workers-investigation-part-two&utm_term=100826&utm_content=linktolanding)*, the leading company in malware analysis and threat intelligence*.

*The article was written by Mauro and Heiner.*

## **Key Takeaways**

* Researchers created a fake DeFi startup and **hired suspected Famous Chollima operatives**, providing a rare inside view of a DPRK IT worker operation.
* **The investigation followed the scheme beyond recruitment**, showing how the operatives worked, collaborated, and accessed company resources after being hired.
* [ANY.RUN](https://any.run/?utm_source=anyrunblog&utm_medium=article&utm_campaign=lazarus-group-it-workers-investigation-part-two&utm_term=100826&utm_content=linktolanding) sandbox environments provided **a live view of the operatives’ behavior**, exposing their evolving toolset, remote access workflow, AI usage, and supporting infrastructure.
* The findings show that DPRK IT worker schemes are **not only a hiring risk**. Once inside, operatives can gain legitimate access to code, systems, intellectual property, and trusted business processes.

## **Introduction**

Back in December, we were **the first ever to fully record the Famous Chollima infiltration cycle**. From recruiting collaborators to help them land jobs at Western companies, to forging documents, shipping laptops to facilitators’ houses, and even using AI tools for live assistance and translation during interviews.

During that investigation, we posed as facilitators willing to take job interviews and lend them laptops so they could find a job in exchange for a percentage of their salaries. The trick was that those laptops were actually [**ANY.RUN** sandbox environments](https://any.run/features/?utm_source=anyrunblog&utm_medium=article&utm_campaign=lazarus-group-it-workers-investigation-part-two&utm_term=100826&utm_content=linktosandboxlanding), recording every click and every movement they made. This gave us tons of indicators, endless hours of laptop and face-to-face footage, and **[an unprecedented investigation](https://any.run/cybersecurity-blog/lazarus-group-it-workers-investigation/)** that made it to the top of many media outlets.

![Aaron A.K.A “Blaze”, Famous Chollima Recruiter](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Famous-Chollima-Recruiter-Exposed-1024x463.png)

*Aaron A.K.A “Blaze”, Famous Chollima Recruiter from Episode 1*

It was definitely not for the faint of heart, requiring months of dedication as we profiled them while acting as their partners in crime. But today, we want to raise the stakes.

This time, instead of playing facilitators, we posed as the founders of **Ballena Azul LTD**, a new DeFi protocol working directly with crypto whales across different chains and looking for new developers to build it. Developers we could trust with *lots of money*. More than you and all your friends could ever fit in your pockets. Numbers you can barely read without counting the commas. All while resisting the temptation to drain it to an embargoed nation far away to the East.

![Ballena Azul LTD / Blue Whale LTD Website](https://any.run/cybersecurity-blog/wp-content/uploads/2026/08/Ballena-Azul-LTD-Blue-Whale-LTD-Website-1024x629.png)

*Ballena Azul LTD / Blue Whale LTD Website*

This new episode has it all: **an overconfident CEO** who does not run bac...