---
title: Emotet Resumes Spam Operations, Switches to OneNote
url: https://blog.talosintelligence.com/emotet-switches-to-onenote/
source: Over Security - Cybersecurity news aggregator
date: 2023-03-23
fetch_date: 2025-10-04T10:23:47.238853
---

# Emotet Resumes Spam Operations, Switches to OneNote

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# Emotet resumes spam operations, switches to OneNote

By
[Edmund Brumaghin](https://blog.talosintelligence.com/author/edmund-brumaghin/),
[Jaeson Schultz](https://blog.talosintelligence.com/author/jaeson-schultz/)

Wednesday, March 22, 2023 15:41

[Threat Advisory](https://blog.talosintelligence.com/category/threat-advisory/)
[Threats](https://blog.talosintelligence.com/category/threats/)

![](https://blog.talosintelligence.com/content/images/2023/03/image9.jpg)

* Emotet resumed spamming operations on March 7, 2023, after a months-long hiatus.
* Initially leveraging heavily padded Microsoft Word documents to attempt to evade sandbox analysis and endpoint protection, the botnets switched to distributing malicious OneNote documents on March 16.
* Since returning, Emotet has leveraged several distinct infection chains, indicating that they are modifying their approach based on their perceived success in infecting new systems.
* The initial emails delivered to victims are consistent with what has been observed from Emotet over the past several years.

# Initial campaign

Following its initial return to spamming operations, Emotet was leveraging heavily padded Microsoft Word documents in an attempt to evade detection. By leveraging a large number of inconsequential bytes in their documents, they could increase the size of the documents to surpass the maximum file size restrictions that automated analysis platforms like sandboxes and anti-virus scanning engines enforce.

The initial emails were consistent with what has been commonly observed from Emotet in recent years. They typically contained an attached ZIP archive containing a Microsoft Word document. An example of one such email is shown below.

![](https://blog.talosintelligence.com/content/images/2023/03/image5.png)

While the ZIP archives are often small, in some cases only ~646KB, the Microsoft Word document when fully extracted was ~500MB in size.

![](https://blog.talosintelligence.com/content/images/2023/03/image8.png)

The document included a large number of 0x00 bytes, a technique [commonly referred to as “padding.”](https://blog.talosintelligence.com/malware-meets-sysadmin-automation-tools/)

![](https://blog.talosintelligence.com/content/images/2023/03/image14.png)

Some of the documents also featured excerpts from the classic novel “Moby Dick,” another attempt to increase the size of the documents for evasion purposes.

![](https://blog.talosintelligence.com/content/images/2023/03/image10.png)

The Office documents featured templates consistent with those used by Emotet in the past, as shown below.

![](https://blog.talosintelligence.com/content/images/2023/03/image1.png)

The Word documents in this campaign contained malicious VBA macros that, when executed, functioned as a malware downloader, retrieving the Emotet payload from attacker-controlled distribution servers and infecting systems, thus adding them to the Emotet botnets.

![](https://blog.talosintelligence.com/content/images/2023/03/image11.png)

# Emotet shifts to OneNote

Microsoft recently [deployed new security mechanisms](https://learn.microsoft.com/en-us/deployoffice/security/internet-macros-blocked) around protecting endpoints from macro-based malware infections, which resulted in various threat actors moving away from Office document-based malspam campaigns. In many cases, these malware distribution campaigns switched to distributing OneNote documents instead, likely as a result of decreased infections and lower success rates. Emotet is no different — shortly after their return to spamming operations on March 16, 2023, they began distributing OneNote files, as well.

In one example, the sender purported to be from the U.S. Internal Revenue Service (IRS) and requested that the recipient complete the attached form.

![](https://blog.talosintelligence.com/content/images/2023/03/image13.png)

The attached OneNote document featured templates similar to what has been observed in other Office document formats over the past several years, prompting the user to click inside the document to view the file.

![](https://blog.talosintelligence.com/content/images/2023/03/image7.png)

When clicked, an embedded WSF script linked behind the view button containing malicious VBScript code is executed.

![](https://blog.talosintelligence.com/content/images/2023/03/image3.png)

This VBScript downloader is responsible for retrieving the Emotet malware payload from an attacker-controlled server and infecting the system.

![](https://blog.talosintelligence.com/content/images/2023/03/image12.png)

More recently, the embedded object inside of the OneNote files contained JavaScript instead of VBScript but offered the same functionality within the infection chain.

![](https://blog.talosintelligence.com/content/images/2023/03/image2.png)

Hovering over the next button indicates that an object called “Object1.js” will execute when the button is clicked. This is because the attacker has embedded a clickable object behind the lure image as shown below.

![](https://blog.talosintelligence.com/content/images/2023/03/image15-1.png)

This object is a heavily obfuscated JavaScript downloader responsible for retrieving and executing the Emotet payload on the system. A snippet from the obfuscated downloader is shown below.

![](https://blog.talosintelligence.com/content/images/2023/03/image6-1.png)

In a relatively short period, Emotet has modified its infection chain several times to maximize the likelihood of successfully infecting victims.

# Indicators of Compromise

Indicators of compromise (IOCs) associated with ongoing Emotet campaigns can be found [here](https://github.com/Cisco-Talos/IOCs/blob/main/2023/03/emotet-switches-to-onenote.txt).

# Coverage

![](https://blog.talosintelligence.com/content/images/2023/03/image4.png)

[Cisco S...