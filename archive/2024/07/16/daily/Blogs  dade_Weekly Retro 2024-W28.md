---
title: Weekly Retro 2024-W28
url: https://0xda.de/blog/2024/07/weekly-retro-2024-w28/
source: Blogs  dade
date: 2024-07-16
fetch_date: 2025-10-06T17:42:48.667244
---

# Weekly Retro 2024-W28

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/07/weekly-retro-2024-w28/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

6 minutes

# [Weekly Retro 2024-W28](https://0xda.de/blog/2024/07/weekly-retro-2024-w28/)

---

* [Framework Progress](#framework-progress)
* [Website Improvements](#website-improvements)
* [Catppuccin](#catppuccin)
* [Markdown Presentations](#markdown-presentations)
* [What I’m Reading](#what-im-reading)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

My Framework 16 is finally usable for daily use after I spent weeks of spare time using it to learn NixOS on bare metal. I also added sidenotes to my site, discovered an appreciation for the Catppuccin themes, and I’m writing my slides in Obsidian with Advanced Slides.

## Framework Progress

If you’ve read my blog or social media at all in the last 2 months, you’ll know I’ve been working on getting my [Framework 16 laptop setup for daily use with NixOS](https://0xda.de/blog/2024/07/framework-and-nixos-daily-use/). I think I’ve finally reached that point, after adding some basic daily use packages like a browser and obsidian, getting my media controls and brightness controls to work, and [setting up a screen lock and idle daemon](https://0xda.de/blog/2024/07/framework-and-nixos-locking-customization/).

Maybe I’ll make a commitment to myself to write my next retro entirely on my Framework. I don’t think there’s much I’m missing to be able to do that.

## Website Improvements

It’s been several retros since the last time I talked about adding
something new to my site
[ ]

Okay literally last week I wrote about website improvements. Same header and everything.
.

This week I added the ability to use [sidenotes in hugo](https://0xda.de/blog/2024/07/hugo-sidenotes-shortcode/), as well as added a `kbd` shortcode to make keyboard shortcuts appear consistent across the site (such as
`WIN`+`L`
). I also figured out why my code highlighting was all being forced to one theme, and was surprised to learn that it was being done in Javascript, for some reason.

Hugo supports [syntax highlighting](https://gohugo.io/content-management/syntax-highlighting/) automatically, and supports all sorts of [different themes via Chroma](https://swapoff.org/chroma/playground/). But the `hello-friend-ng` theme that I based this site off of used `prism.js` to do code highlighting, but it would just stomp over whatever Hugo was already doing. This led to an inconsistent experience, and also, frankly, using javascript to do syntax highlighting is kinda dumb. So I just ripped that out. I also swapped my syntax highlighting theme to catpuccing-frappe (though I think there’s still something not quite working right with this, I will figure it out).

```
[markup]
  [markup.highlight]
    anchorLineNos = false
    codeFences = true
    guessSyntax = true
    hl_Lines = ''
    hl_inline = false
    lineAnchors = ''
    lineNoStart = 1
    lineNos = false
    lineNumbersInTable = true
    noClasses = true
    noHl = false
    style = 'catppuccin-frappe'
    tabWidth = 4
```

## Catppuccin

I’m not going to lie, I went a little overboard with the Catppuccin theme this week. It started because I needed a [hyprlock theme to use for my laptop](https://github.com/catppuccin/hyprlock). Then I was like “Dang, I like this color palette, I wonder what else I can use it with,” and now I have it setup for:

* [Obsidian](https://github.com/catppuccin/obsidian) - I also *love* the font that this came with, I feel like it made my Obsidian vault much nicer to look at.
* [Slack](https://github.com/catppuccin/slack) - It warns that this won’t work quite right, but I think it worked pretty much fine.
* [VS Code](https://github.com/catppuccin/vscode) + [icons](https://marketplace.visualstudio.com/items?itemName=Catppuccin.catppuccin-vsc-icons)
* [Thunderbird](https://github.com/catppuccin/thunderbird) (I’m not sold on this one yet)
* [PyCharm](https://github.com/catppuccin/jetbrains)

## Markdown Presentations

Have you ever thought to yourself “I wish it was harder to make powerpoints, but also commit them to Github”? Boy howdy, Advanced Slides has you covered. Under the hood, [Advanced Slides](https://mszturc.github.io/obsidian-advanced-slides/) converts your markdown files, written in Obsidian, into a [reveal.js](https://revealjs.com/) presentation.

I think ever since watching [The Unreasonable Effectiveness of Plain Text](https://www.youtube.com/watch?v=WgV6M1LyfNY), I’ve been interested in finding new places to integrate plain text into my workflows. This also aligns with [File over app](https://stephango.com/file-over-app), the philosophy of the creator of Obsidian. While I highly doubt Powerpoint is going anywhere, there is something I love about just having some markdown representation of my slides. Even if the `reveal.js` project goes away, even if `Advanced Slides` goes away, I still have a representation of all my content, even if it’s not exactly as I had intended to represent it.

My only complaint about the Advanced Slides plugin, at least so far, is that the presentation view doesn’t seem to work very well on my windows machine. Since it’s supposed to just be rendering the markdown to HTML and then showing the HTML, I’m a bit confused how this could be so inconsistent. But it works great on my laptop, which is what I’ll be presenting from anyways.

Once I get the slides done, I’m going to spend some time figuring out how to embed it directly into my site, that way I can direct link to the slides and the transcript from the end of the slides.

## What I’m Reading

![Book cover for Tor, by Ben Collier. Subtitle 'From the Dark Web to the Future of Privacy'](https://0xda.de/img/books/Tor-BenCollier.707217e2e555c61ae61bfda7e1186776.jpg)

### Tor: From the Dark Web to the Future of Privacy

#### By Ben Collier

**ISBN: 9780262548182**
[Learn More](https://mitpress.mit.edu/9780262548182/tor/ "Learn More About The Book")

---

Even more progress this week, I’m getting back into reading more regularly. This week I was surprised to learn about just how many similar ideas and technologies existed prior to Tor, and how Tor had to focus on usability and adoption to become a useful anonymity network.

## Interesting Links

* [PyPI.org Github PAT leaked](https://blog.pypi.org/posts/2024-07-08-incident-report-leaked-admin-personal-access-token/) - Beware the `.pyc` files shipped in your docker containers.
* [Semiphemeral returns (Soon)](https://semiphemeral.com/like-a-phoenix-semiphemeral-will-rise-from-the-ashes/) - Semiphemeral is a cool project from Micah Lee, and this details how he is bringing it back after Twitter killed their API. Interested to see how this goes.
* [The significance of the X window system boot stipple](https://matttproud.com/blog/posts/x-window-system-boot-stipple.html)
* [The case for burning counterterrorism operations](https://blog.kwiatkowski.fr/the-case-for-burning-counterterrorism-operations) - A few weeks ago someone published another post on why companies shouldn’t report on adversarial actions that happen to be run by
  friendly
  [ ]

  For varying definitions of friendly
  governments. This is a good counterargument. I personally stand on the side of “If you get caught, you get caught, try harder.”
* [Exploiting Ghostscript using format strings](https://codeanlabs.com/blog/research/cve-2024-29510-ghostscript-format-string-exploitation/) - If you know about Ghostscript, you probably know how bi...