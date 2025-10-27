---
title: Thomas Fitzsimmons: firefox-javascript-repl
url: https://www.fitzsim.org/blog/?p=669
source: Planet Classpath
date: 2023-06-08
fetch_date: 2025-10-04T11:46:51.480824
---

# Thomas Fitzsimmons: firefox-javascript-repl

[Skip to content](#content)

[fitzsim's development log](https://www.fitzsim.org/blog/)

# firefox-javascript-repl

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1) [June 6, 2023June 9, 2023](https://www.fitzsim.org/blog/?p=669)
[Leave a comment on firefox-javascript-repl](https://www.fitzsim.org/blog/?p=669#respond)

*Read-Evaluate-Print Loops are great for doing quick experiments. I recently released two new REPL packages for Emacs to GNU ELPA. This is the first in a two part series. [Here is part 2.](https://www.fitzsim.org/blog/?p=681)*

I wanted something along the lines of SLIME or CIDER’s REPL (just the REPL part) but for JavaScript. There have been many options for this over the years, MozRepl, skewer-mode, jsSlime [1](#footnote-1), and more recently dap-mode. I tried all of these existing options but all except for dap-mode are no longer maintained. The Firefox Remote Debugging Protocol has evolved over the past decade, and it has not always maintained backward compatibility. It is not meant to be an API, I guess, but more a reflection of Firefox internals.

I did try dap-mode, but I couldn’t install it on my development version of Emacs; there seemed to be Elisp compatibility problems with some of its many dependencies. It also seemed to require on the Firefox side a JavaScript extension from the repository for an unrelated proprietary IDE, which I found strange.

I just wanted a simple Emacs mode to communicate with Firefox directly, for small JavaScript experimentation. It seemed like everything was already available in Emacs and Firefox to do that.
I started with the [Mastering Emacs Comint guide](https://www.masteringemacs.org/article/comint-writing-command-interpreter), and for the Firefox side, the [geckordp](https://github.com/jpramosi/geckordp) project does a great job of documenting the Firefox Remote Debugging Protocol. Firefox needs to run in a special debug mode for the protocol to be available, so I added that logic to the new Emacs command.

The result is [`firefox-javascript-repl`](https://elpa.gnu.org/packages/firefox-javascript-repl.html), available in GNU ELPA. I tested it on GNU/Linux. I would like this to work on other operating systems too, patches accepted.

I made sure this mode works on Emacs versions 26.1 (released in 2018) and newer [2](#footnote-2). I’ve also tested on the most recent Firefox (113.0.2) and Firefox ESR (102.11.0esr). I’ll strive to keep up with changes in the Firefox Remote Debugging Protocol, to minimally keep `firefox-javascript-repl` working for the latest Firefox and Firefox ESR releases (though if the FRDP breaks compatibility, `firefox-javascript-repl` will also break compatibility with older browser versions, to avoid a large test matrix).

~~I was going to do a video of this working but it’s easy enough to try yourself.~~ **\*Update 2023-06-09\*** Here is a video of the Emacs side of `firefox-javascript-repl`:

This inline player uses only free and open source JavaScript. Or you can download `[firefox-javascript-repl-1.cast](/screenshots/firefox-javascript-repl-1.cast)` and play it with the `[asciinema](https://asciinema.org/)` command line player.

The Firefox window looks like this:
![A Firefox window in which the URL bar has a robot icon left of the search magnifying glass, and in which the URL bar background is pink and purple diagonal strips.](/screenshots/firefox-javascript-repl-1.png)
It creates a new temporary Firefox profile, so it doesn’t mess with any of your existing profiles. Try `M-x package-install RET firefox-javascript-repl RET; M-x firefox-javascript-repl RET`. If Firefox starts and everything succeeds, you should see an interesting JavaScript quirk-of-the-day, courtesy of the [wtfjs project](https://github.com/denysdovhan/wtfjs).
*Thank you to Andrew Overholt for testing on Fedora, and for experimenting with Macintosh Operating System support (in progress).*

1. I wish [jsSlime](https://github.com/segv/jss) were still maintained, in which case I wouldn’t need to write this post or this REPL.[^](#sup-1)
2. I welcome patches to make it work on older versions of Emacs, but I can’t build anything older than Emacs 26.1 to test against.[^](#sup-2)

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1)[June 6, 2023June 9, 2023](https://www.fitzsim.org/blog/?p=669)Posted in[Emacs](https://www.fitzsim.org/blog/?cat=3)

## Post navigation

[Previous Post Previous post:
Excorporate and OAuth 2.0](https://www.fitzsim.org/blog/?p=596)

[Next Post Next post:
ulisp-repl](https://www.fitzsim.org/blog/?p=681)

## Leave a comment

### [Cancel reply](/blog/?p=669#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name

Email

Website

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

[About www.fitzsim.org](/about)

## Meta

* [Log in](https://www.fitzsim.org/blog/wp-login.php)
* [Entries feed](https://www.fitzsim.org/blog/?feed=rss2)
* [Comments feed](https://www.fitzsim.org/blog/?feed=comments-rss2)
* [WordPress.org](https://wordpress.org/)

[fitzsim's development log](https://www.fitzsim.org/blog/),
[Proudly powered by WordPress.](https://wordpress.org/)