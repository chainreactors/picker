---
title: The Same Ten Passwords, Twenty Years Later
url: https://stateofsecurity.com/the-same-ten-passwords-twenty-years-later/
source: Instapaper: Unread
date: 2026-09-25
fetch_date: 2026-09-26T06:51:57.897728
---

# The Same Ten Passwords, Twenty Years Later

[Skip to primary content](#content)

# [MSI :: State of Security](https://stateofsecurity.com/)

## Insight from the Information Security Experts

[![MSI :: State of Security](https://stateofsecurity.com/wp-content/uploads/2018/10/MSIblogheader1000x2881_new.jpg)](https://stateofsecurity.com/)

Search

### Main menu

* [Home](https://stateofsecurity.com/)
* [Learn More About MicroSolved, Inc.](https://stateofsecurity.com/microsolved-website/)

### Post navigation

[← Previous](https://stateofsecurity.com/authentication-is-not-the-finish-line-secure-the-token-lifecycle/)

# The Same Ten Passwords, Twenty Years Later

Posted on [September 24, 2026](https://stateofsecurity.com/the-same-ten-passwords-twenty-years-later/ "12:20 pm")  by  [Adam Hostetler](https://stateofsecurity.com/author/ahostetler/ "View all posts by Adam Hostetler")

We’ve been logging the credentials that bots throw at an SSH honeypot (our HoneyPoint Security Server™). Nothing exotic: listeners that accept the handshake, record the username/password pair, and the source IP. After letting this run for a bit, the first thing we noticed was how little the dictionary has changed.

![HoneyComb](https://stateofsecurity.com/wp-content/uploads/2026/09/HoneyComb.jpg "HoneyComb.jpg")

## The numbers

Top usernames over the capture window:

| Username | Tries | Sources |
| --- | --- | --- |
| `root` | 45,302 | 350 |
| `admin` | 3,254 | 256 |
| `user` | 1,978 | 132 |
| `enable` | 1,863 | 12 |
| `test` | 1,414 | 101 |
| `ubuntu` | 1,142 | 125 |
| `user2` | 452 | 26 |
| `debian` | 433 | 39 |
| `deploy` | 387 | 47 |
| `support` | 372 | 104 |

`root` alone accounts for more attempts than everything else combined, by a factor of about four. That’s not surprising. What’s worth noticing is the *sources* column: 350 distinct IPs tried `root`, 256 tried `admin`. This is the broad, low-effort campaign layer to find the most basic common hanging fruit.

Top passwords:

| Password | Tries | Sources |
| --- | --- | --- |
| `123456` | 1,916 | 233 |
| `linuxshell` | 1,841 | 8 |
| `1234` | 746 | 180 |
| `123` | 728 | 124 |
| `password` | 532 | 151 |
| `12345` | 393 | 116 |
| `12345678` | 393 | 88 |
| `1` | 367 | 68 |
| `admin` | 365 | 139 |
| `root` | 322 | 108 |

Strip out `linuxshell` for a second (I’ll come back to it) and this list is indistinguishable from a 2006 SSH brute-force wordlist. `123456`, `password`, `1234`, `admin`, `root`. Nine of the top ten passwords have been in every public leaked-password top-25 for two decades.

The pair frequency shows it well:

| Username | Password | Tries | Sources |
| --- | --- | --- | --- |
| `enable` | `linuxshell` | 1,841 | 8 |
| `admin` | `admin` | 134 | 108 |
| `root` | `123456` | 116 | 89 |
| `root` | `root` | 112 | 91 |
| `root` | `1234` | 104 | 83 |
| `root` | `admin` | 102 | 82 |
| `root` | `password` | 101 | 83 |
| `root` | `12345` | 94 | 72 |
| `user` | `user` | 92 | 74 |
| `admin` | `1234` | 91 | 79 |

`root:root`, `admin:admin`, `user:user`, `root:password`. These are the first guesses in any credential scanner I’ve ever seen.

## Why this is the depressing part

A botnet operator doesn’t keep `root:123456` in the list out of tradition. They keep it because it’s still working somewhere. The credential lists in these tools get pruned and reweighted based on what actually produces shells. If a pair stopped working at scale, it would drop off in favor of something that does, because brute forcing takes time and they don’t want to waste time on passwords that never work.

So the fact that the dictionary hasn’t moved in twenty years isn’t a statement about attackers being lazy. It’s a statement about the install base. Somewhere out there, a measurable fraction of internet-facing SSH is still `root` with a password from the top ten, and the population is stable enough that the guessing strategy hasn’t needed to evolve.

That’s the number I’d actually like to know and can’t measure from this side: the hit rate. The honeypot only sees the attempts. But the attempts are the derivative of the success rate, and the derivative is flat.

## The outlier: `enable` / `linuxshell`

One pair dominates the table and doesn’t fit the pattern. `enable:linuxshell` was tried 1,841 times from only 8 sources. Compare `root:123456`: 116 tries from 89 sources.

Eight IPs hammering one specific pair means a single campaign, not the ambient background. `enable` is the Cisco IOS privilege-escalation command, and `enable`-as-a-username shows up in IoT and embedded-device wordlists that were forked from Mirai. `linuxshell` could be a default from a specific device family or firmware. This particular scanner seems to be built for a particular class of embedded gear, and it doesn’t care that it’s talking to something that isn’t that gear. It’s going to try the same pair 200+ times per source regardless.

If you filter this out, the remaining data is almost pure legacy dictionary.

## The newcomers

Here’s the list of usernames that aren’t in the standard brute-force set:

| Username | Tries | Sources |
| --- | --- | --- |
| `enable` | 1,863 | 12 |
| `prueba` | 235 | 40 |
| `noreply` | 220 | 30 |
| `claude` | 127 | 22 |
| `testuser` | 109 | 35 |
| `deployer` | 103 | 29 |
| `frappe` | 100 | 24 |
| `openclaw` | 78 | 13 |
| `alex` | 69 | 33 |
| `trader` | 67 | 15 |

Most of these are explainable. `prueba` is Spanish for “test”. `frappe` is the default service account for the Frappe/ERPNext stack. `trader` is aimed at crypto trading bots, which tend to run on cheap VPSes with hastily created accounts. `deployer` and `testuser` are what people name accounts when they’re not thinking about it.

Two are new: `claude` and `openclaw`.

`claude` got 127 tries from 22 sources; `openclaw` got 78 from 13. Neither existed in any wordlist I’ve seen before the last year or two. What they have in common is obvious: both are names of AI agent tooling, and both are the kind of name someone would pick for a dedicated Unix user when standing up an agent on a box. `useradd claude`, drop the agent config in its home directory, give it a password so you can `su` into it, forget about it.

Attackers have noticed. The reasoning is straightforward from their side: agent hosts are a new class of machine that is (a) internet-facing, (b) frequently set up in a hurry by people who aren’t primarily sysadmins, (c) holding API keys and credentials for whatever the agent has been wired into, and (d) often running with more privilege than a web app would because the agent needs to “do things”. That’s a better target than a generic VPS, and the username is a cheap fingerprint for it.

Twenty-two sources for `claude` is small compared to the 350 for `root`. But `ubuntu` got 125 sources and `debian` got 39. Usernames get added to lists when someone believes there’s a population worth probing. That a couple dozen distinct scanners already carry `claude` and `openclaw` means the operators think the population exists.

## What to do with this

None of this is novel advice. The point is that the data says the advice is still not being followed.

* Firstly, don’t expose SSH (or any similar service) at all if it’s not necessary, allow only IPs that need to access it.
* Disable password authentication on SSH. Keys only. This closes the entire top-ten list in one config line.
* If you can’t, `PermitRootLogin no`. `root` is 80% of the attempts.
* If you’re running an agent under a service account, don’t name it after the product, don’t give it a password, and don’t let it own the SSH login path at all. The agent needs to run as *something*; it doesn’t need to be reachable as that something.
* Rotate anything the agent’s account can read, on the assumption that the account name is now on a list.

The old passwords are still being tried because they still work. The new usernames are being tried because someone expects them to. Both of those are fixable on the defender’s side in an afternoon, which is presumably why they’ve gone unfixed fo...