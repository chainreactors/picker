---
title: CSPT the Eval Villain Way!
url: https://blog.doyensec.com/2024/12/03/cspt-with-eval-villain.html
source: Over Security - Cybersecurity news aggregator
date: 2024-12-04
fetch_date: 2025-10-06T19:40:49.788938
---

# CSPT the Eval Villain Way!

[

](https://doyensec.com/img/home-video.mp4)

[![](/public/images/doyensec-logo.svg)](/index.html)

[![](/public/images/logo.svg)](/index.html)

#### ABOUT US

We are [**security engineers**](https://doyensec.com) who break bits and tell stories.

Visit us
[doyensec.com](https://doyensec.com)

Follow us
[@doyensec](https://twitter.com/doyensec)

Engage us
info@doyensec.com

#### Blog Archive

* 2025
* 2024
* 2023
* 2022
* 2021
* 2020
* 2019
* 2018
* 2017

© 2025 [Doyensec LLC](https://doyensec.com) [![](/public/images/rss.png)](/atom.xml "RSS")

# CSPT the Eval Villain Way!

03 Dec 2024 - Posted by Dennis Goodlett

Doyensecâs Maxence Schmitt recently built a
[playground](https://github.com/doyensec/CSPTPlayground) to go with his
[CSPT research](https://blog.doyensec.com/2024/07/02/cspt2csrf.html). In this blog post, we will demonstrate how to find and exploit CSPT bugs with Eval Villain. For this purpose, we will leverage the second challenge of Maxenceâs playground.

# A step-by-step intro to CSPT with Eval Villain

The next image shows what this methodology yields.

![Eval Villain shows CSPT inital and secondary CSPT sinks](../../../public/images/cspt_with_ev_1.png)

Weâve added some boxes and arrows in orange to better illustrate the current situation. First,
Eval Villain saw that part of the pageâs path is being used in a `fetch` request.
There, you can plainly see the `asdf%2f..` was being URL decoded. Or if you prefer, you can expanded
the âEncoder functionâ group to check. Either way, Eval Villain had discovered the CSPT sink.

The second square is on top of a debug statement from `evSourcer`. This was
where the response from the first `fetch` was being added to Eval Villainâs
source bank. As a result, Eval Villain warned us that the `_id` parameter from
the CSPT response had hit another `fetch` sink. Again, you could get a bit more
details from the âEncoder functionâ.

From the `arg[2/2]` of each `fetch` we learned more. The first `fetch` is a `GET`
that had `"redirect":"follow"` and the second had `"method":"POST"`. So we
controlled the path of a client-side `GET` request and an open redirect could have sent
that request to our own server. The response of our own server would have then been
used in the path of an authenticated `POST` request. This one image shows the
entire exploit chain for a CSPT2CSRF exploit.

All of this instrumentation stays around to help us with our exploit. Clicking
the provided solution we see the following image. This shows exactly how the
exploit works.

![Eval Villain shows an intended CSPT2CSRF solution](../../../public/images/cspt_with_ev_2.png)

# Building the picture yourself

## Step 0: Tools

You will need Firefox with [Eval
Villain](https://addons.mozilla.org/en-US/firefox/addon/eval-villain/)
installed.

Youâll also need the [CSPT playground](https://github.com/doyensec/CSPTPlayground),
which runs in Docker via `docker compose up`. This should bring up a vulnerable
web app on `http://127.0.0.1:3000/`. Read the `README.md` for more info.

We really do recommend trying this out in the playground. CSPT is one of those
bugs that seems easy when you read about it in a blog but feels daunting when you run
into it on a test.

## Step 1: Finding a CSPT

Log into the playground and visit the âCSPT2CSRF : GET to POST Sinkâ page. Open
the console with `ctrl+shift+i` on Linux or `cmd+option+i` on Mac. Ensure Eval
Villain is turned on. With the default configuration of Eval Villain, you
should just see `[EV] Functions hooked for http://127.0.0.1:3000` in the
console.

In a real test though, we would see that there is obviously a parameter in the URL
path. Eval Villain does not use the path as a source by default, due to false
positives. So lets turn on âPath searchâ in the âEnable/Disableâ pop-up menu
(click the Eval Villain logo).

Now, after a page refresh, Eval Villain will tells us about two calls to `fetch`,
each using the path. We donât know if they are CSPT yet, we need to check if
`../` is accepted, but it looks hopeful.

![Eval Villain a finding potential CSPT via Path Search](../../../public/images/cspt_with_ev_3.png)

Note: You may only see one `fetch` here, that is ok.

## Step 2 Testing For CSPT

To test for actual CSPT, just add the string `%2fasdf%2f..` to the end of the
path. This is a good tip, since this will normalize to the original path, the
website will act the same if itâs vulnerable. When you refresh the page you
will see this in the console.

![Eval Villain verifying a CSPT primitive](../../../public/images/cspt_with_ev_4.png)

Itâs that easy to find a CSPT primitive. Had the source been in `window.name` or a
URL parameter, Eval Villain would likely have found it right away.

Since the URL path was encoded, Eval Villain gives us an encoder function. You
can paste that into your console and use it to try new payloads quickly. The
function will automatically apply URL encoding.

With a CSPT primitive, the next step toward exploitation is learning how the
response of this request is used. For that, we want to ingest the response as a
new source for Eval Villain.

## Step 3 Enable `evSourcer`

First you need to enable the `evSourcer` global in Eval Villain. Go to the
configuration page from the pop-up menu and scroll to the globals table. Enable
the row that says âevSourcerâ. Donât forget to click save.

![Enabling evSourcer in Configuration page](../../../public/images/cspt_with_ev_5.png)

Now you can refresh the page and just run `evSourcer.toString()` in the console
to verify the configuration change took.

![evSourcer.toString()](../../../public/images/cspt_with_ev_6.png)

You can run a quick test to try out the feature. Anything that goes into the
second parameter of this function will be put into the Eval Villain source
bank. Before using `evSinker` the string `foobar` does not generate a warning
from the `eval` sink, afterward it does.

![evSourcer example](../../../public/images/cspt_with_ev_7.png)

## Step 4: Getting the response of the CSPT request into `evSourcer`

So, if we put the response of the CSPT request into `evSourcer`, Eval Villain
can tell us if it hits `eval`, `.innerHTML`, `fetch` or any other sink we have
hooked.

To find the response to the CSPT request, we just look at the stack trace Eval
Villain gave us.

![Stack trace from CSPT sink](../../../public/images/cspt_with_ev_8.png)

Here we have highlighted what we think of as the âmagic zoneâ. When you see
function names go from minified garbage, to big readable strings, that is where
you typically want to start. That often means a transition from library code to
developer written code, either forward or back. One of those two functions are
probably what we want. Based on context, `fetchNoteById` is probably returning the
info to `Ko`. So go to the `Ko` function in the debugger by clicking the link
next to it. Once you get there, beautify the code by clicking the `{}` icon in
the lower left of the code pane.

You will see some code like this:

```
      return (0, t.useEffect) (
        (
          () => {
            r &&
            ot.fetchNoteById(r).then((e => { // <-- fetchNoteById call here
              ot.seenNote(e._id),         // <-- so `e` is probably our JSON response
              n(e)
            })).catch((e => {
              //...
```

`fetchNoteById` apparently returns a promise. This makes sense,
so we would normally set a breakpoint in order to inspect `e` and compare it with
the response from `fetch`. Once you validate it, itâs time to instrument.

Right-click on the line number that contains `ot.seenNote` and click âAdd
Conditional breakpointâ. Add in the `evSinker` call, using a name you can
recognize as injecting the `e` variable. The `evSinker` function always returns
`false` so we will never actually hit this breakpoint.

![Adding response with evSourcer using a conditional breakpoint](../../../public/images/cspt_with_ev_9.png)

Notice we ...