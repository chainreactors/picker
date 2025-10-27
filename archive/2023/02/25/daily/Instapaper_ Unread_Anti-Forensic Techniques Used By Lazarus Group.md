---
title: Anti-Forensic Techniques Used By Lazarus Group
url: https://asec.ahnlab.com/en/48223/
source: Instapaper: Unread
date: 2023-02-25
fetch_date: 2025-10-04T08:07:04.298256
---

# Anti-Forensic Techniques Used By Lazarus Group

![](https://image.ahnlab.com/img_upload/assets/images/ko/logo-ahnlab-black.svg)

[![](https://asec.ahnlab.com/wp-content/uploads/2024/05/cropped-cropped-c96015c52f1541dbb6bc195e81ca4859-300x118-1-e1716271120827.webp)](https://asec.ahnlab.com/)

[![](https://asec.ahnlab.com/wp-content/uploads/2024/05/cropped-c96015c52f1541dbb6bc195e81ca4859-300x118-1-e1716271120827.webp)](https://asec.ahnlab.com/)

* [Threat Resources](/)
  + [Malware](https://asec.ahnlab.com/en/category/malware-en/)
  + [Dark Web](https://asec.ahnlab.com/en/category/darkweb-en/)
  + [Vulnerabilities](https://asec.ahnlab.com/en/category/vulnerability-en/)
  + [Phishing/Scam](https://asec.ahnlab.com/en/category/phishing-scam-en/)
  + [CERT](https://asec.ahnlab.com/en/category/cert-en/)
  + [Smishing](https://asec.ahnlab.com/en/category/smishing-en/)
  + [EndPoint](https://asec.ahnlab.com/en/category/endpoint-en/)
  + [Mobile](https://asec.ahnlab.com/en/category/mobile-en/)
  + [Networks](https://asec.ahnlab.com/en/category/networks-en/)
  + [APT](https://asec.ahnlab.com/en/category/apt-en/)
  + [Trend](https://asec.ahnlab.com/en/category/trend-en/)
* [Daily Threats](/en/category/threatviews-en/?latest)
* [Security Advisory](https://asec.ahnlab.com/en/security-advisory-en/)
* [RSS](https://asec.ahnlab.com/en/feed/)
* [Feedly](https://feedly.com/i/subscription/feed/https%3A//asec.ahnlab.com/en/feed/)
* Language
  + [한국어](/ko/)
  + [English](/en/)
  + [日本語](/jp/)

한국어

English

日本語

RSS

Feedly

[APT](https://asec.ahnlab.com/en/category/apt-en/)

# Anti-Forensic Techniques Used By Lazarus Group

* Feb 15 2023

![Anti-Forensic Techniques Used By Lazarus Group](https://asec.ahnlab.com/wp-content/uploads/2023/02/60_north-korea-hacker_01-803x490.png?crop=1)

Since approximately a year ago, the Lazarus group’s malware has been discovered in various Korean companies related to national defense, satellites, software, and media press. The AhnLab ASEC analysis team has been continuously tracking the Lazarus threat group’s activities and other related TTPs.

Among the recent cases, this post aims to share the anti-forensic traces and details found in the systems that were infiltrated by the Lazarus group.

## **Overview**

### **Definition of Anti-Forensics**

Anti-forensics refers to the tampering of evidence in an attempt to mitigate the effectiveness of a forensics investigation at a crime scene. From a breaching point of view, anti-forensics generally have the following objectives.

* Detection evasion and obstruction of information collection
* Increase the analysis time of digital forensic analysts
* Disable or cause the malfunction of digital forensic tools
* Block, bypass or delete logs to hide traces of access or execution of tools

The Lazarus group carried out anti-forensics to conceal their malicious acts.

### **Anti-Forensic Techniques**

While there are various standards on the classification of anti-forensic techniques, this post will use the most widely received anti-forensic classification proposed by Dr. Marcus Roger to distinguish and analyze concealment measures taken by the Lazarus group.

Dr. Marcus Roger classified anti-forensic techniques which hinder forensic analysis into 5 main categories: data hiding, artifact wiping, trail obfuscation, attacks against computer forensics, and physical.

Looking at the 5 categories above, the Lazarus group utilized data hiding, artifact wiping, and trail obfuscation, a total of 3 techniques.

## **Data Hiding**

Data hiding refers to the method of data concealment that renders their detection difficult. Major examples include data obfuscation, encryption, steganography, and hiding data in non-allocated areas.

### **Encryption**

The Lazarus group distinguished and used their malware in 3 parts. The loader, executable file, and configuration file. The major features of each file are as follows.

* Loader: Decrypts encrypted PE files and loads them onto the memory
* Encrypted PE: A malware that runs on the loader memory and decrypts encrypted configuration files to communicate with the C2 address.
* Encrypted Config: An encrypted configuration file that contains C2 information.

The Lazarus group transmits the configuration file that has the C2 information and the PE file that communicates with the C2 in encrypted forms to evade detection by security products. The encrypted files operate after being decrypted onto the memory by the loader file. They then receive additional files from the C2 and perform malicious acts.

![](https://image.ahnlab.com/atip/content/image/20240722/sHb64u6P3su606x7TVyD4Ho4W0vRScF9QaWSf8mK.png)

Figure. Backdoor operation process

![](https://lh5.googleusercontent.com/R3aBuY2aO1N8iMCUWAOwub37YmpduNh8Jcq6YWU2MrzWAEiB7lUMg6V0oy5Isp1vx4faJPL73JsBs5w1q_Z3kZsH7CWFG71p5FnFys0DDHTwh3xpelqENXfspoJsjJoKoQwQAPqMrRNunnQOdLZy3gs)

### **Other Forms of Data Hiding**

The Lazarus group either used a system folder as a hiding place or imitated the name of a normal file to hide their malware. The default system folders are where their malware hiding is mainly done. The malware is hidden by either creating a similar folder within the system or by disguising the malware as a normal file within a system file that’s hidden by default.

* C:\ProgramData\
* C:\ProgramData\Microsoft\
* C:\Windows\System32\

The C:\ProgramData folder is a default system folder which is hidden by default. A folder with a name similar to the default folder (MicrosoftPackages) is created inside this folder as a malware hiding place or the malware is disguised as a similar file inside the default folder.

![](https://image.ahnlab.com/atip/content/image/20240722/Wy4IlGLGBD78X4TLHdUkYVRFh4jPFFPqH0RKmEY3.png)

Figure. Similar folder created to use as a malware hiding place

![](https://lh6.googleusercontent.com/fD8yQAvFWECrpnipvBO70ewsHSyHA1a_4pB0Z5z5LdxfG_jDxXQqr7RFWibufEfe2T7tAlXrnlT7fYJXvthch-gbj1_ErS1a7Q6XSgjNOVwpmg6xwbkMVMLXpEGFv4X80lobHYZBPc8vNv27BVZDtnA)
![](https://image.ahnlab.com/atip/content/image/20240722/jVjz794cm9CKwaZf7vNFlNo7c1328Taw1KcucSNu.png)

Figure. Hiding malware by imitating default folder names

## **Artifact Wiping**

Artifact wiping refers to the task of permanently deleting specific files or the whole file system. Not only does it involve file deletion, but expert tools can also be used to erase all traces of use. For example, the Disk Clean-up utility, file deletion, and disk demagnetization are all included in artifact wiping.

### **File Wiping**

Excluding the backdoor malware, the Lazarus group deleted the malware and the artifacts that occurred while the malicious behavior was being performed. In the malware’s case, its data was overwritten and its filename was changed before being deleted.

The original file content can no longer be seen if the data section is overwritten during file deletion since this makes data recovery through methods such as file restoration and data carving difficult.

![](https://image.ahnlab.com/atip/content/image/20240722/SVEYH26yT0IW8l3D0deWFMOFlo4jyABqNfXBVhZg.png)
![](https://lh5.googleusercontent.com/fXMvWd7FdGyhvKwcfrz-JhaEjLySQPHYneYAdFF3yb2KCmQsEjt4KgwU8PFKxmJnv5o51I5UqlOoMsylHusu0EE6OQPzDPrzZj8sjkp0mC48c_BNcLXsdMQZkNDJb5rtMCCUoFNrkpo3nse6l1WN158)

Figure. Malware deletion log confirmed in USNJrnl

The Lazarus group also deleted artifacts related to their malware execution at the same time. For example, the prefetch files, which are artifacts related to application execution, were collectively deleted to remove traces of the malware being executed.

![](https://image.ahnlab.com/atip/content/image/20240722/MCEGy9QF6WgfVPEfzLSaP5acjGpQaCstDaAfECFw.png)

Figure. Log showing the collective deletion of prefetch files

## **Trail Obfuscation**

Trail obfuscation refers to the task of confusing the forensic process to hide malicious behavior. Modification/Deletion of logs, spoofing, inserting incorrect information, and backbone hopping can be considered examples of ways to interfere with analysis o...