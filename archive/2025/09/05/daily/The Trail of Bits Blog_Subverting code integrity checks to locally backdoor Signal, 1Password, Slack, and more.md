---
title: Subverting code integrity checks to locally backdoor Signal, 1Password, Slack, and more
url: https://blog.trailofbits.com/2025/09/03/subverting-code-integrity-checks-to-locally-backdoor-signal-1password-slack-and-more/
source: The Trail of Bits Blog
date: 2025-09-05
fetch_date: 2025-10-02T19:40:27.951336
---

# Subverting code integrity checks to locally backdoor Signal, 1Password, Slack, and more

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Subverting code integrity checks to locally backdoor Signal, 1Password, Slack, and more

Darius Houle

September 03, 2025

[application-security](/categories/application-security/), [vulnerability-disclosure](/categories/vulnerability-disclosure/), [vulnerabilities](/categories/vulnerabilities/), [exploits](/categories/exploits/)

Page content

* [Application integrity isn’t a new problem](#application-integrity-isnt-a-new-problem)
* [From frozen pizza to unsigned code execution](#from-frozen-pizza-to-unsigned-code-execution)
* [Gadget hunting](#gadget-hunting)
* [Developing a proof of concept](#developing-a-proof-of-concept)
* [The future looks Chrome](#the-future-looks-chrome)

On my first project shadow at Trail of Bits, I investigated a variety of popular [Electron](https://www.electronjs.org/)-based [applications](https://www.electronjs.org/apps) for code integrity checking bypasses. **I discovered a way to backdoor Signal, 1Password (patched in v8.11.8-40), Slack, and Chrome by tampering with executable content outside of their code integrity checks.** Looking for vulnerabilities that would allow an attacker to slip malicious code into a signed application, I identified a framework-level bypass that affects nearly all applications built on top of the Chromium engine. The following is a dive into **Electron** **CVE-2025-55305**, a practical example of backdooring applications by overwriting V8 heap snapshot files.

## Application integrity isn’t a new problem

Ensuring code integrity is not a new problem, but approaches to it vary between software ecosystems. The Electron project provides a combination of [fuses](https://www.electronjs.org/docs/latest/tutorial/fuses) (a.k.a. *feature toggles*) to enforce [integrity checking](https://www.electronjs.org/docs/latest/tutorial/asar-integrity) on executable script components. These fuses are not on by default, and must be explicitly enabled by the developer.

![Figure 1: EnableEmbeddedAsarIntegrityValidation and OnlyLoadAppFromAsar enabled in Slack](/img/electron-cve-2025-55305/electron-cve-2025-55305-1.png)

Figure 1: EnableEmbeddedAsarIntegrityValidation and OnlyLoadAppFromAsar enabled in Slack

`EnableEmbeddedAsarIntegrityValidation` ensures that the archive containing Electron’s application code is byte-for-byte what the developer packaged with the application, and `OnlyLoadAppFromAsar` ensures the archive is the only place application code is loaded from. In combination, these two fuses comprise Electron’s approach to ensuring that any JavaScript that the application loads is tamper-checked before execution. Coupled with OS-level executable code signing, this is intended to provide a guarantee that the code the application runs is *exactly what the developer distributed*. The loss of this guarantee opens a Pandora’s box of issues, most notably that attackers can:

* Inject persistent, stealthy backdoors into vulnerable applications
* Distribute tampered-with applications that nonetheless pass signature validation

Far from being theoretical, abuse of Electron applications without integrity checking is widespread enough to have its own MITRE ATT&CK technique entry: [T1218.015](https://attack.mitre.org/techniques/T1218/015/). [Loki C2](https://github.com/boku7/Loki/), a popular command and control framework based on this technique, uses backdoored versions of trusted applications (VS Code, Cursor, GitHub Desktop, Tidal, and more) to evade endpoint detection and response (EDR) software such as CrowdStrike Falcon as well as bypass application controls like AppLocker. Knowing this, it’s no surprise to find that organizations with high security requirements like 1Password, Signal, and Slack enable integrity checking in their Electron applications in order to mitigate the risk of those applications becoming the next persistence mechanism of an advanced threat actor.

## From frozen pizza to unsigned code execution

In the words of the Google V8 team,

| V8 uses a shortcut to speed things up: just like thawing a frozen pizza for a quick dinner, we deserialize a previously-prepared snapshot directly into the heap to get an initialized context. |
| --- |

Being Chromium-based, Electron apps inherit the use of “[V8 heap snapshot](https://v8.dev/blog/custom-startup-snapshots)” files to speed up loading of their various browser components (see [main, preload, renderer](https://www.electronjs.org/docs/latest/tutorial/process-model)). In each component, application logic is executed in a freshly instantiated V8 JavaScript engine sandbox (referred to as a V8 isolate). These V8 isolates are expensive to create from scratch, and therefore Chromium-based apps load previously created baseline state from heap snapshots.

While heap snapshots aren’t outright executable on deserialization, JavaScript builtins within can still be clobbered to achieve code execution. All one would need is a gadget that was executed with high consistency by the host application, and unsigned code could be loaded into any V8 isolate. Oversight in Electron’s implementation of `EnableEmbeddedAsarIntegrityValidation` and `OnlyLoadAppFromAsar` meant it did not consider heap snapshots as “executable” application content, and thus it did not perform integrity checking on the snapshots. Chromium does not perform integrity checks on heap snapshots either.

Tampering with heap snapshots is *particularly* problematic when applications are installed to user-writable locations (such as `%AppData%\Local` on Windows and `/Applications` on macOS, with certain limitations). With the majority of Chromium-derivative applications installing to user-writable paths by default, an attacker with filesystem write access can quietly write a snapshot backdoor to an existing application or bring their own vulnerable application (all without privilege elevation). The snapshot doesn’t present as an executable file, is not rejected by OS code-signing checks, and is not integrity-checked by Chromium or Electron. This makes it an excellent candidate for stealthy persistence, and its inclusion in all V8 isolates makes it an incredibly effective Chromium-based application backdoor.

## Gadget hunting

While creating custom V8 heap snapshots normally involves painfully compiling Chromium, Electron thankfully provides a [prebuilt component](https://github.com/electron/mksnapshot) usable for this purpose. Therefore, it’s easy to create a payload that clobbers members of the global scope, and subsequently to run a target application with the crafted snapshot.

```
// npx -y electron-mksnapshot@37.2.6 "/abs/path/to/payload.js"
// Copy the resulting over file your application's `v8_context_snapshot.bin`

const orig = Array.isArray;

// Use the V8 builtin `Array.isArray` as a gadget.
Array.isArray = function() {
    // Attacker code executed when Array.isArray is called.
    throw new Error("testing isArray gadget");
};
```

Figure 2: A simple gadget example

Clobbering `Array.isArray` with a gadget that unconditionally throws an error results in an expected crash, demonstrating that integrity-checked applications happily include unsigned JavaScript from their V8 isolate snapshot. Different builtins can be discovered in different V8 isolates, which allows gadgets to forensically discover which isolate they are running in. For instance, Node.js’s `process.pid` and various Node.js methods are uniquely present in the main process’s V8 isolate. The example below demonstrates how gadgets can use this technique to selectively deploy code in different isolates.

```
const orig = Array.isArray;

// Clobber the V8 builtin `Array.isArray` with a custom implementation
// This is used in diverse contexts across an application's lifecycle
Array.isArray = function() {
    // Wait to be loaded in the main process, using process.pid as a sentinel
    try {
   ...