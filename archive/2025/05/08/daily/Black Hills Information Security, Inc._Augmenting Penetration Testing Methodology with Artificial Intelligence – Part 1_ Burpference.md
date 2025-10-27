---
title: Augmenting Penetration Testing Methodology with Artificial Intelligence – Part 1: Burpference
url: https://www.blackhillsinfosec.com/penetration-testing-with-ai-part-1/
source: Black Hills Information Security, Inc.
date: 2025-05-08
fetch_date: 2025-10-06T22:28:42.658213
---

# Augmenting Penetration Testing Methodology with Artificial Intelligence – Part 1: Burpference

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

7
May
2025

[Informational](https://www.blackhillsinfosec.com/category/informational/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/)
[AI](https://www.blackhillsinfosec.com/tag/ai/), [artifical intelligence](https://www.blackhillsinfosec.com/tag/artifical-intelligence/), [Artificial Intelligence](https://www.blackhillsinfosec.com/tag/artificial-intelligence/), [burpference](https://www.blackhillsinfosec.com/tag/burpference/), [penetration testing](https://www.blackhillsinfosec.com/tag/penetration-testing/)

# [Augmenting Penetration Testing Methodology with Artificial Intelligence – Part 1: Burpference](https://www.blackhillsinfosec.com/penetration-testing-with-ai-part-1/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/CVincent-150x150.png)

| [Craig Vincent](https://www.blackhillsinfosec.com/team/craig-vincent/)

*Craig is a former software developer and red teamer. He has been pentesting at Black Hills Infosec since 2018.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/burpference_header.png)

Artificial Intelligence (AI) has been a hot topic in information technology and information security since before I entered the industry. Developments in AI are something that I had been aware of, but I hadn’t chosen to really dive into the subject in terms of leveraging AI as part of my job as a penetration tester. I gave a webcast on penetration testing methodology a while back, and someone asked me afterward how I use AI in my methodology/workflow. At the time, my answer was “I don’t.”

For a long time, I considered AI to be interesting but not particularly useful. However, progress has been made, technology has improved, and it has become clear that AI has matured to the point where we absolutely can use it to help us with our jobs as penetration testers. So, what does that look like? This blog post will be the first in a series of posts where I will describe my initial experiences trying to integrate AI into my penetration testing methodology.

When exploring new technology and incorporating it into your methodology, it’s always a good idea to start by examining what other folks in your space are already doing with that technology. When I initially started going down this path, my BHIS colleague Derek Banks introduced me to a project called [burpference](https://github.com/dreadnode/burpference/). Burpference is a Burp Suite plugin that takes requests and responses to and from in-scope web applications and sends them off to an LLM for inference. In the context of artificial intelligence, inference is taking a trained model, providing it with new information, and asking it to analyze this new information based on its training.

Installing the burpference extension in Burp Suite is a straightforward task. The extension utilized the [Jython](https://www.jython.org/download.html) standalone JAR. Once I downloaded the JAR, I configured the Burp Suite Python environment to point to the JAR. This setting can be found by opening “Extensions settings” in the Extensions tab.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture1.png)

**Python Environment Configured**

Once the Python environment was configured, I downloaded and unzip the latest [burpference release](https://github.com/dreadnode/burpference/releases). Burpference generates log files in the extension directory, so I needed to ensure that Burp Suite had write permissions to that location. Next, I opened the “Installed” page of the Extensions tab, clicked the “Add” button, and selected the burpference.py file from the extension directory.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture2.png)

**Selecting Burpference Extension**

I checked the Output section of the Burp Suite extension loader to ensure no errors occurred. Once the extension was loaded, I opened the new burpference tab and selected a configuration file that pointed to my LLM. For my initial experimentation with burpference, I set up a small (7 billion parameter) deepseek-r1 model in Ollama on an older gaming PC in my lab.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture3.png)

**Burpference Configuration File Pointing to Local LLM**

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture4.png)

**Configuration File Selected in Burpference Tab**

To test the extension functionality, I installed and ran a local instance of OWASP’s intentionally vulnerable [Juice Shop](https://owasp.org/www-project-juice-shop/) application.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture5.png)

**Browsing Juice Shop Application**

To cut down on noise and unnecessary load on the LLM, ...