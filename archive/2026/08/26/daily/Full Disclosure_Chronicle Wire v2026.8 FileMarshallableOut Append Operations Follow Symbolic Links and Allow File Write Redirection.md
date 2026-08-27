---
title: Chronicle Wire v2026.8 FileMarshallableOut Append Operations Follow Symbolic Links and Allow File Write Redirection
url: https://seclists.org/fulldisclosure/2026/Aug/83
source: Full Disclosure
date: 2026-08-26
fetch_date: 2026-08-27T12:14:27.367592
---

# Chronicle Wire v2026.8 FileMarshallableOut Append Operations Follow Symbolic Links and Allow File Write Redirection

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

[![Previous](/images/left-icon-16x16.png)](82)
[By Date](date.html#83)
[![Next](/images/right-icon-16x16.png)](102)

[![Previous](/images/left-icon-16x16.png)](82)
[By Thread](index.html#83)
[![Next](/images/right-icon-16x16.png)](102)

![](/shared/images/nst-icons.svg#search)

# Chronicle Wire v2026.8 FileMarshallableOut Append Operations Follow Symbolic Links and Allow File Write Redirection

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 22 Aug 2026 08:41:27 -0400

---

```
Chronicle Wire's FileMarshallableOut follows symbolic links when writing
files in append mode. When ?append=true is enabled, the implementation
opens the supplied output path directly using FileOutputStream(path, true)
without preventing symbolic-link resolution.

If an attacker can create or replace the expected output file with a
symbolic link before the append operation occurs, the operating system
resolves the link and Chronicle Wire writes to the link target using the
privileges of the application process.

This can redirect application-generated output from its intended
destination to another file writable by the application.

The proof of concept confirms that an append operation directed at a
symbolic-link path modifies the underlying target file. A separate boundary
test confirms that non-append overwrite mode does not exhibit the same
behavior: the symbolic-link path is replaced while the original target
remains unchanged.

The vulnerability is therefore specifically limited to the append-mode
file-opening path.
Vulnerability Details

FileMarshallableOut determines the destination used for file output based
on whether append mode is enabled:

final String path = url.getPath();
final String path0 = options.append ? path : (path + ".tmp");

When append mode is disabled, Chronicle Wire writes through a temporary
path.

When append mode is enabled, however, path0 directly references the
supplied destination:

path0 = path;

The resulting file is opened using:

try (FileOutputStream out =
         new FileOutputStream(path0, options.append)) {

    final Bytes<byte[]> bytes =
        Jvm.uncheckedCast(wire.bytes());

    out.write(
        bytes.underlyingObject(),
        0,
        (int) bytes.readLimit());
}

In append mode, the effective operation is therefore:

new FileOutputStream(path, true);

No protection against symbolic-link resolution is applied when this file is
opened.

If path identifies a symbolic link, normal filesystem resolution causes the
underlying target to be opened and modified.

The existing path validation does not prevent this condition:

String path = url.getPath();

if (path == null ||
    path.isEmpty() ||
    path.contains(".."))
    throw new IllegalArgumentException(
        "Invalid file path: " + path);

This prevents certain malformed or traversal-style paths but does not
protect the final destination from symbolic-link substitution.
Root Cause

The append implementation opens the destination using a filesystem
operation that follows symbolic links without enforcing a no-follow policy.

The vulnerability does not require .. traversal or an unusual path syntax.
The apparent destination itself can be a valid filesystem path while
referencing a symbolic link created or substituted by another user or
process.

This creates a security issue when there is a privilege or trust-boundary
difference between the process performing the append operation and the
party capable of manipulating the destination filesystem entry.

For example, a less-privileged attacker may be able to create or replace a
predictable output file within a shared or attacker-writable directory. If
a more privileged application subsequently performs a FileMarshallableOut
append against that path, the resulting write can be redirected to a
different file accessible to the application.
Security Impact

An attacker capable of manipulating the filesystem entry used as an append
destination may redirect Chronicle Wire output to another file writable by
the application's privileges.

Potential consequences depend on the target application's filesystem
permissions and the contents being written.

Affected deployment patterns may include applications writing to:

   - shared writable directories;
   - predictable temporary locations;
   - application export directories;
   - CI/CD workspaces;
   - shared container volumes;
   - cache or working directories;
   - plugin-controlled filesystem locations; or
   - other locations where a less-privileged party can manipulate
   destination entries.

The confirmed security primitive is *file write redirection through
symbolic-link following*.

The proof of concept does not establish arbitrary file overwrite because
the affected operation uses append semantics. The attacker-selected target
must also be writable by the application process.
Proof of Concept

The proof of concept creates an ordinary target file containing:

before

A symbolic link named:

safe-looking-output.yaml

is then created pointing to:

target.txt

Chronicle Wire is instructed to write to safe-looking-output.yaml with
append mode enabled.

The apparent destination is therefore the symbolic-link path, while the
actual filesystem object modified by the operation is target.txt.
Observed Results

The test confirmed the symbolic-link destination and target:

FileMarshallableOut append followed symlink:
/.../safe-looking-output.yaml

FileMarshallableOut symlink target:
/.../target.txt

Before the Chronicle Wire operation, the target contained:

FileMarshallableOut symlink content before BEGIN
before
FileMarshallableOut symlink content before END

The value supplied to FileMarshallableOut was:

FileMarshallableOut symlink value written:
message=symlink-append-proof

After the append operation, the target contained:

FileMarshallableOut symlink content after BEGIN
before
message: symlink-append-proof
...
FileMarshallableOut symlink content after END

The original contents remained and the Chronicle Wire output was appended
directly to the symbolic-link target.

This confirms that FileMarshallableOut followed the symbolic link during
the append operation.
Boundary Validation

Non-append mode was tested separately to determine whether the behavior
affected all FileMarshallableOut file writes.

The original target contained:

before

After performing the non-append operation through the symbolic-link path,
the original target still contained:

before

The test confirmed that non-append processing replaced the symbolic-link
path rather than following the link and modifying its original target.

The demonstrated vulnerability is therefore specifically associated with:

?append=true

and the corresponding:

new FileOutputStream(path, true);

file-opening path.
PoC Results

The security test confirmed the following behavior:

[CONFIRMED] Append destination was a symbolic link[CONFIRMED] Symbolic
link referenced a separate target file[CONFIRMED] Chronicle Wire
opened the apparent destination in append mode[CONFIRMED] Output was
written to the symbolic-link target[CONFIRMED] Original target
contents remained intact[CONFIRMED] Chronicle Wire data was appended
to the target[CONFIRMED] Non-append mode did not modify the original
symlink target

The runtime evidence demonstrates that append-mode output can cross the
apparent filesystem boundary established by the supplied destination path.

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Applicat...