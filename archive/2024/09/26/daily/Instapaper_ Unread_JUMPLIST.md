---
title: JUMPLIST
url: https://forensicfossil.com/2024/09/jumplist
source: Instapaper: Unread
date: 2024-09-26
fetch_date: 2025-10-06T18:31:46.480805
---

# JUMPLIST

![](https://forensicfossil.com/themes/blog/images/logo.png)

## [Forensicfossil](https://forensicfossil.com/)

SOC Analyst Blog

[Twitter](https://twitter.com/forensicfossil)[Instagram](https://instagram.com/forensicfossil)[RSS](https://forensicfossil.com/feed/rss)

Toggle navigation

* [Home](https://forensicfossil.com/)

1. [Home](https://forensicfossil.com/)
»2. [Windows Artifacts](https://forensicfossil.com/category/windows-artifacts)
» JUMPLIST

[![JUMPLIST](https://forensicfossil.com/content/images/20240922051959-WhatsApp Image 2024-09-22 at 11.19.28_aad7f90f.jpg)](https://forensicfossil.com/2024/09/jumplist)

# JUMPLIST

21 September 2024 - Posted in
[Windows Artifacts](https://forensicfossil.com/category/windows-artifacts) by
[Pawn](https://forensicfossil.com/author/Pawn)

**Jump Lists** were introduced with the release of Windows 7.
Jump Lists are automatically created by Windows to allow users to ‘jump to’ or access items they frequently or recently accessed. Jump Lists are software application specific in that they record files opened from a specific software application. To access a Jump List, the user would right-click the software application from the task bar (i.e. Microsoft Word) and a list of recent documents associated with the software application would be displayed (SANS Forensics 408 Windows Forensic Analysis Volume 4, Core Windows Forensics Part III 2014, 25). They are similar to the Windows shortcuts (link files) because they are designed to take a user directly to a specific file or directory used frequently or
recently. There are two variations of Jump Lists – **Automatic Destinations and Custom Destinations**.

**PATH : C:\Users\username\AppData\Roaming\Microsoft\Windows\Recent**

![enter image description here](https://forensicfossil.com/content/images/20240921061326-123.png)

**AutomaticDestination:** These Jump List files are created automatically when the users open a file or an application. The files are Microsoft Compound File Binary (CFB) file format, also referred to as OLE (Object Linking and Embedding) files. These files contain streams of individual hexadecimal numbered SHLLINK streams and a DestList stream.
Automatic Destinations contain features which are common across all software applications. Automatic Destinations contain the file extension .automaticDestinations-ms. Automatic Destinations are compound files which contain multiple data streams within the single file. Within Automatic Destinations, each stream contains an embedded LNK entry which can be extracted and parsed. The DestList stream acts as a Most Recent Used (MRU) list for files opened from the software application
**C:\%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations**

**CustomDestination:** These are custom made Jump Lists, created when a user pins a file or an application to the Taskbar or Start Menu. The structure of these files is different from AutomaticDestinations Jump List files; it follows a structure of sequential MS-SHLLINK binary format.
Custom Destinations have application specific features which can vary based on the developer’s decision to implement the features. Custom Destinations have the file extension .customDestinations-ms. Custom Destinations can also contain a series of LNK entries for files opened using the software application (13Cubed 2017).

**C:\%UserProfile%\AppData\Roaming\Microsoft\Windows\Recent\CustomDestinations**

**JumpList could contain**

* Tasks
* Links to recent files
* frequently used files
* Links to pinned files

**Digital Forensics Value of Jumplist Artifacts**

The records maintained by Jump Lists are considered an important source of evidentiary information during investigations. The analysis of Jump List files can provide valuable information about users’ historic activity on the system such as file creation, access and modification. Examiners can utilize data extracted from Jump List files to construct a timeline of user activities. What makes this artifact more valuable is the fact that the information is maintained on the system long after the source file and application have ceased to exist on the system.

Additinal Information: Each application has a unique APP ID that will be included in the automatic.destination-ms file or Custom.Destination-ms file .
Here is my Automatic.Destination directory the one highlighted **fb3b0dbfee58fac8.automaticDestinations-ms** is a Microsoft Office Word APP ID
![enter image description here](https://forensicfossil.com/content/images/20240922032328-micro.png)

If you visit this website [App-ID](https://forensics.wiki/list_of_jump_list_ids/) you will find APP ID and the apps names
![enter image description here](https://forensicfossil.com/content/images/20240922032104-AppI.png)

I will be using Eric-Zimmerman Tools call JLECmd to parse the fb3b0dbfee58fac8.automaticDestination-ms file and i will be using a GUI software call JumpListExplorer to also parse this same artifacts.

**JLECmd.exe -f C:\Users\Pawn\Desktop\fb3b0dbfee58fac8.automaticDestinations-ms -q --csv C:\Users\Pawn\Desktop\mac**

The command uses JLECmd.exe to parse the Jump List file (fb3b0dbfee58fac8.automaticDestinations-ms) from the specified path, and outputs the results in CSV format to the folder C:\Users\Pawn\Desktop\mac, while running in quiet mode (-q suppresses extra output).

![enter image description here](https://forensicfossil.com/content/images/20240922034057-csv.png)

I will view the csv file with another Eric-Zimmerman tool call Timelinexplorer ![enter image description here](https://forensicfossil.com/content/images/20240922034355-tie.png)

After viewing the csv file timeline explorer it gave me so many information like

![enter image description here](https://forensicfossil.com/content/images/20240922040102-0.png)
![![enter image description here](https://forensicfossil.com/content/images/20240922040114-01.png)]
I would like to discuss the file path that shows "E:". This indicates that the file originated from an external drive, which is also displayed as a removable drive in the second image at the drive path section. This detail can be crucial for investigators during a criminal investigation, as this information wouldn’t appear in an LNK file as a removable drive.
![enter image description here](https://forensicfossil.com/content/images/20240922040125-012.png)
![enter image description here](https://forensicfossil.com/content/images/20240922040136-013.png)

**GUI TOOL (JUMPLIST EXTRACT )**
This software only gave me few information without including MAC address and other information.
![enter image description here](https://forensicfossil.com/content/images/20240922041355-014.png)

**CASE SCENERIO:**

Walmart security identified Craig Tucker as a suspect in a counterfeit coupon scheme after he matched a suspect description and used fraudulent coupons. He was detained, denied knowing the coupons were fake, and consented to a search of his computer, leading to a forensic investigation of his hard drive for evidence related to the fraud. During the investigation, I discovered a illegal content involving minors image in the LNK file and needed to determine its origin, as it wasn't in the recycle bin nor sent by any associates of Craig Tucker. By examining the Jump List folder, I confirmed that the image had been viewed from a removable device, which provided crucial information for the case.
Lnk File only showed when the file was created and not when what drive they were actually on.
![enter image description here](https://forensicfossil.com/content/images/20240922044306-019.png)

**JumpLister**

the jump list shows the underage pictures that were opened on the E: drive.
I did not have this information in the link files because the link files were updated.
You can see in the column Date/Time that the pictures Underage\_lolita\_r@ygold\_001.jpg and
Underage\_lolita\_r@ygold\_002.jpg were opened on the E:\ drive and in the Pictures folder on the
following...