---
title: How Modern Design Principles Strengthen Security
url: https://zeltser.com/modern-design-security
source: Lenny Zeltser
date: 2026-04-14
fetch_date: 2026-04-15T04:44:11.768205
---

# How Modern Design Principles Strengthen Security

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

×

# How Modern Design Principles Strengthen Security

Unnecessary complexity makes products hard to maintain and hard to secure. Modern apps such as Cloudflare's EmDash and Tailscale show that designing for simplicity produces stronger security as a side effect.

![How Modern Design Principles Strengthen Security - illustration](/assets/modern-design-security.CEd44wl1_rBKJq.webp)

Every design choice in a product shapes what customers must configure, monitor, and maintain. When the software requires an operating system, someone must patch it. When authentication relies on passwords, someone must store, hash, rotate, and reset them. When extensions run with unrestricted system access, every extension author becomes a security dependency. Modern applications are showing how simpler designs can produce stronger security as a side effect.

## Every Component Is a Liability

WordPress illustrates the pattern. 90-96% of its security issues originate in plugins, according to [Patchstack](https://patchstack.com/whitepaper/state-of-wordpress-security-in-2025/) and [Wordfence](https://www.wordfence.com/blog/2025/04/2024-annual-wordpress-security-report-by-wordfence/). WordPress architecture gives every plugin unrestricted access to the entire system, so the extensibility that drove its adoption also made it difficult to secure. A malicious or exploited extension can affect the entire environment.

Software components not only add features, but also add things the customer can misconfigure, forget to update, or leave exposed. Self-hosted databases need replication setup, backup configuration, and version upgrades. Container platforms need network policies, image scanning, and cluster maintenance. The longer that component list grows, the harder it becomes to keep up.

## Design for Simplicity, Get Security

Cloudflare’s [EmDash](https://blog.cloudflare.com/emdash-wordpress/) shows how modern product design can strengthen security as a side effect. They rebuilt WordPress from scratch as a serverless CMS. The app’s architecture made it simpler to operate and harder to attack:

* **Eliminate customer-managed infrastructure.** EmDash has no PHP runtime, no customer-managed operating system, no long-running web server, and no customer-managed database. The application runs in lightweight sandboxes that spin up on demand and shut down when idle.
* **Isolate extensions and require explicit permissions.** Plugins run in isolated sandboxes and must declare the capabilities they need, such as “read:content” or “email:send.” A plugin that declares only content-reading capabilities can’t access the network or the filesystem.
* **Let the underlying platform handle patching.** The platform provider handles patching on its own schedule, with no customer-managed OS to maintain.

EmDash is new and unproven (as of this writing), and platform offloading creates its own vendor dependency. But its architecture shows what a simpler design can achieve.

Consider another example: Traditional VPN deployments require opening a port on a firewall, standing up a server, distributing credentials, and maintaining certificates. Multi-component VPN software, such as OpenVPN, added a significant attack surface on top of that operational burden.

[WireGuard](https://www.wireguard.com/) took a different approach. Rather than building a full VPN stack, it designed a tunneling protocol around radical simplicity. Its entire implementation fits in roughly 4,000 lines of kernel code, small enough for a single person to audit. It uses one fixed cryptographic suite with no cipher negotiation. Products such as [Tailscale](https://tailscale.com) build on WireGuard to create identity-based mesh networks. The customer maintains no server, no open ports, and no certificates to rotate.

## Defaults That Win

Reducing complexity removes entire categories of risk. But the components that remain still need safe defaults, because users rarely change what ships out of the box.

The most successful secure defaults don’t feel like security at all. When Microsoft [made passkeys the default](https://www.microsoft.com/en-us/security/blog/2025/05/01/pushing-passkeys-forward-microsofts-latest-updates-for-simpler-safer-sign-ins/) for new accounts, passkey sign-ins grew by 120%. The FIDO Alliance reports a [93% success rate](https://fidoalliance.org/fido-alliance-launches-passkey-index-revealing-significant-passkey-uptake-and-business-benefits/) for passkey logins compared to 63% for traditional methods. Passkeys are faster and easier to use than passwords for many people, and they happen to be phishing-resistant.

Misconfigured cloud storage buckets were among the most common sources of data breaches before AWS [made Block Public Access the default](https://aws.amazon.com/blogs/aws/heads-up-amazon-s3-security-changes-are-coming-in-april-of-2023/) for all new S3 buckets in 2023. The feature had existed since 2018, but it required customers to enable it. Changing the default eliminated an entire category of exposure.

EmDash applies the same deny-by-default approach to extensions, and even administrators who make no changes still get a secure configuration.

## Where These Principles Lead

EmDash, WireGuard, and Tailscale all followed modern design principles: They minimized components, offloaded infrastructure to platforms, and defaulted to least privilege. The security improvements emerged from those architectural decisions, not from adding controls on top.

For builders designing new products or rearchitecting existing ones, the following principles can guide the work. For existing apps, each component simplified, offloaded, or removed is one fewer thing to patch, configure, and directly defend.

**Review your component list.** For each component, whether the runtime, database, authentication system, or extensibility model, ask whether the product truly needs it. Could a platform service replace it, and does that shift reduce your overall risk? Could a different architecture eliminate it entirely?

**Default to the safest configuration.** If a user installs your product and makes no changes, it should be in a secure state. Every permission, integration, and capability should require an explicit opt-in rather than an opt-out.

**Measure what you eliminated, not just what you added.** A well-designed product makes security problems structurally impossible. If your customers configure fewer components, rotate fewer credentials, and patch fewer systems, you’ve strengthened security before adding any controls.

The design decisions that reduce what customers must manage also reduce what attackers can target. Builders who design for simplicity will find they’ve already designed for security.

Receive my blog posts by email.

Email addressSubscribe

Get posts by emailEmail addressSubscribe

Copy link

More on

[Product Management](/topic/product-management)[Security](/topic/security)

After 6+ years building the security program at [Axonius](https://www.axonius.com/) from startup to scale, I'm exploring what's next. As I work on independent projects, I'm open to CISO or security product leadership roles where technical depth enables business growth. To talk, reach out on [LinkedIn](https://www.linkedin.com/in/lennyzeltser/) or email me at *my first name* at *my last name* dot com.

4 min to read

April 14, 2026

### Related Articles

[![](/assets/designing-for-humans-and-ai.BsDuNVx0_m1WIu.webp)Designing Security Products for Humans and AI Agents](/designing-for-humans-and-ai)[![](/assets/what-platform-means-cybersecurity.DrNzij4t_xKj5k.webp)Most Cybersecurity Products Aren't Platforms and It's OK](/what-platform-means-cybersecurity)

### About the Author

Lenny Zeltser is a cybersecurity executive with deep technical roots, product management experience, and a business mindset. He has built security products and programs...