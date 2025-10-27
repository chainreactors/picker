---
title: Best Practices for SmartScreen AppRep
url: https://textslashplain.com/2024/11/15/best-practices-for-smartscreen-apprep/
source: text/plain
date: 2024-11-16
fetch_date: 2025-10-06T19:17:33.468008
---

# Best Practices for SmartScreen AppRep

[Skip to content](#content)

[text/plain](https://textslashplain.com/)

ericlaw talks about security, the web, and software in general

# Best Practices for SmartScreen AppRep

Posted by[ericlaw](https://textslashplain.com/author/ericlaw1979/)[2024-11-152025-03-10](https://textslashplain.com/2024/11/15/best-practices-for-smartscreen-apprep/)Posted in[security](https://textslashplain.com/category/security/), [tech](https://textslashplain.com/category/tech/)Tags:[Authenticode](https://textslashplain.com/tag/authenticode/), [best-practices](https://textslashplain.com/tag/best-practices/), [Defender](https://textslashplain.com/tag/defender/), [SmartScreen](https://textslashplain.com/tag/smartscreen/), [Windows](https://textslashplain.com/tag/windows/)

Last year, I wrote about [how Windows integrates SmartScreen Application Reputation](https://textslashplain.com/2023/08/23/smartscreen-application-reputation-in-pictures/) to help ensure users have a secure and smooth experience when running downloaded software.

*tl;dr:* When a user runs a downloaded program, a call to SmartScreen’s web-based reputation service is made, and four possible outcomes can occur:

1. **“Known Good”** SmartScreen’s Web Service indicates that the file is “Known safe”, and the program runs without prompting.
2. **“Known Bad”** SmartScreen’s Web Service indicates that the file is “Known malicious”, and the user is blocked from running the software via a red warning dialog.
3. **“Unknown”** SmartScreen’s Web Service indicates that the file is “Unknown,” and the user is interrupted from running the software via a blue confirmation dialog.
4. “**Offline”:** SmartScreen’s Web Service is offline or unreachable and the user sees a notice that SmartScreen cannot help decide whether the software is safe to run. The user sees a blue confirmation dialog.

As a software developer, it’s natural that you’ll want to have your apps classified as “Known Good” to streamline the installation of your software.

This post explores how to achieve that.

### Building Positive Reputation

The Application Reputation service builds reputation based on individual file hashes (SHA256) *and/or* the certificates used to [sign those files](https://textslashplain.com/tag/authenticode/). The following are best practices we recommend.

#### Sign Your Files

Because any update to a file changes its hash, this means that new files that are unsigned have no reputation by default. To avoid triggering warnings after every update, be sure to **sign your software using an Authenticode certificate**.

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-12.png?w=961)](https://www.digicert.com/faq/code-signing-trust/what-is-code-signing)

Because your certificate can be used to sign files for years, it will [accumulate reputation](https://www.microsoft.com/en-us/security/blog/2018/08/16/partnering-with-the-industry-to-minimize-false-positives/#:~:text=Keep%20good%20reputation) that will accrue to files you sign in the future. To maximize reputation data, you should aim to **use the same certificate for as long as possible**. Certificates periodically expire, however, and you may find that when you being using a new certificate if must build reputation again.

To help ensure that all of your good reputation accrues in one place, try to **sign everything with a single certificate** (e.g. do not use a different certificate for each product, or a different certificate for each of your company’s divisions, or anything like that).

From ~2013 to ~2019, all files signed by an Extended Validation Authenticode Certificate [were given a “positive” reputation by default](https://www.microsoft.com/en-us/security/blog/2018/08/16/partnering-with-the-industry-to-minimize-false-positives/?msockid=39cdc11345396a5823f1d22d41396c93#:~:text=At%20the%20time%20this%20post%20was%20written), but **EV certificates are no longer treated specially** — every certificate must build reputation individually.

#### Sign *All* Files

Beyond `.exe` and `.dll` files, you can also sign `.msi` Installers, script files (PowerShell, VBScript, JavaScript), and `.cab` Archives.

While SmartScreen only checks the reputation of the *main*file that the user executes (aka its “entry point”), you should **sign all files**to help protect them from tampering, and to ensure your app works correctly when [Win](https://support.microsoft.com/en-us/topic/what-is-smart-app-control-285ea03d-fa88-4d56-882e-6698afdb7003)[d](https://textslashplain.com/2016/04/04/downloads-and-the-mark-of-the-web/#:~:text=Smart%20App%20Control%20is%20enabled)[ows 11’s Smart App Control](https://support.microsoft.com/en-us/topic/what-is-smart-app-control-285ea03d-fa88-4d56-882e-6698afdb7003) feature is enabled. The Windows 11 Smart App Control feature goes further than SmartScreen and evaluates trust/signatures of *all* code that is *loaded* by the Windows OS Loader and script engines.

**NOTE:** [Smart App Control’s signature check](https://learn.microsoft.com/en-us/windows/apps/develop/smart-app-control/code-signing-for-smart-app-control) does not currently support ECC signatures.

#### Always Follow the Objective Criteria

Ensure that everything you install follows Microsoft’s [Objective Criteria for well-behaved software](https://learn.microsoft.com/en-us/defender-xdr/criteria). Adherence to the criteria ensures that users will not be surprised or upset about the behavior of your software.

Violations of the objective criteria can cause SmartScreen, Microsoft Defender, and 3rd-party security products to treat your app as Malware or Potentially Unwanted Software.

### Escalations

If your software is blocked by the red “known bad” dialog box:

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-10.png?w=573)](https://textslashplain.com/wp-content/uploads/2024/11/image-10.png)

… you should investigate to determine whether anything unexpected is included; for instance, was malware injected into your product by [a supply-chain attack](https://www.fortinet.com/resources/cyberglossary/solarwinds-cyber-attack)? You should upload your files to [VirusTotal.com](https://virustotal.com) and what, if any, detections occur across the universe of security products. If you cannot find any indications of compromise, report the potential false-positive to Microsoft Security Intelligence by [uploading your files to the WDSI portal](https://www.microsoft.com/en-us/wdsi/filesubmission).

If your software is blocked by the blue “unknown” dialog box:

[![](https://textslashplain.com/wp-content/uploads/2024/11/image-11.png?w=536)](https://textslashplain.com/wp-content/uploads/2024/11/image-11.png)

… don’t despair. Ensure that you’ve followed the best practice of signing your software with a certificate, and then just wait. As your software gets downloaded by more users around the world (“increasing prevalence”), its honorable behavior will be noted and eventually its reputation will move into the “Known good” category.

### Bypass for Enterprises

Some enterprises build and distribute their own software internally and wish to avoid SmartScreen prompts for their applications. For security reasons, you ***can and should*** still sign internally-developed software. However, internally-developed software might never be used broadly enough to organically build a positive reputation within the SmartScreen Service.

*Note: Microsoft Defender for Endpoint customers might reasonably expect that creating an [Allow Indicator for a certificate](https://learn.microsoft.com/en-us/defender-endpoint/indicators-overview#certificate-indicators) would allow files signed by that certificate to bypass SmartScreen AppRep. This is a* reasonable *expectation, but unfortunately does not presently work (as of November 2024).*

Enterprises are in control of how their users get software, and most internal software deployment systems do not result in SmartScreen checks. Only software downloaded by web browsers or cop...