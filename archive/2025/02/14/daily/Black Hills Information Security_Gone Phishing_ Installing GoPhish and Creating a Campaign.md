---
title: Gone Phishing: Installing GoPhish and Creating a Campaign
url: https://www.blackhillsinfosec.com/installing-gophish-and-creating-a-campaign/
source: Black Hills Information Security
date: 2025-02-14
fetch_date: 2025-10-06T20:36:16.103534
---

# Gone Phishing: Installing GoPhish and Creating a Campaign

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

13
Feb
2025

[External/Internal](https://www.blackhillsinfosec.com/category/red-team/external/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Nick Caswell](https://www.blackhillsinfosec.com/category/author/nick-caswell/), [Phishing](https://www.blackhillsinfosec.com/category/red-team/phishing/), [Red Team](https://www.blackhillsinfosec.com/category/red-team/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/), [Social Engineering](https://www.blackhillsinfosec.com/category/red-team/social-engineering/)
[GoPhish](https://www.blackhillsinfosec.com/tag/gophish/), [Mail Security](https://www.blackhillsinfosec.com/tag/mail-security/), [Phishing Campaign](https://www.blackhillsinfosec.com/tag/phishing-campaign/)

# [Gone Phishing: Installing GoPhish and Creating a Campaign](https://www.blackhillsinfosec.com/installing-gophish-and-creating-a-campaign/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/NCaswell-150x150.png)

| [Nick Caswell](https://www.blackhillsinfosec.com/team/nick-caswell/)

*Nick has been tinkering with technology for the last 20 years in both professional and personal capacities. He has held a variety of technical roles and has experience with an array of software and hardware solutions used in enterprise environments. As a security analyst for Black Hills Information Security, Nick continues to pursue his passion of learning how a systems works, how to misuse it, and how to protect it.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/BLOG_chalkboard_00708.png)

GoPhish provides a nice platform for creating and running phishing campaigns. This blog will guide you through installing GoPhish and creating a campaign.

For this blog we will target our fictitious company, InfoTekExpress. A look-a-like domain, infotekexp**N**ess.com, was purchased for the sending domain and landing pages. Additionally, other things were done behind the scenes:

* DMARC and SPF records were configured in accordance with our third-party SMTP sending service provider.
* DNS A records for @ and online.microsoft were created and pointed towards the GoPhish server.
* Microsoft 365 email filter rules:
  + Added mail flow rule to set SCL to 0 for “infotekexpness.com”
  + Added the sender as “trusted” sender through PowerShell online

### **Setup**

We are using Debian 12 and GoPhish version 0.12.1 for this blog.

First, we downloaded GoPhish with the following command:

```
wget "https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip"
```

Next, we executed the following commands to extract the archive into a folder named GoPhish, open the directory, and add the execute permission to the GoPhish binary.

```
unzip gophish-v0.12.1-linux-64bit.zip -d gophish
cd gophish
chmod +x gophish
```

Create a screen session and launch GoPhish:

```
screen -S gophish
./gophish
```

![Launching GoPhish](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/Selection_001-1024x176.png)

When GoPhish starts for the first time it will display the admin password and the admin URL.

If your operating system has a GUI, you can connect to the URL with a browser.

If your GoPhish server does not have a GUI, you can use a system with a GUI and SSH client you can create a local port forward using:

```
ssh -N -L 3333:127.0.0.1:3333 <username>@<GoPhishServer>
```

Log in to the GoPhish admin URL with the password from the terminal, and don’t forget to update the password.

![Log in to GoPhish](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/Selection_002.png)

### **User Management**

Add your targets to GoPhish by creating a new group under User & Groups > New Group.

![Add targets to GoPhish](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/Selection_003.png)

You can import users through a comma-delimited CSV file or manually enter their information.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/Selection_004-734x1024.png)

### **Sending Profile**

Create a new sending profile by navigating to Sending Profiles > New Profile.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/Selection_005.png)

Configure sending profiles for any sending domain you’ll use.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/02/Selection_006-677x1024.png)

Make sure you configure the “SMTP From” to an email address with your sending domain. This domain will be used to perform SPF checks on sent messages.

By default, GoPhish includes an X-Mailer header with a value of “GoPhish”. This is a huge red flag for most email security produ...