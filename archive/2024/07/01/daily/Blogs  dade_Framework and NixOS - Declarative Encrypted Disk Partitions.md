---
title: Framework and NixOS - Declarative Encrypted Disk Partitions
url: https://0xda.de/blog/2024/06/framework-and-nixos-declarative-encrypted-disk-partitions/
source: Blogs  dade
date: 2024-07-01
fetch_date: 2025-10-06T17:41:02.900253
---

# Framework and NixOS - Declarative Encrypted Disk Partitions

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/06/framework-and-nixos-declarative-encrypted-disk-partitions/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

12 minutes

# [Framework and NixOS - Declarative Encrypted Disk Partitions](https://0xda.de/blog/2024/06/framework-and-nixos-declarative-encrypted-disk-partitions/)

This is part 4 in my series of posts learning how to setup NixOS on my Framework 16" AMD laptop. It is not meant as a guide, necessarily, but more as a captain’s log of my thoughts and processes along the way.

* [Framework and NixOS - Day One](https://0xda.de/blog/2024/06/framework-and-nixos-day-one/)
* [Framework and NixOS - Day Two](https://0xda.de/blog/2024/06/framework-and-nixos-day-two/)
* [Framework and NixOS - Secure Boot](https://0xda.de/blog/2024/06/framework-and-nixos-secure-boot-day-three/)

## Full Disk Encryption

As a self-respecting security person, I can’t very well be walking around with a laptop with an unencrypted disk.

But here’s my dilemma. I’ve already partitioned my disk when I did the original install and I’m not using luks. Additionally, my disk partition isn’t particularly declarative – it’s not actually tracked in my configuration at all, so if I want to replicate my operating system in the future, I’d have to remember to set it all up just the right way.

Since I only have the one root partition right now, I need to back up a few files that I don’t want to lose before I do any partitioning. In particular, I’m going to save the contents of my `/etc/secureboot` directory that I generated earlier, as well as just save my whole `/home/dade` directory. In the future I’d like to avoid saving this whole directory all willy nilly like this, but right now I’d prefer to not lose any of the state that I’ve accumulated.

It turns out I can’t copy a lot of things from my home directory over to my flash drive, because a bunch of things are symlinks to my nix store. That’s okay, though – I have most everything I need, and anything in my nix store should be recoverable by just building my config again on the new disk layout when I’m done.

### Disk partitioning

I’ll be using [disko](https://github.com/nix-community/disko) to setup a declarative disk partitioning scheme, as well as indicate my preference for a luks encrypted volume. I also want to be wary of my future intentions to use [impermanence](https://github.com/nix-community/impermanence).

I think to get started, I’m going to use the [luks btrfs subvolumes example from the disko repository](https://github.com/nix-community/disko/blob/master/example/luks-btrfs-subvolumes.nix). This looks like it’ll be similar to what I want to do with impermanence and at least get me started.

One thing of note is that the disko nix configuration used here uses a key file, or I can comment it out and specify a password file for an interactive password entry when I boot up my laptop. You’ll see a bit later on that I opted for a password entry, since this volume will contain my entire operating system, so using a key file is a bit harder than I’d like to figure out.

#### Adding disko as an input

First up, let’s add disko as an input to our `flake.nix` file.

```
{
  inputs = {
  ...
    disko = {
      url = "github:nix-community/disko";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };
  ouputs = { self, nixpkgs, disko, lanzaboote, ...}@inputs: {
	  nixosConfigurations.serenity = nixpkgs.lib.nixosSystem {
	    specialArgs = { inherit inputs; };
	    modules = [
	      disko.nixosModules.disko
	      lanzaboote.nixosModules.lanzaboote
	      ./hosts/serenity/configuration.nix
	      inputs.home-manager.nixosModules.default
	    ];
	  };
  };
}
```

I’m going to do a nixos-rebuild switch here, just to make sure the disko input gets picked up correctly. If all goes well, my next rebuild is going to reformat my drive, so this will likely be my last time rebuilding before the switch. I anticipate needing to boot into a live media to do the next rebuild, otherwise the rebuild will destroy the contents of the disk and nix will immediately stop working. But for now we’re going to stay in our nice environment and setup the disko configuration.

Since we’re going to base our config off the luks-btrfs-subvolumes example mentioned above, let’s get that onto our disk to start making it match what we want. To do this, I used `nix-shell -p wget` to open a shell with wget installed, then `wget https://raw.githubusercontent.com/nix-community/disko/master/example/luks-btrfs-subvolumes.nix -O ~/nixcfg/hosts/serenity/disko-config.nix`.

#### Setting up my disko config

Based on the next steps of the [Disko Quickstart](https://github.com/nix-community/disko/blob/master/docs/quickstart.md), it’s supposed to be time to boot into our installer image so we can modify the disk without issue. But I’m going to skip that just a little bit and make some tweaks to my disko-config.nix and commit it to my repo. It’s kind of a pain to use ssh to pull my nixcfg from a private repository from a live installer, so I’m going to try to get it as close to setup as possible and then do a little mount trick after I boot into the live media.

At this point we can get the disk name, `nvme0n1`, which *should* remain consistent for the lifecycle of my Framework laptop. Even if I add an additional drive, `nvme0n1` should be a consistent name to refer to this drive. We’re also going to comment out the `keyFile` and `additionalKeyFiles` settings, and uncomment the passwordFile so that we can set a password for our lukscrypt volume when we run disko.

```
{
  disko.devices = {
    disk = {
      main = {
        type = "disk";
        device = "/dev/nvme0n1";
        content = {
          type = "gpt";
          partitions = {
            ESP = {
              size = "512M";
              type = "EF00";
              content = {
                type = "filesystem";
                format = "vfat";
                mountpoint = "/boot";
                mountOptions = [
                  "defaults"
                ];
              };
            };
            luks = {
              size = "100%";
              content = {
                type = "luks";
                name = "crypted";
                # disable settings.keyFile if you want to use interactive password entry
                passwordFile = "/tmp/secret.key"; # Interactive
                settings = {
                  allowDiscards = true;
                  #keyFile = "/tmp/secret.key";
                };
                #additionalKeyFiles = [ "/tmp/additionalSecret.key" ];
                content = {
                  type = "btrfs";
                  extraArgs = [ "-f" ];
                  subvolumes = {
                    "/root" = {
                      mountpoint = "/";
                      mountOptions = [ "compress=zstd" "noatime" ];
                    };
                    "/persist" = {
                      mountpoint = "/persist";
                      mountOptions = [ "compress=zstd" "noatime" ];
                    };
                    "/nix" = {
                      mountpoint = "/nix";
                      mountOptions = [ "compress=zstd" "noatime" ];
                    };
                    "/swap" = {
                      mountpoint = "/.swapvol";
                      swap.swapfile.size = "16G";
                    };
                  };
                };
              };
            };
          };
        };
      };
    };
  };
}
```

At this point, I’m...