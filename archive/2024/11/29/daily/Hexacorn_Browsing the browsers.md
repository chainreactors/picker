---
title: Browsing the browsers
url: https://www.hexacorn.com/blog/2024/11/28/browsing-the-browsers/
source: Hexacorn
date: 2024-11-29
fetch_date: 2025-10-06T19:17:00.808707
---

# Browsing the browsers

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2024/11/23/portability-of-old-windows-programs/)
[Next →](https://www.hexacorn.com/blog/2024/11/28/windows-storage-lol/)

# Browsing the browsers

Posted on [2024-11-28](https://www.hexacorn.com/blog/2024/11/28/browsing-the-browsers/ "12:00 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

This a weird post; it doesn’t give many answers and it pretty much focuses on describing results of a simple task of data hoarding…

When people think of a ‘browser’ they usually think of a software like Chrome, Safari, Firefox, Opera, Brave, Vivaldi, maybe Edge, and some older people maybe think of Internet Explorer (rip) and Netscape (totes rip). And if we ask malware authors, they will probably expand this list to include many chrome-based browsers that ‘appeared on the market’ in recent years. And if we look at some of the actual Microsoft code, we will find out that they consider many Web control hosting apps to be browsers as well.

For example, at the time of Internet Explorer dominance, many applications were utilizing IE’s web control ([IWebBrowser](https://learn.microsoft.com/en-us/dotnet/api/microsoft.uii.csr.browser.web.iwebbrowser?view=dynamics-usd-3)) to deliver a flashy, HTML-based GUI. At some stage in early 2000s it was so ‘fad’ and prevalent that eventually every major software company was using it, and most of users… hated it. And here we are, in 2024, with web controls still all over the place – f.ex. including most of the Electron apps (ignored in this post).

I have outlined some of the process names associated with browsers in this [old post](https://www.hexacorn.com/blog/2023/01/08/excelling-at-excel-part-2/), and today I will expand on it a bit.

How? By building a more robust list of processes that kinda meet the ‘is this a browser process?’ condition:

* 360chrome.exe
* 360se.exe
* authhost.exe
* avant.exe
* brave.exe
* browser.exe
* browser\_broker.exe
* chrome.exe
* citrio.exe
* coolnovo.exe
* coowon.exe
* cyberfox.exe
* DCIScanner
* deepnet.exe
* dooble.exe
* epic.exe
* explorer.exe
* FAKEVIRTUALSURFACETESTAPP.EXE
* firefox.exe
* FirstLogonAnim.exe
* IEUTLAUNCH.EXE
* iexplore.exe
* iridium.exe
* jshost.exe
* k-meleon.exe
* LOADER42.EXE
* maxthon.exe
* MicrosoftEdge.exe
* MicrosoftEdgeBCHost.exe
* MicrosoftEdgeCP.exe
* MicrosoftEdgeDevtools.exe
* MicrosoftEdgeSH.exe
* midori.exe
* msedge.exe
* msedge\_proxy.exe
* msedge\_pwa\_launcher.exe
* MSFEEDSSYNC.EXE
* MSHTMPAD.EXE
* MSOOBE.EXE
* mustang.exe
* NETPLWIZ.EXE
* opera.exe
* orbitum.exe
* palemoon.exe
* pickerhost.exe
* qqbrowser.exe
* qupzilla.exe
* RESTOREOPTIN.EXE
* safari.exe
* seamonkey.exe
* sleipnir.exe
* sogueexplorer.exe
* superbird.exe
* SYSPREP.EXE
* TE.EXE
* Te.ProcessHost.exe
* tor.exe
* torch.exe
* USERACCOUNTBROKER.EXE
* vivaldi.exe
* Windows.WARP.JITService.exe
* WWAHOST.EXE

But… we know this is not everything…

Over last few years we have seen a number of randomly-named Chrome-based browser clones appearing ‘on the market’ and Threat Actors did take a notice.

Many infostealers actively look for user profiles associated with these browser paths:

* \360Chrome\Chrome\
* \7Star\7Star\
* \8pecxstudios\Cyberfox\
* \Amigo\
* \BraveSoftware\Brave-Browser\
* \CatalinaGroup\Citrio\
* \CentBrowser\
* \Chedot\
* \Chromium\
* \CocCoc\Browser\
* \Comodo\Dragon\
* \Comodo\IceDragon\
* \Coowon\Coowon\
* \CryptoTab Browser\
* \Elements Browser\
* \Epic Privacy Browser\
* \Fenrir Inc\Sleipnir5\setting\modules\ChromiumViewer
* \Flock\Browser\
* \Google\Chrome\
* \Google Chrome Canary\
* \Chrome SxS\
* \Iridium\
* \K-Meleon\
* \Kometa\
* \liebao\
* \MapleStudio\ChromePlus\
* \Microsoft\Edge\
* \Moonchild Productions\Pale Moon\
* \Mozilla\Firefox\
* \Mozilla\icecat\
* \Mozilla\SeaMonkey\
* \NETGATE Technologies\BlackHawk\
* \Opera Software\Opera Stable\
* \Orbitum\
* \Postbox\
* \QIP Surf\
* \Sputnik\Sputnik\
* \Tencent\QQBrowser\
* \Torch\
* \uCozMedia\Uran\
* \Vivaldi\
* \Waterfox\
* \Yandex\YandexBrowser\

I believe this is a very comprehensive list, but I bet I missed some entries. If you notice anything missing, please let me know and I will add it.

The bottom line: there are so many browsers or web control-hosting apps out there today that it makes sense to build a list of keywords that reference them, so we can detect info stealers’ quickly – in their code, data and/or in the telemetry they generate…

This entry was posted in [Archaeology](https://www.hexacorn.com/blog/category/archaeology/), [asset inventory](https://www.hexacorn.com/blog/category/asset-inventory/), [Browsers](https://www.hexacorn.com/blog/category/browsers/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/11/28/browsing-the-browsers/ "Permalink to Browsing the browsers").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")