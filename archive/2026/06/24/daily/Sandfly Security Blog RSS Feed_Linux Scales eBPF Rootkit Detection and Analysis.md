---
title: Linux Scales eBPF Rootkit Detection and Analysis
url: https://sandflysecurity.com/blog/linux-scales-ebpf-rootkit-detection-and-analysis
source: Sandfly Security Blog RSS Feed
date: 2026-06-24
fetch_date: 2026-06-25T06:08:40.542585
---

# Linux Scales eBPF Rootkit Detection and Analysis

[Major Auto Manufacturer Gains Total Linux Visibility. Learn More](/why-sandfly/case-studies/automotive-manufacturer-achieves-complete-linux-security-visibility)

[Partners](/partners)[Support](/support)[Contact Us](/contact-us)

PlatformWhy SandflyResourcesAbout[Blog](/blog)[Get Sandfly](/get-sandfly)

Sandfly Blog

# Linux Scales eBPF Rootkit Detection and Analysis

24 June 2026

Rootkits

The Scales Linux rootkit was recently discovered and used to target Arch User Repository (AUR) supply-chains (dubbed Atomic Arch) affecting more than 1,500 packages. This malware incorporated an integrated eBPF rootkit to hide, a built-in Tor client for command and control (C2) traffic, and had extensive features to steal credentials to enable further attacks.

This write-up will discuss technical details of the malware, how Sandfly detects it already, and command line forensics to verify if a system is affected.

### Malware Features

This malware is large at around 3 MB in size. The binary uses multiple methods to hide, communicate, and steal credentials:

* Deploys an eBPF rootkit to hide malicious process and network activity.
* Deploys a Tor client to enable anonymous C2 traffic to attackers.
* Deploys persistence mechanisms in *systemd* to restart the malware on system boot.
* Deploys multiple methods to find credentials, tokens, and other valuable access data.
* Has additional features such as malicious *sudo* replacement to steal local user passwords.

### Sandfly Detection

Because Sandfly looks for Linux attack tactics like process cloaking, it detects the Scales rootkit evasion out of the box without requiring custom rule updates or prior knowledge of the specific malware signatures. Customers do not need to upgrade as they are already covered.

Below is a complete list of alerts you may receive from a system infected with the Scales rootkit. This list includes standard enabled checks such as process de-cloaking, and also [drift detection alerts](https://sandflysecurity.com/platform/drift-detection) you may receive if you have enabled that feature on a host.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly detecting scales eBPF Linux stealth rootkit.](https://www.datocms-assets.com/56687/1782253959-scales-rootkit-all-alerts.png?auto=format&dpr=2&q=60&w=920 "Sandfly detecting scales eBPF Linux stealth rootkit.")

The main detections customers will see are the following:

*process\_running\_hidden\_stealth* - Two processes running that are being actively cloaked by the rootkit.

*dirs\_hidden\_bin* - Directory containing trojaned *sudo* command to steal user credentials.

Other detections shown will vary depending if a customer is using drift detection features such as new processes being started, ebpf enabled processes, etc. The two alerts above though are extremely high confidence indicators regardless of drift detection or other detection modules being used.

### eBPF Rootkit Hiding and Detection

The rootkit has an embedded eBPF program that is loaded on startup to hide processes, process names, and inodes to conceal network activity.

The rootkit will start two processes. The main process is the rootkit binary and has a random name and copies itself under the */var/lib* directory so it can persist between reboots.

The second process runs under a bogus *dbus-daemon* name and is the Tor client used to anonymize the C2 communications to the attacker.

In the image below we see the two processes de-cloaked by Sandfly and in this run it uses the name *simece*, but again this is random each time it runs so it can't be used for searching across systems.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly de-cloaks two hidden processes from the Scales eBPF rootkit on Linux.](https://www.datocms-assets.com/56687/1782254426-process-hidden-stealth-list.png?auto=format&dpr=2&q=60&w=920 "Sandfly de-cloaks two hidden processes from the Scales eBPF rootkit on Linux.")

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Scales eBPF rootkit hidden process details.](https://www.datocms-assets.com/56687/1782254571-rootkit-process-hidden-stealth.png?auto=format&dpr=2&q=60&w=920 "Scales eBPF rootkit hidden process details.")

The rootkit also renames the command line to various selections. In the example here it picked a name to mimic a kernel thread *kworker/0:3.* We can see the outcome of this name stomping in the process forensics as the command line is padded out. This is belt-and-suspenders hiding presumably in case the eBPF rootkit didn't load. In that case, the malware can still conceal itself under a bogus name.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Scales eBPF rootkit process forensic data.](https://www.datocms-assets.com/56687/1782266380-rootkit-process-forensic-data.png?auto=format&dpr=2&q=60&w=920 "Scales eBPF rootkit process forensic data.")

The rootkit has hidden the above process with PID 764 and the Tor client will also be a PID near the main process. If you are using command line tools like *ps*, the process will not be visible.

`ps -auxw`

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![eBPF rootkit hides a process from command line tools.](https://www.datocms-assets.com/56687/1782254898-ps-no-pid-764.png?auto=format&dpr=2&q=60&w=920 "eBPF rootkit hides a process from command line tools.")

We can go further and look at the */proc* directory to see if the PID is being listed there. With this eBPF rootkit active, the directory entry is actually hidden from this as well. The listing shows a gap where no PID 764 is seen where it should be.

`ls -al /proc`

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![The /proc listing does not show the hidden process from the rootkit.](https://www.datocms-assets.com/56687/1782255454-proc-listing-no-pid-764.png?auto=format&dpr=2&q=60&w=920 "The /proc listing does not show the hidden process from the rootkit.")

### Manually Investigating Scales eBPF Hidden Processes

Since we have had Sandfly already de-cloak the hidden process we can isolate the system and then do some quick checks to confirm something is actually wrong for incident response escalation.

Using our PID recovered by Sandfly, the first thing we can do is a simple *stat* command in /proc to see if the directory really exists. This rootkit hides the directory listing from view with tools like *ls*, but the *stat* command is not affected:

`stat /proc/PID`

When the above command is run, it will come back with directory status information if it exists. This indicates that the process is there, but is simply being hidden by the rootkit.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Using Linux stat command to show a hidden process actually exists.](https://www.datocms-assets.com/56687/1782255266-stat-proc-764-shows-dir-present-though.png?auto=format&dpr=2&q=60&w=920 "Using Linux stat command to show a hidden process actually exists.")

Next we can go into the process directory and look around.

`cd /proc/PID`

A simple *ls* shows the *exe* path to the suspicious binary.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![](https://www.datocms-assets.com/56687/1782255706-cd-proc-764-ls-listing.png?auto=format&dpr=2&q=60&w=920)

The link from the *exe* will point to */var/lib* but the directory and binary name will be random when the malware first goes active. However, this directory is visible and easily accessed to obtain the binary from the full path.

### Grabbing A Process Binary

As of Sandfly 5.8, we can grab the process binary directly from the UI using our response feature. The binary will be stored in the server where security teams can download it for further analysis or sandbox detonation. This can all be done without logging into the remote system, which may be safer during the initial investigation steps.

![](data:image/svg+xml;base64...)![](data:image/jpeg;base64...)![Sandfly response f...