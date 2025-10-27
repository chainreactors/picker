---
title: Fixing Opencode Transparency in Ghostty Terminal
url: https://danielmiessler.com/blog/opencode-ghostty-transparency-fix
source: Daniel Miessler
date: 2025-07-19
fetch_date: 2025-10-07T00:04:07.705155
---

# Fixing Opencode Transparency in Ghostty Terminal

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# Fixing Opencode Transparency in Ghostty Terminal

How to make Opencode respect your terminal's transparent background

July 18, 2025

[#terminal](/archives/?tag=terminal) [#tutorial](/archives/?tag=tutorial) [#productivity](/archives/?tag=productivity)

[![Opencode with transparent Ghostty terminal](/images/opencode-ghostty-transparency-new.png)](/images/opencode-ghostty-transparency-new.png)

Opencode running with transparent background in Ghostty (click for full size)

If you're using [Opencode](https://opencode.ai) in [Ghostty terminal](https://ghostty.org) and noticed that your beautiful transparent background disappears when Opencode launches, here's the fix.

## The Problem [​](#the-problem)

Opencode's TUI doesn't honor Ghostty's transparent background by default, making the Opencode part of your terminal opaque when the app runs.

## The Solution [​](#the-solution)

Configure Opencode to use its `system` theme, which adapts to your terminal's native appearance including transparency.

Create the file structure if it doesn't exist.

### Quick Fix [​](#quick-fix)

1. Open your Opencode config:

   bash

   ```
   nvim ~/.config/opencode/opencode.json
   ```

   1
2. Set the theme to `system`:

   json

   ```
   {
     "$schema": "https://opencode.ai/config.json",
     "theme": "system"
   }
   ```

   1
   2
   3
   4
3. Save the file
4. Restart Opencode

This works by using `none` for background.

Now your Opencode will seamlessly blend with your terminal's transparency settings.

Happy hacking!

#### Notes

1. This also works for other terminals with transparency like [Alacritty](https://alacritty.org) or [iTerm2](https://iterm2.com).
2. I am using this fine with the `tokyonight` theme as shown in the header image.

Share

[Post](https://ul.live/share/x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fopencode-ghostty-transparency-fix&title=Fixing%20Opencode%20Transparency%20in%20Ghostty%20Terminal "Share on X")  [LinkedIn](https://ul.live/share/linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fopencode-ghostty-transparency-fix&title=Fixing%20Opencode%20Transparency%20in%20Ghostty%20Terminal "Share on LinkedIn") [HN Hacker News](https://ul.live/share/hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fopencode-ghostty-transparency-fix&title=Fixing%20Opencode%20Transparency%20in%20Ghostty%20Terminal "Share on Hacker News")  [Reddit](https://ul.live/share/reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fopencode-ghostty-transparency-fix&title=Fixing%20Opencode%20Transparency%20in%20Ghostty%20Terminal "Share on Reddit")  [Facebook](https://ul.live/share/facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fopencode-ghostty-transparency-fix&title=Fixing%20Opencode%20Transparency%20in%20Ghostty%20Terminal "Share on Facebook")  [Forward](https://ul.live/share/email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fopencode-ghostty-transparency-fix&title=Fixing%20Opencode%20Transparency%20in%20Ghostty%20Terminal "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fopencode-ghostty-transparency-fix&title=Fixing%20Opencode%20Transparency%20in%20Ghostty%20Terminal)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fopencode-ghostty-transparency-fix&title=Fixing%20Opencode%20Transparency%20in%20Ghostty%20Terminal)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fopencode-ghostty-transparency-fix&title=Fixing%20Opencode%20Transparency%20in%20Ghostty%20Terminal)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fopencode-ghostty-transparency-fix&title=Fixing%20Opencode%20Transparency%20in%20Ghostty%20Terminal)

Search

This post was tagged with:

terminaltutorialproductivity

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2025 Daniel Miessler. All rights reserved.