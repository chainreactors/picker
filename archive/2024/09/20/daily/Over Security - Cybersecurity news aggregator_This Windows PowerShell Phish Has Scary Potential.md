---
title: This Windows PowerShell Phish Has Scary Potential
url: https://krebsonsecurity.com/2024/09/this-windows-powershell-phish-has-scary-potential/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-20
fetch_date: 2025-10-06T18:29:02.240084
---

# This Windows PowerShell Phish Has Scary Potential

Advertisement

[![](/b-sysdig/1.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000460_1240x110)

Advertisement

[![](/b-action1/2.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# This Windows PowerShell Phish Has Scary Potential

September 19, 2024

[60 Comments](https://krebsonsecurity.com/2024/09/this-windows-powershell-phish-has-scary-potential/#comments)

Many **GitHub** users this week received a novel phishing email warning of critical security holes in their code. Those who clicked the link for details were asked to distinguish themselves from bots by pressing a combination of keyboard keys that causes **Microsoft Windows** to download password-stealing malware. While it’s unlikely that many programmers fell for this scam, it’s notable because less targeted versions of it are likely to be far more successful against the average Windows user.

A reader named Chris shared an email he received this week that spoofed GitHub’s security team and warned: “Hey there! We have detected a security vulnerability in your repository. Please contact us at https://github-scanner[.]com to get more information on how to fix this issue.”

![](https://krebsonsecurity.com/wp-content/uploads/2024/09/powerphish.png)

Visiting that link generates a web page that asks the visitor to “Verify You Are Human” by solving an unusual CAPTCHA.

![](https://krebsonsecurity.com/wp-content/uploads/2024/09/verifyhuman.png)

This malware attack pretends to be a CAPTCHA intended to separate humans from bots.

Clicking the “I’m not a robot” button generates a pop-up message asking the user to take three sequential steps to prove their humanity. Step 1 involves simultaneously pressing the keyboard key with the Windows icon and the letter “R,” which opens a Windows “Run” prompt that will execute any specified program that is already installed on the system.

![](https://krebsonsecurity.com/wp-content/uploads/2024/09/githubscanner.png)

Executing this series of keypresses prompts the built-in Windows Powershell to download password-stealing malware.

Step 2 asks the user to press the “CTRL” key and the letter “V” at the same time, which pastes malicious code from the site’s virtual clipboard.

Step 3 — pressing the “Enter” key — causes Windows to launch a **PowerShell** command, and then fetch and execute a malicious file from github-scanner[.]com called “**l6e.exe**.”

PowerShell is a powerful, cross-platform automation tool built into Windows that is designed to make it simpler for administrators to automate tasks on a PC or across multiple computers on the same network.

According to [an analysis](https://www.virustotal.com/gui/file/d737637ee5f121d11a6f3295bf0d51b06218812b5ec04fe9ea484921e905a207/details) at the malware scanning service **Virustotal.com**, the malicious file downloaded by the pasted text is called **Lumma Stealer**, and it’s designed to snarf any credentials stored on the victim’s PC.

This phishing campaign may not have fooled many programmers, who no doubt natively understand that pressing the Windows and “R” keys will open up a “Run” prompt, or that Ctrl-V will dump the contents of the clipboard.

But I bet the same approach would work just fine to trick some of my less tech-savvy friends and relatives into running malware on their PCs. I’d also bet none of these people have ever heard of PowerShell, let alone had occasion to intentionally launch a PowerShell terminal.

Given those realities, it would be nice if there were a simple way to disable or at least heavily restrict PowerShell for normal end users for whom it could become more of a liability.

However, Microsoft strongly advises against nixing PowerShell because some core system processes and tasks may not function properly without it. What’s more, doing so requires tinkering with sensitive settings in the Windows registry, which can be a dicey undertaking even for the learned.

Still, it wouldn’t hurt to share this article with the Windows users in your life who fit the less-savvy profile. Because this particular scam has a great deal of room for growth and creativity.

*This entry was posted on Thursday 19th of September 2024 03:39 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Latest Warnings](https://krebsonsecurity.com/category/latest-warnings/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[CAPTCHA](https://krebsonsecurity.com/tag/captcha/) [GitHub](https://krebsonsecurity.com/tag/github/) [Lumma Stealer](https://krebsonsecurity.com/tag/lumma-stealer/) [Microsoft PowerShell](https://krebsonsecurity.com/tag/microsoft-powershell/) [Virustotal.com](https://krebsonsecurity.com/tag/virustotal-com/)

Post navigation

[← Scam ‘Funeral Streaming’ Groups Thrive on Facebook](https://krebsonsecurity.com/2024/09/scam-funeral-streaming-groups-thrive-on-facebook/)
[Timeshare Owner? The Mexican Drug Cartels Want You →](https://krebsonsecurity.com/2024/09/timeshare-owner-the-mexican-drug-cartels-want-you/)

## 60 thoughts on “This Windows PowerShell Phish Has Scary Potential”

1. Tom [September 19, 2024](https://krebsonsecurity.com/2024/09/this-windows-powershell-phish-has-scary-potential/#comment-615527)

   Hi, nextdns to block the phishing website and hardentools to disable powershell.

   All the tools to block phishing scams already exist.

   1. BitcoDavid [September 20, 2024](https://krebsonsecurity.com/2024/09/this-windows-powershell-phish-has-scary-potential/#comment-615572)

      Why would you want to disable Powershell? The URL in this phishing scam is github-scanner[.]com, not github[.]com. Learning how to read and understand URLs might serve you better than disabling the most useful app Microsoft ever created. Also, as the author stated in the article, Windows + R opens the run dialog, and CTL + V dumps the clipboard. All this happens on your screen in front of your eyes. If you push the enter key from there, your problem isn’t just limited to malware.

      1. an\_n [September 20, 2024](https://krebsonsecurity.com/2024/09/this-windows-powershell-phish-has-scary-potential/#comment-615602)

         The average user has no more use for powershell than they do the cmd line or even less. Since they aren’t using it and malware is targeting it, the reason is pretty obvious why the average user might want to disable it.

         1. Jammon [October 10, 2024](https://krebsonsecurity.com/2024/09/this-windows-powershell-phish-has-scary-potential/#comment-616839)

            Not really true, as often time as deskside support, you’ll need access to command line or powershell to fix an issue specific to the profile. It also does not stop the run command from functioning.
      2. Brett Mitchell [September 22, 2024](https://krebsonsecurity.com/2024/09/this-windows-powershell-phish-has-scary-potential/#comment-615650)

         > Learning how to read and understand URLs might serve you better than disabling the most useful app Microsoft ever created.

         Are you suggesting that the best defense is to rely on uninformed users educating themselves entirely on their own volition? I hope you don’t work in security…
   2. WhiteHatNani [September 23, 2024](https://krebsonsecurity.com/2024/09/this-windows-powershell-phish-has-scary-potential/#comment-615674)

      Except how to stop humans from believing lies…and how to block BEFORE they click on new, unknown bait…
2. Joseph [September 19, 2024](https://krebsonsecurity....