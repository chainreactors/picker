---
title: Php-Internalog, Introspection Applied to 0day Research
url: https://thinkloveshare.com/hacking/php-internalog-introspection-for-0day-research/
source: Think
Love
Share
date: 2022-11-19
fetch_date: 2025-10-03T23:13:45.536940
---

# Php-Internalog, Introspection Applied to 0day Research

[Think
Love
Share](/)
[![Author Image](/img/laluka.png)](/)

[InfoSec, Code, Thoughts & Feels](/)

* [Hacking](/hacking/)
* [OffenSkill](/offenskill/)
* [Streaming](/streaming/)
* [The Rest](/the_rest/)
* [Sponso](/sponso/)
* [About](/about/)

Need a **Training**,
**Pentest**, or **Code Audit**?

Visit[OffenSkill.com](https://offenskill.com/)

© 2025 Laluka.
[Licensing](https://creativecommons.org/licenses/by-nc-sa/4.0/).

# Php-Internalog, Introspection Applied to 0day Research

Nov 18, 2022
 14 min read
[Translate](https://thinkloveshare-com.translate.goog/?_x_tr_sl=en&_x_tr_tl=fr)

 Any typos? Any ideas to suggest? Feedback appreciated!

---

This article is the transcript of a talk (FR) [@Groumpf\_](https://twitter.com/Groumpf_) and [I](https://twitter.com/thelaluka) gave for the [RumpARennes](https://twitter.com/securinsa) and [GreHack](https://twitter.com/grehack) events in 2022, kudos to the staff!

Slides: <Custom-php-Introspection-for-0-Day-Research.pdf>

---

Like previous conference-related articles, this one will sound more like a transcript than a regular “technical & in depth presentation”.

Read the slides first, their explanation will be written below.

![png-01](png-01.png)

# 1. Whoami || Whoarewe

![png-04](png-04.png)

If you’re here, you already know me. I like web 0-day research, and infosec in general. But for this specific project, I was wasting tons of time coding in C for low level needs in the core of Php. In the meantime, I really wanted to share projects with close-friends as it’s way funnier that way. Therefore, I pinged one that had the skills I needed, and the fun I was looking for: [@Groumpf\_](https://twitter.com/Groumpf_)

*Appears magically*: Hello there, I’m Groumpf, aka [maxmarsc](https://github.com/maxmarsc) or Sarumax sometimes (can’t quite decide on the pseudo). I’m mainly an audio software engineer. I like dev, audio, music, low-level dev, embedded dev, music-making embedded dev… I think you got the point. My main tools are C, C++, Python and Rust, so when Laluka offered me to help him mess with the PHP source code I thought it would be funny!

# 2. Introspection 101

![png-06](png-06.png)

Apart for the lonely time we spend under the shower thinking about ourselves, introspection is a collection of techniques to gather information about running code, like an object’s method, attributes, or execution time. Some languages have built-in features, some better than others.

> Reflection is almost the same thing but goes further. The idea of reflection is not only to gather data, but also to modify it, on the fly.

![png-07](png-07.png)

Introspection can be used in many ways, so here are a few examples to better understand what we’re speaking about.

* Debugging: Ipdb is a python interactive debugger relying heavily on python’s own introspection features like dir, type, getattr, etc.
* Optimisation: Perf is a linux tool that can be used to profile a tool by tracing its behavior, pinpointing most used functions and bottlenecks.
* Fuzzing: Burp infiltrator is a single jar file one can inject in a java backend to get information about juicy classes loaded or dangerous functions reached while fuzzing with BurpSuite.
* Dynamic Security Checks (DAST): Sqreen is a product one can use to instrument an application during its runtime to monitor for dangerous behaviors and pitfalls, it hooks functions and detects quirks while keeping an accurate vision of the context they appear in.

![png-09](png-09.png)

Long story short, what do we want?

> **Know WTF is going on inside the box**

![png-10](png-10.png)

Said in a more classy way, we want to know which (dangerous) functions are called, when, where, by whom, and the payload or parameter that reached it.

# 3. Php-Internalog & Iterations

Before we begin, on the left side is a sample php file containing some smelly code. This is not exhaustive, but good enough for a first approach to see what we’ll be able to catch as we iterate!

### V0 - ltrace, strace, LD\_PRELOAD

![png-12](png-12.png)

The first approach I had was really dummy, and I was 99% sure nothing really interesting would stand out as it’s way too low level for the type of bug we want to catch. But as it costs no time, better double check just in case!

So there we go with ltrace and strace. I omitted the attempt with LD\_PRELOAD as this was slightly better, but was suffering the same issues.

![png-13](png-13.png)

And as expected, we’re getting low level debug information. It’s not “nothing” as we’re already able to catch file reads, listing, writing, socket calls, library calls, and so on. But for logic bugs, or higher level issues, it’s a dead-end.

![png-14](png-14.png)

*Self explanatory slide noise*

It’s fast at setup time and runtime, but it’s not showing us what we need. Next!

### V1 - Fork php-7.4, UDP client, netcat

![png-15](png-15.png)

The idea for this first real iteration was to be able to log targeted functions, by adding a custom UDP client to php, and by blasting string-formatted lines of logs that a simple netcat UDP server would print out. So I tried to figure out where would be the right place to put the UDP client within php, and the right (or dirtyest?) place seemed to be right next to the declaration of the PHP\_FUNCTION macro that is called pretty much everywhere a function lives.

![png-16](png-16.png)

Once our UDP client is in place, we still need to understand how functions work in Php, parse their arguments, format them nicely in our log-strings with snprintf (no sprintf for pwn PTSD (๏ᆺ๏υ) ), and send them out.

* Long story short 1: Functions are declared in with the PHP\_FUNCTION macro, and the macros ZEND\_PARSE\_PARAMETERS\_END and ZEND\_PARSE\_PARAMETERS\_START are kind of unstacking arguments passed through Z\_VAL objects.
* Long story short 2: Even though I wrote only a few lines of C, I might have introduced security issues and performance issues. C is hard and I don’t pretend to be good at it. M’kay?

![png-17](png-17.png)

So that’s it, it’s manual, it’s tedious, but it definitely works!

Now, how could we cover more interesting functions? How could we automate the process of hooking, parsing, formating, and sending information? How could we reach a decent speed at runtime? And how could we avoid recompiling the whole (php/zend) thing everytime we change a single char?:x

Also, hwo caw ne pverent thaerds fmro diong taht? HLEP!

You get the idea, this first iteration validates the idea, but won’t do the trick on its own.

### V2 - xDebug is all you need, but SLOW AF

![png-18](png-18.png)

The second iteration came from the idea of relying on developers tools. As demonstrated earlier, devs also use introspection a lot for profiling, troubleshooting, and debugging. In Php, xDebug is THE .so you need. It’s really easy to install, not too painful to configure, and it can both allow the use of a live debugger or automate the tracing of EVERY SINGLE FUNCTION CALL OR PHP LINE!

> This was actually not that easy to setup as the documentation is sometimes quite cryptic, and the in-between for versions 2 and 3 is a bit blurry, so it took some time to have the right rules to have a clean dump printed out at the right place, but we’re getting there!

![png-19](png-19.png)

The output can be parsed to some extent, and the given information is way more than what we need. But…

It’s SO DAMN SLOW!!!

And the overhead, oh my god. As EVERYTHING is logged, the output can be really **really** huge.

> Fun fact: I’ve had crazy issues with this one. I used to place the dumped files in /dev/shm to benefit from the writing speed this device (actually ram) offers. But while playing with Magento2, the generation of a css file with php had so many nested functions that **one single request took more than 20Go**!
> I have a 32Gb laptop. I ran the curl twice to check if this was a hiccup or a normal behavior. 20Go+20Go definitely fills my 32Go of ram, my computer froze, then crashed. Gg me.

![...