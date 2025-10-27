---
title: Recovering Passwords by Measuring Residual Heat
url: https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html
source: Instapaper: Unread
date: 2022-10-14
fetch_date: 2025-10-03T19:53:45.511800
---

# Recovering Passwords by Measuring Residual Heat

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

## Recovering Passwords by Measuring Residual Heat

Researchers have used thermal cameras and ML guessing techniques to [recover passwords](https://dl.acm.org/doi/pdf/10.1145/3563693) from measuring the residual heat left by fingers on keyboards. From the abstract:

> We detail the implementation of ThermoSecure and make a dataset of 1,500 thermal images of keyboards with heat traces resulting from input publicly available. Our first study shows that ThermoSecure successfully attacks 6-symbol, 8-symbol, 12-symbol, and 16-symbol passwords with an average accuracy of 92%, 80%, 71%, and 55% respectively, and even higher accuracy when thermal images are taken within 30 seconds. We found that typing behavior significantly impacts vulnerability to thermal attacks, where hunt-and-peck typists are more vulnerable than fast typists (92% vs 83% thermal attack success if performed within 30 seconds). The second study showed that the keycaps material has a statistically significant effect on the effectiveness of thermal attacks: ABS keycaps retain the thermal trace of users presses for a longer period of time, making them more vulnerable to thermal attacks, with a 52% average attack accuracy compared to 14% for keyboards with PBT keycaps.

“ABS” is Acrylonitrile Butadiene Styrene, which some keys are made of. Others are made of Polybutylene Terephthalate (PBT). PBT keys are less vulnerable.

But, honestly, if someone can train a camera at your keyboard, you have bigger problems.

News [article](https://news.yahoo.com/heat-fingertips-used-crack-passwords-102357016.html).

Tags: [cameras](https://www.schneier.com/tag/cameras/), [computer security](https://www.schneier.com/tag/computer-security/), [machine learning](https://www.schneier.com/tag/machine-learning/), [passwords](https://www.schneier.com/tag/passwords/)

[Posted on October 12, 2022 at 6:30 AM](https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html) •
[22 Comments](https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html#comments)

### Comments

Sam •
[October 12, 2022 6:49 AM](https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html/#comment-410943)

Can this be used on ATM to get the PIN of the last user?

Austin •
[October 12, 2022 6:51 AM](https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html/#comment-410944)

“But, honestly, if someone can train a camera at your keyboard, you have bigger problems.”

Bilateralrope •
[October 12, 2022 7:29 AM](https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html/#comment-410946)

> if someone can train a camera at your keyboard, you have bigger problems.

Sure. But getting a single photo of it seems easier than getting video.

Bilateralrope •
[October 12, 2022 7:35 AM](https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html/#comment-410947)

I wonder if it’s possible to design the cooling within a laptop to interfere with this attack. Though that probably will come with tradeoffs in comfort and battery life

Clive Robinson •
[October 12, 2022 8:15 AM](https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html/#comment-410951)

@ Sam, ALL,

Re : Where your finger has been.

> “Can this be used on ATM to get the PIN of the last user?”

Long answer short, “Yes”.

Long answer, “It’s a question of energy transfer”.

That is,

1, between your finger and the surface material of the key.
2,The key to the environment it’s in.

@ Bilateralrope,

> “I wonder if it’s possible to design the cooling within a laptop to interfere with this attack. “

The ability for an IR / Thermal imager to be of use depends on,

1, The energy difference
2, The speed of trabsmission.

Importantly remember thermal energy only moves “one way” from hot to cold so the main environment would have to be less than the surface temprature of the persons finger. And any electronics to do this would need to be active and fast with a feedback mechanism to acount for peoples disparate finger tip tempratures.

Thus a low mass metallic key cap –say etched copper– in an environment near but below skin temprature will provide the least imagable surface difference.

Whilst it sounds hard, remember harder thetmal control at a much more rapid speed is done in ink-jet printers.

@ ALL,

This is not new information it’s been known and discussed for oh a couple of decades or more. I came across it originally with digital locks for security doors where the equivalent of a telescope and thermal imager were demonstrated as being able to read key touches from wall mountd digital lock pannels mounted at average shoulder hight. Either during or imediately after the employee had typed in or gone through the door.

It was one of the reasons for the development of those LED digital displays behind a transparent keyboard, where the digits were “supppsedly” randomly displayed…

Only in some –like we’ve heard about gambling machines– somebody thought using a “Linear Feedback Shift Register”(LFSR) was “A OK” which it was not…

Neill •
[October 12, 2022 9:40 AM](https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html/#comment-410954)

Given the recent events and the high viral loads – physical and virtual – I am very inclined to wear gloves everywhere I go. Should result in less heat transfer.

Ted •
[October 12, 2022 9:41 AM](https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html/#comment-410955)

One cool thing the researchers note is that thermal cameras have come down in price. Mind you, this could also make thermal-based attacks more ubiquitous.

Here’s a thermal camera you can attach to your smartphone.

<https://www.flir.com/flir-one/>

(The company, Teledyne FLIR, notes the cameras could be useful for electricians, mechanical inspectors, automotive technicians, and HVAC professionals.)

You can see how the use of ML would make an attack like ThermoSecure more fruitful. The design setup is an interesting compilation of processing and analyses.

Bilateralrope •
[October 12, 2022 10:11 AM](https://www.schneier.com/blog/archives/2022/10/recovering-passwords-by-measuring-residual-heat.html/#comment-410957)

@Clive Robinson

I was actually thinking of something that moved the waste heat from the laptops CPU, and other internal components, to the keyboard keys.

Since that waste heat depends on how much load the CPU/GPU is under, that means the equilibrium temperature the keys reach can vary with load. That seems like a confounding factor. We are probably looking at different equilibrium temperatures for each key for a given load, requiring the attacker to know how that laptops coolin...