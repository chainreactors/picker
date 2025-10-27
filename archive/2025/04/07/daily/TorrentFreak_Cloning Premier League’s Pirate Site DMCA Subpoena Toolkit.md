---
title: Cloning Premier League’s Pirate Site DMCA Subpoena Toolkit
url: https://torrentfreak.com/recreating-premier-leagues-pirate-site-dmca-subpoena-toolkit-250406/
source: TorrentFreak
date: 2025-04-07
fetch_date: 2025-10-06T22:05:19.647588
---

# Cloning Premier League’s Pirate Site DMCA Subpoena Toolkit

[![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/search.svg)

* News ▼
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/x.svg)

# Cloning Premier League’s Pirate Site DMCA Subpoena Toolkit

April 6, 2025 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") >

A Premier League DMCA subpoena requires Cloudflare to hand over the details of individuals behind 38 pirate streaming sites. Before that process could even begin, the Premier League needed to obtain certain information about the pirate sites to support its claims. Today we'll attempt to recreate the toolkit used to gather that information and, if all goes to plan, it won't cost a single penny,

![premier-os](https://torrentfreak.com/images/premier-os.png)
Most prevalent in the movie and TV show sectors, applications for DMCA subpoenas are regularly filed at courts in the United States.

Aside from their intended purpose, DMCA subpoenas can provide useful clues about future anti-piracy strategies. When subpoenas are contested by intermediaries, subpoena applications sometimes become copyright cases in their own right. From a rightsholders’ perspective, in some cases they may be the only potential source of information yet to be exhausted.

## Getting Prepared

A few days ago, the UK’s Premier League asked a California federal court to issue a DMCA subpoena against Cloudflare. [The application identifies 38 target pirate streaming sites](https://torrentfreak.com/premier-league-subpoena-requires-cloudflare-to-unmask-streaming-pirates-250401/), many of which utilize multiple domains. Since the platforms all use Cloudflare, the Premier League hopes that information held by the company will help to unmask the sites’ currently anonymous operators.

Before filing an application under Section 512(h) of the DMCA, which allows copyright owners to obtain a subpoena and receive “information sufficient to identify an anonymous infringer,” applicants are first required to send DMCA takedown notices to the platform in question. The notices should identify the infringing content and state where the content can be found; in cases involving streaming sites, the right tools can prove helpful.

## Recreating the Toolkit

The screenshot below shows a live match playing on a pirate streaming site. Culled from the Premier League’s application, it provides clues that allow us to start identifying the tools in use and the problems they’re likely to solve once combined with Open Source Intelligence ([OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence)).

At a basic level in this context, OSINT can be almost any information made available on the internet. The screenshot is our primary source; it will help us identify the tools to recreate the toolkit, which in turn will use other public information sources to satisfy the requirements of the application.

## M3U8 Sniffer

![m3u8sniffer](https://torrentfreak.com/images/m3u8sniffer.png)
In this example it appears that when the Premier League visited the website sporttuna.pro, they were redirected to sporttuna.website and then to sporttuna.xyz (boxed in red).

Like most pirate sites, the ‘backend link’ or source of the stream (boxed in green) isn’t on public display. These links can be obtained in various ways but in this case, Chrome extension *M3U8 Sniffer* is the weapon of choice.

*M3U8 Sniffer*

![m3u8sniffer-v1](https://torrentfreak.com/images/m3u8sniffer-v1.png)

***From the developer’s website:** The extension intercepts visited web page’s network requests and identifies all m3u8 video stream URLs. When a m3u8 URL request is found, it is displayed in a box that overlays the visited web page (see images above) from which you can copy the m3u8 URL or play the video stream. Also, you can open the extension’s popup window to view the first and last m3u8 URLs found for each site, as well as to set a variety of extension options.*

*M3U8 Sniffer is a [free extension](https://chrome.google.com/webstore/detail/video-m3u8-sniffer-find-h/akkncdpkjlfanomlnpmmolafofpnpjgn) available from the Chrome Web Store. Further information is available from the developer at [SnifferTV.com](https://sniffertv.com/docs/).*

## Identifying the Remaining Tools

![](https://torrentfreak.com/images/ant-app.png)
Identifying the remaining tools was a little time-consuming but if we said the method was advanced or complicated, that would be a lie.

We simply trawled through the browser evidence images and took screenshots of the toolbars. These contain the icons of the apps used to obtain the evidence.

After extracting the toolbar icons we put those we recognized to the side, then identified the remainder using reverse image search tools. Straightforward options include Google Images and [Google Lens](https://lens.google/).

As an alternative, Chrome extension [RevEye Reverse Image Search](https://chromewebstore.google.com/detail/reveye-reverse-image-sear/keaaclcjhehbbapnphnmpiklalfhelgf) provides instant results from Google, Bing, Yandex, and TinEye.

*(Note: Bad extensions exist, trust nobody, [check the source](https://gist.github.com/paulirish/78d6c1406c901be02c2d#file-how-to-view-source-of-chrome-extension-md))*

## Internet Download Manager

![idm](https://torrentfreak.com/images/idm.png)
Given that M3U8 Sniffer “does NOT provide functionality to download the actual video streams” another piece of software comes in handy. IDM is a popular choice in the niche and appears to be the downloader of choice in this particular toolkit.

***From the official website:** When you click on a download link in a browser, IDM will take over the download and accelerate it. You don’t need to do anything special, just browse the Internet as you usually do. IDM will catch your downloads and accelerate them. IDM supports HTTP, FTP, HTTPS and MMS protocols.*

Unfortunately, IDM isn’t free but it is free to try via a [30-day trial](https://www.internetdownloadmanager.com/download.html). Some prefer [JDownloader](https://jdownloader.org/) since the price is more predictable, but there are [plenty of options](https://fmhy.net/file-tools#download-managers) in this niche.

## Fiddler

![fiddler2](https://torrentfreak.com/images/fiddler2.png)
Our best guess at identifying this next tool comes with a small caveat that its icon was almost impossibly blurred and even when fresh it’s still pretty basic. Ultimately, a green diamond and a single white ‘F’ works here.

Fiddler and tools with similar functionality (web debugging proxy tools) are used extensively by developers and investigators when keeping a close eye on HTTP traffic is a must. For those who’ve never cared to take a closer look, it can be real eye-opener. Even the most innocuous websites can behave pretty badly until users notice, so there’s never a bad time to take a first look.

[Fiddler Classic](https://www.telerik.com/fiddler/fiddler-classic) and [Fiddler Everywhere](https://www.telerik.com/download/fiddler-everywhere) are both available as free trials, and the same is true for [Charles Proxy](https://www.charlesproxy.com/download/) which appears regularly as evidence in Indian site-blocking cases.

Some prefer to monitor traffic with [Wireshark](https://www.w...