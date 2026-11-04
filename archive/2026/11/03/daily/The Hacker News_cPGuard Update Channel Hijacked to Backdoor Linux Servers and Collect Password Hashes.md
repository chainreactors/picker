---
title: cPGuard Update Channel Hijacked to Backdoor Linux Servers and Collect Password Hashes
url: https://thehackernews.com/2026/11/cpguard-update-channel-hijacked-to.html
source: The Hacker News
date: 2026-11-03
fetch_date: 2026-11-04T08:19:20.687653
---

# cPGuard Update Channel Hijacked to Backdoor Linux Servers and Collect Password Hashes

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [cPGuard Update Channel Hijacked to Backdoor Linux Servers and Collect Password Hashes](https://thehackernews.com/2026/11/cpguard-update-channel-hijacked-to.html)

**Swati Khandelwal**Nov 03, 2026Web Security / Cyber Attack

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjtc3HOtWwxZPk7V8yva9o6Oe5lWAPX8KZsWHG27ohycqrb04wAKSDSSdk6ta6y284N9gT6Ab6QKIWwTPss2bBK4PtS3Fm7gSI9QG5kec2AvEgQPjQnc0YlhlUQx0uZKt2ygn576BQ3aburL-IhrMRFVm1vEpTR5ol06R0BtjySvifD05Q_dQGUPvyPLxs/s1700-nu-rw-lo-l85-e365/cpgaurd.png)

An attacker broke into the update system of the cPGuard security tool on November 2 and used it to send a malicious script to customers' Linux servers.

The script installed a backdoor and collected password hashes and other sensitive files from servers that ran it, cPGuard maker OPSSHIELD said in an [advisory](https://opsshield.com/notice/cpguard-update-channel-compromise.html). The attacker has since taken some of that data.

cPGuard 5.88.25 and later versions remove the backdoor and the files the script left. Credentials the script copied may still work after the update, so any server that may have run the script also needs new passwords and keys.

At 02:06 UTC, the attacker, who has not been identified, used compromised credentials to get into cPGuard's update system. The script went out in cPGuard versions 5.88.12 through 5.88.19.

The attack was detected within 12 hours of those versions going out, according to OPSSHIELD. The company has cleared its infrastructure credentials and stopped the script from reaching more servers. It is still investigating how the attacker got the credentials.

OPSSHIELD has not said how many servers installed one of these versions. Servers check for updates at intervals, so some may not have run the script.

Admins can check whether a server installed an affected version by searching its update log:

`grep 'Successfully updated' /opt/cpguard/logs/install_log`

An entry for any version from 5.88.12 through 5.88.19 means the server installed an affected update. The entry alone does not show that the script ran or that data left the server. The server should still be treated as potentially compromised, even if it now runs 5.88.25 or later.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

A server with no matching entries, or with a missing or incomplete log, may still have run the script. Admins who are unsure can contact OPSSHIELD Support.

The script collected these kinds of data, OPSSHIELD found: `/etc/shadow` and `/etc/passwd`, root's MariaDB or MySQL configuration (`my.cnf`), root's shell history, and the SSH authorization and known-hosts files for root. It may not have collected every file from every server, and the company is still working out what left each one.

The `/etc/shadow` file stores one-way password hashes. Weak, common or previously leaked passwords can be recovered from those hashes by testing guesses offline, and even strong ones still need resetting. Secrets that may sit in the database configuration or shell history have no such hashing to protect them.

The script uploaded what it collected to a licensing server run by OPSSHIELD itself, using a compromised account, so the attacker could pick it up later. OPSSHIELD has since secured that account.

The attacker took 32 files from that server, each tied to one customer server, OPSSHIELD estimated late on November 2 UTC. The count covers only files known to have been taken, and it may change. It does not show how many servers may be involved in total.

Beyond the data collection and the backdoor, OPSSHIELD has found no other malicious activity so far, a finding it says is not final.

### What cPGuard Admins Should Do Now

OPSSHIELD asks admins to update every cPGuard server now and confirm the version:

1. Run `cpgcli update --start` on each server.
2. Run `cpgcli --version` and check that it reports 5.88.25 or later. If the update fails or the version is lower, contact OPSSHIELD Support.

Admins should also take these steps for any server where the script ran or may have run:

1. From a trusted recovery environment, reset the passwords for root and every other local Linux account that uses a password.
2. From a trusted device, change any of those passwords that are also used on other systems.
3. Rotate the server's database passwords, S3 access keys, DigitalOcean tokens and any secrets recorded in root's shell history.
4. Replace the SSH private keys stored under `/root/.ssh`, and remove the matching old public keys from every system that trusts them.

OPSSHIELD is not recommending a full reset or operating system rebuild as a routine step, and says that view could change as the investigation continues. Admins who find other signs of compromise, or cannot confirm a server is clean, should ask OPSSHIELD Support for a case-by-case review, which may lead to a rebuild.

Separately, OPSSHIELD is releasing another update, as a precaution, that removes its support-access keys from cPGuard servers where they were added earlier.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

Support access is a cPGuard feature customers use to let OPSSHIELD staff into a server for troubleshooting. Granting it adds an SSH public key belonging to OPSSHIELD to the `authorized_keys` file for root, according to the company's [documentation](https://support.opsshield.com/shared/support).

OPSSHIELD has not said whether the private key that matches its support-access key was exposed in the attack.

### Files the Script Left Behind

OPSSHIELD published these file names. The update removes the backdoor shell and the collection directory, so their absence after updating proves nothing about whether the script ran.

* **File**: `cpguard-v58812-i91511.sh` (the malicious script)
* **File**: `/var/tmp/.cpg91511_sh` (backdoor shell)
* **Directory**: `/var/tmp/.cpg91511` (where the script gathered files)
* **Fi...