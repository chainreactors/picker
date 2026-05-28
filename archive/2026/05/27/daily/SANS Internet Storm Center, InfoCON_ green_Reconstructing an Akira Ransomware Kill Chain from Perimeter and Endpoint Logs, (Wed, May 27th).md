---
title: Reconstructing an Akira Ransomware Kill Chain from Perimeter and Endpoint Logs, (Wed, May 27th)
url: https://isc.sans.edu/diary/rss/33024
source: SANS Internet Storm Center, InfoCON: green
date: 2026-05-27
fetch_date: 2026-05-28T06:03:45.718208
---

# Reconstructing an Akira Ransomware Kill Chain from Perimeter and Endpoint Logs, (Wed, May 27th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Manuel Humberto Santander Pelaez](/handler_list.html#manuel-humberto-santander-pelaez "Manuel Humberto Santander Pelaez")

Threat Level: [green](/infocon.html)

* [previous](/diary/33018)

Click HERE to learn more about classes Manuel Humberto is teaching for SANS

# [Reconstructing an Akira Ransomware Kill Chain from Perimeter and Endpoint Logs](/forums/diary/Reconstructing%2Ban%2BAkira%2BRansomware%2BKill%2BChain%2Bfrom%2BPerimeter%2Band%2BEndpoint%2BLogs/33024/)

**Published**: 2026-05-27. **Last Updated**: 2026-05-27 21:14:03 UTC
**by** [Manuel Humberto Santander Pelaez](/handler_list.html#manuel-humberto-santander-pelaez) (Version: 1)

[0 comment(s)](/diary/Reconstructing%2Ban%2BAkira%2BRansomware%2BKill%2BChain%2Bfrom%2BPerimeter%2Band%2BEndpoint%2BLogs/33024/#comments)

Most Akira write-ups focus on the ransom note or the encryption routine. By the time those show up the interesting forensic work is over. The questions that matter to defenders sit earlier. How did they get in. When did they get domain admin. What did they touch before the binary fired. Those answers live in the days before impact. They sit in two log sources that almost never get joined. The perimeter firewall and the Windows event channel.

This diary walks through a recent Akira-attributed intrusion at a mid-sized organization. The reconstruction used only SSLVPN syslog and Windows EVTX exports. No EDR. No memory captures. Every identifier in the post has been anonymized. The event types and sequencing are preserved exactly as observed.

# **The setup**

The environment was a single-site Active Directory forest behind a perimeter NGFW. SSLVPN gave remote access to a small workforce. We started the engagement with the following sources available:

* Firewall syslog covering roughly seven days before the encryption event. Authentication, IPS and traffic categories were retained.
* EVTX exports from both domain controllers and three member servers. Channels covered were Security, System and Microsoft-Windows-PowerShell/Operational.
* The ransom note text file and a sample of encrypted files. Used only to confirm attribution.

No EDR. No PCAP. No proxy logs. This is a representative starting point for many small and mid-sized organizations. It is also why the joinable signal between the firewall and the Windows event channels matters so much.

# **Stage 1: Initial access**

The first useful signal came from the firewall authentication log. We filtered SSLVPN events for the 72 hours before the encryption event. An unambiguous brute-force pattern jumped out. It targeted a single local SSLVPN account. The customer confirmed later that the account had been disabled in Active Directory. It remained provisioned as a local firewall user.

![](https://isc.sans.edu/diaryimages/images/Imagen%201.png)

Two details from Figure 1 deserve a closer look. The brute force was not distributed. Every failure came from a single source IP in a hosting-provider range. One IPS rule or a geo-block would have stopped it. The successful authentication landed inside the ramp. There was no pause to test the credential. The attacker walked straight in once one matched. That is the behavioral fingerprint of credential stuffing against a known target.

Mapping this to the firewall vendor known SSLVPN credential exposure issue is plausible. It is not strictly provable from the logs we had. What is provable is this. The local account had no MFA. It had been deprovisioned in AD but not in the firewall. Its password survived a six-hour online attack.

# **Stages 2 and 3: Discovery and credential access**

Once on the VPN the attacker had a layer-3 path into the user VLAN. The pivot point to internal evidence was the firewall NAT log. It gave us the post-VPN source IP and the relevant time window. We joined that window against the Windows Security channel. The first internal events of interest were EID 4624 logons from the VPN-assigned IP to a jump host. The customer confirmed the jump host was used by legitimate remote administrators.

What followed was textbook discovery activity. All of it was visible in EID 4688 process creation events.

EID 4688  parent: explorer.exe   child: cmd.exe

EID 4688  parent: cmd.exe        child: nltest.exe   /dclist:

EID 4688  parent: cmd.exe        child: net.exe      group "Domain Admins" /domain

EID 4688  parent: cmd.exe        child: net.exe      group "Enterprise Admins" /domain

EID 4688  parent: cmd.exe        child: whoami.exe   /all

EID 4688  parent: cmd.exe        child: <renamed>.exe  (AdFind.exe behavior)

About 24 hours later a cluster of EID 4769 events appeared against three service accounts. All RC4-encrypted. All from the jump host. All inside a 90-second window. That combination is the signature pattern for Kerberoasting. It is also the cheapest detection any AD-joined organization can deploy.

# **Stage 4: Lateral movement**

Lateral movement spread across two days and used RDP almost exclusively. The relevant pattern is the well-known EID 4624 Logon Type 10 cluster. Successful logons originated from the jump host. Targets included the file server, both domain controllers and the backup server. EID 4672 followed each domain-controller logon. The attacker now held domain-level privilege.

Two artifacts from this phase deserve attention. The attacker created a new account in a non-default OU. They added it to a built-in group using its Well-Known SID rather than the localized group name. That is a small but reliable indicator. The operator was scripting for environment portability and not working interactively in the local language.

Several PowerShell sessions ran with the -EncodedCommand flag. Once decoded the contents showed reconnaissance against backup infrastructure and shadow-copy state. That is pre-staging for the impact stage. Worth alerting on by itself.

# **Stages 5 and 6 defense evation and impact**

The final 12 hours collapsed into a rapid sequence. The Security event log on the jump host was cleared. That is EID 1102. Several endpoint protection services were stopped using sc.exe and net stop. We saw this in System EID 7036. A vssadmin delete shadows /all /quiet ran across every reachable host. Encryption followed within minutes. Figure 2 shows the full sequence.

[![](https://isc.sans.edu/diaryimages/images/fig2(1).png)](https://isc.sans.edu/diaryimages/images/fig2%281%29.png)

The time distribution in Figure 2 matters more than the sequence. The encryption event is what the customer sees. It represents maybe five percent of the total dwell time. The other 95 percent is where defensive opportunity sits. Almost all of it was visible in logs the customer already had.

# **Why joining the sources matter**

Most defenders treat perimeter logs and endpoint event logs as two separate problems handled by two separate teams. Figure 3 shows what that separation costs. Each stage of this intrusion was visible in only one of the two sources at high confidence.

[![](https://isc.sans.edu/diaryimages/images/fig3(1).png)](https://isc.sans.edu/diaryimages/images/fig3%281%29.png)

An analyst working only the firewall syslog would have caught the brute force and the successful login. Nothing past that. An analyst working only EVTX would have seen anomalous internal behavior with no anchor for the entry point. The joined view turns two partial accounts into one full kill chain. The pivot field is source IP. The axis is normalized time.

The join itself is trivial. The expensive parts are retention and time synchronization. In this engagement the firewall retained seven days of syslog. The Windows event channels had been left at default sizes. EID 4688 had already rolled off the jump host by the time analysis started. Recovery required reaching back into a single off-host log forwarder.

# **Detection and hunting guidance**

Concrete actions any organization can im...