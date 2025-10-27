---
title: Indicator Removal on Linux: A T1070 Purple Team Cheatsheet
url: https://www.hackingdream.net/2025/08/indicator-removal-on-linux-t1070-purple-team-cheatsheet.html
source: Hacking Dream
date: 2025-08-26
fetch_date: 2025-10-07T00:48:07.705134
---

# Indicator Removal on Linux: A T1070 Purple Team Cheatsheet

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Indicator Removal on Linux: A T1070 Purple Team Cheatsheet

[August 25, 2025](https://www.hackingdream.net/2025/08/indicator-removal-on-linux-t1070-purple-team-cheatsheet.html "permanent link")

Indicator Removal on Linux: A T1070 Purple Team Cheatsheet

# Indicator Removal on Linux: A T1070 Purple Team Cheatsheet

*Updated on Sep 07, 2025*

### Table of Contents

* [What is T1070 - Indicator Removal?](#t1070-intro)
* [T1070.001 - Clear System Image](#t1070-001)
* [T1070.002 - Clear Linux System Logs](#t1070-002)
* [T1070.003 - Clear Command History](#t1070-003)
* [T1070.004 - File Deletion](#t1070-004)
* [T1070.005 - Network Share Connection Removal](#t1070-005)
* [T1070.006 - Timestomp](#t1070-006)
* [T1070.007 - Clear Network Connection History and Configurations](#t1070-007)
* [T1070.008 - Clear Mailbox Data](#t1070-008)
* [T1070.009 - Clear Persistence](#t1070-009)
* [T1070.010 - Relocate Malware](#t1070-010)

## What is T1070 - Indicator Removal?

**[T1070 (Indicator Removal)](https://attack.mitre.org/techniques/T1070/)** covers adversary techniques for deleting evidence of their presence and actions on a compromised system. The primary goal is to frustrate [digital forensics and incident response (DFIR)](INSERT\_INTERNAL\_URL) investigations, delay detection, and hide the attacker's tracks. This includes clearing logs, deleting tools, altering timestamps, and removing other artifacts they may have created.  This guide focuses specifically on indicator removal on Linux systems.

[![Indicator Removal on Linux: A T1070 Purple Team Cheatsheet](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfhMyFfK3Ka-E1wwoRK7rzw1QientH8jSsUnGH3TNy8t-MWW6FDbW3pa9GfABQ4yp7gLb_rqAnCpdGqsUmz1WMZRPrCLsmq2YX8GDr4k2MzfnyWaXhrI0Xq5PnUkOA9Kp5LWoRQPBWTn_xhMfvs8NPW_xC6OCVuMkI3cLcKXsJqePEegpWtHvvSAVeiL04/w640-h292/Indicator-Removal-on-Linux-A-T1070-Purple-Team-Cheatsheet.jpg "Indicator Removal on Linux: A T1070 Purple Team Cheatsheet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfhMyFfK3Ka-E1wwoRK7rzw1QientH8jSsUnGH3TNy8t-MWW6FDbW3pa9GfABQ4yp7gLb_rqAnCpdGqsUmz1WMZRPrCLsmq2YX8GDr4k2MzfnyWaXhrI0Xq5PnUkOA9Kp5LWoRQPBWTn_xhMfvs8NPW_xC6OCVuMkI3cLcKXsJqePEegpWtHvvSAVeiL04/s1024/Indicator-Removal-on-Linux-A-T1070-Purple-Team-Cheatsheet.jpg)

---

## T1070.001 - Clear System Image

This technique involves the removal of virtual machine (VM) or container images that the adversary may have used or created. By deleting the image, they remove the entire environment they operated in, making analysis difficult.

### Commands

1. **Remove a Docker container:** This command forcefully stops and deletes a container, removing the runtime instance of an image.

   ```
   docker rm -f <container_id>
   ```
2. **Remove a Docker image:** This deletes the underlying image from the local registry, erasing the template the container was built from.

   ```
   docker rmi <image_id>
   ```
3. **Undefine a libvirt/KVM virtual machine:** This removes the XML definition of a VM, effectively "deleting" it from the hypervisor's management.

   ```
   virsh undefine <vm_name>
   ```
4. **Delete a VM's disk image:** After undefining a VM, the attacker deletes the actual virtual disk file, which contains the filesystem and all data.

   ```
   rm /var/lib/libvirt/images/<vm_name>.qcow2
   ```
5. **Prune the Docker system:** This is a broad cleanup command that removes all stopped containers, unused networks, and dangling images.

   ```
   docker system prune -a -f
   ```

### Remediation

* **Restrict Daemon Access:** Limit access to virtualization and container daemons (e.g., `dockerd`, `libvirtd`) using Unix socket permissions and user groups.
* **Audit Logging:** Enable audit logging for all commands sent to container/VM daemons. For Docker, you can forward daemon logs to a SIEM.
* **Registry Security:** Use a secure, private container registry with immutable image tags and vulnerability scanning.
* **Backups:** Maintain regular, off-site backups of critical VM and container image definitions and storage volumes.

---

## T1070.002 - Clear Linux System Logs

This involves deleting or overwriting logs generated by the operating system and applications to hide specific actions like logins, errors, or commands.

### Commands

1. **Overwrite a log file with nothing:** This is a quick way to empty a log file without deleting it, which is sometimes less suspicious.

   ```
   cat /dev/null > /var/log/auth.log
   ```
2. **Truncate a log file:** `truncate` resizes a file to a specified size, with `0` effectively clearing its contents instantly.

   ```
   truncate -s 0 /var/log/syslog
   ```
3. **Securely delete logs:** `shred` overwrites a file multiple times with random data before deleting it, making recovery nearly impossible.

   ```
   shred -n 1 -z -u /var/log/secure
   ```
4. **Clear user login records:** The `wtmp` file tracks all logins and logouts. Overwriting it erases this history.

   ```
   echo "" > /var/log/wtmp
   ```
5. **Clear journalctl logs:** On systems using `systemd-journald`, logs can be cleared by size or time. This command removes all logs except for the last day's worth.

   ```
   journalctl --vacuum-time=1d
   ```

### Remediation

* **Remote Log Forwarding:** The most effective control. **Forward all logs** in real-time to a remote, write-once/immutable central logging server or [SIEM (Security Information and Event Management)](https://www.splunk.com/en_us/data-insider/what-is-a-siem.html).
* **File Integrity Monitoring (FIM):** Use a FIM tool like [Wazuh or AIDE](INSERT\_INTERNAL\_URL) to monitor critical log files for changes, such as a sudden decrease in size.
* **Strict Permissions:** Log files should have permissions that prevent non-privileged users from modifying or deleting them.

---

## T1070.003 - Clear Command History

Adversaries clear shell command history to hide the commands they executed during their session.

### Commands

1. **Clear current session history:** The `history -c` command clears the list of commands from the current, active shell session.

   ```
   history -c
   ```
2. **Overwrite the history file:** This command empties the `.bash_history` file, erasing all previously saved commands.

   ```
   echo "" > ~/.bash_history
   ```
3. **Prevent future history saving:** By linking the history file to `/dev/null`, any new commands are discarded instead of being written to disk.

   ``...