---
title: age v1.3.2
url: https://kitploit.com/en/posts/github-filosottile-age-v132
source: Kitploit
date: 2026-08-29
fetch_date: 2026-08-30T07:41:54.533618
---

# age v1.3.2

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/8927/c2a391f1769197fe312fa58d0d27858e0f023740d67cde4236d508f71cee7814.png)

New releaseAug 29, 2026

# age v1.3.2

A simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and UNIX-style composability.

Share

![The age logo, a wireframe of St. Peters dome in Rome, with the text: age, file encryption](https://raw.githubusercontent.com/FiloSottile/age/main/logo/logo.svg)

[![Go Reference](https://pkg.go.dev/badge/filippo.io/age.svg)](https://pkg.go.dev/filippo.io/age)
[![man page](https://raw.githubusercontent.com/filosottile/age/HEAD/%3Chttps:/img.shields.io/badge/age(1)-man%20page-lightgrey%3E)](https://filippo.io/age/age.1)
[![C2SP specification](https://img.shields.io/badge/%C2%A7%23-specification-blueviolet)](https://age-encryption.org/v1)

age is a simple, modern and secure file encryption tool, format, and Go library.

It features small explicit keys, post-quantum support, no config options, and UNIX-style composability.

root@kitploit:~

```
$ age-keygen -o key.txt
Public key: age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
$ tar cvz ~/data | age -r age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p > data.tar.gz.age
$ age --decrypt -i key.txt data.tar.gz.age > data.tar.gz
```

📜 The format specification is at [age-encryption.org/v1](https://age-encryption.org/v1). age was designed by [@benjojo](https://github.com/benjojo) and [@FiloSottile](https://github.com/FiloSottile).

🦀 An alternative interoperable Rust implementation is available at [github.com/str4d/rage](https://github.com/str4d/rage).

🌍 [Typage](https://github.com/FiloSottile/typage) is a TypeScript implementation. It works in the browser, Node.js, Deno, and Bun.

🔑 Hardware PIV tokens such as YubiKeys are supported through the [age-plugin-yubikey](https://github.com/str4d/age-plugin-yubikey) plugin.

✨ For more plugins, implementations, tools, and integrations, check out the [awesome age](https://github.com/FiloSottile/awesome-age) list.

💬 The author pronounces it `[aɡe̞]` [with a hard *g*](https://translate.google.com/?sl=it&text=aghe), like GIF, and it's always spelled lowercase.

## Installation

|  |  |
| --- | --- |
| Homebrew (macOS or Linux) | `brew install age` |
| MacPorts | `port install age` |
| Windows | `winget install --id FiloSottile.age` |
| Alpine Linux v3.15+ | `apk add age` |
| Arch Linux | `pacman -S age` |
| Debian 12+ (Bookworm) | `apt install age` |
| Debian 11 (Bullseye) | `apt install age/bullseye-backports` ([enable backports](https://backports.debian.org/Instructions/#index2h2) for age v1.0.0+) |
| Fedora 33+ | `dnf install age` |
| Gentoo Linux | `emerge app-crypt/age` |
| Guix System | `guix package -i age` |
| NixOS / Nix | `nix-env -i age` |
| openSUSE Tumbleweed | `zypper install age` |
| Ubuntu 22.04+ | `apt install age` |
| Void Linux | `xbps-install age` |
| FreeBSD | `pkg install age` (security/age) |
| OpenBSD 6.7+ | `pkg_add age` (security/age) |
| Chocolatey (Windows) | `choco install age.portable` |
| Scoop (Windows) | `scoop bucket add extras && scoop install age` |

On Windows, Linux, macOS, and FreeBSD you can use the pre-built binaries.

root@kitploit:~

```
https://dl.filippo.io/age/latest?for=linux/amd64
https://dl.filippo.io/age/v1.3.1?for=darwin/arm64
...
```

If you download the pre-built binaries, you can check their [Sigsum proofs](https://github.com/filosottile/age/blob/HEAD/SIGSUM.md).

If your system has [a supported version of Go](https://go.dev/dl/), you can build from source.

root@kitploit:~

```
go install filippo.io/age/cmd/...@latest
```

Help from new packagers is very welcome.

## Usage

For the full documentation, read [the age(1) man page](https://filippo.io/age/age.1).

root@kitploit:~

```
Usage:
    age [--encrypt] (-r RECIPIENT | -R PATH)... [--armor] [-o OUTPUT] [INPUT]
    age [--encrypt] --passphrase [--armor] [-o OUTPUT] [INPUT]
    age --decrypt [-i PATH]... [-o OUTPUT] [INPUT]

Options:
    -e, --encrypt               Encrypt the input to the output. Default if omitted.
    -d, --decrypt               Decrypt the input to the output.
    -o, --output OUTPUT         Write the result to the file at path OUTPUT.
    -a, --armor                 Encrypt to a PEM encoded format.
    -p, --passphrase            Encrypt with a passphrase.
    -r, --recipient RECIPIENT   Encrypt to the specified RECIPIENT. Can be repeated.
    -R, --recipients-file PATH  Encrypt to recipients listed at PATH. Can be repeated.
    -i, --identity PATH         Use the identity file at PATH. Can be repeated.

INPUT defaults to standard input, and OUTPUT defaults to standard output.
If OUTPUT exists, it will be overwritten.

RECIPIENT can be an age public key generated by age-keygen ("age1...")
or an SSH public key ("ssh-ed25519 AAAA...", "ssh-rsa AAAA...").

Recipient files contain one or more recipients, one per line. Empty lines
and lines starting with "#" are ignored as comments. "-" may be used to
read recipients from standard input.

Identity files contain one or more secret keys ("AGE-SECRET-KEY-1..."),
one per line, or an SSH key. Empty lines and lines starting with "#" are
ignored as comments. Passphrase encrypted age files can be used as
identity files. Multiple key files can be provided, and any unused ones
will be ignored. "-" may be used to read identities from standard input.

When --encrypt is specified explicitly, -i can also be used to encrypt to an
identity file symmetrically, instead or in addition to normal recipients.
```

### Multiple recipients

Files can be encrypted to multiple recipients by repeating `-r/--recipient`. Every recipient will be able to decrypt the file.

root@kitploit:~

```
$ age -o example.jpg.age -r age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p \
    -r age1lggyhqrw2nlhcxprm67z43rta597azn8gknawjehu9d9dl0jq3yqqvfafg example.jpg
```

#### Recipient files

Multiple recipients can also be listed one per line in one or more files passed with the `-R/--recipients-file` flag.

root@kitploit:~

```
$ cat recipients.txt
# Alice
age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
# Bob
age1lggyhqrw2nlhcxprm67z43rta597azn8gknawjehu9d9dl0jq3yqqvfafg
$ age -R recipients.txt example.jpg > example.jpg.age
```

If the argument to `-R` (or `-i`) is `-`, the file is read from standard input.

### Post-quantum keys

To generate hybrid post-quantum keys, which are secure against future quantum
computer attacks, use the `-pq` flag with `age-keygen`. This may become the
default in the future.

Post-quantum identities start with `AGE-SECRET-KEY-PQ-1...` and recipients with
`age1pq1...`. The recipients are unfortunately ~2000 characters long.

root@kitploit:~

```
$ age-keygen -pq -o key.txt
$ age-keygen -y key.txt > recipient.txt
$ age -R recipient.txt example.jpg > example.jpg.age
$ age -d -i key.txt example.jpg.age > example.jpg
```

Support for post-quantum keys is built into age v1.3.0 and later. Alternatively,
the `age-plugin-pq` binary can be installed and placed in `$PATH` to add support
to any version and implementation of age that supports plugins. Recipients will
work out of the box, while identities will have to be converted to plugin
identities with `age-plugin-pq -identity`.

### Passphrases

Files can be encrypted with a passphrase by using `-p/--passphrase`. By default age will automatically generate a secure passphrase. Passphrase protected files are automatically detected at decrypt time.

root@kitploit:~

```
$ age -p secrets.txt > secrets.txt.age
Enter passphrase (leave empty to autogenerate a secure ...