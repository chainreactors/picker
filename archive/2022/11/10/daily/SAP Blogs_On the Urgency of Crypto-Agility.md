---
title: On the Urgency of Crypto-Agility
url: https://blogs.sap.com/2022/11/09/on-the-urgency-of-crypto-agility/
source: SAP Blogs
date: 2022-11-10
fetch_date: 2025-10-03T22:14:41.627557
---

# On the Urgency of Crypto-Agility

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* On the Urgency of Crypto-Agility

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47268&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [On the Urgency of Crypto-Agility](/t5/application-development-and-automation-blog-posts/on-the-urgency-of-crypto-agility/ba-p/13564892)

![anselme_kemgnetueno](https://avatars.profile.sap.com/a/5/ida527150fe8cd0a5d7bb0edcd215b8382f747e003580baf6198003d7ffd7b4470_small.jpeg "anselme_kemgnetueno")

![Associate](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Associate")
[anselme\_kemgnetueno](https://community.sap.com/t5/user/viewprofilepage/user-id/673049)

Associate

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47268)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47268)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13564892)

‎2022 Nov 09
11:45 PM

[5
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47268/tab/all-users "Click here to see who gave kudos to this post.")

1,481

* SAP Managed Tags
* [Security](https://community.sap.com/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

* [Security

  Topic](/t5/c-khhcw49343/Security/pd-p/49511061904067247446167091106425)

View products (1)

Cryptography prevents unauthorized people from reading private messages and therefore helps us protect our digital data, be it in transit, at rest, or even during computation. Using a key, a crypto-schema transforms a clear text into a ciphertext that reveals nothing about the initial clear text. Encryption schemas are secure as long as no one has detected an attack. This situation may evolve over time, or new algorithms may be introduced that are more efficient or offer new features. As such, standards and regulations may require replacing old algorithms or adding new ones in the existing ecosystem, which has historically led to time-consuming and challenging migrations. The solution is crypto-agility, which is about having applications relying on cryptography to be (crypto-)agile. Crypto-agility is the ability of an IT system to rapidly migrate to new cryptographic algorithms and standards in a sustainable and swift way [2]. As with software vulnerabilities, it should be possible to quickly update existing software, when encryption schemas are likely to become obsolete in the foreseeable future. To understand what this means, it is essential to understand what the problem with cryptography is.

**The basic principles**

Cryptography is the last line of defense against data breaches. It designs and analyses encryption and hash algorithms that ensure IT security goals such as confidentiality, integrity, and authentication. When all other security measures have failed, cryptography provides the last barrier that protects company secrets against unauthorized access. There are symmetric (aka shared-key schemas) and asymmetric (aka public-key) schemas. Both have advantages and disadvantages such that in real-world settings they are used in a hybrid way: slower public-key schemas allow keys to be exchanged, over an insecure channel, which are then used for faster symmetric encryption of the communication. Public-key schemas base their security on mathematical problems that are difficult to solve on a computer. Since its invention in the mid-1970s, public-key cryptography has been relying on two problems, namely **prime-factorization** (see Figure 1), and **discrete logarithm** (see Figure 2). Even after several decades of cryptanalysis, their security against classical computers has not been significantly affected.

![](/legacyfs/online/storage/blog_attachments/2022/11/Figure-1-1.png)

Figure 1: Factorization Problem

![](/legacyfs/online/storage/blog_attachments/2022/11/Figure-2.png)

Figure 2: Discrete Logarithm Problem

**The crypto-apocalypse problem**

In 1994, American mathematician Peter Shor published an efficient quantum algorithm that finds the prime factors or the discrete logarithm of any integer. When quantum computers become powerful enough to run Shor’s algorithm for commonly used key lengths, cryptographic schemas that rely on the difficulty of prime-factorization or discrete-logarithm will be broken. Public-key cryptography, however, is present in a multitude of applications. It has an impact on the Internet, e-mail, key management, secure shell, virtual private networks, distributed ledgers, code signing, and basically any scenario that requires security goals such as confidentiality, authenticity, integrity, etc. Today, the Internet enables 4.1 billion users to visit 2 billion websites and generates $3 trillion in retail activity while relying on public-key cryptographic standards to ensure our privacy and the security of our data [2]. That is, a large-scale quantum computer represents an apocalyptic cybersecurity threat to our IT infrastructure. Current schemas need to be replaced by other schemas not basing their security on integer factorization (Figure 1) and discrete logarithms (Figure 2).

![](/legacyfs/online/storage/blog_attachments/2022/11/Figure-3.png)

Figure 3: Post-Quantum Crypto-Families

**The NIST Counterattack**

As a reaction to the quantum threat on cryptography; in 2016 the National Institute of Standards and Technology (NIST) initiated a process to solicit, evaluate, and standardize quantum-resistant public-key cryptographic algorithms [4]. In its call for proposals, NIST requested schemas that implement one or more of the following functionalities: public-key encryption, key encapsulation mechanisms (KEM), and digital signatures. The cryptography community is now investigating what is called **Post-Quantum Cryptography** (PQC) [4, 10]. PQC relies on different math problems (see Figure 3) and provides encryption schemas that run on conventional computers and are believed to be secure against attacks from both classical and quantum computers. Such schemas are therefore called **quantum-safe**, **quantum-resistant**, or **post-quantum**. Based on previous standardization processes for Advanced Encryption Standard (AES) or Secure Hash Algorithm (SHA), NIST’s goal is to select quantum-safe schemas to replace current schemas that are vulnerable to quantum attacks.

Bruce Schneir [1], a renowned cryptographer, compares the NIST process to a demolition derby consisting of a few rounds each lasting a few years. Participants put their algorithms into the ring and then beat each other’s schemas in each rou...