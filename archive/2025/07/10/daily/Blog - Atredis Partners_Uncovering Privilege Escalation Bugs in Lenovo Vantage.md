---
title: Uncovering Privilege Escalation Bugs in Lenovo Vantage
url: https://www.atredis.com/blog/2025/7/7/uncovering-privilege-escalation-bugs-in-lenovo-vantage
source: Blog - Atredis Partners
date: 2025-07-10
fetch_date: 2025-10-06T23:26:01.109870
---

# Uncovering Privilege Escalation Bugs in Lenovo Vantage

[0](/cart)

[Skip to Content](#page)

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[![Atredis Partners](//images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/1566943528908-J56DPCZRQ9SVG4TFPP27/WhiskeyBirdTextOverlayWhite.png?format=1500w)](/)

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

Open Menu
Close Menu

[About](/)

[Ownership](/ownership)

[Team](/team)

[Pentesting](/pentesting)

[Embedded](/embedded)

[OCP SAFE](/ocp-safe)

[Risk](/risk)

[Contact](/contact)

[Blog](/blog)

# Uncovering Privilege Escalation Bugs in Lenovo Vantage

Jul 9

Written By [Bryan Alexander](/blog?author=67c88e52079bf056021dbb94)

This post details several privilege escalation vulnerabilities Atredis identified in Lenovo Vantage, a common management platform bundled with Lenovo laptops. We'll detail Vantage's architecture and its implications in the impact, and mitigation of, the logic bugs identified. The following CVEs were assigned to track the described issues:

* [CVE-2025-6230](https://www.cve.org/CVERecord?id=CVE-2025-6230)
* [CVE-2025-6231](https://www.cve.org/CVERecord?id=CVE-2025-6231)
* [CVE-2025-6232](https://www.cve.org/CVERecord?id=CVE-2025-6232)

Patches were released on July 8th to remediate all findings ([LEN-196648](https://support.lenovo.com/us/en/product_security/LEN-196648)). A full disclosure timeline is included at the bottom of this post.

## Lenovo Vantage

### Architecture

Lenovo Vantage comes pre-installed on Lenovo laptops and provides device updating capabilities, configuration nobs, and overall health and maintenance functionality. It's designed to be modular and pluggable with a single Vantage service running as SYSTEM and add-ins loaded and unloaded as needed. All components are written in C# which vastly simplifies the reverse engineering process due to the recoverability of pseudocode from MSIL (Microsoft Intermediate Language). The following diagram describes its architecture at a high level:

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/0bd2d412-cf4b-42f5-9620-907aae77302b/vantage_arch.jpg)

Lenovo Vantage Architecture

The Vantage service spins up an RPC endpoint that add-ins, and GUI clients, can connect into to submit requests. Importantly, add-ins themselves also expose RPC endpoints and communicate with the Vantage service via RPC. Requests are JSON and take the following form:

```
{
    "contract"    : "Target",
    "command"     : "Command",
    "payload"     : "EncodedPayload",
    "targetAddin" : "Unused",
    "clientId"    : "12",
    "CallerPid"   : 12
}
```

We observed only the first three values used throughout Vantage.

The Vantage service handles routing requests to registered add-ins, which are described by XML files located in the root folder of each add-in at `%ProgramData%\Lenovo\Vantage\Addins`. For example, the `SmartInteractAddin` exposes three contracts:

```
<Contracts>
    <Contract name="SystemManagement.SmartGesture" />
    <Contract name="SystemManagement.PrecisionTouchPad" />
    <Contract name="SystemManagement.VisionProtection" />
  </Contracts>
```

In addition to contract definitions, the add-in XML files specify other runtime configuration such as event subscriptions and signature blocks. `SmartInteractAddin` configures itself with the following:

```
<Addin name="SmartInteractAddin" version="1.0.3.64" isRollback="false" secondaryServer="false" noSWFlags="false" armReady="false" platform="MSIL" runas="user">
```

The `runas` key designates execution context of the add-in. Of the approximately 20 add-ins supported by Vantage, 5 of them run under an elevated context.

In order to pass requests through to the Vantage service and its registered add-ins, clients must be considered trusted. A rudimentary authentication routine is implemented in the Vantage service and performs the following:

![](https://images.squarespace-cdn.com/content/v1/576323cfd482e984e113fe9c/f62986e5-55e9-4534-9fb0-d92926babd75/vantage_authz.jpg)

RPC Authorization Check

Ostensibly, the determinitive check is the digital signature verification of the client's process. If the assembly is not signed by Lenovo then the client is considered untrusted and the request rejected. This is a very common strategy employed by various laptop and software vendors, including [Dell](https://dronesec.net/blog/dell-digital-delivery-cve-2018-11072-local-privilege-escalation/), [Asus](https://blog.talosintelligence.com/decrement-by-one-to-rule-them-all/), and [Symantec](https://web.archive.org/web/20210621094826/https%3A//www.accenture.com/us-en/blogs/cyber-defense/exploiting-arbitrary-file-move-in-symantec-endpoint-protection), and is trivial to bypass. Three options quickly come to mind:

1. Leverage common remote process injection techniques (`CreateRemoteThread`)
2. Identify a signed Lenovo binary loading DLLs from the local path and hijack
3. Create a UWP app

We found the second option to be simplest and ended up leveraging `FnhotkeyWidget.exe` to facilitate access to the RPC endpoints. This binary attempts to load a few DLLs from the local path which we can hijack by copying the binary to a writable location. We then put a DLL named `profapi.dll` in the local path of the binary and executed to obtain code execution within the signed binary.

### Sending Requests

Since each add-in communicates with the Vantage service over RPC, Lenovo developed a standard RPC client to generically support all clients. `Lenovo.Vantage.RpcClient.dll` is a C# DLL exposing common communication routines and transparently supporting various architectures. It can be used as follows to send a request to the Vantage RPC endpoint:

```
Dictionary<string, string> DiskSpaceRequest = new Dictionary<string, string>()
{
    { "contract", "SystemOptimization.SystemUpdate" },
    { "command", "Get-FreeDiskSpace" },
};
string requestStr = JsonConvert.SerializeObject(DiskSpaceRequest);

RpcClient client = new RpcClient();
string text = client.MakeRequest(requestStr, delegate(string response)
{
    return Lenovo.Vantage.RpcCommon.RpcCallbackResult.Ok;
});
```

With that we can now access the Vantage RPC endpoint and subsequently registered add-in interfaces.

We initially began by mapping out available contracts to add-ins running in an elevated context. Five of the 20 add-ins were running as SYSTEM: CommercialAddin, LenovoAuthenticationAddin, LenovoHardwareScanAddin, LenovoSystemUpdateAddin, and VantageCoreAddin. The VantageCoreAddin is the core service add-in that runs perpetually along side Lenovo Vantage and provides a variety of basic system functionality services. We began our research here and identified two issues.

## CVE-2025-6230

The first set of bugs Atredis identified were within the Vantage service core routines. Though nearly all functionality and request handlers are implemented via add-ins, several core contracts exist within Vantage itself.

One of these is within `VantageCoreAddin` which is responsible for basic functionality on the host, such as fetching system information, starting bluetooth scans, and updating the add-in settings database. One of the supported commands, `Lenovo.Vantage.AddinSetting`, is used to configure local Vantage settings. These settings live in a SQLite database at `C:\ProgramData\Lenovo\Vantage\Settings\LocalSettings.db` and are accessible only to the SYSTEM account.

When processing a `DeleteTable` command, the `payload` is expected to contain an embedded JSON package containing the table name which is then purged from the database:

```
u...