---
title: Memory Mystery Challenge
url: https://memoryforensic.com/memory-mystery/
source: Instapaper: Unread
date: 2024-07-05
fetch_date: 2025-10-06T17:45:17.597475
---

# Memory Mystery Challenge

[Skip to content](#content)

Search for:

* [Home](https://memoryforensic.com)
* [Tutorials](https://memoryforensic.com/category/tutorials/)
* [Challenges](https://memoryforensic.com/category/challenges/)
* [Write-ups](https://memoryforensic.com/category/write-ups/)
* [Samples](https://memoryforensic.com/category/samples/)
* [Tools](https://memoryforensic.com/category/tools/)
* [Reviews](https://memoryforensic.com/category/reviews/)

[![memory forensic logo](data:image/gif;base64...)](https://memoryforensic.com/)

* [Home](https://memoryforensic.com)
* [Tutorials](https://memoryforensic.com/category/tutorials/)
* [Challenges](https://memoryforensic.com/category/challenges/)
* [Write-ups](https://memoryforensic.com/category/write-ups/)
* [Samples](https://memoryforensic.com/category/samples/)
* [Tools](https://memoryforensic.com/category/tools/)
* [Reviews](https://memoryforensic.com/category/reviews/)

Analyze Memory
[Our Services](/services)

[Memory Forensic](https://memoryforensic.com)

Master the Art of Memory Forensics

[Memory Forensic](https://memoryforensic.com)

Master the Art of Memory Forensics

[![memory forensic logo](data:image/gif;base64...)](https://memoryforensic.com/)

* [Home](https://memoryforensic.com)
* [Tutorials](https://memoryforensic.com/category/tutorials/)
* [Challenges](https://memoryforensic.com/category/challenges/)
* [Write-ups](https://memoryforensic.com/category/write-ups/)
* [Samples](https://memoryforensic.com/category/samples/)
* [Tools](https://memoryforensic.com/category/tools/)
* [Reviews](https://memoryforensic.com/category/reviews/)

[Our Services](/services)

[Challenges](https://memoryforensic.com/category/challenges/)[Samples](https://memoryforensic.com/category/samples/)[Write-ups](https://memoryforensic.com/category/write-ups/)

# Memory Mystery Challenge

[Husam Shbib](https://memoryforensic.com/author/hoxed/)[Jun 29, 2024Jul 25, 2024](https://memoryforensic.com/memory-mystery/)

![memory mystery memory forensics challenge](https://memoryforensic.com/wp-content/uploads/2024/06/memory-mystery-challenge.webp)

## Credit

This Challenge is made by [Husam Shbib](https://www.linkedin.com/in/husamshbib/). He made the challenge for [Hacktoria](https://hacktoria.com/) before, but they have revamped their website now.

## Lab Scenario

> Memory Mystery challenge tests the basic skills of memory forensics and password cracking of players. The players need to analyze a memory dump and connect dots together to be able to get the flag. It is not a real-life scenario challenge by any means, but I am sure, you will learn a lot in doing it!

We have received some catastrophic news from our sources about a cyber attack had hit a high-profile organization. Our sources have informed us that the attackers may have overlooked to remove some volatile traces contained in the compromised systems.

Based on our sources, the cyber attack was done by an Advanced Persistent Threat group called APT777. They managed to stay off radar for some time, but we believe that we can trace them back this time.

We have attached a memory dump file of one of the most critical compromised systems that needs to be analyzed using your digital forensics skills to gather more information on this group, and trace them using the evidences that you may find in the memory dump.

## Downloading the Memory Dump / Running on the Cloud Lab

> Attention: the sample you are about to download is including malicious files and malware samples. To protect your system, please analyze it on a completely isolated virtual machine if it is not running on cloud

You can download the memory dump directly from [here](https://drive.google.com/file/d/1xMbyvvuvrc6LBxswa8uwFMQI_18DRSoW/edit).

## Submit Your Answer

**Flag Format**: XXXXXX

What is the flag?

Δ

Show the Hint:

The flag is the word to open the file, not inside the file ^^

## My Walk-through

I do not recommend checking the write-up **unless** you are really stuck.

Write-up Steps:

* Install latest compiled version of Volatility 2.6 for Windows
* Copy the Challenge.vmem inside volatility\_2.6\_win64\_standalone folder
* open cmd.exe inside the volatility\_2.6\_win64\_standalone folder
* run volatility\_2.6\_win64\_standalone.exe on the sample memory image “Challenge.vmem” to determine the memory image profile as follows:

```
volatility_2.6_win64_standalone.exe -f Challenge.vmem imageinfo
```

* Then run pslist plugin on the sample memory image after determining the memory image profile as follows:

```
volatility_2.6_win64_standalone.exe -f Challenge.vmem --profile=Win7SP1x86_23418 pslist
```

* We can notice that there is a notepad.exe process open in the memory sample along with other processes
* As notepad is running, we can do some initial investigations using some plugins such as clipboard plugin as follows:

```
volatility_2.6_win64_standalone.exe -f Challenge.vmem --profile=Win7SP1x86_23418 clipboard
```

* We found a strange value, which is: “JBQWG23UN5ZGSYJAINXW45DSMFRXIICGNFWGKLT2NFYA====”
* We go to CyberChef, and paste the value, then it is recognized as Base32 encoding by Magic plugin.
* We decode the base32 text to get “Hacktoria Contract File.zip”
* We can confirm the same value by searching in the files of memory dump using filescan plugin of volatility and check note.txt file as follows:

```
volatility_2.6_win64_standalone.exe -f Challenge.vmem --profile=Win7SP1x86_23418 filescan > files.txt
```

* We can find note.txt file inside the output file “files.txt” at offset “0x000000003fc77360”, so we can dump the file to the current directory using its offset as follows:

```
volatility_2.6_win64_standalone.exe -f Challenge.vmem --profile=Win7SP1x86_23418 dumpfiles -Q 0x000000003fc77360 -D .
```

* We can open the dumped file using notepad and we will get the same encoded value “JBQWG23UN5ZGSYJAINXW45DSMFRXIICGNFWGKLT2NFYA====”
* After we decoded the value and get Hacktoria Contract File.zip, this seems to be a filename for one of the zipped files, right? So we need to search for this file by also using filescan plugin, but we do not need to do it again as we redirected the output of the plugin’s results to files.txt previously.
* After searching in files.txt file, we found that there is a file with the same name “Hacktoria Contract File.zip” at offset “0x000000003da0fac0”, so we need to dump it to the current directory as follows:

```
volatility_2.6_win64_standalone.exe -f Challenge.vmem --profile=Win7SP1x86_23418 dumpfiles -Q 0x000000003da0fac0 -D .
```

* After dumping the zipped file, we opened it and we found a text file called “flag.txt”, which it protected with a password.
* If we think where passwords are stored in Windows, we can recall that passwords hashes are stored in SAM hive in registry, so we need to dump registry files to the current directory, as it may contain valuable information for us as follows:

```
volatility_2.6_win64_standalone.exe -f "Challenge.vmem" --profile=Win7SP1x86_23418 dumpregistry -D .
```

* Then, we need to analyze the SAM Hive using a Registry Explorer and unzip it.
* Run RegistryExplorer.exe and open the SAM hive “registry.0x969519c8.SAM”, which you dumped previously. You can press on File (in the menu) -> load hive -> then locate the SAM hive.
* Then you can view CMI-CreateHive{899121E8-11D8-44B6-ACEB-301713D5ED8C}\SAM\Domains\Account\Users\000003E8, and you will find a password hint as follows: End it with 5.
* Rockyou.txt is one of the most famously used wordlists, and we got in the password hint “end it with 5”, so we need to try using the rockyou.txt wordlists and append “5” to all passwords in the wordlist.
* Download the [rockyou.txt wordlist](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)
* Install Python3 for Windows.
* write a small Python3 script to append “5” to the all words in rockyou.txt wordlist as follows:

```
import sys

# Read from standard input
input_lines = sys.stdin.readlines()

# Append "5...