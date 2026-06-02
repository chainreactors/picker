---
title: ShellBag Forensics Tracking User Folder Interactions
url: https://digitalinvestigator.blogspot.com/2026/05/shellbag-forensics-tracking-user-folder.html
source: Instapaper: Unread
date: 2026-06-01
fetch_date: 2026-06-02T06:33:18.917425
---

# ShellBag Forensics Tracking User Folder Interactions

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# ShellBag Forensics: Tracking User Folder Interactions

Joseph Moronwi
May 29, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiD0qEImPx5oj8BYyvXaPnKNBNmtEMrLu32ukSLz6ey09AA4399cVpipldiVm5B07VniNJDGlT3LKhPY7Xmw1a4dzjZbkyQlNDTy8t2DJYLzu1JZAipxY1XYN2UnCyFcK1MW3IKkSyhV0ybqjmg02ssbpoCLtAzlfZtOF6Sh_MeHE8IFqZIK2rFca6igXM/w655-h281/Figure%205.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiD0qEImPx5oj8BYyvXaPnKNBNmtEMrLu32ukSLz6ey09AA4399cVpipldiVm5B07VniNJDGlT3LKhPY7Xmw1a4dzjZbkyQlNDTy8t2DJYLzu1JZAipxY1XYN2UnCyFcK1MW3IKkSyhV0ybqjmg02ssbpoCLtAzlfZtOF6Sh_MeHE8IFqZIK2rFca6igXM/s1331/Figure%205.png)

ShellBags are among the most intricate and analytically demanding registry artifacts encountered in Windows digital forensic examinations. Nevertheless, their evidentiary yield justifies the analytical investment, furnishing robust corroboration of the existence of files and folders, user awareness, and interaction provenance. These artifacts are particularly instrumental in resolving complex questions of data enumeration, assessing the scope of exfiltration or destruction in intrusion investigations, reconstructing the contents of defunct removable media, and documenting access to previously mounted encrypted volumes or synchronized cloud storage directories. Critically, ShellBags frequently preserve references to deleted folders and volumes, delivering high-value intelligence regarding artifacts no longer resident within the active file system.

Windows maintains ShellBags to record user-specific preferences governing the graphical presentation of folders and shell objects within File Explorer. This encompasses column visibility and ordering, view modes (icons, details, list, tiles, content), sorting criteria, and window geometry. The persistence of these customizations upon subsequent access exemplifies the functionality of ShellBags. Notably, Windows treats numerous non-traditional entities as shell folders, including compressed archives, mobile device file systems, Control Panel applets, and virtual network locations. Beginning with Windows 11 22H2, native Explorer support was significantly expanded to encompass nearly a dozen additional archive formats—such as 7-Zip, RAR, TAR, and Gzip—via integrated libarchive handling. Given threat actors’ increasing reliance on native tools to minimize forensic footprints, this enhancement is anticipated to yield substantial probative evidence in future investigations. Creation or modification of ShellBags entries requires explicit interaction through the Windows GUI, most commonly via File Explorer.

The mere presence of a ShellBags subkey corresponding to a specific folder or shell namespace object attests that the associated user account actively interacted with it. Leveraging the LastWrite timestamps inherent to registry keys, examiners can establish precise temporal boundaries—specifically, the initial interaction time and most recent update—while cross-correlating these with embedded shell item target MAC timestamps. Because substantial portions of this interaction data reside exclusively within the ShellBags structure, the artifact has achieved paramount importance in modern Windows forensic workflows.

# Location of ShellBags Data

The storage location of ShellBags data evolved with the release of Windows Vista. In Windows XP, the primary data resided within the NTUSER.dat hive. From Windows Vista onward, the preponderance of ShellBags information was relocated to the USRCLASS.dat hive, although residual artifacts—particularly those related to desktop items and mapped network shares—persist in NTUSER.dat. Comprehensive analysis, therefore, necessitates examination of both registry hives. The specific keys are listed as follows.

Windows Vista and Later (Including Windows 7, 8, 10, and 11)

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\BagMRU
HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell\Bags
```

(Live analysis)

```
NTUSER.DAT\Software\Microsoft\Windows\Shell\BagMRU
NTUSER.DAT\Software\Microsoft\Windows\Shell\Bags
```

(Disk analysis)

Stores data for folders accessed from the network (UNC path).

```
HKEY_CURRENT_USER\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\BagMRU
HKEY_CURRENT_USER\Software\Classes\Local Settings\Software\Microsoft\Windows\Shell\Bags
```

(Live analysis)

```
UsrClass.DAT\Local Settings\Software\Microsoft\Windows\Shell\BagMRU
UsrClass.DAT\Local Settings\Software\Microsoft\Windows\Shell\Bags
```

(Disk analysis)

Stores data for folders accessed locally and on removable drives.

```
C:\Users\USER\AppData\Local\Packages\APP_PACKAGE_NAME\SystemAppData\Helium\User.dat\ (Disk analysis)
```

Stores data for folders accessed from the network (UNC path) from a specific app.

```
C:\Users\USER\AppData\Local\Packages\APP_PACKAGE_NAME\SystemAppData\Helium\UserClasses.dat\ (Disk analysis)
```

Stores data for folders accessed locally and on removable drives from a specific app.

Windows XP

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\ShellNoRoam
```

(Live analysis)

```
NTUSER.DAT\Software\Microsoft\Windows\ShellNoRoam
```

(Disk analysis)

Stores data for folders accessed locally.

```
HKEY_CURRENT_USER\Software\Microsoft\Windows\Shell
```

(Live analysis)

```
NTUSER.DAT\Software\Microsoft\Windows\Shell
```

(Disk analysis)

Stores data for folders accessed from the network (UNC path).

The core ShellBags artifacts manifest under the following primary keys in USRCLASS.dat:

* **BagMRU**: Constructs a hierarchical representation of accessed shell namespaces through a cascading series of numbered subkeys that mirror the folder structure traversed by the user.
* **Bags**: Contains the associated view and configuration preferences for each corresponding entry in BagMRU.

The colloquial designation “ShellBags” derives directly from these two keys (Shell + Bags). A foundational concept in ShellBags analysis is that all data originates from registry keys, each of which bears a LastWrite timestamp that updates upon modification. These timestamps form the evidentiary basis for determining “First Interacted” and “Last Interacted” temporal markers.

## ShellBags Analysis

Analysis typically commences with the BagMRU key. This structure is distinctive in that it replicates the folder hierarchy using sequentially numbered subkeys (0, 1, 2, …), wherein each subkey represents a child namespace object. Identification of each folder’s identity and properties requires inspection of its parent key, which maintains binary values named according to its children. These values encapsulate the shell item data, including folder names and associated metadata.

MRU (Most Recently Used) lists within the BagMRU key consist of ordered sequences of hexadecimal values that establish the relative recency of user interaction with shell namespace objects. As the name implies, these lists provide a chronological ordering of items interacted with based on the sequence in which they appear.

Each MRU entry is represented by a four-byte (DWORD) value stored in little-end...