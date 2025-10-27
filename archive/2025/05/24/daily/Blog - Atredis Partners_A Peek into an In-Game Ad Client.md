---
title: A Peek into an In-Game Ad Client
url: https://www.atredis.com/blog/2025/5/19/in-game-ads
source: Blog - Atredis Partners
date: 2025-05-24
fetch_date: 2025-10-06T22:27:44.931447
---

# A Peek into an In-Game Ad Client

[0](/cart)

[Skip to Content](#page)

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

# A Peek into an In-Game Ad Client

May 23

Written By [Jordan Whitehead](/blog?author=607868e1c0c84d602cd982b5)

*This should be a quick one! No crazy bugs, just an interesting little target I hadn't seen anyone dig into, and a few helpful tricks for quick reverse engineering.*

A little bit ago I re-installed the racing game Trackmania, and I noticed I got product ads displayed at me in-game alongside the racetrack. Where were those coming from?

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/a584cf43-e3e4-4851-b293-8a1655e2efb0/image5.png)

*In-Game Ad in Trackmania*

A bit of digging revealed a DLL loaded into the game, `anzu.dll`. Finding the company’s site, [anzu.io](https://www.anzu.io/) helped to peel back the covers. These in-game ads were part of a complete ad-breakfast, including targeting, analytics, ad bidding, and more. Their site even claimed you could target ads [based on in-game metrics](https://www.anzu.io/blog/in-game-targeting-guide)). Their site also had many fun pictures of smiling people holding controllers in teal hoodies.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/5a3a7640-0bcb-4049-b441-02937e20dea7/image4.png)

*Happy Gamer at* [*anzu.io*](https://www.anzu.io/pc-console-game-developers)

Digging into the DLL I wanted to see how this library was being used. The DLL was stripped of symbol information, hiding function and variable names that would have made reverse engineering easier. The exceptions were the exported symbols, and there were quite a few exports. We could just start walking through in Binary Ninja or another decompiler, but having a concrete look at the way the game was using the library would make things go much quicker.

## Trampoline Tricks

I wanted to start with just tracking what `Anzu_` functions were called, and how. Which functions exported by the library even mattered? What did the arguments look like? To quickly gather call traces I generated a "trampoline" DLL that exported all of the same functions as the original, but each function would simply output to a log file before jumping into the original DLL.

To do this we couldn't just export a C function with the same name, like so:

```
int Anzu_CampaignMetricGet(...) {
    printf("Called Anzu_CampaignMetricGet\n");
    return real_Anzu_CampaignMetricGet();
}
```

This would not work as we didn't know how many arguments these calls took, or what types the arguments should have been. I solved this by generating a small assembly stub for each export that would:

1. Save the register state to the stack
2. Call the logging function with the export's name
3. Restore the register state
4. `jmp` to the original function

If you try this, just make sure you save the SIMD registers as well, or you will clobber your float arguments and end up sending a bunch of strange requests to the server. (Oops!)

```
EXTERN real_Anzu_CampaignMetricGet : QWORD

Anzu_CampaignMetricGet proc EXPORT
    //; save volatile registers
    push rax
    push rcx
    //;...snipped

    //; call log
    lea rcx, [Anzu_CampaignMetricGet_name]
    call log_proc

    //; restore
    //;...snipped
    pop rcx
    pop rax

    //; go to original
    jmp [real_Anzu_CampaignMetricGet]
Anzu_CampaignMetricGet ENDP

Anzu_CampaignMetricGet_name db "Anzu_CampaignMetricGet", 0
```

*Example Trampoline*

Our generated trampoline logic would now load the original DLL and save off pointers to all the original functions. Our exports were these small assembly stubs passing all the arguments on to the original functions. (I also double checked that all the exports seemed to be functions, exported data pointers would need some extra care.)

You can see my messy little code generator here in the repo [`gen_stubs.py`](https://github.com/atredis-jordan/anzu_peek/blob/main/gen_stubs.py). It outputs:

1. A declaration section to:
   * Export the trampoline stub with `__declspec`
   * Create a global to hold a pointer to the original function
2. Logic to grab the original function pointer using `GetProcAddress`
3. The assembly stub for each needed export

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/248eeb8e-14b3-4444-bccc-f2d59f6001b4/image8.png)

*Including Generated Stubs*

This all took only a few minutes and a python script to be able to gather some traces showing how Trackmania was using the Anzu library. (Thankfully Trackmania didn't do any sort of signature checks on the DLL, and would just load any DLL at the correct path.)

```
Interception DLL Loaded
Init complete
@ Anzu_GetVersionFloat
@ Anzu_InternalDebugging
@ Anzu_SetGDPRConsent
@ Anzu_InternalDebugging
@ Anzu_ApplicationActive
@ Anzu_InternalDebugging
@ Anzu_SetLogLevel
@ Anzu_RegisterLogCallback
@ Anzu_RegisterMessageCallback
@ Anzu_RegisterTextureUpdateCallback
@ Anzu_RegisterTextureInitCallback
@ Anzu_RegisterTextureImpressionCallback
@ Anzu_InternalDebugging
@ Anzu_InternalDebugging
@ Anzu_RegisterTexturePlaybackCompleteCallback
@ Anzu_InternalDebugging
@ Anzu_InternalDebugging
...snipped
```

*Initial Library Call Trace*

Of course, we could have done all this easily with a scriptable debugger like Frida, x64dbg, or WinDbg. A simple `.logopen` and pattern breakpoint (`bm anzu!* ".printf \"%y\\n\", @rip; gc"`) in WinDbg would get us a similar trace.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/553e27f5-974e-452c-bc78-6a4645791655/image7.png)

*Quick Library Trace in WinDbg*

If we could have accomplished all this in a debugger, why go through the trouble of building our own DLL? I chose the DLL route to give us a nice way to start iterating. Our initial traces showed us the functions we cared to start digging into. As we delved into those with our disassembler we started defining nicer stubs than our generic assembly trampolines. We started logging arguments and even changing functionality. Below is a stub that enabled more verbose logging in Anzu, even when the game asked for only error logging.

```
__declspec(dllexport) void Anzu_SetLogLevel(int32_t level) {

    fprintf(g_logf, "@ Anzu_SetLogLevel(%x) (forcing 0 and injecting debug setup)\n", level);
    real_Anzu_SetLogLevel(0);

    fprintf(g_logf, "DEBUG: Force registering log file:" LOG_NAME "\\n");
    real_Anzu_InternalDebugging(0xc0de5b05, LOG_NAME);
}
```

*Forcing Verbose Logging*

```
Interception DLL Loaded
Init complete
@ Anzu_GetVersionFloat
@ Anzu_InternalDebugging(c0de5b11, 0000000008000000) => 0000000000000000
@ Anzu_SetGDPRConsent
@ Anzu_InternalDebugging(c0de5b10, 00000165857AD171) => 0000000000000000
@ Anzu_ApplicationActive(d6eb0001)
@ Anzu_InternalDebugging(c0de5b03, 0000000000000001) => 0000000000000000
@ Anzu_SetLogLevel(4) (forcing 0 and injecting debug setup)
DEBUG: Force registering log file:log.log
@ Anzu_RegisterMessageCallback(00007FF783725A50, 0000000000000000) (redirecting)
DEBUG: Force registering net callback
@ Anzu_RegisterMessageCallback(00007FF61B645B70, 0000000000000000) (redirecting)
@ Anzu_Re...