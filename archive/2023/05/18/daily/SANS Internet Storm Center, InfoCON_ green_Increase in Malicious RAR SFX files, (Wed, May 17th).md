---
title: Increase in Malicious RAR SFX files, (Wed, May 17th)
url: https://isc.sans.edu/diary/rss/29852
source: SANS Internet Storm Center, InfoCON: green
date: 2023-05-18
fetch_date: 2025-10-04T11:42:40.286210
---

# Increase in Malicious RAR SFX files, (Wed, May 17th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29848)
* [next](/diary/29858)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Increase in Malicious RAR SFX files](/forums/diary/Increase%2Bin%2BMalicious%2BRAR%2BSFX%2Bfiles/29852/)

**Published**: 2023-05-17. **Last Updated**: 2023-05-17 04:19:08 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Increase%2Bin%2BMalicious%2BRAR%2BSFX%2Bfiles/29852/#comments)

This isn't a new attack vector, but I’ve found many malicious RAR SFX files in the wild for a few weeks. An “SFX” file is a self-extracting archive that contains compressed files and is wrapped up with some executable code to decompress them on the fly. The final user receives an executable file (PE file) that can be launched with the need to install a specific tool to decompress the content.  This technique has been used for a while by attackers, and even more interesting, the self-decompression routine can launch any executable (another executable, a script, …)[[1](https://www.rarlab.com/vuln_sfx_html.htm)]

Most of the time, these files aren’t detected as a known threat because payloads (the files) are compressed (sometimes encrypted too - if a password is used). But they are generally detected as “suspicious”. I wrote a simple YARA rule to detect such files:

```

rule SelfExtractingRAR
{
    meta:
        description = "Detects an SFX archive with automatic script execution”
        author = “Xavier “Mertens <[email protected]>”

    strings:
        $exeHeader = "MZ"
        $rarHeader = "Rar!" wide ascii
        $sfxSignature = "SFX" wide ascii
        $sfxSetup = "Setup=" wide ascii

    condition:
       $exeHeader at 0 and $rarHeader and $sfxSignature and $sfxSetup
}
```

Here is an example of such SFX file that I spotted yesterday. The file was delivered through a phishing campaign and was called "USD 1,810,500.exe” with the following SHA256: e08a8ff9fadce5026127708c57b363bd0b2217a0a96d9ba4e7994601ad1a8963[[2](https://bazaar.abuse.ch/sample/e08a8ff9fadce5026127708c57b363bd0b2217a0a96d9ba4e7994601ad1a8963/)]. A good point with such files is that you don’t need to execute them to extract the content. A classic rar command will do the job:

```

remnux@remnux:/MalwareZoo/20230516$ rar t "USD 1,810,500.exe"

RAR 5.50   Copyright (c) 1993-2017 Alexander Roshal   11 Aug 2017
Trial version             Type 'rar -?' for help

Testing archive USD 1,810,500.exe

1ktZ3RF93vZq427h3lvsYTk434w53G56ek6xCJ
SILENT= 144k80p185MQ7FN1
sF7Yy34s49U9R76Rku09Q0L19P
Setup=wscript Update-sk.s.vbe
q2X4nb8h8ay8003mjTM3W41S2Q77ssEIDH7zXpA
Path=%homedrive%\pxbc
TDaTWZ41l2f4d80XMx97NB5C298bdY
Update=U 06646163K1p2p66F
67562az6K38H90tYJgQTx963kZWMg

Testing     vicmmge.buj                                               OK
Testing     uhupfsx.xml                                               OK
Testing     kmpxxcxmlq.docx                                           OK
Testing     Update-sk.s.vbe                                           OK
Testing     pxqic.pif                                                 OK
Testing     fpss.msc                                                  OK
Testing     epmtilluig.xml                                            OK
Testing     psxgfd.icm                                                OK
Testing     pprwvki.ppt                                               OK
Testing     qcrk.xls                                                  OK
Testing     ppldgtbkm.xml                                             OK
Testing     loffd.mp3                                                 OK
Testing     wfsdrusej.icm                                             OK
Testing     utmkbkhe.jpg                                              OK
Testing     lhuhm.docx                                                OK
Testing     jcftejksj.xls                                             OK
Testing     nkeej.xl                                                  OK
Testing     wtnjesas.pdf                                              OK
Testing     riaam.txt                                                 OK
Testing     clff.pdf                                                  OK
Testing     rnovsgsm.txt                                              OK
Testing     gcprhnl.xls                                               OK
Testing     lhulocrs.xls                                              OK
Testing     bxmrh.msc                                                 OK
Testing     xsdmudolb.xml                                             OK
Testing     xppwqdiutn.jpg                                            OK
Testing     eleuutbq.ppt                                              OK
Testing     cttrdjfv.xml                                              OK
Testing     ccgjrkh.ini                                               OK
Testing     lpuukd.icm                                                OK
Testing     eetv.exe                                                  OK
Testing     sqtu.docx                                                 OK
Testing     uvkmtkcrvq.icm                                            OK
Testing     efitdtqci.bmp                                             OK
Testing     ruvjtenq.mp3                                              OK
Testing     wucrjivio.pdf                                             OK
Testing     bhbeq.icm                                                 OK
Testing     waemwttb.pdf                                              OK
Testing     wfhesiw.xml                                               OK
Testing     sxvkks.xls                                                OK
Testing     negbxaqdr.msc                                             OK
Testing     wmlpuwiwdd.ini                                            OK
Testing     vged.msc                                                  OK
Testing     pmevdiqiww.ppt                                            OK
Testing     gwrtofbgi.mp3                                             OK
Testing     kejrxfveni.jpg                                            OK
Testing     bnubxgq.pdf                                               OK
Testing     bdldxj.msc                                                OK
Testing     hnbfjb.icm                                                OK
Testing     tpshh.xml                                                 OK
Testing     exdsgg.icm                                                OK
Testing     jmwnkkmc.icm                                              OK
Testing     bkmlgvggjq.xml                                            OK
Testing     mqen.bin                                                  OK
Testing     inxwfoap.dll                                              OK
Testing     qxskgk.ppt                                                OK
Testing     etiwhseh.txt                                              OK
Testing     gvgbbm.mp3                                                OK
Testing     duacabnhh.txt                                             OK
Testing     blcvjevx.msc                                              OK
Testing     xjwwawkp.msc                                              OK
Testing     jfbbaim.dat                                               OK
Testing     xksrkjuj.exe                                              OK
Testing     dndafdxcs.docx                                            OK
Testing     cauhoxnn.bmp                                              OK
Testing     adtp.icm                                                  OK
Testing     miwvkhxw.xml        ...