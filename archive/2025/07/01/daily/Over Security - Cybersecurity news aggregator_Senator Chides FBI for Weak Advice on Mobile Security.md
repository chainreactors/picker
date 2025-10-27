---
title: Senator Chides FBI for Weak Advice on Mobile Security
url: https://krebsonsecurity.com/2025/06/senator-chides-fbi-for-weak-advice-on-mobile-security/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-01
fetch_date: 2025-10-06T23:56:50.417414
---

# Senator Chides FBI for Weak Advice on Mobile Security

Advertisement

[![](/b-knowbe4/36.jpg)](https://www.knowbe4.com/resources/kits/cybersecurity-awareness-month?utm_source=Krebs&utm_medium=display&utm_campaign=cybersecurityawarenessmonth&utm_content=hrm+)

Advertisement

[![](/b-action1/2.jpg)](https://action1.com/double-endpoints-free-cam2025/?utm_source=paidmedia&refid=Display_CAM_Krebs)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Senator Chides FBI for Weak Advice on Mobile Security

June 30, 2025

[27 Comments](https://krebsonsecurity.com/2025/06/senator-chides-fbi-for-weak-advice-on-mobile-security/#comments)

Agents with the **Federal Bureau of Investigation** (FBI) briefed Capitol Hill staff recently on hardening the security of their mobile devices, after a contacts list stolen from the personal phone of the White House Chief of Staff **Susie Wiles** was reportedly used to fuel a series of text messages and phone calls impersonating her to U.S. lawmakers. But in a letter this week to the FBI, one of the Senate’s most tech-savvy lawmakers says the feds aren’t doing enough to recommend more appropriate security protections that are already built into most consumer mobile devices.

![](https://krebsonsecurity.com/wp-content/uploads/2025/06/wyden-patel-letter.png)

On May 29, **The Wall Street Journal** [reported](https://www.wsj.com/politics/policy/federal-authorities-probe-effort-to-impersonate-white-house-chief-of-staff-65da0d59) that federal authorities were investigating a clandestine effort to impersonate Ms. Wiles via text messages and in phone calls that may have used AI to spoof her voice. According to The Journal, Wiles told associates her cellphone contacts were hacked, giving the impersonator access to the private phone numbers of some of the country’s most influential people.

The execution of this phishing and impersonation campaign — whatever its goals may have been — suggested the attackers were financially motivated, and not particularly sophisticated.

“It became clear to some of the lawmakers that the requests were suspicious when the impersonator began asking questions about Trump that Wiles should have known the answers to—and in one case, when the impersonator asked for a cash transfer, some of the people said,” the Journal wrote. “In many cases, the impersonator’s grammar was broken and the messages were more formal than the way Wiles typically communicates, people who have received the messages said. The calls and text messages also didn’t come from Wiles’s phone number.”

Sophisticated or not, the impersonation campaign was soon [punctuated](https://www.justice.gov/opa/pr/after-two-day-manhunt-suspect-charged-shooting-two-minnesota-lawmakers-and-their-spouses) by the murder of Minnesota House of Representatives Speaker **Emerita Melissa Hortman** and her husband, and the shooting of Minnesota State Senator **John Hoffman** and his wife. So when FBI agents offered in mid-June to brief U.S. Senate staff on mobile threats, more than 140 staffers took them up on that invitation (a remarkably high number considering that no food was offered at the event).

But according to **Sen. Ron Wyden** (D-Ore.), the advice the FBI provided to Senate staffers was largely limited to remedial tips, such as not clicking on suspicious links or attachments, not using public wifi networks, turning off bluetooth, keeping phone software up to date, and rebooting regularly.

“This is insufficient to protect Senate employees and other high-value targets against foreign spies using advanced cyber tools,” Wyden wrote in [a letter](https://www.wyden.senate.gov/download/wyden-letter-to-fbi-defensive-cyber-advice) sent today to **FBI Director Kash Patel**. “Well-funded foreign intelligence agencies do not have to rely on phishing messages and malicious attachments to infect unsuspecting victims with spyware. Cyber mercenary companies sell their government customers advanced ‘zero-click’ capabilities to deliver spyware that do not require any action by the victim.”

Wyden stressed that to help counter sophisticated attacks, the FBI should be encouraging lawmakers and their staff to enable anti-spyware defenses that are built into Apple’s iOS and Google’s Android phone software.

These include Apple’s [Lockdown Mode](https://support.apple.com/en-us/105120), which is designed for users who are worried they may be subject to targeted attacks. Lockdown Mode restricts non-essential iOS features to reduce the device’s overall attack surface. Google Android devices carry a similar feature called [Advanced Protection Mode](https://support.google.com/accounts/answer/9764949?hl=en).

Wyden also urged the FBI to update its training to recommend a number of other steps that people can take to make their mobile devices less trackable, including the use of ad blockers to guard against malicious advertisements, [disabling ad tracking IDs in mobile devices](https://krebsonsecurity.com/2024/10/the-global-surveillance-free-for-all-in-mobile-ad-data/), and opting out of commercial data brokers (the suspect charged in the Minnesota shootings reportedly [used multiple people-search services](https://krebsonsecurity.com/wp-content/uploads/2025/06/minnshooting-peoplesearch.png) to find the home addresses of his targets).

The senator’s letter notes that while the FBI has recommended all of the above precautions in various advisories issued over the years, the advice the agency is giving now to the nation’s leaders needs to be more comprehensive, actionable and urgent.

“In spite of the seriousness of the threat, the FBI has yet to provide effective defensive guidance,” Wyden said.

**Nicholas Weaver** is a researcher with the **International Computer Science Institute**, a nonprofit in Berkeley, Calif. Weaver said Lockdown Mode or Advanced Protection will mitigate many vulnerabilities, and should be the default setting for all members of Congress and their staff.

“Lawmakers are at exceptional risk and need to be exceptionally protected,” Weaver said. “Their computers should be locked down and well administered, etc. And the same applies to staffers.”

Weaver noted that Apple’s Lockdown Mode has a track record of blocking zero-day attacks on iOS applications; in September 2023, **Citizen Lab** [documented](https://krebsonsecurity.com/2023/09/adobe-apple-google-microsoft-patch-0-day-bugs/) how Lockdown Mode foiled a zero-click flaw capable of installing spyware on iOS devices without any interaction from the victim.

![](https://krebsonsecurity.com/wp-content/uploads/2022/09/lockdownmode.png)

Earlier this month, Citizen Lab researchers [documented a zero-click attack](https://citizenlab.ca/2025/06/first-forensic-confirmation-of-paragons-ios-mercenary-spyware-finds-journalists-targeted/) used to infect the iOS devices of two journalists with Paragon’s Graphite spyware. The vulnerability could be exploited merely by sending the target a booby-trapped media file delivered via iMessage. Apple also recently updated its advisory for the zero-click flaw (CVE-2025-43200), noting that it was mitigated as of iOS 18.3.1, which was released in February 2025.

Apple has not commented on whether CVE-2025-43200 could be exploited on devices with Lockdown Mode turned on. But HelpNetSecurity [observed](https://www.helpnetsecurity.com/2025/06/13/ios-zero-click-attacks-used-to-deliver-graphite-spyware-cve-2025-43200/) that at the same time Apple addressed CVE-2025-43200 back in February, the company fixed another vulnerability flagged by Citizen Lab researcher **Bill Marczak**: [CVE-2025-24200](https://support.apple.com/en-us/122174), which Apple said was used in an extremely sophisticated *physical* attack against specific targeted indivi...