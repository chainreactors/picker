---
title: Writeup: Cynet Incident Response Challenge
url: https://fareedfauzi.github.io/2020/05/28/Cynet-Writeup.html
source: Over Security
date: 2026-11-02
fetch_date: 2026-11-03T08:51:32.855201
---

# Writeup: Cynet Incident Response Challenge

xml version="1.0" standalone="no"?

[root@fareed:~#](/ "Personal blog for research, education and note purpose.
")

* [Cheatsheets](/cheatsheets.html)
* [Archive](/archive.html)
* [About](/about.html)

# Writeup: Cynet Incident Response Challenge

* [DFIR](/archive.html?tag=DFIR)
* [Writeup](/archive.html?tag=Writeup)

* May 28, 2020

Hello everyone. Cynet conducted a CTF DFIR-based where particapted user can test their own skills in Digital Forensics and Incident Response.

There are 3 categories splitted by levels. Basic, medium and advanced.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-12-17-08-19.png)

The submition can be only submit one attempt only where if your flag is wrong, you cannot submit the right flag again. So, we need to be careful and take a high consideration before submit the question.

So, let’s start.

| Challenges name | Difficulty |
| --- | --- |
| [Time machine](https://fareedfauzi.github.io/write-up/Cynet/#time-machine) | Easy |
| [Hello DOK](https://fareedfauzi.github.io/write-up/Cynet/#hello-dok) | Easy |
| [Bling-Bling](https://fareedfauzi.github.io/write-up/Cynet/#bling-bling) | Easy |
| [Is that you](https://fareedfauzi.github.io/write-up/Cynet/#is-that-you) | Easy |
| [B4 Catch](https://fareedfauzi.github.io/write-up/Cynet/#b4-catch) | Easy |
| [Titan](https://fareedfauzi.github.io/write-up/Cynet/#titan) | Easy |
| [Sports](https://fareedfauzi.github.io/write-up/Cynet/#sports) | Easy |
| [LNK files](https://fareedfauzi.github.io/write-up/Cynet/#lnk-files) | Easy |
| [Can’t touch this](https://fareedfauzi.github.io/write-up/Cynet/#cant-touch-this) | Medium |
| [Copy Paste](https://fareedfauzi.github.io/write-up/Cynet/#copy-paste) | Medium |
| [WhoaMI](https://fareedfauzi.github.io/write-up/Cynet/#whoami) | Medium |
| [Kiwi](https://fareedfauzi.github.io/write-up/Cynet/#kiwi) | Medium |
| [Seashell](https://fareedfauzi.github.io/write-up/Cynet/#seashell) | Medium |
| [Sneak](https://fareedfauzi.github.io/write-up/Cynet/#sneak) | Medium |
| [Universal](https://fareedfauzi.github.io/write-up/Cynet/#universal) | Medium |
| [Notes](https://fareedfauzi.github.io/write-up/Cynet/#notes) | Medium |
| [Psss](https://fareedfauzi.github.io/write-up/Cynet/#psss) | Medium |
| [Roots](https://fareedfauzi.github.io/write-up/Cynet/#roots) | Medium |
| [2nd Base](https://fareedfauzi.github.io/write-up/Cynet/#2nd-base) | Hard |
| [Meow](https://fareedfauzi.github.io/write-up/Cynet/#meow) | Hard |
| [Insurance](https://fareedfauzi.github.io/write-up/Cynet/#insurance) | Hard |
| [Layers](https://fareedfauzi.github.io/write-up/Cynet/#layers) | Hard |
| [Frog Find](https://fareedfauzi.github.io/write-up/Cynet/#frog-find) | Hard |

# Time machine

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-08-22-29-50.png)

## Solution:

They gave us a `$MFT` file and we need to find the filename and time stamp as organizer tell us in the instruction.

After few minutes spending time about MFT forensic, I found this website good for us to read to solve the challenge, <https://www.1337pwn.com/using-ftk-imager-to-find-file-artifacts-in-master-file-table/> .

The question tell us that the file are reside on the Desktop, so that could be one of our hint to find the file.

We then continue our research on how to parse the MFT without using hex viewer.

I found this tool named [analyzeMFT](https://github.com/dkovar/analyzeMFT). AnalyzeMFT is designed to fully parse the MFT file from an NTFS filesystemand present the results as accurately as possible in multiple formats.

```
$ analyzeMFT.py -f "/mnt/c/Users/pins/Desktop/MFT" -o report.csv
```

So, as soon as it parsed and give us the result in `.csv`, we then fire up file with excel and find any files that reside in Desktop.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-12-17-23-58.png)

Looking into the files one by one, the most suspicious time of a file is `Mod-File.txt`

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-28-10-55-07.png)

| Question | Answer |
| --- | --- |
| File name | Mod-File.txt |
| Original creation time | 19-01-2020 11:51:19 |

## Hello DoK

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-08-22-31-33.png)

## Solution:

They gave us these few files:

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-12-17-36-35.png)

The `amcache.hve` file contain information about application shortcuts, device containers, and more. Some of the useful bits of data that can be found through analysis of the amcache include device serial numbers, descriptions (e.g. FriendlyName-like values), volume names, VID/PID data, and more. When a USB storage device is connected to a system, multiple subkeys in the amcache are created under Root\InventoryDevicePnp.

The others file is registry files.

Because our goal is to find USB uid, then we can find it in `amcache.hve` file or `SYSTEM` registry files file.

A. I will go for SYSTEM registry files to find the USB uid using AccessData Registry Viewer tool.

I refer this blog post [https://df-stream.com/2015/02/leveraging-devicecontainers-key](https://df-stream.com/2015/02/leveraging-devicecontainers-key/) and found out the serial UID for Sandisk cruzer is `4C530000281008116284&0` at `SYSTEM\ControlSet001\Enum\USBSTOR\Disk&Ven_SanDisk&Prod_Cruzer_Blade&Rev_1.00\`

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-12-17-48-28.png)

B. we can also find the UID in `Amcache.hve` using any hex viewer.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-08-22-51-10.png)

C. USB Detective Community Edition.

Fire up USB Detective and we can start analyse the artifacts by choose our evidence files (SYSTEM, SOFTWARE and Amcache) in USB Detective.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-28-10-06-40.png)

USB Detective then will process our artifact on the go.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-28-10-10-36.png)

| Question | Answer |
| --- | --- |
| USB Serial | 4C530000281008116284 |

# Bling bling

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-08-22-53-52.png)

## Solution:

Soon we downloaded the files, they gave us a few files of `AutomaticDestinations-ms`.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-08-23-10-49.png)

Files created under `\Users\<username>\AppData\Roaming\Microsoft\Windows\Recent\AutomaticDestinations-ms` are created automatically when a user interacts with the system performing such acts as opening applications or accessing files.

To analyse this file, we can use JumpList Explorer by Eric Zimmerman.

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-28-11-08-11.png)

After looking to the output of user Daenrys, there is nothing suspicious.

We then try analyse JSnow `AutomaticDestinations-ms` and here the result for App WinRar:

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-28-11-18-37.png)

| Question | Answer |
| --- | --- |
| Suspect first name | John |
| Creation Time stamp | 2020-02-07 00:03:54 |

# Is that you?

![](https://raw.githubusercontent.com/fareedfauzi/fareedfauzi.github.io/master/assets/images/cynet-ir/2020-05-08-23-17-33.png)

## Solution:

We got a memory dump file for this challenge. We then start analyse this file by using a memory forensic tool called ...