---
title: [0day-rubbish] Dataedo Portal 26.2.8 with Dataedo Agent 26.2.8 unrestricted scheduler job-type deserialization to Agent-host command execution (8.1)
url: https://seclists.org/fulldisclosure/2026/Oct/15
source: Full Disclosure
date: 2026-10-15
fetch_date: 2026-10-16T06:37:52.815166
---

# [0day-rubbish] Dataedo Portal 26.2.8 with Dataedo Agent 26.2.8 unrestricted scheduler job-type deserialization to Agent-host command execution (8.1)

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

[![Previous](/images/left-icon-16x16.png)](14)
[By Date](date.html#15)
[![Next](/images/right-icon-16x16.png)](16)

[![Previous](/images/left-icon-16x16.png)](14)
[By Thread](index.html#15)
[![Next](/images/right-icon-16x16.png)](16)

![](/shared/images/nst-icons.svg#search)

# [0day-rubbish] Dataedo Portal 26.2.8 with Dataedo Agent 26.2.8 unrestricted scheduler job-type deserialization to Agent-host command execution (8.1)

---

*From*: disclosure via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Tue, 13 Oct 2026 02:21:33 +0000

---

```
0day Rubbish Research Team is publicly disclosing a vulnerability in Dataedo
Portal 26.2.8 together with Dataedo Agent 26.2.8, the closed-source enterprise
data-catalog and data-governance platform from Dataedo sp. z o.o. (Poland).
Both components are in scope because the chain crosses from one to the other:
the Portal discloses a database credential, and the separately installed Agent
executes an injected scheduler job on its own host. In the verified shape the
command ran as `nt authority\system`.

Type: deserialization of untrusted data by unrestricted invocation-type
resolution (CWE-502 primary, with CWE-470 an equally defensible
characterisation of the same mechanism), enabled by insufficiently protected
credentials (CWE-522) under a hard-coded cryptographic key (CWE-321), with
incorrect authorization and missing privilege separation (CWE-863 / CWE-284)
and execution with unnecessary privileges (CWE-250 / CWE-732) contributing.

The entry route works exactly as designed, which is the point. `GET
/api/repository/connection-string` returns the repository database connection
string to a caller holding a repository-management role, encrypted with
`SimpleAES` - an AES-256-CBC construction whose 32-byte key and 16-byte IV are
byte-array literals in the shipped `Dataedo.Settings.dll` and are
byte-identical across builds, with PKCS7 padding and every ciphertext byte
encoded as a three-digit decimal group. Anyone holding a copy of the product
therefore decrypts the response offline; both values are reproduced in the
published proof-of-concept. `GenerateEncryptionKey()` exists at
`Dataedo.Settings:116` and no call path was found that replaces the static
field with its output. A full census counted the same static pair referenced
from 19 assemblies. The recovered login in the tested deployments was `sa`, a
sysadmin-level principal on the repository database - and that database also
holds the Hangfire scheduler storage in the `[Scheduler]` schema.

The sink is on the Agent side. `AgentServiceRegistration.AddScheduler` calls
`AddHangfireServer` twice, once for the `default` queue with a worker count of
one and once for the `priority` queue, and registers no `ITypeResolver`
restriction and no invocation allowlist with either, so Hangfire's default type
resolver will resolve any type name the runtime can load. `FilterInitializer`
then runs `GlobalJobFilters.Clear()` and adds four filters, none of which
constrains execution: `ExecutionCreatingFilter` and `RequestUpdatingFilter` are
`IClientFilter` implementations, which run on the client-side job-creation path
rather than on server-side execution and additionally return early unless the
declaring type implements `ISchedulerTaskExecutor`; `JobCancellationFilter` is
an `IApplyStateFilter` that reacts only to transitions into `DeletedState`;
and `AutomaticRetry` is configured with `Attempts = 0`, which disables retries
and has no bearing on authorization. After `Clear()` nothing in the chain
inspects the invocation type, the declaring type, the method name or the
arguments at execution time. The producer is disciplined and the consumer is
not, and the consumer is the one that executes.

One row into `[Scheduler].Job` plus one row into `[Scheduler].JobQueue` is
therefore enough, and no gadget chain is needed because the invocation document
names the sink directly:

    {"Type":"System.Diagnostics.Process, System.Diagnostics.Process",
     "Method":"Start",
     "ParameterTypes":"[\"System.String\",\"System.String\"]",
     "Arguments":"[\"cmd.exe\",\"/c <payload>\"]"}

Three details are load-bearing and none of them is obvious. The `Arguments`
column and the `InvocationData.Arguments` member must both carry the command,
and the latter is a JSON array serialized as a string inside the outer JSON
object, so a Windows path appears with doubled backslashes in the outer
document and quadrupled backslashes in the inner one while the enclosing T-SQL
literal doubles every single quote. `QUOTED_IDENTIFIER` must be ON because the
scheduler schema uses filtered indexes. And the `JobQueue` row must name a
queue the Agent actually polls, otherwise the job exists and is never fetched.

Execution lands on the Agent host as the identity of the Agent process. Two
shapes were observed and both are recorded because they bound the claim:
`whoami` returned `<agent-host>\administrator` when the Agent was launched from
a console under an interactive administrative account, and `nt authority\system`
when it ran resident as a SYSTEM-privileged scheduled task, where filtered
`tasklist` output for PID 4 appended to the same file showed the System process
in session 0 under the Services session name, consistent with a service-context
execution environment. For production the Agent is installed as a Windows
service through `AddWindowsService` with an empty `ServiceConfiguration`, so
the identity is whatever that service is configured with: SYSTEM is what the
default service configuration yielded in the tested shape and is not a claim
about every deployment, and the installer's own service-registration table was
not inspected to finality, so the production service account is an inference
from the host configuration call rather than an artifact-confirmed value.

How confirmation works. The recorded job was assigned identifier 7 and its
state progression was read directly from the storage tables: Enqueued ->
Processing (with the fetching worker's own ServerId recorded) -> Succeeded,
with `PerformanceDuration` of 4 milliseconds and `State.Result` equal to "Can
not serialize the return value". That pair is proof of invocation rather than
of bookkeeping: `Process.Start` returns a live Process object which the
scheduler cannot serialize into its state column, so it records that string,
and a job that had been rejected or never fetched would not have reached
Succeeded at all. A marker file was written on the Agent host by the executed
command. The marker path and the marker token are command-line arguments of the
published tool, and neither the path nor the token from the recorded run is
reproduced here, because both are artefacts of one execution on one host rather
than evidence about the product.

The strongest single piece of evidence in the package is an argument-provenance
control. The first injection attempt wrote a placeholder token into the
`[Scheduler].Job.Arguments` column while the `InvocationData` document was
correct, and the Agent's run log recorded the shell complaining that the
placeholder was not recognized as an internal or external command. That
establishes that the executed arguments came from the database row and not from
any configuration, command line or code path inside the Agent, and it
identified the column mismatch in the same breath. Without it a reviewer could
reasonably ask whether the observed execution was an artefact of the test rig;
with it the causality is direct.

What was deliberately no...