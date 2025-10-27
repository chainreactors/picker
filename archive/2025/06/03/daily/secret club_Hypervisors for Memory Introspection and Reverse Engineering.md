---
title: Hypervisors for Memory Introspection and Reverse Engineering
url: https://secret.club/2025/06/02/hypervisors-for-memory-introspection-and-reverse-engineering.html
source: secret club
date: 2025-06-03
fetch_date: 2025-10-06T22:55:14.546859
---

# Hypervisors for Memory Introspection and Reverse Engineering

[SECRET CLUB](/) [HOME](/) [ABOUT](/about)

# Hypervisors for Memory Introspection and Reverse Engineering

![main authors image](/assets/author_img/memn0ps.jpg)  [memN0ps](/author/memn0ps)

 Jun 2, 2025

---

## [Introduction](#introduction)

In this article, we explore the design and implementation of Rust-based hypervisors for memory introspection and reverse engineering on Windows. We cover two projects - [illusion-rs](https://github.com/memN0ps/illusion-rs), a UEFI-based hypervisor, and [matrix-rs](https://github.com/memN0ps/matrix-rs), a Windows kernel driver-based hypervisor. Both leverage Extended Page Tables (EPT) to implement stealthy control flow redirection without modifying guest memory.

We begin by identifying how to reliably detect when the System Service Descriptor Table (SSDT) is fully initialized within `ntoskrnl.exe`, allowing hooks to be safely installed without risking a system crash. Illusion and Matrix differ in how they trigger and redirect execution. Illusion uses a single EPT and in-place patching with VM-exit instructions like `VMCALL`, combined with `Monitor Trap Flag (MTF)` stepping to replay original bytes safely. In contrast, Matrix uses a dual-EPT model where the primary EPT maps read/write memory and the secondary EPT remaps execute-only shadow pages containing trampoline hooks. Execution is redirected using `INT3` breakpoints and dynamic EPTP switching during EPT violations. Both approaches hide inline hooks from guest virtual memory and redirect execution flow to attacker-controlled code - such as shellcode or handler functions - using EPT-based remapping and VM-exits triggered by CPU instructions like `INT3`, `VMCALL`, or `CPUID`.

In hypervisor development, shadowing refers to creating a second, hypervisor-controlled view of guest memory. When a page is shadowed, the hypervisor creates a duplicate of the original page - typically referred to as a shadow page - and updates the EPT to redirect access to this copy. This allows the hypervisor to intercept, monitor, or redirect memory accesses without modifying the original guest memory. Shadowing is commonly used to inject hooks, conceal modifications, or control execution flow at a fine-grained level. The guest and shadow pages remain distinct: the guest believes it is accessing its own memory, while the hypervisor controls what is actually seen or executed.

We demonstrate how to use execute-only permissions to trap instruction fetches, read/write-only permissions to catch access violations, and shadow pages to inject trampoline redirections. For introspection and control transfer, we rely on instruction-level traps such as `VMCALL`, `CPUID`, and `INT3`, depending on the context. In Illusion, instruction replay is handled via `Monitor Trap Flag (MTF)` single-stepping to safely restore overwritten bytes.

While these techniques are well-known in the game hacking community, they remain underutilized in infosec. This article aims to bridge that gap by providing a practical, reproducible walkthrough of early boot-time and kernel-mode EPT hooking techniques. All techniques used are public, stable, and do not rely on undocumented internals or privileged SDKs.

The approach taken prioritizes minimalism and reproducibility. We assume readers have a working understanding of paging, virtual memory, and the basics of Intel VT-x and EPT. While some concepts may apply to AMD SVM and NPT, this article focuses exclusively on Intel platforms. Both hypervisors avoid modifying guest memory entirely, preserving system integrity and navigating around kernel protections like PatchGuard. This enables stealth monitoring of functions like `NtCreateFile` and `MmIsAddressValid` from outside the guest’s control using EPT-backed remapping.

### [Table of Contents](#table-of-contents)

* [Illusion: UEFI-Based Hypervisor with EPT-Based Hooking](#illusion-uefi-based-hypervisor-with-ept-based-hooking)
  + [Setting up IA32\_LSTAR MSR hook during Initialization (`initialize_shared_hook_manager()`)](#setting-up-ia32_lstar-msr-hook-during-initialization-initialize_shared_hook_manager)
  + [Setting Kernel Image Base Address and Size (`set_kernel_base_and_size()`)](#setting-kernel-image-base-address-and-size-set_kernel_base_and_size)
  + [Detecting When SSDT Is Loaded Inside `ntoskrnl.exe`](#detecting-when-ssdt-is-loaded-inside-ntoskrnlexe)
    - [On Intel processors, the execution path is reliable (verified via Binary Ninja analysis on Windows 11 build 26100):](#on-intel-processors-the-execution-path-is-reliable-verified-via-binary-ninja-analysis-on-windows-11-build-26100)
    - [On AMD processors, the path is conditional (verified via Binary Ninja analysis on Windows 11 build 26100):](#on-amd-processors-the-path-is-conditional-verified-via-binary-ninja-analysis-on-windows-11-build-26100)
  + [Setting Up EPT Hooks (`handle_cpuid()`)](#setting-up-ept-hooks-handle_cpuid)
  + [Resolving Targets and Dispatching Hooks (`manage_kernel_ept_hook()`)](#resolving-targets-and-dispatching-hooks-manage_kernel_ept_hook)
  + [Second-Level Address Translation (SLAT): EPT (Intel) and NPT (AMD)](#second-level-address-translation-slat-ept-intel-and-npt-amd)
  + [EPT Hooking Overview (`build_identity()`)](#ept-hooking-overview-build_identity)
    - [Installing the Hook Payload (`ept_hook_function()`)](#installing-the-hook-payload-ept_hook_function)
    - [Mapping the Large Page (`map_large_page_to_pt()`)](#mapping-the-large-page-map_large_page_to_pt)
    - [Step 1 - Splitting the Page (`is_large_page()` -> `split_2mb_to_4kb()`)](#step-1---splitting-the-page-is_large_page---split_2mb_to_4kb)
    - [Shadowing the Page (`is_guest_page_processed()` -> `map_guest_to_shadow_page()`)](#shadowing-the-page-is_guest_page_processed---map_guest_to_shadow_page)
    - [Step 2 - Cloning the Code (`unsafe_copy_guest_to_shadow()`)](#step-2---cloning-the-code-unsafe_copy_guest_to_shadow)
    - [Step 3 - Installing the Inline Hook](#step-3---installing-the-inline-hook)
    - [Step 4 - Revoking Execute Rights (`modify_page_permissions()`)](#step-4---revoking-execute-rights-modify_page_permissions)
    - [Step 5 - Invalidating TLB and EPT Caches (`invept_all_contexts()`)](#step-5---invalidating-tlb-and-ept-caches-invept_all_contexts)
    - [Step 6 and 7 - Catching Execution with EPT Violations (`handle_ept_violation()`)](#step-6-and-7---catching-execution-with-ept-violations-handle_ept_violation)
    - [Step 8 - Handling VMCALL Hooks (`handle_vmcall()`)](#step-8---handling-vmcall-hooks-handle_vmcall)
    - [Step 9 - Single-Stepping with Monitor Trap Flag (`handle_monitor_trap_flag()`)](#step-9---single-stepping-with-monitor-trap-flag-handle_monitor_trap_flag)
    - [Catching Read/Write Violations (`handle_ept_violation()`)](#catching-readwrite-violations-handle_ept_violation)
  + [Illusion Execution Trace: Proof-of-Concept Walkthrough](#illusion-execution-trace-proof-of-concept-walkthrough)
    - [Controlling EPT Hooks via Hypercalls](#controlling-ept-hooks-via-hypercalls)
* [Matrix: Windows Kernel Driver-Based Hypervisor Using Dual EPT](#matrix-windows-kernel-driver-based-hypervisor-using-dual-ept)
  + [Initializing Primary and Secondary EPTs (`virtualize_system()`)](#initializing-primary-and-secondary-epts-virtualize_system)
  + [Step 1 and 2 - Creating Shadow Hooks and Setting Up Trampolines (`hook_function_ptr()`)](#step-1-and-2---creating-shadow-hooks-and-setting-up-trampolines-hook_function_ptr)
  + [Step 3, 4, 5 and 6 - Dual-EPT Remapping for Shadow Execution (`enable_hooks()`)](#step-3-4-5-and-6---dual-ept-remapping-for-shadow-execution-enable_hooks)
  + [Step 7 - Configuring VMCS for Breakpoint VM-Exits (`setup_vmcs_control_fields()`)](#step-7---configuring-vmcs-for-breakpoint-vm-exits-setup_vmcs_control_fields)
  + [Step 8 - Handling EPT Violations with Dynamic EPTP Switching (`handle_ept_violation()`)](#step-8---handling-ept-violations-with-dynamic-eptp-switching-handle_ept_violation)
  + [Step 9 - Redirecting Execution via Brea...