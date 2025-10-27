---
title: OpenSIPS Security Audit Report is fully disclosed and out there
url: https://www.rtcsec.com/post/2023/03/opensips-security-audit-report/
source: Real-time communications security on Communication Breakdown - VoIP & WebRTC Security
date: 2023-03-18
fetch_date: 2025-10-04T09:56:56.080424
---

# OpenSIPS Security Audit Report is fully disclosed and out there

[Skip to main content](#content)

[![Enable Security logo](https://www.enablesecurity.com/assets/img/logo-header-white.min.ac2c259ad95c9e369b3d7e44d9986a07c2c45fec663fbceaefe184e92011793a.svg)](/)

* [Get in touch](/contact/)

* Security Testing
  + [VoIP Penetration Testing](/voip-penetration-testing/)
  + [WebRTC Penetration Testing](/penetration-testing/)
  + [VoIP Security Assessment](/voip-security-assessment/)
  + [DDoS Resilience Testing](/ddos-testing/)
  + [Code & Config Analysis](/code-and-config-analysis/)
  + [Fuzz Testing](/fuzz-testing/)
* [SIPVicious](/sipvicious/)
* [Consultancy](/consultancy/)
* [Research](/research/)
* [Blog](/blog/)
* [Newsletter](/newsletter/)
* [About](/about/)
* [Contact](/contact/)

![Sandro Gauci](https://www.enablesecurity.com/assets/img/sandro-thumb_hubedf31446211def026ce81cb6e7c2636_36362_60x60_resize_q75_box.jpg)

[**Sandro Gauci**](#author-sandrogauci), Enable Security

# OpenSIPS Security Audit Report is fully disclosed and out there

Published on Mar 17, 2023
in
*[sip security](https://www.enablesecurity.com/tags/sip-security/)*,
*[sipvicious pro](https://www.enablesecurity.com/tags/sipvicious-pro/)*,
*[sip security testing](https://www.enablesecurity.com/tags/sip-security-testing/)*,
*[security tools](https://www.enablesecurity.com/tags/security-tools/)*,
*[opensips](https://www.enablesecurity.com/tags/opensips/)*,
*[kamailio](https://www.enablesecurity.com/tags/kamailio/)*,
*[fuzzing](https://www.enablesecurity.com/tags/fuzzing/)*,
*[denial of service](https://www.enablesecurity.com/tags/denial-of-service/)*,
*[research](https://www.enablesecurity.com/tags/research/)*

It’s almost a year since the OpenSIPS project published a minimized version of our security audit report from 2022. Now, the full version has been published, with all the information intact on how to reproduce the vulnerabilities and extra details in an 80+ page report.

The OpenSIPS security audit report can be found [here](https://github.com/EnableSecurity/reports/raw/master/opensips-security-audit/opensips-audit-technical-report-full.pdf).

[![OpenSIPS security audit report front page](opensips-security-audit-report.png)](https://github.com/EnableSecurity/reports/raw/master/opensips-security-audit/opensips-audit-technical-report-full.pdf)

## What is the OpenSIPS security audit?

OpenSIPS is a SIP server that often has a critical security function within an IP communications system. Thus, it makes absolute sense to perform a thorough security audit for such software. We had been dealing with OpenSIPS servers from time to time in our work so we were rather familiar with the software and the project itself. Then back in January 2021, the lead developer for OpenSIPS, Bogdan-Andrei Iancu, asked us if we would be interested in doing some proper security work. Naturally, our answer was *yes please*!

We planned to do the following for OpenSIPS 3.2.2:

* whitebox fuzz testing, or coverage-guided fuzzing based on libfuzzer and AFL
* blackbox fuzz testing using the [SIPVicious PRO fuzzing tool](https://docs.sipvicious.pro/stable/cui-reference/sip/fuzz/request/)
* manual code review of various security-critical functions
* basic DDoS security tests

For further background of how this happened, do watch [the presentation](https://youtu.be/JZ1hFDWlcFs?t=9530) or [slides](https://www.slideshare.net/sandrogauci/the-opensips-security-audit-opensips-summit-sandro-gauci) that we presented at the OpenSIPS Distributed Summit 2021, before starting the actual security audit.

Here’s a bit of a timeline of how things went:

* Early discussions: January 2021
* Fund raising started: June 2021
* Fund raising finished: September 2021
* Started work: September 2021
* First status report: November 2021
* Second status report: February 2022
* Minimized report delivered: March 2022
* Minimized report published: April 2022
* Full report published: March 2023

## Vulnerability findings and security fixes

As a result of this security audit, we reported the following security findings:

* Segmentation fault due to invalid `Content-Length` header (CVSS: 8.6)
* Crash when specially crafted REGISTER message is challenged for authentication (CVSS: 8.6)
* Buffer over-read in function `delete_sdp_line` leads to DoS or undefined behaviour (CVSS: 8.6)
* Buffer over-read in the function `parse_param_name` leads to DoS or undefined behaviour (CVSS: 8.6)
* Buffer over-read in the function `extract_field` leads to DoS or undefined behaviour (CVSS: 8.6)
* Buffer over-read in function `extract_rtpmap` leads to DoS or undefined behaviour (CVSS: 8.6)
* Buffer over-read in the function `extract_fmtp` leads to DoS or undefined behaviour (CVSS: 8.6)
* Off-by-one error in the function `append_hf` leads to a crash (CVSS: 8.6)
* Segmentation fault in the function `build_res_buf_from_sip_req` might lead to DoS (CVSS: 6.2)
* Segmentation fault when calling the function `calc_tag_suffix` leads to DoS (CVSS: 8.6)
* Crash in the function `t_reply_matching` may lead to DoS (Info)
* Heap-buffer-overflow in function `parse_hname2` leads to AddressSanitizer false positives (Info)
* Segmentation fault in the function `rewrite_ruri` leads to DoS (CVSS: 8.6)
* Memory leak in `parse_mi_request` might lead to Denial of Service (CVSS: 7.1)
* Buffer over-read in function `stream_process` leads to DoS (CVSS: 8.6)

This led to the following advisories from OpenSIPS’s end:

* [Memory leak in cJSON lib (CVE-2023-28096)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-2mg2-g46r-j4qr) CVSS: 4.5
* [Vulnerability 3 in the codec\_delete\_XX() functions (CVE-223-27596)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-3ghx-j39m-cw4f) CVSS: 7.5
* [Vulnerability in the Content-Length Parser (CVE-2023-28097)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-c6j5-f4h4-2xrq) CVSS: 7.5
* [Vulnerability in the ds\_is\_in\_list() function (CVE-2023-28099)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-pfm5-6vhv-3ff3) CVSS: 5.9
* [Vulnerability in the parse\_uri() function (CVE-2023-27597)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-358f-935m-7p9c) CVSS: 7.5
* [Vulnerability in the parse\_via() function (CVE-2023-27598)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-wxfg-3gwh-rhvx) CVSS: 7.5
* [Vulnerability in the parse\_to\_param() function (CVE-2023-27599)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-qvj2-vqrg-f5jx) CVSS: 7.5
* [Vulnerability 2 in the codec\_delete\_XX() functions (CVE-2023-27600)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-67w7-g4j8-3wcx) CVSS: 7.5
* [Vulnerability in the codec\_delete\_XX() functions (CVE-2023-27601)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-xj5x-g52f-548h) CVSS: 7.5
* [Vulnerability in the building the local negative replies (CVE-2023-28095)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-7pf3-24qg-8v9h) CVSS: 7.5
* [Vulnerability in the Digest Authentication Parser (CVE-2023-28098)](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-jrqg-vppj-hr2h) CVSS: 5.9

One thing to note is that while we’re using the *overall CVSS score*, the advisories use the *CVSS base score*. Another is that according to our analysis, the vulnerabilities found should only result in Denial of Service rather than arbitrary code execution.

In addition to actual vulnerabilities, we also reported two informational findings. In each case, these were results from our fuzzing exercises where further analysis gave us a strong indication that they were not exploitable. We still report these findings because fixing them allows further fuzzing to be done that might reveal actual real vulnerabilities. With the developers, we also highlighted the value of having code that is easy to fuzz using instrumented code coverage techniques such as those supported by libfuzzer.

## The actual work

Our methodology consisted of iterating between blackbox ...