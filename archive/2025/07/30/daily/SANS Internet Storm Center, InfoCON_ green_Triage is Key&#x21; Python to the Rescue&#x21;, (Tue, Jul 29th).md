---
title: Triage is Key&#x21; Python to the Rescue&#x21;, (Tue, Jul 29th)
url: https://isc.sans.edu/diary/rss/32152
source: SANS Internet Storm Center, InfoCON: green
date: 2025-07-30
fetch_date: 2025-10-06T23:55:57.333707
---

# Triage is Key&#x21; Python to the Rescue&#x21;, (Tue, Jul 29th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32148)
* [next](/diary/32154)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

# [Triage is Key! Python to the Rescue!](/forums/diary/Triage%2Bis%2BKey%2BPython%2Bto%2Bthe%2BRescue/32152/)

**Published**: 2025-07-29. **Last Updated**: 2025-07-29 09:29:53 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/Triage%2Bis%2BKey%2BPython%2Bto%2Bthe%2BRescue/32152/#comments)

When you need to quickly analyze a lot of data, there is one critical step to perform: Triage. In forensic investigations, this step is critical because it allows investigators to quickly identify, prioritize, and isolate the most relevant or high value evidence from large volumes of data, ensuring that limited time and resources are focused on artifacts most likely to reveal key facts about an incident. Sometimes, a quick script will be enough to speed up this task.

Today, I'm working on a case where I have a directory containing +20.000 mixed files. Amongst them, a lot of ZIP archives (mainly Office documents), containing also lot of files. The idea is to scan all those files (including the ZIP archives) for some keywords. I wrote a quick Python script that will scan all files against the embedded YARA rule and, if a match is found, copy the original file into a destination directory.

Here is the script:

```

#
# Quick Python triage script
# Copy files matching a YARA rule to another directory
#
import yara
import os
import shutil
import zipfile
import io

# YARA rule
yara_rule = """
rule case_xxxxxx_search_1
{
    strings:
        $s1 = "string1" nocase wide ascii
        $s2 = "string2" nocase wide ascii
        $s3 = "string3" nocase wide ascii
        $s4 = "string4" nocase wide ascii
        $s5 = "string5" nocase wide ascii
    condition:
        any of ($s*)
}
"""

source_dir = "Triage"
dest_dir = "MatchedFiles"
os.makedirs(dest_dir, exist_ok=True)
rules = yara.compile(source=yara_rule)

def is_zip_file(filepath):
    """
    Check ZIP archive magic bytes.
    """
    try:
        with open(filepath, "rb") as f:
            sig = f.read(4)
            return sig in (b"PK\x03\x04", b"PK\x05\x06", b"PK\x07\x08")
    except Exception:
        return False

def safe_extract_path(member_name):
    """
    Returns a safe relative path inside the destination folder (Prevent .. in paths).
    """
    return os.path.normpath(member_name).replace("..", "_")

def scan_file(filepath, file_bytes=None, inside_zip=False, zip_name=None, member_name=None):
    """
    Scan a file with YARA.
    """
    try:
        if file_bytes is not None:
            matches = rules.match(data=file_bytes)
        else:
            matches = rules.match(filepath)

        if matches:
            if inside_zip:
                print("[MATCH] {member_name} (inside {zip_name})")
                rel_path = os.path.relpath(zip_name, source_dir)
                filepath = os.path.join(source_dir, rel_path)
                dest_path = os.path.join(dest_dir, rel_path)
            else:
                print("[MATCH] {filepath}")
                rel_path = os.path.relpath(filepath, source_dir)
                dest_path = os.path.join(dest_dir, rel_path)

            # Save a copy
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.copy2(filepath, dest_path)
    except Exception as e:
        print(e)
        pass

# Main
for root, dirs, files in os.walk(source_dir):
    for name in files:
        filepath = os.path.join(root, name)
        if is_zip_file(filepath):
            try:
                with zipfile.ZipFile(filepath, 'r') as z:
                    for member in z.namelist():
                        if member.endswith("/"):  # Skip directories
                            continue
                        try:
                            file_data = z.read(member)
                            scan_file(member, file_bytes=file_data, inside_zip=True, zip_name=filepath, member_name=member)
                        except Exception:
                            pass
            except zipfile.BadZipFile:
                pass
        else:
            scan_file(filepath)
```

Now, you can enjoy some coffee while the script does the job:

```

[MATCH] docProps/app.xml (inside Triage\xxxxxxx.xlsx)
[MATCH] xl/sharedStrings.xml (inside Triage\xxxxx.xlsx)
[MATCH] xl/sharedStrings.xml (inside Triage\xxxxxxxxxxxxxxxxxxxx.xlsx)
[MATCH] ppt/slides/slide3.xml (inside Triage\xxxxxxxxxxxxxxxxxxxxxx.pptx)
[MATCH] ppt/slides/slide12.xml (inside Triage\xxxxxxxxxxxxxxxxxxxxxx.pptx)
[MATCH] ppt/slides/slide14.xml (inside Triage\xxxxxxxxxxxxxxxxxxxxxx.pptx)
[MATCH] ppt/slides/slide15.xml (inside Triage\xxxxxxxxxxxxxxxxxxxxxx.pptx)
[MATCH] xl/sharedStrings.xml (inside Triage\xxxxxxxx.xlsx)
[MATCH] Triage\xxxxxxxxxxxxxxxxxxxxxxx.pdf
[MATCH] Triage\xxxxxxxxxxxxxxxxxxx.xls
[MATCH] xl/sharedStrings.xml (inside Triage\xxxxxxxxxxxxxxxx.xlsx)
[MATCH] Triage\xxxxxxxxxxxxxxxxxxxxxxxxxx.xls
```

You can see that, with a few lines of Python, you can speedup the triage phase in your investigations. Note that the script is written to handle my current files set and is not ready for broader use (lile to handle password-protected archives or other types of archives)

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [DFIR](/tag.html?tag=DFIR) [Forensic](/tag.html?tag=Forensic) [Investigation](/tag.html?tag=Investigation) [Python](/tag.html?tag=Python) [Script](/tag.html?tag=Script) [Triage](/tag.html?tag=Triage)

[0 comment(s)](/diary/Triage%2Bis%2BKey%2BPython%2Bto%2Bthe%2BRescue/32152/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Reverse-Engineering Malware: Advanced Code Analysis](https://www.sans.org/event/live-online-europe-october-2025/course/reverse-engineering-malware-advanced-code-analysis) | Online | Greenwich Mean Time | Oct 27th - Oct 31st 2025 |

* [previous](/diary/32148)
* [next](/diary/32154)

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

* [Link To Us](/lin...