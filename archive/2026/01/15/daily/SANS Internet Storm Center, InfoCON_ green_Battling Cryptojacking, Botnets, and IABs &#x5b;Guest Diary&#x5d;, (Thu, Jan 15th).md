---
title: Battling Cryptojacking, Botnets, and IABs &#x5b;Guest Diary&#x5d;, (Thu, Jan 15th)
url: https://isc.sans.edu/diary/rss/32632
source: SANS Internet Storm Center, InfoCON: green
date: 2026-01-15
fetch_date: 2026-01-16T03:30:42.316441
---

# Battling Cryptojacking, Botnets, and IABs &#x5b;Guest Diary&#x5d;, (Thu, Jan 15th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Guy Bruneau](/handler_list.html#guy-bruneau "Guy Bruneau")

Threat Level: [green](/infocon.html)

* [previous](/diary/32628)

# [Battling Cryptojacking, Botnets, and IABs [Guest Diary]](/forums/diary/Battling%2BCryptojacking%2BBotnets%2Band%2BIABs%2BGuest%2BDiary/32632/)

**Published**: 2026-01-15. **Last Updated**: 2026-01-15 10:49:10 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Battling%2BCryptojacking%2BBotnets%2Band%2BIABs%2BGuest%2BDiary/32632/#comments)

[This is a Guest Diary by Matthew Presnal, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

Cryptojacking and botnets can pose a greater threat than a simple drain of resources. These organizations have been known to engage in “DDoS for Hire” or even selling off footholds, acting as Initial Access Brokers (IABs). To better understand how to get ahead of the adversary, I am going to walk you through the real-world attacks observed on my DShield honeypot and attempt to better predict their next steps.

**Early Recognition**

As we know from a certain company's model for stopping attacks (I'll let you fill in the blanks), the earlier you are able to break the chain, the better the outcome. While the ideal situation is to have impenetrable defenses, thus making it so you have nothing to worry about, that is just not realistic. If we are able to recognize early signs of a potential attack, i.e recon, we can posture or even preempt the attack by implementing hardening that we may otherwise avoid due to operational impact.

The screenshot below is from recent activity observed on my honeypot. In this instance, the IP points back to a Digital Ocean machine, but I have numerous other accounts of this exact script being run to enumerate the system from several other IPs outside of this range.

![](https://isc.sans.edu/diaryimages/images/Matthew_Presnal_pic1.png)

In the interest of readability, I have supplied the enumeration script here:

![](https://isc.sans.edu/diaryimages/images/Matthew_Presnal_pic5.png)

At this stage, the threat actor already has access (this resulted from SSH spraying), and they are enumerating the machine for kernel info, system architecture, uptime, CPU model and capabilities, GPU info, binary versions, and login info. They then output all of this information in a standardized format to be parsed, either via an automated process or handed off to someone to start building persistence/determining if the system is suitable for the botnet.

In a real environment recognizing this as a potential adversarial first step does a few different things for us in addition to activating the Incident Response Plan (IRP):

1. It gives us the opportunity to ensure adequate coverage of the network
2. An opportunity to start diverting traffic away from a known compromised machine and introducing isolation/quarantining the machine
3. The ability to “play by play” adversarial actions and build detection rules that can be implemented across the network
4. Roll out hardening tailored to the adversarial activity to enact the “Pyramid of Pain” at the TTP level (Bonus points if you are able to attribute the attack real-time)

**Actions on Objective**

The attack chain below was witnessed on the same honeypot, and I believe it to be part of the same “run book” presumably carried out by the cryptojacking and botnet organization “Outlaw":

Actor IP: 197.221.232.44
Kibana GeoIP: Harare, Zimbabwe

![](https://isc.sans.edu/diaryimages/images/Matthew_Presnal_pic6.png)

The first several lines of this chain are more enumeration and situational awareness, gathering more system info, user info, processes, and even which users are logged in with the ‘w’ command. The first real exploitation action starts with the recursive remove command, prepping the system for the SSH persistence mechanism Outlaw is known for.

**Malware**

In the interest of brevity, this section will not go into any real depth but will rather attempt to further flesh out the post-exploitation phase of the attack. As you can see in the screenshots below, the hash of the malware downloaded on the honeypot is identified as a Trojan and a Miner, and it has references to a ‘zombie’ within the strings of the code itself suggesting likely botnet involvement.

![](https://isc.sans.edu/diaryimages/images/Matthew_Presnal_pic2.png)

![](https://isc.sans.edu/diaryimages/images/Matthew_Presnal_pic3.png)

This malware stems from a series of Chinese IPs that are all within the same ASN. While I cannot directly relate these to the suspected “Outlaw” scripts earlier, the Kibana logs are interesting for these IPs. They all start with a successful SSH connection and quickly move to an SFTP transfer of the malware. The malware itself appears to be a Go binary which is a deviation from the expected “Perl-based backdoor” noted by TrendMicro [[4](https://isc.sans.edu/diary/DShield%2BSensor%2BSetup%2Bin%2BAzure/29370)].
With this unlikely to be “Outlaw” directly, I am choosing to include this activity for two main reasons:

1) I am using “Outlaw” activity as more of a threat model rather than the group being the primary subject for this post
2) Each occurrence of this payload is precluded by activity identical or nearly identical to the scanning and persistence discussed earlier

This behavior is suggestive of either an evolution of processes by implementing specialization within the organization or the IAB-like activity mentioned earlier.

This malware was the result of:

shield@dshield:/srv/cowrie/var/lib/cowrie/downloads$ sudo strings -a 649eecfd7b02b59248ef5d1fce494e2f1b9d2fc20eef43fc4c74be8bc10ce1c1 -n 80 | less

**What Can Be Done?**

In the Early Recognition section, I gave a few suggestions of what you can do to cutoff the threat actor at the first sign of intrusion. This section aims to use some best practices to defend the network against this type of activity.

* Enforce strong authentication controls for remote access by disabling password-based SSH authentication in favor of key-based authentication
* Enforce multi-factor authentication (MFA) for administrative access were supported
* Use TCP Wrappers (/etc/hosts.allow and /etc/hosts.deny) as a defense-in-depth mechanism to restrict access to known management networks and reduce unauthenticated connection attempts
* Apply file integrity monitoring (FIM) to critical system and configuration files, including /etc/hosts.allow, /etc/hosts.deny, user .ssh directories, authorized\_keys, and cron configurations
* Monitor for post-exploitation enumeration activity by alerting on rapid execution of common reconnaissance commands such as uname, lscpu, cat /proc/cpuinfo, w, top, and crontab -l
* Detect and investigate destructive or preparatory commands often used to enable persistence, such as recursive deletion of .ssh directories, use of chattr
* Routinely audit user accounts, group memberships, and privilege assignments
* Centralize authentication, process execution, and network logs, ensuring a minimum of 90 days log retention to support incident response and threat hunting activities
* Perform routine patching and vulnerability management for operating systems and exposed services to reduce the effectiveness of automated exploitation and scanning frameworks
* Test and exercise the incident response plan (IRP) to ensure rapid containment, isolation, and investigation can occur when early indicators of compromise are detected
* Consider investing resources into Threat Hunting and Cyber Threat Intelligence to better identify and predict adversarial activity

**Conclusion**

This style of attack (Password spray of SSH -> System enumeration -> Persistence mechanisms via SSH -> Transfer of malicious file) is the most common attack I witnessed while monitoring DShield via Kibana. While it makes sense for ...