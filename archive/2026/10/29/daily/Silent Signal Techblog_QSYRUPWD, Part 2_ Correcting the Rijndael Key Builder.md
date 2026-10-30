---
title: QSYRUPWD, Part 2: Correcting the Rijndael Key Builder
url: https://blog.silentsignal.eu/2026/10/29/qsyrupwd-part-2-correcting-the-rijndael-key-builder/
source: Silent Signal Techblog
date: 2026-10-29
fetch_date: 2026-10-30T07:56:42.060968
---

# QSYRUPWD, Part 2: Correcting the Rijndael Key Builder

[![Silent Signal](/assets/img/s2_avatar.jpg)](/)

Silent Signal

Professional Ethical Hacking Services

### Contact us

2026 © Silent Signal

![QSYRUPWD, Part 2: Correcting the Rijndael Key Builder](/img/part2.gif)

# QSYRUPWD, Part 2: Correcting the Rijndael Key Builder

[pz](/authors/pz.html) 2026-10-29

The Rijndael key builder in [Part 1](https://blog.silentsignal.eu/2026/07/28/the-cipher-behind-qsyrupwd-reconstructing-ibm-i-password-hashes/) worked for the first set of samples, but its split-buffer model was wrong. QSYS/QZLSRTPW builds one 32-byte value, `00×5 ‖ des_plaintext_16 ‖ format_byte ‖ username_cp037_10`, and insertion-sorts all 32 bytes in ascending order. I tested the corrected decoder against almost 900 `QSYRUPWD` API output buffers, which IBM i calls *receiver variables*. The decoder decrypted the 192-byte QZLS ciphertext field in every receiver that contained it and reproduced its embedded username.

There are several other corrections. The variable outer marker is the single byte at receiver offset 93, followed by fixed bytes `40F0`, and the seven-byte interpretation came from adjacent zero-filled data. That marker cannot be treated as a reliable copy of [`QPWDLVL`](https://www.ibm.com/docs/en/i/7.5.0?topic=passwords-password-level-qpwdlvl), the IBM i password-level system value. The corrected one-based SHA-1 slice order is `D[17..20] ‖ D[12..15] ‖ D[7..10] ‖ D[2..5]`.

Receiver and decrypted-plaintext offsets in this post are zero-based. Digest notation `D[1]` through `D[20] is one-based. IBM documents` QSYRUPWD` as an API that returns one-way encrypted password data for a specified user profile to an authorized caller. The byte-level names below are my reverse-engineering labels. IBM does not publish this layout as a data contract, and it may change between releases. IBM’s API documentation is available under [Retrieve Encrypted User Password (QSYRUPWD)](https://www.ibm.com/docs/en/i/7.5.0?topic=q-retrieve-encrypted-user-password-qsyrupwd).

## How the corpus broke the old model

My original key builder explained the examples I had at the time. It treated the legacy DES-verifier area as smaller pieces, stripped padding in some paths, and grew special cases around the assumed boundary. The plaintext looked right and the known hash cracked, so I moved on.

Later I ran it against a larger corpus from a separate IBM i 7.5 system configured with `QPWDLVL` 2. Many profiles had both eight-byte legacy slots populated, and several dozen used format byte `T` (`0x54`) instead of `D` (`0x44`). Receivers that looked similar combined different outer markers and decrypted layouts. A wrong key still returned 192 bytes of plaintext-shaped noise, which made failures less obvious than I would have preferred.

The decrypted `QZLS` structure starts with the same ten-byte EBCDIC username stored in the receiver. I used that as a cheap oracle and rejected a key unless plaintext bytes 0..9 matched receiver bytes 8..17 exactly.

I first preserved the two eight-byte halves. Then I tried stripping `0x40` padding and moving bytes across the boundary when the second slot was populated. Hard-coding D survived until the first T record. Records with two populated slots failed in one branch, while T records failed in another. Empty legacy areas worked only under assumptions that contradicted the populated cases.

At that point I went back to the generated instructions in `QSYS/QZLSRTPW` and followed the byte loads and stores around the key buffer. The loop was insertion sort.

The first successful records had one populated slot followed by eight `0x40` bytes. This synthetic shape explains why the original model looked plausible:

```
B35DF85FA7E6B31A 4040404040404040
| populated slot | empty slot     |
```

The full synthetic fixture later in this post uses both slots:

```
B35DF85FA7E6B31A 4FAE64805DFC20B5
| populated slot | populated slot |
```

The same loop handles both shapes without a separate key-building branch.

## Receiver layout

The observed 2,000-byte receiver in IBM’s [`UPWD0100` format](https://www.ibm.com/docs/en/i/7.5.0?topic=q-retrieve-encrypted-user-password-qsyrupwd) has the following layout. The table includes fields that document the surrounding Machine Interface (MI) CIPHER call chain even when the current decoder does not consume them:

| Receiver offsets | Length | Observed purpose |
| --- | --- | --- |
| 0..3 | 4 | Bytes returned, big-endian |
| 4..7 | 4 | Bytes available, big-endian |
| 8..17 | 10 | `0x40`-padded EBCDIC username |
| 18 | 1 | Format byte, D or T |
| 19..34 | 16 | Wrapped or null legacy DES area |
| 35..51 | 17 | Internal zero/padding area (Zero\_1); unused by this recovery path |
| 52 | 1 | Fixed 05 byte |
| 53..72 | 20 | Wrapped or null SHA-1 area |
| 73..92 | 20 | Internal zero/padding area (Zero\_2); unused by this recovery path |
| 93 | 1 | Outer marker |
| 94..95 | 2 | Fixed 40F0 |
| 96..287 | 192 | QZLS Rijndael ciphertext or a 0x40-filled null field |
| 288..319 | 32 | CBC chaining value produced by the third QZLSRTPW CIPHER |
| 320..383 | 64 | Block returned by the fifth QSYRUPWD CIPHER |
| 384..1979 | 1,596 | Remaining internal/padding area; unused here |
| 1980..1999 | 20 | Key-derivation digest D |

[Part 1](https://blog.silentsignal.eu/2026/07/28/the-cipher-behind-qsyrupwd-reconstructing-ibm-i-password-hashes/) attributed NT recovery to the fifth `QSYRUPWD` CIPHER. Its own captured control block describes that call as a 64-byte ECB operation. The NT fields recovered here come from the plaintext of the 192-byte field at 96..287, produced by the third `QZLSRTPW` CIPHER with a 32-byte key, 32-byte blocks, and CBC mode. The fifth-call output is the separate 64-byte field at 320..383.

The chaining value and fifth-CIPHER block remain useful when reconstructing the complete CIPHER call chain. They exist in the observed receiver, but the current decoder does not use or export bytes 288..383.

Fixed offsets matter. The search pattern `00000000000240F0` is eight bytes and pulls zeroes from Zero\_2 into the incorrectly inferred seven-byte marker `000000000240F0`. Trimming trailing zeroes and searching backward can also shift the digest away from 1980..1999 and quietly derive the wrong AES key.

I do not know what format byte `T` means semantically. The program includes its literal value (`0x54`) in the same key input position used by `D` (`0x44`), so I preserve it.

## The insertion sort and reconstructed key

The excerpt below comes from MAIN in `QSYS/QZLSRTPW`, a `*PGM`. I omitted unrelated setup and compiler-generated bounds checks.

Instruction locations are shown as decimal offsets in my disassembly listing.

```
9504:   ADDI 19,0,1
        ... unrelated instructions omitted ...
9560:   LBZ 7,0XFDE1(31)
9564:   ADDI 5,19,-1
        ... bounds checks omitted ...
9588:   LBZ 11,0X220(4)
9592:   CMP 0,0,11,7
9596:   BC 4,1,0X38
        ... bounds checks omitted ...
9624:   STB 11,0X220(10)
        ...
9660:   ADDI 9,5,-1
        ... bounds checks omitted ...
9692:   LBZ 11,0X220(4)
9696:   CMP 0,0,11,7
9700:   BC 12,1,0XFFA0
9708:   ADDI 10,19,1
        ... bounds checks omitted ...
9724:   EXTSW 19,10
        ... bounds checks omitted ...
9744:   STB 7,0X220(8)
9752:   CMPLI 0,0,10,32
9760:   BC 12,0,0XFF88
```

The compiler reuses registers, so their roles depend on the instruction being executed.

`r19` holds the outer index `i`. At the end of the outer loop, `r10` holds `i + 1`, and `r19` is updated from it.

`LBZ 7,0XFDE1(31)` loads the saved current byte into `r7` from a compiler frame slot populated earlier. `r31` is the frame base for that load.

Inside the backward scan, `r5` is the active index `j`, initialized to `i - 1`. `r9` temporarily holds `j - 1`, and omitted bounds and copy instructions feed it into the next inner-loop iteration. `r11` holds `key[j]`.

The memory accesses show the address-register roles. `LBZ 11,0X220(4)` uses `r4` for `key[j]`. `STB 11,0X220(10)` uses `r10` for the right-shift s...