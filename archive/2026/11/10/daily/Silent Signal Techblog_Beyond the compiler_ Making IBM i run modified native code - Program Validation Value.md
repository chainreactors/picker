---
title: Beyond the compiler: Making IBM i run modified native code - Program Validation Value
url: https://blog.silentsignal.eu/2026/11/10/Beyond-the-compiler-Making-IBM-i-run-modified-native-code-PVV/
source: Silent Signal Techblog
date: 2026-11-10
fetch_date: 2026-11-11T08:35:34.888582
---

# Beyond the compiler: Making IBM i run modified native code - Program Validation Value

[![Silent Signal](/assets/img/s2_avatar.jpg)](/)

Silent Signal

Professional Ethical Hacking Services

### Contact us

2026 © Silent Signal

![Beyond the compiler: Making IBM i run modified native code - Program Validation Value](/img/door.gif)

# Beyond the compiler: Making IBM i run modified native code - Program Validation Value

[pz](/authors/pz.html) 2026-11-10

## Why this matters

IBM i does not treat an application program as a normal file that happens to
contain POWER instructions. A compiler produces Machine Interface (MI) code,
IBM i’s stable instruction-level boundary, and the system translates it into a
native form. The generated native code contains checks that support the IBM i
object and tagged-pointer model.

Changing those instructions can make IBM i execute behavior that was not
present in the MI input. Earlier
[Below MI research](https://silentsignal.github.io/BelowMI/) examined the wider
consequences on IBM i V7R4. Here I focus on the IBM i 7.5
[Program Validation Value (PVV)](https://www.ibm.com/docs/ssw_ibm_i_74/rzamv/rzamvprotectagainstviruses.htm),
a 32-byte value stored with a saved program.

I reconstructed the 32-byte PVV calculation and matched all 1,223 known-valid
values. The reconstructed calculation derives its HMAC key entirely from saved
program attributes and fixed Licensed Internal Code (LIC) constants; it
contains no separate secret for origin authentication. IBM i applies separate
digital-signature checks where required. In controlled USER-state programs—the
ordinary, non-SYSTEM execution mode—recalculating PVV and the separate save-file
checks allowed selected native instruction changes to survive restore and
resave. A disposable CrackMe produced the expected changed output,
demonstrating execution.

USERB1, an ordinary test account without special authorities, restored a
USERB1-owned, PVV-repaired `MEMDUMP` program through IBM’s Restore Object List
(`QSRRSTO`) API, and a resave preserved its modified native instructions. Its
executable payload matched byte-for-byte the payload used in a controlled
runtime test. In that test, `MEMDUMP` ran as USERB1 and read from a known-address
USER-domain buffer in a cooperating job running under QSECOFR, IBM i’s
security-officer profile. Other controls showed IBM i rejecting unsigned SYSTEM
and INHERIT program-state variants and enforcing the SYSTEM-domain access
boundary.

My [previous article](https://blog.silentsignal.eu/2026/10/06/512-bytes-at-a-time-reconstructing-IBM-i-save-file-checksums/)
covered the outer save file (SAVF) container: its per-record checksums and
global checksum. During restore, IBM i also calculates PVV and compares it
with four values stored in the saved program.

The USER-state controls ran under the test system’s existing
[restore-policy system values](https://www.ibm.com/docs/en/i/7.5.0?topic=40-validation-programs-being-restored)
(`QVFYOBJRST=3`, `QFRCCVNRST=1`, and `QALWOBJRST=*ALL`) at
[QSECURITY 40](https://www.ibm.com/docs/en/i/7.5.0?topic=reference-using-system-security-qsecurity-system-value),
which enforces resource security and integrity protection.

## Program validation and research approach

SAVF record and global checks establish container consistency; PVV establishes
consistency with selected serialized program data. LIC copies the 32-byte
descriptor unchanged into the HMAC key object. Every descriptor byte
comes from saved program attributes or fixed LIC constants, and the recovered
path contributes no additional secret. A party with the serialized program and
the reconstructed algorithm can therefore derive the key and recompute PVV; a
match establishes consistency, not trusted origin. Restore authorization and
system policy still govern the operation, while digital signatures authenticate
origin where required.

A program has separate
[state and domain attributes](https://www.ibm.com/docs/en/i/7.5.0?topic=40-preventing-use-unsupported-interfaces).
Its execution state is USER, SYSTEM, or INHERIT; INHERIT uses the caller’s
state. The program object itself has a USER or SYSTEM domain, and that saved
attribute contributes separately to the PVV descriptor. Other objects accessed
by the executing code also have domains. The USER domain is a storage-domain
classification, not a user identity or ownership boundary. At QSECURITY 40,
USER-state code cannot directly access SYSTEM-domain objects.

### The algorithm at a glance

```
PVV = HMAC-SHA-256(descriptor, canonical_message)
```

PVV is calculated in four steps for the supported program format:

1. Walk the saved program graph, select the protected byte ranges, normalize
   saved pointers, and put the ranges into canonical-message order.
2. Build a 32-byte descriptor from program attributes and constants chosen
   by the recovered state, domain, version, release, and mode selectors.
3. Use the descriptor as the HMAC key and the canonical message as the input to
   HMAC-SHA-256.
4. Split the result into four 64-bit values and compare them with the stored
   values.

### Leif Svalgaard’s earlier PVV work was a clue

Leif Svalgaard described the earlier mechanism in Chapter 15, “Program
Validation Value,” of [AS/400 Machine Level Programming](https://web.archive.org/web/20220523023735/https%3A//svalgaard.leif.org/as400/mlp0tc.htm).
His [public program index](https://web.archive.org/web/20220523023735/https%3A//svalgaard.leif.org/as400/programs/index.htm)
also lists `MIPGMVV`, which calculates an eight-byte value from program
attributes. I reproduced his published example. Its four selector constants do
not match the current LIC descriptor constants in either byte order, but both
designs select values according to state and domain. That similarity pointed
me toward the current 32-byte validation route.

## Finding the validator

I started with `CHKOBJITG`, the IBM i command that checks object integrity.

For a program, `CHKOBJITG` reaches the IBM-supplied `QSYS/QSYCHKIT` program.
Its native procedure `QSYINTEGRI::checkPgmMod` contains this sequence, copied
from the retained IBM Display/Alter/Dump (DAD) output:

```
2B463690C5 0052B4  0000D4  62E30000  ORI 3,23,0
2B463690C5 0052B8  0000D8  39400103  ADDI 10,0,259
2B463690C5 0052BC  0000DC  44000141  SCV 10
```

`ADDI` loads selector 259 into `r10`; the following `SCV 10`, Supervisor Call
Vectored, enters dispatcher vector 10. The `10` in the mnemonic identifies the
vector, while the value in `r10` selects the service. That combination led to
this observed call path:

```
QSYCHKIT/QSYINTEGRI::checkPgmMod
  -> #cfmir
  -> #dotssob
  -> VBNTSSOB::#bntssob
  -> VBNTSSOB::vbnskew4
  -> VBNNAPE2::vbnspnt2
```

The live capture tied the path to the loaded address of my `CALLAES` test
fixture. I matched the remaining code against the IBM i 7.5 LIC from
installation media by procedure name, normalized instruction sequence, call
topology, constants, and tables. The live instructions and invocation frames
identify the observed `CHKOBJITG` route; the build-matched LIC supplies the
complete procedure bodies. For both `VBNTSSOB` and `VBNNAPE2`, the installation
addresses were `0x3000` above the captured live addresses and the normalized
bodies agreed; that displacement is evidence for this match, not an IBM i
addressing rule.

## Reconstructing PVV

My parser supports uncompressed IBM i 7.5 program (`*PGM`) and service-program
(`*SRVPGM`) items whose record graph, section descriptors, and 40-bit segment
identity plus 24-bit in-segment pointer mapping follow the recovered layout. It
rejects other layouts before calculation instead of trying models until one
happens to match the stored result.

### The stored result

`vbnspnt2` writes 32 calculated bytes, loads them as four 64-bit doublewords,
and compares them with four values stored in different parts of the program
graph. Any mismatch returns false.

For `CALLAES`, the item starts at SAVF logical offset `0x4000`. The item-relative
offset must first be converted to a SAVF logical offset. That logical ...