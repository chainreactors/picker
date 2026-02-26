---
title: Kali & LLM: macOS with Claude Desktop GUI & Anthropic Sonnet LLM
url: https://www.kali.org/blog/kali-llm-claude-desktop/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-25
fetch_date: 2026-02-26T04:11:49.532523
---

# Kali & LLM: macOS with Claude Desktop GUI & Anthropic Sonnet LLM

* [Get Kali](https://www.kali.org/get-kali/)
* [Blog](https://www.kali.org/blog/)
* Documentation

  [Documentation Pages](https://www.kali.org/docs/)
  [Tools Documentation](https://www.kali.org/tools/)
  [Frequently Asked Questions](https://www.kali.org/faq/)
  [Known Issues](https://bugs.kali.org/search.php?project_id=1&category_id[]=General%20Bug&category_id[]=Kali%20Package%20Bug&category_id[]=Kali%20Package%20Improvement&status[]=30&status[]=40&status[]=50&sticky=on&sort=id%2Clast_updated&dir=DESC%2CDESC&hide_status=-2&match_type=0)
* Community

  [Community Support](https://www.kali.org/community/)
  [Forums](https://forums.kali.org/)
  [Discord](https://discord.kali.org/)
  [Join Newsletter](https://www.kali.org/newsletter/)
  [Mirror Location](https://http.kali.org/README?mirrorlist)
  [Get Involved](https://www.kali.org/docs/community/contribute/)
* [Courses](https://www.offsec.com/kali-training/courses/?utm_source=kali&utm_medium=web&utm_campaign=menu)
* Developers

  [Git Repositories](https://gitlab.com/kalilinux)
  [Packages](https://pkg.kali.org/)
  [Auto Package Test](https://autopkgtest.kali.org/)
  [Bug Tracker](https://bugs.kali.org/)
  [Kali NetHunter Stats](https://nethunter.kali.org/)
* About

  [Kali Linux Overview](https://www.kali.org/features/)
  [Press Pack](https://gitlab.com/kalilinux/documentation/press-pack/-/archive/main/press-pack-main.zip)
  [Wallpapers](https://www.kali.org/wallpapers/)
  [Kali Swag Store](https://offsec.usa.dowlis.com/kali/view-all.html)
  [Meet The Kali Team](https://www.kali.org/about-us/)
  [Partnerships](https://www.kali.org/partnerships/)
  [Contact Us](https://www.kali.org/contact/)

LIGHT
[ ] DARK

![](https://www.kali.org/blog/kali-llm-claude-desktop/images/banner-kali-claude-desktop.jpg)
Wednesday, 25 February 2026

# Kali & LLM: macOS with Claude Desktop GUI & Anthropic Sonnet LLM

Table of Contents

* [SSH](#ssh)
  + [Kali Setup](#kali-setup)
  + [macOS](#macos)
  + [Testing](#testing)
* [MCP Server (MCP Kali Server)](#mcp-server-mcp-kali-server)
  + [Testing](#testing-1)
* [Claude Desktop](#claude-desktop)
* [MCP Client (Claude Desktop)](#mcp-client-claude-desktop)
  + [Testing](#testing-2)
* [Recap](#recap)

This post will focus on an alternative method of using Kali Linux, moving beyond direct terminal command execution. Instead, we will leverage a Large Language Model (LLM) to translate “natural language” descriptions of desired actions into technical commands. Achieving this setup requires the integration of three distinct systems:

* UI: Apple’s macOS *(Can also use Microsoft Windows, but not covered in this guide)* - with Claude Desktop
* Attacking box: Kali Linux - using various tools
* LLM: *In the cloud* - Anthropic’s Sonnet 4.5

---

The LLM is only part of the story. When paired with Model Context Protocol (MCP)’s, it allows/enables the LLM to seamlessly connect with external sources (data, programs/tools etc).
At a very high level:

1. We can ask a LLM to-do a task via a “prompt”.

* *“Can you please port scan `scanme.nmap.org`, if you find a valid web server, check if `security.txt` exists”*

2. The LLM will understand what we asked it to-do.

* *“First task, I need to use Nmap/Network Mapper to-do a port scan of scan `scanme.nmap.org`”*

3. LLM will then request the MCP to-do any action(s).

* *“Is Nmap installed? Can I access it?”*

4. MCP will run the request and return results

* *`$ nmap scanme.nmap.org`*

5. The LLM will process the results as well as showing it to us as end-users.

* *“I found that `scanme.nmap.org` is up, and contains a web server on port 80/TCP & 443/TCP.”*

6. If needed, could be a loop, and re-run a command/action again back in the MCP until the prompt has been completed/full-filled.

* *“Now I need see if `/.well-known/security.txt` gives `HTTP 200` response”*

Just like the joys of text editors wars *(`vim` vs `emacs` vs `nano`)*, this is not to say its the “best” way to-do it. This is **a way**.
This scenario may work for you, or it may not be acceptable to you *(e.g. privacy)*. That is fine.

---

If you are wonder “Why this setup? Why are you using multiple OSes?”, there are various reasons why!

* You may want a graphical user interface (GUI), which Claude Desktop is.
  + Its an official product from Anthropic, who is making the model we want to run. However Claude Desktop is not officially supported on Linux.
  + There are workarounds (e.g. [community packages](https://github.com/aaddrick/claude-desktop-debian) or [WINE](https://www.winehq.org/), as well as other solutions, such as [5ire](https://github.com/nanbingxyz/5ire), [AnythingLLM](https://anythingllm.com/), [Goose (Desktop)](https://block.github.io/goose/) & [Witsy](https://witsyai.com/)
* It being “free”.
  + *At the time of writing, 2026-01*
* Speed
  + Having Kali running in “the cloud”, may have greater network connection , or be closer to your target - thus speeding things up!

## SSH

We are going to want our macOS box, to be able to talk/interact/communicate to Kali.
For this, we will use SSH.

### Kali Setup

First up, Kali.
If you are using Kali in the cloud, you likely already have SSH pre-setup.
If SSH is not setup, let’s quickly install and run:

```
$ sudo apt update
[...]
$
$ sudo apt install -y openssh-server
[...]
$
$ sudo systemctl enable --now ssh
[...]
$
```

### macOS

Switching over to our macOS machine, open up `Terminal` *(or similar program)*, and either find out public SSH key or generate one:

```
user@Users-MacBook-Pro ~ % ls -lah .ssh
ls: .ssh: No such file or directory
user@Users-MacBook-Pro ~ %
```

This is a clean install, so we will be generating a new key.

---

Generating a new SSH key, is the same steps as doing it on Linux:

```
user@Users-MacBook-Pro ~ % ssh-keygen
Generating public/private ed25519 key pair.
Enter file in which to save the key (/Users/user/.ssh/id_ed25519):
Created directory '/Users/user/.ssh'.
Enter passphrase for "/Users/user/.ssh/id_ed25519" (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /Users/user/.ssh/id_ed25519
Your public key has been saved in /Users/user/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:9JWMFmD6Jhq9gSLVrWSQaqR0hOOfGC5wd/HoMW1CoKU [email protected]
The key's randomart image is:
+--[ED25519 256]--+
|  +oo.  o..      |
| =.B .oo   + .   |
|=.E +.o=. o +    |
|+=.o.+*o+o .     |
|=.=.=o+=S .      |
|.+ + o.=         |
|.   . .          |
|                 |
|                 |
+----[SHA256]-----+
user@Users-MacBook-Pro ~ %
user@Users-MacBook-Pro ~ % cat ~/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFVZPT158E6mNNGrtOXTBQtK/7sXj09gRGZjkyMt82hs [email protected]
user@Users-MacBook-Pro ~ %
```

*Password is not shown*

---

Now, lets add that public SSH key from macOS to Kali, allowing for key authentication.
Our Kali is located at `192.168.1.30`, change the IP to match your setup:

```
user@Users-MacBook-Pro ~ % ssh-copy-id [email protected]
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/Users/user/.ssh/id_ed25519.pub"
The authenticity of host '192.168.1.30 (192.168.1.30)' can't be established.
ED25519 key fingerprint is SHA256:s1EHXZomZxup5ybdUSgTJwnyjwrMBxFSmAgt4+ijhws.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
[email protected]'s password:

Number of key(s) added:        1

Now try logging into the machine, with: "ssh '[email protected]'"
and check to make sure that only the key(s) you wanted were added.

user@Users-MacBook-Pro ~ %
```

*Password is not shown*

This hopefully will be the last time you need to type in your Kali password when connecting via SSH!

---

### Testing

Finally, let’s test it out:

```
user@Users-MacBook...