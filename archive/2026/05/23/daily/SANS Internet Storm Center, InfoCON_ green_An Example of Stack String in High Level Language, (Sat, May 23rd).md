---
title: An Example of Stack String in High Level Language, (Sat, May 23rd)
url: https://isc.sans.edu/diary/rss/33008
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-23
fetch_date: 2026-05-24T06:01:15.820363
---

# An Example of Stack String in High Level Language, (Sat, May 23rd)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33006)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

# [An Example of Stack String in High Level Language](/forums/diary/An%2BExample%2Bof%2BStack%2BString%2Bin%2BHigh%2BLevel%2BLanguage/33008/)

**Published**: 2026-05-23. **Last Updated**: 2026-05-23 05:49:17 UTC
**by** [Xavier Mertens](/handler_list.html#xavier-mertens) (Version: 1)

[0 comment(s)](/diary/An%2BExample%2Bof%2BStack%2BString%2Bin%2BHigh%2BLevel%2BLanguage/33008/#comments)

This week, I’m attending the SEC670[[1](https://www.sans.org/cyber-security-courses/red-team-operations-developing-custom-tools-windows)] training (“Red Teaming Tools - Developing Windows Implants, Shellcode, Command and Control”). From my point of view, this training fits perfectly with FOR610 or FOR710 (malware analysis) because it addresses malware from the opposite: Instead of performing reverse engineering, you write malicious code! Always interesting to have another point of view.

Many techniques used by threat actors are often discovered while reversing the malware code and are read in assembly. A perfect example are stack strings. This is a malware obfuscation technique where strings are constructed dynamically at runtime by assigning individual characters or bytes directly onto the stack, rather than storing them as contiguous string literals in the binary's static data sections. Read: they won’t be detected by simple tools like “strings” or “pestr”.

From an assembly code point of view, a stack string looks like this:

```

sub     esp, 16                 ; Reserve 16 bytes (padded to hold our string)
mov     byte [esp + 0], 0x73    ; 's'
mov     byte [esp + 1], 0x61    ; 'a'
mov     byte [esp + 2], 0x6E    ; 'n'
mov     byte [esp + 3], 0x73    ; 's'
mov     byte [esp + 4], 0x20    ; ' '
mov     byte [esp + 5], 0x69    ; 'i'
mov     byte [esp + 6], 0x73    ; 's'
mov     byte [esp + 7], 0x63    ; 'c'
mov     byte [esp + 8], 0x00    ; '\0' null terminator
mov     eax, 4                  ; sys_write
mov     ebx, 1                  ; fd = stdout
mov     ecx, esp                ; buf = stack string
mov     edx, 8                  ; len = 8
int     0x80
```

The string "sans isc" will be printed on the console.

But, how do you implement this in a high-level language like C? Here is an example:

```

#include <stdio.h>
#include <string.h>

void plainTextExample(void) {
    // Will be stored in .rodata and easy to spot with "strings" tools
    const char* url = "http://plain-malicious.com/";
    printf("Plain URL = %s\n", url);
}

void stackStringExample(void) {
    // Now we use a stack string. The script will be located in .text!
    char url[30];
    url[0] = 0x68;   // 'h'
    url[1] = 0x74;   // 't'
    url[2] = 0x74;   // 't'
    url[3] = 0x70;   // 'p'
    url[4] = 0x3A;   // ':'
    url[5] = 0x2F;   // '/'
    url[6] = 0x2F;   // '/'
    url[7] = 0x65;   // 'e'
    url[8] = 0x6E;   // 'n'
    url[9] = 0x63;   // 'c'
    url[10] = 0x6F;  // 'o'
    url[11] = 0x64;  // 'd'
    url[12] = 0x65;  // 'e'
    url[13] = 0x64;  // 'd'
    url[14] = 0x2D;  // '-'
    url[15] = 0x6D;  // 'm'
    url[16] = 0x61;  // 'a'
    url[17] = 0x6C;  // 'l'
    url[18] = 0x69;  // 'i'
    url[19] = 0x63;  // 'c'
    url[20] = 0x69;  // 'i'
    url[21] = 0x6F;  // 'o'
    url[22] = 0x75;  // 'u'
    url[23] = 0x73;  // 's'
    url[24] = 0x2E;  // '.'
    url[25] = 0x63;  // 'c'
    url[26] = 0x6F;  // 'o'
    url[27] = 0x6D;  // 'm'
    url[28] = 0x2F;  // '/'
    url[29] = 0x00;  // '\0'
    printf("Obfuscated URL = %s\n", url);
    memset(url, 0, sizeof(url));
}

int main(void) {
    plainTextExample();
    stackStringExample();
    return 0;
}
```

Because characters are hex-encoded, it makes them even more difficult to be spotted by the reverse engineer's eyes.

Once compiled, let’s disassemble it with Ghidra. As expected the first string is directly discovered:

![](https://isc.sans.edu/diaryimages/images/isc-20260523-1.png)

Now, let's try to find the second string. It's not directly available. The stack string is generated with the code below. Characters are moved one by one (0x68, 0x74, 0x74, ...):

![](https://isc.sans.edu/diaryimages/images/isc-20260523-2.png)

Of course, we are lazy people and we need tools and processes to spot such type of strings. We have tools to do this, like floss[[2](https://github.com/mandiant/flare-floss)]. But, to better understand how we can spot them, let's have a look at a "manual" technique. Because bytes are moved one by one on the stack, the ASM instruction used is "movb" or "mov BYTE PTR" (depending on the syntax convention, AT&T or Intel). Let's try to decode the strings with a simple shell:

```

$ objdump -D StackStrings.exe \
| grep -oP 'mov\s+BYTE PTR \[[^\]]+\],\s*0x\K[0-9a-fA-F]{1,2}' \
| while read hex
> do
> printf "\x${hex}"
> done
http://encoded-malicious.com/G
```

Magic! So /bin/bash can be considered as a reverse-engineering tool :-)

Happy reversing!

[1] <https://www.sans.org/cyber-security-courses/red-team-operations-developing-custom-tools-windows>
[2] <https://github.com/mandiant/flare-floss>

Xavier Mertens (@xme)
Xameco
Senior ISC Handler - Freelance Cyber Security Consultant
[PGP Key](https://keybase.io/xme/key.asc)

Keywords: [ASM](/tag.html?tag=ASM) [Assembly](/tag.html?tag=Assembly) [Bash](/tag.html?tag=Bash) [Malware](/tag.html?tag=Malware) [Obfuscation](/tag.html?tag=Obfuscation) [Reverse](/tag.html?tag=Reverse) [Stackstring](/tag.html?tag=Stackstring)

[0 comment(s)](/diary/An%2BExample%2Bof%2BStack%2BString%2Bin%2BHigh%2BLevel%2BLanguage/33008/#comments)

Click [HERE](https://www.sans.org/profiles/xavier-mertens) to learn more about classes Xavier is teaching for SANS

* [previous](/diary/33006)

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

© 2026 SANS™ Internet Storm Center
Developers: We have an [API](/api/) for you!   [![Creative Commons License](/images/cc.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

* [Link To Us](/linkback.html)
* [About Us](/about.html)
* [Handlers](/handler_list.html)
* [Privacy Policy](/privacy.html)