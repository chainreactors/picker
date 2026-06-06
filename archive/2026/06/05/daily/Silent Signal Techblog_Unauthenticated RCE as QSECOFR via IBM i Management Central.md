---
title: Unauthenticated RCE as QSECOFR via IBM i Management Central
url: https://blog.silentsignal.eu/2026/06/05/unauthenticated-rce-as-qsecofr-via-ibm-i-management-central/
source: Silent Signal Techblog
date: 2026-06-05
fetch_date: 2026-06-06T05:51:30.442292
---

# Unauthenticated RCE as QSECOFR via IBM i Management Central

[![Silent Signal](/assets/img/s2_avatar.jpg)](/)

Silent Signal

Professional Ethical Hacking Services

### Contact us

2026 © Silent Signal

![Unauthenticated RCE as QSECOFR via IBM i Management Central](/img/reddington.webp)

# Unauthenticated RCE as QSECOFR via IBM i Management Central

[pz](/authors/pz.html) 2026-06-05

# Intro

We discovered and developed an exploit for a pre-authentication remote code execution vulnerability in IBM i Management Central (MGTC). The vulnerability allows an unauthenticated attacker to execute arbitrary CL commands as QSECOFR – the root-equivalent profile on IBM i – by abusing the MGTC packet protocol on port 5555.

## What is Management Central?

Management Central is a Java-based system management framework that has been part of IBM i since the early 2000s. It provides centralized task scheduling, system monitoring, software distribution, and remote command execution across groups of IBM i systems. If that sounds like a powerful service to expose on the network, it is.

The service runs as two listeners. Port 5544 is an RMI-based interface that uses `McRMISocketFactory` – a custom `RMISocketFactory` – to wrap every incoming connection in a serialized `McSocketBundle` exchange before any RMI method calls occur. There was a deserialization vulnerability in Management Central that we discovered and reported to IBM PSIRT.
([CVE-2024-31879](https://www.ibm.com/support/pages/node/7154380)).

Port 5555 runs `McSocketListener`, which extends `java.net.ServerSocket` directly, skipping RMI and Java serialization. It accepts raw TCP connections, performs a custom binary handshake, and then creates a `McPacketConnection` that processes packets using `McBuffer`, a custom binary serialization format. This is the port and protocol we exploit in this post.

Both ports are started by the MGTC server job (`QYPSJSVR`) when the service is active. The CL command is `STRTCPSVR SERVER(*MGTC)`.

IBM has been deprecating Management Central. Starting with V7R5, the service is no longer part of the operating system. On V7R4 and earlier, it is a standard component and often starts automatically. Given IBM i’s long upgrade cycles, there are plenty of V7R4 systems in production.

## Finding the Pieces

The MGTC implementation ships as a set of JAR files. The client-side classes are included in IBM i Access Client Solutions (ACS): `McClient.jar`, `McPacketClient.jar`, `McServer.jar`, and `McOSClient.jar`. On the server side, the same JARs live under `/QIBM/ProdData/OS400/Mgtc/` – over 40 JARs in total, plus `jt400.jar` from `/QIBM/ProdData/OS400/jt400/lib/`.

Decompiling these JARs gives us the complete picture. The MGTC protocol has no public documentation – everything described in this post was reconstructed from the bytecode using `javap -p -c` on the class files.

The key classes are:

| Class | Role |
| --- | --- |
| `McSocketListener` | Server socket for port 5555 (extends `ServerSocket`) |
| `McSocketConnection` | Handles the binary handshake, sends/receives packets |
| `McPacketConnection` | Wraps `McSocketConnection`, manages the packet lifecycle |
| `McBuffer` | Custom binary serializer (not `ObjectInputStream`) |
| `McPacket` | Base class for all packets; carries routing + auth data |
| `McClassManager` | Maps integer classIds to Java class names |
| `McPacketableAuthenticationData` | Per-packet auth structure (the vulnerable component) |
| `McPacketManager` | Routes packets, calls `authenticate()` and `execute()` |

## The Class ID System

MGTC uses integer class identifiers to map packet types to Java classes. `McClassManager` maintains a static array of 3000 entries initialized at startup. The important ones for this exploit:

```
classId  3 → McCreateRequest         (registers a managed object)
classId 16 → McStartRequest          (starts/executes an activity)
classId 21 → McTaskRequest           (task lifecycle operations)
classId 82 → McStatusReply           (success response)
classId 87 → McManagedObjectReply    (returns created object with assigned ID)
classId 99 → McSlashedAndBurnedReply (error response)
classId 251 → McEndpointManagedCmdData    (command task data)
classId 252 → McManagedCmdDefinition      (command definition with CL string)
```

When the server receives a packet, it reads the classId from the wire, looks up the corresponding class name in the array, instantiates it via reflection, and calls `inflate()` to deserialize the packet from a `McBuffer`.

## The McBuffer Format

`McBuffer` is the serialization engine for all MGTC packet data. Instead of using the built-in Java `ObjectInputStream`, it uses a custom binary format with explicit type encoding. The primitives:

| Method | Wire format |
| --- | --- |
| `deflate(int)` | 4 bytes big-endian |
| `deflate(long)` | 8 bytes big-endian |
| `deflate(float)` | 4 bytes IEEE 754 |
| `deflate(byte)` | 1 byte |
| `deflate(byte[])` | raw bytes, no length prefix |
| `deflate(String)` | 2-byte length (short) + UTF-16BE data |
| `deflate(String, (short)4)` | 4-byte length (int) + UTF-16BE data |

When the server creates a `McBuffer` for outgoing data, it calls `allocate()` which writes a 4-byte version float (e.g., `7.2f` = `0x40e66666`) as the first bytes. Incoming data is expected to start with this version header.

## The Binary Handshake

The handshake on port 5555 is the first barrier. `McSocketConnection.sendHandshake()` and `receiveHandshake()` implement a multi-step exchange. The connector (client) sends a 1144-byte structure for IPv4:

**Buffer (1120 bytes):**

```
Offset 0-511:     hostname (UTF-16BE, zero-padded)
Offset 512-1023:  hostname (repeated)
Offset 1024-1055: IP address (UTF-16BE, 32 bytes)
Offset 1056-1087: OS name (UTF-16BE, 32 bytes)
Offset 1088-1119: OS version (UTF-16BE, 32 bytes)
```

**Metadata (24 bytes):**

```
[hostLen:2][hostLen:2][addrLen:2][osLen:2][verLen:2][ipv4Flag:2][mcVersion:4][connectKey:4][acceptKey:4]
```

The server responds with the same structure. But the handshake does not end here. The server’s `sendHandshake()` method blocks on a `readFully(4)` call, waiting for the connector to send back 4 bytes: `manipulateKey(server_localKey)`. If you don’t send them, the server hangs and nothing else happens. This cost us a fair amount of debugging time.

The key derivation uses constants 12345 and 54321:

```
long manipulateKey(long key) {
    long t = (key & 0xFFFFL) << 8;
    long r = key | ((t * 12345L) & 0xFFFFFFFFL);
    t = (r & 0xFFFF0000L) >> 8;
    return (r ^ ((t * 54321L) & 0xFFFFFFFFL)) & 0xFFFFFFFFL;
}
```

After key verification, if the Management Central version is >= 5.1, a 4-byte negotiation follows (each side sends a random key). For version >= 5.21, a configuration exchange (5 ints out, variable-length response) completes the setup.

The OS name field matters. The server’s `receiveHandshake()` checks it: if `authLevel == 1` and the remote OS starts with `"WIN32"`, the connection key is manipulated normally. Otherwise, depending on the server’s `authLevel` vs `MIN_AUTH_LEVEL`, the connection may be rejected. We use `"WIN32"` in the handshake for this reason.

## The Packet Wire Format

After the handshake, `McSocketConnection.sendPacket()` and `receivePacket()` handle the packet exchange. Each packet on the wire has a simple framing:

```
[classId: 4 bytes][dataLength: 4 bytes][data: dataLength bytes]
```

The `classId` identifies the packet type (see the class ID table above). The `data` is `McBuffer`-encoded and starts with a 4-byte version float, followed by the fields defined by each packet class’s `deflate()` method.

Every packet inherits from `McPacket`, which defines a common header deflated by `McPacket.deflate()`:

```
[version: 4 float]          ← McBuffer version header
[classId: 4 int]            ← packet's own classId
[destination: 2+N string]   ← short-prefixed UTF-16BE string (usually empty)
[routingInfo]               ← McPacketableRoutingInfo (see below)
[authData]                  ← McPacketableAu...