---
title: Framework & NixOS - Daily Use
url: https://0xda.de/blog/2024/07/framework-nixos-daily-use/
source: Blogs  dade
date: 2024-07-13
fetch_date: 2025-10-06T17:42:01.448461
---

# Framework & NixOS - Daily Use

[>
cd /0xda.de/](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/)

* [About](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/about/)
* [Blog](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/)
* [Speaking](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/speaking/)
* [Music](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/music/)

  [Clearnet](https://0xda.de/blog/2024/07/framework-nixos-daily-use/ "Clearnet")

[0xdade](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/)
![Photo of the site's author](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

18 minutes

# [Framework & NixOS - Daily Use](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/07/framework-nixos-daily-use/)

---

* [Enabling Specific Non-Free Packages](#enabling-specific-non-free-packages)
* [Fixing 1Password to Float](#fixing-1password-to-float)
* [Disable Touchpad While Typing](#disable-touchpad-while-typing)
* [Configuring a browser](#configuring-a-browser)
* [Switching to PipeWire](#switching-to-pipewire)
* [Mapping Media Controls](#mapping-media-controls)
  + [Mapping Sound Controls w/ Pipewire and wpctl](#mapping-sound-controls-w-pipewire-and-wpctl)
  + [Setting The Media Control Binds](#setting-the-media-control-binds)
  + [Mapping Monitor Brightness Controls](#mapping-monitor-brightness-controls)
* [Nix Flake Update](#nix-flake-update)

---

This is **part 6** in my series of posts learning how to setup NixOS on my Framework 16" AMD laptop. It is not meant as a guide, necessarily, but more as a captain’s log of my thoughts and processes along the way.

* [Framework and NixOS - Day One](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/06/framework-and-nixos-day-one/)
* [Framework and NixOS - Day Two](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/06/framework-and-nixos-day-two/)
* [Framework and NixOS - Secure Boot](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/06/framework-and-nixos-secure-boot-day-three/)
* [Framework and NixOS - Declarative Encrypted Disk Partitions](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/06/framework-and-nixos-declarative-encrypted-disk-partitions/)
* [Framework and NixOS - Sops-nix Secrets Management](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/07/framework-and-nixos-sops-nix-secrets-management/)

I had some other plans for what I was going to do next, but I realized that I haven’t really moved into my laptop yet – none of the posts that I’ve written so far have been written on my laptop. That changes today. I setup Obsidian, re-setup my 1Password vault, get a browser setup, and figure out if I can fix the touchpad sensitivity that has already screwed up my writing like 4 times while writing this small paragraph.

## Enabling Specific Non-Free Packages

As I previously noted, 1Password is my password manager of choice, but also isn’t free and required being explicitly declared as a non-free package in my `home.nix` file. The same goes for Obsidian. I want to be explicit about my choices for non-free packages, so I’m going to reiterate the way we set that up in a previous post, as well as add obsidian to my list. In `home.nix`, add the following:

```
{
  nixpkgs = {
    config = {
      allowUnfreePredicate = pkg: builtins.elem (lib.getName pkg) [
        "1password"
        "obsidian"
      ];
    };
  };
}
```

Note that when we add these unfree predicates, they are wrapped in quotes, which is different than what we do when we add new packages. Then we’ll have add the following to our `home.packages`, further down in the file:

```
home.packages = with pkgs; [
  ...
  _1password_gui
  obsidian
];
```

We can do a `switch` and away we go, we now have Obsidian and 1Password available to us in our launcher (which we can access with
`SUPER`+`R`
, or
`WIN`+`R`
).

## Fixing 1Password to Float

While most of the time I like that my windows automatically tile in Hyprland, 1Password is a good example of a window that I typically don’t want to open in a new tile; I’d rather it open as a floating window that I can quickly reference in whatever my current context is, then get it out of my way and get back to whatever I’m doing.

Thankfully, Hyprland provides a way to do this with [Window Rules](https://wiki.hyprland.org/hyprland-wiki/pages/Configuring/Window-Rules/). We can open up our nix-managed hyprland.conf file, `~/nixcfg/home/dade/.config/hypr/hyprland.conf`, and add a new window rule. I’m going to do this towards the bottom, because there is already one window rule towards the bottom, and I’d like the window rules to be grouped together.

In order to create the window rule, we need to decide if we’re going to use the class or the title of the window to apply the rule. To figure out the class of my 1Password window, I opened up 1Password using rofi with
`SUPER`+`R`
. Once it was open, I ran `hyprctl clients` in my terminal, which gave me information about all of my open windows.

Ultimately, I decided to use `class` instead of `title`, since `title` could match things like opening `1Password` in a browser window, among other things. I anticipate that the `class` of my 1Password vault won’t change often. So I’m going to add this line to the bottom of `~/nixcfg/home/dade/.config/hypr/hyprland.conf`.

```
windowrulev2 = float,class:(1Password)
```

After running another `switch`, I tried re-opening 1Password and it didn’t float automatically like I would have expected. In hindsight, this makes sense, since rebuilding nix and putting the config file in place didn’t actually cause Hyprland to reload the config. Thankfully `hyprctl` provides a useful command here, too – `hyprctl reload`.

After reloading the config, I launched 1Password again, and now it was floating. Fantastic. Now how do I move the floating window? Thankfully, this is already included in the default Hyprland config file I have:

```
bindm = $mainMod, mouse:272, movewindow
bindm = $mainMod, mouse:273, resizewindow
```

`mouse:272` maps to the left mouse button, and `mouse:273` maps to the right mouse button. I don’t really care to resize my 1Password window, but I can do that by clicking in the bottom right corner of my Touchpad if I do ever need to. I just want to be able to move it around so I can more easily see the primary page I’m working with.

## Disable Touchpad While Typing

Based on what I was able to find, this shouldn’t be a problem by default on Hyprland, but for some reason it was a problem for me. While I was typing this post, my cursor was randomly moving to wherever my pointer was. At first I just attributed this to learning to type on a new laptop keyboard, but it kept happening frequently enough that I thought surely something must be wrong.

Hyprland uses libinput, according to a random reddit thread I found while searching for this problem, and one thing people recommended checking was whether or not the touchpad was being detected as a touchpad or as a generic mouse. I can use `libinput list-devices` for this. But I don’t have it installed right now, so instead I’m going to run it in a nix-shell. `sudo nix-shell -p libinput --run "libinput list-devices"` shows that I have a mouse at `/dev/input/event8` and a touchpad at `/dev/input/event9`. I’m unclear what the Mouse device is, but the fact that a Touchpad device is seen is a good sign.

Just to make explicit my preferences, I’m going to update my `hyprland.conf` file with the following:

```
input {
  ...
  touchpad {
    natural_scroll = true
    disable_while_typing = true
  }
}
```

The default in my configuration f...