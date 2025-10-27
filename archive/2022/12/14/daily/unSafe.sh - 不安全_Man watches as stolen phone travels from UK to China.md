---
title: Man watches as stolen phone travels from UK to China
url: https://buaq.net/go-139899.html
source: unSafe.sh - 不安全
date: 2022-12-14
fetch_date: 2025-10-04T01:23:05.733969
---

# Man watches as stolen phone travels from UK to China

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

![]()

Man watches as stolen phone travels from UK to China

Have you ever wondered what happens to your phone if it’s stolen while
*2022-12-13 21:0:0
Author: [www.malwarebytes.com(查看原文)](/jump-139899.htm)
阅读量:21
收藏*

---

Have you ever wondered what happens to your phone if it’s stolen while on vacation or a business trip? The answer may surprise you, as it did one Mastodon user who graciously shared a tale of a smartphone gaining some serious air miles. Our intrepid business traveller was in London when their phone was [snatched from their hand in the street](https://hachyderm.io/%40em0/109494779578990831).

Thankfully, they'd taken the precaution of setting up Apple's [Find My](https://en.wikipedia.org/wiki/Find_My_iPhone) service prior to making their trip.

In practical terms, this meant that the phone could be remotely wiped (via Find My) and essentially turned into a paperweight. This has a two fold advantage: Keeping valuable data out of the thief's hands, and also making the phone considerably less useful to a criminal.

You might think a theft such as this stays local, and that's what it looked like for a while with the phone [coming to a halt](https://hachyderm.io/%40em0/109494855455381888) a few miles away. I would have assumed the phone would be sold locally or scrapped, but in this story our thief had other ideas in mind. What followed was an attempt to revive the phone via phishing, and a very long flight.

## When a theft gets phishy

The thief was not just interested in grabbing the device and selling it on in its bricked form. They wanted to reactivate the device too. This was attempted via a [text message](https://hachyderm.io/%40em0/109494876603962275) sent to the phone owner’s emergency contacts. The text reads as follows:

> *Your iPhone 13 Pro 256GB Sierra Blue has been found. View location: [URL]*
>
> *Apple Support*

The site, which spoofed the Find My website, was phishing for an Apple ID login to kickstart the reviving process. I’m sure the thief wouldn’t have objected to whatever data was locked behind that Apple ID too, but we can presume that getting the phone up and running is the primary concern.

Roughly a month after the phone was stolen, the [activation lock](https://support.apple.com/en-gb/HT201365#:~:text=Find%20My%20includes%20Activation%20Lock,Find%20My%20on%20your%20device.) for the device started pinging home. This is the feature which prevents random people from unlocking a lost or stolen device.

The victim of this crime was surprised to learn that the stolen device had [travelled from the UK to Shenzen in China](https://hachyderm.io/%40em0/109494947636636603). You may wonder if the Find My service was perhaps malfunctioning and the stolen device was still in London somewhere, but as we're about to see, this is far from the only example of this happening.

## Why do stolen phones end up in China?

Stolen phones ending up in China is, perhaps surprisingly, not uncommon. In fact, searching for this kind of thing brings up a wealth of results (try it!) and they all tend to look something like this:

> My phone was swiped from my hand in London a month ago. Annoyed, I immediately blocked the phone and erased its contents.
>
> Anyway, I got a notification today and that my phone has now been switched on in Shenzen, China. [pic.twitter.com/nPNEGaflQT](https://t.co/nPNEGaflQT)
>
> — Scott Bryan (@scottygb) [October 25, 2021](https://twitter.com/scottygb/status/1452632418670850052?ref_src=twsrc%5Etfw)

Phones make their way via “[networks of black marketers](https://www.cbsnews.com/news/iphone-stolen-in-nyc-now-in-china-icloud-photos-reveal/)” to their new owners in cities where phones, and modifications, are extremely cheap. In many cases, the final destination for the stolen iPhone is someone who has no idea a theft took place. Occasionally there’s a [heartwarming story and meet up](https://www.buzzfeed.com/mjs538/i-followed-my-stolen-iphone-across-the-world-became-a-celebr), but mostly it’s just a case of “My phone is gone and now I need to do something about it”.

## What to do if your iPhone is stolen

There are some [great tips gleaned from personal experience](https://hachyderm.io/%40em0/109494983398916571) via the above tale, most importantly making sure you [turn on Find My](https://support.apple.com/en-gb/HT210400). This is the way you’ll be able to remotely scrub that device and make it unusable for the thief. The other great tip is to make sure you have a secondary (and fast!) way to access Find My. If you don’t have an additional device with you, then you may struggle to find a way to get online and remedy the situation. Every second counts. It’s worth noting that you can [still take steps to protect your data](https://support.apple.com/en-gb/HT211207) even if you don’t enable Find My.

Apple provides several tips for [what you should do in the event of a theft](https://support.apple.com/en-gb/HT201472). Here’s some of the more pressing technical related suggestions:

1. **Lock your phone down**. Use the previously mentioned [Find My service](https://www.icloud.com/find). Do this in advance of any theft! In your Settings app, tap your name, and then select Find My.

**2. Mark your phone as lost**. Doing this [via the Find My app](https://support.apple.com/en-gb/HT210515#markaslost) disables the Apple Pay service, and locks the device with a passcode like so:

* Open the Find My app and choose the Devices tab or the Items tab.
* Select your missing device or item.
* Scroll down to Mark As Lost or Lost Mode and select Activate or Enable.
* Follow the onscreen steps if you want your contact information to be displayed on your missing device or item, or if you want to enter a custom message asking the finder of your missing device to contact you.
* Select Activate.

**Erase the device remotely**. To [do this](https://support.apple.com/en-gb/HT210515#erasedevice):

* Open the Find My app and choose the Devices tab.
* Select the device you want to erase remotely.
* Scroll down and choose Erase This Device.
* Select Erase This [device].

## What to do if your Android is stolen

This can be a bit trickier, as there are so many different models out there and often network carriers nudge you towards using their own bespoke tracking solutions. Despite this, the [basic Android options](https://support.google.com/accounts/answer/6160491?hl=en) should always be available. To enable Android's find my device service:

* Open Settings
* Tap Security > Find My Device.
* If you can't see the Security option, tap Security > location or Google > Security.
* Ensure Find My Device is enabled.
* Test the service out on the [Find my Device site](https://www.google.com/android/find).
* From the map, you can select the "Lock and Erase" option. Note that it may not erase the contents of an SD card.

Losing your phone, laptop, or other device to a thief is never a pleasant experience but you’re never totally out of options. The trick is to ensure you put some time into setting these solutions in place long before the possibility of a theft happens. Stay safe out there!

---

文章来源: https://www.malwarebytes.com/blog/news/2022/12/man-watches-as-stolen-phone-travels-from-uk-to-china
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)