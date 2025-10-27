---
title: Windows Registry Analysis
url: https://blog.cyber5w.com/Introducing-Windows-Registry.html
source: Instapaper: Unread
date: 2024-07-02
fetch_date: 2025-10-06T17:50:08.813117
---

# Windows Registry Analysis

[![CYBER 5W](/images/logo.png)](/)

## Menu

* [Home](https://www.cyber5w.com/)
* [Blog](/)
* [Academy](https://academy.cyber5w.com/)
* [About](/about/)
* [Contact Us](/contact/)

* [Home](https://www.cyber5w.com/)
* [Blog](/)
* [Academy](https://academy.cyber5w.com/)
* [About](/about/)
* [Contact Us](/contact/)

Search

Search for Blog

![Windows Registry Analysis](/images/registry_pic/cover.png)

5 min read
Jun 30, 2024

## Windows Registry Analysis

[![Cyber 5W's Picture](https://avatars.githubusercontent.com/u/80437140?s=328&v=32)](/about/)

[Cyber 5W](/about/)
in

[Disk-Forensics](/tag/Disk-Forensics)

# What Is Registry

The registry is a hierarchical database, The Windows Registry holds configuration information about all the applications on the system, user-specific settings, configuration of various hardware devices used by the system, settings for all the software on the system, etc.

DIVE INTO THE REGISTRY, ONE OF THE FIRST THING WE NEED TO KNOW IS… WHERE IS IT? AND WHERE IS THE KEY COMPONANT? HOW IS IT ORGANIZED? Why is this registry path useful?

Let’s assume you downloaded a video attachment from an email. When you opened that video, you noticed that it also opens up the Notepad application on its own and it has some content written in a foreign language. You closed that video, but every time you restart your system, you notice that the Notepad application opens automatically and the same foreign language content is displayed.

What is happening here is:

when you downloaded the video attachment, you accidentally downloaded some malware onto your computer. The video could have been from a malicious source. That malware has modified the autostart location in the registry to bring up the binary for Notepad whenever the system is rebooted.
and WE DIVE INTO THAT IN THE PRACTISE SECTION!

# Registry Structure

The registry is structured very similarly to the Windows directory/subdirectory structure. You have the five root keys or hives and then subkeys. In some cases, you have sub-subkeys. These subkeys then have descriptions and values that are displayed in the contents pane. the values are simply `0` or `1`, meaning on or off, but also can contain more complex information usually displayed in hexadecimal.

![error](/images/registry_pic/reg_editor.png)

Inside the registry, there are root folders. These root folders are referred to as hives. There are five (5) registry hives.

* **HKEY\_USERS:** contains all the loaded user profiles
* **HKEY\_CURRENT\_USER:** profile of the currently logged-on user
* **HKEY\_CLASSES\_ROOT:** configuration information on the application used to open files
* **HKEY\_CURRENT\_CONFIG:** hardware profile of the system at startup
* **HKEY\_LOCAL\_MACHINE:** configuration information including hardware and software settings

![error](/images/registry_pic/reg_structure.png)

**Keys:**

* Similar to folders(keys) and subfolders(subkeys),
* produces a folder directory hierarchy

**Values:**

* Data stored within a key, contains data in the form of strings, binary data, integers, and lists.
* where the most valuable forensics data is found

Collection of data files called hives.

When viewed in a registry viewer, hive names are used:

*Hkey\_local\_machine(HKLM)* contain hives:

* SAM
* Security
* system
* software

*hkey\_current\_user(Hkcu)* contain hive:

* NTuser.dat

![error](/images/registry_pic/key_value.png)

# Registry file acquisition

Investigating the Windows registry is quite a difficult task because to investigate it properly, the registry needs to be extracted from the computer. Extraction of the registry file is not just a normal copy-and-paste function.

Since registry files store all the configuration information of the computer, it automatically updates every second. To extract Windows registry files from the computer, investigators have to use third-party software such as FTK Imager.

FTK Imager is one of the most widely used tools for this task. Apart from using third-party software, some research has been carried out to demonstrate how to extract registry information from Windows CE memory images and volatile memory (RAM).
The steps to extract registry files from Access Data FTK Imager are as follows:

**Step 1:** Open access data ftk imager and click on the “add evidence item” button then select the “logical drive” radio button

![error](/images/registry_pic/ftk_imager.png)

note:

* Physical Drive: Extract from a hard drive
* Logical Drive: Extract from a partition
* Image File: Extract from an image file
* Contents of a Folder: Logical file-level analysis only: excludes deleted files and unallocated space

**Step 2:** Then select the source drive and after that scan “MFT” by expanding “evidence tree”, go to windows/system32/config/

**Step 3:** Export the registry file by clicking the “export files” button then select the destination folder

![error](/images/registry_pic/export_registry.png)

We are going to open it in the registry explorer to view the content we have exported

![error](/images/registry_pic/registry_exeplorer.png)

# Deleted Registry keys/values

Registry hives have unallocated space similar to filesystems

A deleted hive key is marked as unallocated

recovery of unallocated keys possible

* keys
* values
* timestamps

lack of anti-forensics tools to completely wipe unallocated registry hive data
recovery of deleted keys possible

* displays
    - hive unallocated space
    - deleted keys

![error](/images/registry_pic/unallocated_space.png)

# Interesting Windows Registry Keys

**Windows Version and Owner Info**

* Located at Software\Microsoft\Windows NT\CurrentVersion, you’ll find the Windows version, Service Pack, installation time, and the registered owner’s name straightforwardly.

**Computer Name**

* The hostname is found underSystem\ControlSet001\Control\ComputerName\ComputerName.

**Time Zone Setting**

* The system’s time zone is stored in System\ControlSet001\Control\TimeZoneInformation.
  Access Time Tracking
* By default, the last access time tracking is turned off (NtfsDisableLastAccessUpdate=1). To enable it, use: fsutil behavior set disablelastaccess 0
  Windows Versions and Service Packs
* The Windows version indicates the edition (e.g., Home, Pro) and its release (e.g., Windows 10, Windows 11), while Service Packs are updates that include fixes and, sometimes, new features.

**Enabling Last Access Time**

* Enabling last access time tracking allows you to see when files were last opened, which can be critical for forensic analysis or system monitoring.

**Network Information Details**

* The registry holds extensive data on network configurations, including types of networks (wireless, cable, 3G) and network categories (Public, Private/Home, Domain/Work), which are vital for understanding network security settings and permissions.

**CLIENT-SIDE Caching (CSC)**

* CSC enhances offline file access by caching copies of shared files. Different CSCFlags settings control how and what files are cached, affecting
  performance and user experience, especially in environments with intermittent connectivity.

**AutoStart Programs**

* Programs listed in various Run and RunOnce registry keys are automatically launched at startup, affecting system boot time and potentially being points of interest for identifying malware or unwanted software.

**Shellbags**

* Shellbags not only store preferences for folder views but also provide forensic evidence of folder access even if the folder no longer exists. They are invaluable for investigations, revealing user activity that isn’t obvious through other means.

**USB Information and Forensics**

* The details stored in the registry about USB devices can help trace which devices were connected to a computer, potentially linking a device to sensitive file transfers or unauthorized access incidents.

**Volume Serial Number**

* The Volume Serial Number can be crucial for tracking the specific instance of a file system, useful in...