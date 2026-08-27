---
title: Escargot v4.3.0-214-gfaee4437 Debugger WebSocket Off-by-One Stack Buffer Overflow
url: https://seclists.org/fulldisclosure/2026/Aug/107
source: Full Disclosure
date: 2026-08-26
fetch_date: 2026-08-27T12:14:25.487085
---

# Escargot v4.3.0-214-gfaee4437 Debugger WebSocket Off-by-One Stack Buffer Overflow

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](106)
[By Date](date.html#107)
[![Next](/images/right-icon-16x16.png)](108)

[![Previous](/images/left-icon-16x16.png)](106)
[By Thread](index.html#107)
[![Next](/images/right-icon-16x16.png)](108)

![](/shared/images/nst-icons.svg#search)

# Escargot v4.3.0-214-gfaee4437 Debugger WebSocket Off-by-One Stack Buffer Overflow

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 22 Aug 2026 08:44:45 -0400

---

```
Escargot contains a remotely triggerable one-byte stack-based out-of-bounds
write in the WebSocket message handling logic used by the debugger.

When Escargot::DebuggerTcp::receive() receives a binary WebSocket payload
that completely fills the caller-provided stack buffer, the function
successfully copies the payload into the available buffer space but
subsequently appends an additional NUL byte without verifying that space
remains for the terminator.

A 125-byte binary WebSocket payload causes the debugger to write the
terminating NUL byte to buffer[125], immediately beyond the end of the
125-byte stack allocation.

A proof-of-concept client establishes a valid WebSocket connection to the
Escargot debugger endpoint and sends the boundary-sized binary frame.
AddressSanitizer consistently detects the resulting stack-buffer overflow
inside Escargot::DebuggerTcp::receive().

The vulnerability results in stack memory corruption and can remotely
terminate an Escargot process exposing the debugger interface. The current
proof of concept demonstrates reliable denial of service and memory
corruption but does not establish arbitrary code execution.
Vulnerable Code

The debugger decodes the incoming masked WebSocket payload directly into a
caller-provided buffer:

const uint8_t* source = mask_end;
uint8_t* buffer_end = buffer + m_payloadLength;

while (buffer < buffer_end) {
    *buffer++ = *source++ ^ *mask++;

    if (mask >= mask_end) {
        mask -= 4;
    }
}

*buffer_end = 0;

The payload copy itself does not exceed the destination when the payload
length exactly equals the destination capacity.

The vulnerability occurs immediately afterward:

*buffer_end = 0;

Because buffer_end is calculated as:

buffer + m_payloadLength

a payload that completely fills the destination causes buffer_end to point
exactly one byte beyond the allocated object.

The implementation does not receive or validate the destination buffer
capacity before performing this additional write.
Root Cause

The vulnerability is an off-by-one error caused by treating a fixed-size
binary buffer as though it always contains sufficient additional capacity
for a NUL terminator.

The affected caller uses a 125-byte stack buffer. With a 125-byte payload,
the copy operation occupies the complete valid range:

buffer[0] ... buffer[124]

After the copy completes:

buffer_end == &buffer[125];

The subsequent operation:

*buffer_end = 0;

is therefore equivalent to:

buffer[125] = '\0';

For a 125-byte allocation, index 125 is outside the object. Valid indexes
are only 0 through 124.

This results in a one-byte stack-based out-of-bounds write.
Proof of Concept

The PoC was executed against an AddressSanitizer-instrumented Escargot
build:

[*] Target binary :
    /work/escargot/security-poc/build-debugger-asan/escargot
[*] Debugger URL :
    ws://127.0.0.1:6611/escargot-debugger
[*] Payload :
    125-byte binary frame
[*] Bug trigger :
    DebuggerTcp::receive() writes NUL at buffer[payloadLength]

The client first performs a legitimate WebSocket handshake.

The Escargot debugger accepts the connection:

[+] WebSocket handshake accepted

HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: voBbwZEm0j70WZ2O4Hx37ERFeqA=

This confirms that the PoC reaches the debugger through the expected
WebSocket protocol rather than invoking the vulnerable function directly.

The client then sends the boundary-sized binary frame:

[*] Sending binary frame:
    opcode=0x2
    payload_len=125

The test reports successful reproduction:

[+] Confirmed: True[*] Process return code: -6

The -6 return code corresponds to process termination through SIGABRT. In
this test configuration, the important evidence is not the return code
itself but the accompanying AddressSanitizer report identifying the invalid
stack write.
AddressSanitizer Evidence

AddressSanitizer reports a stack-buffer overflow directly within the
vulnerable receive function:

[evidence] SUMMARY: AddressSanitizer: stack-buffer-overflow
(/work/escargot/security-poc/build-debugger-asan/escargot+0x4fe03c)
(BuildId: 1545896c0ed347436f48a03cdab84e73c634fadd)
in Escargot::DebuggerTcp::receive(unsigned char*, unsigned long&)

The top of the stack trace identifies DebuggerTcp::receive() as the
location of the invalid memory access:

[evidence] #0 0xaaaadfd0e03c
in Escargot::DebuggerTcp::receive(unsigned char*, unsigned long&)
(/work/escargot/security-poc/build-debugger-asan/escargot+0x4fe03c)
[evidence] #1 0xaaaadfcfeb98
in Escargot::DebuggerEscargot::processEvents(
    Escargot::ExecutionState*,
    Escargot::Optional<Escargot::ByteCodeBlock*>,
    bool
)
/work/escargot/src/debugger/DebuggerEscargot.cpp:767

Most importantly, AddressSanitizer identifies the precise stack object that
is exceeded:

[evidence] [800, 925) 'buffer' (line 762)
           <== Memory access at offset 925 overflows this variable

The buffer object occupies stack offsets:

[800, 925)

This represents exactly:

925 - 800 = 125 bytes

The first byte outside the allocation is offset 925.

AddressSanitizer reports the invalid access at exactly that offset:

Memory access at offset 925 overflows this variable

The runtime evidence therefore precisely matches the source-level defect.

For a 125-byte buffer:

Stack object:       [800, 925)
Buffer size:        125 bytes
Valid offsets:      800 through 924
Invalid write:      925
Overflow distance:  1 byte

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](106)
[By Date](date.html#107)
[![Next](/images/right-icon-16x16.png)](108)

[![Previous](/images/left-icon-16x16.png)](106)
[By Thread](index.html#107)
[![Next](/images/right-icon-16x16.png)](108)

### Current thread:

* **Escargot v4.3.0-214-gfaee4437 Debugger WebSocket Off-by-One Stack Buffer Overflow** *Ron E (Aug 26)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.o...