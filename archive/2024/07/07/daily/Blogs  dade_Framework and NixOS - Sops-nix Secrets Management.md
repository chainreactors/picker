---
title: Framework and NixOS - Sops-nix Secrets Management
url: https://0xda.de/blog/2024/07/framework-and-nixos-sops-nix-secrets-management/
source: Blogs  dade
date: 2024-07-07
fetch_date: 2025-10-06T17:41:21.550604
---

# Framework and NixOS - Sops-nix Secrets Management

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/07/framework-and-nixos-sops-nix-secrets-management/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

14 minutes

# [Framework and NixOS - Sops-nix Secrets Management](https://0xda.de/blog/2024/07/framework-and-nixos-sops-nix-secrets-management/)

---

* [Re-enabling Secure Boot](#re-enabling-secure-boot)
* [Getting connected to WiFi](#getting-connected-to-wifi)
* [Restoring my backup home directory](#restoring-my-backup-home-directory)
* [One Rebuild For Good Measure](#one-rebuild-for-good-measure)
* [Installing Sops-nix](#installing-sops-nix)
  + [Generating encryption keys](#generating-encryption-keys)
  + [Creating our sops configuration](#creating-our-sops-configuration)
  + [Separating our secrets from our config](#separating-our-secrets-from-our-config)
  + [Adding our secrets to nixcfg](#adding-our-secrets-to-nixcfg)
* [The moment of truth](#the-moment-of-truth)
  + [Testing our changes](#testing-our-changes)
* [Next Time on Dragon Ball Z](#next-time-on-dragon-ball-z)

---

This is part 5 in my series of posts learning how to setup NixOS on my Framework 16" AMD laptop. It is not meant as a guide, necessarily, but more as a captain’s log of my thoughts and processes along the way.

* [Framework and NixOS - Day One](https://0xda.de/blog/2024/06/framework-and-nixos-day-one/)
* [Framework and NixOS - Day Two](https://0xda.de/blog/2024/06/framework-and-nixos-day-two/)
* [Framework and NixOS - Secure Boot](https://0xda.de/blog/2024/06/framework-and-nixos-secure-boot-day-three/)
* [Framework and NixOS - Declarative Encrypted Disk Partitions](https://0xda.de/blog/2024/06/framework-and-nixos-declarative-encrypted-disk-partitions/)

## Re-enabling Secure Boot

Picking up right where I left off yesterday, I remembered that I had to disable secure boot enforcement to boot from the live installation USB. So I rebooted back into the UEFI interface and re-enabled secure boot enforcement, hit f10 to save and exit, and the booted back into NixOS. I was very thankful that I had no problems here, and I’m pretty sure that’s because I remembered to save the contents of `/etc/secureboot` before I reformatted my drive, and then restore it before re-enforcing secure boot. Otherwise I would have had to go through the secure boot key installation process again.

## Getting connected to WiFi

At the end of the previous post, I mentioned how my WiFi credentials weren’t declared as part of my Nix config – as a result of this, I can’t really do anything on my laptop until I get my network configured. In the live media, it was easy because the system bar had a button you could click to configure WiFi.

Hyprland doesn’t provide any such bar, and my Waybar configuration does tell me the status of my network, but I can’t click it to get into the configuration. So I will have to find out to do this on the terminal.

I did a little digging in `/etc` to see if I could find what controlled the network, and wouldn’t you know it, there’s a `/etc/NetworkManager`. Now I just have to learn how to use NetworkManager, or otherwise configure the network via the config file. I did a little searching and found out NetworkManager provides `nmcli`, which I can use to interact with my network devices. Looks like I can simply use `nmcli device wifi connect` – or more completely:

```
nmcli device wifi connect MY_WIFI_SSID password thepasswordisonthefridge
```

After a small amount of time, it returned and told me `Device 'wlp1s0' successfully activated with '<uuid>'`. Waybar automatically updated to show that I’m connected to my network.

It’s just about time to actually start working on adding safeguarded secrets to my Nix configurations.

## Restoring my backup home directory

Before I get into the next steps, I need to restore the files I backed up from my home directory – specifically, I need to restore the `.ssh/` folder and the `nixcfg` folder from my flashdrive into my new home directory. Once I did this, all my file permissions were messed up, all files were world readable by default, which I didn’t want (and in the case of ssh, it won’t allow it). It also captured the file mode change in the git repo, from 644 to 755, which I didn’t want. To fix this, I ran `find . -type f -exec chmod 644 {} \;` – ChatGPT told me to. Sure enough, that cleared the diff on all the files that I didn’t actually change the contents of.

Once I fixed all my file permissions, I wanted to make sure to capture the changes to my configuration that I made during the live USB – specifically, now I can remove the original filesystem declarations from my hardware config, and commit that change to add my disk config to my `hosts/serenity/configuration.nix` file.

I didn’t bother to restore all the other random stuff that was in my home directory, just the `nixcfg` and `.ssh` directories – the other stuff wasn’t really placed there by me, and I don’t care to keep it if I don’t need it. I’d like to be more particular about the way I manage files on here, which means not just letting random junk gunk up the output of my `ls` commands.

## One Rebuild For Good Measure

Now that I’m roughly back to where I started before having to format my disk, I am going to run a `switch` command (which I have aliased to `sudo nixos-rebuild switch --flake ~/nixcfg`), just to make sure everything is in a consistent state. While doing this, I noticed that `sudo` is prompting me for my password again – this means that my fingerprint is no longer enrolled, which makes sense. So I’ll go ahead and do that again real quick with `sudo fprintd-enroll dade`. I wonder if we can manage the fingerprint enrollment with sops-nix as well… I suppose I’ll have to look into how fprintd works.

## Installing Sops-nix

As I’ve previously mentioned, I am planning to use [sops-nix](https://github.com/Mic92/sops-nix) to manage secrets in my nix configuration. I want to be able to capture secrets in a relatively safe way, since they are very often a necessary part of any machine. Whether it’s SSH keys, API keys, your WiFi password, or your user password, you probably want them present automatically on a new system – after all, that is kind of the whole appeal to NixOS, isn’t it?

Getting started, I need to add sops-nix to my `flake.nix` inputs, outputs, and system modules. I’ve cut out other existing config using `...` where appropriate.

```
{
  inputs = {
    ...
    sops-nix = {
      url = "github:Mic92/sops-nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = { self, nixpkgs, disko, lanzaboote, sops-nix, ...}@inputs: {
    nixosConfigurations.serenity = nixpkgs.lib.nixosSystem {
      ...
      modules = [
        ...
        sops-nix.nixosModules.sops
      ];
    };
  };

}
```

Just to make sure sops-nix gets picked up, I ran a `switch` here and confirmed that I saw the new inputs getting added. I also noticed that sops-nix brings a `sops-nix/nixpkgs-stable` input with it. My system input for nixpkgs is unstable, so I suppose this is probably for the best.

### Generating encryption keys

I’m going to be using [age](https://github.com/FiloSottile/age) for the encryption method, for two reasons: GPG sucks, and I use ed25519 ssh keys pretty much exclusively, which I can use conveniently with `ssh-to-age`. I anticipate I’m going to need `age` somewhat regularly, so I’m going to go ahead and add it to my `home.nix` and do another `switch`.

```
{
  ...
  home.packages = with pkgs; [
    ...
    age
  ];
  ...
}
```

Ne...