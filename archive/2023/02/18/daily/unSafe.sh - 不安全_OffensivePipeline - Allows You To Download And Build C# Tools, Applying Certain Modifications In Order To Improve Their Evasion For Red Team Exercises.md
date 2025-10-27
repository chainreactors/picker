---
title: OffensivePipeline - Allows You To Download And Build C# Tools, Applying Certain Modifications In Order To Improve Their Evasion For Red Team Exercises
url: https://buaq.net/go-149882.html
source: unSafe.sh - 不安全
date: 2023-02-18
fetch_date: 2025-10-04T07:20:19.252066
---

# OffensivePipeline - Allows You To Download And Build C# Tools, Applying Certain Modifications In Order To Improve Their Evasion For Red Team Exercises

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

![](https://8aqnet.cdn.bcebos.com/f43a3a8edeb7410e20c8198c5d20941e.jpg)

OffensivePipeline - Allows You To Download And Build C# Tools, Applying Certain Modifications In Order To Improve Their Evasion For Red Team Exercises

OfensivePipeline allows you to download and build C# tools, applying certain modifications i
*2023-2-17 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-149882.htm)
阅读量:82
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiIAcpmG9faTqljBdLq3FhZCnf5ehyEHVNYC9uuf1QTJ2bVy0fG0W0IguKY9PygJr93gmkvbZuy_1YJ1c14v3gQi11IDcs1qaMCWAiXGVa41VqWEYBzsZ7ZlUwVJyEgNpC2kTD4Exg8HfE1AK-JL3qgBdTrejGYMt_NnwqWknBc2yZQGii3G17C0rdipA=w640-h436)](https://blogger.googleusercontent.com/img/a/AVvXsEiIAcpmG9faTqljBdLq3FhZCnf5ehyEHVNYC9uuf1QTJ2bVy0fG0W0IguKY9PygJr93gmkvbZuy_1YJ1c14v3gQi11IDcs1qaMCWAiXGVa41VqWEYBzsZ7ZlUwVJyEgNpC2kTD4Exg8HfE1AK-JL3qgBdTrejGYMt_NnwqWknBc2yZQGii3G17C0rdipA)

**OfensivePipeline** allows you to download and build C# tools, applying certain modifications in order to improve their evasion for Red Team exercises.

## Features

* Currently only supports C# (.Net Framework) projects
* Allows to clone public and private (you will need credentials :D) git repositories
* Allows to work with local folders
* Randomizes project GUIDs
* Randomizes application information contained in AssemblyInfo
* Builds C# projects
* Obfuscates generated binaries
* Generates shellcodes from binaries
* There are 79 tools parameterised in YML templates (not all of them may work :D)
* New tools can be added using YML templates
* It should be easy to add new plugins...

## What's new in version 2.0

* Almost complete code rewrite (new bugs?)
* Cloning from private repositories possible (authentication via GitHub authToken)
* Possibility to copy a local folder instead of cloning from a remote repository
* New module to generate shellcodes with [Donut](https://github.com/TheWover/donut "Donut")
* New module to randomize GUIDs of applications
* New module to randomize the AssemblyInfo of each application
* 60 new tools added

## Examples

* List all tools:

```
OffensivePipeline.exe list
```

* Build all tools:

```
OffensivePipeline.exe all
```

* Build a tool

```
OffensivePipeline.exe t toolName
```

* Clean cloned and build tools

### Output example

```
PS C:\OffensivePipeline> .\OffensivePipeline.exe t rubeus

ooo
                                                                                           .osooooM M
      ___   __  __                _           ____  _            _ _                      +y.     M M
     / _ \ / _|/ _| ___ _ __  ___(_)_   _____|  _ \(_)_ __   ___| (_)_ __   ___           :h  .yoooMoM
    | | | | |_| |_ / _ \ '_ \/ __| \ \ / / _ \ |_) | | '_ \ / _ \ | | '_ \ / _ \          oo  oo
    | |_| |  _|  _|  __/ | | \__ \ |\ V /  __/  __/| | |_) |  __/ | | | | |  __/          oo  oo
     \___/|_| |_|  \___|_| |_|___/_| \_/ \___|_|   |_| .__/ \___|_|_|_| |_|\___|          oo  oo
                                                     |_|                            MoMoooy.  h:
                                                                                       M M     .y+
                                                                                    M Mooooso.
                                                                                    ooo

@aetsu
                                                                                v2.0.0

[+] Loading tool: Rubeus
    Clonnig repository: Rubeus into C:\OffensivePipeline\Git\Rubeus
                 Repository Rubeus cloned into C:\OffensivePipeline\Git\Rubeus

[+] Load RandomGuid module
        Searching GUIDs...
                > C:\OffensivePipeline\Git\Rubeus\Rubeus.sln
                > C:\OffensivePipeline\Git\Rubeus\Rubeus\Rubeus.csproj
                > C:\OffensivePipeline\Git\Rubeus\Rubeus\Properties\AssemblyInfo.cs
        Replacing GUIDs...
                File C:\OffensivePipeline\Git\Rubeus\Rubeus.sln:
                           > Replacing GUID 658C8B7F-3664-4A95-9572-A3E5871DFC06 with 3bd82351-ac9a-4403-b1e7-9660e698d286
                        > Replacing GUID FAE04EC0-301F-11D3-BF4B-00C04F79EFBC with 619876c2-5a8b-4c48-93c3-f87ca520ac5e
                        > Replacing GUID 658c8b7f-3664-4a95-9572-a3e5871dfc06 with 11e0084e-937f-46d7-83b5-38a496bf278a
                [+] No errors!
                File C:\OffensivePipeline\Git\Rubeus\Rubeus\Rubeus.csproj:
                        > Replacing GUID 658C8B7F-3664-4A95-9572-A3E5871DFC06 with 3bd82351-ac9a-4403-b1e7-9660e698d286
                        > Replacing GUID FAE04EC0-301F-11D3-BF4B-00C04F79EFBC with 619876c2-5a8b-4c48-93c3-f87ca520ac5e
                        > Replacing GUID 658c8b7f-3664-4a95-9572-a3e5871dfc06 with 11e0084e-937f-46d7-83b5-38a496bf278a
                [+] No errors!
                File C:\OffensivePipeline\Git\Rubeus\Rubeus\Properties\AssemblyInfo.cs:
                           > Replacing GUID 658C8B7F-3664-4A95-9572-A3E5871DFC06 with 3bd82351-ac9a-4403-b1e7-9660e698d286
                        > Replacing GUID FAE04EC0-301F-11D3-BF4B-00C04F79EFBC with 619876c2-5a8b-4c48-93c3-f87ca520ac5e
                        > Replacing GUID 658c8b7f-3664-4a95-9572-a3e5871dfc06 with 11e0084e-937f-46d7-83b5-38a496bf278a
                [+] No errors!

[+] Load RandomAssemblyInfo module
        Replacing strings in C:\OffensivePipeline\Git\Rubeus\Rubeus\Properties\AssemblyInfo.cs
                [assembly: AssemblyTitle("Rubeus")] -> [assembly: AssemblyTitle("g4ef3fvphre")]
                [assembly: AssemblyDescription("")] -> [assembly: AssemblyDescription("")]
                [assembly: AssemblyConfiguration("")] -> [assembly: AssemblyConfiguration("")]
                [assembly: AssemblyCompany("")] -> [assembly: AssemblyCompany("")]
                [assembly: AssemblyProduc   t("Rubeus")] -> [assembly: AssemblyProduct("g4ef3fvphre")]
                [assembly: AssemblyCopyright("Copyright ©  2018")] -> [assembly: AssemblyCopyright("Copyright ©  2018")]
                [assembly: AssemblyTrademark("")] -> [assembly: AssemblyTrademark("")]
                [assembly: AssemblyCulture("")] -> [assembly: AssemblyCulture("")]

[+] Load BuildCsharp module
        [+] Checking requirements...
        [*] Downloading nuget.exe from https://dist.nuget.org/win-x86-commandline/latest/nuget.exe
                [+] Download OK - nuget.exe
                [+] Path found - C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\Common7\Tools\VsDevCmd.bat
        Solving dependences with nuget...
        Building solution...
                [+] No errors!
                [+] Output folder: C:\OffensivePipeline\Output\Rubeus_vh00nc50xud

[+] Load ConfuserEx module
        [+] Checking requirements...
        [+] Downloading ConfuserEx from https://github.com/mkaring/ConfuserEx/releases/download/v1.6.0/ConfuserEx-CLI.zip
                [+] Download OK - ConfuserEx
        Confusing...
                [+] No errors!

[+] Load Donut module
        Generating shellcode...

Payload options:
        Domain: RMM6XFC3
        Runtime:v4.0.30319

Raw Payload: C:\OffensivePipeline\Output\Rubeus_vh00nc50xud\ConfuserEx\Donut\Rubeus.bin
B64 Payload: C:\OffensivePipeline\Output\Rubeus_vh00nc50xud\ConfuserEx\Donut\Rubeus.bin.b64

[+] No errors!

[+] Generating Sha256 hashes
                Output file: C:\OffensivePipeline\Output\Rubeus_vh00nc50xud

-----------------------------------------------------------------
                SUMMARY

- Rubeus
         - RandomGuid: OK
         - RandomAssemblyInfo: OK
            - BuildCsharp: OK
         - ConfuserEx: OK
      ...