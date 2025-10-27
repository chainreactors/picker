---
title: Async BOFs – “Wake Me Up, Before You Go Go”
url: https://www.outflank.nl/blog/2025/07/16/async-bofs-wake-me-up-before-you-go-go/
source: Publications | Outflank
date: 2025-07-17
fetch_date: 2025-10-06T23:28:13.778625
---

# Async BOFs – “Wake Me Up, Before You Go Go”

[Skip to the content](#content)

[logo](https://www.outflank.nl)
Experts in red teaming

* [Red Team Tools](/products/)
  + [Outflank Security Tooling](/products/outflank-security-tooling/)
    - [Outflank C2](https://www.outflank.nl/products/outflank-security-tooling/outflank-c2/)
    - [Payload Generator](/products/outflank-security-tooling/pe-payload-generator/)
    - [Tooling](/products/outflank-security-tooling/ost-tool-list/)
    - [Tradecraft](/products/outflank-security-tooling/tradecraft/)
    - [Demo Videos](/videos/ost-demo-videos/)
  + [Cobalt Strike](/products/cobalt-strike/)
  + [Red Team Bundle](/datasheets/red-team-bundle/)
  + [Advanced Red Team Bundle](/datasheets/advanced-red-team-bundle/)
* [Red Team Services](/services/red-teaming/)
* Blog & Resources
  + [Outflank Blog](/blog/)
  + [Community](/products/outflank-security-tooling/ost-community/)
  + [Datasheets](/datasheets/)
  + [OST Demo Videos](/videos/ost-demo-videos/)
  + [OST Releases](/services/outflank-security-tooling/releases/)
  + [Upcoming Events](https://www.outflank.nl/upcoming-events/)
* [About Us](/company/)
  + [Our Company](/company/)
  + [OST Testimonials](/company/outflank-security-tooling-testimonials/)
  + [Contact Us](/contact/)
* [Schedule a Demo](/demo-request/)
* [REQUEST QUOTEREQUEST QUOTE](/request-a-quote/)

# Publications

# [Async BOFs – “Wake Me Up, Before You Go Go”](https://www.outflank.nl/blog/2025/07/16/async-bofs-wake-me-up-before-you-go-go/ "Async BOFs – “Wake Me Up, Before You Go Go”")

[Dima van de Wouw](https://www.outflank.nl/blog/author/dima/ "Posts by Dima van de Wouw")
 |
July 16, 2025

**Asynchronous BOFs: Enabling New Use Cases for Red Team Operators**

The [introduction of Beacon Object Files (BOFs)](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/beacon-object-files_main.htm) by [Cobalt Strike](https://www.outflank.nl/products/cobalt-strike/) in 2020 revolutionized the capabilities of red team operators and developers, offering a standardized interface for operator code to run within, and interact with, an implant. However, the current BOF standard was designed for synchronous operations, [limiting its potential applications](https://aff-wg.org/2025/06/26/beacon-object-files-five-years-on/).

**Asynchronous BOFs Execution Would Enable New Red Team Capabilities**

Within this blog Cornelis ([@Cneelis](https://x.com/Cneelis)) and I introduce the concept and initial design of *real-time monitoring for events (e.g. sleep until an admin logs in, sleep until a user starts his password vault)* for Beacon Object Files. This new asynchronous design allows operators to roll out a network of sensors and stream these events to the C2 server for further processing – all while the implant is sleepmasked. The server can in turn queue automated tasks, such as downsleeping, asking a TGT (and periodically renewing it) or starting a keylogger.

**Background**

Within Outflank Security Tooling (OST), we offer both a collection of tradecraft (including BOFs) and a custom implant. At Outflank we constantly try to innovate and push boundaries of existing technologies.

One of the areas we are experimenting with for a while is asynchronous Beacon Object Files, and this blog will share some insights into our journey so far.

*Note: At this point in time, we are not sharing a specification or code samples. This is because the server and implant-side API specifications can change as we are in the midst of our research journey and first want to collect feedback.*

## Our Research Journey

**Where it Started**

During our operations we regularly encounter shortcomings of the current BOF implementation. In large customer environments where modern security solutions (NGAV/EDR) are used, it might be OPSEC expensive/risky to perform process injection, so we prefer to stay in the process. However, unfortunately not all BOF tools that we use (think of domain/share enumeration tools or monitoring tools) are suitable to run for a longer/indefinite period without the implant itself temporarily not responding anymore.

Additionally, a long running BOF task will prevent the implant from going into (deep) sleep, keeping it visible in memory and showing an unbacked thread stack. This can cause OPSEC risks with current EDR solutions.

In short, the current BOF standard was initially designed for synchronous operations, limiting its potential applications. This is due to the design; the BOF makes function calls to the implant code (text section) every time a `Beacon` (i.e. `BeaconPrintf`) function is called. If done from a separate thread, while the implant is sleeping with a sleepmask enabled, the process will crash.

**Brainstorming on Asynchronous BOFs**

To get around these problems we started looking at a solution where we can make BOF execution asynchronous. The most basic idea is to run BOF tools in the background and still be able to use our implant. As soon as new data is available from the BOF, this data should seamlessly pass on to the server (console) and as soon as the BOF is done with its task everything is cleaned up nicely by the implant.

In one of the whiteboard-sessions we identified a need for stopping tasks and waking up the implant from within the BOF code. We liked the idea and started further exploring.

At RedTreat 2024 (an invite-only conference) we presented and discussed a first version of asynchronous BOFs. We’ve since then refined the design and ideas.

## Use Case: Monitoring the Compromised Endpoint for an Admin Login

After various research discussions, we identified the following use case:

*“An operator should have a capability to instruct an implant to sleep until an admin logs in on the infected machine, and once the admin logs-in the implant should check-in instantly to relay this information”.*

This capability would allow an operator to be:

* *M****ore* *time-efficient*:** No need to manually monitor or spend time on checking and waiting for an event to occur on the infected machine.
* ***More stealth*:** as the implant is sleeping and preventing unnecessary check-ins / network communication there is less detection risk.
* ***More reliable*:** you are sure to not miss the event, even if an event only lasts a couple of minutes or occurs outside of office hours.
* ***More effective:*** instant check-in once the specific event occurs instead of waiting ‘until the next sleep interval’ making it much more likely that you are ‘on-time’ to execute your next action. Additionally, if combined with pre-programmed response actions, it would be possible to extract the value (i.e., credentials, etc) of an event in order to continue later (i.e., after the weekend).

Once this use case works, we can imagine the following situation:

## Example Scenario

Imagine a reasonably well designed and tiered (+clean source) environment from a target organisation that already experienced multiple (3+) Red Team engagements. In this example, their environment is not perfect, so for admin / business purposes, there is a brief tier violation.

A highly privileged admin / service account only logs in for a couple of minutes every week on a shared / lower tier workstation. Obtaining these credentials/tickets would rule out any manual monitoring. We need to monitor and react to user logon events. This asynchronous task will wake the implant up at every new/interesting logon. The implant will relay each newly logged on username to the server. On the server is a task that handles the output of this monitoring job. The server can queue automated tasks if a tier violation is detected or if the user is in the whitelist / not on the blacklist, etc. These tasks can include downsleeping, asking a TGT (and periodically renewing it), injecting into a process, starting a keylogger or running an AskCreds BOF to spawn a popup asking for the admin’s credentials. Additionally, operators can also be notified.

Once all preparations are done...