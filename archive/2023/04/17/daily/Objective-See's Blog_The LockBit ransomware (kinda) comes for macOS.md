---
title: The LockBit ransomware (kinda) comes for macOS
url: https://objective-see.org/blog/blog_0x75.html
source: Objective-See's Blog
date: 2023-04-17
fetch_date: 2025-10-04T11:31:33.790570
---

# The LockBit ransomware (kinda) comes for macOS

* [![](/images/logoApple.png)

  Objective-See

  a non-profit 501(c)(3) foundation.](/index.html)
* [ ]

  + [![](/images/aboutIcon.png)
    About](/about.html)
  + [![](/images/conferenceIcon.png)
    #OBTS](https://objectivebythesea.org/)
  + [![](/images/bookIcon.png)
    Book Series](https://taomm.org/)
  + [![](/images/weIcon.png)
    Objective-We](/we.html)
  + [![](/images/storeIcon.png)
    Our Store/Swag](https://objective-see.myshopify.com/)
  + [![](/images/malwareIcon.png)
    Malware Collection](/malware.html)
* Support Us!
* [![](/images/blogIcon.png)](/blog.html)
* [![](/images/productsIcon.png)

  tools](/tools.html)

---

The LockBit ransomware (kinda) comes for macOS

Analyzing an arm64 mach-O version of LockBit

by: Patrick Wardle / April 16, 2023

Objective-See's research, tools, and writing, are supported by the "Friends of Objective-See" such as:

[![](/images/friends/textless/jamf.png)

Jamf](https://www.jamf.com/?utm_source=objective-see&utm_medium=sponsored-link&utm_campaign=next-gen-security&utm_content=2021-02-05_protect)

[![](/images/friends/textless/mosyle.png)

Mosyle](https://l.linklyhq.com/l/18wF2)

[![](/images/friends/textless/kandji.png)

Kandji](https://www.kandji.io)

[![](/images/friends/textless/cmm.png)

CleanMyMac X](https://macpaw.com/cleanmymac)

[![](/images/friends/textless/kolide.png)

Kolide](https://l.kolide.co/Objective-See)

[![](/images/friends/textless/panw.png)

Palo Alto Networks](https://www.paloaltonetworks.com)

[![](/images/friends/textless/sophos.png)

Sophos](https://www.sophos.com)

📝 👾 Want to play along?

As “Sharing is Caring” I’ve uploaded the malicious binary [LockBit](https://github.com/objective-see/Malware/raw/main/LockBit.zip) to our public macOS malware collection. The password is: infect3d

...please though, don't infect yourself!

### Background

Late Saturday (April 15the), [@MalwareHunterTeam](https://twitter.com/malwrhunterteam/) tweeted about a new LockBit ransomware variant targeting macOS:

> "locker\_Apple\_M1\_64": 3e4bbd21756ae30c24ff7d6942656be024139f8180b7bddd4e5c62a9dfbd8c79
> As much as I can tell, this is the first Apple's Mac devices targeting build of LockBit ransomware sample seen...
> Also is this a first for the "big name" gangs?
> 🤔[@patrickwardle](https://twitter.com/patrickwardle?ref_src=twsrc%5Etfw)
> cc [@cyb3rops](https://twitter.com/cyb3rops?ref_src=twsrc%5Etfw) [pic.twitter.com/SMuN3Rmodl](https://t.co/SMuN3Rmodl)
>
> — MalwareHunterTeam (@malwrhunterteam) [April 15, 2023](https://twitter.com/malwrhunterteam/status/1647384505550876675?ref_src=twsrc%5Etfw)

As shown in the tweet, the ransomware binary initially was undetected by any of the anti-virus engines on VirusTotal:

![](../images/blog/blog_0x75/VT.jpeg)
locker\_Apple\_M1\_64 on VirusTotal (image credit: @MalwareHunterTeam)

Good news, if you refresh the [page on VirusTotal](https://www.virustotal.com/gui/file/3e4bbd21756ae30c24ff7d6942656be024139f8180b7bddd4e5c62a9dfbd8c79/detection) the AV engines are now starting to pick up the file as malicious.

Shortly after [@MalwareHunterTeam](https://twitter.com/malwrhunterteam/)’s tweet, the fine folks of [@vxunderground](https://twitter.com/vxunderground/status/1647424861810065410) added their thoughts and shared samples:

> Lockbit ransomware group has created their first MacOS-based payload. We believe this is the first time a large ransomware threat group has developed a payload for Apple products.
>
> We have samples.
>
> Intel via [@malwrhunterteam](https://twitter.com/malwrhunterteam?ref_src=twsrc%5Etfw) & [@BrettCallow](https://twitter.com/BrettCallow?ref_src=twsrc%5Etfw)
>
> Download: <https://t.co/bMGJXWYvc3> [pic.twitter.com/My9ZtAHCcq](https://t.co/My9ZtAHCcq)
>
> — vx-underground (@vxunderground) [April 16, 2023](https://twitter.com/vxunderground/status/1647424861810065410?ref_src=twsrc%5Etfw)

The relevance of this macOS specimen is well articulated in their tweet:

> “Lockbit ransomware group has created their first MacOS-based payload. We believe this is the first time a large ransomware threat group has developed a payload for Apple products.” vx-underground

Interested in learning more about the LockBit Ransomware Group? Read:

["The Unrelenting Menace of the LockBit Ransomware Gang"](https://www.wired.com/story/lockbit-ransomware-attacks/) (Wired/Lily Hay Newman).

Ok, so even though it’s the weekend, we have what appears to be a new macOS malware specimen from one of the more notorious ransomware gangs! Coupled with the fact that this may be, (as noted by @VXUnderground), “*the first time a large ransomware threat group has developed a payload for Apple products*” …I was intrigued to decided to dig right in!

In this blog post we’ll tear apart the sample, showing that ultimately, while yes it can indeed run on Apple Silicon, that is basically the extent of it’s impact. Thus macOS users have nothing to worry about …for now!

### Triage

The (SHA-1) hash for the binary (aptly named `locker_Apple_M1_64`) is `2D15286D25F0E0938823DCD742BC928E78199B3D`

While we're only focusing on the macOS sample, it appears the LockBit group has compiled this sample for a host of other OS's:

![](../images/blog/blog_0x75/samples.png)

Using macOS’s `file` utility, we see the `locker_Apple_M1_64` binary is a 64-bit arm64 Mach-O:

```
% file LockBit/locker_Apple_M1_64
LockBit/locker_Apple_M1_64: Mach-O 64-bit executable arm64
```

And what about it’s code signing information? Let’s take a peek via macOS’s `codesign` and `spctl` utilities:

```
% codesign -dvv LockBit/locker_Apple_M1_64
Executable=LockBit/locker_Apple_M1_64
Identifier=locker
Format=Mach-O thin (arm64)
CodeDirectory v=20400 size=3295 flags=0x20002(adhoc,linker-signed) hashes=100+0 location=embedded
Signature=adhoc
Info.plist=not bound
TeamIdentifier=not set
Sealed Resources=none
Internal requirements=none

% spctl -a -vvv -t install LockBit/locker_Apple_M1_64
LockBit/locker_Apple_M1_64: invalid signature (code or signature have been modified)
```

The `codesign` utility shows that though it’s signed, it’s signed “ad-hoc” (say vs. an Apple Developer ID). This means if downloaded to a macOS system (i.e. deployed by the attackers) macOS won’t let it run. This is confirmed by the `spctl` utility which shows “invalid signature” …or if you’re brave enough to try run it:

![](../images/blog/blog_0x75/blocked.png)
An invalid signature means macOS will block it

Let’s now run the `strings` command (with the `"-"` option which instructs it to scan the whole file), we find a few strings that appear to be related to standard ransomware activity including:

* Encryption
* File Extensions
* A file path, perhaps containing ransom instructions

```
% strings - -n 3 locker_Apple_M1_64

curve25519xsalsa20poly1305
blake2b
blake2b_final
blake2b-ref.c
sodium_crit_enter
_sodium_malloc
/dev/urandom
/dev/random

...
cmd
ani
adv
msi
msp
com
nls
ocx
mpa
cpl
mod
hta
prf
rtp
rdp
bin
shs
wpx
bat
rom
msc
spl
ics
key
exe
dll
...

restore-my-files.txt
...

winmd
ntldr
ntuser.dat.log
bootsect.bak
autorun.inf
thumbs.db
iconcache.db
```

Also interesting are the strings related to Windows artifacts (e.g. `autorun.inf`, `ntuser.dat.log`, etc…). This may indicate the ransomware was originally written to target Windows platforms.

This wraps up our triage of the `locker_Apple_M1_64` binary. Time to dive in deeper with our trusty friends: the disassembler and debugger!

### Analysis of `locker_Apple_M1_64`

In this section we’ll more deeply analyze the malicious logic of the `locker_Apple_M1_64` binary …which is simplified by the fact that the binary’s symbols aren’t stripped. (So function and method names are left intact ….yay!)

First, we pointed out that the `locker_Apple_M1_64` is an arm64 binary (`Mach-O 64-bit executable arm64`). This means we better have at least a cursory understanding of AArch64. If you’re not familiar with this instruction set, here’s two of my favorite resources to get you up to speed:

* [“Arm’d ...