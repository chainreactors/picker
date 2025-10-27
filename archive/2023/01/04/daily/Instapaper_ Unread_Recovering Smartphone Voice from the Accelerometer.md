---
title: Recovering Smartphone Voice from the Accelerometer
url: https://www.schneier.com/blog/archives/2022/12/recovering-smartphone-voice-from-the-accelerometer.html
source: Instapaper: Unread
date: 2023-01-04
fetch_date: 2025-10-04T03:01:36.846132
---

# Recovering Smartphone Voice from the Accelerometer

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

## Recovering Smartphone Voice from the Accelerometer

Yet another smartphone side-channel attack: “[EarSpy: Spying Caller Speech and Identity through Tiny Vibrations of Smartphone Ear Speakers](https://arxiv.org/pdf/2212.12151.pdf)“:

> **Abstract:** Eavesdropping from the user’s smartphone is a well-known threat to the user’s safety and privacy. Existing studies show that loudspeaker reverberation can inject speech into motion sensor readings, leading to speech eavesdropping. While more devastating attacks on ear speakers, which produce much smaller scale vibrations, were believed impossible to eavesdrop with zero-permission motion sensors. In this work, we revisit this important line of reach. We explore recent trends in smartphone manufacturers that include extra/powerful speakers in place of small ear speakers, and demonstrate the feasibility of using motion sensors to capture such tiny speech vibrations. We investigate the impacts of these new ear speakers on built-in motion sensors and examine the potential to elicit private speech information from the minute vibrations. Our designed system *EarSpy* can successfully detect word regions, time, and frequency domain features and generate a spectrogram for each word region. We train and test the extracted data using classical machine learning algorithms and convolutional neural networks. We found up to 98.66% accuracy in gender detection, 92.6% detection in speaker detection, and 56.42% detection in digit detection (which is 5X more significant than the random selection (10%)). Our result unveils the potential threat of eavesdropping on phone conversations from ear speakers using motion sensors.

It’s not great, but it’s an impressive start.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [eavesdropping](https://www.schneier.com/tag/eavesdropping/), [side-channel attacks](https://www.schneier.com/tag/side-channel-attacks/), [smartphones](https://www.schneier.com/tag/smartphones/)

[Posted on December 30, 2022 at 7:18 AM](https://www.schneier.com/blog/archives/2022/12/recovering-smartphone-voice-from-the-accelerometer.html) •
[57 Comments](https://www.schneier.com/blog/archives/2022/12/recovering-smartphone-voice-from-the-accelerometer.html#comments)

### Comments

Winter •
[December 30, 2022 9:23 AM](https://www.schneier.com/blog/archives/2022/12/recovering-smartphone-voice-from-the-accelerometer.html/#comment-414756)

> zero-permission motion sensors

I think the root of the problem is that there are zero-permission data sources in mobile phones. Maybe the only solution for this game of whack-a-mole is complete segregation of data streams between apps.

Every app should be considered a security risk for every other app. For instance, if one app plays to the speakers, no other app should have zero-permission access to the speakers.

Clive Robinson •
[December 30, 2022 11:22 AM](https://www.schneier.com/blog/archives/2022/12/recovering-smartphone-voice-from-the-accelerometer.html/#comment-414758)

@ ALL,

Whilst this “instance” is relatively small it falls into a more general “class” of mechanical vibration “side channels”.

And it’s got a lot worse since “Micro Electro-Mechanical Systems”(MEMS) transducers. Basically MEMS are made in a very similar way to semiconductor chips, thus you get many thousand on a standard wafer.

The thing is the mechanical component that moves is extrodinarily small, light, and sensitive, which gives them a very wide bandwidth.

The difference between a MEMS microphone transducer and MEMS accelerometer or motion sensor is actually very small. The real difference is in what part of the mechanical vibration frequency range you want them to work.

Typically microphones in the 50-15,000Hz range and motion sensors below 50Hz.

Thus what makes the MEMS different is the “Digital Signal Processing”.

However we know that recovering usable audio in that low frequency range is quite “achivable” from the work of those using high speed video cameras watching light reflect of crisp/chip packets and similar shiny surfaces.

Ted •
[December 30, 2022 3:22 PM](https://www.schneier.com/blog/archives/2022/12/recovering-smartphone-voice-from-the-accelerometer.html/#comment-414762)

FYI … if you want to experiment with what the researchers used, you can download the **Physics Toolbox Sensor Suite** app. The app connects with a lot of your phone’s sensors.

You can use it to view your phone’s accelerometer data. The Z-axis was most relevant for measuring ear speaker vibrations. It’s pretty fun.

pup vas •
[December 30, 2022 4:49 PM](https://www.schneier.com/blog/archives/2022/12/recovering-smartphone-voice-from-the-accelerometer.html/#comment-414766)

See no evil: People find good in villains

=Across these measures, the research indicated that both children and adults consistently evaluated villains’ true selves to be overwhelmingly evil and much more negative than heroes’. At the same time, researchers also detected an asymmetry in the judgments, wherein villains were more likely than heroes to have a true self that differed from their outward behavior.=

Erdem Memisyazici •
[December 30, 2022 5:51 PM](https://www.schneier.com/blog/archives/2022/12/recovering-smartphone-voice-from-the-accelerometer.html/#comment-414769)

@Clive Robinson

That was very informative, thank you. [Here](http://people.csail.mit.edu/mrub/VisualMic/) is an MIT project demonstrating what they deemed a “visual microphone”. One use I thought was really interesting is recovering audio from silent movies which with a ton of approximation could restore the actors’ vocal performances (if you can extract tone and cadence, the script can be used to generate the audio).

It should also be possible to recover audio from charged particles in the air or WIFI even similar to [this](https://youtu.be/g3LT_b6K0Mc) project. I suppose neutrinos could tell you about vibrations in a planet’s core. As a friend and colleague once told me, “it’s all just waves man.” 😄

Help me darth vader, you're my only hope •
[December 30, 2022 8:06 PM](https://www.schneier.com/blog/archives/2022/12/recovering-smartphone-voice-from-the-accelerometer.html/#comment-414772)

If you guys want a *REAL* treat, check out:

**Air-Gap Research Page**

<https://cyber.bgu.ac.il/advanced-cyber/airgap>

By Dr. Mordechai Guri
Cyber-Security Research Center
Ben-Gurion University of the Negev, Israel

This page is dedicated to air-gap jumping research

Matt •
[December 30, 2022 8:06 PM](https://www.schneier.com/blog/archives/2022/12/recovering-smartphone-voice-from-the-accelerometer.html/#comment-414773)

It’s important to discuss this in the context of existing mitigations in Android. There are new restrictions for sampling motion at 200 Hz and older restrictions (Android 9 and later) on apps running in the background.

The suggestion at the end of the paper that “smartphone manufac...