---
title: [0day-rubbish] PacsOne Server 7.3.9 authenticated DICOMweb STOW-RS SOP Instance UID path traversal to www-data code execution on a PACS host (7.2)
url: https://seclists.org/fulldisclosure/2026/Oct/18
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:51.771763
---

# [0day-rubbish] PacsOne Server 7.3.9 authenticated DICOMweb STOW-RS SOP Instance UID path traversal to www-data code execution on a PACS host (7.2)

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] PacsOne Server 7.3.9 authenticated DICOMweb STOW-RS SOP Instance UID path traversal to www-data code execution on a PACS host (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Oct 2026 02:22:16 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in PacsOne
Server 7.3.9, Premium Edition, Linux x86-64 distribution, the closed-source
commercial PACS (medical imaging archive and DICOM server) from RainbowFish
Software, California, United States. The product combines a native C++ DICOM
and HL7 service with a PHP web interface of 204 endpoints running on MySQL
and Apache, fronted by a single Apache alias that maps /pacsone to the
product's php/ directory.

Type: path traversal on a file-write sink (CWE-22 primary; CWE-73 External
Control of File Name or Path and CWE-20 Improper Input Validation
contributing). The DICOMweb STOW-RS handler stowrs.php reads the SOP Instance
UID attribute (0008,0018) out of the posted DICOM object and uses it as the
storage filename. In import() in dicomweb.php, approximately lines
1391-1440, the construction is:

    $uid     = $rawTags->getAttr(0x00080018);
    $dir     = dirname($tempfile);
    $newfile = $dir . "/" . $uid;
    rename($tempfile, $newfile);

$dir is the per-day study directory under the configured archive root, from
getStowRsStoreDir() in database.php:1780; $tempfile is staged in that same
directory by DicomWebStow::__construct (dicomweb.php:1165), which reads the raw
body from php://input, splits it on the declared boundary and writes each
application/dicom part through tempnam() and file_put_contents(); and $uid is
the raw attribute value as it appeared on the wire: RawTags::getAttr()
(dicom.php:4516) returns it unfiltered, and the Explicit VR parser
parseDataExplicit() (dicom.php:4378) applies trim() only, which is VR padding
normalisation and not a security control. The presence checks in store()
(dicomweb.php:1592) verify only that
the SOP Class, SOP Instance, Study and Series Instance UIDs are non-empty,
which any non-empty string satisfies. There is no character whitelist, no
canonicalisation, no length bound and no containment check on this path, so a
SOP Instance UID of ../../../php/x.php moves the received object out of the
study directory and into the directory Apache serves through the /pacsone
alias. The 128-byte DICOM Part 10 preamble is never interpreted by the DICOM
parser, so it can carry a PHP marker script, and once the file is in the
served tree mod_php executes it under the web server identity.

The identity reached is uid=33(www-data) gid=33(www-data)
groups=33(www-data) - the Apache worker serving the request, confirmed by id,
whoami, a read of /etc/passwd, a marker write-and-read under /tmp, hostname
and uname. There is no child process and no identity change in this chain.
Root was not reached and is not claimed; no privilege escalation, no
container or host escape, and no contact with any other machine was
attempted.

The ordering inside import() decides both whether the write is usable and
whether a reproduction appears to work. rename() executes BEFORE the database
inserts, so no database-layer control - schema constraint, length limit,
uniqueness check - sits upstream of the damage, and the operation is not
transactional: the file lands even when the corresponding study record never
does. Each of the image, series, study and patient inserts is followed on
failure by unlink($newfile), so a minimal DICOM object writes the payload and
then deletes it, returning HTTP 409 with failure reason 272 (ProcessingFailure).
Making all four inserts succeed requires Patient Name (0010,0010), Patient ID
(0010,0020) and the pixel attributes (0028,xxxx). Anyone attempting a
reproduction without those attributes will watch the file disappear and may
conclude this is a false positive. It is not.

The root cause is an asymmetry rather than a general absence of input
validation. The product contains a UID validator, isUidValid(), and does call
it on the unauthenticated wadoAnonymized.php read path, where its character
whitelist blocks "/" and therefore blocks traversal. The store path that turns
a UID into a filename never calls it. Two details narrow where a fix has to
go: the server uses the dataset value and not the file meta header value, so
a validator bolted onto the meta header parse alone would miss this (the
verified object carried an ordinary dotted UID in (0002,0003) and the
traversal in (0008,0018)); and the parser is structurally lenient - it
accepted a (0028,xxxx) group emitted in non-ascending order - so leniency
cannot be relied on to reject malformed identifiers either.

How confirmation works. The STOW-RS JSON response echoes the identifier back,
so the outcome is machine-readable without any filesystem access: the nested
sequence carries (0008,1155) with the traversal string verbatim plus a
per-instance Retrieve URL in which it appears percent-encoded, a success
arrives as HTTP 200 and a failure as HTTP 409 with failure reason 272. That
makes the one deployment-variable quantity - how many ../ components separate
the study directory from a served directory - cheap to enumerate with clear
feedback and one request per guess, which is why Attack Complexity is rated
Low. Three components on the layout we configured; Setup.exe lets the
operator choose the archive directory, so another installation needs a
different count. The target directory has to satisfy only two conditions: the
web server user can write into it, and something served by the web server
executes files there. Relocating the archive outside the web tree is therefore
hardening rather than a fix. We did not reconcile this build's use of
(0008,1199) for the successful-store sequence against the DICOM PS3.18
STOW-RS response definition, and nothing in the finding depends on that tag
numbering. Execution is then confirmed by an unauthenticated GET for the
written file: the gate protects the store operation, not the file the store
operation created. The response body begins with the command's stdout and is
followed by the binary remainder of the DICOM object rendered as literal
output, which is itself evidence that the whole object, preamble included, was
written intact. The file on disk was 580 bytes - the size of the object sent -
owned by the web server identity at mode 0600. That mode is what tempnam()
creates and rename() preserved; it does not obstruct execution, because the
writer, the owner and the interpreter are the same uid.

What was deliberately not reproduced: the rename()/unlink() pairing on the
failure branch, which is argued from POSIX rename() atomic-replace semantics
and from the shipped code rather than exercised. Because unlink($newfile)
operates on the same attacker-chosen path, a deliberately failing store can
replace and then remove an existing file that the web server user can write.
The primitive is then not only "write an attacker-chosen file" but also
"replace and then delete a file whose name the attacker chooses, inside any
directory the web server user can write". No procedure for it is published and
the PoC refuses to target any path that already ...