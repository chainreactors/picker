---
title: How to Integrate Claude Code with Neovim Using Ghostty Terminal Panes
url: https://danielmiessler.com/blog/claude-code-neovim-ghostty-integration
source: Daniel Miessler
date: 2025-07-09
fetch_date: 2025-10-07T00:08:34.737560
---

# How to Integrate Claude Code with Neovim Using Ghostty Terminal Panes

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# How to Integrate Claude Code with Neovim Using Ghostty Terminal Panes

No more Cursor FOMO

July 8, 2025

[#ai](/archives/?tag=ai) [#productivity](/archives/?tag=productivity) [#technology](/archives/?tag=technology) [#tutorial](/archives/?tag=tutorial) [#recommended](/archives/?tag=recommended) [#top](/archives/?tag=top)

![Claude Code and Neovim integration through Ghostty terminal](/images/claude-neovim-ghostty.png)

If you're a Neovim user feeling left out watching everyone use Claude Code with VS Code, here's my dead simple solution: three terminal panes.

## The Setup [​](#the-setup)

One Ghostty window, three panes:

* **Left**: Claude Code
* **Right**: Neovim
* **Bottom**: Terminal

## The Configuration [​](#the-configuration)

Add these to your Ghostty config:

toml

```
keybind = ctrl+h=goto_split:left
keybind = ctrl+j=goto_split:bottom
keybind = ctrl+k=goto_split:top
keybind = ctrl+l=goto_split:right
```

1
2
3
4

Now use Control + vim keys to jump between panes instantly. No mouse, no window switching.

## Why It Works [​](#why-it-works)

This setup eliminates the need for VS Code or Cursor. You keep your Neovim config, your muscle memory, and gain AI assistance exactly when you need it.

The best integrations don't feel like integrations.

## Getting Started [​](#getting-started)

1. Install Ghostty (or any terminal with panes)
2. Add the keybindings
3. Open three panes
4. Start Claude Code, Neovim, and a terminal

That's it. We get all the CC goodness without losing vim!

#### Notes

1. AIL Level 4 (AI Created, Human Basic Idea) [AIL Levels](https://danielmiessler.com/blog/ai-influence-level-ail)

Share

[Post](https://ul.live/share/x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fclaude-code-neovim-ghostty-integration&title=How%20to%20Integrate%20Claude%20Code%20with%20Neovim%20Using%20Ghostty%20Terminal%20Panes "Share on X")  [LinkedIn](https://ul.live/share/linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fclaude-code-neovim-ghostty-integration&title=How%20to%20Integrate%20Claude%20Code%20with%20Neovim%20Using%20Ghostty%20Terminal%20Panes "Share on LinkedIn") [HN Hacker News](https://ul.live/share/hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fclaude-code-neovim-ghostty-integration&title=How%20to%20Integrate%20Claude%20Code%20with%20Neovim%20Using%20Ghostty%20Terminal%20Panes "Share on Hacker News")  [Reddit](https://ul.live/share/reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fclaude-code-neovim-ghostty-integration&title=How%20to%20Integrate%20Claude%20Code%20with%20Neovim%20Using%20Ghostty%20Terminal%20Panes "Share on Reddit")  [Facebook](https://ul.live/share/facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fclaude-code-neovim-ghostty-integration&title=How%20to%20Integrate%20Claude%20Code%20with%20Neovim%20Using%20Ghostty%20Terminal%20Panes "Share on Facebook")  [Forward](https://ul.live/share/email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fclaude-code-neovim-ghostty-integration&title=How%20to%20Integrate%20Claude%20Code%20with%20Neovim%20Using%20Ghostty%20Terminal%20Panes "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fclaude-code-neovim-ghostty-integration&title=How%20to%20Integrate%20Claude%20Code%20with%20Neovim%20Using%20Ghostty%20Terminal%20Panes)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fclaude-code-neovim-ghostty-integration&title=How%20to%20Integrate%20Claude%20Code%20with%20Neovim%20Using%20Ghostty%20Terminal%20Panes)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fclaude-code-neovim-ghostty-integration&title=How%20to%20Integrate%20Claude%20Code%20with%20Neovim%20Using%20Ghostty%20Terminal%20Panes)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fclaude-code-neovim-ghostty-integration&title=How%20to%20Integrate%20Claude%20Code%20with%20Neovim%20Using%20Ghostty%20Terminal%20Panes)

Search

This post was tagged with:

aiproductivitytechnologytutorialrecommendedtop

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2025 Daniel Miessler. All rights reserved.