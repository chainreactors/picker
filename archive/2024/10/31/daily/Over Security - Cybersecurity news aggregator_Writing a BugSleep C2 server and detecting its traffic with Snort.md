---
title: Writing a BugSleep C2 server and detecting its traffic with Snort
url: https://blog.talosintelligence.com/writing-a-bugsleep-c2-server/
source: Over Security - Cybersecurity news aggregator
date: 2024-10-31
fetch_date: 2025-10-06T18:57:21.279577
---

# Writing a BugSleep C2 server and detecting its traffic with Snort

# Cisco Talos Blog

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

![](/content/images/2024/10/NTDR-DeepDive.jpg)

# Writing a BugSleep C2 server and detecting its traffic with Snort

By
[Aaron Boyd](https://blog.talosintelligence.com/author/aaron/)

Wednesday, October 30, 2024 06:00

[RAT](/category/rat/)
[malware](/category/malware/)

In June 2024, security researchers published their analysis of a novel implant dubbed “[MuddyRot](https://blog.sekoia.io/muddywater-replaces-atera-by-custom-muddyrot-implant-in-a-recent-campaign/)”(aka "[BugSleep](https://research.checkpoint.com/2024/new-bugsleep-backdoor-deployed-in-recent-muddywater-campaigns/)"). This remote access tool (RAT) gives operators reverse shell and file input/output (I/O) capabilities on a victim’s endpoint using a bespoke command and control (C2) protocol. This blog will demonstrate the practice and methodology of reversing BugSleep’s protocol, writing a functional C2 server, and detecting this traffic with Snort.

# Key findings

* BugSleep implant implements a bespoke C2 protocol over plain TCP sockets.
* BugSleep operators have demonstrated multiple file-obfuscation techniques to avoid detection.
* BugSleep implements reverse shell, file I/O, and persistence capabilities on the target system.

# Sending and receiving data

This blog will use sample b8703744744555ad841f922995cef5dbca11da22565195d05529f5f9095fbfca for analysis. Two of the lowest functions in the C2 stack, referred to as SendSocket (FUN\_1400034c0) and ReadSocket (FUN\_140003390), are very light wrappers for the send and receive API functions and handle payload encryption. They include some error handling by attempting to send or receive data 10 times before failing.

This protocol uses a pseudo-TLV (Type Length Value) structure with only two types: integer or string. Integers are sent as little-endian 4- or 8-byte values, and strings are prepended with the 4-byte value of its length. Payloads are then encrypted by subtracting a static value from each byte in the buffer (in this sample it is three).

|  |  |  |  |
| --- | --- | --- | --- |
| Type | Value | Plain text | Cipher text |
| IntegerMsg | 6 | 06 00 00 00 | 03 FD FD FD |
| StringMsg | Talos | 05 00 00 00 48 65 6C 6C 6F | 02 FD FD FD 51 5E 69 6C 70 |

*Figure 1: Example of data encryption used by BugSleep*

There are two main functions for handling C2 communications: C2Loop (FUN\_1400012c0) and CommandHandler (FUN\_1400028a0). C2Loop is responsible for setting up socket connections with the server and sending a beacon, while CommandHandler is responsible for processing and executing commands from the server.

After setting up the socket connection, the implant beacons (FUN\_140003d80) to the C2 server for a command. The beacon is a StringMsg in the form ComputerName/Username. If the server responds with an IntegerMsg equal to 0x03, BugSleep will terminate itself. We suspect this is remnants of an old kill command or an emergency kill without the overhead of reading the real kill command later.

Each BugSleep command is sent as an IntegerMsg after the beacon response. The following enumeration defines all the command IDs discovered.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-a85a7b31-0f66-4555-aaad-68e725e7f73f.png)

Figure 2: Command IDs used by implant

# Phoning home

The implant communicates using plain TCP sockets, which can be seen using a Netcat listener and Wireshark.

![A screenshot of a computer  Description automatically generated](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-9bba947a-966d-4dbe-9539-3d173a7cfc7c.png)

Figure 3: BugSleep beacon as seen through Wireshark.

Recalling the message encryption demonstrated in Figure 1, the beacon can be decrypted with a little bit of Python (Figure 4). This will be used again when building the rest of the C2 server.

![A computer screen shot of a program code  Description automatically generated](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-24cee908-e7ee-46ac-b7dc-838e765bea60.png)

Figure 4: Decoding beacon data

# Python C2 server

With an understanding of the protocol basics, it is time to start building the C2 server. Full source code can be found [here](https://github.com/Cisco-Talos/IOCs/tree/main/2024/10/server).

## Beacon

As mentioned earlier, the BugSleep beacon function sends a StringMsg and reads an IntegerMsg response from the server. Since the IntegerMsg returned can be anything but 0x03, we returned the length of the Computer Name/Username string received by the server.

![A screenshot of a computer program  Description automatically generated](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-14de2c53-4ea3-4527-8f37-bae223cc48a8.png)

Figure 5: Output from C2 server receiving beacon data

## Ping command

The simplest command to implement is the Ping command. It has the command ID of 0x63 (BugSleep subtracts one from whatever ID it receives). The code is simple: send back 4 bytes.

![](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-dcc3ad4d-4771-4441-b65c-9fecf79a1cc6.png)

Figure 6: Switch case for handling ping command

Once the beacon comes in, the server is responsible for:

1. Sending 4 bytes for beacon response
2. Sending 4 bytes for Ping command ID
3. Reading 4 bytes of Ping data

The ping command was observed sending back 4 bytes recently allocated on the heap, so it's not guaranteed to know what that data looks like. To validate things are really working, a breakpoint can be set in WinDbg and memory set manually before being sent.

![A screenshot of a computer program  Description automatically generated](https://blog.talosintelligence.com/content/images/2024/10/data-src-image-8a6e6f35-d744-40c7-abd2-e8f1bd34679d.png)

Figure 7: Confirming 0xdeadbeef written to memory is received by the server in a...