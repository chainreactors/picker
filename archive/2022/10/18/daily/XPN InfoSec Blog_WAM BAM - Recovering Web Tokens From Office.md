---
title: WAM BAM - Recovering Web Tokens From Office
url: https://blog.xpnsec.com/wam-bam/
source: XPN InfoSec Blog
date: 2022-10-18
fetch_date: 2025-10-03T20:06:28.890797
---

# WAM BAM - Recovering Web Tokens From Office

[![avatar](/images/profile-image.jpg)](https://blog.xpnsec.com)
[XPN's InfoSec Blog](https://blog.xpnsec.com)

Adam Chester

Hacker and Infosec Researcher

## [XPN InfoSec Blog](https://blog.xpnsec.com "XPN InfoSec Blog")

[« Back to home](https://blog.xpnsec.com "Back to homepage")

# [WAM BAM - Recovering Web Tokens From Office](/wam-bam/)

Posted on

2022-10-17
Tagged in
[windows](/tags#windows), [low-level](/tags#low-level), [azure](/tags#azure)

This weekend I wanted to take a look at something that had been bugging me. Over the last few weeks, a trend of pulling Azure JWT’s from memory has appeared, mostly due to a nice blog post by [mr.d0x](https://mrd0x.com/stealing-tokens-from-office-applications/) showing how dumping memory from Microsoft Office allows Red Teamer’s to recover authentication tokens for Azure and M365 services.

The question that has been on my mind however, was how are these tokens reloaded into Office each time it starts? After all, we obviously aren’t re-authenticating every time we open Word, so they have to be persisted somewhere right?

In this post I’ll go through two areas that I identified while reversing the authentication mechanism of Office, and provide some POC tools to help recover stored tokens without memory scraping.

Before reading on, I would like to caveat that the details shown in this post do not constitute a “security issue”, in a similar way that stealing cookies from a users workstation isn’t a vulnerability. This is very much Office, Windows and Web API’s working as they are intended. This post is more to satisfy my own curiosity about how some of this stuff works so I can craft some tools, and get some sleep without thinking about JWT’s! With that said, onto the fun bit.

## Microsoft Account Service

I must admit, when I first started looking at this, scraping the memory of my running Word process didn’t result in the documented signature `eyJ0eX` being found.

This is the primary method current tools are using to identify active tokens, and I utilise a Microsoft 365 account (product name correct at the time of posting) with my Windows login.. so what gives?

Well it turns out that Microsoft Account’s (MSA) authentication tokens are handled in a different way to the usual Azure AD SSO accounts. So for all of you who have been running the latest Red Team minidump war3z and not having much success.. this should hopefully answer some questions.

Let’s start with looking at MSA authenticated Office sessions. Firing up Microsoft Office (now with symbols, thank you very much Microsoft!) and look at the loaded DLL’s. One thing that stood out was `MicrosoftAccountWAMExtension.dll`.

Loading this DLL into Ghidra, we can start hunting for what is responsible for generating authentication tokens for our MSA account.

If we look for RPC calls within this DLL, we can see that a bunch are being directed to a service called `wlidsvc`:

![](https://assets.xpnsec.com/WAM-BAM/wambam-image1_nqyfd1.png)

Unfortunately Microsoft do not make an IDL available for RPC calls to this service (or provide much information at all), so we’re going to have to do a bit of reversing to figure this out.

Let’s attach WinDBG to `wlidsvc` and monitor the RPC calls being made. After authenticating in any Office process, we see that the first call made is to the RPC method `WLIDCCreateContext` to create a context, and then to `WLIDCAcquireTokensWithNGC`… followed by a bunch of others calls which we’ll ignore for now.

If we add a breakpoint to the latter method, logging into our MSA account in Office results in a hit:

![](https://assets.xpnsec.com/WAM-BAM/wambam-image2_kheror.png)

Stepping until we hit a `ret` and inspecting the populated parameters shows something interesting in argument 12’s memory region.

![](https://assets.xpnsec.com/WAM-BAM/wambam-image3_ity3av.png)

That sure looks like a token to me! If we open a proxy like Fiddler, we see that this matches the authentication token format used when Office accesses web services:

![](https://assets.xpnsec.com/WAM-BAM/wambam-image4_ui0qc0.png)

So how can we make a call to this from our own tooling? Let’s use [James Forshaw’s](https://twitter.com/tiraniddo) [NtObjectManager](https://www.powershellgallery.com/packages/NtObjectManager/1.1.32) to generate a stub that we can work with.

```
$rpc = ls C:\windows\system32\wlidsvc.dll | Get-RpcServer -DbgHelpPath "C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\dbghelp.dll"
$rpc | Format-RpcClient -OutputPath .\rpc
```

It is worth nothing that the RPC stubs generated differ depending on the version of Windows, for example in Windows 10 we find that field counts change on input structures, so keep this in mind if you receive the dreaded `(0x800706F7) - The stub received bad data.` error.

Crafting a quick C# application using the RPC client stub, we’ll replay the inbound RPC call that we observed earlier and add in our parameters, which gives us something like this:

```
Struct_5[] s5 = new Struct_5[1];
int arg1, arg2, arg3, arg4, arg6;
NdrContextHandle context;

Struct_4[] s4 = new Struct_4[] {
	new Struct_4(
    // Change the scope to gen tokens for other services
  "scope=service::substrate.office.com::MBI_SSL_SHORT&telemetry=MATS&uaid=ABCDEF12-3456-7890-AAAA-DEADB33F0000&clientid=00000000480728C5",
	"TOKEN_BROKER",
    "",
    0,
    0,
    0,
    1
    )
};

client.Connect();
client.WLIDCreateContext(email, clientID, 0x880000, out context);
client.WLIDAcquireTokensWithNGC(context, 0x200, 1, s4, "", 0, "Silent", out arg1, out arg2, out arg3, out arg4, out s5, out arg6);
```

And if we call this:

![](https://assets.xpnsec.com/WAM-BAM/wambam-image5_actqg7.png)

As this is an MSA authentication request, we’re going to have to use services like Substrate to access Microsoft 365 services. Spinning up a proxy and navigating through Office is the best way to figure out what to call and what parameters these web services take. But you can see that with the passport token returned, we can authenticate and interact just fine:

![](https://assets.xpnsec.com/WAM-BAM/wambam-image6_sxqsni.png)

## Token Cache

Now we’ve looked at how MSAs are recovered, what about Azure AD? Well we know via [Lee Christensen](https://twitter.com/tifkin_)‘s [post](https://posts.specterops.io/requesting-azure-ad-request-tokens-on-azure-ad-joined-machines-for-browser-sso-2b0409caad30) that we can request new tokens on demand quite easily, but what about those cached tokens that we’ve been seeing within Office processes being dumped, how are they being loaded on startup?

Let’s provision a new host and associate our user account with AzureAD, then sign into Office and then try and figure out where tokens are stored.

![](https://assets.xpnsec.com/WAM-BAM/wambam-image7_g1vr6n.png)

To make sure we’re on the right track, let’s dump some strings from memory and make sure that our elusive `eyJ0eX` signature is present:

![](https://assets.xpnsec.com/WAM-BAM/wambam-image8_iidxcx.png)

Again we dive back into hunting DLLs, but this time we’ll focus on `Windows.Security.Authentication.Web.Core.dll`.

Now I know what you’re thinking… and with that naming convention I thought the same… but unfortunately this isn’t a .NET assembly (that would have made things too easy and would have given me time away from my PC this weekend). Instead this is a WinRT library, so we need to head into Ghidra to understand what is happening.

After some coffee and a late night, a method of `AddWebTokenResponseToCache` stands out:

![](https://assets.xpnsec.com/WAM-BAM/wambam-image9_z1lu1p.png)

If we chase this further, we see that this method is actually responsible for caching credentials to serialised files which can be found in `%LOCALAPPDATA%\Microsoft\TokenBroker\Cache`

![](https://assets.xpnsec.com/WAM-BAM/wambam-image10_husyrq.png)

OK, let’s take a look at those `TBRES` files:

![](https://assets.xpnsec.com/WAM-BAM/wambam-image11_oprrcy.png)

Looks too clean and easy… But sure ...