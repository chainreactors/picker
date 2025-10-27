---
title: Process Forensics on a Live Linux System
url: https://digitalinvestigator.blogspot.com/2023/02/process-forensics-on-live-linux-system.html
source: Instapaper: Unread
date: 2023-02-11
fetch_date: 2025-10-04T06:23:59.669258
---

# Process Forensics on a Live Linux System

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Incident Response](https://digitalinvestigator.blogspot.com/search/label/Incident%20Response)

# Process Forensics on a Live Linux System

Joseph Moronwi
February 08, 2023
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWwVbfqXekSdBdv8JcCz09PQk5VxgK4mueUcbODDGOh-YrAB6HoEVh7-X5EmsqKN-fdH4gkp39shqFRfM8DOHYRmTa-E9WxxjV-78eymT9uy5FlLWEA904CJ1NnCnO3tI1EC1a5jac_wkXt1Yc9CBiT5-sbozILcG8AVs4xzE81Fqe6hon2Z18XhcK/w655-h338/linux.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiWwVbfqXekSdBdv8JcCz09PQk5VxgK4mueUcbODDGOh-YrAB6HoEVh7-X5EmsqKN-fdH4gkp39shqFRfM8DOHYRmTa-E9WxxjV-78eymT9uy5FlLWEA904CJ1NnCnO3tI1EC1a5jac_wkXt1Yc9CBiT5-sbozILcG8AVs4xzE81Fqe6hon2Z18XhcK/s620/linux.jpg)

There is plenty of volatile data that can be collected from a suspect system. Collecting this data will help you make a preliminary determination as to whether or not there was an incident.

Linux process environment allows to extract interesting information about used commands and directories, users, system variables, SSH connection, etc. From a forensic point of view, artifacts of interest might include:

* Anti-forensic actions performed by the suspect.
* SSH source IP address.
* Process environment variables

# Linux Process Forensics

To collect a simple list of running processes and assigned process identifiers (PIDs) from a subject system, including process activity times, enter the following command.

```
ps -ef
ps auxwv
```

To gather deeper context regarding the owner of a suspect process, enter the following commands [enter arguments separated with comma individually at a time].

```
ps -eo pid, user, group, args, etime, lstart | grep <SUSPICIOUS_PID>
```

Upon execution, malware spawns additional processes, or child processes. To obtain a structure hierarchical ‘tree’ view of processes, query the suspect system with the ps or pstree utility. The table below provides command options to achieve varying levels of process tree details.

|  |  |  |
| --- | --- | --- |
| **Tool** | **Command** | **Description** |
| ps | ps -ejh | Displays the Process ID (PID), Process Group ID (PGID), Session ID (SID), Controlling Terminal (TTY), time the respective processes have been running (TIME), and associated Command-line parameters (COMMAND). |
|  | ps -axjf | Displays the Parent Process ID (PPID), Process ID (PID), PGID, SID, TTY, Process Group ID associated with the controlling TTY Process Group ID (TPGID), Process State (STAT), User ID (UID), TIME, and Command-line parameters (COMMAND). |
|  | ps -aux | Displays the User ID (UID), PID, CPU usage (%CPU), Memory usage (%MEM), Virtual Set Size (VSS), Resident Set Size (RSS), TTY, Process State (STAT), Process start time/date (START), TIME, and COMMAND. |
| pstree | pstree -a | Displays command-line arguments. |
|  | pstree -al | Displays command-line arguments using long lines (non-truncated). |
|  | pstree -ah | Displays command-line arguments and highlights each current process and its ancestors. |

Another thing the incident responder or forensic investigator might want to do is to list out the Process ID (PID) under /proc/<PID> to see what is going on.

```
ls -al /proc/<SUSPICIOUS_PID>
```

A lot of exploits work out of `/tmp` and `/dev/shm` directories on Linux. These are both writable directories on almost all Linux systems and many malwares and exploits will drop their payloads there to run. A process that is making its home in /tmp or /dev/shm is suspicious.

As long as the process is still running, it is very easy to recover a deleted process binary on Linux:

```
cp /proc/<SUSPICIOUS_PID>/exe /tmp/recovered
```

You can calculate hash of the binary obtained from the above step by entering the following command.

```
sha1sum /bin/nc
sha1sum /tmp/recovered
```

The command line is stored under `/proc/<PID>/ cmdline` and the command name is shown under `/proc/<PID>/comm`. Some malware will cloak this data to masquerade as another process. You may see different names for the program in this case or even names that are trying to hide as something else like apache or sshd.

```
cat /proc/<SUSPICIOUS_PID>/cmdline
cat /proc/<SUSPICIOUS_PID>/comm
```

If you see multiple different names, then it is very likely the program is malicious.

You will also need to investigate the file descriptors the malware has opened. This can often show you hidden files and directories that the malware is using along with open sockets:

```
ls -al /proc/<SUSPICIOUS_PID>/fd
```

You will also want to take a look at the environment our malware inherited when it started. This can often reveal information about who or what started the process.

```
strings /proc/<SUSPICIOUS_PID>/environ
```

- If histsize is 0, it indicates an anti-forensic action
- sshconnection, with ip source and port and destination source and port.
- sshclient, with ip and port source.

To find all processes automatically that have ssh client, enter the following command.

```
find /proc -name environ -maxdepth 2 -type f 2>/dev/null | xargs grep -o "SSH_CLIENT" 2>/dev/null
```

Another area to look into is the Linux process maps. This shows libraries the malware is using and again can show links to malicious files it is using as well.

```
cat /proc/<SUSPICIOUS_PID>/maps
```

The `/proc/<PID>/stack` area can sometimes reveal more details, therefore, it is important to look at it also.

```
cat /proc/<SUSPICIOUS_PID>/stack
```

Finally, look at /proc/<PID>/status for overall process details. This can reveal parent PIDs, memory usage, and additional details.

```
cat /proc/<SUSPICIOUS_PID>/status
```

A great utility for viewing the libraries loaded by a running process is pmap. This does not only identify the modules invoked by a process but reveals the memory offset in which the respective libraries have been loaded.

```
pmap -d <SUSPICIOUS_PID>
```

The commands discussed here can be combined with those listed in an **[earlier post](https://digitalinvestigator.blogspot.com/2022/05/linux-commands-for-incident-response_31.html)** for a more robust forensic investigation of live Linux systems.

Tags
[Incident Response](https://digitalinvestigator.blogspot.com/search/label/Incident%20Response)

* Share

### [Joseph Moronwi](https://www.blogger.com/profile/16921333364875033449)

DFIR and Adversary Hunting, Malware Research, and OSINT.

### Post a Comment

#### Post a Comment

[Previous Post](https://digitalinvestigator.blogspot.com/2023/05/facebook-osint-investigation.html)
[Next Post](https://digitalinvestigator.blogspot.com/2023/01/vehicle-based-osint-investigations.html)

### Digital Investigator Blog List

* ![]()

  [AboutDFIR – The Definitive Compendium Project](https://aboutdfir.com/)

  [InfoSec News Nuggets 10/02/2025](https://aboutdfir.com/infosec-news-nuggets-10-02-2025/)
  -
  UK Government Issues New Order to Access iCloud User Data The report
  reveals that, in early September, the UK Home Office demanded that Apple
  creates a w...

  1 day ago
* ![]()

  [This Week In 4n6](https://thisweekin4n6.com)

  [Week 39 – 2025](https://thisweekin4n6.com/2025/09/28/week-39-2025/)
  -
  Inside the Salesloft-Drift Breach: What It Means for SaaS & Identity
  Secu...