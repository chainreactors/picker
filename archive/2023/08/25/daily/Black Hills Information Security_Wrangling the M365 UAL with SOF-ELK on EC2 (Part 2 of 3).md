---
title: Wrangling the M365 UAL with SOF-ELK on EC2 (Part 2 of 3)
url: https://www.blackhillsinfosec.com/wrangling-the-m365-ual-with-sof-elk-on-ec2-part-2-of-3/
source: Black Hills Information Security
date: 2023-08-25
fetch_date: 2025-10-04T12:01:51.307119
---

# Wrangling the M365 UAL with SOF-ELK on EC2 (Part 2 of 3)

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

24
Aug
2023

[How-To](https://www.blackhillsinfosec.com/category/how-to/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 201](https://www.blackhillsinfosec.com/category/infosec-201/), [Patterson Cake](https://www.blackhillsinfosec.com/category/author/patterson-cake/), [Phishing](https://www.blackhillsinfosec.com/category/red-team/phishing/)
[BEC](https://www.blackhillsinfosec.com/tag/bec/), [Business Email Compromise](https://www.blackhillsinfosec.com/tag/business-email-compromise/), [EC2](https://www.blackhillsinfosec.com/tag/ec2/), [Exchange Online Management](https://www.blackhillsinfosec.com/tag/exchange-online-management/), [M365](https://www.blackhillsinfosec.com/tag/m365/), [Microsoft 365](https://www.blackhillsinfosec.com/tag/microsoft-365/), [SOF-ELK](https://www.blackhillsinfosec.com/tag/sof-elk/), [UAL](https://www.blackhillsinfosec.com/tag/ual/), [Unified Audit Log](https://www.blackhillsinfosec.com/tag/unified-audit-log/)

# [Wrangling the M365 UAL with SOF-ELK on EC2 (Part 2 of 3)](https://www.blackhillsinfosec.com/wrangling-the-m365-ual-with-sof-elk-on-ec2-part-2-of-3/)

[Patterson Cake](https://www.blackhillsinfosec.com/team/patterson-cake/) //

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/08/BLOG_chalkboard_00637-1-1024x576.png)

In **[PART 1](https://www.blackhillsinfosec.com/wrangling-the-m365-ual-with-powershell-and-sof-elk-part-1-of-3/)** of “Wrangling the M365 UAL,” we talked about the value of the Unified Audit Log (UAL), some of the challenges associated with acquisition, parsing, and querying of the UAL data, and strategies for overcoming those challenges using PowerShell and SOF-ELK, focusing on how to properly format our exported data for easy ingestion into SOF-ELK, running as a locally-installed virtual machine. In this post, we’ll look at spinning up SOF-ELK on EC2 to give us greater portability, flexibility, and extensibility for UAL wrangling!

For quick and easy SOF-ELK deployment, it’s hard to beat downloading the pre-packaged [virtual machine](https://for572.com/sof-elk-vm) and running it locally via VMWare. But for those times when you need a little extra computing capacity or to collaborate with others on an investigation or to take advantage of ease of access to data or systems that are already cloud-based, deploying SOF-ELK on EC2 is worth the additional effort.

We’ll start the process just like we did with our local VM deployment by downloading and unzipping the VM. The next step is to create an OVA from the extracted VM. If you have VMWare Workstation or Fusion, you can launch VMWare, import the VM, select it, then go to “File” and “Export to OVF:”

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/08/Picture8-1.png)

**VMWare Workstation – Export to OVF**

You’ll then be prompted to specify where you want to save your export and what to name it.

*IMPORTANT*: *Make sure you specify a file extension of “.ova” when entering the file name, e.g. “sof-elk-20230623.ova.”*

Alternatively, you can use the command-line “OVF Tool,” which is included with VMWare Workstation, Fusion, and Player. Just open a terminal and navigate to the “OVFTool” directory under your VMWare installation directory. From there, invoke the ovftool executable, providing the path to your source VMX file and a path for the export, remembering to give the file name an “.ova” extension:

![](https://www.blackhillsinfosec.com/wp-content/uploads/2023/08/Picture9-1-1024x199.png)

**VMWare Workstation “ovftool” – Export to OVA**

Next, we’ll need to prepare for upload of our exported “ova” to S3 and conversion to an Amazon Machine Image (AMI). We’ll create an S3 bucket, a “containers.json” file to describe our import, create an Identity and Access Management (IAM) role and policy for the import, and use the AWS CLI to import our image. Don’t panic… we’ll walk through it step-by-step!

You can accomplish most of the necessary AWS steps in either the web UI or via the CLI but, unless you are using “Migration Hub Orchestrator,” you’ll need the CLI for the “import-image” task. So, let’s start with installation and setup of the CLI, detailed in the Amazon guides below:

[Install or update the latest version of the AWS CLI – AWS Command Line Interface (amazon.com)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

[Set up the AWS CLI – AWS Command Line Interface (amazon.com)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html)

Once the AWS CLI is installed and configured, we’ll make an S3 bucket for our upload, paying careful attention to make the bucket region match the region where we want to perform the image import:

```
a...