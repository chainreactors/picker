---
title: Introducing Squeegee: The Microsoft Windows RDP Scraping Utility
url: https://www.blackhillsinfosec.com/introducing-squeegee-the-microsoft-windows-rdp-scraping-utility/
source: Black Hills Information Security
date: 2024-05-18
fetch_date: 2025-10-06T16:51:19.622296
---

# Introducing Squeegee: The Microsoft Windows RDP Scraping Utility

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

17
May
2024

[David Fletcher](https://www.blackhillsinfosec.com/category/author/david-fletcher/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)

# [Introducing Squeegee: The Microsoft Windows RDP Scraping Utility](https://www.blackhillsinfosec.com/introducing-squeegee-the-microsoft-windows-rdp-scraping-utility/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/DFletcher-150x150.png)

| [David Fletcher](https://www.blackhillsinfosec.com/team/tim-fowler/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Squeegee-header.png)

Hi, it’s David with BHIS! You’ll be saying, “Wow,” every time you use this tool. It’s like a shammy. It’s like a towel. It’s like a sponge. A regular towel doesn’t work wet. This works wet or dry. This is for the house, the car, the boat, the RV. It’s Squeegee! Holds 12 times its weight in liquid. Look at this. It just does the work. Why would you want to work twice as hard? It doesn’t drip. It doesn’t make a mess.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture1.png)

Just kidding. Squeegee won’t clean up your messes, but hopefully, you will find it useful on your tests. Squeegee is actually a tool to scrape text from RDP screen captures.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture2.png)

You are probably asking yourself why that might be useful. We are constantly thinking about ways to get information using unconventional techniques. Imagine that you are on an internal penetration test and you want to know what the local administrator account username is on hosts, but you have hundreds or thousands of RDP listeners on the network. How might you approach that problem?

Next, consider a situation where you might want to get active session information from the environment in an effort to move laterally and escalate privileges. Bloodhound session data isn’t as reliable as it used to be, and, in modern Windows environments, session enumeration tends to get caught. What about cataloging users with active RDP sessions?

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture3.png)

Example RDP Logged In Users

Squeegee can help in both of these situations. The first step is to collect RDP screen captures using a tool like NCC Group’s scrying. Once you have the RDP screen captures, you can process the entire group of results using Squeegee by just pointing the tool at the correct folder.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture4.png)

Squeegee Execution

Squeegee will filter string content that is not likely to be useful in the context of username harvesting and system analysis. In addition, the tool will interpret various strings commonly observed in RDP image output to identify the operating system, the domain the computer is joined to, and whether the system is missing patches. Reporting options include console output, logfile output, and an HTML report.

The HTML report organizes results by operating system and includes links to download the full list of unique usernames and usernames associated with a given RDP instance.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture5.png)

Squeegee HTML Report (Table of Contents)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture6.png)

Squeegee Sample Results

Squeegee uses the easyocr library for OCR support. As a result, text can be extracted from images with support for 81 different languages. This provides an easy method to process an image like the one shown below.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture7.png)

RDP Screen Capture with Non-Latin Characters

Without OCR support, reproducing strings presented on the screen may take considerable effort. Passing in the ISO language code to the script will cause easyocr to process strings associated with the target language. Once the images have been processed, usernames can be copied and pasted from the report or downloaded in the accompanying text file.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/05/Picture8-1.png)

Non-Latin Strings Extracted from RDP Screen Capture

**Check out the Squeegee repository at <https://github.com/OOAFA/squeegee>.**

---

---

Ready to learn more?

Level up your skills with affordable classes from Antisyphon!

**[Pay-Forward-What-You-Can Training](https://www.antisyphontraining.com/pay-forward-what-you-can/)**

Available live/virtual and on-demand

![](https://www.blackhillsinfosec.com/wp-content/upl...