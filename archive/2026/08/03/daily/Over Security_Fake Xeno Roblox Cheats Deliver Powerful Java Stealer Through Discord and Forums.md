---
title: Fake Xeno Roblox Cheats Deliver Powerful Java Stealer Through Discord and Forums
url: https://www.bitdefender.com/en-us/blog/labs/fake-xeno-roblox-discord-executor
source: Over Security
date: 2026-08-03
fetch_date: 2026-08-04T05:01:09.766309
---

# Fake Xeno Roblox Cheats Deliver Powerful Java Stealer Through Discord and Forums

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

15 min read

# Fake Xeno Roblox Cheats Deliver Powerful Java Stealer Through Discord and Forums

[![Janos Gergo SZELES](https://blogapp.bitdefender.com/labs/content/images/size/w100/2020/11/jszeles.png "Janos Gergo SZELES")](/en-us/blog/labs/author/jszeles "Janos Gergo SZELES")[![Silviu STAHIE](https://0.gravatar.com/avatar/c341806f635818bcc6faa8f684e3d9d0?s=64&d=mm&r=g "Silviu STAHIE")](/en-us/blog/labs/author/sstahie "Silviu STAHIE")

[Janos Gergo SZELES](/en-us/blog/labs/author/jszeles "Janos Gergo SZELES")[Silviu STAHIE](/en-us/blog/labs/author/sstahie "Silviu STAHIE")

August 03, 2026

  ![Fake Xeno Roblox Cheats Deliver Powerful Java Stealer Through Discord and Forums](https://blogapp.bitdefender.com/labs/content/images/size/w600/2026/08/ChatGPT-Image-Aug-3--2026--02_23_41-PM-1.jpg "Fake Xeno Roblox Cheats Deliver Powerful Java Stealer Through Discord and Forums")

*A malware campaign disguised as an “undetected” version of the Xeno Roblox script executor is directly affecting players looking to download a legitimate tool.*

Promoted through various gaming forums and Discord communities, the fake cheat launches a multi-stage Java infection chain built to stay hidden in plain sight. Its components imitate real Xeno files, use Windows-style names and hide inside trusted-looking directories, which includes a folder associated with Xbox Game Bar, formerly Microsoft GameDVR.

The final payload goes far beyond conventional credential theft. It can steal browser cookies, Discord, Roblox and Minecraft accounts, cryptocurrency-wallet data and payment information.

Unlike the more generic stealers, this one can also record keystrokes, access the webcam, stream the victim’s desktop, manipulate files, run PowerShell commands and give attackers interactive control of the infected computer.

Newly identified command-and-control infrastructure and expanded functionality suggest the malware, previously documented as Powercat, remains under active development.

The campaign is particularly worrying because Roblox-related cheats can attract children and teenagers, potentially exposing accounts, private conversations, webcam images and financial information stored on shared family computers.

## Key findings

* Attackers distribute the malware as an undetected version of the Xeno Roblox script executor through gaming forums and Discord communities.
* The campaign uses a multi-stage Java infection chain with files, directories and persistence mechanisms that imitate legitimate Windows and gaming components.
* The final payload combines information theft, surveillance, persistence, remote access, file manipulation and command execution.
* Its targets include Discord, Roblox and Minecraft accounts, browser data, cryptocurrency wallets and payment-related tokens.
* Researchers identified new command-and-control infrastructure and additional capabilities, suggesting continued development.
* Security insights show that users have been affected since the beginning of the year, with activity rising sharply in the second half of March.

# Introduction

Gaming communities offer threat actors a fruitful environment for reaching potential victims. Players frequently exchange mods, scripts, and unofficial tools through forums, Discord servers and file-sharing websites.

Attackers are all too aware of gamers’ habits. They can exploit this behavior by disguising malware as cheats or utilities that promise exclusive features, improved performance, or the ability to evade anti-cheat systems.

Bitdefender security researchers have identified a malware campaign targeting players searching for cheats for games such as Roblox. The campaign impersonates Xeno, a popular Roblox script executor used to automate actions and run custom scripts.

Because such tools are frequently detected or blocked by the game client, versions advertised as “undetected” can be particularly attractive to users seeking to bypass these restrictions.

The malicious packages are promoted through forums and Discord communities, either directly by the operators or through compromised and impersonated accounts.

Throughout the infection chain, the malware tries to maintain a veneer of legitimacy. Its components imitate files from a Xeno installation, while later stages use Windows-like DLL names, trusted-looking directories and display-related persistence entries.

The final malware stage is a sophisticated stealer and remote access trojan that uses anti-analysis and anti-sandboxing techniques, which means that it’s trying hard not to be analyzed by security researchers.

It can steal browser cookies, personal accounts such as Discord, Roblox and Minecraft, and payment-related information that could lead to financial damage.

ThreatLocker researchers previously [documented](https://www.threatlocker.com/blog/powercat-malware-campaign-fake-game-cheats-deliver-infostealer-targeting-discord-roblox-and-crypto-wallets) this campaign under the name Powercat. Our insights revealed additional command-and-control domains and capabilities, which suggests that the malware remains under active development and continues to be used in cybercriminal operations.

The campaign has affected users since the beginning of the year. Activity increased significantly during the second half of March and has since maintained a relatively consistent infection rate.

![](https://blogapp.bitdefender.com/labs/content/images/2026/08/killchain_java.drawio.png)

Fig. 1. Java stealer killchain

## Initial Access: Fake Xeno Cheats and Stage 1 Execution

For initial access, users are tricked into downloading fake game cheats, such as Xeno, a widely used cheat software for Roblox. The software packages often come either in the form of archives containing extraction and execution instructions or as self-extracting archives that automatically unpack and prepare the environment.

These archives use a directory structure that resembles a legitimate Xeno installation. File names are chosen to make the package look convincing to users expecting Roblox cheat software. Some files are indeed LUA scripts taken from a Xeno installation, while others, such as RbxAnalytics.png, are only small 10-byte files containing junk data.

![](https://blogapp.bitdefender.com/labs/content/images/2026/08/-A1A65453-44F4-4F08-8B22-D71DB67EB39E--20260708-094739-1.png)

Fig. 2. Mimicking a Xeno installation

The user is then told to run the main entry point located at *%LOCALAPPDATA%\Xeno\workspace\cache\xeno.exe*, believing it will launch the expected game cheat. In reality, this is not the legitimate Xeno binary, but the first stage of the malware masquerading as it.

First, xeno.exe checks whether a Java executable exists at %LOCALAPPDATA%\Java\jre\bin\javaw.exe. If the file is missing, it extracts a Java Runtime Environment to that path from an archive named instance.exe, using an embedded PowerShell command.

```
powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -Command \"Add-Type -AssemblyName System.IO.Compression.FileSystem;[System.IO.Compression.ZipFile]::ExtractToDirectory(...)
```

Next, xeno.exe reads the contents of *XenoIcon.jpg*, which contains the keys required by the second stage to validate its execution with the C2 server. Finally, it launches javaw.exe to execute a JAR file masquerading as *decompiler.exe*, passing the contents of XenoIcon.jpg as command-line arguments.

## Stage 2: decompiler.exe, a JAR Disguised as a Windows Executable

The decompiler.exe file is a JAR file masque...