---
title: New PowerShell History Defense Evasion Technique
url: https://www.blackhillsinfosec.com/new-powershell-history-defense-evasion-technique/
source: Black Hills Information Security
date: 2022-11-30
fetch_date: 2025-10-04T00:05:04.696976
---

# New PowerShell History Defense Evasion Technique

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

29
Nov
2022

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Carrie Roberts](https://www.blackhillsinfosec.com/category/author/carrie-roberts/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Recon](https://www.blackhillsinfosec.com/category/red-team/recon/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/)

# [New PowerShell History Defense Evasion Technique](https://www.blackhillsinfosec.com/new-powershell-history-defense-evasion-technique/)

[Carrie Roberts](https://twitter.com/OrOneEqualsOne) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2022/11/BLOG_chalkboard_006905-1024x576.jpg)

PowerShell incorporates the handy feature of writing commands executed to a file to make them easy to refer back to later. This functionality is provided by the PSReadline module. This feature is helpful from a usability perspective but can be a tool that hackers use against you.

For example, if sensitive information like passwords are entered into the PowerShell command line, they will also be added to the history file and a hacker can review this history to discover that sensitive information.

In an effort to solve this issue, the PSReadline module version v2.0.4+ will skip adding a command line to the history file if it contains sensitive words like (more info [here](https://learn.microsoft.com/en-us/powershell/module/psreadline/about/about_psreadline?view=powershell-5.1#command-history)):

* Password
* Asplaintext
* Token
* Apikey
* Secret

PowerShell v7.0.11+ ships with a PSReadline version that supports this feature out-of-the-box, but Windows PowerShell version 5.1 ships with PSReadline version 2.0.0 and doesn’t support this feature, however it can easily be updated.

Let’s see the sensitive history scrubbing in action.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2022/11/Picture1.png)

In the image above, we ran three commands, one of which contained one of the words that trigger the “sensitive” filter. Notice that the password line is not listed when we “cat” (aka print to screen) the history file.

This is kind of nifty, but it also makes for a really easy defense evasion technique where a hacker can control which of their commands show up in the history file.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2022/11/Picture2.png)

In the image above, we were able to keep the second command from being recorded in the history file by simply adding a comment containing one of the “sensitive” words.

This really isn’t an earth-shattering discovery because attackers have always been able to open the history file and individually remove commands from it if they wanted to. Nevertheless, this does make this defense evasion tactic even easier and is a trick that I would use on my next red teaming engagement.

Another interesting option for defense evasion is to define your own code for deciding whether a command is written to the history file. We could disable all history logging for the current session as follows:

* Set-PSReadLineOption -AddToHistoryHandler { return $false }

The “AddToHistoryHandler” receives the current command as the $line variable and then returns $true if the line should be written to the history file. Here we simply return $false so nothing gets added to the history file for the current session. On the defensive side, we could keep an eye out for any funny business when the AddToHistoryHandler parameter is used. In fact, keeping an eye on the use of all the PSReadLineOption functions would probably be a good idea. Here are a few more examples of defense evasion.

Prevent logging: Set-PSReadlineOption -HistorySaveStyle SaveNothing

Delete history file: Remove-Item (Get-PSReadlineOption).HistorySavePath

Set alternate file path: Set-PSReadLineOption -HistorySavePath $env:TEMP\out.txt

Use ContrainedLanguage mode: $ExecutionContext.SessionState.LanguageMode = “ConstrainedLanguage”

If you are interested in learning more about PowerShell topics such as ‘Just Enough Admin’, PowerShell remoting, language modes and more, check out my 16-hour course called “PowerShell For InfoSec” [here](https://www.antisyphontraining.com/powershell-for-infosec-what-you-need-to-know/).

---

---

You can learn more from Carrie in her classes!

Check them out here:

**[Attack Emulation Tools: Atomic Red Team, CALDERA and More](https://www.antisyphontraining.com/attack-emulation-tools-atomic-red-team-caldera-and-more-w-carrie-roberts/)**

[**PowerShell for InfoSec**](https://w...