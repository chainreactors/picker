---
title: Kali Community Themes
url: https://www.kali.org/blog/kali-community-themes/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:20.276000
---

# Kali Community Themes

* [Join Free CTF](https://www.offsec.com/events/the-gauntlet/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/kali-community-themes/images/kali-community-themes-banner.jpg)
Monday, 24 October 2022

# Kali Community Themes

Table of Contents

* [ZephyFoxy#5208](#zephyfoxy5208)
* [tachyglossues#2480](#tachyglossues2480)
* [fumenoid#9548](#fumenoid9548)
* [leo-tornado#4019](#leo-tornado4019)
* [\_Henry\_#3058](#_henry_3058)
* [Wrapping Up](#wrapping-up)

The following blog post was written by a moderator on the [Kali Linux & Friends](https://discord.kali.org/) Discord server, Tristram. A massive thank you to Tristram for writing this blog post and to all of the participants!

This past summer we held our first community event on the [Kali Linux & Friends](https://discord.kali.org/) Discord. With this event, we asked everyone who wanted to participate to share their Kali Linux setup. With each submission, the community had to select their favorite by adding the `:kali4kids:` emoji (Shown below). The five submissions with the most `:kali4kids:` emojis were deemed the winner.

[![](images/kali4kids.png)](https://www.kali.org/blog/kali-community-themes/images/kali4kids.png)

The community has spoken and we are happy to showcase the following setups. The author of each setup has provided us with a little blurb to get to know them a little more, as well as their setup.

## ZephyFoxy#5208

I am a senior security consultant working for a large, multinational consulting firm. I conduct pentests in a variety of different fields, and have been working in Android malware analysis for the last year. I hold the OSCP and OSEP certifications, and I will be working towards OSED and OSWE in the near future. I chose this setup for my Kali Linux because I personally prefer a colourful environment that really stands out.

The customization to the terminal comes from the need to reference my IP address for things such as reverse shells or file transfers. You can find a copy of my `~/.zshrc` on my [GitHub](https://github.com/purpl3f0xsecur1ty/useful_random_stuff/blob/main/.zshrc).

[![](images/ZephyFoxy.png)](https://www.kali.org/blog/kali-community-themes/images/ZephyFoxy.png)

---

## tachyglossues#2480

I’m a French student who likes to tinker and understand how computers work especially on the software side and I’ve been using Kali for about a year and a half.

The program I wrote works by running `top` to get the list of software running on the session with the RAM and CPU they use and after that a python dependency that is used to generate word clouds is used with a mask of the kali4kids logo to give the shape and colour and this mask is a simple .png file. I made this program because I like to have a wallpaper that I made and also I like minimalist wallpapers and it can be useful. You can find a copy on my [GitHub](https://github.com/tachyglossues/wallpaper-process-wordcloud).

[![](images/tachyglossues.png)](https://www.kali.org/blog/kali-community-themes/images/tachyglossues.png)

## fumenoid#9548

Hi, I am fume. I have recently graduated from uni and I am working as a penetration tester. Aside from my job, I also like to develop challenges for CTF events. My time sinks are anime, manga, and at times I also play CS:GO.

* [XCT i3 kali setup script](https://github.com/xct/kali-clean)
  I love Kali Linux, it has always been one of my favourite penetration testing distros. My Kali setup is highly inspired from [xct’s Kali setup](https://github.com/xct/kali-clean), so I use [kali-i3 gaps](https://pkg.kali.org/pkg/i3-gaps) as my desktop environment with [alacritty](https://pkg.kali.org/pkg/rust-alacritty-terminal) as my terminal emulator. I use Zsh and have customized it with oh-my-zsh (theme: `agnoster`). I have done further additions to the i3 bar and have added custom shortcuts in configs to organize my workflow. I am also using [ranger](https://pkg.kali.org/pkg/ranger) as my command line file manager and [btop](https://pkg.kali.org/pkg/btop) for rice. A pretty slick thing about ranger is that it also has the same shortcuts as [vim](https://pkg.kali.org/pkg/vim). And yes I believe in vim supremacy :P. Also, I am using megumi’s picture as my wallpaper, the best girl right?

I don’t have scripts or dot-files publicly available for my setup but here are some resources that might help y’all to build a similar/better setup.

* [XCT i3 kali setup script](https://github.com/xct/kali-clean)
  + I would recommend reading the script and using it as a base but please don’t blindly execute it if you aren’t aware of what you are doing.
* [Alex Booker YouTube videos on i3wm:](https://www.youtube.com/watch?v=8-S0cWnLBKg)
* [Luke Smith’s YouTube videos on Ranger and Vim](https://www.youtube.com/watch?v=L6Vu7WPkoJo)

Feel free to reach out to me on the Kali Linux discord if you have further questions :D

[![](images/fumenoid.png)](https://www.kali.org/blog/kali-community-themes/images/fumenoid.png)

---

## leo-tornado#4019

My name is Ahmed and I am 17 years old. I study mathematics and have a passion for cyber security. I am interested in making my own desktop as it encourages me to keep working. I can’t explain it but when you open the computer and find something you made, it inspires you to keep learning more. I don’t have links to share, but anyone can do this so you just have to be a little creative. It was a good competition, thank you for organizing.

[![](images/leo-tornado.png)](https://www.kali.org/blog/kali-community-themes/images/leo-tornado.png)

---

## \_Henry\_#3058

Hey guys, I’m Henry. I’m currently a “Cybersecurity Engineer” by day, and a bad PEN-300 student by night (I really need to get those labs done). You might have interacted with me in a Discord livestream, or maybe peeped one of my (admittedly few) walk-through videos on my [YouTube channel](https://www.youtube.com/channel/UCIFrSJrAxgC86z19u6W1H8Q). While I am not the greatest among us, I take enjoyment in helping others fulfil their potential and achieve their goals, pentesting or otherwise.

Regarding my build, while I half entered the competition as a joke, I unironically REALLY like the default Kali terminal. The only modification I’ve made is I’ve changed the key bindings of moving between split terminals from “**Alt...