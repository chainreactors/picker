---
title: Thomas Fitzsimmons: Lisp ELF toolkit
url: https://www.fitzsim.org/blog/?p=767
source: Planet Classpath
date: 2025-04-19
fetch_date: 2025-10-06T22:05:22.397525
---

# Thomas Fitzsimmons: Lisp ELF toolkit

[Skip to content](#content)

[fitzsim's development log](https://www.fitzsim.org/blog/)

# Lisp ELF toolkit

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1) [April 18, 2025](https://www.fitzsim.org/blog/?p=767)
[Leave a comment on Lisp ELF toolkit](https://www.fitzsim.org/blog/?p=767#respond)

I recently needed to generate an `ELF` binary with both `RPATH` and `RUNPATH` entries. I could not figure out how to produce this using linker command line arguments.

I was considering attempting a linker script, but first I switched to my `Lisp` `REPL` buffer 1 and found that `(ql:quickload "elf")` loaded a promising-looking [`Common Lisp ELF` library](https://github.com/eschulte/elf.git).

I created a stub library with `RPATH` using `gcc` and an empty `C` file, then loaded it with `(elf:read-elf)`.

With the `SLIME` inspector (`M-x slime-inspect`) I could traverse the structure of the `ELF` headers. I eventually found the `RPATH` entry.

In the `REPL` I built up a function to search for `RPATH` then `push` a new `RUNPATH` entry alongside it.

It turned out the `ELF` library had no support for the `RUNPATH` entry, so I redefined its `dyn-tag` dictionary to include it.

After adding `RUNPATH`, I wrote the modified `ELF` structures to a file using `(elf:write-elf)`. The generated `ELF` file sufficed for the test case.

I thought this was an interesting use case to share, demonstrating unique properties of the `Lisp` environment. I published [the result](https://git.sr.ht/~fitzsim/add-runpath-to-rpath-elf/tree/d74f5e2d22a55242ed9b38aa583ed2ad8e61f5ac/item/add-runpath.lisp) (I realize now I should have written `generate-example-library.sh` in `Lisp` instead of shell!; oh well).

1. Which I have been trying to keep open lately, inspired by [this post](https://funcall.blogspot.com/2025/04/why-i-program-in-lisp.html).

Posted by[Thomas Fitzsimmons](https://www.fitzsim.org/blog/?author=1)[April 18, 2025](https://www.fitzsim.org/blog/?p=767)Posted in[Lisp](https://www.fitzsim.org/blog/?cat=6)

## Post navigation

[Previous Post Previous post:
Product Idea: CRT-alike OLED driver](https://www.fitzsim.org/blog/?p=479)

## Leave a comment

### [Cancel reply](/blog/?p=767#respond)

Your email address will not be published. Required fields are marked \*

Comment \*

Name

Email

Website

Δ

This site uses Akismet to reduce spam. [Learn how your comment data is processed.](https://akismet.com/privacy/)

[About www.fitzsim.org](/about)

## Meta

* [Log in](https://www.fitzsim.org/blog/wp-login.php)
* [Entries feed](https://www.fitzsim.org/blog/?feed=rss2)
* [Comments feed](https://www.fitzsim.org/blog/?feed=comments-rss2)
* [WordPress.org](https://wordpress.org/)

[fitzsim's development log](https://www.fitzsim.org/blog/),
[Proudly powered by WordPress.](https://wordpress.org/)