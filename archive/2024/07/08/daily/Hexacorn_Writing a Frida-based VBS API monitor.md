---
title: Writing a Frida-based VBS API monitor
url: https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor/
source: Hexacorn
date: 2024-07-08
fetch_date: 2025-10-06T17:40:57.053112
---

# Writing a Frida-based VBS API monitor

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2024/06/22/enter-sandbox-28-automated-access-primitives-extraction/)
[Next →](https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor-take-two/)

# Writing a Frida-based VBS API monitor

Posted on [2024-07-07](https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor/ "12:04 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

**Update**

See the updated version of the script [here](https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor-take-two/).

**Old Post**

I love experimenting with Frida and I have presented a [few](https://www.hexacorn.com/blog/2022/02/20/delphi-api-monitoring-with-frida-part-3/) [different](https://www.hexacorn.com/blog/2024/03/31/subfrida-v0-1/) API Monitoring prototypes based on this framework a few times before…

Today I will demonstrate how to write a quick & dirty VBS/VBScript (Visual Basic Script) API Monitor.

As many of you probably know, when we execute *.vbs* scripts via *cscript.exe* or *wscript.exe* the actual dirty work is done by the *vbscript.dll*. From some quick poking around inside this library I can tell that many functions available to Visual Basic Script programmers are implemented as callbacks, and these callback routines rely on a [VARIANT](https://learn.microsoft.com/en-us/windows/win32/winauto/variant-structure) structure. What it means in practice is that arguments are passed by means of using this structure, where the first field of the structure defines the type of the data being passed as an argument, followed by the actual data or offset to data. On a 64-bit version of Windows, and using the 64-bit version of *vbscript.dll*, the first field of this VARIANT structure is 8-bytes long (qword).

The below screenshot from XDBG shows an example of such structure as seen in memory:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs1_variant.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs1_variant.png)

The first qword is holding a value 8 which means it is a String. The address following this qword is the offset to the actual Unicode string.

The VARIANT types are described all over the place, and sometimes these descriptions actually vary. This is because of the migration from the 32- to 64-bit architecture, plus some of the types have evolved over time. And on top of that, this is a shared commodity — win32 APIs use it, COM methods use it, VBS uses it, VB uses it and VBA as well. It’s a bit of a mess (f.ex. type ‘2’ may be a *vbInteger* or *vbShort*, depending on where you look).

It doesn’t matter from our perspective too much as we can build a list of known values (this is not a final list!) that is good enough for our purposes:

* 0 – vbEmpty
* 1 – vbNull
* 2 – vbShort
* 3 – vbInteger
* 4 – vbSingle
* 5 – vbDouble
* 6 – vbCurrency
* 7 – vbDate
* 8 – vtString
* 9 – vbObject
* 10 – vbError
* 11 – vbBoolean
* 12 – vbVariant
* 13 – vbDataObject
* 14 – vbDecimal
* 17 – vbByte
* 17 – vbChar
* 20 – vbLong
* 36 – vbUserDefined
* 8192 – vbArray
* 16384 – vbByRef
* 16392 – vbStringByRef

Now that we know how the data is being passed to these callbacks, let’s find out where they reside inside the *vbscript.dll*.

One way to find them is to analyze the library’s disassembled code and look for popular VBS function names f.ex. *MsgBox* and see where they are being referenced, f.ex.:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs2-1024x225.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs2.png)

And yes, we can easily find a reference to *MsgBox* function inside a very large subroutine that appears to be handling all vbs functions really – with some additional analysis it is pretty clear that it is most likely the main dispatcher function. What’s also encouraging is the fact that further code analysis shows that the compiler was very nice to us – for all these string comparisons looking for vbs functions it generated code that is easy to process in a batch way. As you can see from the below snippet, if there is a string match, a pointer to the structure defining the function’s call back is always assigned to *rdi* register the same way:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs3.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs3.png)

Because of this pattern we can easily enumerate all these repetitive sequences and start generating Frida handlers!

So, we write a simple idapython script that will walk through all the chunks of the dispatcher function, find all occurrences of what looks like a function name comparison, and once these are found – we discover the offset to their callback structure, then use it to find the vbs function callback routine and then generate its generic Frida handler.

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs7.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs7.png)

Here’s the [idapython script](https://hexacorn.com/d/vbs_frida.py) that does it for you.

Note: I used a 64-bit *vbscript.dll* from Windows 10 – in my case the dispatcher function is located at 0x180014DD0 – you may need to adjust the address to your version of Windows/*vbscript.dll*.

How does it all work in practice?

I wrote a lame test vbs script that looks like this:

```
MsgBox "Find the PID of this process & run Frida-Trace now"

b = "ABCDEFGH"
a = Right(b, 1) & StrReverse ("olle") & StrReverse ("dlrow")
a = Replace(a,"world","VBS_API_Mon")
MsgBox a
MsgBox "End of the demo"
```

The first *MsgBox* is a helper function or a breakpoint of sort. Frida has problems hooking functions from libraries that are loaded dynamically (*vbscript.dll* is not statically linked to *cscript.exe*). As such, I force the *vbscript.dll* to be loaded first and this first *MsgBox* gives us time to run frida-trace on the cscript process.

In other words:

* Run *cscript.exe* *test.vbs*; let it pause on the first *MsgBox*
* Run Frida-trace with the PID of the *cscript.exe* process
* Click the OK in the Message Box – now you are monitoring all the calls

Here it is in action:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs5.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/07/vbs5.png)

We can see that basic function invocations are handled relatively well – we could extract all the strings being passed to string functions that handle actual strings. There is definitely a limitation when it comes to operators and functions not operating on strings.

The two MsgBox invocations are of special interest:

* MsgBox a — not handled well at the moment
* MsgBox “End of the demo” – handled well

It turns out that apart from the VARIANT structure there are also some other bits at play — ones that I didn’t explore yet.

It all took around 4 hours. I knew nothing about *vbscript.dll* internals prior to this exercise. The rapid prototyping power that Frida gives us cannot be understated…

This entry was posted in [Frida](https://www.hexacorn.com/blog/category/frida/), [Sandboxing](https://www.hexacorn.com/blog/category/sandboxing/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/07/07/writing-a-frida-based-vbs-api-monitor/ "Permalink to Writing a Frida-based VBS API monitor").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")