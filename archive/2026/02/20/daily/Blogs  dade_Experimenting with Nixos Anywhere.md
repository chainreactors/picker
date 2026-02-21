---
title: Experimenting with Nixos Anywhere
url: https://0xda.de/blog/2026/02/experimenting-with-nixos-anywhere/
source: Blogs  dade
date: 2026-02-20
fetch_date: 2026-02-21T04:00:26.095650
---

# Experimenting with Nixos Anywhere

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2026/02/experimenting-with-nixos-anywhere/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

7 minutes

# [Experimenting with Nixos Anywhere](https://0xda.de/blog/2026/02/experimenting-with-nixos-anywhere/)

In preparation for migrating my servers to NixOS, I want to get the deployment process down. For simplicity, I’m going to use [nixos-anywhere](https://github.com/nix-community/nixos-anywhere) to deploy to a new ubuntu server. This will make it really easy to start with a basic server from any provider (or from my ESXi host) and get to the nixos configuration I want.

One of the problems I’ve run into with how my nix config is setup so far is that my home-manager configuration assumes I will always be deploying my home config to a desktop environment. This isn’t necessarily true, so I’ll want to revisit that later to distinguish between server-home and desktop-home. But for now, I’m going to setup my disko configuration and test it out.

One of the things that I’m not sure about for my disko config is my device setting - `device = "/dev/disk/by-diskseq/1";` I first tried to use `by-diskseq` thinking that I could avoid hardcoding in the disk UUID, which would make this more reusable.

Testing my configuration, which I’m calling `ds1` in my flake, should be as easy as the following. But unfortunately I’m operating from my macbook, which has a different architecture, so even this test doesn’t work. The cross-architecture problems are going to be the bane of my existence until I figure out how to fix it. But that’ll be a problem for later.

```
nix run github:nix-community/nixos-anywhere -- --flake ./github/0xdade/nixcfg#ds1 --vm-test
```

Since I can’t easily test, instead I took a snapshot of the VM in ESXi and I’m going to just test in “production” – this server isn’t useful for anything yet and I can just revert the snapshot if I need to. To prepare to run the nixos-anywhere installer, I just need to give myself SSH access to the server as the root user (so that I can avoid being prompted for sudo).

```
nix run github:nix-community/nixos-anywhere -- --generate-hardware-config nixos-generate-config ~/github/0xdade/nixcfg/hosts/nixos/ds1/hardware-configuration.nix --flake ~/github/0xdade/nixcfg#ds1 --target-host root@51.81.64.17
```

After I run this, it appears to download some stuff and then use kexec to reboot into NixOS. It reboots and nixos-anywhere picks up where it left off, but immediately fails the disko configuration because my earlier decision about `by-diskseq` turned out to be a bad one.

```
Problem opening /dev/disk/by-diskseq/1 for reading! Error is 2.
The specified file does not exist!
Information: Creating fresh partition table; will override earlier problems!
Caution! Secondary header was placed beyond the disk's limits! Moving the
header, but other problems may occur!
Unable to open device '' for writing! Errno is 2! Aborting write!
```

Instead, I think I’ll try to install this with `/dev/sda`, since I’m installing to a server with only one disk, and that will be my most common deployment pattern. I think I can override this value on a per-server basis when deploying, but that relies on specific imperative commands, which I’d like to try to minimize as much as possible. But I also don’t want to rely on disk UUIDs where every disk configuration has to be exactly aligned with the server I’m deploying it on. It’s just not very reusable.

Not sure what to do next, I figured I’ll just try to re-run my `nixos-anywhere` command and see if it can pick up where it left off. Thankfully it seems like it does, which means so far I don’t need to restore the snapshot. I am getting periodic errors about the architecture difference, I imagine maybe nixos-anywhere was trying to save time by starting builds locally to copy them over later. But the errors don’t appear to be hard blocking, which means nixos-anywhere probably has fallback behavior that works correctly.

A few minutes later and my terminal shows:

```
Installation finished. No error reported.
installation finished!
### Rebooting ###
Pseudo-terminal will not be allocated because stdin is not a terminal.
### Waiting for the machine to become unreachable due to reboot ###
mux_client_request_session: read from master failed: Broken pipe
ssh: connect to host 51.81.64.17 port 22: Connection refused
### Done! ###
```

Neat. Let’s give it a few minutes and reboot, see what happens. If my configuration is correct, I should be able to ssh to `dade@<ip>` with my SSH key and correctly use sudo with the password I set in my configuration. I went with a barebones deployment, so there shouldn’t be too many things running yet, and shouldn’t be too many things that could go wrong.

## Hardware-configuration?

So I guess there was one thing that could go wrong. The nixos-anywhere command I ran that generated my hardware-configuration.nix file for the server sets the default value for networking.useDHCP to true. `networking.useDHCP = lib.mkDefault true;` – this server doesn’t use DHCP, and in fact most internet-routable servers probably aren’t using DHCP. But of course, I didn’t see this until after the reboot, so now I have to decide how to continue.

I could restore the snapshot and re-try from the beginning. That would be the best way to get the full end-to-end nixos-anywhere experience and make sure it works for the future. But for now I’m going to just try using the ESXi console to login and see if I can fix it.

Unfortunately for me, my password for this machine is a 32 character randomly generated password from my password manager, and I can’t paste into the ESXi console. So I have to type it in manually, and after a few attempts, I figured out that when I get the password wrong, it tells me as much. When I get the password correct, it is just redirecting me back to the login screen. This represents a problem, maybe my user’s shell isn’t set up correctly or something, I’m not sure. I guess it’s time to restore from snapshot.

Thankfully the snapshot restore is nearly instant, so I modified my `hardware-configuration.nix` for the server to turn off DHCP and hopefully that prevents me from getting locked out via SSH. Or at least, hopefully it results in the SSH server listening.

Unfortunately, re-running the same command caused the entire hardware-configuration.nix file to get rewritten back to the “scanned” value. So that’s problematic. I’ll try rearranging my flake so that `hardware-configuration.nix` comes before `ds1/default.nix` and then set `networking.useDHCP = false;` in the default configuration. Maybe this will cause the DHCP value to be ignored and the specific IP address to be handled correctly.

Unfortunately, still nothing. SSH does not appear to have come back up, and I still can’t login, for some reason.

## Disk Problems?

After trying several more things, I didn’t really get anywhere. SSH still wasn’t coming up, and the console still wasn’t working. But once in a while the console would hang for a little bit and then flash an error message before resetting the screen to the login window. So I recorded my screen and discovered the error `Unable to cd to /home/dade`. That gives me… something, I guess? I’m not sure why it’s happening, but at least gives me something to start looking at.

After a bit of searching, I found an [Incorrect Home Directory Permissions](https://github.com/NixOS/nixpkgs/issues/10888) github issue from NixOS. This looks to be a problem with decl...