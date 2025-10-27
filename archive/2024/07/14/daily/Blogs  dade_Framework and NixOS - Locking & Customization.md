---
title: Framework and NixOS - Locking & Customization
url: https://0xda.de/blog/2024/07/framework-and-nixos-locking-customization/
source: Blogs  dade
date: 2024-07-14
fetch_date: 2025-10-06T17:41:02.645365
---

# Framework and NixOS - Locking & Customization

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/07/framework-and-nixos-locking-customization/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

7 minutes

# [Framework and NixOS - Locking & Customization](https://0xda.de/blog/2024/07/framework-and-nixos-locking-customization/)

---

* [Setting up a lock screen](#setting-up-a-lock-screen)
  + [Installing Nerd Fonts](#installing-nerd-fonts)
  + [Hiding Screen Contents](#hiding-screen-contents)
* [Creating a lock hotkey](#creating-a-lock-hotkey)
* [Hypridle](#hypridle)
* [Adding a Spotlight-like keybind](#adding-a-spotlight-like-keybind)
* [Testing Screensharing](#testing-screensharing)

---

This is **part 7** in my series of posts learning how to setup NixOS on my Framework 16" AMD laptop. It is not meant as a guide, necessarily, but more as a captain’s log of my thoughts and processes along the way.

* [Framework and NixOS - Day One](https://0xda.de/blog/2024/06/framework-and-nixos-day-one/)
* [Framework and NixOS - Day Two](https://0xda.de/blog/2024/06/framework-and-nixos-day-two/)
* [Framework and NixOS - Secure Boot](https://0xda.de/blog/2024/06/framework-and-nixos-secure-boot-day-three/)
* [Framework and NixOS - Declarative Encrypted Disk Partitions](https://0xda.de/blog/2024/06/framework-and-nixos-declarative-encrypted-disk-partitions/)
* [Framework and NixOS - Sops-nix Secrets Management](https://0xda.de/blog/2024/07/framework-and-nixos-sops-nix-secrets-management/)
* [Framework and NixOS - Daily Use](https://0xda.de/blog/2024/07/framework-and-nixos-daily-use/)

## Setting up a lock screen

I’ve done all this work to secure my laptop, setting up secure boot, setting up an encrypted disk partition, etc. But my laptop never locks – there’s no idle timeout, no hot key, and there’s no lock screen.

Thankfully, the folks over at Hyprland have produced tools just for this – [hyprlock](https://wiki.hyprland.org/Hypr-Ecosystem/hyprlock/) and [hypridle](https://wiki.hyprland.org/Hypr-Ecosystem/hypridle/). We’re going to get started by setting up a `hyprlock` config file. We’re going to put all of our config files into our `~/nixcfg/home/dade/.config/hypr/` folder. I copied the [catppuccin](https://github.com/catppuccin/hyprlock) [frappe](https://github.com/catppuccin/hyprland/blob/main/themes/frappe.conf) hyprlock theme.

Next we need to update home.nix to include our new hypr config files into our home directory.

```
  home.file = {
    ".config/hypr/hyprland.conf".source = home/dade/.config/hypr/hyprland.conf;
    ".config/hypr/hyprlock.conf".source = home/dade/.config/hypr/hyprlock.conf;
    ".config/hypr/frappe.conf".source = home/dade/.config/hypr/frappe.conf;
  };
```

After doing this, I enabled hyprlock in `~/nixcfg/hosts/serenity/configuration.nix` via `programs.hyprlock.enable`. I also read that I [need to set a pam service for hyprlock](https://mynixos.com/home-manager/option/programs.hyprlock.enable), so I added a line for that as well.

```
  programs.hyprland.enable = true;
  programs.hyprland.portalPackage = pkgs.xdg-desktop-portal-hyprland;
  programs.hyprlock.enable = true; # new line
  security.pam.services.hyprlock = {}; # new line
```

After a `switch`, I manually ran `hyprlock` in the terminal and it presented the lock screen but I noticed a couple issues:

1. The login prompt has a broken icon in it
2. More importantly, my screen contents are still visible.

### Installing Nerd Fonts

To fix the broken icon, I’m going to install the Jet Brains Mono Nerd Font. I don’t have a *strong* preference on fonts, and since that’s what the theme uses by default, I’ll just stick with that for now. I can do this by adding the following to `~/nixcfg/hosts/serenity/configuration.nix`:

```
  fonts.packages = with pkgs; [ (nerdfonts.override { fonts = [ "JetBrainsMono" ]; }) ];
```

Run a `switch` and now I’ve got the relevant fonts installed and when I run `hyprlock`, I can see that the broken icon was actually a lock icon. Perfect. I might come back to this and update my Waybar configuration to use this font as well instead of Font Awesome.

### Hiding Screen Contents

Next, I need to address the fact that my screen contents are still visible. I believe that this is happening because the theme specifies a background file, but I’m not providing a background file. I’m going to just comment it out and see if that fixes the problem.

```
# BACKGROUND
background {
    monitor =
#    path = ~/.config/background
    blur_passes = 0
    color = $base
}
```

Sure enough, commenting out the line in the theme that sets a background image, it switches to just using the color for the background.

Just to give it a little more flare, I want to add a straight line across the screen similar to how the screenshot of the theme appears in the github repo. But instead of doing it with an image, I’m going to do it with a simple shape in the `hyprlock.conf` file.

```
shape {
  monitor =
  size = 2560, 4 # width, height (matches border thickness of login box)
  color = $accent
  rounding = -1
  rotate = 0
  xray = false
  position = 0, -35 # -35 is the same offset as the login box
  halign = center
  valign = center
}
```

## Creating a lock hotkey

Now that I have a lock mechanism in place, I’d like to set up a hot key to quickly lock my screen. Since I already am used to windows environments, I’m pretty comfortable with
`WIN`+`L`
to lock the screen. Let’s add another keybind to `~/nixcfg/home/.config/hypr/hyprland.conf`.

```
bind = $mainMod, l, exec, hyprlock
```

We can `switch` and then hit
`WIN`+`L`
and we’re greeted with our lock screen. Perfect. Now let’s get that automated.

## Hypridle

Next I need an idle daemon that will automatically lock the screen after my laptop has been idle for a little while. I couldn’t find exact instructions on how to do this at the host level, but based on the [MyNixOS](https://mynixos.com/home-manager/option/services.hypridle.enable) page for Hypridle, it appears to be available as a home-manager service. I’m going to try to do the same thing in my NixOS configuration and just hope it works.

In `~/nixcfg/hosts/serenity/configuration.nix` I’m going to add the following line:

```
services.hypridle.enable = true;
```

According to the [Hypridle wiki page](https://wiki.hyprland.org/Hypr-Ecosystem/hypridle/), Hypridle *requires* a config file. So let’s set one up. We’re going to start with the example from the wiki page and put it at `~/nixcfg/home/dade/.config/hypr/hypridle.conf`.

```
general {
    lock_cmd = pidof hyprlock || hyprlock       # avoid starting multiple hyprlock instances.
    before_sleep_cmd = loginctl lock-session    # lock before suspend.
    after_sleep_cmd = hyprctl dispatch dpms on  # to avoid having to press a key twice to turn on the display.
}

listener {
    timeout = 150                                # 2.5min.
    on-timeout = brightnessctl -s set 10         # set monitor backlight to minimum, avoid 0 on OLED monitor.
    on-resume = brightnessctl -r                 # monitor backlight restore.
}

# turn off keyboard backlight, comment out this section if you dont have a keyboard backlight.
listener {
    timeout = 150                                          # 2.5min.
    on-timeout = brightnessctl -sd rgb:kbd_backlight set 0 # turn off keyboard backlight.
    on-resume = brightnessctl -rd rgb:kbd_backlight        # turn on keyboard backlight.
}

listener {
    timeout = 300                                 # 5min
    on-timeout = loginctl lock-session            # lock screen when...