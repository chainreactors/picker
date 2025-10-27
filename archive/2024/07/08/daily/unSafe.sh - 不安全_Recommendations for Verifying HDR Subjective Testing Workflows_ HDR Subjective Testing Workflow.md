---
title: Recommendations for Verifying HDR Subjective Testing Workflows: HDR Subjective Testing Workflow
url: https://buaq.net/go-249226.html
source: unSafe.sh - 不安全
date: 2024-07-08
fetch_date: 2025-10-06T17:40:53.168395
---

# Recommendations for Verifying HDR Subjective Testing Workflows: HDR Subjective Testing Workflow

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/5846aba8b358eccc559604fd91234ddb.jpg)

Recommendations for Verifying HDR Subjective Testing Workflows: HDR Subjective Testing Workflow

Author:(1) Vibhoothi,Sigmedia Group, Department of Electronic and Electrical Engineering, Trinity
*2024-7-7 20:0:15
Author: [hackernoon.com(查看原文)](/jump-249226.htm)
阅读量:7
收藏*

---

**Author:**

(1) Vibhoothi,Sigmedia Group, Department of Electronic and Electrical Engineering, Trinity College Dublin, Ireland (Email: [[email protected]](https://hackernoon.com/cdn-cgi/l/email-protection));

(2) Angeliki Katsenou, Sigmedia Group, Department of Electronic and Electrical Engineering, Trinity College Dublin, Ireland & Department of Electrical and Electronic Engineering, University of Bristol, United Kingdom (Email: [[email protected]](https://hackernoon.com/cdn-cgi/l/email-protection));

(3) John Squires, Sigmedia Group, Department of Electronic and Electrical Engineering, Trinity College Dublin, Ireland (Email: [[email protected]](https://hackernoon.com/cdn-cgi/l/email-protection));

(4) Franc¸ois Pitie, Sigmedia Group, Department of Electronic and Electrical Engineering, Trinity College Dublin, Ireland (Email: [[email protected]](https://hackernoon.com/cdn-cgi/l/email-protection));

(5) Anil Kokaram, Sigmedia Group, Department of Electronic and Electrical Engineering, Trinity College Dublin, Ireland (Email: [[email protected]](https://hackernoon.com/cdn-cgi/l/email-protection)).

## Table of Links

* [Abstract and Introduction](https://hackernoon.com/preview/xplDkg0h6IkVsg5Fj0KR?ref=hackernoon.com)
* [HDR Standards](https://hackernoon.com/preview/NbtOsOKwYPa8GhAf117l?ref=hackernoon.com)
* [HDR Subjective Testing Workflow](http://hackernoon.com/preview/GVTiBWbGuPjnKfIZoEE1?ref=hackernoon.com)
* [Conclusion and References](https://hackernoon.com/preview/KeD36G20ESlzOj6CrNM5?ref=hackernoon.com)

## III. HDR SUBJECTIVE TESTING WORKFLOW

To ensure conformity with the modern HDR standard (ITU BT.2100 [11]), we require to validate multiple factors for the HDR quality assessment framework. The framework consists of three distinct parts. The first part is for the playback pipeline which includes cross-checking the playback, brightness, colour, and bit-depth of the display device. The second part is for handling intermediate file conversions. Finally, the third part concerns the testing environment.

### A. Playback Pipeline

1. Playback: Figure 1 outlines the typical playback pipeline to be used in a testing workflow. The initial part of the workflow is conversion and making the source into an encoderfriendly format (More in Section III-B). When it comes to HDR video playback, many software video players across different operating systems (OS) do not support true-HDR playback. This is either due to the limitation of hardware or software support (lack of implementation or OS-level support).

![](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-ti831oh.png?auto=format&fit=max&w=3840)

To circumvent this problem, we recommend using dedicated hardware for video playback. In this work, we utilised a Blackmagic Decklink 8K Pro Playback device [14] in a Linux environment, where a build of FFmpeg [15] software with Blackmagic support is used for video playback. Alternatively, the open-source GStreamer, or vendor-specific playback software (e.g. DaVinci Resolve [16] can be utilised.

Extension to consumer displays. In modern HDR consumer displays (televisions, or monitors), signalling metadata (colour primaries, transfer characteristics, matrix coefficients etc) is essential for HDR playback. Often, the hardware playback device or any converters which are used in the pipeline would strip the HDR metadata which can result in SDR playback. We recommend forcing HDR metadata on the device end, in cases where it is not available, an intermediate device that inserts HDR metadata is advised (e.g. Dr HDMI from HDFury [17]).

Signal Validation. When multiple sets of hardware devices (including various cables) are used in the playback pipeline, signal integrity (or statistics/existence) should be checked. To this end, and for signal passthrough, we recommend using a cross-converter/waveform monitor (we used Atmos Shogun 7).

2) Displays: The next milestone to accomplish true HDR video playback is the reliability of the television/monitor’s display panel in use. For this, at least five aspects should be observed: i) the ability to programmatically set the HDR settings in the display device, ii) option to turn off vendor-specific features for picture quality enhancement (tone-mapping, auto brightness limiter (ABL), gradation etc) iii) faithful tracking of the electro-optical transfer function (EOTF) in use (PQ) for both low and high-luminance areas, iv) the ability to display at least 1000 nits of brightness for at least 5-10% window, v) Behaviour of sustained brightness over the period. Keeping all of these in consideration, we are utilising a Sony BVM-X300v2 OLED critical reference monitor as a source of reference, along with two consumer-level LCD (Sony KD75ZD9) and OLED (Sony A80J) HDR display televisions.

Local dimming analysis. To analyse the display panel’s local dimming, blooming effect, and colour-bleeding artefacts, we developed a night-sky-star test pattern [18]. This pattern randomly distributes different percentages (1, 2, 5, 10, 20, 50, 80%) of peak-white pixels across the display resolution. Figure 2 showcases the behaviour of a 1% white window with a reference monitor (middle) and the Sony LCD TV (right). We advise using this artificial test pattern for measuring the

![](https://hackernoon.imgix.net/images/fWZa4tUiBGemnqQfBGgCPf9594N2-fb931dx.png?auto=format&fit=max&w=1920)

true behaviour of the panel over real night-sky patterns as they are prone to ISO camera noise. We later measured the brightness of a small area where most pixels are i) black, and ii) white. If a significant increase of brightness over window size for both is observed, the panel is susceptible to poor local dimming. In our study, we observed the brightness of the LCD panel increased linearly based on the number of white pixels, and the OLED panel showcased superior local dimming.

3) Brightness: Many of the current consumer displays have ABLs that do not allow peak brightness beyond a certain window size (gradually decreases) and/or sustained peak brightness over time. Many displays include this to protect the display units. Thus, we recommend analysing i) the sustained brightness using a 1% full white window; ii) the brightness variation over different window-size. In EBU’s Tech Report 3225v2 [6], it is recommended to test the peak brightness (L) of the TVs using a full-white window at four levels of screen area (S) (4, 10, 25 and 81%). In our analysis, we discovered that four points may not be sufficient to model the true behaviour of consumer displays. We recommend expanding this by including more steps S ∈ {1 . . . 5, 7, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 80, 90, 100}%. Figure 3a shows the sustained brightness of 1% window observed for a period of 600 seconds for the three considered display units. As easily observed, the reference monitor (yellow line) consistently sustains the brightness. The LCD TV (blue line) sustained high brightness for a long period (≈180 sec for >=1500nits). The OLED TV (red line) demonstrated a significant drop in brightness after 100 secs. We believe the primary reason for this behaviour is due to heating and the limited cooling of the OLED panel. When the temperature of the TV panel reaches ≈55◦C, the peak

![](https://hackernoon...