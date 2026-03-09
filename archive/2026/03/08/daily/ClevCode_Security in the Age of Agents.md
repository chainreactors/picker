---
title: Security in the Age of Agents
url: https://clevcode.org/security-in-the-age-of-agents/
source: ClevCode
date: 2026-03-08
fetch_date: 2026-03-09T04:08:12.285492
---

# Security in the Age of Agents

[Skip to content](#page)

[ClevCode](https://clevcode.org/)

Vulnerability Research, Exploit Development, Reverse-Engineering

### Recent Posts

* [Security in the Age of Agents](https://clevcode.org/security-in-the-age-of-agents/)
* [The Mystery of Skype](https://clevcode.org/the-mystery-of-skype/)
* [Ashley Madison Post-Mortem](https://clevcode.org/ashley-madison-post-mortem/)
* [Android HID device forwarding](https://clevcode.org/android-hid-device-forwarding/)
* [Low-latency VR desktop with Immersed](https://clevcode.org/low-latency-vr-desktop-with-immersed/)

### Categories

* [Ashley Madison](https://clevcode.org/category/ashley-madison/) (1)
* [Codegate](https://clevcode.org/category/codegate/) (1)
* [CTF](https://clevcode.org/category/ctf/) (13)
* [Exploit Development](https://clevcode.org/category/exploit-development/) (7)
* [GCHQ](https://clevcode.org/category/gchq/) (3)
* [Mentorship](https://clevcode.org/category/mentorship/) (1)
* [Plaid CTF](https://clevcode.org/category/plaidctf/) (12)
* [Research](https://clevcode.org/category/research/) (4)
* [Reverse-Engineering](https://clevcode.org/category/reverse-engineering/) (1)
* [Team](https://clevcode.org/category/team/) (3)
* [Uncategorized](https://clevcode.org/category/uncategorized/) (2)
* [VR/XR/MR](https://clevcode.org/category/vr-xr-mr/) (2)
* [Work](https://clevcode.org/category/work/) (1)
* [Writeup](https://clevcode.org/category/ctf/writeup/) (15)

### People

* [Gynvael Coldwind](http://gynvael.coldwind.pl/)
* [Halvar Flake](http://addxorrol.blogspot.com/)
* [j00ru](http://j00ru.vexillium.org/)
* [Joshua J. Drake](http://twitter.com/jduck)
* [Michal Zalewski](http://lcamtuf.blogspot.com/)
* [Rolf Rolles](http://twitter.com/rolfrolles)
* [Sean Heelan](http://seanhn.wordpress.com/)

### Tools

* [BinaryNinja](https://binary.ninja/)
* [GDB](http://www.gnu.org/software/gdb/)
* [Ghidra](https://ghidra-sre.org/)
* [IDA Pro](http://www.hex-rays.com/idapro/)
* [Neovim](https://neovim.io/)
* [OllyDbg](http://www.ollydbg.de/)
* [Vim](http://www.vim.org/)
* [x64dbg](https://x64dbg.com/)

Expand Menu

* [ClevCode](https://clevcode.org/)
* [About](https://clevcode.org/about/)
* [Team](https://clevcode.org/team/)
* [Solving Cicada 3301](https://clevcode.org/cicada-3301/)
* [GCHQ](https://clevcode.org/canyoucrackit-co-uk-gchq-challenge-solution/)
* [pCTF](https://clevcode.org/pctf/)
* [Contact](https://clevcode.org/contact/)

![](https://clevcode.org/wp-content/uploads/2022/10/profile.jpg)

Joel Eriksson

Vulnerability researcher, exploit developer and reverse-engineer. Have spoken at BlackHat, DefCon and the RSA conference. CTF player. Puzzle solver (Cicada 3301, Boxen)

# Security in the Age of Agents

2026-03-08
[0](https://clevcode.org/security-in-the-age-of-agents/#respond)
[Joel Eriksson](https://clevcode.org/author/je/ "Posts by Joel Eriksson")
[Uncategorized](https://clevcode.org/category/uncategorized/)

[](https://clevcode.org/wp-content/uploads/2026/03/openfang-pwn.mp4)

So many AI agent orchestration frameworks and “operating systems” are being released right now, that claim to be built with security in mind – proudly listing their extensive security features, related to everything from their use of cryptography to sandboxes and memory-safe languages.

Then once you take a peek inside, the castle made of sand generally crumbles down fast.

Here we will take a look at one of them, a self-proclaimed Agent Operating System, named [OpenFang](https://openfang.sh)

[![](https://clevcode.org/wp-content/uploads/2026/03/scrshot-25-1024x360.png)](https://clevcode.org/wp-content/uploads/2026/03/scrshot-25.png)

As is often the case, it sounds like security is a priority and that they’ve really thought about security from the ground up. It sounds quite promising, as long as you don’t bother to take a peek under the surface. 16 security systems, sandboxed execution, Merkle audit trail and taint tracking etc.

[![](https://clevcode.org/wp-content/uploads/2026/03/scrshot-26-1024x608.png)](https://clevcode.org/wp-content/uploads/2026/03/scrshot-26.png)

When taking a closer look, the “taint tracking” used to enforce an allowlist of commands for agents could be trivially bypassed in at least four different ways (command-splitting on |, ;, && and || but a whitelisted command followed by & cmd, `cmd`, $(cmd) and <newline>cmd works fine. Overall, they’re fighting a losing game by implementing a command line parsing based sandbox rather than using an actual sandbox (using seccomp-bpf, for instance), a container or a microVM.

As for the AES-256-GCM based auth in the OpenFang P2P protocol, well, besides being vulnerable to a replay attack, the protocol itself is completely in plaintext after the handshake!

Regarding the “WASM sandboxes”, turns out they aren’t actually used for anything, there’s not a single WASM agent in the repo, and since rather than conforming to WASI they require implementing a completely custom API, it’s unlikely that anyone would bother making a WASM based agent in the first place (not even the maintainers do, so).

And as for the “Merkle audit trail”, that audit trail is stored entirely in-memory, so simply restarting the daemon is enough to erase any traces of that trail.

Last but not least, it turns out that even their API key based authentication could be trivially bypassed, so anyone with access to the dashboard URL can get remote code execution. That’s the part I demonstrate in the video at the top, so enjoy. ;)

Note that I’m not against the idea of using AI agents. On the contrary, I think that it will become increasingly important for people to leverage the power of AI to accelerate themselves.

Being able to do so in a way that actually limits the risk and blast radius of any attack is a difficult problem though, which is why it’s one of the things I’m focusing heavily on right now…

To get notified when I start releasing some of the things I do within that space in the future, make sure to register at [GRAFIT](https://grafit.io)

UPDATE: The OpenFang team released an update within a few hours, and although it’s still not perfect they are definitely taking steps in the right direction.
![](https://clevcode.org/wp-content/uploads/2026/03/2026-03-08-202348_1652x1604_scrot.png)

UPDATE 2: After reviewing the fixes in the v0.3.30 release, I sent the maintainers the comments below:

It looks to me that you’re now unconditionally blocking metacharacters even for full mode, which means that even in full mode the agent will not be able to use pipes and shell redirections etc, which severely limits the ability for even a full mode agent to do useful work. You should really look into a proper OS-level based sandbox architecture instead of trying to enforce it on a command-level.

As for the OFP wire protocol issues, messages are still sent in plaintext, so an attacker with the ability to MITM can still inject anything.

It also looks like the broadcast notification mechanism is broken (but it also seems unused!). In the release notes you mention that it requires a shared secret and uses authenticated writes, but you’re generating a nonce and deriving a session key from it, without sharing the nonce -> peers will not be able to derive the correct session key.

You should use the connections you’ve already established to the peers in question to send the “broadcast” notifications as well, instead of establishing new connections for those.

You also have unnecessary unauthenticated fallback paths in the connection\_loop in peer.rs, from read\_message\_authenticated -> read\_message. The fallback paths seems unreachable in practice right now, but having them at all increases the risk of accidentally introducing a vulnerability later.

Regarding the audit trail, that you now persist in sqlite, the core remaining issue here is that it doesn’t really do anything to stop an attacker from erasing their tracks once they have code execution. They can just delete rows from audit\_entries a...