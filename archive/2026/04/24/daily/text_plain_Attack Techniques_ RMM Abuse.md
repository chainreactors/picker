---
title: Attack Techniques: RMM Abuse
url: https://textslashplain.com/2026/04/24/attack-techniques-rmm-abuse/
source: text/plain
date: 2026-04-24
fetch_date: 2026-04-25T04:37:00.247896
---

# Attack Techniques: RMM Abuse

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Attack Techniques: RMM Abuse

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-04-242026-04-24](https://textslashplain.com/2026/04/24/attack-techniques-rmm-abuse/)Posted in[security](https://textslashplain.com/category/security/)Tags:[InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [security](https://textslashplain.com/tag/security/)

After you sign up on the Social Security Administration’s website, they’ll send you a yearly email inviting you to [check out your benefits](https://www.ssa.gov/myaccount/). Flipping through my Junk Mail folder this afternoon, I found the following email:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-20.png?w=563)](https://textslashplain.com/wp-content/uploads/2026/04/image-20.png)

It looks reasonably plausible, except for the return address (`cuonlineedu.in`, a [university in India](https://www.cuonlineedu.in/)). I’m always game to look at an attack, so I naturally clicked the “View my statement” link the bad guy hopes I’d click. This navigation results in redirecting through a page on the University’s website to go to a Spanish TLD:

```
GET http://delivery.cuonlineedu.in/UDFEKT?id=28719=c0oCVAtaBQlfGAQDA1YCAl4BAwZSBQVYUFwFAloGVgNRUFRTDFcHDAUAA1YMVgcFDA5LBj1cVhYRXFpXXXZcCkRbUw1VTFFXCxgBUQNVU1IBDQBXUgQCV1sKA0hQQkAVChkdAFwOW04DFklIVxYMDVRRWQYHVEJPClcbYXxwcS5kCVsARRQB&fl=WEJGFEpYHRcEAUMSXQcGCllLVREXXlhPAFZZGl1FGw==

302 Redirect to https://bestideiasbruno.com.es/

GET https://bestideiasbruno.com.es/download.php?url=aHR0cHM6Ly9hcm9taXNiZC5jb20vd3AtY29udGVudC9nZW4ubXNp&name=eStatement455378357_pdf.msi

200 (application/octet-stream)

GET https://www.ssa.gov/myaccount/statement.html

200 (text/html)
```

When that page loads, it claims that your “statement is being prepared” and a file download appears. The file download, named (`eStatement####_pdf.msi`) is an Windows Installer package named to make it look like a PDF file.

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-21.png?w=912)](https://textslashplain.com/wp-content/uploads/2026/04/image-21.png)

For contrast, the legitimate download would’ve looked like this:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-22.png?w=827)](https://textslashplain.com/wp-content/uploads/2026/04/image-22.png)

After kicking off the MSI file download, the attack site navigates to a [legitimate page on the Social Security site](https://www.ssa.gov/myaccount/statement.html).

Okay, so the fake site dropped a file hoping we’d open it, and we can be pretty sure that a file delivered this way is going to be some form of malware. But it’s very concerning that neither SmartScreen or Microsoft Defender Antivirus complained about the file. Let’s take a closer look.

The first thing to note is that the file is [Authenticode-signed](https://textslashplain.com/tag/authenticode):

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-19.png?w=443)](https://textslashplain.com/wp-content/uploads/2026/04/image-19.png)

The MSI file is signed by a legitimate company and after uploading it, we see that it’s [“Clean” on VirusTotal](https://www.virustotal.com/gui/file/c8d33b9b1c46e4059f1d049ff2a3be2c0c963bf51116eb234015041270b495a9/community).

*Hrm.* Maybe the company got hacked and someone stole their certificate to sign malware? Looking more closely at the file information, we see that it was signed on April 13th and the file information looks legitimate “*This installer database contains the logic and data required to install AteraAgent.*” rather than what an attacker might pick (e.g. “*You’re Social Security Info. Open me hurry hurry hurry*.”)

At this point, I had a strong hint that I knew what was going on, but in this AI-hyped world, I wondered whether Copilot would give me good advice.

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-23.png?w=875)](https://textslashplain.com/wp-content/uploads/2026/04/image-23.png)

Microsoft Copilot correctly recognizes that it’s a scam, but it gets the details wrong:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-24.png?w=830)](https://textslashplain.com/wp-content/uploads/2026/04/image-24.png)

Let’s ask Google’s Gemini:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-25.png?w=1024)](https://textslashplain.com/wp-content/uploads/2026/04/image-25.png)

Gemini gets it right — the file is legitimate, but it’s being used. The Altera Agent is a piece of software that is categorized as a **Remote Monitoring and Management (RMM)** tool, which might be referred to by another name: a **backdoor**.

If you run the file (**in a sandbox**, *obviously*), you just get a simple install screen:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-26.png?w=458)](https://textslashplain.com/wp-content/uploads/2026/04/image-26.png)

After the install has proceeded for a while, the following dialog box is shown:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-27.png?w=561)](https://textslashplain.com/wp-content/uploads/2026/04/image-27.png)

If you hit the big blue **Continue** button, the service is started:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-28.png?w=1024)](https://textslashplain.com/wp-content/uploads/2026/04/image-28.png)

…and your device immediately sets up connections to the infrastructure that will allow the attacker to take control of your device:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-29.png?w=593)](https://textslashplain.com/wp-content/uploads/2026/04/image-29.png)

### Tools and Weapons

*(Note: Microsoft President Brad Smith [wrote a book of this title](https://amzn.to/4ualdc5)).*

This attack demonstrates one of the most challenging parts of cybersecurity: many *tools* can be turned into *weapons* simply by using them maliciously. The dominant use of the AteraAgent is legitimate, but in the hands of an attacker, the impact on the victim is the same as if they had installed malware on their device.

Now, what can Atera do about the abuse of their tool? They’ve done at least the *bare minimum* thing (added a notification screen during the install), but they probably could do more. For example, the screen doesn’t clearly explain the threat, and there’s no button to “*Report Abuse to Atera*” for example. An unanswered two year old [thread](https://www.reddit.com/r/atera/comments/1al5vtv/how_do_i_report_abuse/) on Reddit suggests these Atera-powered attacks have been going on for quite some time, and there have been [high-profile attacks](https://www.broadcom.com/support/security-center/protection-bulletin/seedworm-exploits-atera-agent-in-a-spear-phishing-campaign) in the past. Hopefully they are keeping a close eye on their “Trial” customers as those are the ones most likely to be attackers.

What can a normal computer user do to protect against this attack? Not a ton. Certainly, they should take care when interacting with their PC (e.g. don’t be me and go trolling around in the Junk Mail folders to click on links, take care with file downloads, keep an eye out when asked to make decisions, be paranoid).

A security-conscious Enterprise might block an attack like this by using Application Control software to block all (or unexpected) RMM tools on their devices. Beyond protecting against campaigns like this one, it can also help inhibit [Tech Scams](https://textslashplain.com/2023/09/12/attack-techniques-fullscreen-abuse/).

-Eric

PS: Note that Windows itself ships with an RMM tool called “QuickAssist”, and sadly it has nothing to say about scams in its UI:

[![](https://textslashplain.com/wp-content/uploads/2026/04/image-30.png?w=463)](https://textslashplain.com/wp-content/uploads/2026/04/image-30.png)

### Share this:

* [Share on X (Opens in new window)
  X](https://textslashplain.com/2026/04/24...