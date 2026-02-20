---
title: MacOS & Nix-Darwin
url: https://0xda.de/blog/2026/02/macos-nix-darwin/
source: Blogs  dade
date: 2026-02-19
fetch_date: 2026-02-20T04:07:10.864705
---

# MacOS & Nix-Darwin

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2026/02/macos-nix-darwin/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

5 minutes

# [MacOS & Nix-Darwin](https://0xda.de/blog/2026/02/macos-nix-darwin/)

Note: Like my previous articles about Nix, this is not meant to be a guide. It’s just my narrative journey while I explore the thing.

It’s been quite some time since my first foray into [NixOS on my framework laptop](https://0xda.de/blog/2024/06/framework-and-nixos-day-one/). While I still love my Framework laptop, I find that I don’t use it that often – in part because it doesn’t really integrate into my Apple ecosystem, but really because it turns out the 16" laptop was just not a very convenient choice. It barely fits in my backpack and it’s just generally too big to carry around. I’ll probably use it to replace my desktop whenever it dies, but I haven’t been using it very much as a daily driver laptop.

I have, however, been using my old first-gen M1 Macbook quite a bit. I also started a new job a few months ago where I got another Apple-silicon Macbook. It was around that time that I learned that I failed to save a lot of my configurations from my previous job’s Macbook, and so I was trying to remember what I liked. I’m not good at remembering things. So I found myself basically setting up two macbooks, and both of them have subtle differences. Not just because one is work and so has a bunch of work software on it, but because I’m human, forgetful, and error-prone.

I found myself longing for the declarative nature of my Framework laptop. I was also chatting with my friend, [Adam](https://technowizardry.net/), about his [NixOS experiences](https://technowizardry.net/2025/11/i-like-the-idea-of-nix-but-dont-enjoy-using-it/) and some of the cool work he was doing with generating diffs on pull requests and the potential for better CI/CD integration. A very rapid unplanned inspiration event led me from “I should update my servers to NixOS so I don’t have to worry about them so much anymore” to “Well I have to use my laptop to update my servers, so I guess I should put Nix on my Macbook first.”

## Nix-Darwin

Thankfully [Nix-Darwin](https://github.com/nix-darwin/nix-darwin/) exists, which lets you turn your Macbook into a NixOS-like experience, albeit with a few caveats. I think the most important caveat for me, and something I am exceedingly happy about while writing this, is that it doesn’t blow away all your installed applications or configuration when you set up Nix-Darwin. I hadn’t even considered this a possibility until the moment the rebuild started working (more on this in a minute), but then I briefly panicked like “Oh no, I already have a user, I already have all these apps installed, I already have a bunch of configuration, what if my barebones config blows that all away and I brick my Macbook?”

In classic hacker fashion, of course the command was already running before those thoughts crossed my mind. It would have been too late. Thankfully Nix-Darwin seems to be more forgiving about being installed on existing functional systems and it didn’t modify any of my existing stuff. But let’s rewind a little bit to the struggles that led up to this panic moment.

### Installing nix-darwin

The readme for nix-darwin has some guidance in it, but the guidance was kind of confusing for me. I already had a flake from my existing NixOS configurations, and I’d like to reuse that so that I can keep it all in one repo and reuse components where appropriate. One could certainly make the argument that the darwin configuration and the nixos configuration should be completely separate, and I probably would even agree with that idea – it certainly would have made my life easier tonight.

Before I could install nix-darwin, I had to install nix. According to the nix-darwin readme, they recommend installing [Lix](https://lix.systems/install/#on-any-other-linuxmacos-system) rather than Nix, because Lix ships with an uninstaller, whereas Nix does not. In the event that I don’t like declaratively managing my Macbook, I thought the uninstaller would be helpful.

Installing Lix was uneventful and it behaves as Nix behaves, or at least so far it does. Next it was time to get the flake configuration setup. I cloned my `nixcfg` repo that houses the rest of my configuration, and started trying to follow the nix-darwin guidance. Unfortunately the command it suggests running repeatedly did not work for me - `sudo nix run nix-darwin/nix-darwin-25.05#darwin-rebuild -- switch`. It would just complain `warning: Nix search path entry '/nix/var/nix/profiles/per-user/root/channels' does not exist, ignoring error: file 'darwin' was not found in the Nix search path (add it using $NIX_PATH or -I)`. Like, duh, I’m trying to install nix-darwin, of course it’s not in the path yet.

After a fair bit of searching, I figured out that the solution was obvious in hindsight – I needed to enable flakes, specify my flake, and make sure my darwin configuration was added to my repo. Same as I did for my NixOS machine.

```
sudo nix run nix-darwin/master#darwin-rebuild --extra-experimental-features "nix-command flakes" -- switch --flake ./flake.nix
```

This ended up working for me from inside my `nixcfg` repo. But I’m pretty sure it would also work correctly from anywhere if I replaced `./flake.nix` with `~/nixcfg`, the path to my nixcfg repo.

After this ran successfully, I now had the `darwin-` commands available that I expected, such as `darwin-rebuild`, `darwin-help`, `darwin-options`, `darwin-version`, and `darwin-uninstaller`.

### Dustin Lyon’s Nix Config

What also ended up being a huge help is [Dustin Lyon’s nixos-config repository](https://github.com/dustinlyons/nixos-config/). It’s well laid out, taught me several things about Nix, especially how to integrate nix-darwin into my existing config repo, and overall just gave a lot of inspiration. He even provides templates for new configurations, but since I’m integrating into my existing config, that won’t be particularly helpful for me. I’ll instead be manually integrating the things I like, and leaving out the things I don’t like.

This also serves as a catalyst for me to clean up my nix config and make the repo public – I have gotten a great deal of value from the repos that others have made public, I should contribute that back. I just need to look through the history and make sure there are no secrets that would be problematic if published. On the other hand, I don’t necessarily want to map out all my infrastructure in one repo, so I’m still weighing this. I have some specific ideas for NixOS server configurations that I might publish independently, though.

---

Share this page

`https://0xda.de/blog/2026/02/macos-nix-darwin/`

[nix](https://0xda.de/tags/nix)

1047 Words

Date Published

2026-02-19 03:05 +0000

60aefca @ 2026-02-19

---

[ГўВҶВҗ
Experimenting with Nixos Anywhere](https://0xda.de/blog/2026/02/experimenting-with-nixos-anywhere/)

[Weekly Retro 2025-W17
ГўВҶВ’](https://0xda.de/blog/2025/04/weekly-retro-2025-w17/)

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

© 2026
[Privacy](https://0xda.de/privacy/)
[Colophon](https://0xda.de/colophon/)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2026/02/macos-nix-darwin/ "Tor")
[CC BY-NC 4.0](https...