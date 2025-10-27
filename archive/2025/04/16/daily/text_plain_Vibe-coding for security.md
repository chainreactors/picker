---
title: Vibe-coding for security
url: https://textslashplain.com/2025/04/15/vibe-coding-for-security/
source: text/plain
date: 2025-04-16
fetch_date: 2025-10-06T22:07:12.119828
---

# Vibe-coding for security

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Vibe-coding for security

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2025-04-152025-09-23](https://textslashplain.com/2025/04/15/vibe-coding-for-security/)Posted in[dev](https://textslashplain.com/category/dev/), [security](https://textslashplain.com/category/security/)Tags:[AI](https://textslashplain.com/tag/ai/), [InfoSecTTP](https://textslashplain.com/tag/infosecttp/), [security](https://textslashplain.com/tag/security/)

Recently, there’s been a surge in the popularity of [trojan clipboard](https://textslashplain.com/2024/06/04/attack-techniques-trojaned-clipboard/) attacks whereby the attacker convinces the user to carry their attack payload across a security boundary and compromise the device.

Meanwhile, AI hype is all the rage. I recent had a [bad experience](https://bsky.app/profile/ericlawrence.com/post/3lmf7zbc5ic2h) in what I thought was a simple AI task (draw a map with pushpins in certain cities):

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-31.png?w=406)](https://textslashplain.com/wp-content/uploads/2025/04/image-31.png)

The generated map with wildly incorrect city locations

… but I was curious to see what AI would say if I pretended to be the target of a trojan clipboard attack. I was pleased to discover that the two AIs I tried both gave solid security advice for situation:

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-28.png?w=1024)](https://textslashplain.com/wp-content/uploads/2025/04/image-28.png)

ChatGPT and Gemini both understood the attack and the risk

A few days later, the term “[vibe-coding](https://en.wikipedia.org/wiki/Vibe_coding)” crossed my feed and I groaned a bit when I learned what it means… Just describe what you want to the AI and it’ll build your app for you. *And yet.* That’s kinda exactly [how I make a living as a PM](https://textslashplain.com/2023/02/06/a-new-era-pm-swe/#:~:text=What%20Did%20PMs%20Do%2C%20Anyway): I describe what I want an app to do, and wait for someone else (ideally, our dev team) to build it. I skimmed a few articles about [vibe coding](https://www.techtarget.com/searchapparchitecture/opinion/My-first-attempt-at-vibe-coding) and then moved on with my day. I don’t have a lot of time to set up new workflows, install new devtools, subscribe to code-specific AI models, and so forth.

Back to the day job.

Talking to some security researchers looking into the current wave of trojan clipboard attacks, I brainstormed some possible mitigations. We could try to make input surfaces more clear about risk:

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-29.png?w=440)](https://textslashplain.com/wp-content/uploads/2025/04/image-29.png)

… but as I noted in my old [blog post](https://textslashplain.com/2024/06/04/attack-techniques-trojaned-clipboard/), we could be even smarter, detecting when the content of a paste came from a browser (akin to the “[Mark of the Web](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/)” on downloads) and provide the user with a context specific warning.

In fact, I realized, we don’t even need to change any of the apps. Years ago, I [updated SlickRun](https://bayden.com/SlickRun) to flash anytime the system clipboard’s content changes as a simple user-experience improvement. A simple security tool could do the same thing– watch for clipboard changes, see if the content came from the browser, and then warn the user if it was dangerous.

In the old days, I’d’ve probably spent an evening or two building such an app, but life is busier now, and my C++ skills are super rusty.

But… what if I vibe-coded it? Hmm. Would it work, or would it fail as spectacularly as it did on my map task?

### Vibe-coding ClipShield

I popped open [Google Gemini](https://gemini.google.com/) (Flash 2.0) and told directed it:

```
> Write me a trivial C++ app that calls AddClipboardFormatListener and on each WMClipboardUpdate call it scans the text on the clipboard for a string of my choice. If it's found, a MessageBox is shown and the clipboard text is cleared.
```

In about 15 seconds, it had emitted an entire C++ source file. I pasted it into Visual Studio and tried to compile it, expecting a huge pile of mistakes.

Sure enough, VS complained that there was no `WinMain` function. Gemini had named its function `main()`. I wonder if it could fix it itself?

```
> Please change the entry point from main to WinMain
```

The new code compiled and worked perfectly. Neat! I wonder how well it would do with making bigger changes to the code? Improvements occurred to me in rapid succession:

```
> To the WM_CLIPBOARDUPDATE code, please also check if the clipboard contains a format named "Chromium internal source URL".

> Update the code so instead of a single searchString we search for any of a set of strings.

> please make the string search case-insensitive

> When blocking, please also emit the clipboard string in the alert, and send it to the debug console via OutputDebugString
```

In each case, the resulting code was pretty much spot on, although I took the opportunity to tweak some blocks manually for improved performance. Importantly, however, I wasn’t wasting any time on the usual C++ annoyances, string manipulations and conversions, argument passing conventions, et cetera. I was just… *vibing*.

There was a compiler warning from Visual Studio in the log. I wonder if it could fix that? I just pasted the error in with no further instruction:

```
> Inconsistent annotation for 'WinMain': this instance has no annotations. See c:\program files (x86)\windows kits\10\include\10.0.26100.0\um\winbase.h(1060).
```

Gemini explained what the warning meant and exactly how to fix it. Hmm… What else?

```
> Is there a way to show the message box on a different thread so it does not block further progress?
```

Gemini refactored the code to show the alert in a different thread. Wait, is that even legal?

```
> In Windows API, is it legal to call MessageBox on another thread?
```

Gemini explained the principles around the UI thread and why showing a simple MessageBox was okay.

```
> Can you use a mutex to ensure single-instance behavior?
```

Done. I had to shift the code around a bit (I didn’t want errors to be fatal), but it was trivial.

Hmm…. What else. Ooh… What if I actually got real antivirus into the mix? I could call [AMSI](https://textslashplain.com/2024/10/25/defensive-technology-antimalware-scan-interface-amsi/) with the contents of the clipboard to let Defender or the system antivirus scan the content and give a verdict on whether it’s dangerous.

```
> Can you add code to call AMSI with the text from the clipboard?
```

It generated the code instantly. *Amazing*. Oops, it’s not quite right.

```
> clipboardText.c_str() is a char* but the AmsiScanString function needs an LPCWSTR
```

Gemini apologized for the error and fixed it. Hmm. Linking failed. This has always been a hassle. I wonder how Gemini will do?

```
> How do I fix the problem that the link step says "unresolved external symbol AmsiOpenSession"?
```

Gemini explained the cause of the problem and exactly how to fix it, including every click I needed to perform in Visual Studio. *Awesome!*

[![](https://textslashplain.com/wp-content/uploads/2025/04/image-35.png?w=511)](https://textslashplain.com/wp-content/uploads/2025/04/image-35.png)

By now, I was just having tons of fun, pair programming a combination of my knowledge with Gemini’s strengths.

```
> Please hoist a time_point named lastClipboardUpdate to a global variable and update it each time the clipboard contents change.

> Please rewrite GetTimestamp not to use auto

I like to know what my types actually are.

> Please monitor keystrokes for the Win+R hotkey and if pressed and it's within 30 seconds of the clipboard copy, show a warn...