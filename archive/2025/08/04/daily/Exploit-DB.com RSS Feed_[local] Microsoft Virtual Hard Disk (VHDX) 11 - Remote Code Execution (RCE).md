---
title: [local] Microsoft Virtual Hard Disk (VHDX) 11 - Remote Code Execution (RCE)
url: https://www.exploit-db.com/exploits/52394
source: Exploit-DB.com RSS Feed
date: 2025-08-04
fetch_date: 2025-10-07T00:14:56.597993
---

# [local] Microsoft Virtual Hard Disk (VHDX) 11 - Remote Code Execution (RCE)

[![Exploit Database](/images/spider-white.png)](/)
[Exploit Database](/)

* [Exploits](/)
* [GHDB](/google-hacking-database)
* [Papers](/papers)
* [Shellcodes](/shellcodes)

---

* [Search EDB](/search)
* [SearchSploit Manual](/searchsploit)
* [Submissions](/submit)

---

* [Online Training](https://www.offsec.com/?utm_source=edb&utm_medium=web&utm_campaign=www)

[![Exploit Database](/images/edb-logo.png)](/)

* [Stats](/exploit-database-statistics)
* [About Us](/)

  [About Exploit-DB](/about-exploit-db)
  [Exploit-DB History](/history)
  [FAQ](/faq)
* Search

# Microsoft Virtual Hard Disk (VHDX) 11 - Remote Code Execution (RCE)

#### EDB-ID:

###### 52394

#### CVE:

###### [2025-49683](https://nvd.nist.gov/vuln/detail/CVE-2025-49683)

---

**EDB Verified:**

#### Author:

###### [nu11secur1ty](/?author=10359)

#### Type:

###### [local](/?type=local)

---

#### Platform:

###### [Windows](/?platform=windows)

#### Date:

###### 2025-08-03

---

**Vulnerable App:**

```
# Titles: Microsoft Virtual Hard Disk (VHDX) 11 - Remote Code Execution (RCE)
# Author: nu11secur1ty
# Date: 07/23/2025
# Vendor: Microsoft
# Software: https://www.microsoft.com/en-us/windows/windows-11?r=1
# Reference: https://nvd.nist.gov/vuln/detail/CVE-2025-49683
# Base Score: 7.8 HIGHVector:  CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H

## Overview

This PowerShell script (`vdh.ps1`) demonstrates a **soft corruption
vulnerability** in Windows Virtual Hard Disk (VHDX) handling, related to
**CVE-2025-49683**.

The script performs the following:

- Creates a new dynamic VHDX file (virtual disk) of 10MB size.
- Mounts the VHDX as a new drive in the system.
- Initializes, partitions, and formats the virtual disk with NTFS.
- Dismounts the VHDX and applies **soft byte-level corruption** at an 8 KB
offset inside the VHDX file.
- Re-mounts the corrupted VHDX to observe potential filesystem or mounting
errors.
- Lists the contents of the corrupted volume to show the impact.
- Creates an **immediate restart batch script (`your-salaries.bat`)**
inside the mounted volume which forces a system restart when executed.
- Offers cleanup options to dismount and delete the corrupted VHDX file.

---

## Purpose

This PoC is designed for **security researchers and penetration testers**
to:

- Understand how minor VHDX file corruptions can lead to system instability
or vulnerability exploitation.
- Demonstrate how CVE-2025-49683 affects VHDX mounting and usage.
- Help develop detection and mitigation strategies for such virtual disk
corruption attacks.

---

## Usage Instructions

1. **Run the script in an elevated PowerShell session** (Run as
Administrator - The already malicious authorized user):

   ```powershell
   .\vdh.ps1

2. The script will:

 - Create, mount, and format a new VHDX file.

- Corrupt the file at the byte level.

- Re-mount and attempt to read the volume.

- Create a batch file your-salaries.bat inside the mounted drive.

3. To trigger an immediate restart, navigate to the mounted drive (e.g.,
D:\) and run:

```
your-salaries.bat
```

4. At script end, press 0 to clean up (dismount and delete the corrupted
VHDX), or press any other key to exit and keep the file for further
analysis.

### Important Warnings & Considerations

- Run only on test or isolated environments.
This script creates corruption and forcibly restarts the system via the
batch file. Do not run on production or important machines.

- Immediate Restart Batch File
The your-salaries.bat file triggers an immediate system restart without any
warning or confirmation. Be cautious when executing it.

- Corruption is simulated and subtle.
The corruption at 8 KB offset is a soft corruption intended for
demonstration. Real-world attacks could apply more complex modifications.

- Impact may vary by OS version and environment.
Results depend on Windows version and configuration. Some systems may
detect and repair corruption automatically.

- Elevated privileges required.
Script requires administrative rights to create, mount, initialize, and
corrupt VHDX files.

### Technical Details

- Corruption offset: 8192 bytes (8 KB) into the VHDX file.

- Corruption pattern: Byte sequence [0x00, 0xFF, 0x00, 0xFF, 0xDE, 0xAD,
0xBE, 0xEF].

- Disk initialization: MBR partition style with a single NTFS partition.

- Batch restart command: shutdown /r /t 0 /f to force immediate restart.

### Sample Output

```vbnet
[*] Checking for existing VHDX file to avoid conflicts...
WARNING: [!] Could not dismount VHDX, maybe not mounted: The path
"C:\Users\MicrosoftLoosers\Desktop\CVE-2025-49683\corrupted_test.vhdx" is
not the path to a mounted virtual hard disk file.
[*] Removed existing VHDX file.
[*] Creating new VHDX (Virtual Hard Disk) file...
    Size: 10 MB
    Path:
C:\Users\MicrosoftLoosers\Desktop\CVE-2025-49683\corrupted_test.vhdx
[*] Mounting the new VHDX...
[*] Disk initialized and formatted with NTFS.
    This disk emulates a real drive to test mounting and corruption
handling.
[*] Drive mounted as E:
    You can access this drive like a physical hard disk in Windows Explorer.
[*] Dismounting the VHDX before applying corruption...
[*] Simulating corruption by modifying bytes at offset 8 KB...
    This models how subtle corruption can affect VHDX file integrity,
    which may lead to file system errors or crashes when accessed.
[+] Corruption successfully applied.
    Note: This is a soft corruption for testing and demonstration purposes
only.
[*] Re-mounting the corrupted VHDX to observe effects...
[*] Drive letter(s) assigned after corruption: E
[*] Listing contents of the mounted drive to detect file system anomalies...
[*] Attempting to list contents of drive E:\ ...
[*] Created immediate restart batch script: your-salaries.bat
    Running this batch will force an immediate restart.

[*] Script complete.
    This demo showcases how VHDX file corruption at the byte level
    can impact system behavior and why patching CVE-2025-49683 is crucial.

[*] Press '0' to clean up and remove the corrupted VHDX, or any other key
to exit.
[*] Cleaning up...
[*] VHDX dismounted.
[*] Deleted VHDX file.
```

### License & Disclaimer

This script is provided for educational and research purposes only. The
author and distributor disclaim all liability for any damage caused by
misuse.

Use responsibly, and always obtain proper authorization before testing or
exploiting vulnerabilities on any system.

### References

[CVE-2025-49683](
https://msrc.microsoft.com/update-guide/vulnerability/CVE-2025-49683)
(Windows VHDX file corruption vulnerability)

Microsoft Windows Virtual Hard Disk (VHDX) documentation

Windows PowerShell documentation

# Video:
[href](https://www.youtube.com/watch?v=lkEu_AZnzk4)

# Source:
[href](
https://github.com/nu11secur1ty/CVE-mitre/tree/main/2025/CVE-2025-49683)

# Buy me a coffee if you are not ashamed:
[href](https://www.paypal.com/donate/?hosted_button_id=ZPQZT5XMC5RFY)

# Source download
[href](
https://nu11secur1ty.github.io/DownGit/#/home?url=https://github.com/nu11secur1ty/CVE-mitre/tree/main/2025/CVE-2025-49683
)

# Time spent:
05:35:00

--
System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstormsecurity.com/
https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
                          nu11secur1ty <http://nu11secur1ty.com/>

--

System Administrator - Infrastructure Engineer
Penetration Testing Engineer
Exploit developer at https://packetstorm.news/
https://cve.mitre.org/index.html
https://cxsecurity.com/ and https://www.exploit-db.com/
0day Exploit DataBase https://0day.today/
home page: https://www.nu11secur1ty.com/
hiPEnIMR0v7QCo/+SEH9gBclAAYWGnPoBIQ75sCj60E=
                          nu11secur1ty <http://nu11secur1ty.com/>
```

**Tags:**

**Advisory/Source:**
[Link](https://github.com/nu...