---
title: Taking SSH Off the Internet With Cloudflare Tunnel and Access - Pt3
url: https://blog.zsec.uk/ssh-ghost-3/
source: ZephrSec - Adventures In Information Security
date: 2026-11-22
fetch_date: 2026-11-23T10:02:59.305341
---

# Taking SSH Off the Internet With Cloudflare Tunnel and Access - Pt3

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

# Taking SSH Off the Internet With Cloudflare Tunnel and Access - Pt3

Going further: checking it all from the outside, short-lived SSH certificates and hardware keys, the mistakes that bit me, OS-level hardening and housekeeping, re-checking the lot against a critical nginx CVE before moving to nginx.org's packages, and a recap of the whole series.

[Andy Gill](/author/andy/)
/
22 November 2026
/
15 min read
/

 views

![](/content/images/size/w30/2026/11/L1060285.jpg)
![Close-up of a metal sign with the cut-out numbers 0300, a magazine and a plant blurred behind it](/content/images/size/w1200/2026/11/L1060285.jpg)

0300, ZephrSnaps

On this page

On this page

If you haven't read Parts 1 and 2, check them out first, as this is the last of the three and carries straight on from them.

[Part 1](https://blog.zsec.uk/ssh-ghost-1/) closed the SSH port and [Part 2](https://blog.zsec.uk/ssh-ghost-2/) locked the origin and added detection. This part covers the remaining hardening: outside verification, further SSH tightening, the mistakes I made, and OS-level work that matters on the same box.

In this final part I'm going to cover:

* Checking it all from the outside
* Going further with SSH: short-lived certificates, hardware keys and tighter settings
* Locking down the Cloudflare account that everything now depends on
* The mistakes that bit me along the way
* Kernel and OS hardening, plus housekeeping
* Re-checking it all against a critical nginx CVE, then moving to nginx.org's packages
* What all of this doesn't protect against

## Step 6: Check It From the Outside

"Done" meant a scan of the origin IP finds nothing, so scan it from a machine that isn't the server, on a network that isn't Cloudflare's. Scanning your own server is normally fine, but check your provider's terms first.

```
nmap -Pn -p- --open <origin-ip>                # expect no open ports
sudo nmap -Pn -sU --top-ports 50 <origin-ip>   # and nothing on common UDP ports
ssh -o ConnectTimeout=5 you@<origin-ip>        # times out
curl -sk --connect-timeout 5 --resolve blog.example.com:443:<origin-ip> https://blog.example.com/   # times out
```

Then check the ways that should work still do: `curl -sI https://blog.example.com/` returns 200 through Cloudflare, `ssh blog-tunnel` gets you a shell after the Access login, and `/ghost/` asks for the Access login in a private window.

![Diagram: through Cloudflare the blog answers and SSH works after Access, while a scanner on another network finds nothing answering on the origin IP](https://blog.zsec.uk/content/images/2026/11/ssh-pt3-outside-view.png)

From the outside, nothing answers on the origin IP; everything goes through Cloudflare

Keep the origin IP out of anything you publish, including screenshots of these commands.

## Going Further With SSH

Everything above is the baseline, and the sections below go further, roughly in order of how much they add; On this server I've done the short-lived certificates, `AllowUsers` and the MAC trimming, and the rest are options worth weighing up for your own.

### Short-Lived Certificates From Access

Access can act as an SSH certificate authority, so after the Access login `cloudflared` gets a certificate that expires within minutes and the server trusts the CA instead of a list of keys, which means a stolen laptop key is useless on its own.

1. In Zero Trust, find the short-lived certificate settings under Access service credentials, pick your SSH application and generate a certificate, then save the public key it shows on the server as `/etc/ssh/ca.pub`.
2. Add `TrustedUserCAKeys /etc/ssh/ca.pub` to the hardening drop-in, then `sshd -t && systemctl reload ssh`.
3. The certificate's principal is the part of your Access email before the `@`, so if your Unix username doesn't match, map it with `AuthorizedPrincipalsFile /etc/ssh/principals/%u`. I log in as root, so `/etc/ssh/principals/root` holds my principal and nothing else.
4. On the laptop, `cloudflared access ssh-config --hostname xxxxxxxxxx.example.com --short-lived-cert` prints the SSH config block to use, and it replaces the Part 1 `Host blog-tunnel` block rather than sitting alongside it, because `IdentitiesOnly yes` with a fixed `IdentityFile` stops the certificate from ever being offered.
5. Once a certificate login works, and sshd's log shows `ECDSA-CERT` for it rather than a plain key, remove the long-lived key from `authorized_keys`; mine is now empty, so a key copied off my laptop no longer opens anything.

Cloudflare's dashboard labels have changed over time and the newer Access for Infrastructure option uses the WARP client, so check the current docs before you start.

### Hardware-Backed Keys

A FIDO2 security key keeps the private key on the hardware, and `verify-required` makes it ask for the key's PIN on every login:

```
ssh-keygen -t ed25519-sk -O resident -O verify-required -C "you@laptop"
```

Put the new public key in `authorized_keys` and add `PubkeyAuthOptions verify-required` to the drop-in so sshd rejects signatures made without the PIN, but only once every `-sk` key you use was created with `verify-required`, because keys in a password manager can't meet that requirement.

### Pin the Key to the Tunnel

Every tunnel login arrives from loopback, which means you can restrict the key to loopback in `authorized_keys`:

```
from="127.0.0.1,::1" ssh-ed25519 AAAA... you@laptop
```

If sshd were ever reachable on a public address, that key would still be refused from outside, and with certificates the same `from=` option works at the start of a line in the principals file.

### Tighter sshd Settings

```
# add to /etc/ssh/sshd_config.d/00-hardening.conf
AllowUsers root          # or your named user - test a login from a second session first
DisableForwarding yes
ClientAliveInterval 300
ClientAliveCountMax 2
```

`AllowUsers` refuses every other account, including service accounts that somehow gain a key, while `DisableForwarding` (OpenSSH 8.4+) turns off agent, X11, TCP and socket forwarding in one line, and the `ClientAlive` lines drop a connection whose client has stopped responding after about ten minutes (a genuinely idle session stays up, since the client still answers, and OpenSSH 9.2+ has `ChannelTimeout` if you want those closed too).

I run `AllowUsers root` here, since root is the only account that ever logs in, and it's a cheap extra layer even with the port never exposed: any other account is refused before a key or certificate is even looked at, and sshd logs it as `not listed in AllowUsers`, which makes a nice tripwire in its own right.

### Modern Algorithms Only

[ssh-audit](https://github.com/jtesta/ssh-audit?ref=blog.zsec.uk) lists every key exchange, cipher, MAC and host key your server offers, and flags the weak ones:

```
apt install ssh-audit
ssh-audit 127.0.0.1
```

Follow its recommendations for your OpenSSH version, and add a `HostKey /etc/ssh/ssh_host_ed25519_key` line to the drop-in so sshd only offers that key; clients that saved a different key type will warn once and then get on with it.

I've also trimmed the MACs to the ETM SHA-2 variants, so `hmac-sha1` and `umac-64` are gone. With chacha20 or GCM ciphers the MAC isn't used at all, but it tidies up the ssh-audit output, and a quick `ssh -o Ciphers=aes128-ctr -o MACs=hmac-sha1 127.0.0.1` should now fail with `no matching MAC found`:
...