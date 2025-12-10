---
title: Further Hardening Android GPUs
url: http://security.googleblog.com/2025/12/further-hardening-android-gpus.html
source: Google Online Security Blog
date: 2025-12-09
fetch_date: 2025-12-10T03:20:48.483096
---

# Further Hardening Android GPUs

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Further Hardening Android GPUs](https://security.googleblog.com/2025/12/further-hardening-android-gpus.html "Further Hardening Android GPUs")

December 9, 2025

Posted by Liz Prucka, Hamzeh Zawawy, Rishika Hooda, Android Security and Privacy Team

Last year, Google's Android Red Team partnered with Arm to conduct an [in-depth security analysis](https://security.googleblog.com/2024/09/google-arm-raising-bar-on-gpu-security.html?content_ref=by+focusing+on+the+arm+mali+gpu+the+android+red+team+could+assess+the+security+of+a+gpu+implementation+running+on+millions+of+android+devices+worldwide) of the Mali GPU, a component used in billions of Android devices worldwide. This collaboration was a significant step in proactively identifying and fixing vulnerabilities in the GPU software and firmware stack.

While finding and fixing individual bugs is crucial, and [progress continues on eliminating them entirely](https://www.collabora.com/news-and-blog/news-and-events/racing-karts-on-a-rust-gpu-kernel-driver.html), making them unreachable by restricting attack surface is another effective and often faster way to improve security. This post details our efforts in partnership with Arm to further harden the GPU by reducing the driver's attack surface.

## **The Growing Threat: Why GPU Security Matters**

The Graphics Processing Unit (GPU) has become a critical and attractive target for attackers due to its complexity and privileged access to the system. The scale of this threat is significant: since 2021, the majority of Android kernel driver-based [exploits](https://docs.google.com/spreadsheets/d/1lkNJ0uQwbeC1ZTRrxdtuPLCIl7mlUreoKfSIgajnSyY/view?gid=694054923#gid=694054923) have targeted the GPU. These exploits primarily target the interface between the User-Mode Driver (UMD) and the highly privileged Kernel-Mode Driver (KMD), where flaws can be exploited by malicious input to trigger memory corruption.

## **Partnership with Arm**

Our goal is to raise the bar on GPU security, ensuring the Mali GPU driver and firmware remain highly resilient against potential threats. We partnered with Arm to conduct an analysis of the Mali driver, used on approximately 45% of Android devices. This collaboration was crucial for understanding the driver’s attack surface and identifying areas that posed a security risk, but were not necessary for production use.

## **The Right Tool for the Job: Hardening with SELinux**

One of the key findings of our investigation was the opportunity to restrict access to certain GPU IOCTLs. IOCTLs act as the GPU kernel driver’s user input and output, as well as the attack surface. This approach builds on earlier kernel hardening efforts, such as those described in the 2016 post **[Protecting Android with More Linux Security](https://security.googleblog.com/2016/07/protecting-android-with-more-linux.html)**. Mali ioctls can be broadly categorized as:

* Unprivileged: Necessary for normal operation.
* Instrumentation: Used by developers for profiling and debugging.
* Restricted: Should not be used by applications in production. This includes IOCTLs which are intended only for GPU development, as well as IOCTLs which have been deprecated and are no longer used by a device’s current User-Mode Driver (UMD) version.

Our goal is to block access to deprecated and debug IOCTLs in production. Instrumentation IOCTLs are intended for use by profiling tools to monitor system GPU performance and are not intended to be directly used by applications in production. As such, access is restricted to `shell` or applications marked as `debuggable`. Production IOCTLs remain accessible to regular applications.

## **A Staged Rollout**

The approach is iterative and is a staged rollout for devices using the Mali GPU. This way, we were able to carefully monitor real-world usage and collect data to validate the policy, minimizing the risk of breaking legitimate applications before moving to broader adoption:

1. Opt-In Policy: We started with an "opt-in" policy. We created a new SELinux attribute, `gpu_harden`, that disallowed instrumentation ioctls. We then selectively applied this attribute to certain system apps to test the impact. We used the `allowxperm` rule to audit, but not deny, access to the intended resource, and monitored the denial logs to ensure no breakage.
2. Opt-Out Policy: Once we were confident that our approach was sound, we moved to an "opt-out" policy. We created a `gpu_debug` domain that would allow access to instrumentation ioctls. All applications were hardened by default, but developers could opt-out by:

* Running on a rooted device.
* Setting the `android:debuggable="true"` attribute in their app's manifest.
* Requesting a permanent exception in the SELinux policy for their application.

This approach allowed us to roll out the new security policy broadly while minimizing the impact on developers.

## **Step by Step instructions on how to add your Sepolicy**

To help our partners and the broader ecosystem adopt similar hardening measures, this section provides a practical, step-by-step guide for implementing a robust SELinux policy to filter GPU ioctls. This example is based on the policy we implemented for the Mali GPU on Android devices.

The core principle is to create a flexible, platform-level macro that allows each device to define its own specific lists of GPU `ioctl` commands to be restricted. This approach separates the general policy logic from the device-specific implementation.

Official documentation detailing the added macro and GPU security policy is available at:

SELinux Hardening Macro: [GPU Syscall Filtering](https://source.android.com/partners/android-16/security/features/gpu-syscall-filtering)

Android Security Change: [Android 16 Behavior Changes](https://developer.android.com/about/versions/16/behavior-changes-16#gpu-syscall-filtering)

## **Step 1: Utilize the Platform-Level Hardening Macro**

The first step is to use a generic macro that we built in the platform's `system/sepolicy` that can be used by any device. This macro establishes the framework for filtering different categories of ioctls.

In the file`/sepolicy/public/te_macros`, a new macro is created. This macro allows device-specific policies to supply their own lists of ioctls to be filtered. The macro is designed to:

* Allow all applications (`appdomain`) access to a defined list of unprivileged ioctls.
* Restrict access to sensitive "instrumentation" ioctls, only permitting them for debugging tools like `shell` or `runas_app` when the application is debuggable.
* Block access to privileged ioctls based on the application's target SDK version, maintaining compatibility for older applications.

#### **Step 2: Define Device-Specific IOCTL Lists**

With the platform macro in place, you can now create a device-specific implementation. This involves defining the exact `ioctl` commands used by your particular GPU driver.

1. Create an `ioctl_macros` file in your device's sepolicy directory (e.g., `device/your_company/your_device/sepolicy/ioctl_macros`).
2. Define the ioctl lists inside this file, categorizing them as needed. Based on our analysis, we recommend at least `mali_production_ioctls`, `mali_instrumentation_ioctls`, and `mali_debug_ioctls`. These lists will contain the hexadecimal `ioctl` numbers specific to your driver.

   For example, you can define your IOCTL lists as follows:

   ```
   define(`unpriv_gpu_ioctls', `0x0000, 0x0001, 0x0002')
   define(`restricted_ioctls', `0x1110, 0x1111, 0x1112')
   define(`instrumentation_gpu_ioctls', `0x2220, 0x2221, 0x2222')
   ```

Arm has provided official categorization of their IOCTLs in Docu...