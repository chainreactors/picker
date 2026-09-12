---
title: Experimentation: Just Try It!
url: https://textslashplain.com/2026/09/11/experimentation-just-try-it/
source: text/plain
date: 2026-09-11
fetch_date: 2026-09-12T06:48:31.729531
---

# Experimentation: Just Try It!

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Experimentation: Just Try It!

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2026-09-11](https://textslashplain.com/2026/09/11/experimentation-just-try-it/)Posted in[design](https://textslashplain.com/category/design/), [dev](https://textslashplain.com/category/dev/), [tech](https://textslashplain.com/category/tech/), [web](https://textslashplain.com/category/tech/web/)Tags:[browsers](https://textslashplain.com/tag/browsers/), [Defender](https://textslashplain.com/tag/defender/), [HSTS](https://textslashplain.com/tag/hsts/)

I’ve now been working in tech for 25 years, and in that time I’ve developed some wisdom. One theme I’ve discovered and blogged about repeatedly over the years is profound despite its simplicity:

***In many cases, the best way to know whether something will work is to just try it.***

I’ve written numerous posts making fundamentally the same point:

* Want to [detect if a user is online](https://textslashplain.com/2023/05/15/detecting-when-the-user-is-offline/)? Just try sending a request!
* Want to know if a new feature will result in user churn or crashes? [Conduct a field trial with feature flags](https://textslashplain.com/2019/07/16/updating-browsers-quickly-flags-respins-and-components/#:~:text=using%20ChromiumDash.-,Field%20Trial%20Flags,-In%20some%20cases)!
* Want to know how a setting or Group Policy will behave? Create a trivial test and [try it out](https://textslashplain.com/2020/02/09/demystifying-browsers/#:~:text=it%E2%80%99s%20often%20easiest%20to%20definitively%20answer%20questions%20about%20how%20browsers%20work%20by%20trying%20things)!
* Want to know if your app or site will work after the next browser update? [Try a pre-release channel](https://textslashplain.com/2022/08/04/understanding-browser-channels/)!
* Want to know if you’re likely to be broken in the future? Use a [practical time machine](https://textslashplain.com/2021/10/01/practical-time-machines/) to check!

While I believe experimentation is usually the *best* approach, it’s not *always* practical to try things out — you might not have the time, resources, or expertise required to experiment. And sometimes your experiment might be flawed and talking to an expert or reading the spec or code might reveal hidden complexities you didn’t foresee.

Beyond that, unfortunately some systems weren’t designed to facilitate experimentation.

### Experimentation vs. Trapdoors

In this [short clip](https://www.youtube.com/watch?v=rxsdOQa_QkM), Jeff Bezos talks about decision making and the importance of recognizing the difference between a “two-way door” decision and a “one-way door” (trapdoor) decision. Put simply: If a decision can be easily reversed, you should make it quickly and without too much thought, avoiding analysis paralysis. *Just try it*!

In contrast, making a **trapdoor** decision requires much more thought: when a mistake would be very costly or unrecoverable, it is worthwhile to invest significant energy in making sure that your first choice is the best one.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-2.png?resize=750%2C750&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-2.png?ssl=1)

In my experience, there are relatively few trapdoor actions in the real-world: yes, it’s often worthwhile to “*measure twice and cut once*“, but the number of actions with unrecoverable outcomes is small and such circumstances are typically obvious.

### Design for Experimentation

To the extent possible, designers should strive to build products and standards that facilitate experimentation, allowing easy recovery if the user makes a mistake.

#### Observability

An experiment is risky if the outcome cannot be determined.

One important characteristic of experiment-friendly designs is that the experimenter can determine the result of the experiment. In some cases, the user can directly observe the result– desktop publishing software got much easier to use with the invention of “print preview” and what-you-see-is-what-you-get ([WYSIWYG](https://en.wikipedia.org/wiki/WYSIWYG)). In others, the product needs instrumentation and telemetry to determine the outcome (e.g. “*With the new compositor feature flag enabled, our crash rate increased by 4%*).

Sometimes the best way to make an experiment safe is to allow observation of the outcome *without actually making the change* (e.g. “print preview” shows the outcome without actually wasting paper); some products offer a “simulation” mode.

#### Latency

An experiment is risky if undoing the experiment takes too much time.

For example, the Web Platform’s [Strict Transport Security](https://textslashplain.com/tag/hsts/) feature allows a site to announce that it is only loadable over HTTPS, refusing to load over HTTP. A site owner can even decree that browsers should “pre-load” this enforcement to protect every visitor’s first visit. The problem is that the browser’s [HSTS Preload list](https://hstspreload.org/) only updates every few weeks, meaning [a common mistake](https://textslashplain.com/2018/04/09/hsts-preload-and-subdomains/) is that a site owner preloads their entire domain but quickly learns that some overlooked subdomains only support HTTP. Then they panic and beg the browser vendors for help, but it’s too late — it’ll be weeks before their domain can be removed from the preload list. *Oops*.

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-4.png?resize=750%2C277&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-4.png?ssl=1)

Timeline of misery (Browsers now ship even faster, but the time-to-recover is still very long)

The Web Platform’s [HTTP Public Key Pinning feature](https://tools.ietf.org/html/rfc7469) was so often a source of self-inflicted outages that the feature was [removed from Chrome entirely](https://chromestatus.com/feature/5903385005916160) in version 72.

As a less extreme example, [Microsoft Defender’s Network Protection](https://textslashplain.com/2025/04/07/understanding-smartscreen-and-network-protection/) Indicators feature allows an organization to block any “indicator” (domain, IP address, code-signing certificate or executable file’s hash). When the Security Operation Center adds a block against an indicator, Defender will prevent access to the resource. For example, if your IT department configures a Defender Custom Certificate Indicator to forbid use of Notepad++ inside your enterprise, attempting to download or run the installer will [result in a block](https://textslashplain.com/2026/01/27/microsoft-defender-false-positives/#:~:text=block%20from%20Company%20Policy):

[![](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-3.png?resize=750%2C671&ssl=1)](https://i0.wp.com/textslashplain.com/wp-content/uploads/2026/09/image-3.png?ssl=1)

But what happens if the SOC administrator read some threat intelligence and naively decided to block `s3.amazonaws.com` via a network indicator? They would very quickly find that a huge number of websites that use Amazon S3 storage fail to load correctly, preventing their colleagues from loading mission-critical web applications. The SOC admin would immediately delete the errant indicator, but because changes to Defender’s indicators typically take **two hours** to propagate to all devices, they’ve just created an expensive **outage**.

Custom Indicators are an extremely powerful feature, but to experiment with them safely the admin cannot blindly “*set it and forget it*.”

#### Audit/ReportOnly Mode

An experiment is safe if running the experiment is harmless.

Defender’s Indicators feature allows the admin to specify that the indicator should run in **[audit mode](https://learn.microsoft.com/en-us/defender-endpoint/indicators-overview#:~:text=on%20your%20dev...