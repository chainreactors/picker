---
title: When your IoT Device Logs in as Admin, It&#x3f;s too Late&#x21; &#x5b;Guest Diary&#x5d;, (Wed, Mar 11th)
url: https://isc.sans.edu/diary/rss/32788
source: SANS Internet Storm Center, InfoCON: green
date: 2026-03-12
fetch_date: 2026-03-13T04:07:57.711902
---

# When your IoT Device Logs in as Admin, It&#x3f;s too Late&#x21; &#x5b;Guest Diary&#x5d;, (Wed, Mar 11th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jan Kopriva](/handler_list.html#jan-kopriva "Jan Kopriva")

Threat Level: [green](/infocon.html)

* [previous](/diary/32786)

# [When your IoT Device Logs in as Admin, It?s too Late! [Guest Diary]](/forums/diary/When%2Byour%2BIoT%2BDevice%2BLogs%2Bin%2Bas%2BAdmin%2BIts%2Btoo%2BLate%2BGuest%2BDiary/32788/)

**Published**: 2026-03-11. **Last Updated**: 2026-03-12 01:19:35 UTC
**by** [Adam Thorman, SANS.edu BACS Student](/handler_list.html#adam-thorman,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/When%2Byour%2BIoT%2BDevice%2BLogs%2Bin%2Bas%2BAdmin%2BIts%2Btoo%2BLate%2BGuest%2BDiary/32788/#comments)

[This is a Guest Diary by Adam Thorman, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

**Introduction**

Have you ever installed a new device on your home or company router? Even when setup instructions are straightforward, end users often skip the step that matters most: changing default credentials. The excitement of deploying a new device frequently outweighs the discipline of securing it.
This diary explains a little real-world short story and then walks through my own internship observations overseeing a honeypot and vulnerability assessment that demonstrate just how quickly default credentials are discovered and abused.

**Default Credentials in a Real-World Example**

Default usernames and passwords remain the most exploited attack vector for Internet of Things (IoT) devices. Whether installation is performed by an end user or a contracted vendor, organizations must have a defined process to ensure credentials are changed immediately. Without that process, compromise is often a matter of when, not if.
During a routine vulnerability assessment at work, I identified multiple IP addresses that were accessible using default credentials. These IPs belonged to a newly installed security system monitoring sensitive material. The situation was worse than expected:

* The system was not placed on the proper VLAN
* Basic end user machines could reach it
* The username “root” remained unchanged and password “password” was changed to “admin”

This configuration was still trivial to guess and exploit, regardless of whether access was internal or external. From my point of view, it was easily guessed and accessed, like Figure 1 below.

![](https://isc.sans.edu/diaryimages/images/Adam_Thorman_pic1.jpg)
Figure 1 - Meme of Easily Bypassed Security Controls

**What Logs Showed?**

To better understand how common this issue is, I analyzed SSH and Telnet traffic across an eight-day period (January 18–25) and compared it with more recent data. This ties into the story above based on how many devices are kept with their default settings or slightly changed with common trivial combinations. These graphs were pulled from the Internet Storm Center (ISC) My SSH Reports page [[2](https://isc.sans.edu/mysshreports/)], while the comparison was generated with ChatGPT tool.

JANUARY 27TH, 2026
![](https://isc.sans.edu/diaryimages/images/Adam_Thorman_pic2.png)

FEBRUARY 17TH, 2026
![](https://isc.sans.edu/diaryimages/images/Adam_Thorman_pic3.png)

COMPARISON
![](https://isc.sans.edu/diaryimages/images/Adam_Thorman_pic4.png)

Across both datasets:

* The username “root” remained dominant at ~39%
* The password “123456” increased from 15% to 27%
* These combinations strongly resembled automated botnet scanning behavior

This aligns with publicly known credential lists that attackers use for large scale reconnaissance.

**Successful Connections**

During the analysis window, I observed:

* 44,269 failed connection attempts
* 1,286 successful logins
* A success rate of only 2.9%

That percentage may appear low, but it still resulted in over a thousand compromised sessions.
To perform this analysis, I parsed Cowrie JSON logs using jq, converted them to CSV files, and consolidated them into a single spreadsheet.

From the 1,286 successful connections:

* 621 used the username root
* 154 used admin as the password
* 406 shared the same HASSH fingerprint 2ec37a7cc8daf20b10e1ad6221061ca5
* 47 sessions matched all three indicators

The matched session to that hash is shown in APPENDIX A.

**What Attackers did After Logging in?**

Four session IDs stood out during review of the full report:
1. eee64da853a9
2. f62aa78aca0b
3. 308d24ec1d36
4. f0bc9f078bdd

Sessions 1 and 4 focused on reconnaissance, executing commands to gather system details such as CPU, uptime, architecture, and GPU information.

With the use of ChatGPT [[3](https://chatgpt.com)], I was able to compare each session and the commands the attacker attempted to use.  It was disclosed that Sessions 1 and 4 had reconnaissance from the topmost digital fingerprint HASSH.  They both had the same command but with different timestamps. Refer to APPENDIX B for Session ID 1 and 2 command outputs.

Sessions **2** and **3** demonstrated more advanced behavior:

* SSH key persistence
* Credential manipulation
* Attempts to modify account passwords

Session 308d24ec1d36 ranked as the most severe due to attempted password changes and persistence mechanisms that could have resulted in long term control if it was attempted on a real-world medium. Refer to APPENDIX C for Session ID 2 and 3 command outputs.

**Failed Attempts Tell a Bigger Story**

Failed authentication attempts revealed even more.

One digital fingerprint alone accounted for 18,846 failed attempts, strongly suggesting botnet driven scanning activity.

On January 19, 2026, there were 14,057 failed attempts in a single day — a significant spike compared to surrounding dates.

From a Security Operations Center (SOC) analyst’s perspective, this level of activity represents a serious exposure risk.  It could mean a botnet scanning campaign like the one observed by GreyNoise in late August 2025 [[4](https://eclypsium.com/blog/cisco-asa-scanning-surge-cyberattack/)].

Below is a visual of the top usernames, passwords, and hashes across the analyzed timeframe.

![](https://isc.sans.edu/diaryimages/images/Adam_Thorman_pic5.png)
Figure 2 - Top Usernames, Passwords, and Digital Fingerprints

To note in comparison to the other days, where it’s not even half of 14k, Figure 3 below dictates the spread.
![](https://isc.sans.edu/diaryimages/images/Adam_Thorman_pic6.png)
Figure 3 – Failed Connection Attempts Over Time

**Best Practices to Follow Towards Resolving Default Credentials**

The SANS Cybersecurity Policy Template for Password Construction Standard states that it “applies to all passwords including but not limited to user-level accounts, system-level accounts, web accounts, e-mail accounts, screen saver protection, voicemail, and local router logins.” More specially, the document also states that “strong passwords that are long, the more characters a password has the stronger it is,” and they “recommend a minimum of 16 characters in all work-related passwords [6].”

Establish an immediate policy to change the default password of IoT devices, such an example is a network printer that is shipped with default usernames and passwords [7].

**Practical Experience Without the Real-World Disaster**

Having access to a controlled sandbox environment, such as a honeypot lab, provides valuable hands-on experience for cybersecurity practitioners.
Sometimes you may need to deal with and see the real-world disaster in a controlled environment to deal with it and see the ripple effect it may produce.

**Why Might this Apply to you?**

MITRE ATT&CK explicitly documents adversary use of manufacturers set default credentials on control systems. They stress that it must be changed as soon as possible.
This isn’t just an enterprise issue. The same risks apply to:

* Home routers
* Networked cameras
* Printers
* NAS devices

For hiring managers, even job postings that disclose specific infrastructure details can unintention...