---
title: ICSFuzz
url: https://kitploit.com/en/tools/github/momalab/icsfuzz
source: Kitploit
date: 2026-08-24
fetch_date: 2026-08-25T02:59:20.563609
---

# ICSFuzz

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

ICSFuzz — Instrumented fuzzer for PLC-based ICS control applications, targeting Codesys runtime on Wago controllers to uncover memory corruption and crash-inducing inputs. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/momalab/icsfuzz

![](https://assets.kitploit.com/production/public/tools/50866/05fffa152cf6bc0830ed828246170727c5c5538c307c8d091dc3ff5d7b10ec4a-display-v1.webp)

[Embedded Systems Security](/en/categories/embedded-systems-security)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Dynamic Code Analysis (DAST)](/en/categories/dynamic-code-analysis)[SCADA/ICS Security](/en/categories/scada-ics-security)[Fuzzing](/en/categories/fuzzing)[Penetration Testing](/en/categories/penetration-testing)[Top in SCADA/ICS Security #8](/en/categories/scada-ics-security)

![GitHub](/providers/github.png)momalab/icsfuzz

# ICSFuzz

Instrumented fuzzer for PLC-based ICS control applications, targeting Codesys runtime on Wago controllers to uncover memory corruption and crash-inducing inputs.

30104 years ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[View Repository](https://github.com/momalab/icsfuzz)

---

ICSFuzz: Fuzzing Tool for ICS Control Applications

---

# Overview

`ICSFuzz` is an PLC-side fuzzing tool for uncovering vulnerabilities in ICS control applications

by Dimitris Tychalas `\@ditihala`\_

.. \_`\@ditihala`: <https://www.twitter.com/ditihala>

# Installation

The tool requires an already existing cross compiler on your machine. Since the fuzzer runs natively on the PLC, it needs to be compiled with an ARM-based cross-toolchain, such as OSELAS. For installing such a toolchain please follow the instructions on the following link and modify the Makefile with the location of your cross-compiler.

* `OSELAS toolchain <https://pengutronix.de/en/software/toolchain.html>`\_\_

# Getting Started

The `ICSFuzz` tool is a specialized security assessment tool for evaluating ICS control applications. At this current stage, it supports only applications based on the `Codesys` platform which has been modified and adapted for the `Wago` PLC. While this tool is an ongoing effort on our side, any suggestions for upgrades and enhanced compatibility are more than welcome :) Just shoot me an email at [[email protected]](/cdn-cgi/l/email-protection#e7838e8a8e93958e94c9939e848f868b8694a7899e92c9828392)

* This tool is build as a simple application that will be run on your Wago PLC. Just run the Makefile, copy the produced `fuzzer` binary on your PLC and execute it! Since the tool is accessing and modifying arbitrary process memory, it requires admin privileges. Please make sure to execute it as a sudo or root user.
* The tool is currently compatible with Codesys 3.5, patch 02.06.20(08) and older versions, please upgrade or downgrade your PLC firmware so it can host ICSFuzz properly. For visual feedback on the fuzzing process, you may use the e!cockpit platform which is offered as a development/HMI tool for Wago PLC. Through it, you can track the fuzzing input delivered to the application as well as get informed on a potential crash, as the application will stop executing, the "run" LED will get stuck on red. Since the application will stop, the current (stuck) input is the one that caused the crash. You may restart the application through the e!cockpit and restart the fuzzer once more.
* The fuzzer has an initial hard-coded starting value (note as seed\_input in the source code) which you may modify at will as you play around with the fuzzer.

# Cite us!

If you find our work interesting and use it in your (academic or not) research, please cite our Usenix Security 2021 paper describing ICSFuzz:

Tychalas, Dimitrios, Hadjer Benkraouda, and Michail Maniatakos. "ICSFuzz: Manipulating I/Os and Repurposing Binary Code to Enable Instrumented Fuzzing in {ICS} Control Applications." 30th {USENIX} Security Symposium ({USENIX} Security 21). 2021.

# Acknowledgements

`ICSFuzz`, as all things good in life, is based on the shoulder of giants. The framework is based on the powerful `AFL` by Michal Zalewski for producing the necessary input mutations that are delivered to the ICS application.

* `AFL <https://lcamtuf.coredump.cx/afl/>`\_\_

[Download Tool](https://github.com/momalab/icsfuzz)