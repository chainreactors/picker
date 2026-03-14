---
title: Ivanti EPMM ‘Sleeper Shells’ not so sleepy?
url: https://blog.nviso.eu/2026/03/13/ivanti-epmm-sleeper-shells-not-so-sleepy/
source: NVISO Labs
date: 2026-03-13
fetch_date: 2026-03-14T04:12:10.871098
---

# Ivanti EPMM ‘Sleeper Shells’ not so sleepy?

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# Ivanti EPMM ‘Sleeper Shells’ not so sleepy?

[Olaf Schwarz](https://blog.nviso.eu/author/olaf-schwarz/ "Posts by Olaf Schwarz")

[Blue Team](https://blog.nviso.eu/category/blue-team/), [Incident Response](https://blog.nviso.eu/category/incident-response/), [Forensics](https://blog.nviso.eu/category/forensics/)

March 13, 2026March 13, 2026
5 Minutes

In late January 2026 an [advisory](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Endpoint-Manager-Mobile-EPMM-CVE-2026-1281-CVE-2026-1340?language=en_US) covering two remote code execution vulnerabilities (CVE-2026-1281 & CVE-2026-1340) in **Ivanti Endpoint Manager Mobile** (EPMM) was published. Shortly after reports (in example by [tenable](https://www.tenable.com/blog/cve-2026-1281-cve-2026-1340-ivanti-endpoint-manager-mobile-epmm-zero-day-vulnerabilities)) mentioned publicly available proof-of-concept exploits.

On 09th February 2026, Defused published a [blog post](https://defusedcyber.com/ivanti-epmm-sleeper-shells-403jsp) mentioning a specific webshell being deployed on EPMM devices via this vulnerability. In essence, they reported that exploits result in deployment of a dormant in-memory Java class loader at the location `/mifs/403.jsp`, starting with 04th February 2026. While this webshell has the capability to receive a Java class with the parameter `k0f53cf964d387`,  they have not observed any dynamic command being executed via this webshell. Based on this, they also referenced these as *Sleeper Shells* and the *403.jsp campaign*. We will also use these terms in this post to reference the same activities.

In a recent incident that [NVISO CSIRT](https://www.nviso.eu/contact-us) handled, we came across a compromised Ivanti EPMM device, and the logs quickly revealed that the aforementioned vulnerabilities were used to compromise the device. From the log entries we quickly identified what we believe is the same webshell Defused was reporting about.

We had the file `/mifs/403.jsp` written to the file system. We found requests for that `/mifs/403.jsp` file, including a base64 encoded parameter `k`. We had the same requests including the parameter `k0f53cf964d387`, just followed by two characters – leading to no dynamic code execution. Except for the fact that the requests we observed started already on 03rd February 2026, pretty much what was described in the Defused blog post.

When we were pivoting from the combination of `/mifs/403.jsp` and the presence of the *k* parameter (`/mifs/403.jsp?k=…`), we found requests not containing the `k0f53cf964d387` parameter, leading us to the conclusion that this campaign was perhaps a bit more active than we have read in the Defused blog post.

A few dates and numbers first:

* We have seen approximately 140 requests for `/mifs/403.jsp?k=…&k0f53cf964d387=..` between 03rd February 2026 and 11th February 2026.
* We have seen close to 30 requests for `/mifs/403.jsp?k=…` **NOT** including the `k0f53cf964d387` parameter on two days within the timeframe of 03rd February 2026 to 11th February 2026.
* For these *k-only* requests, the `k` parameter was carrying four different base64 encoded payloads. These four payloads typically formed a block of four consecutive requests, showing up seven times in the logs. Only one occurrence had a `/mifs/403.jsp?k=…&k0f53cf964d387=..` request in between.

Looking at the *k-only* related payloads. All four of them are sent url- and base64 encoded. If we write them to a file and remove the two encodings, we end up with a standard Java class file. To gain the plain Java code, we need to take a Java decompiler – we used [cfr](https://github.com/leibnitz27/cfr) , ran our class file through it and we can investigate the Java code.

Decompiling all four payloads/Java classes showed that they serve the same purpose and have the same structure. In short: When invoked, the class retrieves the servlet request/response from whatever object it’s given, runs a hardcoded command as a separate process via the `exec(String[] cmdarray)` method of `java.lang.Runtime`, the hardcoded command is stored in the String Array called `var9`  and returns any output in the HTTP response. The content of the String Array `var9` is also the only difference in the decompiled code.

Observed commands stored in `public String[] var9`:

```
new String[]{"/bin/sh", "-c", "/usr/bin/env /bin/sh -p -c 'mysqldump --databases mifs --tables mi_user mifs_ldap_users mifs_ldap_server_config > /mi/tomcat/webapps/mifs/css/mibasecss.css'"};
new String[]{"/bin/sh", "-c", "/usr/bin/env /bin/sh -p -c 'tar -czvf /mi/tomcat/webapps/mifs/css/mibasecss3.css /mi/tomcat-properties'"};
new String[]{"/bin/sh", "-c", "/usr/bin/env /bin/sh -p -c 'tar -czvf /mi/tomcat/webapps/mifs/css/mibasecss2.css /mi/files/system'"};
new String[]{"/bin/sh", "-c", "/usr/bin/env /bin/sh -p -c 'rm -f /mi/tomcat/webapps/mifs/css/mibasecss*'"};
```

```
new String[]{"/bin/sh", "-c", "/usr/bin/env /bin/sh -p -c 'mysqldump --databases mifs --tables mi_user mifs_ldap_users mifs_ldap_server_config > /mi/tomcat/webapps/mifs/css/mibasecss.css'"};
new String[]{"/bin/sh", "-c", "/usr/bin/env /bin/sh -p -c 'tar -czvf /mi/tomcat/webapps/mifs/css/mibasecss3.css /mi/tomcat-properties'"};
new String[]{"/bin/sh", "-c", "/usr/bin/env /bin/sh -p -c 'tar -czvf /mi/tomcat/webapps/mifs/css/mibasecss2.css /mi/files/system'"};
new String[]{"/bin/sh", "-c", "/usr/bin/env /bin/sh -p -c 'rm -f /mi/tomcat/webapps/mifs/css/mibasecss*'"};
```

Java

The first command tries to create a database dump of the database `mifs` and write it to `/mi/tomcat/webapps/mifs/css/mibasecss.css`. It utilizes the tool *mysqldump* and limits the output to include the tables `mi_user`, `mifs_ldap_users` and `mifs_ldap_server_config`.

The second and third commands use the tool *tar* to create archives of two locations on the file system: `/mi/tomcat-properties` and `/mi/files/system`. The archives are stored as `/mi/tomcat/webapps/mifs/css/mibasecss3.css` and `/mi/tomcat/webapps/mifs/css/mibasecss2.css`.

The last command serves as a cleanup command, deleting every file matching the given glob: `/mi/tomcat/webapps/mifs/css/mibasecss*`.

The observed sequence of commands was always from 1 to 4, as shown in the above listing. So the first command observed in all seven blocks is the command to achieve a database dump, followed by the two archive-c...