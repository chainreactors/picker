---
title: Replacing Cursor With Neovim and Claude Code
url: https://danielmiessler.com/blog/replacing-cursor-with-neovim-claude-code
source: Daniel Miessler
date: 2025-07-14
fetch_date: 2025-10-06T23:27:33.893135
---

# Replacing Cursor With Neovim and Claude Code

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# Replacing Cursor With Neovim and Claude Code

How to use Claude Code without giving up NeoVim

July 13, 2025

[#ai](/archives/?tag=ai) [#technology](/archives/?tag=technology) [#tutorial](/archives/?tag=tutorial)

[![Neovim and Claude Code Integration](/images/neovim-claude-code-integration.png)](/images/neovim-claude-code-integration.png)

My three-paned Ghostty / Neovim / Claude Code Setup (click for full size)

It kind of sucks right now to be a [(neo)Vim](https://neovim.io/) user if you're super excited about [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).

I even tried to hold my nose and use Cursor for a while.

All that power...right in your editor! It's sooooo great.

But all the Examples that you've seen of people doing it or that you have tried yourself have been with [Cursor](https://cursor.com/), [Windsurf](https://windsurf.com/), or [VSCode](https://code.visualstudio.com/). And the plugins you've tried with Neovim don't work, or they're glitchy, or they're gross to configure and use.

*I solved this for myself with a much simpler configuration.*

## Ghostty to the rescue [​](#ghostty-to-the-rescue)

Ghostty has kind of walked away with the title.

I'm sure you're familiar with [Ghostty](https://ghostty.org/), which is kind of universally accepted as the best terminal.

What I've done is configured my entire IDE, Claude Code, and my terminal interface into a single Ghostty window with three panes.

We spend most time in Claude Code these days.

1. Claude Code on the left
2. Neovim (Code) on the right
3. A shell down below the code window

Super easy to remember because we're just using Vim commands.

And here's the Ghostty configuration I use to open and move between panes.

### The Ghostty Keybindings [​](#the-ghostty-keybindings)

bash

```
# Create new split to the right (for Neovim)
keybind = cmd+d=new_split:right

# Create new split below (for your shell)
keybind = cmd+shift+t=new_split:down

# Navigate between panes (vim-style)
keybind = ctrl+h=goto_split:left
keybind = ctrl+j=goto_split:bottom
keybind = ctrl+k=goto_split:top
keybind = ctrl+l=goto_split:right
```

1
2
3
4
5
6
7
8
9
10
11

## The result [​](#the-result)

So now all you have to do is:

* Open up Ghostty
* Open up a pane to the right
* Open up a pane below that
* Type `claude` on the left
* Open and edit your code/files in NeoVim on the right
* Leave the bottom one your shell

...and you are good to go!

Just `ctrl-[motion]` to move between them!

Hope this helps someone.

Happy hacking!

Share

[Post](https://ul.live/share/x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Freplacing-cursor-with-neovim-claude-code&title=Replacing%20Cursor%20With%20Neovim%20and%20Claude%20Code "Share on X")  [LinkedIn](https://ul.live/share/linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Freplacing-cursor-with-neovim-claude-code&title=Replacing%20Cursor%20With%20Neovim%20and%20Claude%20Code "Share on LinkedIn") [HN Hacker News](https://ul.live/share/hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Freplacing-cursor-with-neovim-claude-code&title=Replacing%20Cursor%20With%20Neovim%20and%20Claude%20Code "Share on Hacker News")  [Reddit](https://ul.live/share/reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Freplacing-cursor-with-neovim-claude-code&title=Replacing%20Cursor%20With%20Neovim%20and%20Claude%20Code "Share on Reddit")  [Facebook](https://ul.live/share/facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Freplacing-cursor-with-neovim-claude-code&title=Replacing%20Cursor%20With%20Neovim%20and%20Claude%20Code "Share on Facebook")  [Forward](https://ul.live/share/email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Freplacing-cursor-with-neovim-claude-code&title=Replacing%20Cursor%20With%20Neovim%20and%20Claude%20Code "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Freplacing-cursor-with-neovim-claude-code&title=Replacing%20Cursor%20With%20Neovim%20and%20Claude%20Code)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Freplacing-cursor-with-neovim-claude-code&title=Replacing%20Cursor%20With%20Neovim%20and%20Claude%20Code)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Freplacing-cursor-with-neovim-claude-code&title=Replacing%20Cursor%20With%20Neovim%20and%20Claude%20Code)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Freplacing-cursor-with-neovim-claude-code&title=Replacing%20Cursor%20With%20Neovim%20and%20Claude%20Code)

Search

This post was tagged with:

aitechnologytutorial

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2025 Daniel Miessler. All rights reserved.