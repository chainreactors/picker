---
title: Rtpengine: RTP Inject and RTP Bleed vulnerabilities despite proper configuration (CVSS v4.0 Score: 9.3 / Critical)
url: https://seclists.org/fulldisclosure/2025/Aug/1
source: Full Disclosure
date: 2025-08-04
fetch_date: 2025-10-07T00:47:43.997590
---

# Rtpengine: RTP Inject and RTP Bleed vulnerabilities despite proper configuration (CVSS v4.0 Score: 9.3 / Critical)

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

[![Previous](/images/left-icon-16x16.png)](0)
[By Date](date.html#1)
[![Next](/images/right-icon-16x16.png)](2)

[![Previous](/images/left-icon-16x16.png)](0)
[By Thread](index.html#1)
[![Next](/images/right-icon-16x16.png)](2)

![](/shared/images/nst-icons.svg#search)

# Rtpengine: RTP Inject and RTP Bleed vulnerabilities despite proper configuration (CVSS v4.0 Score: 9.3 / Critical)

---

*From*: Sandro Gauci via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 31 Jul 2025 07:02:38 +0200

---

```
Rtpengine: RTP Inject and RTP Bleed vulnerabilities despite proper configuration (CVSS v4.0 Score: 9.3 / Critical)

- CVSS v4.0
    - Exploitability: High
    - Complexity: Low
    - Vulnerable system: Medium
    - Subsequent system: Medium
    - Exploitation: High
    - Security requirements: High
    - Vector: https://www.first.org/cvss/calculator/4-0#CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H/SC:H/SI:H/SA:H
- Other references: CVE-2025-53399 (https://www.cve.org/CVERecord?id=CVE-2025-53399)
- Fixed versions: >= mr13.4.1.1 (https://github.com/sipwise/rtpengine/releases/tag/mr13.4.1.1)
- Enable Security Advisory:
https://github.com/EnableSecurity/advisories/tree/master/ES2025-01-rtpengine-improper-behavior-bleed-inject
- Tested vulnerable versions: mr13.3.1.4 and lower
- Timeline:
- First report: 2025-04-24
- Triaged: 2025-04-30
- Fix provided for testing: 2025-05-05
    - Various back and forth and more fixes: 2025-05 / 2025-06
    - Vendor applied all fixes satisfactorily to master branch: 2025-06-05
- Enable Security verified and confirmed fix: 2025-06-26
- Vendor release with fix (mr13.4.1.1): 2025-07-03
- Enable Security advisory: 2025-07-31

DESCRIPTION

Media servers often support source address learning to dynamically adapt to network conditions and client behavior.
This is especially useful in scenarios involving NAT where the source IP and port of incoming RTP packets may differ
from what was initially signaled via SDP over SIP. However, this mechanism can be exploited for two types of attacks if
malicious packets are accepted as legitimate:

1. RTP Bleed - when a victim's media (e.g., audio) can be redirected to an attacker-controlled host
2. RTP Inject – when attackers can insert arbitrary RTP packets into active calls

Note: Neither of these attacks requires the attacker to act as a man-in-the-middle.

Additionally, when rtpengine relays SRTP packets in vulnerable versions, it does not validate their authentication tag,
also allowing RTP Bleed and RTP Inject despite the use of SRTP which should guarantee confidentiality and integrity.
Instead of dropping packets with missing or invalid authentication tags, it forwards them for processing.

The purpose of this advisory is to describe security fixes that aim to fully address or at least mitigate these RTP
Bleed and RTP Inject attacks wherever possible. While complete elimination of these vulnerabilities may not always be
achievable due to the inherent nature of RTP learning mechanisms, the fixes provide significant improvements in
security posture.

TECHNICAL DETAILS

Rtpengine provides the following learning modes through the --endpoint-learning option:

- delayed (default): waits 3 seconds before learning the source address from the first RTP packet received after the
delay.

- immediate: learns the address from the very first incoming packet, with no delay.

- no-learning: disables learning entirely, which is the only mode that is not vulnerable but can break connectivity for
clients behind NAT.

- heuristic: combines a 3-second delay with a ranking system that prefers addresses matching the original SDP, falling
back to partial matches or any observed address if necessary.

Additionally, rtpengine supports an optional strict source flag that forces continued inspection of source addresses
and ports of incoming RTP packets. It does this after the learning phase, enforcing what was previously learned. The
strict source flag is meant to prevent RTP Inject but needs the learning mode to work as expected for it to also work
correctly.

The often recommended mitigation is to make use of SRTP, with the assumption that rtpengine would discard any RTP
packets that fail the authentication tag check. However, in rtpengine mr13.3.1.4 and lower, this was not found to be
the case when using SDES-SRTP.

The following is a behavior matrix for rtpengine versions mr13.3.1.4 and lower showing different learning modes and
flags. This table shows that none of the learning modes nor strict source mitigated the attacks described, except for
the combination of strict source with no-learning:

                    | Delayed       | Heuristic     | No learning         | Immediate     |
no strict source    | Inject, Bleed | Inject, Bleed | Inject only         | Inject, Bleed |
strict source       | Inject, Bleed | Inject, Bleed | No Inject or Bleed  | Inject, Bleed |

The same behavior occurred whether rtpengine relayed plaintext RTP or SDES-SRTP. The heuristic flag did not prevent RTP
Bleed or RTP Inject attacks, even when the correct IPs and ports are exchanged over SDP.

With the updated version, rtpengine's heuristic behavior was changed so that the learning modes behave as expected,
giving administrators the opportunity to mitigate these vulnerabilities while still handling NAT complexities.

The following is the same behavior matrix, but with the fixed version:

                    | Delayed       | Heuristic                | No learning   | Immediate     |
no strict source    | Inject, Bleed | Inject, <5 packets Bleed | Inject only   | Inject, Bleed |
strict source       | Inject, Bleed | <5 packets Inject, <5 packets Bleed | No Inject or Bleed | Inject, Bleed |

This means that with the updated version, the heuristic mode limits attacks to at most the first 5 packets for both
injection and bleeding.
We believe that in many live environments, the recommended setup would be to use heuristic learning with strict source,
which keeps the flexibility of endpoint learning while significantly mitigating RTP inject and RTP bleed attacks.

In the case of SDES-SRTP, we also recommend using heuristic learning mode with strict source, which keeps the
flexibility of endpoint learning while mitigating RTP inject and RTP bleed. However, for complete protection with SRTP,
a patch specific to SRTP was introduced by adding a new recrypt flag. This flag forces rtpengine to decrypt and then
re-encrypt RTP packets, thus validating the authentication tag before any further processing. This ensures that
unauthenticated packets are discarded. This new flag should be used in addition to the previously recommended learning
mode and flag.

Patched version behavior matrix for SDES-SRTP, with and without recrypt:

                    | Delayed            | Heuristic          | No-learning        | Immediate          |
Without recrypt     | Inject, Bleed      | Inject, <5 packets Bleed | Inject only   | Inject, Bleed      |
With recrypt        | No Inject or Bleed | No Inject or Bleed | No Inject or Bleed | No Inject or Bleed |

There is the special case of DTLS-SRTP, typically used for WebRTC environments, which was found vulnerable to RTP Bleed
but not RTP Inject. This was due to the logic applied in this case, where learning mode occurred before the RTP packets
were properly validated. This has also received a security fix.

IMPACT

In the case of plaintext RTP, this vulnerability allows attackers to perform RTP Inject as well as RTP B...