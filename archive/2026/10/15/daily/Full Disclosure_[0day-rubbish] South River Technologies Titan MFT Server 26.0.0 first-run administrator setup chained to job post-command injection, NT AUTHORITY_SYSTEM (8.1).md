---
title: [0day-rubbish] South River Technologies Titan MFT Server 26.0.0 first-run administrator setup chained to job post-command injection, NT AUTHORITY\SYSTEM (8.1)
url: https://seclists.org/fulldisclosure/2026/Oct/20
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:51.053570
---

# [0day-rubbish] South River Technologies Titan MFT Server 26.0.0 first-run administrator setup chained to job post-command injection, NT AUTHORITY\SYSTEM (8.1)

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

[![Previous](/images/left-icon-16x16.png)](19)
[By Date](date.html#20)
[![Next](/images/right-icon-16x16.png)](21)

[![Previous](/images/left-icon-16x16.png)](19)
[By Thread](index.html#20)
[![Next](/images/right-icon-16x16.png)](21)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] South River Technologies Titan MFT Server 26.0.0 first-run administrator setup chained to job post-command injection, NT AUTHORITY\SYSTEM (8.1)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Oct 2026 02:22:46 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability chain in South
River Technologies Titan MFT Server 26.0.0.364, the NextGen generation of the
commercial managed file transfer server from South River Technologies (Annapolis,
Maryland, United States). The product runs as a single .NET 8 process,
titanmft.exe, registered as the Windows service SrtTitanMFTServerService under
LocalSystem, serves a Blazor Server administration application on 0.0.0.0:47443
over TLS, and drives transfers with EF Core over SQLite.

Before anything else, the framing. This is a first-run window, which is a
deployment state, and it is not an absence of authentication. The window opens
when installation completes and the service starts listening, and it closes the
instant the first administrator account exists. While the administration
database's nxUserParams table holds zero rows, the login route renders an
"Initial Admin User Setup" screen to any client that can reach the listener.
Once one administrator exists, that route renders a credential form instead and
this chain's account-creation half has no route whatsoever. The product has
three authentication planes and the message-level one is closed; we measured it
closed, in the same run, at the same time the setup screen was available. What
is exposed is a state, and no configured deployment is exposed to the half that
creates the account.

Type: CWE-306, Missing Authentication for Critical Function, on the first-run
administrator-creation path, chained with CWE-78, Improper Neutralization of
Special Elements used in an OS Command, on the job post-command path.
CWE-250/CWE-269 (LocalSystem execution with no privilege separation) and
CWE-209/CWE-200 (unauthenticated stack-trace echo and window-state leak) are
named as contributing and are deliberately not folded into the score. CWE-1188
is deliberately not used: no insecure default credential ships with this
product, and implying that rotating a password closes the exposure would be
false, because creating the first administrator closes it.

The gate is a row count and nothing else. MxSvrParams.cs:518-520 evaluates
`RunWizard = !nxUserParams.AdminUserExists() && !CreateAdminAtConsole`, and the
clearest form of the same predicate is in the legacy route:

    if (!nxUserParams.AdminUserExists())
        CreateAdminUser(li.user.NxDecryptAPI(), li.pass.NxDecryptAPI());

There is no bootstrap ticket, no CAPTCHA, no first-boot token, no localhost
restriction and no channel binding. We counted zero `[Authorize]` attributes
across the 1,880 decompiled files of the ServerCore assembly, so every
authorisation decision in the product lives in application logic, and for the
setup screen that logic is the empty-table test. Submitting the screen calls
`AppState.CreateAdminUser` followed by `AppState.Login` inside the same
in-process circuit and lands the anonymous client in the management console at
`/SvrHome/<guid>/<guid>`.

The sink is the job post-command. The field labelled `Execute After File
Transfer Task` is persisted verbatim into `nxJobs.document.PostCommandText` and
is executed by the transfer engine:

    // MxUtilSvrJobHandler.cs:970-972  trigger predicate
    if (P_0.IsSuccess() || Job.ExecuteCustomPostProcessOnFileTransferTaskFailure)
        return !string.IsNullOrWhiteSpace(Job.PostCommandText);

    // MxUtilSvrJobHandler.cs:979-982  call site
    LogMsg("Post Command: " + Job.PostCommandText);
    RunCustomProcessAsync(Job.PostCommandText, Job.PostWorkingDir, Job.PostTimeout)

    // MxUtilSvrJobHandler.cs:991 onward (a second pass over the same
    // decompilation records this routine at :996)
    if (command.TrimStart().StartsWith("cmd", OrdinalIgnoreCase)) {
        fileName  = "cmd.exe";
        arguments = "/c " + command.Substring(3).Trim();
    } else {
        int num = command.IndexOf(' ');
        fileName  = num > 0 ? command.Substring(0, num) : command;
        arguments = num > 0 ? command.Substring(num + 1) : "";
    }
    StartInfo = new ProcessStartInfo { FileName = fileName, Arguments = arguments,
        WorkingDirectory = workingDir, UseShellExecute = false, ... }

Four properties make this a command injection rather than a command launcher:
the `cmd`-prefix special case reconstitutes full shell semantics, so
redirection, chaining, percent-expansion and quoting are all live in the payload
space; otherwise the value is split on its first space with no quoting
discipline; `Arguments` is a string rather than a vector, so `ArgumentList`
never protects the value; and there is no allow-list, no path canonicalisation,
no executable-existence check, no metacharacter rejection and no server-side
re-validation between the write and the process start. The only inspection of
the value on the path is `IsNullOrWhiteSpace`, which answers "should I run
anything" and not "is this safe". `UseShellExecute = false` with no
impersonation, no restricted token, no job object and no integrity-level
downgrade means the child inherits the service token, which is LocalSystem.

Identity reached: `NT AUTHORITY\SYSTEM`. The proof is a marker file, 21 bytes,
content `nt authority\system`, written by the injected `cmd /c whoami` child;
its modification time sits 76 milliseconds after the job-completion timestamp
the product itself recorded in its own job-history table for that run. That
offset is the attribution evidence: at that precision the file was written by
the step that followed transfer completion in that job, not by anything else on
the host.

How confirmation works, and what was deliberately not reproduced. The control
leg repeated the entire pipeline with one variable removed: using the
administrator the exploit itself had created, the same job was re-opened, its
`PostCommandText` cleared (confirmed empty both in the field and in the job
document), saved, and run again. The job completed - a second job-history row,
Completed, successful, zero files transferred - and the marker was untouched:
same byte length, same modification time to the millisecond. The two runs were
111.6 seconds apart. That single leg removes every alternative explanation for
the marker that does not involve the injected field: it was not written by the
transfer engine or any pipeline stage, it is not a leftover artifact from
installation or from an earlier experiment, and it was not written by a
scheduled task, a service restart or a background process, because the only
difference between the two runs is one field's contents.

The payload was chosen to prove identity and nothing else. What we deliberately
did not do: no destructive action, no persistence, no lateral movement, no
domain compromise, no access to any partner system, and no second command shape
beyond the one successful-transfer run and its empty-command control. The
pre-transfer counterpart of the same field was not executed, so its
exploitability is inference from shared code shape and...