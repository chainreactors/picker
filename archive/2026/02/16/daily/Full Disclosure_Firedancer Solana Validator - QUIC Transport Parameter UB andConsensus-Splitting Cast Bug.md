---
title: Firedancer Solana Validator - QUIC Transport Parameter UB and	Consensus-Splitting Cast Bug
url: https://seclists.org/fulldisclosure/2026/Feb/14
source: Full Disclosure
date: 2026-02-16
fetch_date: 2026-02-17T04:21:57.157272
---

# Firedancer Solana Validator - QUIC Transport Parameter UB and	Consensus-Splitting Cast Bug

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

![](/shared/images/nst-icons.svg#search)

# Firedancer Solana Validator - QUIC Transport Parameter UB and Consensus-Splitting Cast Bug

---

*From*: Agent Spooky's Fun Parade via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 10 Feb 2026 16:08:58 +0000

---

```
1. SUMMARY

Two independently confirmed vulnerabilities in Jump Crypto's Firedancer
Solana validator (https://github.com/firedancer-io/firedancer, commit
7cd3b6dce):

  A) Three undefined behavior / logic bugs in QUIC transport parameter
     processing, triggerable by a malicious QUIC server with zero
     authentication. Enables remote connection kill or hang.

  B) Incorrect Rust saturating cast emulation that returns ULONG_MAX
     instead of 0 for negative infinity, diverging from Agave's behavior
     in rent and stake calculations. Potential consensus split.

Both bugs were confirmed with UBSAN stack traces against the real
compiled Firedancer source code and, for (B), cross-verified against
rustc output.

2. BUG A: QUIC TRANSPORT PARAMETER UNDEFINED BEHAVIOR

Affected file: src/waltz/quic/fd_quic.c
Function: fd_quic_apply_peer_params (line 2667)
Entry point: fd_quic_tls_cb_peer_params (line 2738), called during
  TLS handshake -- no authentication required.

Three bugs, all triggered from a single malicious TLS handshake:

--- A1: Signed integer overflow (line 2713) ---

  long peer_max_idle_timeout_ns = (long)peer_tp->max_idle_timeout_ms * (long)1e6;

max_idle_timeout_ms is a ulong decoded from a QUIC VARINT (max 2^62-1).
Cast to signed long, then multiplied by 1e6. For values above
LONG_MAX/1e6 (~9.22e12), this is signed integer overflow -- undefined
behavior per C11 6.5/5.

UBSAN output:

  src/waltz/quic/fd_quic.c:2713:72: runtime error: signed integer
  overflow: 9223372036855 * 1000000 cannot be represented in type 'long'
      #0 in fd_quic_apply_peer_params fd_quic.c:2713

In practice, the result wraps negative. fd_long_min then selects this
negative value as the idle timeout, causing immediate connection death.

--- A2: Shift exponent too large (line 2724) ---

  conn->peer_ack_delay_scale = (float)( 1UL << peer_ack_delay_exponent ) * 1e3f;

RFC 9000 Section 18.2: "Values above 20 are invalid." No validation is
performed. For exponent >= 64, this is undefined behavior (shift amount
```

> ```
> = width of unsigned long). For 20 < exponent < 64, the scale becomes
> ```

```
absurdly large (e.g., 4.6e+21 for exponent=62), corrupting all RTT
estimation and loss detection.

UBSAN output:

  src/waltz/quic/fd_quic.c:2724:45: runtime error: shift exponent 64
  is too large for 64-bit type 'unsigned long'
      #0 in fd_quic_apply_peer_params fd_quic.c:2724

--- A3: Unsigned overflow in max_ack_delay (line 2730) ---

  peer_tp->max_ack_delay * 1000UL

RFC 9000 Section 18.2: "Values of 2^14 or greater are invalid." No
validation is performed. For large VARINT values, the multiplication
wraps. The result, cast to float, produces a value on the order of 1e22
nanoseconds. This propagates to PTO calculation (fd_quic_private.h:429),
making the probe timeout effectively infinite. The client never
retransmits.

--- Combined impact ---

A malicious QUIC server sends these transport parameters in one TLS
handshake:

  max_idle_timeout    = 9223372036855 ms
  ack_delay_exponent  = 64
  max_ack_delay       = 2^62 - 1 ms

Result: the Firedancer QUIC client's connection is immediately killed
(A1), its RTT estimation is destroyed (A2), and it will never
retransmit (A3). This is a zero-interaction remote DoS requiring no
authentication.

--- Fix ---

Validate per RFC 9000 Section 18.2 before use:
  - Reject ack_delay_exponent > 20 as TRANSPORT_PARAMETER_ERROR
  - Reject max_ack_delay >= 2^14 as TRANSPORT_PARAMETER_ERROR
  - Use unsigned arithmetic or clamp max_idle_timeout_ms before
    multiplying by 1e6

3. BUG B: fd_rust_cast_double_to_ulong RETURNS ULONG_MAX FOR -INFINITY

Affected file: src/flamenco/types/fd_cast.h
Function: fd_rust_cast_double_to_ulong (line 21)

The function's own documentation (line 17-18) states:
  "Saturate to 0 if the value is negative or NaN."

The implementation checks for infinity (bexp == 0x7FF, mant == 0) at
line 24 and returns ULONG_MAX at line 27 without checking the sign bit.
Both +inf and -inf hit this path. The sign check at line 35 is dead code
for -inf because the function already returned.

Firedancer:  fd_rust_cast_double_to_ulong(-INFINITY) = 18446744073709551615
Rust (1.45+): (-f64::INFINITY as u64)                = 0

Cross-verified by compiling and running the equivalent Rust program.

The existing test (test_cast.c:17) encodes the incorrect behavior:
  FD_TEST( fd_rust_cast_double_to_ulong( ninf ) == ULONG_MAX );

This function is used in:
  - fd_sysvar_rent1.c:12   (rent exempt minimum balance)
  - fd_stake_program.c:551 (stake warmup)
  - fd_stake_program.c:636 (stake cooldown)
  - fd_runtime.c:525       (rent calculation)

Current call sites use non-negative intermediates, so -infinity is
unlikely to occur today. However, the function's contract is violated
and any future call site producing a negative-infinity intermediate
would cause a consensus split between Firedancer and Agave.

--- Fix ---

In the infinity branch (line 26-27), check the sign bit:

  if( fd_dblbits_mant( u )==0 ) {
    return fd_dblbits_sign( u ) ? 0UL : ULONG_MAX;
  }

Update test_cast.c:17 to assert the correct result:
  FD_TEST( fd_rust_cast_double_to_ulong( ninf ) == 0 );

4. TIMELINE

2025-02-07  Bugs identified and POCs developed
2025-02-07  Attempted disclosure to Immunefi; unable to validate researcher identity
2025-02-08  Attempted disclosure to Immunefi; unable to validate researcher identity
2025-02-09  Attempted disclosure to Immunefi; unable to validate researcher identity
2025-02-09  Agent Spooky votes on Full Disclosure; measure passes unanimously.
2025-02-10  Full Disclosure happens.

5. CREDIT

AGENT SPOOKY AND YOUR MOM

Cheers!

Agent Spooky's Fun Parade

P.S. SHOUT OUT TO IMMUNEFI FOR BEING YOUR TYPICAL RUN OF THE MILL CRYPTO BRO HUSTLERS AKA PUNK ASS BITCHES.
WE WON'T FORGIVE. WE WON'T FORGET. ALL YOUR CRYPTO ARE BELONG TO US.

_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#14)
[![Next](/images/right-icon-16x16.png)](15)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#14)
[![Next](/images/right-icon-16x16.png)](15)

### Current thread:

* **Firedancer Solana Validator - QUIC Transport Parameter UB and Consensus-Splitting Cast Bug** *Agent Spooky's Fun Parade via Fulldisclosure (Feb 16)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [...