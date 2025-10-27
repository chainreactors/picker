---
title: 2024-10-23 WarmCookie/BadSpace - APT TA866 - Samples
url: https://contagiodump.blogspot.com/2024/10/2024-10-23-warmcookiebadspace-apt-ta866.html
source: contagio
date: 2024-10-30
fetch_date: 2025-10-06T18:55:51.298012
---

# 2024-10-23 WarmCookie/BadSpace - APT TA866 - Samples

[![contagio](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi2P174ZHnphxnV8a_Xx7hSim4CICVSFnuqeKVEFoI40K_P19maZp1I9cM2ehYNXQvuufvpOruDl_Rhcroi8rv1wW21UWvLPHdG8pK6XkqqSxM75YQ2RoxxbRM1G3nZYa6JOd4b-RP0loM/s1600/contagio222.jpg)](https://contagiodump.blogspot.com/)

## Pages

* [Home](http://contagiodump.blogspot.com/)

[Mobile and print friendly view](http://contagiodump.blogspot.com/?m=1) |

## Monday, October 28, 2024

### [2024-10-23 WarmCookie/BadSpace - APT TA866 - Samples](https://contagiodump.blogspot.com/2024/10/2024-10-23-warmcookiebadspace-apt-ta866.html)

[2024-10-23 TALOS Threat Spotlight: WarmCookie/BadSpace](https://blog.talosintelligence.com/warmcookie-analysis/)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKs2f1dzJv_T_nO0Gmse4p4IwswO66mxOkwVePAcyjBq7DvBWMgZlsC7gcWqcLv88oVLT_uQ_HaIfuW-xpC42uPLuFfRrPJnSxr71DpKwMYzhGILu77Z8t3pfEw895h_FaGgB3N4K2AW7k-CcxB2RPQ1ab5CtbthOYA8OPSjkn4-0gCtJvEJ8wka23hG0/w278-h265/Discord%202024-10-28%2023.15.02.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKs2f1dzJv_T_nO0Gmse4p4IwswO66mxOkwVePAcyjBq7DvBWMgZlsC7gcWqcLv88oVLT_uQ_HaIfuW-xpC42uPLuFfRrPJnSxr71DpKwMYzhGILu77Z8t3pfEw895h_FaGgB3N4K2AW7k-CcxB2RPQ1ab5CtbthOYA8OPSjkn4-0gCtJvEJ8wka23hG0/s367/Discord%202024-10-28%2023.15.02.png)

Summary: WarmCookie, also known as BadSpace, is a sophisticated malware family that emerged in April 2024, primarily distributed through malspam and malvertising. This malware provides long-term access to compromised environments and facilitates the deployment of additional payloads, such as CSharp-Streamer-RAT and Cobalt Strike. Its infection chains and functionality highlight notable development links to Resident backdoor, indicating possible shared authorship by TA866.

WarmCookie’s infection chain initiates through email lures—typically invoice-related and job agency themes—that direct victims to malicious JavaScript-hosting servers. The obfuscated JavaScript downloader, often delivered as a compressed ZIP, triggers a PowerShell command that uses Bitsadmin to download and execute the WarmCookie DLL, embedding itself in the system with persistence.

Persistence: WarmCookie leverages Task Scheduler to achieve persistence, creating scheduled tasks under %ALLUSERSPROFILE% or %ALLDATA%, and re-executing itself after a 60-second delay. The latest version modifies the typical command-line syntax from /p to /u for execution parameters.

Command-and-Control (C2) Adaptation: TA866 previously used unique, detectable C2 user-agent strings (e.g., Mozilla/4.0 (compatible; MSIE 6.0…)), which have since been updated to blend with standard strings like Mozilla/5.0… Firefox/115.0.

Self-Updating Mechanism: An initial implementation of a self-update command allows WarmCookie to receive updates dynamically from its C2 server, although this feature appears incomplete.

C2 Command Updates

The latest WarmCookie samples feature new C2 commands:

Command 0x8: Receives a DLL from C2, assigns it a temporary filename, and executes it.

Command 0xA: Similar to Command 0x8 but adds hardcoded parameters, allowing self-updating.

Command 0xB: Moves the malware to a new temporary filename and deletes the scheduled task to disable persistence and terminate the malware process.

Code and Function Similarities to Resident Backdoor

A code-level comparison between Resident backdoor and WarmCookie shows:

RC4 Decryption Consistency: Both use identical RC4 implementations and mutex management, often employing GUID-like strings for mutexes.

Startup Logic: Both use similar logic for identifying execution as a DLL or EXE and establishing persistence through scheduled tasks. They both use rundll32.exe for DLL-based execution and task scheduling.

Coding Conventions: Functions, parameter passing, and persistence mechanisms align closely, suggesting shared development practices or authorship.

**Download**

[![Image](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj9fekBavhMnuxb9txFvxkWzKz4DZBXwlXNpsm2_s6FKlTJngInQG_9h4amviU59zeRl61NodBmrkvhq-mtc9FDyOUGO8ZaBK-QZFXtHsqFqL0su0Z6rt5Hqpp8WElMdztahWYVyZ2dfdE/s1600/rednag.png)

[Download. Email me if you need the password scheme](https://s3.us-east-1.amazonaws.com/contagio.deependresearch.org/APT/Russia/2024-10-23%2BTA866%2BWarmCookie-BadSpace.zip)

**File Information**

* ├── 0b26abc692b7a2877b6b6fce6aa99b29af125b063f1c41b507362def59f8dfce
* ├── 0c9697506df18baac4b4215e78a43926ea4bb94ea3607c851a1c2fe3b5b31f17
* ├── 0d2cf14d27586ff9da5832e0efaba872a1641617fdb4a47d94b645172f7d2fa6
* ├── 0d305291091bcb0c943c6472dce450272b2291b6287a053c5c553f082654c718
* ├── 0d59c9bef911c879011f21163a083c09b759c9757f1ade9da9f87fdce27dc5f4
* ├── 0da87bff1a95de9fc7467b9894a8d8e0486dfd868c2c7305e83951babacde642
* ├── 0f11caad7cd5cf4de78145a13590fb50a42a63aaf3bbc6066d2a0bb58a2068f7
* ├── 124e2b15b001eb302f0a5f43604621a001d250d42afdf353dc812f41bf249a55
* ├── 13142aa3c815362511acee0b74672081d7bb8cd3cabd8ab4c85fb7ba8126aec5
* ├── 13ccffd00e2fa89167e29a8d382d8c417e198ffce8684df23e4a8a91fdc0f23e
* ├── 15b1eb1072de7e16d5b7693a16269b315c0926558fa2cbbcd2948c2dd16ab8a0
* ├── 193cadbea116833efaaa0bc6fbea552a68c9694fb0177ad873d702001b4cef8d
* ├── 1bcfed8b593a8a7c8b34e074aca3d4fc68a0ea3343b32eae89fdabf35ad40e7d
* ├── 1d9f4690a62fd4d17c031924585b1e46e417d8c72f331ba51cf0eceeb91f6579
* ├── 1dd740062b30ce02e90238d55cb6f786496e120a40e93334fef7033e75d46d79
* ├── 1ea681b79f88c2f0e9344beedb8776643d735c3f8251479c9495537c40fe5ba1
* ├── 283cd2138b4f1ffef36411adee02f5d684593bdf3117c760ade04e19c958028a
* ├── 295d01d02376044ec078128788b4439eba63184147f0137852160952ad1649c2
* ├── 2a311dd5902d8c6654f2b50f3656201f4ceb98c829678834edaeae5c50c316f5
* ├── 2a4451ef47b1f4b971539fb6916f7954f80a6735cf75333fa9d19b169c31de2e
* ├── 2a5a12cc4ef2f0f527cc072243aa27d3e95e48402ef674e92c6709dc03a0836a
* ├── 2cbd9f49b2dec8a36e0961b5471bdb3266a5c061ba8784e14a193e700d156a0c
* ├── 2f434cc508baac8440e95e955306ee354e76680eedca4a3ec2d87f592cfdcba7
* ├── 30a85fa1bf6df41d841efbf986beb286eb829380ebfdf0c1ac694f3d4f24315a
* ├── 32ff6653fb6e4757c1f7206af26475445e1e43c8e1db0af5309ad8a9c4d86ba1
* ├── 33f81ee6d9747afe1c7c5a6ed741822749ea42bb297eb642f720fd44ae35e786
* ├── 34f2fc85932f6fede57846cf2a2d55172d28e4a251bb4434a88a02ce8ec030f0
* ├── 38f4b197dcda32b14dc98127e3a523364822e108f85153105b77b85ce31438d7
* ├── 3f073189506b7ca07fb352e267699688bd3a6c11cde72217ec1ffbae211b6e15
* ├── 40cdac6696e84f677d7e4817fd85f32da0f9256866bb85a25da207e3d5ca7d5c
* ├── 41d9d1e0599b492fdb6fa2ce47f0094112799830dd8dc1c098690a500a8fa6b1
* ├── 425da6a7bd4faedc97990c6458d5e6a0635839037a99611385b77b43b443d1ec
* ├── 43b87cf9b5a73d9bdfdbd9e1da3cb4d1e26a509d328a90c01cc0025a9cb1698f
* ├── 44faed020d5d8b29918a3f02d757b2cfada67574cf9e02748ea7f75ba5878907
* ├── 475edfbb2b03182ef7c42c1bc2cc4179b3060d882827029a6e67c045a0c1149b
* ├── 48320e88c9188d97e7f6a06eddcc8e1f89cf79ed66b68a546cd38e76f183b13e
* ├── 48640e2fb35f073c22937784f32c157d9a0781d61a2293f73fc3566b708205bd
* ├── 4b4e27824cd349192cf0913060f1481a192f2b13d44e2787edbe8d7f0c57fa06
* ├── 4cccc2d7f97a78dd0ef3f06a2fdb555299cd06c4222dd546d87a4ed735743d48
* ├── 4e731e9e0233d53c70830011690f59b0764f61aa19e49cd10bed92b6eb81762c
* ├── 4ff20a31223f3c0a04f1646332979c89fce5111f9d288b69568c9120d13c564c
* ├── 53db2f135883d74dcac2e620d14d7f775876bf49d3d5d4fdb131f8fed4917434
* ├── 5428e75adfc1f8d9b551f0e912db89c9f82db0bb574a80553b2ee8a829668d18
* ├── 55ace018a6c4f355511ce3f6833d4b997d4323afb890520dc815aa2f916499f3
* ├── 5649dcd896bf2155e790c5f05b9fa2ba6fe5befcac85a8cb0beed23945686e02
* ├── 56984cac7431ef001246350eaa6011cf2f34571e231b29572d27f962f6c7f165
* ├── 56f9bd572b3d7c65da3d50d77a71fec0f8b4320f7bf7f691221522ac62e5d99b
* ├── 5970ba228d2afe2031b8e8c17ba284746ebb9066f0ccb8e1fe33a6e3927a6c97
* ├── 5ab9b4e3f15a04bfe240368d9cea4e6f...