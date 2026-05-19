---
title: ICMP Walkthrough — OffSec Lab (Privilege Escalation via hping3)
url: https://infosecwriteups.com/icmp-walkthrough-offsec-lab-privilege-escalation-via-hping3-50ebb4589cae?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-18
fetch_date: 2026-05-19T06:03:29.857753
---

# ICMP Walkthrough — OffSec Lab (Privilege Escalation via hping3)

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ficmp-walkthrough-offsec-lab-privilege-escalation-via-hping3-50ebb4589cae&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ficmp-walkthrough-offsec-lab-privilege-escalation-via-hping3-50ebb4589cae&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-50ebb4589cae---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-50ebb4589cae---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# ICMP Walkthrough — OffSec Lab (Privilege Escalation via hping3)

[![Sana Jalil](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*6u4wEjiGk55yPVgE)](https://medium.com/%40sanajalil9090?source=post_page---byline--50ebb4589cae---------------------------------------)

[Sana Jalil](https://medium.com/%40sanajalil9090?source=post_page---byline--50ebb4589cae---------------------------------------)

5 min read

·

Jan 27, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D50ebb4589cae&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Ficmp-walkthrough-offsec-lab-privilege-escalation-via-hping3-50ebb4589cae&source=---header_actions--50ebb4589cae---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

**About this Lab**

This lab emphasizes systematic network and web service enumeration to identify attack surfaces and misconfigurations. Identified web application components were analyzed to uncover exploitable conditions leading to initial access. Post‑exploitation activities focused on local enumeration and privilege escalation, where misconfigured sudo permissions were abused to obtain elevated privileges.

The lab reinforces a structured, real‑world penetration testing methodology, aligning with professional offensive security assessments.

**Note on IP Address Change**
During testing, the target machine was reset, which resulted in a change of IP address. All references below have been normalized to **192.168.145.218** for clarity.

**Service Enumeration**

A comprehensive service and version enumeration was performed using Nmap to identify open ports and running services on the target system.

The — min-rate option was used to accelerate the scan due to the controlled OffSec lab environment. In real‑world engagements, aggressive rate limits should be avoided to reduce detection risk, prevent service disruption, and comply with operational constraints.

An HTTP service was identified on 192.168.145.218:80, prompting targeted web enumeration to identify accessible resources and potential attack vectors.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

**Exploit Identification and PoC Analysis**

Searchsploit was used to identify any publicly known vulnerabilities and available proof-of-concept exploits relevant to the discovered service.

Press enter or click to view image in full size

![]()

I confirmed the target runs Monitorr 1.7.6m, which is vulnerable to unauthenticated RCE. After locating a public PoC, I reviewed the code to verify its preconditions and executed it in a disposable lab environment. The PoC successfully allowed arbitrary command execution on the web server as the web user, confirming the RCE.

Press enter or click to view image in full size

![]()

Running the exploit uploads a PHP file to`/assets/php/`, which may be accessible and executable by the web server.

Press enter or click to view image in full size

![]()

Executing the exploit resulted in command execution on the target, allowing me to spawn a shell as the web user. A connection was successfully established back to my listener, confirming the shell.

**Initial Foothold**

Press enter or click to view image in full size

![]()

After obtaining a shell, I navigated through the filesystem and enumerated the `/home` directory, where I discovered a `fox` folder. Browsing this directory revealed several files containing potentially valuable information.

![]()

I attempted to access the `devel` directory, but access was denied due to insufficient permissions.The directory is owned by the user **fox**, and `www-data` does not have the required read permissions, indicating that further escalation or permission changes are needed to access its contents.

## Get Sana Jalil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

**Credential Harvesting**

![]()

Reading the reminder file revealed a clue about password hashing, suggesting that `crypt.php` could be used to analyze stored credentials. Although direct access to the `devel` directory was denied, the `crypt.php` file inside was readable. The script uses PHP’s `crypt()` function on a hardcoded string, indicating a weak hashing mechanism. The output contained what appeared to be the `fox` user password hash, so I saved the response and created a local copy of `crypt.php` for analysis. The next step is to crack the hash, verify the credentials using available login vectors, and continue controlled post-exploitation enumeration.

Press enter or click to view image in full size

![]()

**Privilege Escalation Preparation**

The extracted credentials were verified by logging in via SSH as the fox user. Once on the system, I checked `sudo` privileges using `sudo -l` to identify any commands that could be executed with elevated rights. The output was saved for analysis and will inform the next controlled privilege escalation.

Press enter or click to view image in full size

![]()

Privilege escalation reconnaissance using `sudo -l` revealed that the fox user is permitted to execute hping3 with elevated privileges, representing a potential sudo misconfiguration. I then consulted GTFOBins to assess whether `hping3`, when allowed via sudo, could be abused for local privilege escalation. GTFOBins documents potential abuse paths for `hping3`, confirming it as a valid escalation vector to investigate further in a controlled environment.

**Final Compromise**

At this stage, SSH access was validated by logging in as the fox user, allowing further local enumeration.

Press enter or click to view image in full size

![]()

Open a second terminal and establish an SSH session as the fox user. At this point, both sessions are running on 127.0.0.1.

Press enter or click to view image in full size

![]()

O...