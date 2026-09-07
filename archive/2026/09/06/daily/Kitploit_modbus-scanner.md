---
title: modbus-scanner
url: https://kitploit.com/en/tools/github/k3ystr0k3r/modbus-scanner
source: Kitploit
date: 2026-09-06
fetch_date: 2026-09-07T06:48:58.692396
---

# modbus-scanner

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

modbus-scanner — Multithreaded Modbus/TCP detection scanner written in C using libmodbus. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/k3ystr0k3r/modbus-scanner

![](https://assets.kitploit.com/production/public/tools/54128/354ca73e24db1dd292c8a5fe8c42a3c380c175c97502bd08b0731d4a5ecb81a8-display-v1.webp)

[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Network Mapping](/en/categories/network-mapping)[Port Scanning](/en/categories/port-scanning)[SCADA/ICS Security](/en/categories/scada-ics-security)[Information Gathering](/en/categories/information-gathering)[Network Security](/en/categories/network-security)

![GitHub](/providers/github.png)k3ystr0k3r/modbus-scanner

# modbus-scanner

Multithreaded Modbus/TCP detection scanner written in C using libmodbus.

[View Repository](https://github.com/k3ystr0k3r/modbus-scanner)

433 days ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Modbus Detection Scanner

A multithreaded C scanner for detecting Modbus/TCP services using `libmodbus`.

The scanner does not rely only on TCP port `502` being open. Instead, it establishes a Modbus/TCP connection and sends an application layer Modbus request. A valid Modbus response is used as the primary indicator that a Modbus service is present.

---

## Modbus/TCP

Modbus is an industrial communication protocol commonly used by PLCs, RTUs, HMIs, SCADA systems, sensors, meters, and other industrial devices.

Modbus/TCP transports the Modbus application protocol over TCP.

The standard Modbus/TCP port is:

root@kitploit:~

```
TCP/502
```

A typical communication flow is:

root@kitploit:~

```
Scanner
   |
   | TCP connection → 502
   |
   | Modbus/TCP request
   v
Modbus Device
   |
   | Modbus/TCP response
   v
Scanner
```

Unlike protocols that provide a banner immediately after connecting, Modbus/TCP generally requires the client to send a valid Modbus request before the device produces an application layer response.

---

# Detection Method

The scanner performs detection in two stages.

### 1. TCP connection

The scanner attempts to establish a TCP connection to:

root@kitploit:~

```
<target>:502
```

If the connection cannot be established, the target is treated as not responding to Modbus/TCP.

However, an open TCP/502 port by itself is **not considered sufficient evidence** of Modbus.

### 2. Modbus application-layer probe

After connecting, the scanner sends a Modbus request using `libmodbus`.

The primary probe is:

root@kitploit:~

```
modbus_read_input_registers(ctx, 0, 1, &reg);
```

This generates a Modbus Function Code:

root@kitploit:~

```
0x04 - Read Input Registers
```

The request asks the target for one input register starting at address `0`.

If the target returns a valid Modbus response, the scanner considers the service detected.

---

# Modbus/TCP Packet Structure

A Modbus/TCP packet consists of:

root@kitploit:~

```
+----------------------+----------------------+
| MBAP Header          | PDU                  |
+----------------------+----------------------+

MBAP Header:
+------------------+
| Transaction ID   | 2 bytes
| Protocol ID      | 2 bytes
| Length           | 2 bytes
| Unit Identifier  | 1 byte
+------------------+

PDU:
+------------------+
| Function Code    | 1 byte
| Data             | N bytes
+------------------+
```

The MBAP header is specific to Modbus/TCP.

---

# Primary Detection Packet

The scanner's first probe uses Function Code `0x04`.

A representative request is:

root@kitploit:~

```
00 01 00 00 00 06 01 04 00 00 00 01
```

Breaking this down:

root@kitploit:~

```
00 01        Transaction Identifier
00 00        Protocol Identifier
00 06        Length
01           Unit Identifier
04           Function Code
00 00        Starting Address
00 01        Quantity
```

### Transaction Identifier

root@kitploit:~

```
00 01
```

Identifies the transaction.

The value can vary because the transaction identifier is normally managed by the Modbus client library.

### Protocol Identifier

root@kitploit:~

```
00 00
```

A value of `0` identifies Modbus.

### Length

root@kitploit:~

```
00 06
```

Specifies the number of bytes following the length field.

### Unit Identifier

root@kitploit:~

```
01
```

Identifies the target Modbus unit.

### Function Code

root@kitploit:~

```
04
```

Function Code `0x04` means:

root@kitploit:~

```
Read Input Registers
```

### Starting Address

root@kitploit:~

```
00 00
```

The scanner starts at register address `0`.

### Quantity

root@kitploit:~

```
00 01
```

The scanner requests one register.

---

# Expected Response

A successful response to the request contains Function Code `0x04` and the requested register data.

A representative response could look like:

root@kitploit:~

```
00 01 00 00 00 05 01 04 02 00 00
```

Breaking it down:

root@kitploit:~

```
00 01        Transaction Identifier
00 00        Protocol Identifier
00 05        Length
01           Unit Identifier
04           Function Code
02           Byte Count
00 00        Register Value
```

The important part for detection is that the target successfully processes the Modbus request and returns a valid Modbus application-layer response.

The actual register value is device-dependent.

---

# Why Port 502 Alone Is Not Enough

Simply checking:

root@kitploit:~

```
TCP/502 = OPEN
```

does not necessarily prove that the service is Modbus.

Port numbers are conventions. A different application can listen on TCP/502, and a Modbus device may also behave differently depending on its configuration.

The scanner therefore uses:

root@kitploit:~

```
TCP connectivity
        +
Modbus protocol response
        =
Modbus detection
```

This makes application-layer detection more meaningful than a simple port scan.

---

# Fallback Detection

Some devices may not respond to the initial `0x04` request because of their register configuration or supported function codes.

The scanner therefore attempts a second request if the first one fails:

root@kitploit:~

```
modbus_read_bits(ctx, 0, 1, bits);
```

This uses Function Code:

root@kitploit:~

```
0x01 - Read Coils
```

A representative request is:

root@kitploit:~

```
00 02 00 00 00 06 01 01 00 00 00 01
```

Breakdown:

root@kitploit:~

```
00 02        Transaction Identifier
00 00        Protocol Identifier
00 06        Length
01           Unit Identifier
01           Function Code
00 00        Starting Address
00 01        Quantity
```

The scanner considers the target detected when either Modbus operation receives a successful response.

---

# Detection Flow

root@kitploit:~

```
             Target IP
                 |
                 v
          TCP connection
             port 502
                 |
          +------+------+
          |             |
        Failed       Connected
          |             |
          v             v
       Ignore      Function 0x04
                        |
                 +------+------+
                 |             |
               Valid   ...