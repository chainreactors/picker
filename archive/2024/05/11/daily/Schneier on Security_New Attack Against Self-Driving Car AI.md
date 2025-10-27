---
title: New Attack Against Self-Driving Car AI
url: https://www.schneier.com/blog/archives/2024/05/new-attack-against-self-driving-car-ai.html
source: Schneier on Security
date: 2024-05-11
fetch_date: 2025-10-06T17:18:05.649223
---

# New Attack Against Self-Driving Car AI

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

## New Attack Against Self-Driving Car AI

This is another attack that convinces the AI to [ignore road signs](https://www.theregister.com/2024/05/10/baidu_apollo_hack/):

> Due to the way CMOS cameras operate, rapidly changing light from fast flashing diodes can be used to vary the color. For example, the shade of red on a stop sign could look different on each line depending on the time between the diode flash and the line capture.
>
> The result is the camera capturing an image full of lines that don’t quite match each other. The information is cropped and sent to the classifier, usually based on deep neural networks, for interpretation. Because it’s full of lines that don’t match, the classifier doesn’t recognize the image as a traffic sign.
>
> So far, all of this has been demonstrated before.
>
> Yet these researchers not only executed on the distortion of light, they did it repeatedly, elongating the length of the interference. This meant an unrecognizable image wasn’t just a single anomaly among many accurate images, but rather a constant unrecognizable image the classifier couldn’t assess, and a serious security concern.
>
> […]
>
> The researchers developed two versions of a stable attack. The first was GhostStripe1, which is not targeted and does not require access to the vehicle, we’re told. It employs a vehicle tracker to monitor the victim’s real-time location and dynamically adjust the LED flickering accordingly.
>
> GhostStripe2 is targeted and does require access to the vehicle, which could perhaps be covertly done by a hacker while the vehicle is undergoing maintenance. It involves placing a transducer on the power wire of the camera to detect framing moments and refine timing control.

Research [paper](https://tanrui.github.io/pub/GhostStripe-MobiSys.pdf).

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [AI](https://www.schneier.com/tag/ai/), [cars](https://www.schneier.com/tag/cars/), [cyberattack](https://www.schneier.com/tag/cyberattack/), [side-channel attacks](https://www.schneier.com/tag/side-channel-attacks/)

[Posted on May 10, 2024 at 12:01 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-against-self-driving-car-ai.html) •
[5 Comments](https://www.schneier.com/blog/archives/2024/05/new-attack-against-self-driving-car-ai.html#comments)

### Comments

Wannabe Techguy •
[May 10, 2024 12:23 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-against-self-driving-car-ai.html/#comment-436586)

Self driving cars; what could possibly go wrong?

Brian •
[May 10, 2024 12:54 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-against-self-driving-car-ai.html/#comment-436587)

Rather than leave evidence in the area (the fast flashing diodes), one could simply remove the stop sign at the expense of losing some targeting capability. As a potential bonus, this attack may also be effective on non-self-driving cars.

Echo of past arising •
[May 10, 2024 2:40 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-against-self-driving-car-ai.html/#comment-436591)

@ALL

With regards the article extract opening

“Due to the way CMOS cameras operate, rapidly changing light from fast flashing diodes can be used to vary the color.”

People might not realise the same thing happens with human eyes, and has been known about by experimental researchers for getting on for a couple of centuries now.

Children in early school science often get shown a spinning top that has equal quantities of the three primary colors (RGB). When spun sufficiently fast the colors become “white”.

Using tops with different quantities of primary colors the eye will see other colors. Most teachers hope the children do not notice the absence of “Brown”. Which arguably is not a colour as it does not appear in the color spectrum as a frequency but as an intensity difference in the orange spectrum with regards other colours.

But also not talked about is what you see when the color wheels are spun at slow speeds, the human eye will see different colors and you get similar effects to those “Color Blind” tests.

The same principle of operation is how many TV and Video displays work however you can use the inverses of “missing colors” you will hear referred to as CMYK.

The speed of such displays is kept deliberately high to avoid “headaches” and worse in people.

JonKnowsNothing •
[May 10, 2024 6:48 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-against-self-driving-car-ai.html/#comment-436602)

@Brian, ALL

re:  *one could simply remove the stop sign*

(USA) removing, altering or impairing official County, City, State or Federal road signage is a serious offense. Depending on circumstances, damage and any accidents resulting from removing or altering the sign can, and has in the past, led to serious legal and criminal actions.

vas pup •
[May 11, 2024 4:15 PM](https://www.schneier.com/blog/archives/2024/05/new-attack-against-self-driving-car-ai.html/#comment-436668)

Israeli developer of VR drone system used by IDF in Hamas war raises $40m

“Tel Aviv startup Xtend, a developer of a human-guided AI drone and robots
operating system that was tested and deployed by the Israeli army in a dense
urban battlefield during the ongoing war with the Hamas terror group in the Gaza Strip, has raised $40 million in fresh capital in a private funding round.

> The startup’s technology is helping soldiers perform complex and dangerous
> combat missions such as scanning tunnels and remote buildings for terrorists and explosives, or launching grenades, without having to risk their lives.

“Our core vision is to literally save lives by sending a drone or a robot instead of a soldier into the battlefield,” Xtend co-founder Matteo Shapira told The Times of Israel. “It is happening but not on a very massive scale.”

“We are not seeing entire war scenarios where the soldiers are back at the command center and everything is being done by robots, but we are seeing that for critical mission activities robots are being sent in first,” he added.

The technology behind the startup’s human-guided drone operating system was
initially developed to help the Israeli army shoot down incendiary balloons on the border with Gaza.

> Xtend has built a human-guided autonomous operating system utilizing AI that it says enables users, even without any experience, to fly a drone or navigate
> robots to perform accurate maneuvers in any scenario, indoors and outdoors, without relying on GPS, and with minimal training.
>
> The mobile, lightweight system uses virtual reality and sensor fusion
> technologies and allows for multiple robotic devices, from drones to
> quadcopters to be deployed in parallel using a seamless interface. Before the outbreak of the Hamas war, Xtend’s biggest client was the US Department of Defense, Shapira said.

Shapira said that the newly raised capital will...