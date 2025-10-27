---
title: My age+YubiKeys Password Management Solution
url: https://words.filippo.io/dispatches/passage/
source: Filippo Valsorda
date: 2022-12-29
fetch_date: 2025-10-04T02:39:14.728359
---

# My age+YubiKeys Password Management Solution

[![Filippo Valsorda](https://assets.buttondown.email/images/1e8b4251-b3e2-4de1-9b95-9f5d0447644d.png)](https://filippo.io)

28 Dec 2022

# My age+YubiKeys Password Management Solution

Password managers are in the news, and it’s the holidays, so it’s as good a time as ever to describe my password and secret management setup. It’s very much not for everyone, but it’s minimal, simple, and has some interesting security properties: even if my laptop were compromised, it would take an attacker a very long time to extract more than a few low-importance secrets.

I use [passage](https://github.com/FiloSottile/passage), a fork of [password-store](https://www.passwordstore.org/) that encrypts files with [age](https://age-encryption.org/) instead of GnuPG, along with [age-plugin-yubikey](https://github.com/str4d/age-plugin-yubikey) by [Str4d](https://github.com/str4d).

## Storage and sync

`passage`, like `pass`, is effectively a script that makes it convenient to store and retrieve encrypted passwords and secrets from the command line. Each secret is stored in a separate file in `$PASSAGE_DIR`, which I keep synced with [Syncthing](https://syncthing.net/) and backed up with [restic](https://restic.net/). Changes are automatically versioned with git.

```
$ passage generate -n example.com 20
[main de2abc4] Add generated password for example.com.
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 example.com.age
The generated password for example.com is:
EOUblkyPqAXHtKT963aP
$ passage -c example.com
Copied example.com to clipboard. Will clear in 45 seconds.
```

## Security

Secrets are encrypted to two keys generated on two YubiKeys with the default settings of age-plugin-yubikey. These keys can’t be extracted or cracked by any attacker, regardless of how compromised my laptop or vault gets. One YubiKey is a USB-C Nano that lives in my laptop, the other one lives on my keychain. If (when!) one breaks, I can use the other to re-encrypt all files to the replacement.

```
age-plugin-yubikey # run interactive setup
age-plugin-yubikey --identity >> $HOME/.passage/identities
age-plugin-yubikey --list >> $HOME/.passage/store/.age-recipients
```

Since age-plugin-yubikey configures keys to require a PIN for every session, and PINs are limited to 3 + 3[1](#fn:puk) attempts before locking, losing a YubiKey is pretty much a non-event. More importantly, since keys are configured to require touch *at every use* and each secret is encrypted separately, **even a full compromise of my laptop wouldn’t let an attacker dump the whole vault at once**: each secret needs a separate physical YubiKey tap to decrypt. I might not notice a decryption failure or two in daily usage, but I will definitely notice something’s off before I tap the YubiKey dozens of times.

Some secrets which I consider especially sensitive and are used rarely are saved in a subdirectory (called “Brooklyn Battery Tunnel”, in case anyone catches the reference) and encrypted only to the keychain YubiKey.[2](#fn:sub) If an attacker wants even one of those secrets, they will have to compromise my laptop and then wait for weeks until I plug in the higher-privilege YubiKey and tap it. If they hijacked the tap to decrypt a different secret, I would immediately notice that the secret I requested didn’t decrypt successfully.

Note that this is designed to fit my threat model: I trust my sync and storage backend, and I’m mostly interested in hardware-binding the secrets to the YubiKey, to rate-limit exfiltration and give myself a chance to recover from compromise.[3](#fn:heresy) If you don’t trust your storage, you’ll want to at the very least set `$PASSAGE_RECIPIENTS_FILE` to a path on the local system, instead of keeping `.age-recipients` files next to the encrypted files, where the storage provider could change them.

## Recovery

The `.age-recipients` files also include the public key for an offline disaster recovery key. I generated the key with `age-keygen`, encrypted it with `age -p`, printed the ciphertext as a QR code, and wrote the random passphrase in pen. This is a bit convoluted, but I don’t trust printers. 🖨️🧐 All this was done in a tmpfs, so nothing reached storage. Only had to do this once, and have been using that key as the anchor for all my disaster recovery data.

I also periodically rsync the passage store to an SD card. That SD card along with a YubiKey is the starting point to reprovision a new laptop. This is kind of a hassle and I might move that role to iCloud Drive now that it’s end-to-end encrypted.

## Mobile

Everyone asks what I do for mobile, and the thing is, I don’t really use passwords on my phone all that often. Most apps stay logged in forever with Face ID, as they should. I also like not carrying access to all my secrets on me, even if the iPhone is probably the most secure device I have.

When I need to log into an app, I generate a QR code with `passage -q`, scan it with the iOS camera app, and copy and paste it. It would be nice if there was an app that used the password management API to automate this, but this happens rarely enough that it’s not worth optimizing for me.

![A screenshot of the iOS camera app scanning a QR code generated by passage](https://assets.buttondown.email/images/837e6b4d-0fcb-4319-aff7-5caba9aec3fe.jpeg)

## p / fzf

A big usability upgrade is a five-lines bash script that uses [fzf](https://github.com/junegunn/fzf) to provide fuzzy search.

```
#! /usr/bin/env bash
set -eou pipefail
PREFIX="${PASSAGE_DIR:-$HOME/.passage/store}"
FZF_DEFAULT_OPTS=""
name="$(find "$PREFIX" -type f -name '*.age' | \
  sed -e "s|$PREFIX/||" -e 's|\.age$||' | \
  fzf --height 40% --reverse --no-multi)"
passage "${@}" "$name"
```

I have it on `$PATH` as `p`, and ⌘-0 brings up iTerm2, so I can do

⌘-0, “p -c”, ↩, “ex”, ↩, tap YubiKey, ⌘-0, ⌘-V

to copy and paste the password for example.com. It fits nicely in muscle memory.

## Future work: yubikey-agent integration

I’m pretty happy with the setup as it is, but there’s one thing still on the roadmap: [yubikey-agent](https://github.com/FiloSottile/yubikey-agent) integration. yubikey-agent is an SSH agent that uses the YubiKey PIV applet like age-plugin-yubikey. It has a native graphical PIN prompt on macOS, is compatible with all servers, and unlike gpg-agent doesn’t need restarting all the time. It also keeps a persistent connection to the PIV applet, which allows it to use the YubiKey’s PIN cache to require the PIN only once per session. Unfortunately, this connection [keeps an exclusive lock on the applet](https://github.com/FiloSottile/yubikey-agent/issues/4) which conflicts with age-plugin-yubikey.

For now, I solved it by adding `killall -SIGHUP yubikey-agent` to the `p` script, and everything works smoothly, despite having to type the PIN when I switch from SSH to passage.

Soon, I plan to make an age-plugin-yubikey-agent which talks to a running instance of yubikey-agent and uses the keys generated by age-plugin-yubikey. This way, I’ll basically never have to type the PIN.

The main blocker is figuring out the protocol to make age-plugin-yubikey-agent talk to yubikey-agent. One compelling option is to use an SSH agent protocol extension, but I need to make sure it doesn’t get forwarded by `ssh -A` by default. It would be pretty surprising if forwarding SSH authentications also forwarded age decryptions. [OpenSSH recently added some support for detecting forwarded requests](https://www.openssh.com/agent-restrict.html), so that might allow me to deny them for the age protocol, and maybe also add a confirmation prompt for forwarded SSH authentication that tells the user what host the remote is trying to authenticate to.

## Bonus: using passage in scripts

A final tip: age-plugin-yubikey delegates the PIN prompt to age via [the plugin protocol](https://github.com/C2SP/C2SP/pull/5), and age has [a pretty good terminal UI](https://github.com/FiloSottile/age/blob/main/cmd/age/tui.go), so it can ask for th...