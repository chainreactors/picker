---
title: Augmenting Penetration Testing Methodology with Artificial Intelligence – Part 2: Copilot
url: https://www.blackhillsinfosec.com/penetration-testing-with-ai-part-2/
source: Black Hills Information Security, Inc.
date: 2025-05-15
fetch_date: 2025-10-06T22:27:27.955322
---

# Augmenting Penetration Testing Methodology with Artificial Intelligence – Part 2: Copilot

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

14
May
2025

[Craig Vincent](https://www.blackhillsinfosec.com/category/author/craig-vincent/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/)
[AI](https://www.blackhillsinfosec.com/tag/ai/), [artifical intelligence](https://www.blackhillsinfosec.com/tag/artifical-intelligence/), [Copilot](https://www.blackhillsinfosec.com/tag/copilot/), [penetration testing](https://www.blackhillsinfosec.com/tag/penetration-testing/), [Pentesting](https://www.blackhillsinfosec.com/tag/pentesting/)

# [Augmenting Penetration Testing Methodology with Artificial Intelligence – Part 2: Copilot](https://www.blackhillsinfosec.com/penetration-testing-with-ai-part-2/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/11/CVincent-150x150.png)

| [Craig Vincent](https://www.blackhillsinfosec.com/team/craig-vincent/)

*Craig is a former software developer and red teamer. He has been pentesting at Black Hills Infosec since 2018.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/copilot_header.png)

*Read part 1 of this series here: [**Part 1 – Burpference**](https://www.blackhillsinfosec.com/penetration-testing-with-ai-part-1/)*

A common use case for LLMs is rapid software development. One of the first ways I used AI in my penetration testing methodology was for payload generation. For example, I wanted to create an exhaustive list of out-of-band (OOB) command injection payloads. I started by collecting a list of command injection payloads from various sources such as [SecLists](https://github.com/danielmiessler/SecLists), [PayloadAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings), [Payload Box](https://github.com/payloadbox/command-injection-payload-list), etc. Many of these payloads needed some modification because they contained IP addresses and domains for out-of-band interaction that I did not control.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture1-1.png)

**Command Injection Payloads with Unknown Hosts for Interaction**

Ideally, I would like to replace these IPs and domains with URIs for a Burp Suite Collaborator server that I can poll for interactions. So, I opened [Visual Studio Code](https://code.visualstudio.com/) which has built-in [GitHub Copilot](https://github.com/features/copilot) integration. I instructed Copilot to write a Python script that would read a file line by line and replace each instance of an IP address or URL with the placeholder text `{{}}`.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture2-1.png)

**Prompting Copilot to Write Python Script to Replace IPs and URLs**

A few seconds later, I had a Python script that I could save and run on my list of payloads.

```
┌──(root㉿kali)-[/home/kali/Desktop/blog]
└─# python ./url_replacer.py sample-payloads.txt
Processing complete. Modified file saved as: modified_sample-payloads.txt
```

**`Running AI Generated Python Script`**

I reviewed the modified payloads, and it appeared that the script worked.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture3-1.png)

**Payloads Modified with Placeholder**

Next, I asked Copilot to write me a python script that would read two files line by line. I instructed it to replace any instance of the placeholder text in the first file with the next line of the second file and output the results to a third file.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture4-1.png)

**Prompting Copilot for Second Script**

I saved this new script along with a text file where I pasted some Burp Suite Collaborator URIs. I ran the new script with my list of payloads containing placeholders and my Collaborator file. I reviewed the file generated by the script and confirmed that my Collaborator URIs had been successfully inserted in the correct locations.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/05/Picture5-1.png)

**Placeholders Successfully Replaced with Collaborator URIs**

Now, anytime I want to test for command injection, I can save new Collaborator URIs to a file and run the second script again to quickly generate more unique payloads to feed to Intruder. This isn’t super flashy, but I thought it would serve as a good example of how AI-assisted rapid development can help streamline potentially time-consuming penetration testing tasks.

LLMs can also be helpful for brainstorming ideas while penetration testing, but they can sometimes be touchy about what you ask them. For example, let’s say I wanted to review OWASP’s Juice Shop’s main.js file for potential vulnerabilities. I asked Copilot for an example of potentially dangerous Ja...