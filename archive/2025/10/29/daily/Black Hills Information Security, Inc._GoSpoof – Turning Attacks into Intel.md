---
title: GoSpoof – Turning Attacks into Intel
url: https://www.blackhillsinfosec.com/gospoof-turning-attacks-into-intel/
source: Black Hills Information Security, Inc.
date: 2025-10-29
fetch_date: 2025-10-30T03:11:26.709118
---

# GoSpoof – Turning Attacks into Intel

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
Oct
2025

[Blue Team](https://www.blackhillsinfosec.com/category/blue-team/), [Blue Team Tools](https://www.blackhillsinfosec.com/category/blue-team/tool-blue-team/), [External/Internal](https://www.blackhillsinfosec.com/category/red-team/external/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Intern](https://www.blackhillsinfosec.com/category/author/intern/), [Web App](https://www.blackhillsinfosec.com/category/red-team/web-app/)
[Cyber Deception](https://www.blackhillsinfosec.com/tag/cyber-deception/), [Deceptive Tooling](https://www.blackhillsinfosec.com/tag/deceptive-tooling/), [GoSpoof](https://www.blackhillsinfosec.com/tag/gospoof/)

# [GoSpoof – Turning Attacks into Intel](https://www.blackhillsinfosec.com/gospoof-turning-attacks-into-intel/)

by [Ivan Casamalhuapa](https://www.blackhillsinfosec.com/team/ivan-casamalhuapa/) | BHIS Intern

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/10/GOSPOOF_header.png)

Imagine this: You’re an attacker ready to get their hands on valuable data that you can sell to afford going on a sweet vacation. You do your research, your recon, everything, ensuring that there’s no way this can go wrong. The day of the attack, you brew some coffee, crack your knuckles, and get started. A few hours into the service scan, you come to realize that all the network ports are open, but in use. “*How strange,*” you think, but you can already imagine the beach breeze on your skin, so you persist. Attack after attack and… nothing. You can’t seem to get *anything*.

Meanwhile, the organization’s SOC team now has your IP, dates, timestamps, and attack method—all by running GoSpoof.

## GoSpoof

GoSpoof is a deception tool that aims to ruin an attack operation while making SOC teams’ jobs much more bearable. This is a new version of an old tool known as Portspoof. Using Golang, we are able to modernize this beloved tool and make advanced changes to further the development of other cyber-deception tools.

### **Key Features**

GoSpoof was once able to only spoof ports and slow down attackers; now, it can act as a honeypot with the **-honey** flag, logging IPs, dates, timestamps, and data sent in an attack and save it to a honeypot.log.

This tool has a persistency mode as well that can be triggered with **–boot**. This makes a systemd service that saves your flags and runs the tool on boot. To undo this, you can simply run:

```
sudo ./gospoof -rm
```

It can also run a feature we call “RubberGlue.” This tunnels a connection back at the attacker, essentially making a hacker attack their own system, saving all traffic intercepted in a directory inside hash.txt files that can later be read.

GoSpoof now comes with its own built-in website known as the “Command Center.” Here, a SOC analyst can put their honeypot.log in and receive a breakdown of what IPs are attacking the most in the “Attackers” page, as well as being able to look at payloads sent and filter by day, time, or IP in the “Payloads” page.

Our tool is lightweight, easy to use, and easy to report with. The “Attackers” page even features a pie chart to better visualize attacks.

## Now, Let’s See It in Use

First, we need to pull the repo from Github:

```
git clone https://github.com/blackhillsinfosec/GoSpoof
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/10/Gospoof_01.png)

Then we cd into GoSpoof.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/10/Gospoof_02.png)

And build our Command Center with:

```
go run startup.go
```

This installs all website dependencies.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/10/Gospoof_03.png)

Once completed, we can cd into src, run our iptables rules, and build GoSpoof.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/10/Gospoof_04.png)

We can now use our new features to make a persistent service, launch our Command Center, and log attacks with:

```
└─$ sudo ./goSpoof -i 192.168.171.128 -p 4444 -s ../tools/portspoof_signatures -honey y -WebUI –boot
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/10/Gospoof_05.png)

#### Attacker POV

We launched an attack script and here are the results from an attacker’s point-of-view.

Nmap scan being showed fake banners:

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/10/Gospoof_06.png)

Hydra and Fuzzing fail:

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/10/Gospoof_07.png)

Remote bios scan fail:

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/10/Gospoof_08.png)

Meanwhile, back to the Gospoof user’s POV, all this data is being collected and stored. Here is what you get from the terminal view:

![](https://www...