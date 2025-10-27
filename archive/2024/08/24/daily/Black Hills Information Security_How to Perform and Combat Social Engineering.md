---
title: How to Perform and Combat Social Engineering
url: https://www.blackhillsinfosec.com/how-to-perform-and-combat-social-engineering/
source: Black Hills Information Security
date: 2024-08-24
fetch_date: 2025-10-06T18:05:11.877922
---

# How to Perform and Combat Social Engineering

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

22
Aug
2024

[Ashley Knowles](https://www.blackhillsinfosec.com/category/author/ashley-knowles/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Phishing](https://www.blackhillsinfosec.com/category/red-team/phishing/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Social Engineering](https://www.blackhillsinfosec.com/category/red-team/social-engineering/)
[InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/)

# [How to Perform and Combat Social Engineering](https://www.blackhillsinfosec.com/how-to-perform-and-combat-social-engineering/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/AKnowles-150x150.png)

| [Ashley Knowles](https://www.blackhillsinfosec.com/team/ashley-knowles/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2024/08/BLOG_chalkboard_00684.png)

*This article was originally published in the second edition of the InfoSec Survival Guide. Find it free online [HERE](https://www.blackhillsinfosec.com/prompt-zine/prompt-issue-infosec-survival-guide-second-volume/) or order your $1 physical copy on the [Spearphish General Store.](https://spearphish-general-store.myshopify.com/products/infosec-survival-guide-second-volume)*

Social engineering is the use of deceptive tactics and techniques to manipulate users into providing confidential or sensitive information. This information can then be used for nefarious purposes.

### **Performing Social Engineering**

Typically, our red team assessments start with some way to obtain initial access. This initial access is normally obtained through the use of social engineering, whether that be through Microsoft Teams messages, phishing emails, smishing texts, or vishing calls. There are multiple ways to conduct social engineering and not every way is perfect for every organization. There is a lot of OSINT (Open-Source INTelligent) that goes into the development of the perfect social engineering ruse for an organization. Things like what the company does, what products they use, and even information provided by the client is used to develop and appropriate ruse.

Commonly, successful social engineering ruses are done from the perspective of an IT person calling to discuss a problem with an update that wasn’t pushed correctly, or a computer that isn’t calling home appropriately.

Recently, a tester posed as HR calling to ensure that employees have had their yearly review. Before continuing with the call, the “HR representative” attempted to verify the identity of the person they were calling with the last four of their social, date of birth, and employee number. After verification was completed, the tester proceeded with several generic questions about the review and the employee’s experience.

This ruse proved to be incredibly successful. The tester then called the help desk to claim that they lost their phone which had their password manager on it and needed to join a new phone to their MFA account. With the social-engineered PII (personal identifiable information), the tester was able to join a new phone to their MFA account and reset their password. The compromised account could then be used to access sensitive company data.

**If in doubt, go through other means to verify legitimacy. No reputable person is going to request your password or login information.**

### **Combatting Social Engineering**

So, you may ask, how do we train our employees to recognize and report social engineering attempts? The answer is to always be on guard, have an easy to access and use escalation protocol, and conduct regular social engineering engagements against your team.

There are a few simple things that, when followed, can protect most users:

* Always check who is sending the email. This can be done by inspecting email headers on suspicious emails.
  + If the sender’s address does not match who is claiming to be sending the email, report it.
* For text messages or phone calls, the user can use a simple reverse number search on the phone number. Most VoIP phone numbers are suspicious. Threat actors like to use VoIP to hide their dentity and VoIP numbers are easy to obtain.
* If in doubt on whether an email or call/text is malicious, go through other means to contact the actual person to verify legitimacy.

Some questions users can ask themselves that indicate immediate red flags:

* What is being requested of the user?
* Is the user being asked to download software or navigate to a web application?
* Is it too good to be true?
* Are they being asked for their password, date of birth, last four of their social, or other sensitive information?

If you think that you are a target of a social engineering ...