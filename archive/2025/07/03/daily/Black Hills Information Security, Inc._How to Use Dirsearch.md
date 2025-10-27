---
title: How to Use Dirsearch
url: https://www.blackhillsinfosec.com/how-to-use-dirsearch/
source: Black Hills Information Security, Inc.
date: 2025-07-03
fetch_date: 2025-10-06T23:54:21.496540
---

# How to Use Dirsearch

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

2
Jul
2025

[Chris Sullo'](https://www.blackhillsinfosec.com/category/author/chris-sullo/), [General InfoSec Tips & Tricks](https://www.blackhillsinfosec.com/category/infosec-101/general-infosec-tips-tricks/), [How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [Recon](https://www.blackhillsinfosec.com/category/red-team/recon/), [Web App](https://www.blackhillsinfosec.com/category/red-team/web-app/)

# [How to Use Dirsearch](https://www.blackhillsinfosec.com/how-to-use-dirsearch/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/Sullo-150x150.png)

| [Sullo](https://www.blackhillsinfosec.com/team/chris-sullo/)

*Chris has been working in security for 30 years, mainly doing penetration testing in both consulting and corporate environments. Chris is the author of the Nikto web scanner, founder of the RVAsec conference, and has been involved in many OSS projects and community efforts.*

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/dirsearch_header.png)

[Dirsearch](https://github.com/maurosoria/dirsearch) is an open-source multi-threaded “web path discovery” tool first released in 2014. The program, written in Python, is similar to other tools such as Dirbuster or [Gobuster](https://github.com/OJ/gobuster), and aims to quickly find hidden content on web sites. Dirsearch is still under active development, unlike Dirbuster (and possibly Gobuster), and is focused on path discovery unlike Gobuster.

It has several features to aid in discovery and can be easily customized to handle web servers which respond in unusual ways or require additional headers.

It operates by reading in a list of files and paths (a “wordlist”), optionally performing transformations on the list, making an HTTP request for each file, and reporting the results based on internal or user-defined rules.

## Why Use Dirsearch?

Hidden (or unlinked, if you prefer) content on web sites can lead to security issues in multiple ways. This content could include administration panels, installation files, full applications, documentation, test programs, source code repositories, and neglected or forgotten content, among other things. Sometimes this leads to simple information disclosure, and other times can lead to full compromise.

No matter the type of test, knowledge of the full attack surface is critical to properly assessing it.

### **Installation**

Dirsearch requires [Python](https://www.python.org/) and can run on any platform which supports Python version 3.9 or higher. It can be installed with `pip`, manually via GitHub, many operating system package managers, or in Docker. This post details the GitHub installation method.

Git installation:

```
git clone https://github.com/maurosoria/dirsearch.git --depth 1
```

For installation on some operating systems, such as Apple OS X, Python’s virtual environment must be used to properly install dependencies. This can be easily accomplished after the [venv program is installed](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

```
python3 -m venv venv_dirsearch
source venv_dirsearch/bin/activate
python3 -m pip install -r requirements.txt
```

Verify the installation is successful by checking the installed version.

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/07/DIRSEARCH_1.png)

**Dirsearch Version Check**

See the project’s README document on GitHub for other installation options.

### **Wordlists**

Dirsearch is only as good as the wordlist used. A wordlist is a simple text file with paths and/or filenames (with or without file extensions). Dirsearch reads this file, transforms each line if requested by the user, and then makes the HTTP request to look for the file.

Dirsearch includes a word list located at `db/dicc.txt` which includes nearly 10,000 files. Other wordlists can be obtained around the internet, for example from the [Seclists](https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content) repository. Some lists are product specific, such as Java Servlet names, and some are generic. Your selection may vary from website to website. A large and generic list, such as [big.txt](https://github.com/danielmiessler/SecLists/raw/refs/heads/master/Discovery/Web-Content/big.txt), is often a good place to start.

The default wordlist uses custom variables such as **`%EXT%`** to denote where the file extension should be placed. Only these variables will be replaced by default—other lines will not have file extensions. To force the use of extensions on every file, use the `-f` or `—force` flag.

Note that if you use a non-default wordlist wit...