---
title: SlickRun
url: https://textslashplain.com/2023/01/12/slickrun/
source: text/plain
date: 2023-01-13
fetch_date: 2025-10-04T03:45:29.717761
---

# SlickRun

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# SlickRun

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2023-01-122024-07-01](https://textslashplain.com/2023/01/12/slickrun/)Posted in[dev](https://textslashplain.com/category/dev/), [storytelling](https://textslashplain.com/category/storytelling/), [tech](https://textslashplain.com/category/tech/)Tags:[Bayden](https://textslashplain.com/tag/bayden/), [SlickRun](https://textslashplain.com/tag/slickrun/)

While I’m best known for creating [Fiddler](https://fiddler2.com/) two decades ago, eight years before Fiddler’s debut I [started work](https://bayden.com/slickrun/story.asp) on what became [SlickRun](https://bayden.com/slickrun/). SlickRun is a floating command line that provides nearly instant access to almost any app or website. Originally written in Visual Basic 3 and released as *QuickRun* for Windows 3.1, it was soon ported to Borland Delphi and later renamed *SlickRun* to avoid a name-collision with an unrelated tool.

SlickRun was a part of the story of how I joined Microsoft — when I had my on-campus interview for my first internship, I’d brought a binder of screenshots from apps that I’d written. My interviewer was generally interested but got super-excited as I explained what SlickRun did. “*Have you shown this to Microsoft??”* he asked. Flummoxed and wondering *Uh, how exactly would I have done that?*, I replied “*Uh, I guess I just did?*” Five years later when I interviewed for the IE team, the GM interviewing me asked “*How often do you type `www.goo` in the browser address bar and wish it did the right thing?*” to which I responded “*Uh, less than you might think.*” before showing off the autocomplete inside SlickRun. I got that job too.

While I’ve maintained SlickRun routinely over the years, making updates as needed to support 32bit, and then 64bit Windows, and keep it compatible with new paradigms in Windows Vista and beyond, I’ve done relatively little to publicize it to the world at large. It just quietly hums along with a mostly-satisfied userbase of thousands around the world.

Personally, I’ve been using SlickRun nearly daily for almost three decades and have executed almost 200000 commands on my latest fleet of Windows 11 PCs.

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-16.png?w=821)](https://textslashplain.com/wp-content/uploads/2023/01/image-16.png)

Perhaps the biggest problem with SlickRun is that, designed to be small and simple, it offers few affordances to reveal the tremendous amount of power living under the surface. By default, it ships with only a handful of **MagicWords** (command shortcuts/aliases) but it will never achieve its full power unless the user creates their own MagicWords to match their own needs and terminology.

If a user types `HELP`, an online [help page](https://bayden.com/SlickRun/1033/SlickRunHelp.aspx) will open to explain the basics, and for the few who bother to read that page, an [advanced usage page](https://bayden.com/SlickRun/1033/SlickRunAdvancedHelp.htm) reveals some even less obvious features of the tool.

I’ve been meaning to put together a demo reel video for decades now but have never gotten around to it. Mostly, SlickRun has spread organically, with folks seeing it in use on a peer’s desktop and asking “Hey, how … what is *that*?”

### Idle Info Display

Beyond its program-launching features, SlickRun provides a useful little perch for showing information in an always-visible (by default) location on your desktop. If you type `SETUP`, there’s a variety of display customization options. SlickRun’s “idle” appearance which can show useful things like clocks (in arbitrary time zones), date, battery life, days-until-an-event, machine name, IP address, memory usage, CPU usage, etc:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-11.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-11.png)
[![](https://textslashplain.com/wp-content/uploads/2023/01/image-10.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-10.png)

If SlickRun ever gets in your way (e.g. while watching a full-screen video), just type `HIDE` to tell it to hide out in your system tray until summoned.

### The Basics

Click on SlickRun or hit the hotkey to activate it and enter command mode. *(The hotkey is configurable via `SETUP`. For historical reasons, it defaults to* `Win+Q` *which doesn’t work on modern Windows without a simple [registry modification](https://bayden.com/SlickRun/1033/SlickRunHelp.aspx#:~:text=Free%20up%20Windows%20Hotkeys) due to other tools camping on that key. After a decade, I configured mine to* `Alt+Q` *instead.)*

Type a command into SlickRun and hit enter to launch it. You can hit the tab key to jump to the end of an autocomplete suggestion if you want to change or add arguments at the end of the command.

Use the up/down arrow keys to scroll through your command history– if you’ve already typed some characters, the history is filtered to just the commands that match. Or hit `Alt+F` to show a context menu list of all matches (or `ALT+Shift+F` to loosen the matching to the entire command, not just the prefix). Or, hit `Alt+S` to show a context menu list containing any Start Menu shortcuts containing what you’ve already typed.

**SlickRun loves the internet**. Type a url in SlickRun to open it in your default browser. My very favorite MagicWord launches an “I’m Feeling Lucky” Search on Google, so I can type **goto *SlickRun*** and `https://bayden.com/slickrun/` will open (see [this post](https://textslashplain.com/2022/09/01/quickfix-trivial-chrome-extensions/) for more info). This works *magically* well.

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-32.png?w=949)](https://textslashplain.com/wp-content/uploads/2023/01/image-32.png)

As you can see, you can add MagicWords to launch web searches, where `$W$` is filled by a URL-encoded parameter. For example:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-8.png?w=703)](https://textslashplain.com/wp-content/uploads/2023/01/image-8.png)

After creating this MagicWord, you can type **`errors 0x1234`** and your browser will go to the relevant URL. If you fail to specify a parameter when invoking the MagicWord, you’ll be asked to supply it via a popup window:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-9.png?w=933)](https://textslashplain.com/wp-content/uploads/2023/01/image-9.png)

You can type `CALENDAR` to launch a calendar, or `CALENDAR 5/6` to jump to May sixth.

Using `@MULTI@`, you can have a single MagicWord launch multiple commands:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-51.png?w=782)](https://textslashplain.com/wp-content/uploads/2023/01/image-51.png)

In cases where you have related commands, you can name your MagicWords with a slash in the middle of them; each tab of the tab key will jump to the next slash, allowing you to adjust what is autocompleted as you go.

So, for example, I can type e.g. **e{tab}s** to get to “Edge Stable” in the autocomplete:

[![](https://textslashplain.com/wp-content/uploads/2023/01/image-12.png?w=1024)](https://textslashplain.com/wp-content/uploads/2023/01/image-12.png)

When executing a MagicWord, a `$C$` token will replaced by any text found on the clipboard.

Hit `Ctrl+I` to get a Windows file picker to insert a file path at the current location of the command line string. Or, tap `Ctrl+V` with one or more files on your clipboard and SlickRun will insert the file path(s) at the current insertion point. Hit `Ctrl+T` to transpose the last two arguments in the current command (e.g. `windiff A B` becomes `windiff B A`) and hit `CTRL+\` to convert any Unix-style path separator backslashes (`c/src/chrome/`) into Windows-style backslashes (`c\src\chrome\`).

SlickRun can perform simple math...