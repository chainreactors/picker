---
title: Yet Another Random Story: VBScript's Randomize Internals
url: https://blog.doyensec.com/2025/09/25/yet-another-random-story.html
source: Over Security - Cybersecurity news aggregator
date: 2025-09-26
fetch_date: 2025-10-02T20:43:41.399872
---

# Yet Another Random Story: VBScript's Randomize Internals

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# Yet Another Random Story: VBScript's Randomize Internals

25 Sep 2025 - Posted by Adrian Denkiewicz

In one of our [recent posts](https://blog.doyensec.com/2025/08/19/trivial-exploit-on-C-random.html), Dennis shared an interesting case study of C# exploitation that rode on `Random`-based password-reset tokens. He demonstrated how to use the single-packet attack, or a bit of old-school math, to beat the game. Recently, I performed a security test on a target which had a dependency written in VBScript. This blog post focuses on VBSâs `Rnd` and shows that the situation there is even worse.

![VBScript Dice Rolling](../../../public/images/dice_rolling.png)

## Target Application

The application was responsible for generating a secret token. The token was supposed to be unpredictable and expected to remain secret. Hereâs a rough copy of the token generation code:

```
Dim chars, n
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()*&^%$#@!"
n = 32

function GenerateToken(chars, n)
	Dim result, pos, i, charsLength
	charsLength = Int(Len(chars))

	For i = 1 To n
		Randomize
		pos = Int((Rnd * charsLength) + 1)
		result = result & Mid(chars, pos, 1)
	Next

	GenerateToken = result
end function
```

The first thing I noticed was that the `Randomize` function was called inside a loop. That should reseed the PRNG on every single iteration, right? That could result in repeated values. Well, contrary to many other programming languages, in VBScript, the `Randomize` usage within a loop is not a problem per se. The function will not reset the initial state if the same seed is passed again (even if implicitly). This prevents generating identical sequences of characters within a single `GenerateToken` call. If you actually want that behavior, call `Rnd`Â with a [negative argument](https://www.vbsedit.com/html/ac1ef1bb-f1d8-4369-af7f-ddd89c926250.asp) immediately before calling `Randomize`Â with a numeric argument.

But if that isnât an issue, then what is?

## How VBSâs `Randomize` Works in Practice

Hereâs a short API breakdown:

```
Randomize     ' seed the global PRNG using the system clock
Randomize s   ' seed the global PRNG using a specified seed value
r = Rnd()     ' next float in [0,1)
```

If no seed is explicitly specified, `Randomize` uses [`Timer`](https://www.vbsedit.com/html/700b6bc7-b482-4e3f-a20a-894fb5f0e970.asp) to set it (not entirely true, but we will get there). `Timer()` returns seconds since midnight as a `Single` value. ï¿¼`Rnd()` advances a global PRNG state and is fully deterministic for a given seed. Same seed, same sequence, like in other programming languages.

There are some problematic parts here, though. Windowsâ default system clock tick is about 15.625 ms, i.e., 64 ticks per second. In other words, we get a new implicit seed value only once every 15.625 milliseconds.

Because the returned value is of type `Single`, we also get precision loss compared to a `Double` type. In fact, multiple âseedsâ round to the same internal value. Think of collisions happening internally. As a result, there are way fewer unique sequences possible than you might think!

**In practice there are at most 65,536 distinct effective seedings (details below). Because `Timer()` resets at midnight, the same set recurs each day.**

We ran a local copy of the clientâs code to generate unique tokens. During almost 10,000 runs, we managed to generate only 400 unique values. The remaining tokens were duplicates. As time passed, the duplicate ratio increased.

Of course the real goal here would be to recover the original secret. We can achieve that if we know the time of day when the `GenerateToken` function started. The more precise the value, the less computations required. However, even if we have only a rough idea, like âminutes after midnightâ, we can start at 00:00 and slowly increase our seed value by 15.625 milliseconds.

## The PoC

We started by double-checking our strategy. We modified the initial code to use a command-line provided seed value. Note, the same seed is used multiple times. While in the original code, it is possible that seed value changes between the loop iterations, in practice that doesnât happen often. We could expand our PoC to handle such scenarios as well, but we wanted to keep the code as clean as possible for the readability.

```
Option Explicit

If WScript.Arguments.Count < 1 Then
	WScript.Echo "VBS_Error: Requires 1 seed argument."
	WScript.Quit(1)
End If

Dim seedToTest
seedToTest = WScript.Arguments(0)
WScript.Echo "Seed: " & seedToTest

Dim chars, n
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()*&^%$#@!"
n = 32

WScript.Echo "Predicted token: " & GenerateToken(chars, n, seedToTest)

function GenerateToken(chars, n, seed)
	Dim result, pos, i, charsLength
	charsLength = Int(Len(chars))

	For i = 1 To n
		Randomize seed
		pos = Int((Rnd * charsLength) + 1)
		result = result & Mid(chars, pos, 1)
	Next

	GenerateToken = result
end function
```

We took a precise `Timer()` value from another piece of code and used it as an input seed. Strangely though, it wasnât working. For some reason we were ending up with a completely different PRNG state. It took a while before we understood that `Randomize` and `Randomize Timer()` arenât exactly the same things.

VBScript was introduced by Microsoft in the mid-1990s as a lightweight, interpreted subset of Visual Basic. As of Windows 11 version 24H2, VBScript is a Feature on Demand (FOD). That means it is installed by default for now, but Microsoft [plans to disable it in future versions and ultimately remove it](https://techcommunity.microsoft.com/blog/windows-itpro-blog/vbscript-deprecation-timelines-and-next-steps/4148301). Still, the method of interest is implemented within the `vbscript.dll` library and we can take a look at `vbscript!VbsRandomize`:

```
; edi = argc
vbscript!VbsRandomize+0x50:
00007ffc`12d076a0 85ff            test    edi,edi            ; is argc == 0 ?
00007ffc`12d076a2 755b            jne     vbscript!VbsRandomize+0xaf ; if not zero, goto Randomize <seed> path

; otherwise, seed taken from current time
00007ffc`12d076a4 488d4c2420      lea     rcx,[rsp+20h]
00007ffc`12d076a9 48ff15...       call    GetLocalTime

; build "seconds" = hh*3600 + mm*60 + ss
00007ffc`12d076b5 0fb7442428      movzx   eax,word ptr [rsp+28h]
00007ffc`12d076ba 6bc83c          imul    ecx,eax,3Ch
00007ffc`12d076bd 0fb744242a      movzx   eax,word ptr [rsp+2Ah]
00007ffc`12d076c2 03c8            add     ecx,eax
00007ffc`12d076c4 0fb744242c      movzx   eax,word ptr [rsp+2Ch]
00007ffc`12d076c9 6bd13c          imul    edx,ecx,3Ch
00007ffc`12d076cc 03d0            add     edx,eax

; convert milliseconds to double, divide by 1000.0
00007ffc`12d076ce 0fb744242e      movzx   eax,word ptr [rsp+2Eh]
00007ffc`12d076d3 660f6ec0        movd    xmm0,eax
00007ffc`12d076d7 f30fe6c0        cvtdq2pd xmm0,xmm0
00007ffc`12d076db 660f6eca        movd    xmm1,edx
00007ffc`12d076df f20f5e0599...   divsd   xmm0,[vbscript!_real]
00007ffc`12d076e7 f30fe6c9        cvtdq2pd xmm1,xmm1
00007ffc`12d076eb f20f58c8        addsd   xmm1,xmm0

; narrow down
00007ffc`12d076ef 660f5ac1        cvtpd2ps xmm0,xmm1         ; double -> float conversion
00007ffc`12d076f3 f30f11442420    movss   [rsp+20h],xmm0     ; spill float
00007ffc`12d076f9 8b4c2420        mov     ecx,[rsp+20h]      ; load as int bits

; ecx now hold...