---
title: Linker I/O tricks and their downsides
url: https://maskray.me/blog/linker-io-tricks-and-their-downsides
source: MaskRay
date: 2026-09-20
fetch_date: 2026-09-21T07:26:11.642240
---

# Linker I/O tricks and their downsides

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2026-09-20](/blog/linker-io-tricks-and-their-downsides)

# Linker I/O tricks and their downsides

mold and wild enable several tricks by default that other linkers
don't do. This post looks at three of them:

* overwrite an existing output file in place instead of creating a new
  file
* fork a child to do the link, so that the parent can exit before the
  child releases its memory
* ask the kernel for transparent huge pages

Each saves a few percent of wall time in an edit-relink loop. Each
also breaks an assumption that build systems, debuggers, and profilers
make about a process. I measured what they save and what they break.

Setup: Linux 6.18, i7-14700K (28 threads), ext4 on a SATA SSD,
transparent huge pages `enabled=always`. GNU ld 2.47, gold
2.47, LLD 23, mold 2.42.1 (TODO: I used the Rust port under development;
check against the C++ release), wild at commit 47cc8e8e.

## Overwrite the output file in place

### History

In 2006, Ali Bahrami wrote [Settling
An Old Score (Linker Division)](https://www.linker-aliens.org/blogs/ali/entry/settling_an_old_score_linker/). The Solaris linker truncated and
rewrote an existing output file in place. It killed any running process
that had the old file mapped, with a SIGSEGV or SIGBUS far from the real
cause. Linux and macOS linkers unlinked the old file and created a new
one. Bahrami filed PSARC 2006/353 to switch Solaris to
unlink-then-create.

GNU ld, gold, and lld still work this way. A successful relink
creates a new inode and leaves other hard links alone. A failed relink
removes the output and leaves other hard links alone. lld unlinks the
old file first (`unlinkAsync`: open it, unlink it, close the
descriptor on another thread so that freeing its blocks is off the
critical path), mmaps a temporary file
`<out>.tmp%%%%%%%` in the same directory, and renames
it over the output on success.

### mold

mold went back to in-place overwriting almost from the start. Its
November 2020 history has commits trying `O_TRUNC` and
`O_DIRECT`; after them the output is opened without
`O_TRUNC`. [Commit
8a415515](https://github.com/rui314/mold/commit/8a41551562e58c18af664fff5a48531d1a36941e) (2020-12-23, "Handle ETXTBSY") added the current scheme,
released in v0.1:

* rename the existing output to
  `.<name>.<pid>`
* open it read-write without `O_TRUNC`,
  `ftruncate` to the new size, `fallocate`, mmap,
  write
* rename it back at the end
* if the open fails with `ETXTBSY` (the file is being
  executed), unlink the renamed original and create a new file

If the link fails after the output is opened (a relocation out of
range, a disk-full SIGBUS), the cleanup handler unlinks the temporary
file. On this path the temporary file is the original inode.

[Issue #188](https://github.com/rui314/mold/issues/188)
(2021-12) asked for create-and-rename. The fix in v1.3.0 (2022-05) only
disabled overwriting for `-shared`. The comment explains
why:

> By default, mold tries to ovewrite to an output file if exists
> because at least on Linux, writing to an existing file is much faster
> than creating a fresh file and writing to it. However, if an existing
> file is in use, writing to it will mess up processes that are executing
> that file. Linux prevents a write to a running executable file; it
> returns ETXTBSY on open(2). However, that mechanism doesn't protect .so
> files. Therefore, we want to disable this optimization if we are
> creating a shared object file.

Then the kernel changed. Linux 6.11 stopped denying writes to running
executables ([commit
2a010c412853](https://git.kernel.org/torvalds/c/2a010c41285345da60cece35575b4e0af7e7bf44), "fs: don't block i\_writecount during exec"). Its
message says: "Yes, someone in userspace could potentially be relying on
this. It's not completely out of the realm of possibility but let's find
out if that's actually the case and not guess."

In October 2024, [issue #1361](https://github.com/rui314/mold/issues/1361)
reported that ninja's bootstrap segfaulted on Gentoo with mold 2.34.1.
The stage-1 ninja was running while the stage-2 link rewrote its inode.
This is Bahrami's scenario. It took a week and an `rr`
recording to find. mold 2.35.0 disabled the reuse on 6.11 and later. Rui
Ueyama reported the regression to LKML. Christian Brauner asked on the
mold issue whether mold could keep its workaround so that the kernel
could keep the change, "as this was done for the sake of new work and
because the mechanism is really broken", then reverted it for 6.13 ([commit
3b832035387f](https://git.kernel.org/torvalds/c/3b832035387ff508fdcf0fba66701afc78f79e3d), Cc stable): "It seems we found out that someone is
relying on this obscure behavior. So revert the change." mold 2.36.0
re-enabled the reuse on 6.13 and later. 6.11 and 6.12 stay excluded: the
revert was backported, but distribution kernels can't be told apart by
version number.

I commented on the issue that this feels like an instance of Hyrum's
Law. A few years earlier I had insisted that llvm-objcopy emulate
`cp`'s overwrite behavior, before I realized the merit of
atomic rename.

### wild

wild added `--update-in-place` in [January
2025](https://github.com/davidlattimore/wild/commit/0a66760eded961d23c50be4076ed5ddacb567f69): "On one benchmark (rustc without debug) this gave about a 4%
speedup. On another (clang with debug) the difference was small enough
that it was hard to measure." It became the default on Linux in [November
2025](https://github.com/davidlattimore/wild/commit/11c291f5e47d073a86fd71a390c4153764bccf06), with `--no-update-in-place` added [a
month later](https://github.com/davidlattimore/wild/commit/61a6a38543e3e10125a2ee634868bdd6dbf24703). wild opens the output path itself without truncation,
falls back to unlink-and-replace on `ETXTBSY`, and always
unlinks for shared objects and on macOS (the code signature cache is
keyed by inode). Neither mold nor wild checks `st_nlink`.

### Hard links

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` printf '.globl _start\n_start: movl $_start, %%eax; jmp _start\n' | as -o a.o - mold -o a.out a.o; ln a.out b.out ls -li a.out b.out   # 47594364 nlink=2, both names mold -o a.out a.o ls -li a.out b.out   # 47594364 nlink=2: b.out was rewritten too ld.bfd -o a.out a.o ls -li a.out b.out   # a.out 47594365 nlink=1; b.out 47594364, untouched. gold and lld: same ``` |

A failed relink is worse:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` mold -o a.out a.o; ln -f a.out b.out mold -o a.out a.o --image-base=0x100000000   # error: relocation R_X86_64_32 against _start out of range ls -li a.out b.out # ls: cannot access 'a.out': No such file or directory # 47594375 -rwxr-xr-x 1 ray ray 3232 Sep 20 18:11 b.out readelf -h b.out | grep Entry               # Entry point address: 0x1000012b0 ``` |

`a.out` is gone (it was the temporary file).
`b.out` holds the half-written output of the failed link. GNU
ld, gold, and lld would have left `b.out` as the last good
binary.

Hard-linked outputs are common. Cargo hard-links
`target/debug/deps/foo-<hash>` to
`target/debug/foo`. rustc relinks
`deps/foo-<hash>` while `target/debug/foo`
still names the previous inode. So a failed relink corrupts
`target/debug/foo`, and a successful one rewrites it in
place. In my mold checkout, `target/release/mold` and
`target/release/deps/mold-75e55cc9443d1590` share one
inode.

Hard-link snapshots of a build tree are the other victims:

|  |  |
| --- | --- |
| ``` 1 2 3 4 ``` | ``` cp -al build snap-cp                           # nlink=3 rsync -a --link-dest=../build build/ snap-rsync/ mold -o build/a.out build/a.o --image-base=0x400000 cmp good snap-cp/a.out                         # differ; same for snap-rsync. ld.bfd and ld.lld: ...