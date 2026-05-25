---
title: The Last Renaissance Man
url: https://jonlu.ca/posts/the-last-renaissance-man
source: JonLuca's Blog
date: 2026-05-24
fetch_date: 2026-05-25T06:17:50.715256
---

# The Last Renaissance Man

[Skip to content](#main-content)

JonLuca's Blog

[Posts](/ "Posts")[About](/about "About")[Contact](/contact "Contact")[Interesting Snippets](/interesting-snippets "Interesting Snippets")

May 23, 2026

# The Last Renaissance Man

AI models may bring back the ability to combine deep expertise from every field toward a single goal.

There is a common claim that Gottfried Wilhelm Leibniz was the last person who knew everything. Not actually everything, obviously, but enough of the serious human knowledge available at the time that the phrase feels plausible. He worked on calculus, logic, philosophy, law, physics, engineering, geology, and history. The [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/leibniz/) refers to him as the last âuniversal genius.â

He lived just after Galileo, at roughly the last point in history when it was possible for one extremely smart, extremely motivated person to keep a meaningful portion of the known world in their head. Galileo could build telescopes, make observations about the planets, reason about motion, and help invent an entirely new way of doing science. Leibniz could contribute to nearly every serious intellectual field of his time.

After that, there was simply too much to know.

It is not that we stopped producing intelligent people. The frontier just split apart. To make a serious contribution to mathematics now might take decades of specializing in one narrow area of mathematics. The same is true of chemistry, biology, medicine, computer science, materials science, or engineering. A modern Leibniz can learn a lot about a lot of things, but they cannot simultaneously work at the frontier of all of them.

I think AI changes this in a pretty fundamental way. Models might be the new last renaissance man: not because they have perfectly memorized all information, but because the expertise of the smartest person in every relevant field can be applied at once toward a singular goal.

## [#](#a-geometry-problem-solved-with-number-theory) A geometry problem solved with number theory

On May 20, 2026, [OpenAI announced](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) that an internal general-purpose reasoning model had disproved a longstanding conjecture about the planar unit distance problem.

The problem is extremely easy to state. Put some number of points on a flat plane, and count how many pairs are exactly one unit apart. How densely can you arrange the points while creating as many unit-length connections as possible?

Paul Erdos first posed the problem in 1946. For decades, the prevailing belief was that square-grid-like constructions were essentially as good as it gets: the number of unit distances could grow a little faster than the number of points, but not polynomially faster. The OpenAI model produced a counterexample, showing that for infinitely many sizes there are configurations with at least `n^(1 + delta)` unit distances for a fixed positive `delta`.

What is more interesting than the statement is where the answer came from.

This is a problem in discrete geometry. You can draw it on a piece of paper and explain it to a child with a ruler. The proof, however, came from algebraic number theory. It uses richer versions of the number system behind the original grid construction, number fields with particular symmetries, class field towers, Golod-Shafarevich theory, and then lattice and geometry-of-numbers arguments to turn those abstract objects back into points in the plane.

That is a fairly absurd collection of expertise to bring to a question about dots connected by equal-length lines. It is also exactly why the result is important.

The model did not retrieve an existing solution. There was no existing solution to retrieve. It found that techniques built by people in a very different part of mathematics could be used to attack a problem that generations of geometers had thought about. External mathematicians then verified the result and wrote [companion remarks](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf) digesting and strengthening the argument.

The internet made every field searchable. It did not make it obvious that class field towers were useful for a geometry conjecture. That is the difference between having access to a library and being able to think with all the books in it at once.

## [#](#smoothing-out-the-frontier) Smoothing out the frontier

The frontier of research is currently extremely jagged. One field can have a tool that would unlock a problem in another, without anyone noticing for decades. Progress depends on a fairly random collision: someone has to be good enough at both fields, interested in the right question, at the right moment, with enough time to see the connection through.

That is what the unit distance proof illustrates. It was not that algebraic number theory suddenly appeared in 2026. The relevant techniques had been built over many years. What was missing was effectively the best discrete geometer and the best algebraic number theorist concentrating on the same simple-looking question at the same time.

This is the part that will become normal. A question in topology will not have to wait for the right insight from representation theory; biology will not have to wait for someone who also understands a new imaging method or an unexpected statistical result. Every problem can have something approximating the smartest person in each adjacent field thinking about it at once.

Consider making a better battery. A usable battery is not just an electrochemistry result. It needs a material that can be manufactured at scale, survives thousands of cycles, does not overheat, charges quickly, uses available inputs, is cost effective, and works inside an actual product. Each constraint belongs to people with different expertise, different papers, and different intuitions about what matters.

A model that can hold all of those constraints together can search for a material while already considering thermal behavior, manufacturing yield, charging systems, and supply chain constraints. It can look for the solution that is not merely publishable, but buildable. It will not make experiments or verification unnecessary, but it can dramatically change which experiments are worth running in the first place.

The result is not that every open problem immediately disappears. It is that the frontier gets smoother. Areas that were neglected because the right combination of expertise never randomly assembled around them now get the same kind of attention as the fields lucky enough to have the right person in the room.

## [#](#on-demand) On demand

Leibniz was one person. Even if he really had managed to know everything worth knowing in 1700, he could only spend his time on a small number of questions. The same is true of every exceptional expert today: their attention is scarce, and getting the right group of them together around one problem is hard.

Models are different. The same general ability can be pointed at a geometry conjecture, a battery design, a new drug candidate, a climate model, or an obscure infrastructure problem. It can be used again and again, on thousands of goals in parallel.

This does not mean that human expertise stops mattering. Someone still has to decide that a problem is important. Mathematicians had to verify the proof and understand what it teaches us. Engineers would have to test the battery, and people would have to decide whether a product should exist at all.

But there is a new participant in the process: something that can bring the relevant parts of many fields together whenever there is a goal worth aiming at.

There was a last renaissance man because human knowledge eventually became too large for one person. There may now be another one, and the strange part is that this time it will not be limited to one lifetime, one set of interests, or one probl...