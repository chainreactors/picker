---
title: warpgate v0.28.0-beta.1
url: https://kitploit.com/en/posts/github-warp-tech-warpgate-v0280-beta1
source: Kitploit
date: 2026-08-30
fetch_date: 2026-08-31T07:52:38.550922
---

# warpgate v0.28.0-beta.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/48433/73f2b2f1cf851724653236bc44f6c736fc81486bdca9f5792a1a52b2adcb202d.gif)

New releaseAug 30, 2026

# warpgate v0.28.0-beta.1

Fully transparent SSH, HTTPS, Kubernetes, MySQL and Postgres bastion/PAM that doesn't need additional client-side software

Share

![](https://assets.kitploit.com/production/public/readmes/48433/73f2b2f1cf851724653236bc44f6c736fc81486bdca9f5792a1a52b2adcb202d.gif)

![Shows a black logo in light color mode and a white one in dark color mode.](https://raw.githubusercontent.com/warp-tech/warpgate/HEAD/.github/readme/brand-dark.svg)

[![GitHub All Releases](https://img.shields.io/github/downloads/warp-tech/warpgate/total.svg?label=DOWNLOADS&logo=github&style=for-the-badge&color=8f8)](https://github.com/warp-tech/warpgate/releases/latest)   [![](https://shields.io/badge/-Nightly%20Builds-fa5?logo=hackthebox&logoColor=444&style=for-the-badge)](https://nightly.link/warp-tech/warpgate/workflows/build/main)   [![Discord](https://img.shields.io/discord/1280890060195233934?style=for-the-badge&color=acc&logo=discord&logoColor=white&label=Discord)](https://discord.gg/Vn7BjmzhtF)   [![Docs](https://shields.io/badge/-DOCUMENTATION-fa5?logo=gitbook&style=for-the-badge&color=26a)](https://warpgate.null.page/docs/)

[![](https://assets.kitploit.com/production/public/readmes/48433/6998b621babf181d2183fec6957328d7ddf439c7a1c7038ae505b1d6217eee7c.webp)](https://ko-fi.com/J3J8KWTF)

---

Warpgate is a smart & fully transparent SSH, HTTPS, Kubernetes, MySQL, PostgreSQL, RDP and VNC bastion host that doesn't require a client app or an SSH wrapper.

* Set it up in your DMZ, add user accounts and easily assign them to specific hosts and URLs within the network.
* Warpgate will record every session for you to view (live) and replay later through a built-in admin web UI.
* Browser-based SSH, RDP and VNC access is built in; native clients continue to work.
* Not a jump host - forwards connection straight to the target in a way that's fully transparent to the client.
* Native 2FA and SSO support (TOTP & OpenID Connect)
* Built-in brute-force protection with IP blocking and user lockout
* Single binary with no dependencies.
* Written in 100% safe Rust.

Supported by:

[![FLOSS/fund badge](https://floss.fund/static/badge.svg)](https://floss.fund)

## Getting started & downloads

* See the [Getting started](https://warpgate.null.page/getting-started/) docs page (or [Getting started on Docker](https://warpgate.null.page/getting-started-on-docker/)).
* [Release / beta binaries](https://github.com/warp-tech/warpgate/releases)
* [Nightly builds](https://nightly.link/warp-tech/warpgate/workflows/build/main)

## Documentation

Full documentation is available at [warpgate.null.page](https://warpgate.null.page/), including:

* [Login Protection](https://warpgate.null.page/login-protection/) - Configure brute-force protection
* [SSO](https://warpgate.null.page/sso/) - Single Sign-On with OpenID Connect
* [Tickets](https://warpgate.null.page/tickets/) - Temporary access credentials

## How is Warpgate different from a jump host / VPN / Teleport?

| Warpgate | SSH jump host | VPN | Teleport |
| --- | --- | --- | --- |
| ✅ **Precise 1:1 assignment between users and services** | (Usually) full access to the network behind the jump host | (Usually) full access to the network | ✅ **Precise 1:1 assignment between users and services** |
| ✅ **No custom client needed** | Jump host config needed | ✅ **No custom client needed** | Custom client required |
| ✅ **2FA out of the box** | 🟡 2FA possible with additional PAM plugins | 🟡 Depends on the provider | ✅ **2FA out of the box** |
| ✅ **SSO out of the box** | 🟡 SSO possible with additional PAM plugins | 🟡 Depends on the provider | Paid |
| ✅ **Command-level audit** | 🟡 Connection-level audit on the jump host, no secure audit on the target if root access is given | No secure audit on the target if root access is given | ✅ **Command-level audit** |
| ✅ **Full session recording** | No secure recording possible on the target if root access is given | No secure recording possible on the target if root access is given | ✅ **Full session recording** |
| ✅ **Non-interactive connections** | 🟡 Non-interactive connections are possible if the clients supports jump hosts natively | ✅ **Non-interactive connections** | Non-interactive connections require using an SSH client wrapper or running a tunnel |
| ✅ **Self-hosted, you own the data** | ✅ **Self-hosted, you own the data** | 🟡 Depends on the provider | SaaS |
| ✅ **Built-in brute-force protection** | 🟡 Requires fail2ban setup | 🟡 Depends on the provider | ✅ **Built-in brute-force protection** |

![image](https://assets.kitploit.com/production/public/readmes/48433/c4afdeab98bbf88031a84f959c602b7616e4d1a872c693f22d57861b4e7d0bf0.png)

|  |  |  |
| --- | --- | --- |
| ![](https://assets.kitploit.com/production/public/readmes/48433/b99fce07b3e16d0c596549e2cbd6f182327062cad9f2fd698b6aafafef79b785.png) | ![](https://assets.kitploit.com/production/public/readmes/48433/a298ec3822cf2af9dfe19267bfa4e28a6e3b881dc50af21993f8e2b507db4fc3.png) | ![](https://assets.kitploit.com/production/public/readmes/48433/5f7d0559adbb4fe977406267e34116726fc5a5172891453c57b1ef57a84ce8f7.png) |

## Reporting security issues

Please use GitHub's [vulnerability reporting system](https://github.com/warp-tech/warpgate/security/policy).

## Project Status

Warpgate is being actively used in enterprise settings.

What's planned and being worked on next is tracked on the public [roadmap](https://github.com/orgs/warp-tech/projects/1/views/2).

## How it works

Warpgate is a service that you deploy on the bastion/DMZ host, which will accept SSH, HTTPS, Kubernetes, MySQL, PostgreSQL, RDP and VNC connections and provide an (optional) web admin UI.

Run `warpgate setup` to interactively generate a config file, including port bindings. See [Getting started](https://warpgate.null.page/getting-started/) for details.

It receives connections with specifically formatted credentials, authenticates the user locally, connects to the target itself, and then connects both parties together while (optionally) recording the session.

When connecting through HTTPS, Warpgate presents a selection of available targets, and will then proxy all traffic in a session to the selected target. You can switch between targets at any time.

You manage the target and user lists and assign them to each other through the admin UI, and the session history is stored in an SQLite database (default: in `/var/lib/warpgate`).

You can also use the admin web interface to view the live session list, review session recordings, logs and more.

## AI transparency disclosure

In late 2025, this project had started accepting AI-assisted contributions. Contributors are required to disclose AI use. I believe that by applying the same high quality standard to all PRs, whether AI-assisted or not, no sacrifice in quality or security needs to be made.

Since AI is a spectrum between braindead vibe bros and autocomplete users, I believe that being transparent about its use helps establish and limit the place of AI in this project.

Architectural and security decisions on this project are 100% human.

## Contributing / building from source

* You'll need Rust, NodeJS and NPM
* Clone the repo
* [Just](https://github.com/casey/just) is used to run tasks - install it: `cargo install just`
* Install the admin UI deps: `just npm install`
* Build the frontend: `just npm run build`
* Build Warpgate: `cargo build` (optionally `--release`)

The binary is in `target/{debug|release}`.

### T...