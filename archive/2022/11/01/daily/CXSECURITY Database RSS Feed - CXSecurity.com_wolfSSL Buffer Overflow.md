---
title: wolfSSL Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2022100070
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-01
fetch_date: 2025-10-03T21:22:45.298989
---

# wolfSSL Buffer Overflow

[![Home Page](https://cert.cx/cxstatic/images/12018/cxseci.png)](https://cxsecurity.com/)

* [Home](https://cxsecurity.com/)
* Bugtraq
  + [Full List](https://cxsecurity.com/wlb/)
  + [Only Bugs](https://cxsecurity.com/bugs/)
  + [Only Tricks](https://cxsecurity.com/tricks/)
  + [Only Exploits](https://cxsecurity.com/exploit/)
  + [Only Dorks](https://cxsecurity.com/dorks/)
  + [Only CVE](https://cxsecurity.com/cvelist/)
  + [Only CWE](https://cxsecurity.com/cwelist/)
  + [Fake Notes](https://cxsecurity.com/bogus/)
  + [Ranking](https://cxsecurity.com/best/1/)
* CVEMAP
  + [Full List](https://cxsecurity.com/cvemap/)
  + [Show Vendors](https://cxsecurity.com/cvevendors/)
  + [Show Products](https://cxsecurity.com/cveproducts/)
  + [CWE Dictionary](https://cxsecurity.com/allcwe/)
  + [Check CVE Id](https://cxsecurity.com/cve/)
  + [Check CWE Id](https://cxsecurity.com/cwe/)
* Search
  + [Bugtraq](https://cxsecurity.com/search/)
  + [CVEMAP](https://cxsecurity.com/search/cve/)
  + [By author](https://cxsecurity.com/search/author/)
  + [CVE Id](https://cxsecurity.com/cve/)
  + [CWE Id](https://cxsecurity.com/cwe/)
  + [By vendors](https://cxsecurity.com/cvevendors/)
  + [By products](https://cxsecurity.com/cveproducts/)
* RSS
  + [Bugtraq](https://cxsecurity.com/wlb/rss/all/)
  + [CVEMAP](https://cxsecurity.com/cverss/fullmap/)
  + [CVE Products](https://cxsecurity.com/cveproducts/)
  + [Bugs](https://cxsecurity.com/wlb/rss/vulnerabilities/)
  + [Exploits](https://cxsecurity.com/wlb/rss/exploit/)
  + [Dorks](https://cxsecurity.com/wlb/rss/dorks/)
* More
  + [cIFrex](http://cifrex.org/)
  + [Facebook](https://www.facebook.com/cxsec)
  + [Twitter](https://twitter.com/cxsecurity)
  + [Donate](https://cxsecurity.com/donate/)
  + [About](https://cxsecurity.com/wlb/about/)

* [Submit](https://cxsecurity.com/wlb/add/)

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | |  | | --- | | **wolfSSL Buffer Overflow** **2022.10.31**  Credit:  **[Maximilian Ammann](https://cxsecurity.com/author/Maximilian%2BAmmann/1/)**  Risk: **High**  Local: **No**  Remote: ****Yes****  CVE: **[CVE-2022-39173](https://cxsecurity.com/cveshow/CVE-2022-39173/ "Click to see CVE-2022-39173")**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

# wolfssl before 5.5.1: CVE-2022-39173 Buffer overflow when refining
cipher suites
==================================================================================
## INFO
=======
The CVE project has assigned the id CVE-2022-39173 to this issue.
Severity: high 7.5
Affected version: before 5.5.1
End of embargo: The embargo for this vulnerability ended 29th of September, 2022
## SUMMARY
==========
In wolfSSL before 5.5.1 malicious clients can cause a buffer-overflow
during a resumed TLS 1.3 handshake. If an attacker resumes a previous
TLS session by sending a maliciously crafted Client Hello, followed by
another maliciously crafted Client Hello. In total 2 Client Hellos
have to be sent. One which pretends to resume a previous session and a
second one as a response to a Hello Retry Request message.
The malicious Client Hellos contain a list of supported cipher suites,
which contain at least `⌊sqrt(150)⌋ + 1 = 13` duplicates and less than
150 ciphers in total. The buffer-overflow occurs in the `RefineSuites`
function. An overflow of 44700 bytes has been confirmed. Therefore,
large portions of the stack can get overwritten, including return
addresses.
We confirmed the vulnerability by sending packets over TCP to a
Wolfssl server, freshly built from the sources with the
`--enable-session-ticket` flags (or simply `--enable-all`). We can
provide sources for our software (tlspuffin) that produce those
packets (and that automatically found the attack trace). The command
given at the end of this document triggers the buffer overflow.
It is very likely that there is a way to craft an exploit which can
cause a RCE. We have not yet created such an exploit as it would
likely depend on the memory layout of the binary which uses wolfSSL.
Moreover, the size of the overflow can be fine-tuned in order to not
smash the stack and continue the execution with a too large length of
suites buffer and that will cause other routines that iterate over
thus buffer (e.g., `FindSuiteSSL`) to misbehave. Hypothetically, this
might be exploited to make the server use a cipher it should not
accept such as `nullcipher` that would open up new attack vectors such
as downgrade attacks.
While this has not been confirmed yet, the buffer overflow itself has
been confirmed.
## DETAILS
==========
Line numbers below are valid for the wolfSSL Git tag
[v5.4.0-stable](https://github.com/wolfSSL/wolfssl/tree/v5.4.0-stable).
The bug we found is in the `RefineSuites` function. In the following
we want to explain why the function is able to overflow the `suites`
array.
```c
/\* Refine list of supported cipher suites to those common to server and client.
\*
\* ssl SSL/TLS object.
\* peerSuites The peer's advertised list of supported cipher suites.
\*/
static void RefineSuites(WOLFSSL\* ssl, Suites\* peerSuites)
{
byte suites[WOLFSSL\_MAX\_SUITE\_SZ];
word16 suiteSz = 0;
word16 i, j;
XMEMSET(suites, 0, WOLFSSL\_MAX\_SUITE\_SZ);
for (i = 0; i < ssl->suites->suiteSz; i += 2) {
for (j = 0; j < peerSuites->suiteSz; j += 2) {
if (ssl->suites->suites[i+0] == peerSuites->suites[j+0] &&
ssl->suites->suites[i+1] == peerSuites->suites[j+1]) {
suites[suiteSz++] = peerSuites->suites[j+0];
suites[suiteSz++] = peerSuites->suites[j+1];
}
}
}
ssl->suites->suiteSz = suiteSz;
XMEMCPY(ssl->suites->suites, &suites, sizeof(suites));
#ifdef WOLFSSL\_DEBUG\_TLS
[...]
#endif
}
```
tls13.c:4355
The `RefineSuites` function expects a `WOLFSSL` struct which contains
a list of acceptable ciphers suites (`ssl->suites->suites`), as well
as an array of peer cipher suites (`peerSuites`). Both inputs are
bounded by `WOLFSSL\_MAX\_SUITE\_SZ`, which is equal to 300 bytes or 150
cipher suites.
Let us assume that `ssl->suites` consists of a single cipher suite
like `TLS\_AES\_256\_GCM\_SHA384` and the `peerSuites` list contains the
same cipher repeated thirteen times. The `RefineSuites` function will
iterate for each element in `ssl->suites` over `peerSuites` and append
the suite to `suites` if it is a match. The `suites` array has a
maximum length of `WOLFSSL\_MAX\_SUITE\_SZ == 300 bytes == 150 suites`.
With the just mentioned example input, the length of `suites` will now
equal thirteen. The `suites` array is now copied to the `WOLFSSL`
struct in the last line of the listing above. Therefore, `ssl->suites`
contains now thirteen times the `TLS\_AES\_256\_GCM\_SHA384` cipher suite.
Let us now call the same `RefineSuites` function again on the modified
`WOLFSSL` struct and the same `peerSuites` list. The `RefineSuites`
function will iterate for each element in `ssl->suites` over
`peerSuites` and append the suite to `suites` if it is a match.
Because `ssl->suites` contains already 13 times the
`TLS\_AES\_256\_GCM\_SHA384` cipher suite, in total 13 x 13 = 169 cipher
suites are written to `suites`. 169 cipher suites require 338 bytes,
which is more than what's available on the stack. The `suites` buffer
overflows.
The maximum size of `peerSuites` is 150 cipher suites. Therefore, an
overflow of 44700 bytes is possible and has been confirmed.
The buffer `ssl->suites->suites` is supposed to be reset to only
contain the acceptable ciphers at each session start, and thus
initially contains no duplicate. However, by provoking a `HELLO CLIENT
RETRY REQUEST`, it is possible to make the server call `RefineSuites`
twice as explained next.
## TRIGGERING THE BUFFER OVERFLOW
=================================
In order to cause the above buffer-overflow, it is required to call
`RefineSuites` twice. Malicious clients need to perform the handshake
in a certain way to reach this situation.
The buffer overflow at the attacked server can be obtained at least in
the following situation:
1. Resume the previous session by sending a s...