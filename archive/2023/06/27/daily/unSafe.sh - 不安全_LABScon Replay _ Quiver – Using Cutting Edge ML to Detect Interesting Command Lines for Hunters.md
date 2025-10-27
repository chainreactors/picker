---
title: LABScon Replay | Quiver – Using Cutting Edge ML to Detect Interesting Command Lines for Hunters
url: https://buaq.net/go-170416.html
source: unSafe.sh - 不安全
date: 2023-06-27
fetch_date: 2025-10-04T11:44:45.635161
---

# LABScon Replay | Quiver – Using Cutting Edge ML to Detect Interesting Command Lines for Hunters

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

LABScon Replay | Quiver – Using Cutting Edge ML to Detect Interesting Command Lines for Hunters

Quiver – Using Cutting Edge ML to detect interesting command lines for Hunters: Audio automatically
*2023-6-26 21:16:34
Author: [www.sentinelone.com(查看原文)](/jump-170416.htm)
阅读量:16
收藏*

---

## Quiver – Using Cutting Edge ML to detect interesting command lines for Hunters: [Audio automatically transcribed by Sonix](https://sonix.ai/?utm_source=embed "Sonix is the best audio transcription service in 2023")

Quiver – Using Cutting Edge ML to detect interesting command lines for Hunters: [this mp4 audio file](https://sonix.ai/speech-to-text-all-supported-file-formats?utm_source=embed "Sonix's converts the most popular audio file formats to text") was [automatically transcribed by Sonix](https://sonix.ai/transcribe-audio?utm_source=embed "Sonix is the best way to transcribe audio files in 2023") with the [best speech-to-text algorithms.](https://sonix.ai/automated-transcription?utm_source=embed "The best speech-to-text algorithms") This transcript may contain errors.

**Dean Langsam:**

**Dean Langsam:**
So Dall-e two can create an image from text. In that example, we can see a cybersecurity researcher sitting on a beanbag in front of a pool in the desert in a fancy hotel trying to reverse engineer a nation state malware, working on a presentation in a realistic style. So that's you guys. If you can connect with that one, maybe this is you guys as you can see, it's not very good with text, but you are all cyber security researchers.

**Dean Langsam:**
GPT three or GPT three is a model that can generate text. It's applications in cybersecurity. Don't really need to read that. What you need to know is that except for the I've written only the gray part and GPT three created the rest.

**Dean Langsam:**
In the same manner GitHub copilot. I like,this is code that I actually use just some authentication stuff. And when I've written that I just I was just starting to use GitHub copilot and I like only the gray parts or the parts that I've actually typed in and GitHub copilot did the rest for me. You can see that even you have the function that like I made a typo, I called it anonymized password and like it understood that I mean to anonymize the password.

**Dean Langsam:**
Okay, so what's common to all those models? All those models understand language. They share language. Common language features between users or between applications. And part of the learning process is unsupervised, a term that we'll speak about later. The question is, can we do the same for the language of command lines? And the answer is yes, but well, no. So currently you're thinking like, what am I doing here? I came to a cybersecurity conference and we're here to talk about deep learning. Gal and I are not, firstly, cybersecurity people. We are coming from the field of machine learning and deep learning, and we try to get a free trip to Phoenix. So we managed to.

**Dean Langsam:**
We're going to talk about the problems we had with command lines before then. What changed that made this one possible. Then about our package Quiver, which as you've seen, the acronym came first. And eventually we'll show the big show of what we've got. This is Gal.

**Gal Braun:**
So I'm. Gal. Staff data scientist in SentinelOne for the last six years. A father of two. And Breaking Bad is the best show ever.

**Dean Langsam:**
And we are mostly the same person. I'm Dean. I'm a Staff data scientist in SentinelOne for three years, actually. Gal got me into the company. I'm a father of one, and Breaking Bad is the best show ever. Except maybe The Wire.

**Dean Langsam:**
So because we're not in a deep learning conference, let's do like a few minute intro to machine learning and deep learning. What you see here are cats and dogs, and those are called samples. We want to create an algorithm that can distinguish between cats and dogs.

**Dean Langsam:**
One way they try to do this before is like with algorithms that people are trying to generate. Maybe if it has like the ears are, the ears are that way and the tail is that way, maybe it's a cat, maybe it's a dog. And it was a very hard problem. Even a person couldn't tell you like, why the why am I seeing a cat or a dog in this picture? I just like when you know, you know.

**Dean Langsam:**
So we try to make this in deep learning. We just show the the computer, the algorithm, many examples of cats and dogs. This is called tagging or labeling. And you can go into Google and just type like give me pictures of dogs. Those would be the green ones and then give me pictures of cats. Those will be the red ones. And then you show the algorithm enough samples and it will create an algorithm using what we call training.

**Dean Langsam:**
Then when you give it a new sample, the gray one, you, you, you don't tell the algorithm which one it is, which one it is, and you put it in the algorithm and the algorithm spits out, well, this is a cat in the same fashion. It says, This is a dog. Now, that was a pretty easy problem because you could search that on Google, like, give me cats, give me dogs. Enough people tagged cats and dogs in the history of time.

**Dean Langsam:**
Um, but as my friend John Naisbitt, I know he's not actually my friend, but he's a very famous person. He told "We are drowning in information, but we are starved for knowledge". Like all of us have a lot of stuff, like pictures of things, command lines, language, many things. So what we have, we have many command lines in SentinelOne. The thing we don't have is tag data or label data. The people that can actually do tagging for label data like saying is this command line bad or good or bad? The green ones are good. The red ones are bad. Most of the people that can actually label the data for us are in the in this room.

**Dean Langsam:**
So I could ask you guys, instead of listening to the talk, give me ten minutes of your time and start tagging data for me. But that is very manual process and that would not scale up.

**Dean Langsam:**
So what changed? Well, in the old time, meet Mimi. Mimi Katz. She's. She's Jewish like us. And she has a task. Separate, like she gets many papers and we tell her separate those papers between, like, stuff about cyber security and stuff about machine learning. Even if she doesn't know, like, the two concepts, maybe she can try to distinguish between the two. The problem is that the papers are in Hebrew and she doesn't know Hebrew, so she could maybe try and do so. If you give her like thousands of examples, maybe she can try and understand the hieroglyphs of Hebrew and try to understand which hieroglyphs are machine learning and which hieroglyphs are cybersecurity. But that that would again not scale up.

So instead we can introduce a baby. This is a Wonak or Wonak Cry. Won also doesn't speak Hebrew. He doesn't speak any language. He's a baby. But what what he does have is time because he's a baby and people are speaking Hebrew and English next to him all the time. Where does it meet us? Well, this is the old way.

**Dean Langsam:**
We used to do things like the first one is task one. Give the student a task to distinguish between two things, then give another student its task to distinguish between two other things. A baby can do something else. We can try and give it books like first, understand language, understand what's Hebrew, understand the relationships between words. Just understand the language. Then when you give them tasks, we can give them a lot less data to learn on the tasks instead of like giving it like the...