---
title: Chimera - Automated DLL Sideloading Tool With EDR Evasion Capabilities
url: https://buaq.net/go-174424.html
source: unSafe.sh - 不安全
date: 2023-08-15
fetch_date: 2025-10-04T11:59:46.323460
---

# Chimera - Automated DLL Sideloading Tool With EDR Evasion Capabilities

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Chimera - Automated DLL Sideloading Tool With EDR Evasion Capabilities

While DLL sideloading can be used for legitimate purposes, such as loading necessary librarie
*2023-8-14 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-174424.htm)
阅读量:27
收藏*

---

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZ6m7sXp4JI_v03T-6tv3Wtvrndy7MjoWNSQ24a0Z6t2h9oaAYLX2EjyQqZq57JFGY74G3FyyxMXmG4maTLpePuPGq2RuNzoLIw93J8eXh-96hP93RgiB_onVtTtRJO7mTx1tpYjbRhZWdyiIkuwkL_yEJKIoqev3m9aUZzRS4TdyQKKNCbsSJsSk4liF1/w640-h640/Chimera_1_Chimera.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZ6m7sXp4JI_v03T-6tv3Wtvrndy7MjoWNSQ24a0Z6t2h9oaAYLX2EjyQqZq57JFGY74G3FyyxMXmG4maTLpePuPGq2RuNzoLIw93J8eXh-96hP93RgiB_onVtTtRJO7mTx1tpYjbRhZWdyiIkuwkL_yEJKIoqev3m9aUZzRS4TdyQKKNCbsSJsSk4liF1/s1000/Chimera_1_Chimera.png)

While DLL sideloading can be used for legitimate purposes, such as loading necessary libraries for a program to function, it can also be used for malicious purposes. Attackers can use DLL sideloading to execute arbitrary code on a target system, often by [exploiting vulnerabilities](https://www.kitploit.com/search/label/Exploiting%20Vulnerabilities "exploiting vulnerabilities") in legitimate applications that are used to load DLLs.

To automate the DLL sideloading process and make it more effective, Chimera was created a tool that include evasion methodologies to bypass EDR/AV products. These tool can automatically encrypt a shellcode via XOR with a random key and create template Images that can be imported into Visual Studio to create a malicious DLL.

Also Dynamic Syscalls from [SysWhispers2](https://www.kitploit.com/search/label/SysWhispers2 "SysWhispers2") is used and a modified assembly version to evade the pattern that the EDR search for, Random nop sleds are added and also registers are moved. Furthermore Early Bird Injection is also used to inject the shellcode in another process which the user can specify with Sandbox Evasion mechanisms like HardDisk check & if the process is being debugged. Finally Timing attack is placed in the loader which using waitable timers to delay the execution of the shellcode.

This tool has been tested and shown to be effective at bypassing EDR/AV products and executing arbitrary code on a target system.

## Tool Usage

Chimera is written in python3 and there is no need to install any extra dependencies.

Chimera currently supports two DLL options either Microsoft teams or Microsoft OneDrive.

Someone can create userenv.dll which is a missing DLL from Microsoft Teams and insert it to the specific folder to

`⁠%USERPROFILE%/Appdata/local/Microsoft/Teams/current`

For Microsoft OneDrive the script uses version DLL which is common because its missing from the binary example onedriveupdater.exe

### Chimera Usage.

`python3 ./chimera.py met.bin chimera_automation notepad.exe teams`

`python3 ./chimera.py met.bin chimera_automation notepad.exe onedrive`

### Additional Options

* [raw payload file] : Path to file containing shellcode
* [output path] : Path to output the C template file
* [process name] : Name of process to inject shellcode into
* [dll\_exports] : Specify which DLL Exports you want to use either teams or onedrive
* [replace shellcode variable name] : [Optional] Replace shellcode variable name with a unique name
* [replace xor [encryption](https://www.kitploit.com/search/label/Encryption "encryption") name] : [Optional] Replace xor encryption name with a unique name
* [replace key variable name] : [Optional] Replace key variable name with a unique name
* [replace sleep time via waitable timers] : [Optional] Replace sleep time your own sleep time

### Usefull Note

Once the compilation process is complete, a DLL will be generated, which should include either "version.dll" for OneDrive or "userenv.dll" for Microsoft Teams. Next, it is necessary to rename the original DLLs.

For instance, the original "userenv.dll" should be renamed as "tmpB0F7.dll," while the original "version.dll" should be renamed as "tmp44BC.dll." Additionally, you have the option to modify the name of the proxy DLL as desired by altering the source code of the DLL exports instead of using the default script names.

## Visual Studio Project Setup

Step 1: Creating a New Visual Studio Project with DLL Template

1. Launch Visual Studio and click on "Create a new project" or go to "File" -> "New" -> "Project."
2. In the project templates window, select "Visual C++" from the left-hand side.
3. Choose "Empty Project" from the available templates.
4. Provide a suitable name and location for the project, then click "OK."
5. On the project properties window, navigate to "Configuration Properties" -> "General" and set the "Configuration Type" to "Dynamic Library (.dll)."
6. Configure other project settings as desired and save the project.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEho0IKdbW0zv24nue5VmgE4POEI9QYZHVPovMbadzzuTo6jtM-ZEK7SOLCSEjtL1WsXBBEcuMeDiDDa_R0b6rsuw2832SyKLOOKKuj507Wef_0iMxcV_zt8123FCieAoExmT0jdfOCMFL1N8CnyyeC0sY6DbGvfAzHthHwWi1-11ahyH7qvyeox_dBwqzq-/w640-h454/Chimera_2_image.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEho0IKdbW0zv24nue5VmgE4POEI9QYZHVPovMbadzzuTo6jtM-ZEK7SOLCSEjtL1WsXBBEcuMeDiDDa_R0b6rsuw2832SyKLOOKKuj507Wef_0iMxcV_zt8123FCieAoExmT0jdfOCMFL1N8CnyyeC0sY6DbGvfAzHthHwWi1-11ahyH7qvyeox_dBwqzq-/s947/Chimera_2_image.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3T2v2gGlEXNM13T2jhRa7ePCtdui74Sc9EBtfzJ98s2i8rj2cOTaDWeUVxeEzYhMf27gkYhe3JpCp1pWmTV-fsybY1AeKtsRsAZgkmm3Mxc9_xZIF_WnAnbGBgf4zL43umeWvkg5U_lrU7q77_UQ6F9lkDRtPOxEjEiY7Tlvg41oXzRWQyYnWROi7gjFk/w640-h454/Chimera_3_image%25202.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3T2v2gGlEXNM13T2jhRa7ePCtdui74Sc9EBtfzJ98s2i8rj2cOTaDWeUVxeEzYhMf27gkYhe3JpCp1pWmTV-fsybY1AeKtsRsAZgkmm3Mxc9_xZIF_WnAnbGBgf4zL43umeWvkg5U_lrU7q77_UQ6F9lkDRtPOxEjEiY7Tlvg41oXzRWQyYnWROi7gjFk/s947/Chimera_3_image%25202.png)

Step 2: Importing Images into the Visual Studio Project

1. Locate the "chimera\_automation" folder containing the necessary Images.
2. Open the folder and identify the following Images: main.c, syscalls.c, syscallsstubs.std.x64.asm.
3. In Visual Studio, right-click on the project in the "Solution Explorer" panel and select "Add" -> "Existing Item."
4. Browse to the location of each file (main.c, syscalls.c, syscallsstubs.std.x64.asm) and select them one by one. Click "Add" to import them into the project.
5. Create a folder named "header\_Images" within the project directory if it doesn't exist already.
6. Locate the "syscalls.h" header file in the "header\_Images" folder of the "chimera\_automation" directory.
7. Right-click on the "header\_Images" folder in Visual Studio's "Solution Explorer" panel and select "Add" -> "Existing Item."
8. Browse to the location of "syscalls.h" and select it. Click "Add" to import it into the project.

Step 3: Build Customization

1. In the project properties window, navigate to "Configuration Properties" -> "Build Customizations."
2. Click the "Build Customizations" button to open the build customization dialog.

Step 4: Enable MASM

1. In the build customization dialog, check the box next to "masm" to enable it.
2. Click "OK" to close the build customization dialog.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjX0Q_h4AB8lWXPKCEaYQOW0AcwRiNdyUzWde_g3so_y-MQ9IIQM6Wd-cANbwHtxq1Qx7D5DCS_FLd5mYilsCVeNa9Vj5U1ZwRKP7AbQHj10v0HmkW6N3j-1DWUEiLxyNtV2USzVJP3PGSFNFNxfiLpG-WgTyAhpewWBRH8vNrdBlUyEL4TSvt-nkufQEap/w640-h166/Chimera_4_image%25203.png)](https://blogger.googleusercontent.com/img...