---
title: How the Chrome Root Program Keeps Users Safe
url: http://security.googleblog.com/2023/05/how-chrome-root-program-keeps-users-safe.html
source: Google Online Security Blog
date: 2023-05-24
fetch_date: 2025-10-04T11:37:52.214521
---

# How the Chrome Root Program Keeps Users Safe

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [How the Chrome Root Program Keeps Users Safe](https://security.googleblog.com/2023/05/how-chrome-root-program-keeps-users-safe.html "How the Chrome Root Program Keeps Users Safe")

May 23, 2023

Posted by Chrome Root Program, Chrome Security Team

### **What is the Chrome Root Program?**

A root program is one of the foundations for securing connections to websites. The Chrome Root Program was [announced](https://blog.chromium.org/2022/09/announcing-launch-of-chrome-root-program.html) in September 2022. If you missed it, don’t worry - we’ll give you a quick summary below!

### **Chrome Root Program: TL;DR**

Chrome uses [digital certificates](https://en.wikipedia.org/wiki/Public_key_certificate) (often referred to as “certificates,” “HTTPS certificates,” or “server authentication certificates”) to ensure the connections it makes for its users are secure and private. Certificates are issued by trusted entities called “[Certification Authorities](https://en.wikipedia.org/wiki/Certificate_authority)” (CAs). The collection of digital certificates, CA systems, and other related online services is the foundation of [HTTPS](https://web.dev/why-https-matters/) and is often referred to as the “Web PKI.”

Before issuing a certificate to a website, the CA must verify that the certificate requestor legitimately controls the domain whose name will be represented in the certificate. This process is often referred to as “domain validation” and there are several methods that can be used. For example, a CA can specify a random value to be placed on a website, and then perform a check to verify the value’s presence. Typically, domain validation practices must conform with a set of security requirements described in both industry-wide and browser-specific policies, like the CA/Browser Forum “[Baseline Requirements](https://cabforum.org/baseline-requirements-documents/)” and the Chrome Root Program [policy](https://g.co/chrome/root-policy).

Upon connecting to a website, Chrome verifies that a recognized (i.e., trusted) CA issued its certificate, while also performing additional evaluations of the connection’s security properties (e.g., validating data from [Certificate Transparency](https://certificate.transparency.dev/) logs). Once Chrome determines that the certificate is valid, Chrome can use it to establish an encrypted connection to the website. Encrypted connections prevent attackers from being able to intercept (i.e., eavesdrop) or modify communication. In security speak, this is known as [confidentiality](https://en.wikipedia.org/wiki/Information_security#Confidentiality) and [integrity](https://en.wikipedia.org/wiki/Information_security#Integrity).

The Chrome Root Program, led by members of the Chrome Security team, provides governance and security review to determine the set of CAs trusted by default in Chrome. This set of so-called "root certificates" is known at the [Chrome Root Store](https://chromium.googlesource.com/chromium/src/%2B/main/net/data/ssl/chrome_root_store/root_store.md).

### **How does the Chrome Root Program keep users safe?**

The Chrome Root Program keeps users safe by ensuring the CAs Chrome trusts to validate domains are worthy of that trust. We do that by:

* administering policy and governance activities to manage the set of CAs trusted by default in Chrome,* evaluating impact and corresponding security implications related to public security incident disclosures by participating CAs, and* leading positive change to make the ecosystem more resilient.

### **Policy and Governance**

The Chrome Root Program [policy](https://www.chromium.org/Home/chromium-security/root-ca-policy/) defines the minimum requirements a CA owner must meet for inclusion in the Chrome Root Store. It incorporates the industry-wide CA/Browser Forum Baseline Requirements and further adds security controls to improve Chrome user security.

The CA [application process](https://www.chromium.org/Home/chromium-security/root-ca-policy/apply-for-inclusion/) includes a public discussion phase, where members of the Web PKI community are free to raise well-founded, fact-based concerns related to an applicant on an open [discussion forum](https://www.ccadb.org/cas/public-group).

We consider public discussion valuable because it:

* improves security, transparency, and interoperability, and* highlights concerning behavior, practices, or ownership background information not readily available through public audits, policy reviews, or other application process inputs.

For a CA owner’s inclusion request to be accepted, it must clearly demonstrate that the value proposition for the security and privacy of Chrome’s end users exceeds the corresponding risk of inclusion.

Once a CA is trusted, it can issue certificates for any website on the internet; thus, each newly added CA represents an additional attack surface, and the Web PKI is only as safe as its weakest link. For example, in 2011 a [compromised CA](https://www.enisa.europa.eu/media/news-items/operation-black-tulip/) led to a large-scale attack on web users in Iran.

### **Incident Management**

No CA is perfect. When a CA owner violates the Chrome Root Program policy – or experiences any other situation that affects the CA’s integrity, trustworthiness, or compatibility – we call it an incident. Incidents can happen. They are an expected part of building a secure Web PKI. All the same, incidents represent opportunities to improve practices, systems, and understanding. Our program is committed to continuous improvement and participates in a public Web PKI incident management process.

When incidents occur, we expect CA owners to identify the root cause and remediate it to help prevent similar incidents from happening again. CA owners record the incident in a report that the Chrome Root Program and the public can review, which encourages an understanding of all contributing factors to reduce the probability of its reoccurrence in the Web PKI.

The Chrome Root Program prioritizes the security and privacy of its users and is unwilling to compromise on these values. In rare cases, incidents may result in the Chrome Root Program losing confidence in the CA owner’s ability to operate securely and reliably. This may happen when there is evidence of a CA owner:

* [knowingly](https://security.googleblog.com/2016/10/distrusting-wosign-and-startcom.html) violating requirements or obfuscating incidents,* demonstrating sustained patterns of [failure](https://security.googleblog.com/2015/10/sustaining-digital-certificate-security.html), untimely and opaque communications, or an unwillingness to improve elements that are critical to security, or* performing other [actions](https://security.googleblog.com/2015/09/improved-digital-certificate-security.html) that [negatively](https://security.googleblog.com/2013/01/enhancing-digital-certificate-security.html) impact or otherwise [degrade](https://security.googleblog.com/2015/03/maintaining-digital-certificate-security.html) the [security](https://security.googleblog.com/2011/08/update-on-attempted-man-in-middle.html) of the Web.

In these cases, Chrome may distrust a CA – that is, remove the CA from the Chrome Root Store. Depending on the circumstance, Chrome may also block the certificate with a non-bypassable error page.

The above cases are only illustrative, and considerations for CA distrust are not limited to these examples. The Chrome Root Program may remove certificates from the Chrome Root Store, as it deems appropriate and at its sole discretion, to enhance security and promote interoperability in Chrome.

### **Positive Ecosystem Change**

The Chrome Root Progr...