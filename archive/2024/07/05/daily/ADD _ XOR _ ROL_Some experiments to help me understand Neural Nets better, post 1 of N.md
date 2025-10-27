---
title: Some experiments to help me understand Neural Nets better, post 1 of N
url: http://addxorrol.blogspot.com/2024/07/some-experiments-to-help-me-understand.html
source: ADD / XOR / ROL
date: 2024-07-05
fetch_date: 2025-10-06T17:42:41.922796
---

# Some experiments to help me understand Neural Nets better, post 1 of N

# [ADD / XOR / ROL](http://addxorrol.blogspot.com/)

A blog about reverse engineering, mathematics, politics, economics and more ...

## Thursday, July 04, 2024

### Some experiments to help me understand Neural Nets better, post 1 of N

While I have been a sceptic of using ML and AI in adversarial (security) scenarios forever, I also quite like the fact that AI/ML has become important, if only to make me feel like my Math MSc (and abortive Math PhD) were not a waste of time.

I am a big proponent of "bottom-up" mathematics: Playing with a large number of examples to inform conjectures to be dealt with later. I tend to run through many experiments to build intuition; partly because I have crippling weaknesses when operating purely formally, partly because most of my mathematics is somewhat "geometric intuition" based -- e.g. I rely a lot on my geometric intuition for understanding problems and statements.

For a couple years I've wanted to build myself a better intuition about what deep neural networks actually "do". There are folks in the community that say "we cannot understand them", and folks that say "we believe in mechanistic interpretability, and we have found the neuron to recognize dogs"; I never found either statement to be particularly convincing.

As a result, earlier this year, I finally found time to take a pen, pencil, and wastebasket and began thinking a bit about what happens when you send data through a neural network consisting of ReLU units. Why only ReLUs? Well, my conjecture is that ReLUs are as good as anything, and they are both reasonably easy to understand and actually used in practical ML applications. They are also among the "simplest examples" to work with, and I am a big fan of trying the simple examples first.

This blog post shares some of my experiments and insights; I called it the "paper plane or origami perspective to deep learning". I subsequently found out that there are a few people that have written about these concepts under the name "[the polytope lens](https://www.lesswrong.com/posts/eDicGjD9yte6FLSie/interpreting-neural-networks-through-the-polytope-lens)", although this seems to be a fringe notion in the wider interpretability community (which I find strange, because - unsurprisingly - I am pretty convinced this is the right way to think about NNs).

Let's get started. In order to build intuition, we're going to work with a NN that is supposed to learn a function from R^2 to R - essentially learning a grayscale image. This has several advantages:

1. We can intuitively understand what the NN is learning.
2. We can simulate training error and generalisation errors by taking very high-resolution images and training on low-resolution samples.
3. We stay within the realm of low-dimensional geometry for now, which is something most of us have an intuitive understanding of. High dimensions will create all sorts of complications soon enough.

Let's begin by understanding a 2-dimensional ReLU neuron - essentially the function f(x, y) = max( ax + by + c, 0) for various values of a, b, and c.

This will look a bit like a sheet of paper with a crease in it:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrSyPkYgdbN-IjKUaNONs0Rpuy8qjUNpDnOqDfH6Lgm43GLQQPGsUJUygbos4zZ1cqZWlvQoNs6JUHRjNelkhyTKLvm1IV-Vqkzq6vU8t6kV8bt2xcpH1wthwdqilaVid_LyL8JPtZLkIgiCQKAREI6T7T8nas7_O2n9HGp01QFZKeHV-YkTXx/s320/rotate_relu.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjrSyPkYgdbN-IjKUaNONs0Rpuy8qjUNpDnOqDfH6Lgm43GLQQPGsUJUygbos4zZ1cqZWlvQoNs6JUHRjNelkhyTKLvm1IV-Vqkzq6vU8t6kV8bt2xcpH1wthwdqilaVid_LyL8JPtZLkIgiCQKAREI6T7T8nas7_O2n9HGp01QFZKeHV-YkTXx/s1000/rotate_relu.gif)

How does this function change if we vary the parameters a, b, or c? Let's begin by varying a:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfc5f4pV_J2QsTuvJXwHwIb1T6fShqsU4e3i8z8ItBid85maBmUXZQvJIVdZMs2I-N15gZE79R4ybg5AGA9NRT_yfftsOoN7Zzze1lMOrkAJ6ye0dj9dK8us04UmrswnrsF3TJYhYIVUUTkBMB6zPUpZamtIMYQbiAxInrLuTT4Ewe5sEfhP21/s320/vary_a.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgfc5f4pV_J2QsTuvJXwHwIb1T6fShqsU4e3i8z8ItBid85maBmUXZQvJIVdZMs2I-N15gZE79R4ybg5AGA9NRT_yfftsOoN7Zzze1lMOrkAJ6ye0dj9dK8us04UmrswnrsF3TJYhYIVUUTkBMB6zPUpZamtIMYQbiAxInrLuTT4Ewe5sEfhP21/s1000/vary_a.gif)

Now let's have a look at varying b:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOTXj_HIdOK5D06326I_XxNO10jYwEKUv8QG-eWPzTyLnLzozEEm_p0bmmumRH5GwVyj4z8aqfIHGei6VEMR-Pj0J8OjE_DSKmAdivFpwYxB2_XKP48Trg7KjHeZQFC7sBbyxYIgcaoMx1CqQ8ID0nG7d66xGC-Y-jRQ5eaPNkl7zFgsl2a2y2/s320/vary_b.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOTXj_HIdOK5D06326I_XxNO10jYwEKUv8QG-eWPzTyLnLzozEEm_p0bmmumRH5GwVyj4z8aqfIHGei6VEMR-Pj0J8OjE_DSKmAdivFpwYxB2_XKP48Trg7KjHeZQFC7sBbyxYIgcaoMx1CqQ8ID0nG7d66xGC-Y-jRQ5eaPNkl7zFgsl2a2y2/s1000/vary_b.gif)

And finally let's have a look at varying c:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1fOwkO2g_m1fsn9sFb5sCO8L46G4zQBP3A1Wi4ZRyk4jPk8uYi-QgkvQEjBcsknBnyj86ZKVjyh9Vd5mQXkUWeeDnfpN1HiuMzQVIfOepbhnTBW-wESSThKEdtfq36Glwty2dANxzTQVQIvyBSWirmc8nSt3XRvMP4BzNzraLfuahA2zWr7Qj/s320/vary_c.gif)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj1fOwkO2g_m1fsn9sFb5sCO8L46G4zQBP3A1Wi4ZRyk4jPk8uYi-QgkvQEjBcsknBnyj86ZKVjyh9Vd5mQXkUWeeDnfpN1HiuMzQVIfOepbhnTBW-wESSThKEdtfq36Glwty2dANxzTQVQIvyBSWirmc8nSt3XRvMP4BzNzraLfuahA2zWr7Qj/s1000/vary_c.gif)

So the parameters a, b, c really just decide "in which way" the plane should be folded / creased, and the steepness and orientation of the non-flat part. It divides the plane into halfspaces; the resulting function is 0 on one half-plane and linear (respectively affine) on the other.

As a next step, let's imagine a single-layer ReLU network that takes the (x,y) coordinates of the plane, and then feeds it into 10 different ReLU neurons, and then combines the result by summing them using individual weights.

The resulting network will have 3 parameters to learn for each neuron: a, b, and c. Each "neuron" will represent a separate copy of the plane that will then be combined (linearly, additively, with a weight) into the output function. The training process will move the "creases" in the paper around until the result approximates the desired output well.

Let's draw that process when trying to learn the picture of a circle: The original is here:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjedvBqydU2Y5cRMPz4imvTPsLmhMUSvav_jIC_DWkRlpB83mJZiwcm-0-SqMhYjnNeAbKiLgp7eKW3HhiXmCkKRbT6GP7efTDatmhI5wb_CLeOtzqu35M6LuIjWC2UHPp8Vm_ktHVO_J62Tkeh3ybTZHYqdnNyRrzmGlOqjLM6TZbS4JxqXa5W/s1600/black_circle.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjedvBqydU2Y5cRMPz4imvTPsLmhMUSvav_jIC_DWkRlpB83mJZiwcm-0-SqMhYjnNeAbKiLgp7eKW3HhiXmCkKRbT6GP7efTDatmhI5wb_CLeOtzqu35M6LuIjWC2UHPp8Vm_ktHVO_J62Tkeh3ybTZHYqdnNyRrzmGlOqjLM6TZbS4JxqXa5W/s300/black_circle.png)

This shows us how the network tries to incrementally move the creases around so that on each of the convex areas that are created by the creases, it can choose a different affine function (with the condition that on the "creases" the functions will take on the same value).

Let's do another movie, this time with a higher number of first-layer neurons - 500. And let's see how well we will end up approximating the circle.

Aside from being mesmerizing to watch, this is also kinda intriguing and raises a bunch of questions:

1. I don't understand enough about Adam as an optimizer to understand where the very visible "pulse" in the optimization process is coming from. What's going on here?
2. I am pretty surprised by the fact that so many creases end up being extremely similar -- what would cause them to bundle up into groups in the way they do? The circle is completely rotation invariant, but visually the creases seem to bunch into groups much more than random distribution would suggest. Why?
3. It's somewhat surprising how difficult it appears to b...