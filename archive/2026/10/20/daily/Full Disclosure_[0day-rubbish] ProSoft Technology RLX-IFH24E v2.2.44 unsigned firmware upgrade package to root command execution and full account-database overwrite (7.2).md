---
title: [0day-rubbish] ProSoft Technology RLX-IFH24E v2.2.44 unsigned firmware upgrade package to root command execution and full account-database overwrite (7.2)
url: https://seclists.org/fulldisclosure/2026/Oct/32
source: Full Disclosure
date: 2026-10-20
fetch_date: 2026-10-21T06:51:03.994576
---

# [0day-rubbish] ProSoft Technology RLX-IFH24E v2.2.44 unsigned firmware upgrade package to root command execution and full account-database overwrite (7.2)

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

[![Previous](/images/left-icon-16x16.png)](31)
[By Date](date.html#32)
[![Next](/images/right-icon-16x16.png)](33)

[![Previous](/images/left-icon-16x16.png)](31)
[By Thread](index.html#32)
[![Next](/images/right-icon-16x16.png)](33)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] ProSoft Technology RLX-IFH24E v2.2.44 unsigned firmware upgrade package to root command execution and full account-database overwrite (7.2)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 20 Oct 2026 02:31:17 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in the
ProSoft RLX-IFH24E, version v2.2.44, the industrial wireless radio from
ProSoft Technology, Inc. (United States). The appliance is a closed-source
embedded device and an OEM build of the MicroHard Systems IPx21 platform on
the MHX-910 board design: an Intel IXP425 XScale processor, ARM
big-endian, Linux 2.4.24-uc0, with static management pages under /usr/web
and 57 ARM big-endian CGI programs under /usr/lib/cgi-bin/ served by boa
over HTTP and boa_ssl over HTTPS.

The vendor is identified precisely here, by its legal name, its published
headquarters address and its support domain, because a different and
unrelated company trades under a similar name in another country, and this
research concerns the United States industrial radio vendor only. ProSoft
Technology's own legal pages give the entity as ProSoft Technology, Inc.,
9201 Camino Media, Suite 200, Bakersfield, CA 93311, USA, and its support
pages note that support addresses moved from the vendor domain to
belden.com, the domain of its parent company.

THE EVIDENTIAL BOUNDARY, BEFORE ANYTHING ELSE

This disclosure has an unusual evidentiary shape and it is stated up front
so that no reader over-reads it. No HTTP request was ever issued at this
product. No physical appliance was used at any point. The chain is therefore
not presented as an exploit run against a live device, and it is not one.

The finding has two halves. The installer half was measured: the firmware's
own /sbin/upgrade script and the other scripts in /sbin were executed
byte-for-byte unmodified inside an isolated chroot sandbox built on a copy
of the upgrade package's own root filesystem, with marker files and a
recorded executing uid as the evidence. The upload half was inferred: it
rests entirely on disassembly of the shipped ARM big-endian CGI and of the
shared platform UI library, and nothing in it was observed in motion. The
line between those two halves runs down the middle of the chain and is drawn
explicitly wherever it appears in the published analysis.

TYPE AND ROOT CAUSE

Code installed and executed without an integrity or authenticity check.
CWE-494 is the primary classification, with CWE-345 and CWE-347 co-equal
because the only check anywhere in the path is a non-cryptographic string
equality and no signature is verified at any point. CWE-434, CWE-73, CWE-250
and CWE-269 are contributing and are reported separately without raising any
metric. This is explicitly not CWE-78: no command string is injected at
either hop, so a command-injection remediation, filename input filtering or
shell escaping would not close the chain. The shared platform helper
SubProgram_Start at offset 0xbd5c splits its argument string on spaces with
strtok into at most eight tokens and then calls vfork and execvp directly,
so no shell is involved at all.

The system upgrade package RLX-IFH24E_v2244.pkg contains four artefacts
that together describe the whole path: the upload handler
usr/lib/cgi-bin/tool_reprogramming.cgi, the installer /sbin/upgrade that it
invokes as a root process, the factory account database /etc/passwd, and
the default configuration store /etc/db1.

The upload hop, recovered by disassembly. HandleSubmit at offset 0x8d1c
takes the file1 part of a multipart/form-data POST to
/cgi-bin/tool_reprogramming.cgi and performs this sequence, with the format
string sitting at rodata offset 0x2b1c:

    cgiFormFileName("file1")     -> the client's original filename
    cgiFormTempFileName          -> path of the temporary body file
    sprintf(buf, "%s /upgrade/upgrade/%s", tempfile, origfilename)
    SubProgram_Start("/bin/mv", buf)              ; must succeed first
    SubProgram_Start("/sbin/upgrade", origfilename)

The original client filename is used unmodified twice: once to build the
destination of the move, and once as the installer's only argument. That
makes the file extension, and therefore the branch the installer takes,
entirely the requester's choice. The handler applies no extension
whitelist, no digest comparison and no path canonicalisation.

The installer hop, executed and observed. /sbin/upgrade is a short POSIX
shell script that runs with the privileges of the CGI that invoked it,
which are root, and dispatches purely on ${FILE##*.}:

    case "$EXT" in
      passwd)  cp /upgrade/upgrade/$FILE /etc/passwd
               cp /upgrade/upgrade/$FILE /etc/passwd_original ;;
      factory) cp /upgrade/upgrade/$FILE /etc/db1 ;;
      pkg)     gunzip -t /upgrade/upgrade/$FILE || exit 1
               tar -xf /upgrade/upgrade/$FILE -C <staging>
               [ "$DEVICE_PRODUCT_NAME" = "$PKG_LOCK_NAME" ] || refused
               echo "Match image."
               ./pre
               tar -xf extract/upgradepkg.tar -C /
               ./post
               echo "Upgrade Successful"
               reboot ;;
    esac

The .pkg branch is the code-execution primitive. ./pre runs before anything
else is applied, so requester-authored code executes against the pristine
filesystem and can read the old state; tar -xf extract/upgradepkg.tar -C /
applies an inner archive whose entry names are constrained in no way, which
is an arbitrary rootfs write; ./post runs after the write, so the same
requester also sees the new state; and the branch ends in an unconditional
reboot, which makes the change persistent and destroys the runtime
evidence. The .passwd branch is a second, independent route to the same
privilege ceiling and it needs no execution at all: it copies the upload
over both the live account database and the backup copy, so the device's own
recovery path restores the modified database rather than the shipped one.
The .factory branch is the same primitive aimed at the configuration store.

The only validation the installer performs before executing package content
is a string equality, and both of its operands are available to whoever
supplies the package. The expected value DEVICE_PRODUCT_NAME is read from
the appliance's own platform identity file /etc/MHX_CONFIG, where this
firmware records PRODUCT_NAME=IPx21PROSOFT, a compile-time constant
recoverable by reading the shipped firmware once. The asserted value
PKG_LOCK_NAME is read from a file called lockfile inside the package being
installed. A package whose identity is validated against a value carried
inside that same package is not a source of assurance about that package.
The gunzip -t test beside it is a gzip stream-integrity check and proves
only that the file is well-formed. The check that exists was never meant to
answer the authenticity question, and strengthening it would change nothing
while the requester supplies both sides; what is missing from the path
between an HTTP request and root execution is any authenticity step at all.

WHAT WAS MEASURED

A crafted .pkg carrying the correct platform string was placed in the
staging directory, reproducing by hand t...