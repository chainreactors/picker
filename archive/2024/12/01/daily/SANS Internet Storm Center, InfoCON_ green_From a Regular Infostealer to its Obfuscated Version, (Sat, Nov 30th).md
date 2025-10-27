---
title: From a Regular Infostealer to its Obfuscated Version, (Sat, Nov 30th)
url: https://isc.sans.edu/diary/rss/31484
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-01
fetch_date: 2025-10-06T19:38:05.986479
---

# From a Regular Infostealer to its Obfuscated Version, (Sat, Nov 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31480)
* [next](/diary/31486)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [From a Regular Infostealer to its Obfuscated Version](/forums/diary/From%2Ba%2BRegular%2BInfostealer%2Bto%2Bits%2BObfuscated%2BVersion/31484/)

**Published**: 2024-11-30. **Last Updated**: 2024-11-30 06:48:43 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/From%2Ba%2BRegular%2BInfostealer%2Bto%2Bits%2BObfuscated%2BVersion/31484/#comments)

There are many malicious scripts available on the Internet. Github has plenty of info stealers and RATs made available “for testing or research purposes”. Here is one that I found recently: Trap-Stealer[[1](https://github.com/TheCuteOwl/Trap-Stealer/tree/main)]. Often those scripts are pretty well obfuscated to pass through security controls and make Security Analysts’ life harder. Let’s review a practical example.

Today, I won't review the info stealer capabilities because they are common but let's check the obfuscation techniques. The file was dropped as a fake JPEG image: C:\Users\user\AppData\Local\apxpvddh.jpeg. It has a low score on VT: 3/63[[2](https://www.virustotal.com/gui/file/85a0342027420025c477f3f6ab68376aa1608a447d1fb24920ac36b7cf7fd59d/detection)].

First, the code is “flooded” with classes that do nothing:

```

class TtV4adTuzK:
    def __init__(self):
        self.data = True
    def get_data(self):
        return self.data
class nxTJRP4oBo:
    def __init__(self):
        self.data = True
    def get_data(self):
        return self.data
class cLaiqjSQel:
    def __init__(self):
        self.data = True
    def get_data(self):
        return self.data
```

Or useless variables:

```

J4BL2VTnoS = 95994844
Q5eKoFfYgd = 79322716
ME2ZgJpLA0 = 84016443
m4tvU1GFfJ = 31572061
EacvCg0xlz = 58092955
TRwCJhKsQb = 88130587
```

Dependencies with some Python modules are resolved:

```

requirements = [
    ["requests", "requests"],
    ["Cryptodome.Cipher", "pycryptodomex" if not 'PythonSoftwareFoundation' in executable else 'pycryptodome']
]
for modl in requirements:
    try:
        import_module(module[0])
    except:
        subprocess.Popen(executable + " -m pip install " +modl[1], shell=True)
        time.sleep(3)
```

The interesting code starts here:

```

f2KQN4bukRZMWSZicAmmYUWycFs6d0m5AqoEhG(base64.b64decode(S3ZpuwXgombrIYkwUNwRUJmSFtqLNOGKAHETR1))
```

A huge chunk of Base64 data is decoded and passed to f2KQN4bukRZMWSZicAmmYUWycFs6d0m5AqoEhG, an alias for exe()!

Once decoded, a second script obfuscated with the same techniques is disclosed. It contains another Base64 chunk of data. This time, the decoded data is encrypted.

Here a funny technique is used to decrypt the next payload. An array of encryption keys is provided and all of them are tested until the decryption succeeds:

```

s = [b'Co-7hDMhMh7UtUQ29kT0J7krqsTXPUAFXA7RtpcU6xY=',
     b'cbkSAtHBbB-1QGa6bhIz_faB_iLXMnoQ2DnoXOGCxLo=',
     b'0d5ykqArsb7Gkb3ZJtjr5-nzIF-2bOYgKtwAyny8B8k=',
     b'ztG6jHYX0PPlTa_yMzrrxLelrKf79hovRQADx5sioXo=',
     b'JT0JyIIHm3LfeAuit0xf-vej3m37Qhxvnwc3flWQ3ew=',
     b'0lSaIjRa6nePT6QiGIoPpVrw8EMHDCT_I7T6JwCk0Cc=',
     b'KhJzINwra-Dv78aZpTZeqClzc484KhtXEO8fvmV38nY=',
     b'cRReHk0vv3NlLplRTBxly-B5LamTR4s-7UwaGl-iuak=',
     b'NWXrr-8oMnHPP9q46JheOjH46abeH9_kHUcUjhxRbsE=',
     b'4Vu6YVdZGOSclihs4ukSRppyV1M62QFqwp7ZU6y3RBs=',
     b'M1qQk8eFmk_tigtJgYhOFQVb6pxA4YAfzXAbzx-0BhA=',
     b'0KjwnWf-Bqri4ae4UVy3pBUCCcAWiFbgWjkWmd7zsdI=',
     b'WBkyoZfIwgzunYz9je8_-lBeotQ2ntjx59kVuscHboQ=',
     b'usQcLUBWrVM7dENg0A6ge15mHK9RtB4RV6MB4hbD70o=']
for key in s:
    try:
        decrypted_code = wqSJRHIzn7T3FiBgqfmquhhSEyCwLpRRMcdtF3(key.decode("utf-8")).decrypt(encrypted_code)
        break
    except Exception as e:
        pass
```

Finally, the decrypted code is decompressed and executed:

```

decompressed_code = zlib.decompress(decrypted_code).decode('utf-8')
f2KQN4bukRZMWSZicAmmYUWycFs6d0m5AqoEhG(decompressed_code)
```

You may wonder how these obfuscation techniques are implemented by the attacker. They have tools for this! In the context of Trap-Stealer, the obfuscation tool is even part of the repository[[3](https://github.com/TheCuteOwl/Trap-Stealer/blob/main/obfuscator.py)]. Here is how it works:

```

remnux@remnux:/MalwareZoo/20241125/Trap-Stealer$ mkdir build
remnux@remnux:/MalwareZoo/20241125/Trap-Stealer$ cat <<__END__ >build/temp.py
print("This is a super malicious Python script! }:->")
__END__
remnux@remnux:/MalwareZoo/20241125/Trap-Stealer$ python3 ./obfucator.py my_super_cool_infostealer
INFO:root:The code has been encrypted, Filename: ./build/my_super_cool_infostealer.py
remnux@remnux:/MalwareZoo/20241125/Trap-Stealer$ head build/my_super_cool_infostealer.py

from sys import executable, stderr
ueupD5ALo7 = 33628666
VKkflw4g74 = 98340683
XRPK2HJT5b = 80807402
fhaj93exmX = 5089192
class fMVSRbmSTG:
    def __init__(self):
        self.data = True
remnux@remnux:/MalwareZoo/20241125/Trap-Stealer$ python3 build/my_super_cool_infostealer.py
[...pip stuff removed ...]
This is a super malicious Python script! }:->
```

Note that the obfuscated file is pretty big compared to the "clear text" version: 37 bytes for "temp.py" and 20087 bytes for "my\_super\_cool\_infostealer.py". Obfuscation has a cost! :-)

[1] <https://github.com/TheCuteOwl/Trap-Stealer/tree/main>
[2] <https://www.virustotal.com/gui/file/85a0342027420025c477f3f6ab68376aa1608a447d1fb24920ac36b7cf7fd59d/detection>
[3] <https://github.com/TheCuteOwl/Trap-Stealer/blob/main/obfuscator.py>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Python](/tag.html?tag=Python) [Infostealer](/tag.html?tag=Infostealer) [Obfuscation](/tag.html?tag=Obfuscation) [Tool](/tag.html?tag=Tool) [Malware](/tag.html?tag=Malware)

[0 comment(s)](/diary/From%2Ba%2BRegular%2BInfostealer%2Bto%2Bits%2BObfuscated%2BVersion/31484/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31480)
* [next](/diary/31486)

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

[Bluesky](https://bsky.app/profile/sa...