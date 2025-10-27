---
title: Uncovering Windows Events
url: https://posts.specterops.io/uncovering-windows-events-b4b9db7eac54?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2023-03-16
fetch_date: 2025-10-04T09:46:10.287137
---

# Uncovering Windows Events

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fb4b9db7eac54&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fjonny-johnson.medium.com%2Funcovering-windows-events-b4b9db7eac54&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fjonny-johnson.medium.com%2Funcovering-windows-events-b4b9db7eac54&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Uncovering Windows Events

## Threat Intelligence ETW

[![Jonathan Johnson](https://miro.medium.com/v2/resize:fill:64:64/1*ro6iOomAZwYlmMgljL7EfA.png)](/?source=post_page---byline--b4b9db7eac54---------------------------------------)

[Jonathan Johnson](/?source=post_page---byline--b4b9db7eac54---------------------------------------)

6 min read

·

Mar 15, 2023

--

1

Listen

Share

Not all manifest-based Event Tracing for Windows (ETW) providers that are exposed through Windows are ingested into telemetry sensors/EDR’s. One provider commonly that is leveraged by vendors is the Threat-Intelligence ETW provider. Due to how often it is used, I wanted to map out how its events are being written within [TelemetrySource](https://github.com/jsecurity101/TelemetrySource).

This post will focus on the process I followed to understand the events the Threat-Intelligence ETW provider logs and how to uncover the underlying mechanisms. One can use a similar process when trying to reverse other manifest-based ETW providers. This post isn’t a deep dive into how ETW works, if you’d to read more on that I suggest the following posts:

* [Tampering with Windows Event Tracing: Background, Offense, and Defense](https://blog.palantir.com/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63)
* [Data Source Analysis and Dynamic Windows RE using WPP and TraceLogging](https://posts.specterops.io/data-source-analysis-and-dynamic-windows-re-using-wpp-and-tracelogging-e465f8b653f7)

## Threat-Intelligence Provider

The Threat-Intelligence (TI) provider is a manifest-based ETW provider that generates security-related events. The TI provider is unique in the sense that Microsoft seems to continuously update this to provide more information around operations that would take some extreme engineering to obtain (i.e. function hooking) in the kernel. We will take a look at this later when we look into how the TI provider logs operations around writing code to a process’s memory. As we can see below, the TI provider provides a lot of unique events:

The TI provider is also unique as you need to be running as a PPL process in order to log events. Not sure why Microsoft made the decision to prevent logging from non-PPL processes, but this isn’t much of an issue as it is the standard for vendors to run their service binaries as PPL now. This is why tools like [Sealighter-TI](https://github.com/pathtofile/SealighterTI) exist so that others can log events from this provider. You can also change the Protection Level of the EPROCESS structure within WinDbg too. If you want to learn more on PPL I highly suggest [Alex Ionescu’s](https://twitter.com/aionescu) series: [The Evolution of Protected Processes](https://www.crowdstrike.com/blog/evolution-protected-processes-part-1-pass-hash-mitigations-windows-81/#:~:text=Unlike%20the%20simple%20%E2%80%9CProtectedProcess%E2%80%9D%20bit%20in%20EPROCESS%20that,Bit%20%2B0x000%20Signer%20%3A%20Pos%204%2C%204%20Bits).

Let’s take a look at how one of these events are logged!

## WriteProcessMemory

### ETW Provider Registration

The TI provider logs events in the kernel, so to track down how events are tracked we will need to look at ntoskrnl.exe. We will use IDA to analyze code within ntoskrnl.exe.

Anytime a program wants to write to an ETW provider it has to call either [EtwRegister](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-etwregister) (kernel-mode) or [EventRegister](https://learn.microsoft.com/en-us/windows/win32/api/evntprov/nf-evntprov-eventregister) (user-mode). Because the TI provider emits event from the kernel, we will look for EtwRegister. Looking at the cross-references for EtwRegister then we come across a function EtwInitialize. This function registers many ETW providers seen below.

Press enter or click to view image in full size

![]()

Let’s break down EtwRegister’s function:

```
NTSTATUS EtwRegister(
  [in]           LPCGUID            ProviderId,
  [in, optional] PETWENABLECALLBACK EnableCallback,
  [in, optional] PVOID              CallbackContext,
  [out]          PREGHANDLE         RegHandle
);
```

The first value being passed in is a pointer to the ETW Provider GUID. We can see this by double clicking on ThreatIntProviderGuid and seeing the following value which aligns with the ETW TI GUID `f4e1897c-bb5d-5668-f1d8–040f4d8dd344`:

Press enter or click to view image in full size

![]()

We then have 2 other parameters that we will skip for now as they don’t hold a lot of relevance right now.

The 4th parameter is an output parameter that returns a handle to the registered ETW provider. This gets passed into functions like `EtwWrite` so that the function knows what provider to write to. We can double click on this registration handle then cross-reference it within the code to see who calls it. Any function we see that calls it, outside of this one, is most likely writing an event to the TI provider:

Press enter or click to view image in full size

![]()

Because we are taking a look at operations related to writing to a process's memory the Function EtwTiLogReadWriteVm looks interesting. This call eventually makes a call to `EtwWrite`.

The following is how Microsoft defines `EtwWrite`:

```
NTSTATUS EtwWrite(
  [in]           REGHANDLE              RegHandle,
  [in]           PCEVENT_DESCRIPTOR     EventDescriptor,
  [in, optional] LPCGUID                ActivityId,
  [in]           ULONG                  UserDataCount,
  [in, optional] PEVENT_DATA_DESCRIPTOR UserData
);
```

The first parameter is our registration handle which we got from `EtwRegister`.

The second parameter is a pointer to the `[EventDescriptor](https://learn.microsoft.com/en-us/windows/win32/api/evntprov/ns-evntprov-event_descriptor)`, which is defined below:

```
typedef struct _EVENT_DESCRIPTOR {
  USHORT    Id;
  UCHAR     Version;
  UCHAR     Channel;
  UCHAR     Level;
  UCHAR     Opcode;
  USHORT    Task;
  ULONGLONG Keyword;
} EVENT_DESCRIPTOR, *PEVENT_DESCRIPTOR;
```

We can see the different members of this structure, one being the EventId (seen as Id) of the event. Within our code we can see EtwWrite called like the following:

```
result = (struct _KTHREAD *)EtwWrite(
    (PREGHANDLE)EtwThreatIntProvRegHandle,
    (PCEVENT_DESCRIPTOR)v15,
    0i64,
    v28 + v29,
    &UserData);
```

The second parameter is what we want to follow back to get the proper eventId being passed to EtwWrite. If we follow v15 backwards we will come to the following:

Press enter or click to view image in full size

![]()

This code block is saying — if EtwProviderEnabled (registered and enabled to be logged), move on. Then we see another IF statement saying...