---
title: Taking SSH Off the Internet With Cloudflare Tunnel and Access - Pt1
url: https://blog.zsec.uk/ssh-ghost-1/
source: ZephrSec - Adventures In Information Security
date: 2026-11-22
fetch_date: 2026-11-23T10:02:58.752062
---

# Taking SSH Off the Internet With Cloudflare Tunnel and Access - Pt1

[Skip to content](#main)

[![ZephrSec - Adventures In Information Security](/content/images/size/w400/2025/05/YoutubeHeader-Recovered-1.png)](https://blog.zsec.uk)

* [About Andy Gill/ZephrFish](https://blog.zsec.uk/about/)
* [My Red Team Course](https://lms.zsec.red/courses/malwareless-adversarial-emulation)
* [ZephrSec](https://zephrsec.com)
* [My Books](https://leanpub.com/b/LearningTheRopes)
* [Photo Blog](https://photos.zsec.uk/)

[Buy me a coffee](https://blog.zsec.uk/support/)

Toggle colour scheme
[Buy me a coffee](https://blog.zsec.uk/support/)
[Subscribe](#/portal/signup)
Menu

[blueteam](/tag/blueteam/)

# Taking SSH Off the Internet With Cloudflare Tunnel and Access - Pt1

Taking SSH off the internet: a clean sshd baseline (and the drop-in ordering trap that silently undoes it), SSH through Cloudflare Tunnel and Access, and closing port 22 without losing the provider's console.

[Andy Gill](/author/andy/)
/
22 November 2026
/
11 min read
/

 views

![](/content/images/size/w30/2026/11/DSC04718.jpg)
![An autumn avenue of trees with fallen leaves either side of the path](/content/images/size/w1200/2026/11/DSC04718.jpg)

An autumn avenue, ZephrSnaps

On this page

On this page

I've been wanting to write more about SSH lockdown for a while, in one evening I took my blog server from "SSH open to the world on port 22" to "no inbound ports except 443, and only from Cloudflare", with SSH now arriving through a Cloudflare Tunnel behind Zero Trust Access.

I've written about locking down SSH before in [Locking Down SSH the Right Way](https://blog.zsec.uk/locking-down-ssh-the-right-way/), but this time I've taken a different route and used Zero Trust, so the service is never exposed publicly at all. I'll go through it step by step, including the bits I got wrong along the way and some of the main lessons learnt.

The trigger was sshole, Özgün Kültekin's write-up of an OpenSSH bug on musl libc ([github.com/oz9un/sshole](https://github.com/oz9un/sshole?ref=blog.zsec.uk)). On `musl`-based hosts (Alpine, OpenWrt, many Docker images) without PAM, an account whose shadow entry is `*` accepts any password between 257 and 1,024 bytes, because musl's `crypt()` returns `"*"` on failure above 256 bytes and that matches the `*` meant to mean "never matches", and the fix is either OpenSSH 10.6p2 or `PasswordAuthentication no`.

My server wasn't affected, since Ubuntu builds OpenSSH against `glibc` rather than `musl` and password logins were already off, but it was a good prompt to ask why a password prompt faces the internet at all.

It ended up long enough that I've split it into three parts: this one takes SSH off the internet, Part 2 locks down the web origin and adds detection and recovery, and Part 3 checks it all from the outside, goes further, and owns up to the mistakes.

Across the three parts I'm going to cover:

1. A clean sshd baseline and the config-ordering trap that silently undoes it
2. SSH through Cloudflare Tunnel + Access, no open port
3. Closing port 22 while keeping the provider's console as a way back in
4. Locking the origin so only *your* Cloudflare zone can reach it, plus Ghost admin behind Access
5. Detection and recovery: auditd, alerts, backups, cloud firewall, patching
6. Checking the result from outside
7. Further SSH hardening
8. The mistakes, including a 16-second outage from one nginx setting

## Starting Point and Goal

The server is a single VPS running my GhostBlog behind Cloudflare, and origin-unmasking techniques turn up often enough that Step 4 treats its IP as already public.

It already had key-only SSH, a host firewall and web ports limited to Cloudflare's IP ranges, so the question was what was still reachable, by whom and from where.

As for cost and time: Cloudflare Tunnel, Access for a handful of users and authenticated origin pulls are all available on Cloudflare's free plan, so beyond the VPS itself none of this costs anything. The SSH side took one evening; the rest grew over the following couple of weeks as I wrote it up and kept finding things to tighten.

| Surface | Before | After |
| --- | --- | --- |
| TCP 22 (SSH) | Open to the internet, rate-limited | Blocked at the cloud firewall unless I open it for the provider's console; day-to-day logins arrive on loopback through Cloudflare Tunnel |
| TCP 80 | Open to Cloudflare ranges | Closed; redirects happen at the Cloudflare edge |
| TCP 443 | Open to Cloudflare ranges, any hostname | Cloudflare ranges + mutual TLS with my own CA, known hostnames only |
| Ghost admin | IP allowlist in nginx | IP allowlist **and** Access login |

The threat model is ordinary for a personal server: internet-wide scanning, credential stuffing, the next sshd bug, and someone pointing their own Cloudflare zone at my origin IP. "Done" means a scan of the origin IP finds nothing, and every way in requires an identity check plus a key or client certificate.

## Step 1: Building My sshd Baseline

While reviewing everything, I learnt that sshd uses the **first** value it reads for most options. On Ubuntu and Debian, `sshd_config` starts with `Include /etc/ssh/sshd_config.d/*.conf` and the drop-ins load in name order, so my hardening file, called `99-hardening.conf`, would only have worked until something dropped in a `50-cloud-init.conf` with `PasswordAuthentication yes`. cloud-init and some packages do exactly that, and because of the load order the `50-` file wins without sshd giving any warning.

**Decide who logs in.** This server has one administrator, so I log in as root, but only with a key or certificate, using `PermitRootLogin prohibit-password`, which means there is no root password for anyone to guess. If more than one person logs in, or you'd rather every root action went through `sudo`, create a named user first and copy your key across before you change anything:

```
adduser you                      # pick your own username; set a strong password for sudo
usermod -aG sudo you
install -d -m 700 -o you -g you /home/you/.ssh
install -m 600 -o you -g you /root/.ssh/authorized_keys /home/you/.ssh/authorized_keys
```

Check from a second terminal that `ssh you@your-host` works and that `sudo -v` accepts your password, then use `PermitRootLogin no` in place of `prohibit-password` below. Whichever route you take, keep your original session open until the end of this step so that a mistake doesn't lock you out.

Name your hardening file so it sorts first, and make public key the *only* method:

```
# /etc/ssh/sshd_config.d/00-hardening.conf
PasswordAuthentication no
KbdInteractiveAuthentication no
PubkeyAuthentication yes
AuthenticationMethods publickey
PermitEmptyPasswords no
PermitRootLogin prohibit-password
X11Forwarding no
MaxAuthTries 3
```

`AuthenticationMethods publickey` is the belt and braces: even if `PasswordAuthentication` gets flipped back on, no password path can complete a login. Check the syntax, apply it, then ask sshd what it will actually do rather than trusting the files:

```
sshd -t && systemctl reload ssh
sshd -T | grep -Ei '^(passwordauthentication|kbdinteractiveauthentication|authenticationmethods|permitrootlogin|usepam) '
```

![Terminal output of sshd -T showing passwordauthentication no, kbdinteractiveauthentication no and authenticationmethods publickey](https://blog.zsec.uk/content/images/2026/11/image-10.png)

`sshd -T` shows what sshd will actually do, not what the files say: no passwords, no keyboard-interactive, public key only

Then prove it from the outside, where a client that refuses to use keys should be told that only `publickey` is on offer:

```
ssh -o PubkeyAuthentication=no -o PreferredAuthentications=password,keyboard-interactive you@your-host
# you@your-host: Permission denied (publickey).
```

![Terminal: an SSH login with key authentication turned off is refused with Permission denied (publickey)](https://blog.zsec.uk/content/images/2026/11/image-11.png)

Refuse to use keys and there's nothing left to try: only `publickey` is on of...