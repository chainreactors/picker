---
title: Evidence of Execution SRUM Forensics
url: https://digitalinvestigator.blogspot.com/2026/06/evidence-of-execution-srum-forensics.html
source: Instapaper: Unread
date: 2026-06-18
fetch_date: 2026-06-19T07:09:21.871930
---

# Evidence of Execution SRUM Forensics

### Facebook SDK

* [Home](/)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[![Digital Investigator](https://blogger.googleusercontent.com/img/a/AVvXsEjCBXDAFtj3qeFsN0QARpauoOMU-9GGRJMhzK1L_edHwLn3gTy8NtKHApKnUjkKdWPgAEIcdSrosxULEGvjMszmWVhop1V0aiHOOEW8KeeKjSkfEk3bSEuXPRbuGgVQQJlHbfKNju9pNpyZOabgh-Oci700smDybZA3gHWWI5H2Mgy0h08GrB5-FiyV=s150)](https://digitalinvestigator.blogspot.com/)

* [Home](home-icon)
* [whoami](https://digitalinvestigator.blogspot.com/p/trainingswebinars-attended.html?m=1)
* [Subscribe](https://blogspot.us14.list-manage.com/subscribe?u=f0561841d9ef7ca0687144c59&id=93ea8a701f)

[Home](https://digitalinvestigator.blogspot.com/)[Windows Forensics](https://digitalinvestigator.blogspot.com/search/label/Windows%20Forensics)

# Evidence of Execution: SRUM Forensics

Joseph Moronwi
June 15, 2026
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisdxPduXS_TGiuErirWJysnlodINTGvR9pI4nkxRvhrcUlS58fLBbM5YfHxsFr7lZp_u-mOzOomk-afsEjb6hLuozSzgjZu6yDZKIc6fKv6YuS-AR7a2JJEa2-y4MUxN1KCobZZfRzoPMsaBjFRnWhqHg1WcYIDuIl_7mwqd73VXMSxQoa7yvxoyLFT2A/w640-h343/5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEisdxPduXS_TGiuErirWJysnlodINTGvR9pI4nkxRvhrcUlS58fLBbM5YfHxsFr7lZp_u-mOzOomk-afsEjb6hLuozSzgjZu6yDZKIc6fKv6YuS-AR7a2JJEa2-y4MUxN1KCobZZfRzoPMsaBjFRnWhqHg1WcYIDuIl_7mwqd73VXMSxQoa7yvxoyLFT2A/s592/5.png)

In contemporary high-profile investigations, digital evidence frequently constitutes the cornerstone of prosecutorial narratives, underscoring its probative value in establishing criminal culpability. Consequently, digital forensic examiners routinely encounter sophisticated counter-forensic techniques designed to obliterate traces of illicit activity. Among the resilient evidentiary artifacts that persist despite such efforts is the System Resource Usage Monitor (SRUM), a Windows-native telemetry repository that continues to chronicle user and application behavior long after the execution or removal of counter-forensic tools.

For instance, during the analysis of a suspected corporate network breach involving data exfiltration, forensic examination of SRUM records can enable analysts to identify applications executing on compromised hosts that systematically transferred sensitive information to external competitors or nation-state actors. SRUM’s Application Resource Usage and Network Usage tables provide granular attribution by correlating process execution, resource consumption, and network telemetry on an hourly basis, often revealing covert command-and-control or exfiltration activity that evades conventional logging mechanisms.

SRUM data proves equally indispensable in insider threat investigations. Consider the scenario of an employee surreptitiously transferring substantial volumes of proprietary data from the corporate environment to a personal laptop prior to leaving the company. Forensic review of the SRUM database would typically document elevated network receive activity associated with explorer.exe (or similar processes) under the subject user’s Security Identifier (SID). Subsequent analysis could further corroborate the employee’s connection to an external wireless network—such as a public access point at a coffee shop—by recording connection metadata including SSID, interface details, connection duration, timestamps, and the volume of bytes transmitted and received by applications (e.g., web browsers or synchronization clients accessing Dropbox or equivalent cloud storage). This facilitates precise temporal reconstruction and geolocation inference of the data movement.

In one documented forensic engagement involving a seized workstation that remained powered on post-acquisition, examiners leveraged SRUM artifacts to decisively rebut defense assertions of post-seizure tampering. The defense expert alleged that investigative personnel had authenticated to the system using the suspect’s credentials and planted inculpatory evidence. However, SRUM’s comprehensive logging of system uptime, application launches, associated user SIDs, and execution contexts demonstrated that no interactive logons or user-initiated processes had occurred following lawful seizure. This evidentiary timeline provided irrefutable corroboration that the system had not been tampered with by unauthorized actors, thereby validating the integrity of the acquired digital evidence.

SRUM’s evidentiary strength lies in its aggregation of persistent, tamper-resistant records within the SRUDB.dat database, making it an essential component of modern Windows forensic toolkits when traditional artifacts have been compromised or deleted. When properly parsed and contextualized with corroborative sources (e.g., Prefetch, ShimCache, and event logs), SRUM significantly enhances attribution, timeline reconstruction, and counter-forensic resistance in both criminal and civil matters.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGa0s1W6tSvaFJVQrJJmg_ZTcTtjBZxMs8CkimaBVTNULCRFqfgGMdPbkcAb8uFHTcbisQSACFs1ZbBt0LBqfSltm8-tYH3PUDHPMTezV9fnZYwNRYlmeIADBkbyEgbtWel65igSAxqw2Z26Cwo5MRBSXjuyu7pBdW7l3t-5gjXOfMWxxNNAMn1CiGfh0/w648-h522/1-1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhGa0s1W6tSvaFJVQrJJmg_ZTcTtjBZxMs8CkimaBVTNULCRFqfgGMdPbkcAb8uFHTcbisQSACFs1ZbBt0LBqfSltm8-tYH3PUDHPMTezV9fnZYwNRYlmeIADBkbyEgbtWel65igSAxqw2Z26Cwo5MRBSXjuyu7pBdW7l3t-5gjXOfMWxxNNAMn1CiGfh0/s827/1-1.png)

The System Resource Usage Monitor (SRUM) operates as a core component of the Windows [**Diagnostic Policy Service (DPS)**](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc774639%28v%3Dws.10%29?redirectedfrom=MSDN), systematically tracking a broad spectrum of system performance metrics, application execution, and resource utilization. Native to Windows 8 and all subsequent versions—including Enterprise editions—SRUM is enabled by default upon system initialization and maintains persistent telemetry independent of user-visible configurations.

Before 2015, SRUM remained largely unrecognized within the broader digital forensics community. Its forensic significance was formally introduced in February 2015 through the seminal research paper “[**Forensic Implications of System Resource Usage Monitor (SRUM) Data in Windows 8**](https://www.sciencedirect.com/science/article/abs/pii/S1742287615000031)” authored by Yogesh Khatri, Assistant Professor at Champlain College. The paper was [**presented at the SANS 2015 DFIR Summit**](https://www.youtube.com/watch?v=l6-83WU95Sw), followed by a [**detailed interview with Khatri on the CyberSpeak podcast**](https://cyberspeak.libsyn.com/cyberspeak-aug-31-2015-srum) in August 2015, which significantly elevated awareness of SRUM’s evidentiary value among practitioners.

End users may observe a limited subset of SRUM data through the Task Manager interface, specifically under the **App history** and **Details** tabs. The Task Manager aggregates selected records from the underlying SRUM database (SRUDB.dat), presenting both real-time performance statistics and approximately 30 days of historical usage information within the App history view.

Notably, while the App history tab includes a “Delete usage history” option, empirical forensic testing demonstrates that this function does not immediately purge records from the SRUM database. This residual persistence further enhances SRUM’s utility as a counter-forensic-resistant artifact, as user-initiated cleanup attempts frequently prove incomplete or delayed in their effect on the underlying telemetry.

The SRUM database constitutes a rich repository of forensic artifacts, yielding critical telemetry that frequently proves indispensable during digital investigations. Among its most probative elements are detailed records of wireless and wired network affiliations (i...