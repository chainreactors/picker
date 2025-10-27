---
title: Visualizing Colors: The Gradient Oscillation Hyperspace
url: https://buaq.net/go-251618.html
source: unSafe.sh - 不安全
date: 2024-07-21
fetch_date: 2025-10-06T17:39:17.447936
---

# Visualizing Colors: The Gradient Oscillation Hyperspace

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

Visualizing Colors: The Gradient Oscillation Hyperspace

The aim of this article is to present a colored hyperspace, in which the distance is not extracted u
*2024-7-20 21:0:16
Author: [hackernoon.com(查看原文)](/jump-251618.htm)
阅读量:8
收藏*

---

The aim of this article is to present a colored hyperspace, in which the distance is not extracted using numerical values, but by using the color’s change (or oscillation). Imagine the inside of a sphere, randomly add the seven colors of the rainbow as dots within that sphere, and then expand all of them at once and at the same rate (including the sphere).

## **Part 1: The Circle of Colors**

The seven colors of a rainbow are: red, orange, yellow, green, blue, indigo, and violet, and together, they form an infinite line of oscillating colors. We turn the seven colors into a circle through which we can loop indefinitely. To play with that circle, we can paint 25% of it black. When our loop arrives at the beginning of the black area, it immediately teleports at the end of it.

We can also paint another 25% of the circle white. When our loop arrives at the beginning of the white area, it immediately shifts its movement backward and loops in reverse until it arrives at the other beginning of the white area, where it shifts back again.

On this circle, besides the colors we placed, we could use machine learning techniques in order to allow an algorithm to patternize (or sort) opposing concepts on opposing sides. Concepts like: motion (placed up) - static (placed down), hot (placed up) - cold (placed down), change (placed left) - static (placed…down? ).

Machine learning is quite a fuzzy realm. By using context-deciphering algorithms, we aim to categorize concepts and ideas based on their opposites and place them on a spectrum of reason. And later, artificial intelligence does even fuzzier things when that spectrum of reason is used in order to output the most accurate response to the received input.

After lots and lots of training, the concepts are well-categorized and ready to use. This readiness is not a fixed result and can vary in cost, efficiency, and accuracy based on the quality of the used algorithms, the quality of the data, and maybe, the quality of the space on which the sorting is done. When it comes to the quality of the space, we can take our circle as an example and ask a few questions: Is it a flexible space?

We got the black-and-white areas that allow for something akin to dimensional traveling (skipping parts and turning the space upside down); Is it a homogeneous (the same everywhere) space?

The circle is obviously not. If we, however, take a 2D space of 7x7 tiles and fill them with colors in such a way in which, from whatever direction, to whatever alignment we look, we see the colors of the rainbow, then I suppose we got a homogeneous space (+-). In that 2D 7x7 space, we basically got 7 unfolded circles, possibly, all with their own unique sorting and concepts.

## **Part 2: The Hyperspace**

Expanding the 2D 7x7 space to a 3D 7x7x7 one, where from any place, through any row we choose to go, we pass through all the seven colors of a rainbow, we got our homogeneous 3D space. To make it flexible, we have to somehow paint some parts either black or white in order to allow for more complex traveling. Let’s imagine that we paint the middle block black.

Now, from any direction we come, we will inevitably “hit” it, and we will be forced to skip it. And maybe, we want to skip the middle only when we come from the top of the cube. How could we do that?

One, and probably the only possible way, is to separate the inside of the cubes from their borders. This way, each cube will have its own 6 borders, all accounting for either black/white/no special argument, and will allow us to guide each side in its own unique way.

Now, you may wonder why I decided to call this space a “hyperspace” rather than a regular 3D space. A hyperspace is defined in mathematics as a more than 3-dimensional space, and in science fiction, as a space that permits faster-than-light travel. Shifting these ideas to our colored computational space, we acknowledge how each “tick” of the computation takes into account a cube (or its border).

If for example, in our 7x7x7 space, we mark all the upper borders of the middle cubes as black, we instantly skip all of them. But yes, in computation we would normally require to check each and every single border to ensure that all of them are skippable. However, a certain algorithm could be run on this space after it was created, to simply check for each black, and each white border, then write on them their respective number.

For example, since all our middle cubes have blacktop borders, the lowest cube’s border will be given the number 1 as just itself is skipped at that step, the second lower cube will have written on its top border number 2, and so on up to the 7th upper border.

The algorithm tasked to check and mark each cube’s border sits in the middle between the creation of the hyperspace and its unfolding. For the creation part, let’s assume that the concepts are organized in the hyperspace in ways that somewhat allow them to be expressed linearly.

For example, if the lower slice of the space has rows that encapsulate “outside”, “cold”, “cloudy”, “weather” and so on, the “expression line” (or maybe the rational thread of the narrative) may express “outside is very cold because of the cloudy weather”, or maybe, “The cold weather outside is due to the cloudy atmosphere” (assuming that “atmosphere” is in the list of concepts).

Maybe the first expression is less “rationally expensive” simply because it follows the given concepts in a linear measure, whereas the second is more expensive, yet, clearer and more detailed. No matter the case, the point is that there is a clear tie between how the hyperspace of concepts is formed and how it is later used.

## Part 3: The Hyper-Labyrinth

Now that we know what the space looks like, let’s try to see it from the perspective of an algorithm tasked to count the repetitive borders to allow them to ultimately work. Let’s image ourselves inside a big Rubik’s cube. With each step we take, we find ourselves within a new color. Let’s say that we somehow see an area of 5x5x5 cubes around us.

Either by magic, or memory and intuition in case we are familiar with the space. We keep walking through the colors and from a point, we see in front of us a black border with the number 1000 written on it. This means that if we go forth, we will be sent 1000 blocks ahead. We stand there for a while, think about it, and then decide to go.

The place we arrived at is very similar to the one we were in before; after all, we stated that the space is homogeneous. But then, when we turn back, the cubes have no borders on that other side and so, we have to walk all those 1000 cubes one by one in order to arrive at our starting point.

After we walk 10 cubes, we turn around and see the black border with the number 10 on it. It seems that we can always reset the walkback if we find a good reason to.

Our goal however is to explore the space and see what we find within it. Where we find that certain concept, where we find its opposite, and even learn in time the pattern in which the opposing concepts are sorted and the way in which they are tied one to another.

Even if the space is organized in a more or less predictive manner, the algorithm tasked to explore it and later express itself through it may initially have no idea about what it will find there. In my view, this allows for some sort of “intuitive” exploration...