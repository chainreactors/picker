---
title: EyeWitness Cheatsheet
url: https://www.blackhillsinfosec.com/eyewitness-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2025-08-07
fetch_date: 2025-10-07T00:48:20.967084
---

# EyeWitness Cheatsheet

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

6
Aug
2025

[Chris Traynor](https://www.blackhillsinfosec.com/category/author/chris-traynor/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Cheatsheet](https://www.blackhillsinfosec.com/tag/cheatsheet/), [EyeWitness](https://www.blackhillsinfosec.com/tag/eyewitness/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/)

# [EyeWitness Cheatsheet](https://www.blackhillsinfosec.com/eyewitness-cheatsheet/)

By Chris Traynor || [https://ridgebackinfosec.com](https://ridgebackinfosec.com/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/BLOG_cheatsheet_8.png)

**This blog is part of **Offensive Tooling Cheatsheets: An Infosec Survival Guide Resource**. You can learn more and find all of the cheatsheets HERE:** **<https://www.blackhillsinfosec.com/offensive-tooling-cheatsheets/>**

**EyeWitness Cheatsheet**: [PRINT-FRIENDLY PDF](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/CheetSheet_EyeWitness-.pdf)

Find the tool here: <https://github.com/RedSiege/EyeWitness>

---

## **The Basics**

**Offensive Purpose:**

* Efficient way to gather info about web services & their hosting infrastructure

* Automates taking screenshots for quick & easy review

**Limitations:**

* Only works on HTTP services

* Can only capture a screenshot of the landing/login page; will NOT do spidering

**Key Features:**

* Output in multiple formats (i.e. – HTML & text)

* IDs web server software on target systems

* Can use Nmap & Nessus output files

* Ability to resume from the last scan point if it gets interrupted

## **Installation Methods**

**Git & GitHub**

This will ALWAYS have the latest and greatest features but requires a few additional setup steps. You might also run into Python dependency issues that need to be worked around depending on your OS.

```
git clone https://github.com/RedSiege/EyeWitness
cd EyeWitness/Python/setup
sudo ./setup.sh
cd ..

python EyeWitness.py [options]
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/EyeWitness_01.png)

**Git Installation**

## **Advanced Package Tool (APT)**

APT can lag in new feature/fix releases compared to the direct repository method.

```
sudo apt install eyewitness -y

eyewitness [options]
```

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/Eyewitness_02.png)

**APT Installation**

## **Basic Execution**

**Input Options:**

|  |  |
| --- | --- |
| `-f Filename` | Line-separated file containing URLs to capture |
| `-x Filename.xml` | Nmap XML or .Nessus file |
| `--single Single URL` | Single URL/Host to capture |
| `--no-dns` | Skip DNS resolution when connecting to websites |

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/Eyewitness_03.png)

****Nmap XML File Used as Input****

### Tips

* Always set a custom `--user-agent` value to blend in with traffic.

* The `--resume` option is useful if your execution gets interrupted.

* EyeWitness accepts Nmap & Nessus XML output files, and it’ll automatically parse them for targets.

* Always see if the report contains any possible “default credentials” alongside the screenshots.

* The report can sometimes reference white papers for potentially vulnerable targets.

## **Key Customization Options**

|  |  |
| --- | --- |
| `--user-agent User Agent` | User Agent to use for all requests |
| `--proxy-ip 127.0.0.1` | IP of web proxy to go through |
| `--proxy-port 8080` | Port of web proxy to go through |
| `--proxy-type socks5` | Proxy type (socks5/http) |
| `--resolve` | Resolve IP/Hostname for targets |
| `--prepend-https` | Prepend http:// and https:// to URLs without either |
| `--cookies key1=value1,key2=value2` | Additional cookies to add to the request |
| `--resume ew.db` | Path to db file if you want to resume |
| `--max-retries N` | Max retries on timeouts |
| `-d Directory Name` | Directory name for report output |
| `--threads # of Threads` | Number of threads to use while using file-based input |
| `--results Hosts Per Page` | Number of hosts per page of report |

### **Further Learning**

* [https://ridgebackinfosec.com/recordings/](https://ridgebackinfosec.com/recordings/%20)
* <https://www.blackhillsinfosec.com/six-tips-for-managing-penetration-test-data/>

---

---

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/ISSG_YELLOW-668x1024.png)

**Explore the Infosec Survival Guide and more… for FREE!**

Get instant access to all issues of the *Infosec S...