---
title: Three important steps in my maturation process
url: http://addxorrol.blogspot.com/2026/08/three-important-steps-in-my-maturation.html
source: ADD / XOR / ROL
date: 2026-08-21
fetch_date: 2026-08-22T02:51:07.316446
---

# Three important steps in my maturation process

# [ADD / XOR / ROL](http://addxorrol.blogspot.com/)

A blog about reverse engineering, mathematics, politics, economics and more ...

## Friday, August 21, 2026

### Three important steps in my maturation process

My father passed recently, and he was twice my age. I am approximately the same age that he was when I was born, and I am now "the old generation" - there's no one left in the generation above me.

At the same time, I recently joined a company that skews younger-than-me. When I joined Google in 2011, I had just turned 30, and was in the mainstream demographics of Google in 2011. There were a bunch of more senior folks, with the very senior ones being in their 50s and having completed stints at Bell Labs. I admired a lot of these "greybeards" (even though this is a sexist term - what's the right female equivalent? There were a few very senior female engineers that I would love to include).

So perhaps it is natural that I am reflecting on "what were the important realizations that I made since my early 20s that had a profound impact on the way I think about the world"? In some sense: What are the insights I had that made me "more mature", for some positive definition of "mature"?

This post tries to list them.

**1. The importance of understanding your own incentive structure, and not believing everything you think.**

I recently wrote a Twitter thread about the topic. Oppenheimer was very publicly guilt-ridden about the creation of the nuclear bomb, and von Neumann at some point quipped "some people profess guilt to claim credit for sin". In my young years, particularly in situations when I had 0day that nobody else had, I agonized about the responsibility that comes with having 0day. Should I fix them? Should I use them for good? Will the world be harmed this way? Or that way?

In the end, it turns out that - while individuals matter - many ideas have a "time at which they are ripe", and the actions of the individual matter less than the individual thinks in that moment. There is also almost no way to predict the ways in which what you do impacts the broader world.

If you were asked: "Would it be good if this 0day was used to apprehend a terrorist?" you would probably say "this is good". If you were asked "would it be good if this 0day is used to arrest someone and then torture and waterboard him 183 times?", you would probably say "this is bad". So if your 0day was used to capture KSM, it is probably good? Or bad? Things get very complicated very quickly.

Is closing 0days good for society, because it makes everything safer? Or is it enabling oppression, because buggy systems are easier to bypass?

There are no good answers, and your own incentive structure will greatly influence how you choose your beliefs. In the end, people want to be the heroes of their own story, and at the same time they have basal needs for recognition, for material goods, etc. - so they will try to construct a narrative that allows them to satisfy their basal needs while also remaining the hero of their saga.

Anxiety about the impact of your work is self-flattering, and you have to recognize it as such, and keep it in check - it's sugar for your ego, but history will largely route around you, because while individual decisions matter in specific situations, the overall flow of history is less sensitive to the individual than the individual thinks. The broader lesson, though, is: Do not believe everything you think. Examine your own incentive structures carefully. Ask yourself what alternative narratives for your behavior and beliefs could be, especially if they contradict the narrative of the heroic saga you're constructing for yourself. Carefully weighing the question "how might I be the villain in this story?" is an important and valuable skill.

Similarly, meta-cognition - just observing your own thoughts in a detached manner, and then being able to interpret, analyze, and contextualize them with regards to your own incentive structures, is a great skill to cultivate.

**2. Monocausal determinism is an illusion, and largely does not exist outside of computer debugging.**

The monocausal determinism that young computer enthusiasts get used to is an illusion that generations of electrical and process engineers spent their lives perfecting and maintaining. It is because of these engineers that computer scientists could largely get away without probabilities or any empirical grounding in the past. There is an argument that you have so many natural scientists that crossed over into AI because CS education was for a long time too focused on reasoning within the deterministic monocausal illusion.

The reality is: Computing machines are physical devices, which includes wear & tear, differences in quality between items, and "probabilistically deterministic behavior", e.g. it'll appear deterministic most of the time if not shaken too much. If pushed a bit - be it temperature, voltage, electromagnetic fields, or even rapid memory accesses to adjacent DRAM rows - determinism has a tendency to go out of the window, the illusion collapses, and we're dealing with a very different beast.

FWIW - this also makes me wonder about model alignment, because even a perfectly aligned model will be subject to random bit flips in inference, and it's hard for me to imagine that you can maintain any reasonable guarantees in the presence of bit flips to inopportune values at inopportune times.

The real world is one where very few things that happen have a single reason, and very few truly deterministic transmission mechanisms. Everything is probabilistic, and everything is multicausal.

Measurement noise is real, experiment design is difficult.

Interestingly, if you think about this carefully, you also realize that the scientific method is a classifier that is *intentionally biased against accepting something as true* - so that we only accept things as true that are beyond any reasonable doubt true.

A somewhat fascinating corolary of this is that there exists a large class of true things that will never be scientifically shown as true.

**3. The dichotomy between reason and emotion is a cultural construct, and neither grounded in neuroscience nor in logic.**

With some digging, it turns out that the western belief that reason and emotion are two ends of a spectrum is a purely cultural construct, as is the belief that "higher-order" reason needs to reign in "basal" emotions, or that "emotions" intrude on "rationality".

In most non-western cultures, achieving integration between rational deliberation and impulses and emotions is more common, and it turns out that this is much closer to the biological reality.

From a neuroscience perspective, it is clear that emotional valuation is part of a larger decision-making machinery that tends to not function properly if the emotional valuation component is damaged or removed. There is also a large component where things that your brain struggles to articulate verbally are transmitted via emotions, as well as actual feedback from your sensory organs in your body. Fun trivia: Your gut's enteric nervous system contains as many neurons as the entire cerebral cortex of a dog. Your body also forward-deploys neurons in your muscles and extremities, as a form of latency optimization. Your body is feeding you extra information, and most of this shows up in the shape of emotions.

Which brings us to the logical argument why attempting to "remove" emotions from decision-making is a bad idea: Clearly, having the ability of leveraging more information for decision-making will improve the quality of decisions. Attempting to eliminate a particular source of information almost certainly makes the quality of your decisions worse.

This is not to say one should act on impulse alone, but it is certain that integrating the full spectrum of information - which includes emotions - in your decisions is a wise idea.

I am sure that if I think more carefully, I will...