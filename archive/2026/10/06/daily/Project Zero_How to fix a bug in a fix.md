---
title: How to fix a bug in a fix
url: https://projectzero.google/2026/10/emergency-patching.html
source: Project Zero
date: 2026-10-06
fetch_date: 2026-10-07T07:55:48.654101
---

# How to fix a bug in a fix

[Project Zero](/)

---

[ ]

* [blog archive](/archive.html)
* [bug reports](https://project-zero.issues.chromium.org/savedsearches/7162405)
* [about](/about-pz.html)
* [Working at PZ](/working-at-project-zero.html)
* [0day: spreadsheet](/0day.html)
* [0day: Root Cause Analyses](https://googleprojectzero.github.io/0days-in-the-wild/rca.html)
* [vulnerability disclosure policy](/vulnerability-disclosure-policy.html)
* [reporting transparency](/reporting-transparency.html)
* search

# How to fix a bug in a fix

[2026-Oct-06](/2026/10/emergency-patching.html "Permalink to this post")
Natalie Silvanovich

Project Zero often works with software vendors to remediate the vulnerabilities we report and provide broader guidance on making software more secure. Some vendors express concern about potential scenarios in which they are unable to fix vulnerabilities that are causing immediate user harm, due to limitations in their patch delivery systems. Since Project Zero encounters a wide array of systems designed to protect users in the case of exceptional exploitation scenarios, both through vendor discussions and security reviews, we want to share what weâve learned.

This post provides an overview of systems in use by large vendors that allow them to remediate small volumes of vulnerabilities much faster than their typical update process. Our goal is to provide a reference for vendors seeking to implement or enhance the capabilities of such systems, and to encourage vendors to consider how they would fix an urgent vulnerability before they receive one.

## Why patching takes time

Patching a vulnerability typically involves the following stages:

* **Triage** â a vulnerability report is received, validated, prioritized and assigned to a specific developer to be fixed
* **Patch development** â a software development team writes, reviews and commits code that fixes the vulnerability
* **Testing** â the patch is tested to ensure the vulnerability is remediated and the software still functions correctly when the patch is applied. This can include formal testing by a test team, automated testing and alpha and beta testing where a patch is shipped to a limited group of users for feedback on normal use.
* **Partner review** â some software updates require review by third parties before they can be shipped, due to relationships between the software vendor and other organizations, for example, carrier acceptance for some mobile updates.
* **Delivery** â the patch is delivered to and installed by end users
* **Activation** â sometimes an additional step, such as a system restart, is needed to switch the system to the updated software

Of course, this is a simplified picture. Patching can involve repeating steps, for example rewriting a patch if tests fail, or additional stages when third-party vendors are involved. However, this is a minimal set of steps most software updates require.

## The challenges of emergency patches

While triage and patch development time contribute substantially to the speed at which vendors can generally patch vulnerabilities, they contribute less to emergency patch time. Triage is usually very fast in situations where vendors know they have an urgent problem, and patch development can be expedited based on priority. Only in rare circumstances, where a vulnerability is especially complex, or a vendorâs security team does not have a complete picture of their softwareâs components and who within their organization maintains them, have we seen urgent patches delayed in the triage or development phase. Likewise, partner agreements usually have exceptions for updates in emergency situations.

Most vendorsâ patch speed is limited by the testing and delivery stages. Testing is important because all changes to software risk introducing unexpected behavior. The worst-case scenario is that inadequately tested software âbricksâ a device, causing it to malfunction in a way that it can no longer perform key functionality or receive software updates to remediate this. Buggy software updates have also led to situations where user data is corrupted or lost, and any decrease in software functionality after a security update makes users less likely to apply updates in the future.

The potential cost to vendors of shipping poorly tested updates varies depending on the nature of the underlying software. For example, if a mobile application is rendered unusable due to an update that corrupts local data or prevents it from launching, users can easily install the next version via an app store, and their data is usually saved on a remote server, so costs are limited to user support. Meanwhile, if a mobile device gets bricked, it needs to be returned to its manufacturer or place of purchase for repair, leading to substantial costs for the vendor and potentially the user.

The possibility of serious functional bugs is considered in the design of most patch delivery systems. Updates are often rolled out slowly, so that serious problems can be detected before they affect too many users. Often, patching vulnerabilities quickly and avoiding buggy patches are at odds with each other, requiring tradeoffs that prioritize one over the other.

A variety of other technical challenges can limit the speed of patch delivery. One is the design of the patching system. A common design is that devices probe for updates at a regular interval, leading to patch saturation being limited to that interval. âPushâ style update systems can deliver patches to all users faster, but generally require more infrastructure.

User behavior and environment can also be a barrier to patch propagation. Patches that require user interaction to install are often delayed by users, and network speed and data cost are also factors in installation rate. Updating many users at once, as opposed to over a period of time, can strain patch delivery infrastructure. Chrome and Microsoft [have](https://blog.google/security/chrome-stronger-with-every-update/) [written](https://techcommunity.microsoft.com/blog/windows-itpro-blog/securing-devices-faster-with-hotpatch-updates-on-by-default/4500066) about the challenges of updates requiring restart to install, as users are often reluctant to restart their system and restarts take time.

While testing delays and limitations of the patch delivery system affect all updates, the shorter time frame of emergency updates make them a larger contributor to the overall time it takes to deliver a patch.

## Emergency patching methods

### Feature flags

Feature flags are conditional statements in source with paths determined by values provided by a remote server. They are often used for A/B testing, but they can also be used for short term remediation of vulnerabilities in emergency situations. A widely publicized case of this was a serious 2019 FaceTime [vulnerability](https://www.npr.org/2019/01/29/689581417/apple-disables-group-facetime-after-security-flaw-let-callers-secretly-eavesdrop), where Apple temporarily disabled Group Facetime with a feature flag. Several vendors have made at least some media codecs available in 0-click contexts controllable via feature flags, and can disable them in the case of active exploitation, falling back to another codec for realtime transmission.

The main benefit of feature flags as a vulnerability remediation method is that testing can be performed with each flag set in advance, so a fast update does not require shipping untested code. They can also be delivered to users much more quickly, as updating feature flags requires transmitting a very small amount of data.

Recently, Meta published a [blog post](https://engineering.fb.com/2026/04/09/developer-tools/escaping-the-fork-how-meta-modernized-webrtc-across-50-use-cases/) on how they implemented a âdual stackâ library, in which two versions of the WebRTC video conferencing library were compiled into a single binary, with the version in use controllable via a ...