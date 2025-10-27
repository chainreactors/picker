---
title: New technique can defeat voice authentication "after only six tries"
url: https://buaq.net/go-170937.html
source: unSafe.sh - 不安全
date: 2023-07-01
fetch_date: 2025-10-04T11:51:10.872523
---

# New technique can defeat voice authentication "after only six tries"

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

![](https://8aqnet.cdn.bcebos.com/31fdc1781aa2501de426f03c836601da.jpg)

New technique can defeat voice authentication "after only six tries"

Voice authentication is back in the news with another tale of how easy
*2023-6-30 19:30:0
Author: [www.malwarebytes.com(查看原文)](/jump-170937.htm)
阅读量:22
收藏*

---

Voice authentication is back in the news with another tale of how easy it might be to compromise. University of Waterloo scientists have discovered a technique which they claim [can bypass voice authentication](https://uwaterloo.ca/news/media/how-secure-are-voice-authentication-systems-really) with “up to a 99% success rate after only six tries”. In fact this method is apparently so successful that it is said to evade spoofing countermeasures.

Voice authentication is becoming increasingly popular for crucial services we make use of on a daily basis. It’s a particularly big deal for banking. The absolute last thing we want to see is easily crackable voice authentication, and yet that’s exactly what we have seen.

Back in February, reporter Joseph Cox was able to [trick his bank’s voice recognition system](https://www.malwarebytes.com/blog/news/2023/02/ai-generated-voice-recording-grants-access-to-telephone-banking) with the aid of some recorded speech and a tool to synthesise his responses.

A user typically enrolls into a voice recognition system by repeating phrases, so the system at the other end gets a feel for how their voice sounds. As the Waterloo researchers put it:

> When enrolling in voice authentication, you are asked to repeat a certain phrase in your own voice. The system then extracts a unique vocal signature (voiceprint) from this provided phrase and stores it on a server.
>
> For future authentication attempts, you are asked to repeat a different phrase and the features extracted from it are compared to the voiceprint you have saved in the system to determine whether access should be granted.

This is where Cox and his synthesised vocals came into play—his bank’s system couldn’t distingusih between his real voice and a synthesised version of his voice. The response to this was an assortment of countermeasures that involve analysing vocals for bits and pieces of data which could signify the presence of a deepfake.

The Waterloo researchers have taken the game of cat and mouse a step further with their own counter-counermeasure that removes the data characterstic of deepfakes.

From the release:

> The Waterloo researchers have developed a method that evades spoofing countermeasures and can fool most voice authentication systems within six attempts. They identified the markers in deepfake audio that betray it is computer-generated, and wrote a program that removes these markers, making it indistinguishable from authentic audio.

There are many ways to edit a slice of audio, and plenty of ways to see what lurks inside sound files using visualiser tools. Anything that wouldn't normally be present can be traced, analysed, and altered or made to go away if needed.

As an example, loading up a [spectrum analyser](https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html/plugins/Wave%20Candy.htm) (which illustrates the audio signal in visible waves and patterns) may reveal images hidden inside of the sound. Below you can see a hidden image represented by the orange and yellow blocks every time the audio file plays. While the currently discussed research [isn’t available outside of paid access](https://uwaterloo.ca/news/media/how-secure-are-voice-authentication-systems-really), the techniques relied upon to find any deepfake generated cues will likely work along much the same lines. There will be telltale signs of synthetic markers in the sound files, and with these synthetic aspects removed the detection tools will potentially miss the now edited audio because it looks (and more importantly sounds) like the real thing.

![Audio analysis](https://www.malwarebytes.com/blog/news/2023/06/easset_upload_file26668_270986_e.jpg)

It remains to be seen what organisations deploying voice authentication will make of this research. However, you can guarantee whatever they come up with will continue this game of cat and mouse for a long time to come.

---

文章来源: https://www.malwarebytes.com/blog/news/2023/06/new-technique-can-defeat-voice-authentication-in-just-6-attempts
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)