---
title: Cheatsheet: Linux Forensics Analysis
url: https://fareedfauzi.github.io/2024/03/29/Linux-Forensics.html
source: Over Security
date: 2026-11-10
fetch_date: 2026-11-11T08:35:24.365097
---

# Cheatsheet: Linux Forensics Analysis

xml version="1.0" standalone="no"?

[root@fareed:~#](/ "Personal blog for research, education and note purpose.
")

* [Archive](/archive.html)
* [About](/about.html)

# Cheatsheet: Linux Forensics Analysis

* [DFIR](/archive.html?tag=DFIR)

* Mar 29, 2024

Linux Forensic in a nutshell:

1. Validate compromised
   * Interviewing client/user/administrator (what, why, how, when, where, who?)
   * Live response commands / Run triage scripts
2. Collect evidence
   * Live response triage script collection
   * Disk image
   * Memory dump
3. Investigation and analysis
   * Live response analysis
   * Disk analysis
   * Timeline analysis
   * Log analysis
   * Memory analysis
4. Reporting

# Validate compromised

To validate compromise, we often will collect as much information as we can from the client. Then we proceed with the investigation to validate the compromised. I will often run a few commands or execute a triage script to collect live response command results using a single script.

Validation sometimes easy:

* Defaced web pages
* IDS/EDR/AV/SIEM captures
* Ransomware file encrypted

## Interviewing client/user/administrator

Understanding the incident with questions like this:

* What happened?
* What seemed unusual?
* When did you notice it?
* Which host involved
* What’s the purpose of the system
* Who has access to them?
* How are these systems set up?
* What have you done to fix it?

## Live response and triage script

### Linux-CatScale

For more information about what the script collects, please refer to https://labs.withsecure.com/tools/cat-scale-linux-incident-response-collection.

```
git clone https://github.com/WithSecureLabs/LinuxCatScale.git
cd LinuxCatScale
./Cat-Scale.sh
./Extract-Cat-Scale.sh
```

After running the script and extract the collected evidence, we can proceed investigate the triage data in text editor such as VS Code. Figure below shows the result of command `lastlog` collect by Linux-CatScale.

![image](https://github.com/fareedfauzi/fareedfauzi.github.io/assets/56353946/8669bd9a-9971-4213-b06a-fb40a8f2e89a)

### UAC

Another Live Response collection script to perform live response.

```
user@training:~/uac$ git clone https://github.com/tclahr/uac.git
user@training:~/uac$ sudo ./uac -p full /tmp
[sudo] password for user:
--------------------------------------------------------------------------------
  __   __ _______ _______
 |: | |  |:  _   |:  ____|
 |  |_|  |  | |  |  |____
 |_______|__| |__|_______|

 Unix-like Artifacts Collector 2.8.0
--------------------------------------------------------------------------------
Operating System    : linux
System Architecture : x86_64
Hostname            : training
Mount Point         : /
Running as          : root
Temp Directory      : /tmp/uac-data.tmp
--------------------------------------------------------------------------------
Artifacts collection started...
[001/301] 2024-04-02 01:22:10 +0000 live_response/process/ps.yaml
[002/301] 2024-04-02 01:22:11 +0000 live_response/process/lsof.yaml
[003/301] 2024-04-02 01:22:11 +0000 live_response/process/top.yaml
```

### Fennec

fennec is an artifact collection tool written in Rust to be used during incident response on \*nix based systems. Basically, the tool used osquery to perform the triage collection as we can see in this conf file https://github.com/AbdulRhmanAlfaifi/Fennec/blob/master/deps/linux/fennec.yaml.

```
user@training:~$ wget https://github.com/AbdulRhmanAlfaifi/Fennec/releases/download/v0.4.1/fennec_linux_x86_64
user@training:~$ sudo ./fennec_linux_x86_64 -o training.zip --output-format csv

        ______
        |  ___|
        | |_ ___ _ __  _ __   ___  ___
        |  _/ _ \ '_ \| '_ \ / _ \/ __|
        | ||  __/ | | | | | |  __/ (__
        \_| \___|_| |_|_| |_|\___|\___|
        v0.4.1

2024-04-02 00:56:28 [fennec:418] INFO  Started Fennec 0.4.1
2024-04-02 00:56:28 [fennec:491] INFO  Successfuly wrote '16117820' bytes to osquery file './osqueryd'
2024-04-02 00:56:28 [fennec:347] INFO  Start writing the results for the artifact 'authorized_keys' to 'authorized_keys.csv'
2024-04-02 00:56:28 [fennec:358] INFO  Executing the osquery SQL query 'select * from authorized_keys' for the artifact 'authorized_keys'
```

Please refer https://github.com/AbdulRhmanAlfaifi/Fennec for more information.

### Other tools in the list

1. https://github.com/cado-security/varc
2. https://github.com/Velocidex/velociraptor
3. https://github.com/google/grr

## Live response commands

These commands can be used to review anomalous behavior and verify compromise in real-time action. Some of the commands, such as `cat /var/www/html/webshell.php`, can also be used to perform post-compromise disk analysis, where we only need to supply the full path of the mounted compromised disk, for example, `cat /media/compromised_disk/var/www/html/webshell.php`.

### General information

The first thing we are going to do is collect important information regarding the server that we will analyze.

```
# Display current date and time. Verify the timezone.
date

# Timezone information
cat /etc/timezone

# System information
uname -a

# Network information
ifconfig
cat /etc/network/interfaces

# Display distro version
cat /etc/*-release

# Date of installation of the OS. Check the date
ls -ld /var/log/installer

# Display hostname
hostname
cat /etc/hostname
```

### Logon activities

Then, we proceed to review the logon activities of the compromised host.

```
# Check users who are currently logged in
w

# Last login information for all users. It reads the /var/log/lastlog file
lastlog
cat /var/log/lastlog

# List of last logged in users and their login times
last -f /var/log/wtmp

# Failed login attempts
last -f /var/log/btmp

# Searching for login activities in auth.log with specific keyword
grep -v cron /var/log/auth.log* | grep -v sudo | grep -i user
grep -v cron /var/log/auth.log* | grep -v sudo | grep -i Accepted
grep -v cron /var/log/auth.log* | grep -v sudo | grep -i failed
grep -v cron /var/log/auth.log* | grep -v sudo | grep i "login:session"

# CentOS, Red Hat Enterprise Linux (RHEL) of auth.log
cat /var/log/secure
```

### Review processes

Review all running processes and its command could identify malicious process

```
# Interactive process viewer
htop

# Currently running processes and its command
ps -aux

# List all open files associated with a specific process
lsof -p <PID>

# Directories that contains information about a specific process
ls /proc/<PID>
cat /proc/<PID>

# Show process in tree view
pstree -a
```

| File/Directory in /proc/PID | Description |
| --- | --- |
| cmdline | Command-line arguments passed to the process |
| cwd | Symbolic link to the current working directory of the process |
| exe | Symbolic link to the executable file of the process |
| fd | Directory containing symbolic links to open file descriptors used by the process |
| status | Various status information about the process |
| mem | Represents the process’s memory space |
| cpuinfo | CPU-related information for the process |
| maps | Memory maps of the process |
| limits | Resource limits imposed on the process |
| io | I/O statistics for the process |
| stat | Various statistics about the process |
| sched | Scheduling information for the process |
| syscall | Information about system calls made by the process |
| oom\_score | OOM (Out-Of-Memory) score of the process |

### Recover deleted process’s binary

This method attempts to recover the binary executable from the process’s memory by extracting a portion of the memory associated with the process.

```
cd /proc/1234/

# maps contains memory maps of the process, showing the memory regions used by the process
head -1 maps

# Extract memory content (1000 bytes) at specified ADDRESS to tmp directory
dd if=mem bs=1 skip=ADDRESS count=1000 of=/tmp/recovered_proc_file
```

### Review network

Investigate any malicious connection and unexpected IP address

```
#  List all TCP and UDP connections on ...