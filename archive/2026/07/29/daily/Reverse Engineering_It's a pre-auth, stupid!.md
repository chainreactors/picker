---
title: It's a pre-auth, stupid!
url: https://reverse.put.as/2026/07/29/its-a-pre-auth-stupid/
source: Reverse Engineering
date: 2026-07-29
fetch_date: 2026-07-30T04:51:07.894516
---

# It's a pre-auth, stupid!

[![](https://reverse.put.as/images/logo.png)](https://reverse.put.as/ "  (Alt + H)")

* [Home](https://reverse.put.as/ "Home")
* [About](https://reverse.put.as/about/ "About")
* [Archives](https://reverse.put.as/archives/ "Archives")
* [Crackmes](https://reverse.put.as/crackmes/ "Crackmes")
* [Patches](https://reverse.put.as/patches/ "Patches")
* [Tags](https://reverse.put.as/tags/ "Tags")
* [Papers](https://papers.put.as "Papers")

# It's a pre-auth, stupid!

July 29, 2026 Â· 4 min Â· 789 words Â· fG!

This Monday Apple’s Security Bulletin finally brought the bad news I had been waiting for a long time (because I’m a very curious person and like to experiment!).

There was a section on Screen Sharing and while the descriptions looked suspicious there was a chance that one of the greatest bugs I ever found was finally killed.

After updating a VM and testing the bug, it was indeed not working anymore. Saddeness attacked me and so I went to bed. Well, I couldn’t sleep without knowing why, so I came back, loaded IDA, and check what was going on. Yes, a new check was introduced at the right place that killed the bug. Ok, that lets me sleep in some peace!

Next day I better check things, and I still suspect there might be a way to still exploit this. Apple is famous for fucked up patches so why not? But I have other work to do and I’m still “sad” about losing this bug.

Today, I see a blogpost describing a root remote command execution in screensharingd. Ok, these might be the clowns that went crying to Apple about a bug they found. Reading the blogpost and it’s quite clear that they don’t really understand the bug and its full potential.

Maybe the reason is this:

> That is also why this was an interesting automated-discovery result.
> The bug was found through our automated vulnerability-discovery workflow using GPT-5.5 for discovery and validation.

Yeah, the machines found a bug, they are happy with it and can go cry Apple and write a blogpost for kudos.

Turns out they are wrong about it. The real bug is a pre-auth on screensharingd and it allows to pwn any Mac that has Screen Sharing enabled, without knowing password or anything else. You just need to have an IP address :-).

As a friend says, I should have sold it (well if this was a default enabled service I would for sure). Turns out I’m not in the business of selling bugs. Yeah, I’m still an idiot regarding this topic. Oh well, bugs are plenty everywhere, the good ones are still out there.

Anyway, you can find a Go based ARM64 PoC that allows you to download any file from a vulnerable macOS machine. This is a weaker PoC that might fail, but you can keep trying until it works. You wouldn’t expect me to release an insanely stable bug for free, did you?

You need to know the full path to the file you want to download. An easy example is `/etc/sudoers` or any other known file. If you use your brain you can easily find the username list and now you can do better things. Oh, this bug doesn’t care about TCC either!

It’s obfuscated but doesn’t contain any malicious code. You can take my word and reputation for it. You wouldn’t expect me to release source code for free, did you?

And of course I’m not going to explain the bug, you wouldn’t expect me to train the stupid LLMs for free, did you? Fuck those leeches :-).

It would be a very nice long blogpost but I can’t get myself to do it in times where everyone is bragging on top of someone’s else knowledge encoded in models. Very sad times indeed, but life goes on and knowledge goes underground once again.

LLMs are useful, but it will rotten your brain and skills very fast. Use them when useful, but keep practicing your skills and using your brain. Don’t worry that everyone is bragging how productive they are and all the bugs they are finding. Turns out they are finding all the same bugs if you look carefully at the latest Apple Security Bulletin. Btw, I wasn’t even trying to find bugs, I was just trying to understand something and hit it LOLOLOLOLOL.

Do you even understand how insanely amazing this bug was? Nah… It would be perfect if it could bypass SIP. That one it doesn’t do. But I’m not even describing all its features!

Oh, and Apple should rethink its bug fixing policy. This is a massive bug and most probably there are tons of old systems exposed on the internet (and your LANs), that will be left unpatched because the 5 trillion USD company can’t bother allocating resources.

Keep hacking and having fun,
fG!

[navi\_the\_clown](files/navi_the_clown)
SHA256(navi\_the\_clown)= 0bddb0442a873f7a241d06905152be37ee3f532b72b79e1dcd3b23308a98a3ed

Usage:

```
./navi_the_clown -t hostname:5900 -f /etc/sudoers
```

**P.S.:** The binary has no code signature, so you need to resign it after downloading with `codesign -s - -f navi_the_clown`. And probably remove the quarantine bit.

**P.S.2:** The name rang a bell but it wasn’t connecting in the brain until I went search. Ex-Hacking Team the other guy. Touche’. Serendipity is fun :P

[Next Â»
This blog is 18th years old already!](https://reverse.put.as/2025/10/18/18yearsold/)

Â© 2025 fG!
Powered by
[Hugo](https://gohugo.io/) &
[PaperMod](https://github.com/adityatelange/hugo-PaperMod/)