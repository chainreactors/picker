---
title: Migrating comments to giscus
url: https://maskray.me/blog/2025-02-17-migrating-comments-to-giscus
source: MaskRay
date: 2025-02-18
fetch_date: 2025-10-06T20:36:39.073628
---

# Migrating comments to giscus

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2025-02-17](/blog/2025-02-17-migrating-comments-to-giscus)

# Migrating comments to giscus

Followed this guide: <https://www.patrickthurmond.com/blog/2023/12/11/commenting-is-available-now-thanks-to-giscus>

Add the following to `layout/_partial/article.ejs`

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` <% if (!index && post.comments) { %> <section class="giscus"></section> <script src="https://giscus.app/client.js"  data-repo="MaskRay/maskray.me"  data-repo-id="FILL IT UP"  data-category="Blog Post Comments"  data-category-id="FILL IT UP"  data-mapping="pathname"  data-strict="0"  data-reactions-enabled="1"  data-emit-metadata="0"  data-input-position="bottom"  data-theme="preferred_color_scheme"  data-lang="en"  data-loading="lazy"  crossorigin="anonymous"  async> </script> <% } %> ``` |

Unfortunately comments from Disqus have not been migrated yet. If
you've left comments in the past, thank you. Apologies they are now
gone.

While you can create Github Discussions via GraphQL API, I haven't
found a solution that works out of the box. <https://www.davidangulo.xyz/posts/dirty-ruby-script-to-migrate-comments-from-disqus-to-giscus/>
provides a Ruby solution, which is promising but no longer works.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` Failed to define value method for :name, because EnterpriseOrderField already responds to that method. Use `value_method:` to override the method name or `value_method: false` to disable Enum value me thod generation. Failed to define value method for :name, because EnvironmentOrderField already responds to that method. Use `value_method:` to override the method name or `value_method: false` to disable Enum value m ethod generation. Failed to define value method for :name, because LabelOrderField already responds to that method. Use `value_method:` to override the method name or `value_method: false` to disable Enum value method generation. ... .local/share/gem/ruby/3.3.0/gems/graphql-client-0.25.0/lib/graphql/client.rb:338:in `query': wrong number of arguments (given 2, expected 1) (ArgumentError)         from g.rb:42:in `create_discussion' ``` |

Share

* [website](/blog/tags/website/)

[**Newer**

Compiling C++ with the Clang API](/blog/2025-03-09-compiling-c%2B%2B-with-clang-api)
[**Older**

lld 20 ELF changes](/blog/2025-02-02-lld-20-elf-changes)

### Popular

### Tag Cloud

[adc](/blog/tags/adc/) [ai9](/blog/tags/ai9/) [algorithm](/blog/tags/algorithm/) [arm](/blog/tags/arm/) [asc](/blog/tags/asc/) [assebmly](/blog/tags/assebmly/) [assembler](/blog/tags/assembler/) [automaton](/blog/tags/automaton/) [awesome](/blog/tags/awesome/) [bctf](/blog/tags/bctf/) [binary](/blog/tags/binary/) [binutils](/blog/tags/binutils/) [bmc](/blog/tags/bmc/) [build system](/blog/tags/build-system/) [c](/blog/tags/c/) [c++](/blog/tags/c/) [ccls](/blog/tags/ccls/) [cgc](/blog/tags/cgc/) [chroot](/blog/tags/chroot/) [clang](/blog/tags/clang/) [clang-format](/blog/tags/clang-format/) [codinsanity](/blog/tags/codinsanity/) [coffee script](/blog/tags/coffee-script/) [compiler](/blog/tags/compiler/) [compression](/blog/tags/compression/) [computer security](/blog/tags/computer-security/) [contest](/blog/tags/contest/) [cpp](/blog/tags/cpp/) [csv](/blog/tags/csv/) [ctf](/blog/tags/ctf/) [data structure](/blog/tags/data-structure/) [debug](/blog/tags/debug/) [defcon](/blog/tags/defcon/) [desktop](/blog/tags/desktop/) [docker](/blog/tags/docker/) [elf](/blog/tags/elf/) [emacs](/blog/tags/emacs/) [email](/blog/tags/email/) [emoji](/blog/tags/emoji/) [emscripten](/blog/tags/emscripten/) [event](/blog/tags/event/) [expect](/blog/tags/expect/) [ext4](/blog/tags/ext4/) [fdpic](/blog/tags/fdpic/) [feeds](/blog/tags/feeds/) [firmware](/blog/tags/firmware/) [floating point](/blog/tags/floating-point/) [forensics](/blog/tags/forensics/) [fp](/blog/tags/fp/) [freebsd](/blog/tags/freebsd/) [game](/blog/tags/game/) [gcc](/blog/tags/gcc/) [gdb](/blog/tags/gdb/) [gentoo](/blog/tags/gentoo/) [github](/blog/tags/github/) [glibc](/blog/tags/glibc/) [graph](/blog/tags/graph/) [graph drawing](/blog/tags/graph-drawing/) [gtk](/blog/tags/gtk/) [hacker culture](/blog/tags/hacker-culture/) [hackerrank](/blog/tags/hackerrank/) [hanoi](/blog/tags/hanoi/) [haskell](/blog/tags/haskell/) [hpc](/blog/tags/hpc/) [image](/blog/tags/image/) [inotify](/blog/tags/inotify/) [ipsec](/blog/tags/ipsec/) [irc](/blog/tags/irc/) [isc](/blog/tags/isc/) [j](/blog/tags/j/) [javascript](/blog/tags/javascript/) [josephus problem](/blog/tags/josephus-problem/) [jq](/blog/tags/jq/) [kernel](/blog/tags/kernel/) [kythe](/blog/tags/kythe/) [ld](/blog/tags/ld/) [leetcode](/blog/tags/leetcode/) [libunwind](/blog/tags/libunwind/) [linker](/blog/tags/linker/) [linux](/blog/tags/linux/) [lld](/blog/tags/lld/) [lldb](/blog/tags/lldb/) [llvm](/blog/tags/llvm/) [lsp](/blog/tags/lsp/) [m68k](/blog/tags/m68k/) [makefile](/blog/tags/makefile/) [math](/blog/tags/math/) [maze](/blog/tags/maze/) [mirror](/blog/tags/mirror/) [ml](/blog/tags/ml/) [musl](/blog/tags/musl/) [mutt](/blog/tags/mutt/) [n-body](/blog/tags/n-body/) [neovim](/blog/tags/neovim/) [network](/blog/tags/network/) [nginx](/blog/tags/nginx/) [nim](/blog/tags/nim/) [nlp](/blog/tags/nlp/) [node.js](/blog/tags/node-js/) [noip](/blog/tags/noip/) [notmuch](/blog/tags/notmuch/) [npm](/blog/tags/npm/) [ocaml](/blog/tags/ocaml/) [offlineimap](/blog/tags/offlineimap/) [oi](/blog/tags/oi/) [oj](/blog/tags/oj/) [openwrt](/blog/tags/openwrt/) [parallel](/blog/tags/parallel/) [parser generator](/blog/tags/parser-generator/) [perl](/blog/tags/perl/) [powerpc](/blog/tags/powerpc/) [presentation](/blog/tags/presentation/) [puzzle](/blog/tags/puzzle/) [python](/blog/tags/python/) [qq](/blog/tags/qq/) [radare2](/blog/tags/radare2/) [regex](/blog/tags/regex/) [regular expression](/blog/tags/regular-expression/) [reverse engineering](/blog/tags/reverse-engineering/) [review](/blog/tags/review/) [riscv](/blog/tags/riscv/) [router](/blog/tags/router/) [rtld](/blog/tags/rtld/) [ruby](/blog/tags/ruby/) [ructfe](/blog/tags/ructfe/) [s390x](/blog/tags/s390x/) [sanitizer](/blog/tags/sanitizer/) [scheme](/blog/tags/scheme/) [search](/blog/tags/search/) [security](/blog/tags/security/) [sframe](/blog/tags/sframe/) [shell](/blog/tags/shell/) [ssh](/blog/tags/ssh/) [stringology](/blog/tags/stringology/) [student festival puzzle](/blog/tags/student-festival-puzzle/) [suffix array](/blog/tags/suffix-array/) [suffix automaton](/blog/tags/suffix-automaton/) [summary](/blog/tags/summary/) [suricata](/blog/tags/suricata/) [telegram](/blog/tags/telegram/) [telegramircd](/blog/tags/telegramircd/) [terminal](/blog/tags/terminal/) [tls](/blog/tags/tls/) [traversal](/blog/tags/traversal/) [tree](/blog/tags/tree/) [trendmicro](/blog/tags/trendmicro/) [udev](/blog/tags/udev/) [unicode](/blog/tags/unicode/) [unix](/blog/tags/unix/) [usb](/blog/tags/usb/) [vim](/blog/tags/vim/) [vpn](/blog/tags/vpn/) [vte](/blog/tags/vte/) [wargame](/blog/tags/wargame/) [web analytics](/blog/tags/web-analytics/) [webqqircd](/blog/tags/webqqircd/) [website](/blog/tags/website/) [wechat](/blog/tags/wechat/) [wechatircd](/blog/tags/wechatircd/) [window manager](/blog/tags/window-manager/) [windows](/blog/tags/windows/) [x86](/blog/tags/x86/) [xbindkeys](/blog/tags/xbindkeys/) [xmonad](/blog/tags/xmonad/) [xz](/blog/tags/xz/) [yanshi](/blog/tags/yanshi/)

### Blogroll

* [BYVoid](https://byvoid.com)
* [fqj1994](https://fqj.me)
* [ppwwyyxx](http://ppwwyyxx.com)

© 2025 MaskRay
Powered by [Hexo](https://hexo.io/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)