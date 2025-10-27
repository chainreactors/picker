---
title: Evolution of the ELF object file format
url: https://maskray.me/blog/2024-05-26-evolution-of-elf-object-file-format
source: MaskRay
date: 2024-05-27
fetch_date: 2025-10-06T16:49:16.040809
---

# Evolution of the ELF object file format

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2024-05-26](/blog/2024-05-26-evolution-of-elf-object-file-format)

# Evolution of the ELF object file format

Updated in 2025-09.

The ELF object file format is adopted by many UNIX-like operating
systems. While I've [previously delved
into](/blog/2024-01-14-exploring-object-file-formats) the control structures of ELF and its predecessors, tracing the
historical evolution of ELF and its relationship with the System V ABI
can be interesting in itself.

The format consists of the generic specification, processor-specific
specifications, and OS-specific specifications. Three key documents
often surface when searching for the generic specification:

* *Tool Interface Standard (TIS) Portable Formats Specification,
  version 1.2* on <https://refspecs.linuxfoundation.org/>
* [*System
  V Application Binary Interface - DRAFT - 10 June 2013*](https://www.sco.com/developers/gabi/latest/contents.html) on
  www.sco.com
* *Oracle Solaris Linkers and Libraries Guide*

The TIS specification breaks ELF into the generic specification, a
processor-specific specification (x86), and an OS-specific specification
(System V Release 4). However, it has not been updated since 1995. The
Solaris guide, though well-written, includes Solaris-specific extensions
not applicable to Linux and \*BSD. This leaves us primarily with the
System V ABI hosted on www.sco.com, which dedicates Chapters 4 and 5 to
the ELF format.

Let's trace the ELF history to understand its relationship with the
System V ABI.

## History

[Unix
System Laboratories (USL)](https://en.wikipedia.org/wiki/Unix_System_Laboratories) created ELF for their System V Release 4
in late 1980s. USL also maintained the System V Application Binary
Interface, of which ELF was a core component. The dynamic shared library
system was contributed by Sun Microsystems from their [SunOS](https://en.wikipedia.org/wiki/SunOS) 4.x (in 1988, SunOS
4.0 got an extended a.out format with dynamic shared library
support).

USL intended ELF to be an open standard and published documents about
the format, e.g.

* In Proceedings of the Summer 1990 USENIX Conference, *ELF: An
  Object File to Mitigate Mischievous Misoneism* by James Q.
  Arnold
* *UNIX System V Release 4 Programmer's Guide: ANSI C and
  Programming Support Tools* (ISBN 0-13-933706-7) published in
  1990
* *System V Application Binary Interface (Standards)* (ISBN
  0-13-104670-5) published in 1993

In 1993, the Tool Interface Standard (TIS) Committee, a consortium of
industry leaders, adopted ELF and developed the "Tool Interface Standard
(TIS) Portable Formats Specification". Version 1.2 was released in May
1995.

ELF has been very influential. In the 1990s, many Unix and Unix-like
operating systems, including Solaris, IRIX, HP-UX, Linux, and FreeBSD,
switched to ELF. The 86open Project's FAQ specified:

> Q18: How can you get a single binary to work identically across all
> these diverse systems?
>
> Most Unix-on-Intel binary packages are already largely similar.
> Almost all such operating systems use the "ELF" binary 'packaging'; the
> various operating systems have small but significant differences,
> though, that make each system's ELF binary unusable on others'.

### The evolving stewardship of the System V ABI

The Tool Interface Standard (TIS) Committee essentially dissolved
after 1995. The stewardship of the System V ABI, and consequently the
generic ELF specification, has followed a complex path mirroring the
transfer of Unix software assets.

Between 1993 and 2011, Unix assets underwent a few transfers.

* In 1993, Novell [acquired
  Unix assets](https://en.wikipedia.org/wiki/Unix_System_Laboratories#Acquisition_by_Novell) including all copyrights, trademarks, and licensing
  contracts.
* In September 1995, Novell sold the "develop and sell licenses to
  Unix binaries" plus "handle source licencees" business to The Santa Cruz
  Operation (sometimes referred to as "old SCO"). Novell still owned the
  copyrights ([SCO
  vs Novell](https://en.wikipedia.org/wiki/SCO_Group%2C_Inc._v._Novell%2C_Inc.) verdict).
* In 2001, The Santa Cruz Operation sold its Unix software asserts to
  Caldera Systems (later renamed The SCO Group, Inc; sometimes referred to
  as "new SCO" or "SCOX").
* In 2011, The SCO Group's Unix software assets were sold off to UnXis
  (later renamed Xinuos).

**The task of maintaining and updating the generic ABI fell to
these successive owners of Unix software assets**. The Santa Cruz
Operation, and later The SCO Group and Xinuos, managed updates and
extensions to the ABI, including the ELF specification.

In this [binutils
commit](https://sourceware.org/cgit/binutils-gdb/commit/?id=723b0f0d39ebe18c9f28e238c9ecc27931faffa7) in November 2000, it was said that `e_machine`
values should eventually ask `registry@sco.com` for blessing
(now `registry@xinuos.com`).

Dave Prosser had [maintained](http://www.groklaw.net/article.php?story=20040130235310123)
the System V ABI at USL, then The Santa Cruz Operation, and then The SCO
Group. The last maintainer at The SCO Group and UnXis/Xinuous was John
Wolfe, who oversaw updates until his [departure
from Xinuos](https://groups.google.com/g/generic-abi/c/IakWYdGABjQ) in 2015. **The generic ABI (including the ELF
specification) then became unmaintained**.

The final functional update on <https://www.sco.com/developers/gabi/latest/contents.html>
was made in June 2013 [for
`SHF_COMPRESSED`](https://groups.google.com/g/generic-abi/c/9CUHDfWYeu4). Since then, the specification has
remained frozen.

### "All rights reserved"?

The copyright notices on the SCO website's documentation for the
System V ABI seem potentially misleading.

The footnotes of <https://www.sco.com/developers/gabi/1998-04-29/contents.html>
pages today (and in 2003 per web.archive.org) specify:

> Â© 1997, 1998, 1998 The Santa Cruz Operation, Inc. All rights
> reserved.

The footnotes of <https://www.sco.com/developers/gabi/latest/contents.html>
pages specify:

> Â© 1997, 1998, 1999, 2000, 2001 The Santa Cruz Operation, Inc. All
> rights reserved. Â© 2002 Caldera International. All rights reserved. Â©
> 2003-2010 The SCO Group. All rights reserved. Â© 2011-2015 Xinuos Inc.
> All rights reserved.

The repeated phrase "All rights reserved" could be interpreted as
implying exclusive ownership over the ELF format itself. This is
inaccurate, as ELF is an open standard developed through the
collaboration of many organizations and individuals. The Santa Cruz
Operation's role in the evolution of the System V ABI seems to have been
more of an editor than an innovator. After The Santa Cruz Operation sold
its Unix assets in 2001, the specification has largely stayed unchanged
with occasional constant updates.

The earliest available snapshot on the Wayback Machine dates back to
2003, a time when The SCO Group had assumed ownership and initiated a
lawsuit against IBM, alleging that the success of Linux was due to the
misappropriation of SCO's technology. Regrettably, earlier snapshots are
unavailable to provide a more complete historical context.

*Tool Interface Standard (TIS) Portable Formats Specification,
version 1.2* effectively [put
the specification in the public domain](http://www.groklaw.net/article.php?story=20040722135616439):

> The TIS Committee grants you a non-exclusive, worldwide, royalty-free
> license to use the information disclosed in this Specification to make
> your software TIS-compliant; no other license, express or implied, is
> granted or intended hereby.

Further reading:

* [The SCO lawsuit, 20 years
  later](https://lwn.net/Articles/924577/)
* [A Tall
  Tale About ELF - by Frank Sorenson, Dr Stupid and PJ](http://www.groklaw.net/article.php?story=20040722135616...