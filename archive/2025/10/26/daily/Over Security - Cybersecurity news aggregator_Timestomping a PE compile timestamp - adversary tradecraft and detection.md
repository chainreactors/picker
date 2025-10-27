---
title: Timestomping a PE compile timestamp - adversary tradecraft and detection
url: https://fluxsec.red/timestomping-pe-compile-time
source: Over Security - Cybersecurity news aggregator
date: 2025-10-26
fetch_date: 2025-10-27T16:51:00.361294
---

# Timestomping a PE compile timestamp - adversary tradecraft and detection

☰

## Intro

* [About Me](/)

## Sanctum EDR

* [Intro and plan for the Sanctum EDR](/sanctum-edr-intro)
* [Creating a Windows Driver in Rust](/rust-windows-driver)
* [Configuring a Rust Windows driver](/rust-windows-driver-configuration)
* [Building the Driver Object](/rust-windows-driver-object)
* [Error logging](/logging-errors-in-rust)
* [Windows Driver IRQL and acquiring a Driver Mutex](/windows-rust-driver-irql-driver-mutex)
* [wdk-mutex: An idiomatic mutex for Rust Windows Kernel Drivers](/wdk-mutex-windows-driver-mutex)
* [Theory: EDR Syscall hooking and Ghost Hunting, my approach to detection](/edr-syscall-hooking)
* [Implementing syscall hooks in Rust](/implementing-syscall-hooking-rust)
* [Communicating from the hooked syscall](/communicating-from-hooked-syscall-rust)
* [Ghost hunting OpenProcess](/ghost-hunting-open-process)
* [Hooking VirtualAllocEx](/edr-hooking-virtual-alloc-ex-rust-malware)
* [Mitigating broadcast spoofs with Ghost Hunting](/mitigating-broadcast-spoofing-rust-sanctum-edr-ghost-hunting)
* [Creating a Protected Process Light in Rust for Sanctum EDR](/creating-a-ppl-protected-process-light-in-rust-windows)
* [Reading Event Tracing for Windows Threat Intelligence](/event-tracing-for-windows-threat-intelligence-rust-consumer)
* [Improving the Ghost Hunting implementation for flexibility and speed](/improving-the-ghost-hunting-implementation-for-flexibility)
* [Monitoring NTDLL for in memory patching](/monitoring-ntdll-for-memory-patching-etw-hacking-bypass-in-rust-EDR)
* [Reverse engineering undocumented Windows Kernel features to work with the EDR](/reverse-engineering-windows-11-kernel)
* [Full spectrum Event Tracing for Windows detection in the kernel against rootkits](/full-spectrum-event-tracing-for-windows-detection-in-the-kernel-against-rootkits)
* [Real-time Ransomware Detection Strategy](/considering-ransomware-edr-defence-strategy)
* [Making improvements to the EDR DLL injection](/improving-edr-dll-injection-kernel-callback)
* [Strategy for Early Bird APC Queue Injection and improving Ghost Hunting](/early-bird-apc-queue-injection)
* [Alt Syscalls for Windows 11](/alt-syscalls-for-windows-11)
* [Improving consistency with EDR DLL Injection via APCs](/improving-EDR-via-windows-driver-apc-injection-rust)

## Offensive Development - Rust

* [Introduction to the Windows API in Rust with a DLL Loader](/winapi-rust-intro)
* [Building a DLL in Rust](/rust-dll-windows-api)
* [Remote process DLL injection in Rust](/remote-process-dll-injection)
* [Hells Gate Rust - EDR Evasion with syscalls](/rust-edr-evasion-hells-gate)
* [EDR Evasion ETW patching in Rust](/etw-patching-rust)
* [EDR Evasion APC Queue Injection in Rust](/apc-queue-injection-rust)
* [Rust DLL Search Order Hijacking](/rust-dll-search-order-hijacking)
* [Rust OPSEC for Malware Development](/rust-opsec-malware-development)
* [Hells Hollow: A new SSDT Hooking technique](/hells-hollow-a-new-SSDT-hooking-technique-with-alt-syscalls-rootkit)
* [Timestomping a PE compile timestamp - adversary tradecraft and detection](/timestomping-pe-compile-time)

## Offensive Development - General

* [Reflective DLL injection and bootstrapping in C](/reflective-dll-injection-in-c)
* [DLL Injection EDR Evasion 1: Hiding an elephant in the closet](/dll-injection-edr-evasion-1)

## My tools

* [Clipboard Hex Dumper Tool](/chx-copy-hex-dumper)
* [Str Crypter - Payload string encryption with Rust](/str-crypter)
* [Export Resolver](/export-resolver)

## Misc

* [How I developed a markdown blog in Go and HTMX](/how-I-developed-a-markdown-blog-with-go-and-HTMX)
* [Helpful Rust Windows API programming cheat sheet](/rust-windows-api-winapi-programming-msdn-cheatsheet)
* [Inside DCHSpy: Analysing Iranian APT MuddyWater free VPN mobile spyware](/analysing-Iranian-APT-MuddyWater-mobile-spyware-free-vpn-comodo)

[![](/static/images/flux.png)](/)

## Intro

* [About Me](/)

## Sanctum EDR

* [Intro and plan for the Sanctum EDR](/sanctum-edr-intro)
* [Creating a Windows Driver in Rust](/rust-windows-driver)
* [Configuring a Rust Windows driver](/rust-windows-driver-configuration)
* [Building the Driver Object](/rust-windows-driver-object)
* [Error logging](/logging-errors-in-rust)
* [Windows Driver IRQL and acquiring a Driver Mutex](/windows-rust-driver-irql-driver-mutex)
* [wdk-mutex: An idiomatic mutex for Rust Windows Kernel Drivers](/wdk-mutex-windows-driver-mutex)
* [Theory: EDR Syscall hooking and Ghost Hunting, my approach to detection](/edr-syscall-hooking)
* [Implementing syscall hooks in Rust](/implementing-syscall-hooking-rust)
* [Communicating from the hooked syscall](/communicating-from-hooked-syscall-rust)
* [Ghost hunting OpenProcess](/ghost-hunting-open-process)
* [Hooking VirtualAllocEx](/edr-hooking-virtual-alloc-ex-rust-malware)
* [Mitigating broadcast spoofs with Ghost Hunting](/mitigating-broadcast-spoofing-rust-sanctum-edr-ghost-hunting)
* [Creating a Protected Process Light in Rust for Sanctum EDR](/creating-a-ppl-protected-process-light-in-rust-windows)
* [Reading Event Tracing for Windows Threat Intelligence](/event-tracing-for-windows-threat-intelligence-rust-consumer)
* [Improving the Ghost Hunting implementation for flexibility and speed](/improving-the-ghost-hunting-implementation-for-flexibility)
* [Monitoring NTDLL for in memory patching](/monitoring-ntdll-for-memory-patching-etw-hacking-bypass-in-rust-EDR)
* [Reverse engineering undocumented Windows Kernel features to work with the EDR](/reverse-engineering-windows-11-kernel)
* [Full spectrum Event Tracing for Windows detection in the kernel against rootkits](/full-spectrum-event-tracing-for-windows-detection-in-the-kernel-against-rootkits)
* [Real-time Ransomware Detection Strategy](/considering-ransomware-edr-defence-strategy)
* [Making improvements to the EDR DLL injection](/improving-edr-dll-injection-kernel-callback)
* [Strategy for Early Bird APC Queue Injection and improving Ghost Hunting](/early-bird-apc-queue-injection)
* [Alt Syscalls for Windows 11](/alt-syscalls-for-windows-11)
* [Improving consistency with EDR DLL Injection via APCs](/improving-EDR-via-windows-driver-apc-injection-rust)

## Offensive Development - Rust

* [Introduction to the Windows API in Rust with a DLL Loader](/winapi-rust-intro)
* [Building a DLL in Rust](/rust-dll-windows-api)
* [Remote process DLL injection in Rust](/remote-process-dll-injection)
* [Hells Gate Rust - EDR Evasion with syscalls](/rust-edr-evasion-hells-gate)
* [EDR Evasion ETW patching in Rust](/etw-patching-rust)
* [EDR Evasion APC Queue Injection in Rust](/apc-queue-injection-rust)
* [Rust DLL Search Order Hijacking](/rust-dll-search-order-hijacking)
* [Rust OPSEC for Malware Development](/rust-opsec-malware-development)
* [Hells Hollow: A new SSDT Hooking technique](/hells-hollow-a-new-SSDT-hooking-technique-with-alt-syscalls-rootkit)
* [Timestomping a PE compile timestamp - adversary tradecraft and detection](/timestomping-pe-compile-time)

## Offensive Development - General

* [Reflective DLL injection and bootstrapping in C](/reflective-dll-injection-in-c)
* [DLL Injection EDR Evasion 1: Hiding an elephant in the closet](/dll-injection-edr-evasion-1)

## My tools

* [Clipboard Hex Dumper Tool](/chx-copy-hex-dumper)
* [Str Crypter - Payload string encryption with Rust](/str-crypter)
* [Export Resolver](/export-resolver)

## Misc

* [How I developed a markdown blog in Go and HTMX](/how-I-developed-a-markdown-blog-with-go-and-HTMX)
* [Helpful Rust Windows API programming cheat sheet](/rust-windows-api-winapi-programming-msdn-cheatsheet)
* [Inside DCHSpy: Analysing Iranian APT MuddyWater free VPN mobile spyware](/analysing-Iranian-APT-MuddyWater-mobile-spyware-free-vpn-comodo)

# Timestomping a PE compile timestamp - adversary tradecraft and detection

How adversaries weaponise PE compile timestamps to deceive analysts and hide in plain sight.

---

## Intro

If you’ve wondered how advanced adversaries (red teams or real threat actors) try blend into a targ...