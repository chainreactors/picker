---
title: The SOC Toolbox: Analyzing AutoHotKey compiled executables
url: https://blog.nviso.eu/2023/07/20/the-soc-toolbox-analyzing-autohotkey-compiled-executables/
source: NVISO Labs
date: 2023-07-21
fetch_date: 2025-10-04T11:53:37.113562
---

# The SOC Toolbox: Analyzing AutoHotKey compiled executables

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# The SOC Toolbox: Analyzing AutoHotKey compiled executables

[Nicholas Dhaeyer](https://blog.nviso.eu/author/nicholas-dhaeyer/ "Posts by Nicholas Dhaeyer")

[Windows](https://blog.nviso.eu/category/windows/), [Blue Team](https://blog.nviso.eu/category/blue-team/), [Forensics](https://blog.nviso.eu/category/forensics/)

July 20, 2023July 18, 2023
2 Minutes

One day, a long time ago, whilst handling my daily tasks, an alert was generated for an unknown executable that was flagged as malicious by Microsoft cloud app security.

When I downloaded the file through Microsoft security center, I immediately noticed that it might be an AutoHotKey script. Namely, by looking at the Icon, which is the AutoHotKey logo.

As with many unknown executables I like to inspect the executable in PE studio and look at the strings. URL patterns are a quick way to see if an executable could be exfiltrating if there was no obfuscation used.

In the strings section of PE studio there were multiple mentions of AutoHotKey, which confirmed my previous suspicions that this was indeed a AutoHotKey executable. A colleague of mine mentioned [this YARA rule](https://github.com/avast/retdec/blob/master/support/yara_patterns/tools/pe/x64/compilers.yara#L139) to detect AutoHotKey executables which could be used to identify this file.

![](https://blog.nviso.eu/wp-content/uploads/2023/02/image-12-1024x477.png)

AutoHotKey executable in PE studio

After a quick internet search I found the program Exe2Ahk ([www.autohotkey.com/download/Exe2Ahk.exe](http://www.autohotkey.com/download/Exe2Ahk.exe)) which promises to convert executables to AHK (AutoHotKey) scripts. However, this program did not work for me and I had to find another way to extract the AutoHotKey script.

![](https://blog.nviso.eu/wp-content/uploads/2023/02/image-13.png)

Unsuccessful extraction using Exe2Ahk

Thanks to a form post on the [Autohotkey forums](https://www.autohotkey.com/boards/viewtopic.php?t=65566). I found out that the uncompiled script is present in the `RCDATA` section of the executable. When inspecting the executable with 7zip, we notice that we can extract the script that is stored in the `.rsrc\RCDATA` folder. The AutoHotKey script is named: `>AUTOHOTKEY SCRIPT<`. The file can be extracted by simply dragging and dropping the file from the 7zip folder to any other folder on your pc.

![](https://blog.nviso.eu/wp-content/uploads/2023/02/image-14.png)

RCDATA folder in 7Zip

Another website (where I unfortunately lost the URL to) mentioned that the same can be achieved via inspecting the file with Resource Hacker. Resource Hacker parses the PE file sections and can extract embedded files from those sections.

![](https://blog.nviso.eu/wp-content/uploads/2023/02/image-15.png)

RCDATA folder in Resource Hacker

Once the file is extracted via your preferred method, you can open it in any text editor and start your analysis of the file, if you run in to any unknown methods or parameters used in the script or have difficulty with the syntax, the [AutoHotKeys documentation](https://www.autohotkey.com/docs/v2/) can probably help you out.

In this case the file was not malicious, which is why we won’t go in more detail, but we have seen cases in the past where threat actors abused this tool to create malware.

![](https://blog.nviso.eu/wp-content/uploads/2023/02/Dhaeyer-Nicholas-headshot-150x150.jpg?crop=1)

**Nicholas Dhaeyer**

Nicholas Dhaeyer is a Threat Hunter for NVISO. Nicholas specializes in Threat Hunting, Malware analysis & Industrial Control System (ICS) / Operational Technology (OT) Security. Nicholas has worked in the NIVSO SOC solving security incidents for our MDR clients. You can reach out to Nicholas via [Twitter](https://twitter.com/DhaeyerWolf) or [LinkedIn](https://www.linkedin.com/in/nicholas-dhaeyer5167/)

[Twitter](https://twitter.com/DhaeyerWolf)

[LinkedIn](https://www.linkedin.com/in/nicholas-dhaeyer5167/)

### Share this:

* [Click to share on X (Opens in new window)
  X](https://blog.nviso.eu/2023/07/20/the-soc-toolbox-analyzing-autohotkey-compiled-executables/?share=twitter)
* [Click to share on Reddit (Opens in new window)
  Reddit](https://blog.nviso.eu/2023/07/20/the-soc-toolbox-analyzing-autohotkey-compiled-executables/?share=reddit)
* [Click to share on WhatsApp (Opens in new window)
  WhatsApp](https://blog.nviso.eu/2023/07/20/the-soc-toolbox-analyzing-autohotkey-compiled-executables/?share=jetpack-whatsapp)
* Click to email a link to a friend (Opens in new window)
  Email

### Like this:

Like Loading...

* Tagged
* [Blue Team](https://blog.nviso.eu/tag/blue-team/)
* [YARA](https://blog.nviso.eu/tag/yara/)
* [AutoHotKey](https://blog.nviso.eu/tag/autohotkey/)
* [Analysis](https://blog.nviso.eu/tag/analysis/)
* [malware](https://blog.nviso.eu/tag/malware/)
* [SOC](https://blog.nviso.eu/tag/soc/)

## Published by Nicholas Dhaeyer

Nicholas Dhaeyer is a Threat Hunter for NVISO. Nicholas specializes in Threat Hunting, Malware analysis & Industrial Control System (ICS) / Operational Technology (OT) Security. Nicholas has worked in the NVISO SOC solving security incidents for our MDR clients. You can reach out to Nicholas via [Twitter](https://twitter.com/DhaeyerWolf) or [LinkedIn](https://www.linkedin.com/in/nicholas-dhaeyer5167/) [View all posts by Nicholas Dhaeyer](https://blog.nviso.eu/author/nicholas-dhaeyer/)

**Published**
July 20, 2023July 18, 2023

## Post navigation

[Previous Post Introducing CS2BR pt. II – One tool to port them all](https://blog.nviso.eu/2023/07/17/introducing-cs2br-pt-ii-one-tool-to-port-them-all/)

[Next Post Unlocking the power of Red Teaming: An overview of trainings and certifications](https://blog.nviso.eu/2023/07/31/unlocking-the-power-of-red-teaming-an-overview-of-trainings-and-certifications/)

## 2 thoughts on “The SOC Toolbox: Analyzing AutoHotKey compiled executables”

1. Pingback: [The SOC Toolbox: Analyzing AutoHotKey compiled executables - Ciberdefensa](https://ciberdefensa.cat/archivos/17445)
2. Pingback: [The SOC Toolbox: Analyzing AutoHotKey compiled executables – Yet Another News Aggregator Channel](https://yanac.hu/2023/07/20/the-soc-toolbox-analyzing-autohotkey-compiled-executables/)

### Leave a Reply[Cancel reply](/2023/07/20/the-soc-toolbox-analyzing-autohotkey-compiled-executables/#respond)

![](https://blog.nviso.eu/wp-content/uploads/2023/04/logo-nviso1.png)

[N...