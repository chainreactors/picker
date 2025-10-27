---
title: Gmail client-side encryption: A deep dive
url: http://security.googleblog.com/2023/06/gmail-client-side-encryption-deep-dive.html
source: Google Online Security Blog
date: 2023-06-30
fetch_date: 2025-10-04T11:44:27.409638
---

# Gmail client-side encryption: A deep dive

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [Gmail client-side encryption: A deep dive](https://security.googleblog.com/2023/06/gmail-client-side-encryption-deep-dive.html "Gmail client-side encryption: A deep dive")

June 29, 2023

Nicolas Lidzborski, Principal Engineer and Jaishankar Sundararaman, Sr. Director of Engineering, Google Workspace

In February, we [expanded](https://workspace.google.com/blog/product-announcements/gmail-and-calendar-client-side-encryption) Google Workspace [client-side encryption](https://support.google.com/a/answer/10741897) (CSE) capabilities to include Gmail and Calendar in addition to [Drive, Docs, Slides, Sheets](https://workspace.google.com/blog/product-announcements/new-google-workspace-security-features), and [Meet](https://workspaceupdates.googleblog.com/2022/08/client-side-encryption-for-google-meet.html).

CSE in Gmail was designed to provide commercial and public sector organizations an additional layer of confidentiality and data integrity protection beyond [the existing encryption offered by default in Workspace](https://services.google.com/fh/files/misc/google-workspace-encryption-wp.pdf). When CSE is enabled, email messages are protected using encryption keys that are fully under the customer’s control. The data is encrypted on the client device before it’s sent to Google servers that do not have access to the encryption keys, which means the data is indecipherable to us–we have no technical ability to access it. The entire process happens in the browser on the client device, without the need to install desktop applications or browser extensions, which means that users get the same intuitive productivity and collaboration experiences that they enjoy with Gmail today. Let’s take a deeper look into how it works.

How we built Client-side Encryption for Workspace

We invented and designed a new service called, Key Access Control List Service (KACLS), that is used across all essential Workspace applications. Then, we worked directly with customers and partners to make it secure, reliable, and simple to deploy. KACLS performs cryptographic operations with encryption keys after validating end-user authentication and authorization. It runs in a customer's controlled environment and provides the key management API called by the CSE-enabled Workspace clients. We have [multiple partners](https://support.google.com/a/answer/10801691?hl=en) providing software implementations of the KACLS API that can be used by our customers.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwIro9k2FW-1D91TMmj0rHiMSOkytNdqngvne3y9r7B2GpRIOMoP3an-Ld64yKthvRyaR24SdsjJ8i4mB2ZH2BHTT-xJ8FNiVf4cnd7pbmewKn4C5s9-kWHgPgACnUXCzQ3eca1MQB--wAHNAb2qMOs44EFe141axRajX7uZ0vNU2Y-sOhqZimzX2q5tNt/w514-h241/Screenshot%202023-06-29%20at%202.25.21%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjwIro9k2FW-1D91TMmj0rHiMSOkytNdqngvne3y9r7B2GpRIOMoP3an-Ld64yKthvRyaR24SdsjJ8i4mB2ZH2BHTT-xJ8FNiVf4cnd7pbmewKn4C5s9-kWHgPgACnUXCzQ3eca1MQB--wAHNAb2qMOs44EFe141axRajX7uZ0vNU2Y-sOhqZimzX2q5tNt/s1292/Screenshot%202023-06-29%20at%202.25.21%20PM.png)

At a high level, Workspace client code takes advantage of envelope encryption to encrypt and decrypt the user content on the client with a Data Encryption Key (DEK) and leverage the KACLS to encrypt and decrypt the DEK. In order to provide separation of duty, we use the customer's OpenID Connect (OIDC) IdP to authenticate end-users and provide a JSON Web Token assertion with a claim identifying the user (3P\_JWT). For every encryption/decryption request sent to KACLS, the application (e.g. Gmail) provides a JSON Web Token assertion with a claim authorizing the current end-user operation (G\_JWT). KACLS validates these authentication and authorization tokens before returning, for example, a decrypted DEK to the user’s client device.

More details on KACLS are available in [Google Workspace Encryption Whitepaper](https://services.google.com/fh/files/misc/google-workspace-encryption-wp.pdf) and [CSE reference API](https://developers.google.com/workspace/cse/reference).

How we built CSE into Gmail

Google Workspace Engineering teams have been hard at work over multiple years to deliver to our customers the ability to have their data protected with client-side encryption. This journey required us to work closely with customers and partners to provide a capability that was secure, easy to use, intuitive and easily deployable. It was also important for CSE to work seamlessly across the Workspace products: you can create a Meet CSE scheduled meeting in Calendar CSE and follow-up with Gmail CSE emails containing links to Drive CSE files.

Client-side encryption in Gmail was built with openness and interoperability in mind. The underlying technology being used is S/MIME, an open standard for sending encrypted messages over email. S/MIME is already supported in most enterprise email clients, so users are able to communicate securely, outside of their domain, regardless of what provider the recipient is using to read their mail, without forcing the recipients to log into a proprietary portal. S/MIME uses asymmetric encryption. The public key and the email of each user are included in the user's S/MIME certificate. Similarly to TLS used for HTTPS, each certificate is digitally signed by a chain of certificate authorities up to a broadly trusted root certificate authority. The certificate acts as a virtual business card, enabling anyone getting it to encrypt emails for that user. The user's private keys are kept secure under customer control and are used by users for decryption of incoming emails and digital signature of outgoing emails.

We decided to leverage the CSE paradigm used for Drive CSE and not keep the private key on the device, to keep them as safe as possible. Instead, we extended our KACLS API to support asymmetric encryption and signature operations. This enables our customers to centrally provision and enable S/MIME, on the KACLS, for all their users without having to deploy certificates individually to each user device.

CSE in Gmail uses the end-user's client existing cryptographic functionalities (Web Crypto API for web browsers for instance) to perform local encryption operations and run client-side code to perform all S/MIME message generation.

Now let's cover the detailed user flows:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYn35d043ggs8OYGxPfce5HftN_YwiIXnotQ0M7GQ3mojQVaKfIswH0GWKNht6BGYQHiD5V62kfT2SyxmvxEkte54Cw-n-swTKehTax5_3XndDwt8zZZuDs37fcYwsZZhSBFceySXgDbMMizrHhMUytTzGkviDeGRAnCLo7sUqxK0ylrdO-tGkuRwmyyzY/w546-h355/Screenshot%202023-06-29%20at%202.26.22%20PM.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiYn35d043ggs8OYGxPfce5HftN_YwiIXnotQ0M7GQ3mojQVaKfIswH0GWKNht6BGYQHiD5V62kfT2SyxmvxEkte54Cw-n-swTKehTax5_3XndDwt8zZZuDs37fcYwsZZhSBFceySXgDbMMizrHhMUytTzGkviDeGRAnCLo7sUqxK0ylrdO-tGkuRwmyyzY/s1452/Screenshot%202023-06-29%20at%202.26.22%20PM.png)

When sending an email, the Gmail client generates a MIME message, encrypts the message with a random Data Encryption Key (DEK) then uses the recipients' public keys to encrypt the DEK, calls KACLS (with the user authenticated by customer's IdP and authorized by Google) to digitally sign content and finally sends the authenticated and encrypted S/MIME message, which contains both the encrypted email and the encrypted DEK, to Google servers for delivery to the recipients. Below is an animated screenshot showing the user interface of Gmail when using CSE.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhm3Q7zYdbWtToyiVpjUmRl1npqIVOSqMA37jHcTZY8-5kiGY9bB6u54gzEIrk8kEQlb4E141oEFfuKlfG3T8TTLbAMjXfzr9tA6...