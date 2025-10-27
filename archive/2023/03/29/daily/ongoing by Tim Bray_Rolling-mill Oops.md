---
title: Rolling-mill Oops
url: https://www.tbray.org/ongoing/When/202x/2023/03/28/Rolling-Mill
source: ongoing by Tim Bray
date: 2023-03-29
fetch_date: 2025-10-04T10:58:17.857729
---

# Rolling-mill Oops

# Rolling-mill Oops

Search

*[This fragment is available in [an audio version](Rolling-Mill.mp3).]*

The world being what it is, feels like a little humor is in order. Here’s a story from my misspent youth,
when I was a co-op student at a steel mill and had a Very Bad Day.

This story was originally published as a Tweet thread in response to
[the following](https://twitter.com/ElleArmageddon/status/1255870742727585792):

[![Tweet from @ElleArmageddo](tweet.png "Tweet from @ElleArmageddo")](-big/tweet.jpg.html)

That thread will probably go down with the Twitter ship and I’d like to save it, so here goes.

During the summer of 1980, my last before graduation, I had a co-op job at
[Dofasco](https://en.wikipedia.org/wiki/Dofasco), a steel mill in Hamilton, Ontario. It wasn’t great, the tasks were
mostly make-work, although I kind of liked learning
[RSX-11M Plus](https://en.wikipedia.org/wiki/RSX-11) running on PDP-11s.
Sure, it was primitive by modern standards (I already knew V6 Unix)
but it got the job — controlling the
sampling apparatus in a basic-oxygen blast furnace — done.

So, there was this
[Rolling Mill](https://en.wikipedia.org/wiki/Rolling_%28metalworking%29) that
turned big thick non-uniform slabs of steel into smooth precise strips rolled onto a central core; this is the form in which
steel is usually bought by people who make cars or refrigerators or whatever. The factory had lots of rolling mills but this one was
special for some reason, was by itself in a big space away from the others. It was huge, the size of a couple of small trucks.

The problem was, it had started overheating and they didn’t know why. The specifications said the maximum amperage was 400A
RMS, where “RMS” stands for Root Mean Square. The idea is you sample the current every so often and square the measurements and
average the squares and take the square root of that. I believe I learned in college why this is a good idea.

Um, 400A is a whole lot of juice. Misapplied, it could turn a substantial chunk of the factory to smoking ashes.

The mill had an amperage data trap, to which they plugged in a HP “data recorder” with reel-to-reel tape that sampled every
little while, and left it
there until the overheat light started flashing. Then they needed to compute the RMS.

Fortunately ·
They had a
[PDP-11/10](https://gunkies.org/wiki/PDP-11/10), about the smallest 16-bit computer that DEC ever made, with
something like 32K of core memory. It was in a 6-foot-rack but only occupied two or three slots.
It had a device you could plug the data recorder into and read the values off the tape out
of an absolute memory address. And it had a FORTRAN compiler.
It was running
[RT-11](https://en.wikipedia.org/wiki/RT-11).

Who knew FORTRAN? Me, the snot-nosed hippie co-op student! So I wrote a program that read the data points, accumulated the
sum of squares, and computed the RMS. I seem to recall there was some sort of screen editor and the experience wasn’t terrible.
(I kind of wish I remember how you dereference an absolute memory address in FORTRAN, but I digress.) The readings were pretty
variable, between 200 and 500, which the machine specs said was expected.

Anyhow, I ran the program, which took hours, since the data recorder only had one speed, in or out.
The output showed that the RMS amperage started worryingly high but declined after a bit to well below
400A, presumably after the machine had warmed up.
My supervisor looked at the arithmetic and it was right.
The report went to the mill’s General Foreman, a God-like creature. So they told the machine operator not to worry.

Unfortunately ·
I had stored the sum of squares in a FORTRAN “REAL” variable, which in FORTRAN (at least that version) meant
32-bit floating point. Which has only 24 bits of precision.

Can you see the problem? 4002 is 160,000 and you don’t have to add up *that* many of those
before it gets big enough that new values vanish into the rounding error and make no changes to the sum. And thus the average
declines. So the RMS I reported was way low.

Fortunately ·
The mill operator was a grizzled old steel guy who could tell when several million bucks worth of molten-metal
squisher was about to self-incinerate.

He slammed it off on instinct with a steel slab halfway through. It only cost a few shifts of downtime to remediate, which is
to say many times my pathetic co-op salary for the whole summer.

At which point my boss and I had to go visit the General Foreman and explain what DOUBLE PRECISION was and why we hadn’t used
it. It wasn’t fun. For some reason, they didn’t ask me to re-run the calculations with the corrected code.

You can’t possibly imagine how terrible I felt. I was worried that my boss might have taken career damage, but I heard on
the grapevine that he was forgiven, but ribbed unmercifully for months.

And when I graduated they offered me a job. I went to work for DEC instead.

---

**Updated: 2023/03/28**

---

## Contributions

Comment feed for ongoing:[![Comments feed](/ongoing/Feed.png)](/ongoing/comments.atom)

From: [John Cowan](http://vrici.lojban.org/~cowan/) (Mar 29 2023, at 16:25)

I think it's pretty likely that the reference to the absolute address was done using an assembly-language subroutine. The RT-11 Fortran manual at <[http://bitsavers.trailing-edge.com/www.computer.museum.uq.edu.au/RT-11/DEC-11-LRFPA-A-D%20RT-11%20FORTRAN%20Compiler%20and%20Object%20Time%20System%20User's%20Manual.pdf](http://bitsavers.trailing-edge.com/www.computer.museum.uq.edu.au/RT-11/DEC-11-LRFPA-A-D%20RT-11%20FORTRAN%20Compiler%20and%20Object%20Time%20System%20User%27s%20Manual.pdf)> does not describe any PEEK analogue.

*[[link](#c1680132348.116469)]*

From: [Andrew Reilly](http://) (Mar 31 2023, at 18:05)

The thing about floating point (pre-IEEE or not) is that the exponent part makes it relative-accuracy (precision) preserving, rather than absolute. So your anecdote is real, provided that there were a \*lot\* of squares being accumulated, but the bit of set-up about the 400-ness of the numbers is a red herring. Wouldn't have mattered if it was 400, 4 or 0.4.

There are strategies for avoiding the problem, if short floats are all you've got, like sorting the numbers before adding them, or batching the adding process up, or (what I'd recommend for that sort of job:) just not add so many up at once - either window or low-pass filter the accumulation.

However, judicious use of double precision does solve many sins, and is arguably the best answer here.

Oh, and the reason that RMS is important is that it is proportional to power, and it's power that heats things up.

Big machine vs student stories are great. My favourite was a lab at Uni, where we had to learn about phase matching for generators and loads of AC systems. One student team managed to get the phase match exactly wrong (negative), and so when they threw the switch one of the half-ton machines instantly snapped all four half-inch bolts and flipped off the pedestal and rolled across the floor. Luckily no one was injured.

*[[link](#c1680311108.502692)]*

[ongoing](https://www.tbray.org/ongoing/)

[What this is](/ongoing/WhatItIs) ·
[![Subscribe to ongoing](/ongoing/Feed.png "Subscribe to ongoing")](/ongoing/ongoing.atom)
[Truth](/ongoing/Truth) ·
[Biz](/ongoing/Biz) ·
[Tech](/ongoing/Tech)

[author](/ongoing/misc/Tim) ·
[Dad](http://www.textuality.com/BillBray/)
[colophon](/ongoing/misc/Colophon) ·
[rights](/ongoing/misc/Copyright)

---

[March](/ongoing/When/202x/2023/03/) [28](/ongoing/When/202x/2023/03/28/), [2023](/ongoing/When/202x/2023/)
 · [The World](/ongoing/What/The%20World) (158 fragments)

 · · [Humor](/ongoing/What/The%20World/Humor) (24 more)

By [Tim Bray](/ongoing/misc/Tim).

The opinions expressed here
are my own, and no other party
necessarily agrees with them.

A full disclosure of my
professional interests is
on the [author](/ongoing/misc/Tim) page.

I’m on [Mastodon](https://cosocial.ca/%40timbray)!