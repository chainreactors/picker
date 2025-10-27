---
title: Microsoft Secure Boot Bug
url: https://www.schneier.com/blog/archives/2023/05/microsoft-secure-boot-bug.html
source: Schneier on Security
date: 2023-05-18
fetch_date: 2025-10-04T11:42:23.402929
---

# Microsoft Secure Boot Bug

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Microsoft Secure Boot Bug

Microsoft is currently [patching](https://arstechnica.com/information-technology/2023/05/microsoft-patches-secure-boot-flaw-but-wont-enable-fix-by-default-until-early-2024/) a zero-day Secure-Boot bug.

> The BlackLotus bootkit is the first-known real-world malware that can bypass Secure Boot protections, allowing for the execution of malicious code before your PC begins loading Windows and its many security protections. Secure Boot has been enabled by default for over a decade on most Windows PCs sold by companies like Dell, Lenovo, HP, Acer, and others. PCs running Windows 11 must have it enabled to meet the software’s system requirements.
>
> Microsoft says that the vulnerability can be exploited by an attacker with either physical access to a system or administrator rights on a system. It can affect physical PCs and virtual machines with Secure Boot enabled.

That’s important. This is a nasty vulnerability, but it takes some work to exploit it.

The problem with the patch is that it breaks backwards compatibility: “…once the fixes have been enabled, your PC will no longer be able to boot from older bootable media that doesn’t include the fixes.”

And:

> Not wanting to suddenly render any users’ systems unbootable, Microsoft will be rolling the update out in phases over the next few months. The initial version of the patch requires [substantial user intervention to enable](https://support.microsoft.com/en-us/topic/kb5025885-how-to-manage-the-windows-boot-manager-revocations-for-secure-boot-changes-associated-with-cve-2023-24932-41a975df-beb2-40c1-99a3-b3ff139f832d)—you first need to install May’s security updates, then use a five-step process to manually apply and verify a pair of “revocation files” that update your system’s hidden EFI boot partition and your registry. These will make it so that older, vulnerable versions of the bootloader will no longer be trusted by PCs.
>
> A second update will follow in July that won’t enable the patch by default but will make it easier to enable. A third update in “first quarter 2024” will enable the fix by default and render older boot media unbootable on all patched Windows PCs. Microsoft says it is “looking for opportunities to accelerate this schedule,” though it’s unclear what that would entail.

So it’ll be almost a year before this is completely fixed.

Tags: [Microsoft](https://www.schneier.com/tag/microsoft/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/), [zero-day](https://www.schneier.com/tag/zero-day/)

[Posted on May 17, 2023 at 7:01 AM](https://www.schneier.com/blog/archives/2023/05/microsoft-secure-boot-bug.html) •
[17 Comments](https://www.schneier.com/blog/archives/2023/05/microsoft-secure-boot-bug.html#comments)

### Comments

K.S. •
[May 17, 2023 7:54 AM](https://www.schneier.com/blog/archives/2023/05/microsoft-secure-boot-bug.html/#comment-422006)

I am not convinced that additional security provided by secure boot offers an average user with sufficient value to offset the loss of backwards compatibility. I suspect, without evidence to back it up, that this might be another way Microsoft forcing migration to Windows 11.

The Spied Upon One •
[May 17, 2023 8:40 AM](https://www.schneier.com/blog/archives/2023/05/microsoft-secure-boot-bug.html/#comment-422008)

Well, “Hello W…, um, Linux”

Peter A. •
[May 17, 2023 9:06 AM](https://www.schneier.com/blog/archives/2023/05/microsoft-secure-boot-bug.html/#comment-422009)

So if I already have W11 or upgrade to W11 and later get this patch installed forcibly I would never be able to boot a different OS on that computer?

What about new computers bought after the deadline?

Wannabe techguy •
[May 17, 2023 9:06 AM](https://www.schneier.com/blog/archives/2023/05/microsoft-secure-boot-bug.html/#comment-422010)

@ K.S.-Noo why would they do that? Yeah right. lol

Nick Alcock •
[May 17, 2023 9:19 AM](https://www.schneier.com/blog/archives/2023/05/microsoft-secure-boot-bug.html/#comment-422011)

Rj: it adds to the secure boot revocation list in flash, which is consulted by the boot ROM. No changes to the boot *code* are needed — but of course it’s going to break older boot disks etc. (Things run from boot drives that are not written by Microsoft will presumably use other keys, which MS has not revoked — I hope. At least I hope they only revoked the signatures used by their own bootloader and not things like shim that they signed on behalf of other people. From their list of affected media, my hope seems to be borne out. But of course that doesn’t help people using things like Windows emergency boot disks, Windows On-The-Go etc etc.)

Clive Robinson •
[May 17, 2023 10:21 AM](https://www.schneier.com/blog/archives/2023/05/microsoft-secure-boot-bug.html/#comment-422013)

@ ALL,

Blackloutus has been around for a while, and this Microsoft fix is not exactly going to eliminate it or similar…

We’ve seen Blackloutus bounce back before, and it will be able to again, all be it with more difficulty once this Microsoft “walled garden” has been deployed. The thing is though “more difficult” is very relative thus very rarely an impediment, once the ball has started rolling profitably.

So to @Rj and @K.S. yes it does look like a software,”lockin method”.

But… If you are using an older MS OS,

1, Where are you getting your drivers from with newer hardware?

This tends not to be a problem with Linux and supported hardware (Nvidia is not nor ever likely to be supported due to shall we say “Managment Perspective”).

So it’s not just Microsoft gaining by this, many hardware suppliers will as well… as users find their perfectly functional devices “obsoleted”… Which begs the question as to why the EU has not stuck it’s political hoof in with regards long standing directives to do with “Waste Electrical and Electronic Equipment”(WEEE) and similar legislation?

As @Nick Alcock points out it’s not software that is being changed but the rather questionable storage of a revocation list in the hidden EFI storage[1].

Whilst there are tools around that will enable you to change this storage (hence how Blackloutus can get back) the other way around it is to turn secure-boot off if the manufacturer of the motherboard alows it and the likes of HP tend not to…

The thing is there is no way to have the freedom to do what you want with the hardware you’ve purchased, as well as have “secure boot” enabled for that potentially minimal extra security improvment.

Why “minimal security improvment”? Well remember the Microsoft warning given above of,

“either physical access to a system or administrator rights on a system”

Both of which have happened in the past and will continue to happen again and again well into the future. So if you or someone you know or work for is “a person of interest” then Secure-boot won’t be secure for you at all…

Remember all this nonsense has come abo...