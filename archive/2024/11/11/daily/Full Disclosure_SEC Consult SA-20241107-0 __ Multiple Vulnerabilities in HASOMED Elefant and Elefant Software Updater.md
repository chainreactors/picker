---
title: SEC Consult SA-20241107-0 :: Multiple Vulnerabilities in HASOMED Elefant and Elefant Software Updater
url: https://seclists.org/fulldisclosure/2024/Nov/3
source: Full Disclosure
date: 2024-11-11
fetch_date: 2025-10-06T19:16:29.975890
---

# SEC Consult SA-20241107-0 :: Multiple Vulnerabilities in HASOMED Elefant and Elefant Software Updater

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

[![Previous](/images/left-icon-16x16.png)](2)
[By Date](date.html#3)
[![Next](/images/right-icon-16x16.png)](4)

[![Previous](/images/left-icon-16x16.png)](2)
[By Thread](index.html#3)
[![Next](/images/right-icon-16x16.png)](4)

![](/shared/images/nst-icons.svg#search)

# SEC Consult SA-20241107-0 :: Multiple Vulnerabilities in HASOMED Elefant and Elefant Software Updater

---

*From*: SEC Consult Vulnerability Lab via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Fri, 8 Nov 2024 06:55:19 +0000

---

```
SEC Consult Vulnerability Lab Security Advisory < 20241107-0 >
=======================================================================
              title: Multiple Vulnerabilities
            product: HASOMED Elefant and Elefant Software Updater
 vulnerable version: <24.04.00, Elefant Software Updater <1.4.2.1811
      fixed version: 24.04.00, Elefant Software Updater 1.4.2.1811
         CVE number: CVE-2024-50588, CVE-2024-50589, CVE-2024-50590,
                     CVE-2024-50591, CVE-2024-50592, CVE-2024-50593
             impact: Critical
           homepage: https://hasomed.de/produkte/elefant/
              found: 2024-04-15
                 by: Tobias Niemann (Office Bochum)
                     Daniel Hirschberger (Office Bochum)
                     Florian Stuhlmann (Office Bochum)
                     SEC Consult Vulnerability Lab

                     An integrated part of SEC Consult, an Eviden business
                     Europe | Asia

                     https://www.sec-consult.com

=======================================================================

Vendor description:
-------------------
(Translated) "Elefant is the KBV-certified practice software from HASOMED,
specializing in the needs of psychological psychotherapists, child and
adolescent psychotherapists and medical psychotherapists. The software is ideal
for individual and group practices, private accountants, medical care centers
and training institutes in the fields of behavioral therapy, psychoanalysis,
depth psychology -based psychotherapy and systemic therapy."

Source: https://hasomed.de/produkte/elefant/

Business recommendation:
------------------------
The vendor provides a patch which should be installed immediately.

SEC Consult highly recommends to perform a thorough security review of the
product conducted by security professionals to identify and resolve potential
further security issues.

Vulnerability overview/description:
-----------------------------------
1) Unprotected Exposed Firebird Database (CVE-2024-50588)
An unauthenticated attacker with access to the local network of the medical
office can use known default credentials to gain remote DBA access to the
Elefant Firebird database. The data in the database includes patient data and
login credentials among other sensitive data. In addition, this enables
an attacker to create and overwrite arbitrary files on the server filesystem
with the rights of the Firebird database ("NT AUTHORITY\SYSTEM").

2) Unprotected FHIR API (CVE-2024-50589)
An unauthenticated attacker with access to the local network of the medical
office can query an unprotected Fast Healthcare Interoperability Resources
(FHIR) API to get access to sensitive electronic health records (EHR).

3) Local Privilege Escalation via Weak Service Binary Permissions (CVE-2024-50590)
An attacker with local access the to medical office computer can escalate his
Windows user privileges to "NT AUTHORITY\SYSTEM" by overwriting one of two
Elefant service binaries with weak permissions.

4) Local Privilege Escalation via Command Injection (CVE-2024-50591)
An attacker with local access the to medical office computer can escalate his
Windows user privileges to "NT AUTHORITY\SYSTEM" by exploiting a command
injection vulnerability in the Elefant Update Service. The command injection
can be exploited by communicating with the Elefant Update Service which is
running as "SYSTEM" via Windows Named Pipes.

5) Local Privilege Escalation via Race Condition (CVE-2024-50592)
An attacker with local access the to medical office computer can escalate his
Windows user privileges to "NT AUTHORITY\SYSTEM" by exploiting a race condition
in the Elefant Update Service during the repair or update process.

6) Hardcoded Service Password (CVE-2024-50593)
An attacker with local access to the medical office computer can access
restricted functions of the Elefant Service tool by using a hardcoded
"Hotline" password.

Proof of concept:
-----------------
1) Unprotected Exposed Firebird Database (CVE-2024-50588)
Elefant uses a Firebird DB to store data. The Firebird server listens on all
interfaces on port 3050:

<unprotected_db_1.png>

An attacker can connect directly to the database as DBA if he can reach port
3050 of the Elefant server using the known Firebird default credentials
"SYSDBA:masterkey" and specifying the Elefant database path
"C:\Elefant1\ELEFANT.gdb".

<unprotected_db_2.png>

The database contains all Elefant data including patient data and the
obfuscated Elefant login data:

<unprotected_db_3.png>

To obtain the plain login credentials each byte must be xored with 0x1b.

In addition an attacker can create and overwrite arbitrary files on the server
filesystem with the rights of the database ("NT AUTHORITY\SYSTEM") via Firebird
delta files. Depending on other running software (i.e. MS IIS) RCE can be
achieved this way by uploading a webshell.

The weak default credentials are hardcoded into Elefant and Elefant Service.

2) Unprotected FHIR API (CVE-2024-50589)
While the Elefant client is running it listens on port 9090 on all interfaces.

<unprotected_api_1.png>

An unauthenticated FHIR API is exposed on this port. An attacker with access to
port 9090 can query the API for patient and physician data among other data.
The API can be queried via plain HTTP.
All patient data can for example be queried by visiting the following URL:
http://XXX.XXX.XXX.XXX:9090/Patient

The API responds with the patient data:

------------------------------------------------------------------------------
<?xml version="1.0"?>
<Bundle xmlns="http://hl7.org/fhir";>
[...]
  <type value="searchset"/>
  <timestamp value="2024-05-08T20:38:26.859+02:00"/>
  <total value="4"/>
[...]
     <Patient>
        <id value="patient.3"/>
        <meta>
          <versionId value="1"/>
          <lastUpdated value="2024-05-31T14:42:39.685+02:00"/>
          <profile value="https://fhir.kbv.de/StructureDefinition/KBV_PR_VoS_Patient|2.1.0"/>
        </meta>
        <identifier>
          <type>
            <coding>
              <system value="http://terminology.hl7.org/CodeSystem/v2-0203"/>
              <code value="MR"/>
            </coding>
          </type>
          <system value="http://hasomed.de/Elefant/Patient"/>
          <value value="3"/>
        </identifier>
        <identifier>
          <use value="official"/>
          <type>
            <coding>
              <system value="http://fhir.de/CodeSystem/identifier-type-de-basis"/>
              <code value="PKV"/>
            </coding>
          </type>
          <system value="http://fhir.de/sid/pkv/kvid-10"/>
          <value value="aaaaa"/>
        </identifier>
        <name>
          <use value="official"/>
          <text value="Dr. POC Vorname POC Nachname"/>
          <family value="POC Nachname">
            <extension url="http://hl7.org/fhir/StructureDefinition/humanname-own-name";>
              <valueString value="POC Nachname"/>
      ...