---
title: Getting Started with The DFiR Galaxy Workstation
url: https://medium.com/@mahmoudsoheem/getting-started-with-the-dfir-galaxy-workstation-7f4b56bfbe1e
source: Instapaper: Unread
date: 2025-11-04
fetch_date: 2025-11-05T03:12:39.307418
---

# Getting Started with The DFiR Galaxy Workstation

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7f4b56bfbe1e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40mahmoudsoheem%2Fgetting-started-with-the-dfir-galaxy-workstation-7f4b56bfbe1e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40mahmoudsoheem%2Fgetting-started-with-the-dfir-galaxy-workstation-7f4b56bfbe1e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Getting Started with The DFiR Galaxy Workstation

[![Mahmoud Soheem](https://miro.medium.com/v2/resize:fill:64:64/1*qqFhXVer4tpxzzZSc0bClA@2x.jpeg)](/%40mahmoudsoheem?source=post_page---byline--7f4b56bfbe1e---------------------------------------)

[Mahmoud Soheem](/%40mahmoudsoheem?source=post_page---byline--7f4b56bfbe1e---------------------------------------)

4 min read

·

Oct 13, 2025

--

1

Listen

Share

Download Link: <https://1024terabox.com/s/1qTKJ1PM-NxdnFVSNbSmzHg>

Github Repo for Config files: <https://github.com/msoheem/DFiR-Galaxy-Workstation/tree/main>

> ***Important Note:*** *I have found that Windows Explorer limits submenus in the context menu to around 13 visible items. To make all tools accessible, ForensicsTools\_v2.reg introduces a reorganized structure. I have updated the VM and uploaded the new one. If you have the old version of the context menu that do not show all tools, can download it from github repo.*

## 1. Boot and Login

* Once you have booted the VM use the below credentials to login
* Username: Administrator
* Password: dfir4ever

## 2. Desktop Overview

Press enter or click to view image in full size

![]()

The **DFIR Galaxy desktop** is designed for quick and convenient access to your tools, resources, and cheat sheets:

* **Tools Bar** — Provides immediate access to your primary toolkit, useful investigative websites, and a collection of DFIR regular expressions for rapid analysis.
* **Tools Folder** — Contains shortcuts to additional tools not included in the Tools Bar, along with a **Cheat Sheets** folder. All cheat sheets are also accessible from the Favorites in the Edge browser for easy reference.

This layout ensures that essential tools, references, and connectivity utilities are always readily accessible, improving workflow efficiency for DFIR practitioners.

## 3. Add Evidence

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

The “Cases” tab allows you to create a new evidence name, which performs two key functions:

* It automatically creates a subfolder structure in `C:\\Cases\\Analysis`, with subfolders for each evidence category.
* It sets the `EvidenceName` environment variable, ensuring all tools launched from the context menu redirect their output to this new folder.

> *Note: For your convenience, the “Dissect” plugin is available in the forensics tools context menu to quickly retrieve the evidence name.*
>
> *Right-click on the evidence folder → select* ***Forensics Tools for Folders*** *→ Choose* ***Parse with Dissect*** *→ Run* ***osinfo Plugin***

Press enter or click to view image in full size

![]()

## 4. Start investigation

You can start your investigation by creating a super timeline. A helper script for this is available using **Plaso**.

First, create a filesystem timeline with **MFTECmd**:

1. Navigate to the `$MFT` file.
2. Right-click the file and select **Parse with MFTECmd**.

* This will run MFTECmd against the `$MFT` file, creating CSV and body files. The output will be redirected to `C:\\Cases\\Analysis\\%EvidenceName%\\Filesystem`.

Press enter or click to view image in full size

![]()

Next, create the super timeline:

1. From the **WindowsForensicsTools** tab, select **Plaso Helper**.
2. Enter the required parameters when prompted to create the super timeline.

* Once complete, the Plaso super timeline database will be in `C:\\Cases\\Analysis\\%EvidenceName%\\Filesystem`.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

You can easily add the filesystem body file to the database with a single right-click on the body file. Additionally, you can filter the Plaso database by a specific time range by right-clicking the `.plaso` database.

* Add body file to plaso database
* Run psort against a plaso database
* Run cdqr.exe against a plaso database

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

Then you can copy Plaso directory from using the toolbar

Press enter or click to view image in full size

![]()

## 5. Parse specific artifact

To parse a specific artifact, simply use the context menu. For example, you can right-click a Prefetch file and select the option to parse it.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

## Notes about the VM

**Python and Virtual Environment**

Please note that each Python tool has its own virtual environment to prevent dependency conflicts. To run a tool, you have two options:

1. **Activate the virtual environment** by running:`C:\\ForensicPrograms\\DriveFS-Sleuth-1.2.1>.\\venv\\Scripts\\activate.bat (venv) C:\\ForensicPrograms\\DriveFS-Sleuth-1.2.1>python drivefs_sleuth.py`
2. **Call the Python executable directly** from within the virtual environment:`C:\\ForensicPrograms\\DriveFS-Sleuth-1.2.1>.\\venv\\Scripts\\python.exe drivefs_sleuth.py`

**Plaso is a special case.** Each of its tools is compiled into a standalone `.exe`. To use a Plaso tool, simply run its executable directly from the virtual environment folder:

```
C:\\ForensicPrograms\\plaso-main>.\\venv\\Scripts\\log2timeline.exe --version
```

**DFIR\_Toolbar Cleanup Notice**

The **DFIR\_Toolbar**, an open-source Python tool packaged as an executable via PyInstaller, creates a persistent issue with temporary files.

When the `dfir_tool.exe` runs, it unpacks its contents into a temporary folder (`%AppData%\\Temp\\_MEIxxxxx`). Because the toolbar does not shut down normally, Windows fails to delete this temporary folder upon exit. Every subsequent execution creates a **new, temp folder**, leading to a large accumulation of obsolete data in your `%Temp%` directory.

**Recommendation:** Manually delete the older `_MEIxxxxx` folders from `%AppData%\\Temp` periodically to manage disk space.

> *Note that the VM does not have a Windows license. You will need to add your own license.*

[Dfir](/tag/dfir?source=post_page-----7f4b56bfbe1e---------------------------------------)

[Digital Forensics](/tag/digital-forensics?source=post_page-----7f4b56bfbe1e---------------------------------------)

[Cybersecurity](/tag/cybersecurity?source=post_page-----7f4b56bfbe1e---------------------------------------)

[Incident Response](/tag/incident-response?source=post_page-----7f4b56bfbe1e---------------------------------------)

--

--

1

[![Mahmoud Soheem](https://miro.medium.com/v2/resize:fill:96:96/1*qqFhXVer4tpxzzZSc0bClA@2x.jpeg)](/%40mahmoudsoheem?source=post_page---post_author_info--7f4b56bfbe1e---------------------------------------)

[![Mahmoud Soheem](...