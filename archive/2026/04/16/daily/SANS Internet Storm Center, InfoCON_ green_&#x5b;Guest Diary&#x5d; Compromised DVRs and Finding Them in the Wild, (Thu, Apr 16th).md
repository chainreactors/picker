---
title: &#x5b;Guest Diary&#x5d; Compromised DVRs and Finding Them in the Wild, (Thu, Apr 16th)
url: https://isc.sans.edu/diary/rss/32886
source: SANS Internet Storm Center, InfoCON: green
date: 2026-04-16
fetch_date: 2026-04-17T04:51:10.217034
---

# &#x5b;Guest Diary&#x5d; Compromised DVRs and Finding Them in the Wild, (Thu, Apr 16th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Brad Duncan](/handler_list.html#brad-duncan "Brad Duncan")

Threat Level: [green](/infocon.html)

* [previous](/diary/32884)
* [next](/diary/32892)

Click HERE to learn more about classes Jesse is teaching for SANS

# [[Guest Diary] Compromised DVRs and Finding Them in the Wild](/forums/diary/Guest%2BDiary%2BCompromised%2BDVRs%2Band%2BFinding%2BThem%2Bin%2Bthe%2BWild/32886/)

**Published**: 2026-04-16. **Last Updated**: 2026-04-16 19:20:29 UTC
**by** [Alec Jaffe, SANS.edu BACS Student](/handler_list.html#alec-jaffe,-sans.edu-bacs-student) (Version: 1)

[0 comment(s)](/diary/Guest%2BDiary%2BCompromised%2BDVRs%2Band%2BFinding%2BThem%2Bin%2Bthe%2BWild/32886/#comments)

[This is a Guest Diary by Alec Jaffe, an ISC intern as part of the SANS.edu Bachelor's Degree in Applied Cybersecurity (BACS) program [1].

Security cameras are great at monitoring physical doors, but terrible at locking their own digital ones. Across the internet, thousands of unpatched DVRs sit publicly exposed, many guarded only by the default vendor passwords they shipped with. For threat actors, these are low-hanging fruit. This write-up details a recent two-second Telnet capture, providing a mechanical breakdown of how quickly an exposed camera system goes from online to fully compromised by bad actors.

An attack from IP address [46.6.14.135](/ipinfo.html?ip=46.6.14.135) was detected for 1.934 seconds, successfully connecting and authenticating to TCP [port 23](/port/23) (Telnet) for the aforementioned time period. This initial access vector (utilizing username root and password root) maps to MITRE ATT&CK techniques T1110.001 (Password Guessing) [2] and T1078 (Valid Accounts) [3]. The execution of ten sequential commands within a ~2-second session is inconsistent with manual interaction, meaning the attack is most likely automated.

**![](https://isc.sans.edu/diaryimages/images/2006-04-16_figure1_v2.PNG)
Figure 1: Summary of attack from output of cowrieprocessor [4].**

Further investigation of the IP address using Shodan [5] reveals that the offending device is an Airspace Digital Video Recorder, (DVR) exposing an 8-channel CCTV system in Spain. Note that the OEM of Airspace is Dahua, a Chinese manufacturer of surveillance cameras and related equipment.

**![](https://isc.sans.edu/diaryimages/images/2006-04-16_figure2_v2.PNG)
Figure 2: General information & exposed services of offending device, retrieved from Shodan [5], as of 2026-04-01.**

![](https://isc.sans.edu/diaryimages/images/2006-04-16_figure3_v2.PNG)
**Figure 3: More exposed services of the offending DVR device, retrieved from Shodan [5], as of 2026-04-01.**

Note that the cameras are exposed through the web service. It’s highly likely that an unsophisticated threat actor could gain direct access to the camera video feeds relatively easily through this by leveraging common Dahua default credentials (e.g. **`admin/admin`** or **`666666/666666`**), which are explicitly documented in the vendor's own user manuals for legacy systems [6][7]. Additionally, note that the device’s firmware hasn’t been updated since at latest August of 2014, indicated by the **`Last-Modified`** value.

**![](https://isc.sans.edu/diaryimages/images/2006-04-16_figure4_v2.PNG)
Figure 4: AbuseIPDB results [8], as of 2026-04-01.**

**![](https://isc.sans.edu/diaryimages/images/2006-04-16_figure5_v2.PNG)
Figure 5: First attack reported on AbuseIPDB [8], indicating the device has been compromised since 2025-11-28.**

Noticing similar attacks in my honeypot logs, I prototyped a PowerShell script (assisted by Gemini Pro) to estimate the global footprint of these compromised DVRs. For reference, the script is available on my Github [9]. It pulls IPs from Shodan matching the offending device's RTSP server hash [10], then cross-references them against AbuseIPDB to check for malicious activity reported within the last 90 days, utilizing the APIs of both services.

**![](https://isc.sans.edu/diaryimages/images/2006-04-16_figure6_v2.PNG)
Figure 6: sample of PowerShell script [9] output.**

Due to AbuseIPDB’s free-tier API limits, I could only scan the first 1,000 of the 5,313 matching IPs identified on Shodan. Within that limited sample, 38 IPs (3.8%) were actively reported for abuse.

Extrapolating this 3.8% infection rate across all 5,313 exposed devices yields roughly 202 compromised DVRs globally. Because this script only flags devices caught and reported in the last 90 days, this 202 figure should be treated as a highly conservative baseline. The actual number of compromised devices, including dormant ones, is likely much higher.

Once authenticated, the attacker executed a reconnaissance and environmental staging script. Below is a line-by-line breakdown of the payload execution:

```

# enable
# system
# shell
# sh
```

The script sequentially attempts to escape restricted, vendor-specific CLI menus to access a standard Unix shell, mapping to MITRE ATT&CK technique T1059.004 (Unix Shell) [11].

```

# cat /proc/mounts; /bin/busybox RRVHZ
```

The script reads **`/proc/mounts`** to identify writable file systems, mapping to MITRE ATT&CK technique T1082 (System Information Discovery) [12]. Execution capabilities are subsequently verified by calling a non-existent BusyBox applet (**`RRVHZ`**) and monitoring for the resulting error.

```

# cd /dev/shm; cat .s || cp /bin/echo .s; /bin/busybox RRVHZ
```

The script navigates to /dev/shm (a memory-backed filesystem used to evade disk forensics) and copies **`/bin/echo`** to a hidden file (**`.s`**). This dotfile creation maps to MITRE ATT&CK technique T1564.001 (Hidden Files and Directories) [13]. The file is immediately executed to confirm the directory lacks execution restriction, acting as an environmental staging check that maps to MITRE ATT&CK technique T1082 (System Information Discovery) [12].

```

# tftp; wget; /bin/busybox RRVHZ
```

The script checks for the presence of network utilities (tftp and wget) to determine the available mechanisms for downloading the primary malware payload, corresponding to MITRE ATT&CK technique T1105 (Ingress Tool Transfer) [14].

```

# dd bs=52 count=1 if=.s || cat .s || while read i; do echo $i; done < .s
```

The script tests three redundant file-reading mechanisms against the hidden .s test file, mapping to MITRE ATT&CK technique T1564.001 (Hidden Files and Directories) [13]. Specifically, **`dd bs=52 count=1`** attempts to read the first 52 bytes, which corresponds to the standard size of a 32-bit ELF file header. This acts as an environmental staging check, corresponding to MITRE ATT&CK technique T1082 (System Information Discovery) [12], verifying the system's ability to read and process dropped malware binaries.

```

# /bin/busybox RRVHZ # rm .s; exit
```

Mapping to MITRE T1070.004 (File Deletion) [15], the script removes the temporary .s file to avoid leaving forensic artifacts before terminating the staging session.

To protect against this specific attack vector, defenders should implement the following baseline configurations:

* Restrict Telnet access via a local firewall or VPN to a strictly allowed IP list, preventing exposure to the public internet
* Enforce strong password policies and change default credentials for all service accounts
* Disallow remote root login over Telnet

The set-and-forget lifecycle of physical security devices is actively fueling digital insecurity. When a DVR is left exposed and unmanaged, it ceases to be just a camera system and morphs into a free server for malicious actors. The ~2-second compromise documented here is a stark reminder: if you aren't managing your edge devices, someone else already is.

**Methodology & Tooling Note:** The initial triage and data collection for this report were conducted using cowrieprocessor, Shodan, and AbuseIPDB. Gemini Pro [16] was utilized as a supplemental tool to assist with the mechan...