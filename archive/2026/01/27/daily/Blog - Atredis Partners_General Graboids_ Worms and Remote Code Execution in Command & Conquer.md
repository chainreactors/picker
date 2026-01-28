---
title: General Graboids: Worms and Remote Code Execution in Command & Conquer
url: https://www.atredis.com/blog/2026/1/26/generals
source: Blog - Atredis Partners
date: 2026-01-27
fetch_date: 2026-01-28T03:33:54.415004
---

# General Graboids: Worms and Remote Code Execution in Command & Conquer

[0](/cart)

[Skip to Content](#page)

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

# General Graboids: Worms and Remote Code Execution in Command & Conquer

Jan 27

Written By [Bryan Alexander](/blog?author=67c88e52079bf056021dbb94)

*[this work was conducted collaboratively by Bryan Alexander and Jordan Whitehead]*

This post details several vulnerabilities discovered in the popular online game Command & Conquer: Generals. We recently presented some of this work at an information security conference and this post contains technical details about the game’s network architecture, its exposed attack surface, discovered vulnerabilities, and full details of a worm we developed to demonstrate impact.

Full source code, including PoCs, can be found in our public Github repository [here](https://github.com/atredispartners/general-graboids). Though the game is considered end-of-life by Electronic Arts, publicly available community patches are available addressing these issues; for more information see [this project](https://github.com/TheSuperHackers/GeneralsGameCode?tab=readme-ov-file#running-the-game).

## Research introduction

In early 2025, EA Games released the [source code](https://github.com/electronicarts/CnC_Generals_Zero_Hour) for Command & Conquer: Generals (C&C:G), the final installment in the real-time strategy (RTS) series popular in the late 1990’s and early 2000’s. Included in this source release was Zero Hour, the first and only expansion released in 2003, the same year as Generals. The game was released with both single and multiplayer gameplay, with multiplayer supporting LAN and online lobbies via the GameSpy service. Gamespy eventually went defunct in 2014 and along with it the online C&C:G servers.

[Junkyard](https://www.districtcon.org/junkyard) is an end-of-life pwnathon where researchers bring zero-day vulnerabilities to end-of-life (EoL) products, be it hardware, software, firmware, or a combination of the three. Points are given based on impact, presentation engagement and quality, and overall silliness. The event is held during Districtcon, a relatively new information security conference held yearly in Washington DC. We loved the idea of the event and were eager to identify potential targets to contribute. C&C:G fit the bill as both interesting and EoL’d.

When we first started the project we were kicking around ideas for fuzzing the network layer, but once we spent a little bit of time with the code, we found there really was no need.

## Target overview

The source code includes all core components including the engine, networking stack, and various clients, but does not include models and other proprietary dependencies (such as third-party licensed tooling). This means the game cannot be built straight from the repository as is. Instead of attempting to build the game, we instead picked up a few licenses from Steam to provide dynamic instrumentation alongside our static code review.

When a client starts a game lobby, UDP port 8086 is opened up. This is the lobby port and exclusively processes meta-game commands and requests, such as player join, leave, chat, and more. For game packets used to synchronize state, trigger actions, and other combat activities, a separate port is opened once the game begins on port 8080.

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/0a8948a5-c754-401b-b620-fb222a9ae251/network-arch.jpg)

C&C:G Network Architecture

While C&C:G has a peer-to-peer based networking architecture where the host can function as a packet router to all clients, it’s not relevant to the overall attack surface. Each client that connects must be accessible over both of these ports. When played on LAN, this means 0.0.0.0:8086 and 0.0.0.0:8088 must both be routable.

Packet format to both ports follows a similar structure with a few key differences:

```
+-------------------------------------------------------------+
| Wordwise XOR/Endian-swap Encrypted Payload                  |
|                                                             |
|   +----------------------+--------------------------------+ |
|   | CRC32 (LE)           | 4 bytes                        | |
|   +----------------------+--------------------------------+ |
|   | Magic                | 0D F0                          | |
|   +----------------------+--------------------------------+ |
|   | Header               | 1 bytes                        | |
|   +----------------------+--------------------------------+ |
|   | Data                 | up to MAX_FRAG_SIZE bytes      | |
|   +----------------------+--------------------------------+ |
|   | Padding              | 4 byte boundary                | |
|   +-------------------------------------------------------+ |
+-------------------------------------------------------------+
```

The above is the general shape of each packet, which includes a mandatory four byte CRC32 and two byte magic header. Each packet is XOR encoded using a hard-coded key and has a relatively robust packet fragmentation mechanism.

The header is a type header that roughly follows the standard tag-length-value (TLV) format and is recursively parsed by receiving clients. The following is an example of a `NETCOMMANDTYPE_FILE` packet (received on the lobby port):

```
+---------+---------------------------+-------------------------------+
| Offset  | Bytes                    | Description                    |
+---------+---------------------------+-------------------------------+
| 00–03   | fc 37 a9 53              | CRC32 (LE)                     |
+---------+---------------------------+-------------------------------+
| 04–05   | 0d f0                    | Magic                          |
+---------+---------------------------+-------------------------------+
| 06      | 54                       | Command Type Tag (‘T’)         |
+---------+---------------------------+-------------------------------+
| 07      | 12                       | Command Type Value             |
+---------+---------------------------+-------------------------------+
| 08      | 44                       | Data Type Tag (‘D’)            |
+---------+---------------------------+-------------------------------+
| 09–N    | <string>                 | First Data Value               |
+---------+---------------------------+-------------------------------+
| N–N+4   | 04 00 00 00              | Data Length (LE uint32)        |
+---------+---------------------------+-------------------------------+
| N–N+4   | 41 41 41 41              | Second Data Value ("AAAA")     |
+---------+---------------------------+-------------------------------+
| N–N     | 40 40                    | Padding (4 byte boundary)      |
+---------+---------------------------+-------------------------------+
```

The type tag is specified at offset 07 (0x12) and the data for that tag follows the data type tag at offset 08. This structure allows each type to individually parse its section and optionally support multiple types per packet.

Message parsing takes place inside [NetPacket](https://github.com/electr...