---
title: Testing the Security of Modbus Services
url: https://blog.mindedsecurity.com/2024/03/testing-security-of-modbus-services.html
source: IMQ Minded Security Blog
date: 2024-03-07
fetch_date: 2025-10-06T17:08:47.004485
---

# Testing the Security of Modbus Services

[Subscribe our newsletter](https://mindedsecurity.com/newsletter)

[Minded Security](https://mindedsecurity.com)

* Industry
  + [Automotive/Maritime](https://mindedsecurity.com/industry/automotive-maritime/ "Automotive/Maritime")
  + [Financial](https://mindedsecurity.com/industry/financial/ "Financial")
  + [GDO](https://mindedsecurity.com/industry/gdo/ "GDO")
  + [Industrial Control Systems](https://mindedsecurity.com/industry/industrial-control-systems/ "Industrial Control Systems")
  + [IoT Security](https://mindedsecurity.com/industry/iot-security/ "IoT Security")
  + [Healthcare](https://mindedsecurity.com/industry/healthcare/ "Healthcare")
  + [Government](https://mindedsecurity.com/industry/government/ "Government")
* [Services](https://mindedsecurity.com/our-services/ "Services")
  + [Training](https://mindedsecurity.com/our-services/training/ "Training")
    - [Security Hackaton](https://mindedsecurity.com/services/training/security-hackaton/ "Security Hackaton")
    - [Advanced On-site Training](https://mindedsecurity.com/services/training/advanced-on-site-training/ "Advanced On-site Training")
    - [BlueClosure Training](https://mindedsecurity.com/services/training/blueclosure-training/ "BlueClosure Training")
    - [High Level Training](https://mindedsecurity.com/services/training/high-level-training/ "High Level Training")
    - [Webinar](https://mindedsecurity.com/services/training/webinar/ "Webinar")
  + [Testing](https://mindedsecurity.com/our-services/testing/ "Testing")
    - [Manual Secure Code Review](https://mindedsecurity.com/services/testing/manual-secure-code-review/ "Manual Secure Code Review")
    - [Manual WAPT](https://mindedsecurity.com/services/testing/manual-wapt/ "Manual WAPT")
    - [Cloud Security Testing](https://mindedsecurity.com/services/testing/cloud-security-testing/ "Cloud Security Testing")
    - [IoT Security](https://mindedsecurity.com/services/testing/iot-security/ "IoT Security")
    - [API Security](https://mindedsecurity.com/services/testing/api-security/ "API Security")
    - [Mobile Security Assessment](https://mindedsecurity.com/services/testing/mobile-security-assessment/ "Mobile Security Assessment")
    - [Client Side Assessment](https://mindedsecurity.com/services/testing/client-side-assessment/ "Client Side Assessment")
  + [Consulting](https://mindedsecurity.com/our-services/consulting/ "Consulting")
    - [Software Security Advisory](https://mindedsecurity.com/services/consulting/software-security-advisory/ "Software Security Advisory")
    - [5D Framework](https://mindedsecurity.com/services/consulting/5d-framework/ "5D Framework")
    - [Threat Modeling](https://mindedsecurity.com/services/consulting/threat-modeling/ "Threat Modeling")
    - [Secure Design](https://mindedsecurity.com/services/consulting/secure-design/ "Secure Design")
    - [Secure Architecture Review](https://mindedsecurity.com/services/consulting/secure-architecture-review/ "Secure Architecture Review")
    - [Secure Coding Guidelines](https://mindedsecurity.com/services/consulting/secure-coding-guidelines/ "Secure Coding Guidelines")
    - [Fixing Support](https://mindedsecurity.com/services/consulting/fixing-support/ "Fixing Support")
    - [Outsourcing Development Governance](https://mindedsecurity.com/services/consulting/outsourcing-development-governance/ "Outsourcing Development Governance")
  + [Request a brochure](https://mindedsecurity.com/request-a-brochure/ "Request a brochure")
* Resources
  + [Blog](https://blog.mindedsecurity.com/ "Blog")
  + [News](https://mindedsecurity.com/category/news/ "News")
  + [Videos](https://mindedsecurity.com/videos/ "Videos")
  + [Research](https://mindedsecurity.com/research/ "Research")
  + [Advisories](https://mindedsecurity.com/research/advisories/ "Advisories")
* [About us](https://mindedsecurity.com/our-mission/ "About us")
  + [The Company](https://mindedsecurity.com/the-company/ "The Company")
  + [Contact us](https://mindedsecurity.com/contact-us/ "Contact us")
  + [Newsletter](https://mindedsecurity.com/newsletter/ "Newsletter")
  + [Jobs](https://mindedsecurity.com/jobs/ "Jobs")
  + [Privacy Policy](https://mindedsecurity.com/privacy-policy/ "Privacy Policy")

## IMQ Minded Security Blog

[skip to main](#main)  |
[skip to sidebar](#sidebar)

## Wednesday, March 6, 2024

# Testing the Security of Modbus Services

|  |
| --- |
| [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUjtPDsHTU_40xbA4tMMARNyxJZu0USyUlzoYEpX4CYah14yXlEVLZR6z1N-Hyjiymo4za3D_cURAyM0or3FtLoEONbj-BUp3d3aJJcJxoxgoZmG2n5U93cHXZCaa0mFa0csDUlVtiOl68jsL-58f4rl2wiZCXoQRo-I059Xd76Ekjct9y6vq9JydE1i4/w299-h320/BMS_ModBus.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhUjtPDsHTU_40xbA4tMMARNyxJZu0USyUlzoYEpX4CYah14yXlEVLZR6z1N-Hyjiymo4za3D_cURAyM0or3FtLoEONbj-BUp3d3aJJcJxoxgoZmG2n5U93cHXZCaa0mFa0csDUlVtiOl68jsL-58f4rl2wiZCXoQRo-I059Xd76Ekjct9y6vq9JydE1i4/s569/BMS_ModBus.png) |
|  |

ICS and Building Management Systems (BMS) support several protocols such as
***Modbus***, *Bacnet*, *Fieldbus* and so on. Those protocols were designed to provide read/write control over sensors and actuators from a central point.

Driven by our past experience with BMS, we decided to release
our own methodology and internal tool used for proactive attack surface
analysis within systems supporting the Modbus protocol.

### The Modbus Protocol

[Modbus](https://en.wikipedia.org/wiki/Modbus) is a
well defined protocol described on
[modbus.org](https://modbus.org/specs.php). It
was created in 1979 and has become one of the most used standards for
communication between industrial electronic devices in a wide range of buses
and network.

It can be used over a variety of communication media, including serial, TCP,
UDP, etc..

The application part of the protocol is quite simple. In particular, the part
we are interested into is its Protocol Data Unit, which is independent from
the lower layer protocols, is defined as follows:

> | FUNCTION CODE | DATA |

Where *FUNCTION CODE* is a
*1 Byte size 0-127 (0x00-0x7F) value*, and *DATA* is a sequence
of bytes that changes according to the function code.

Here is a set of function codes already defined by the protocol specification:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiQLA-21SSyWWIjvhqq8WGpypkbuMO8Lk2S2jR8gcPsRaWTNu17-hP15qWqsLp_xivwrZ6LsCC7MUw9xd_VWoxbviIz-IXhnl5uikmO5rcyReEBFT_fUCS8FhdKCSc5MrdCZzNi2XHKu77uklyvKDxZ91rDsVnySjSJDn0-7EURHqQLAHg40DIXXZuQjgk=w640-h434)](https://blogger.googleusercontent.com/img/a/AVvXsEiQLA-21SSyWWIjvhqq8WGpypkbuMO8Lk2S2jR8gcPsRaWTNu17-hP15qWqsLp_xivwrZ6LsCC7MUw9xd_VWoxbviIz-IXhnl5uikmO5rcyReEBFT_fUCS8FhdKCSc5MrdCZzNi2XHKu77uklyvKDxZ91rDsVnySjSJDn0-7EURHqQLAHg40DIXXZuQjgk)

By setting a specific function code together with its expected set of data
field values, it will be possibile to read/write the status of coils, inputs
and registers, or access information about other interesting aspects such as
diagnostic data.

For example the following request, queries about the status of 2 coils starting from address 0x0033 in a remote device:

>  \x01\x01\x00\x33\x00\x02

Where:

> | \x01 [**SlaveId**] | \x01 [**Function Code**] | \x00\x33 [**Address**] | \x00\x02
> [**Quantity**] |

As it can be noticed, that is quite similar to an API based modern application, the name of the function and its arguments:

> *Protocol://URL/**EndPoint**?**Parameters**=**Values**..*

Apart from the public function codes, several codes are left as *custom
implementation* and are reserved but not defined in the standard.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjZ23-p_YeYWL_smGaf6c6V9an46z_1Ge0MA9aKlLurjF3xoXaAK427syK0rS9ZeaQ25iUo8izatZkG8YZRF4gALEmVrQgRYItHPC_Q0YtoajS8vdQGr6oD_MvYIYN5tcO1jrn9RhmmCnMgyX4Ii0l33K9BBs-CgxJ2An51det1A2Qc-lLipjKWxyoxGU8=w302-h320)](https://blogger.googleusercontent.com/img/a/AVvXsEjZ23-p_YeYWL_smGaf6c6V9an46z_1Ge0MA9aKlLurjF3xoXaAK427syK0rS9ZeaQ25iUo8izatZkG8YZRF4gALEmVrQgRYItHPC_Q0YtoajS8vdQGr...