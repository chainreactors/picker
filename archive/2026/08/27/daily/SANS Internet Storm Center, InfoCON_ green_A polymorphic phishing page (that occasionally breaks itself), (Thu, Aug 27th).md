---
title: A polymorphic phishing page (that occasionally breaks itself), (Thu, Aug 27th)
url: https://isc.sans.edu/diary/rss/33290
source: SANS Internet Storm Center, InfoCON: green
date: 2026-08-27
fetch_date: 2026-08-28T13:37:53.586517
---

# A polymorphic phishing page (that occasionally breaks itself), (Thu, Aug 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Xavier Mertens](/handler_list.html#xavier-mertens "Xavier Mertens")

Threat Level: [green](/infocon.html)

* [previous](/diary/33284)
* [next](/diary/33292)

Click HERE to learn more about classes Jan is teaching for SANS

# [A polymorphic phishing page (that occasionally breaks itself)](/forums/diary/A%2Bpolymorphic%2Bphishing%2Bpage%2Bthat%2Boccasionally%2Bbreaks%2Bitself/33290/)

**Published**: 2026-08-27. **Last Updated**: 2026-08-27 09:57:28 UTC
**by** [Jan Kopriva](/handler_list.html#jan-kopriva) (Version: 1)

[0 comment(s)](/diary/A%2Bpolymorphic%2Bphishing%2Bpage%2Bthat%2Boccasionally%2Bbreaks%2Bitself/33290/#comments)

As I’ve mentioned before in some of my diaries, from time to time, I like to go over phishing messages that get caught in my various spam traps or sent to us here at the Internet Storm Center.

![](https://isc.sans.edu/diaryimages/images/26-08-27-page.png)

After looking at enough phishing messages, one quickly gets used to seeing the same lures, the same credential-harvesting pages and, quite often, the same obfuscation techniques over and over again. But even something that seems to be “run-of-the-mill” at first glance can sometimes turn out to be quite interesting.

One such message was recently sent to our handler inbox, and as you can see, there was very little about it that would indicate that it would be worth a deeper look.

[![](https://isc.sans.edu/diaryimages/images/26-08-27-phishing.png)](https://isc.sans.edu/diaryimages/images/26-08-27-phishing.png)

The link in the message pointed to a URL with the following, quite usual, structure:

```

hxxps[:]//addresses[.]performs[.]vu/communications.html?good=[recipient_address]
```

Nevertheless, what happened after the link was opened was somewhat less usual.

Instead of displaying a phishing page, the browser remained effectively stuck for about 30 seconds, while utilization of one CPU core in the virtual machine I was using quickly rose to 100 %. Since retrieving the HTML source itself was almost instantaneous, it seemed clear that the delay wasn't caused by the server, and instead something in the page itself was preventing the browser from finishing its work.

Although a quick look at the source code showed that almost all of the page consisted of heavily obfuscated JavaScript, the reason for the unusual behavior fortunately wasn't too difficult to identify.

Among other things, the script contained two functions, which are slightly reformatted here for easier readability:

```

function _il(m) {
    for(k=0; 64>k; k++) {
        m[_lV(_ie(),k)]=k
    }
    return m
}

function _YF(m,h) {
    var v="";
    for(k=m; k<=h; k++) {
        v=v+String.fromCharCode(k)
    }
    return v
}
```

As you can see, both functions use k as a counter in their for loops. The first function is part of a decoding routine, and its loop counter is expected to go from 0 to 63. The second function is a helper used by the same routine to construct strings from ranges of character codes – it is used (among other places) in the \_ie() function, which is called by the first function. The problem is that k isn't declared locally in either one of these functions.

This becomes important because \_ie(), which is called during every iteration of the first loop, uses \_YF() several times to construct the Base64 alphabet. Its final call is \_YF(47,47), which produces the ‘/’ character (ASCII code 47).

Since the counter k used by \_YF() is global, this final call also changes the value of k used by the outer loop. \_YF(47,47) first sets k to 47, executes its loop once and then increments k to 48. At that point, the condition k <= 47 is no longer true, so \_YF() returns with the global value of k left at 48.

Control then returns to the outer for loop, whose own increment changes k from 48 to 49. Since 49 is still smaller than 64, another iteration starts and \_ie() is called again. Its final \_YF(47,47) call once more leaves k at 48. The outer loop therefore never progresses beyond 49.

The resulting sequence therefore looks roughly like this:

```

48 -> 49
48 -> 49
48 -> 49
...
```

This explained both why the page never rendered and why the browser was keeping one CPU core rather busy.

Changing the inner routine to use its own local counter was sufficient to let the decoding process finish. After removing the remaining layers of obfuscation, what emerged was an otherwise completely unremarkable credential-stealing page.

[![](https://isc.sans.edu/diaryimages/images/26-08-27-page.png)](https://isc.sans.edu/diaryimages/images/26-08-27-page.png)

At this point, the most likely explanation seemed fairly straightforward – the authors of the page had simply shot themselves in the foot by using a broken obfuscation mechanism.

Nevertheless, this proved not to be the case, since when I accessed the original URL again a little later, the page loaded normally. Another attempt to load the page was also successful, as were several subsequent ones.

More interestingly, while all of the resulting pages ultimately displayed the same credential-stealing form, their source code wasn't the same.

Function and variable names differed across page loads, functions appeared in a different order, numerical constants were expressed using different arithmetic operations and a large encoded block of code, which contained the actual payload with the form, changed as well. Even the innocuous-looking page title varied between requests using words like "Solution", "Viewer", "Credentials", "Private" and "Authenticate".

It therefore appeared that the first response wasn't a permanently broken copy of the phishing page at all. Rather, the server seemed to generate polymorphic variants of the page and I had simply happened to receive a “broken” one when I first accessed the target URL.

To test this hypothesis, I used a simple script to retrieve the same URL 50 times and, with some help from an LLM, compared the resulting samples.

Among the 50 samples (which all had different SHA-256 hashes), there were 21 different page titles, and, more importantly, 49 deobfuscated successfully while one became stuck in an endless loop – just like the first page I had the luck to land on.

The reason was effectively identical to what happened in the first page I encountered. In this variant, the two relevant functions had different randomized names, but both of their loops had once again been assigned the same undeclared variable k. The inner loop therefore repeatedly reset the value used by the outer one and prevented the decoder from completing.

Once this collision was corrected, the sample decoded normally as well.

The polymorphism wasn't limited to the initial JavaScript wrapper. The 50 page variants (if we include the one I had to manually “fix”) produced 50 different versions of the final phishing HTML. Form and input names, CSS classes, element identifiers and parameters used when loading images were changed, as was the placement of zero-width characters inside visible strings, which were used as a further obfuscation/anti-analysis mechanism. In spite of all these changes, however, the page presented to the user and its basic functionality remained essentially identical.

Polymorphic phishing pages are, of course, not new. The concept has been discussed for well over a decade in academic circles[[1](https://link.springer.com/chapter/10.1007/978-3-642-02617-1_28)], and phishing pages which generate random HTML attribute values for individual visits have been used in the wild for years[[2](https://www.zscaler.com/blogs/security-research/evolution-phishing-kits)]. It has also previously been shown that JavaScript lends itself quite well to producing multiple versions of source code which look different while performing the same task[[3](https://www.akamai.com/blog/security/the-tale-of-double-javascript-obfuscated-scam)] (which is the ba...