---
title: When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Five
url: https://ddanchev.blogspot.com/2026/03/when-data-mining-conti-leaks-leads-to_25.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2026-03-25
fetch_date: 2026-03-26T04:30:25.167001
---

# When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Five

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

In the overwhelming sea of information, access to timely, insightful and independent open-source intelligence (OSINT) analyses is crucial for maintaining the necessary situational awareness to stay on the top of emerging security threats. This blog covers trends and fads, tactics and strategies, intersecting with third-party research, speculations and real-time CYBERINT assessments, all packed with sarcastic attitude

## Wednesday, March 25, 2026

### When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Five

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwgwHwgO3D7ysXflqzrlhyHnZE6QwYO7Br_OEo6hBhIXXhafu-jcXaFSJUqnNXHnv11LCoBq1wUhBxjBJX-2rogHnasT7f14SuxxLxoOK0jmJf_VKecHKBVgf3PG3eIeiFdFdM3fb5iVhniSKXlAT0ScXCaO5bsln4H5znTfQH2_FhmTwkZw4u/s320/Misc_1700.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwgwHwgO3D7ysXflqzrlhyHnZE6QwYO7Br_OEo6hBhIXXhafu-jcXaFSJUqnNXHnv11LCoBq1wUhBxjBJX-2rogHnasT7f14SuxxLxoOK0jmJf_VKecHKBVgf3PG3eIeiFdFdM3fb5iVhniSKXlAT0ScXCaO5bsln4H5znTfQH2_FhmTwkZw4u/s788/Misc_1700.png)

Dear blog readers,

Continuing the "[When Data Mining Conti Leaks Leads to Actual Binaries and to a Hardcoded C2 With an Encryption Key on Tripod.com - Part Four](https://ddanchev.blogspot.com/2026/03/when-data-mining-conti-leaks-leads-to_23.html)" blog post series in this post I'll continue analyzing the next [malicious software](https://ddanchev.blogspot.com/2022/06/a-compilation-of-known-conti-ransomware_21.html) binary which I obtained by [data mining](https://ddanchev.blogspot.com/search?q=conti) [Conti Leaks](https://archive.org/details/rewards-for-justice-01) with a lot of success.

**The actual [malicious software](https://www.virustotal.com/gui/file/c366c4e26ec3d2698a94dc04afb58dad429d6c28dff1820d53e277e108103f8f) binary location URL:**

hxxp://www.delwarren.com/backup/nowin.exe

MD5: 320dd151aed6a181d84e63f78cf801f0
SHA-1: 573e93bb5075ec74ec3c45eaf4190af8e315a429
SHA-256: c366c4e26ec3d2698a94dc04afb58dad429d6c28dff1820d53e277e108103f8f

Here's the analysis.

High-confidence classification

nowin.exe is a Windows x86 network backdoor whose primary behaviors are:

* persistent/repairable multi-threaded C2 beacons (keeps up to 3 concurrent worker threads),
* a custom C2 application protocol (length-framed + lightweight obfuscation using a constant marker),
* remote command execution (via system() with captured output),
* interactive command shell (cmd.exe) over the network,
* a secondary, more complex relay-based shell channel negotiated using a SOCKS-like control exchange.

The overall design is typical of a small bespoke RAT/backdoor: connect to a hardcoded controller, identify/beacon, then loop receiving commands which dispatch into a few core capabilities.

---

## Runtime / threading model

### Process start and initialization

* entry\_point (0x40383c) and runtime\_init (0x40357c) implement standard CRT initialization and single-init locking.
* Initialization uses:
  + InterlockedCompareExchange guarding a global init lock (g\_init\_lock at 0x407504),
  + g\_init\_state (0x407500) to track initialization progress.

### Worker thread redundancy (up to 3 concurrent)

* backdoor\_worker\_thread (0x4019a0) is the main C2 loop.
* It increments/decrements g\_active\_thread\_count (0x4074c0) under g\_thread\_count\_lock (0x40749c).
* On certain failures or after certain commands, it respawns itself via \_beginthread(backdoor\_worker\_thread, 0, 0) until g\_active\_thread\_count < 3 no longer holds.

This provides resilience: if a connection drops or a thread exits, the malware will try to maintain a small pool of active connections.

---

## C2 infrastructure and basic socket operations

### Hardcoded controller address

* C2 IP: 88.214.27.52, constructed at 0x401adc (sprintf("%d.%d.%d.%d", 0x58, 0xd6, 0x1b, 0x34)).
* Port: 443 (htons(0x1bb)), set in connect\_to\_c2 (0x402aa0).

### Connection procedure (connect\_to\_c2, 0x402aa0)

* Creates TCP socket (via WSASocketA(AF\_INET, SOCK\_STREAM, IPPROTO\_TCP)).
* Uses a non-blocking connect pattern:
  + ioctlsocket(FIONBIO, 1) → nonblocking,
  + connect,
  + select(... writefds ..., timeout=10s) to detect connection completion,
  + ioctlsocket(FIONBIO, 0) restore blocking.
* Returns boolean-style success.

This is a common technique for implementing a connect timeout on Windows.

---

## Primary C2 protocol (framing + “AssHole” obfuscation layer)

The malware’s main message channel uses:

1. 4-byte length prefix
2. encoded payload (obfuscated, not encrypted)

### Framing

* Receive path: recv\_command\_from\_c2 (0x4027a0)
  + Reads exactly 4 bytes (the length) via repeated recv.
  + Allocates/resizes a std::string to that length.
  + Reads exactly len bytes via recv\_exact (0x402a60).
* Send path: send\_data\_to\_c2 (0x4028d0)
  + Builds a string, then sends 4-byte length followed by payload (body send uses send\_exact at 0x402a20 for full transmission).

### “AssHole” wrapper purpose and mechanics

* Literal marker: "AssHole" at 0x405558.
* Alphabet used by transform: "0123456789abcdef" at 0x405544.

Both send\_data\_to\_c2 and recv\_command\_from\_c2 incorporate "AssHole" directly into the transform pipeline:

* On send: the outgoing buffer is combined with "AssHole" and passed through encode\_obfuscated\_hex\_string (0x4024a0).
* On receive: the received blob is combined with "AssHole" and passed through decode\_obfuscated\_hex\_string (0x402620).

What this achieves

* It is a lightweight obfuscation/encoding layer that:
  + makes on-the-wire command tokens/results non-plaintext,
  + provides a trivial shared constant that must match between sides (a weak “key”/salt),
  + reduces accidental decoding of arbitrary traffic into meaningful commands.
* This is not cryptography; it behaves like reversible per-character nibble transformations over hex-like text.

---

## Command protocol: exact tokens and behaviors

After initial beaconing, backdoor\_worker\_thread continually:

* recv\_command\_from\_c2 → decodes into a command string
* compares equality against several hardcoded tokens
* dispatches behavior per match

### Exact command tokens (as used in comparisons)

The decoded command string is compared against these literal tokens:

| Role (renamed) | Token string | Address |
| --- | --- | --- |
| kCmd\_ShellIO | Csdnma91fggw7 | 0x405234 (0x407100) |
| kResp\_ShellIO\_Ack | Zcvznw8i739 | 0x405228 (0x407104) |
| kCmd\_StartWorkersAndShell | Fdh9873 | 0x405220 (0x407108) |
| kCmd\_DropPayload | VCNde92756 | 0x405214 (0x40710c) |
| kCmd\_ExecAndReturn | NMFVd8w7663 | 0x405208 (0x407110) |
| kCmd\_SpawnCmdExe | COMM500 | 0x405200 (0x407114) |
| kCmd\_SelfMoveTrash | JWEdj898 | 0x4051f4 (0x407118) |

Also present in the initial beacon string:

* NUDEew97834g at 0x405244 (0x4070fc) (used as part of the initial identification string, not a compare token in the dispatch shown).

### Command behaviors (as implemented)

* Shell/relay initiation
  + Matching kCmd\_StartWorkersAndShell ("Fdh9873") triggers:
    - spawning additional workers (up to 3 total),
    - entering handle\_shell\_io(s) (0x403360) which negotiates and runs the relay-based shell path.
  + Matching kCmd\_ShellIO ("Csdnma91fggw7") results in sending kResp\_ShellIO\_Ack ("Zcvznw8i739") back.
* Remote exec with output capture
  + Matching kCmd\_ExecAndReturn ("NMFVd8w7663") triggers execute\_system\_and\_capture\_output (0x401720):
    - constructs a temporary file path,
    - runs system() redirecting output to file,
    - reads file contents into a std::string,
    - deletes the file,
    - sends the output back (with token appended/used as delimiter/prefixing behavior).
* Direct interactive cmd.exe
  + Matching kCmd\_SpawnCmdExe ("COMM500") triggers spawn\_reverse\_shell(&s) (0x402ba0).
* Drop/write payload to disk
  + Matching kCmd\_Dro...