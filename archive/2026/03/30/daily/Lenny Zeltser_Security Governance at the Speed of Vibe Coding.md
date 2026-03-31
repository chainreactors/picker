---
title: Security Governance at the Speed of Vibe Coding
url: https://zeltser.com/security-governance-vibe-coding
source: Lenny Zeltser
date: 2026-03-30
fetch_date: 2026-03-31T04:37:34.593557
---

# Security Governance at the Speed of Vibe Coding

[Lenny Zeltser](/)Security builder & leader

 [Projects](/projects) [Writing](/writing) [About](/about)

# Security Governance at the Speed of Vibe Coding

Vibe-coded apps now reach production without security review, dependency scanning, or organizational oversight, built by employees who've never written code. The SaaS and DevOps transitions give security teams a starting governance approach that works at this speed.

![Security Governance at the Speed of Vibe Coding - illustration](/assets/security-governance-vibe-coding.BzY_RmG2_FNgvO.webp)

Employees outside engineering now build their own apps using AI coding tools. Developers who use AI for vibe coding present their own governance challenges, but the gap is widest when the builders have no software engineering background at all.

Security leaders have navigated comparable shifts before, though none moved this fast. When SaaS removed IT’s role as gatekeeper for software procurement, it took us years to figure out a reasonable governance approach. We ran into similar challenges when DevOps became the way to deploy software. Those lessons give us a starting point for governing vibe coding by non-engineers, even if the timeline to act is shorter.

## The SaaS transition offers a governance playbook.

Let’s say a marketing analyst uses AI to build an interactive dashboard that consolidates campaign data and surfaces insights. Or a finance team member creates a reconciliation tool that saves hours of manual work. These are the business outcomes we want, and security governance should make them safer, not slower.

During the SaaS adoption wave, we realized that saying “yes, with these guardrails” gave us influence over how adoption happened. We created [discovery workflows, vendor review tiers, and procurement processes](/untangling-saas-complexity) that offered visibility without unnecessary friction. Security teams that didn’t adapt became disconnected from what was running in production.

Most organizations haven’t built equivalent mechanisms for vibe coding. No wonder that [Retool’s 2026 report](https://retool.com/blog/ai-build-vs-buy-report-2026) found that 60% of respondents built software outside IT oversight in the past year. Without discovery workflows or other forms of oversight over AI-built tools, we face the same blind spot we had with early SaaS, but with apps that pop up much faster.

## Vibe-coded apps create challenges SaaS governance didn’t address.

SaaS governance required solving SSO integration, user provisioning, vendor security reviews, and decommissioning. While these controls still apply to vibe-coded software, they’re not enough. We need to address:

**Orphaned code at scale:** When the person who built a vibe-coded app changes roles or leaves, the app loses its owner. Unlike SaaS, where the vendor maintains the product, these apps usually lack the support structure or personnel. They sit in production, accumulating tech debt, with no one responsible for patching, updating, or retiring them. The risk extends beyond security, since a business process that depends on an unmaintained tool is an operational liability.

**A confidence-competence gap:** [Stanford researchers](https://arxiv.org/html/2211.03622v3) found that developers using AI assistants wrote less secure code while rating their own output as more secure. The people who trusted AI the most produced the worst security outcomes. Non-developers building apps with AI have even less ability to design and implement with security, reliability, and maintainability in mind.

**No security input in the creation process:** SaaS vendors typically involve security experts and undergo third-party testing. Apps vibe-coded by employees skip every traditional security practice, including threat modeling, code review, and dependency scanning. Not surprisingly, when [escape.tech scanned 5,600 live vibe-coded apps](https://escape.tech/state-of-security-of-vibe-coded-apps), they found hundreds of vulnerabilities and exposed secrets.

**Unmanaged hosting environments:** Traditional software, including SaaS, runs on managed, secured, and monitored infrastructure. Vibe-coded apps often end up on platforms like Replit that the organization hasn’t vetted and doesn’t monitor.

Classic governance approaches assume someone vetted the vendor, reviewed the code, maintains the software, or manages the infrastructure. Vibe-coded apps invalidate all four assumptions at once.

## Security adapted to DevOps velocity. We can adapt again.

The challenges above look overwhelming, but security teams have adapted to comparable shifts before.

When continuous deployment became mainstream, we wondered how we’d keep up. Zane Lackey and Rebecca Huehls [made the case](https://www.oreilly.com/library/view/building-a-modern/9781492044680/) that security teams had to abandon the gatekeeper mentality. As Etsy’s first CISO, Zane saw developers deploying code dozens of times a day, which was uncommon at the time. His team [learned](https://material.security/resources/from-hacker-to-ciso-to-founder-a-conversation-with-signal-sciences-zane-lackey) that the same velocity that overwhelmed traditional reviews let them patch vulnerabilities in minutes instead of waiting for quarterly releases. Catching and fixing problems fast was better than trying to prevent every issue before deployment.

Vibe coding demands a similar shift. Pre-approval gates don’t work when non-developers build apps outside traditional workflows. We need guardrails embedded into the way people already operate and visibility to spot what slips through.

## Govern through guardrails, not gates.

Governing vibe-coded apps requires a single owner with authority across IT, security, legal, and privacy. Without that, apps that fall between team jurisdictions get no oversight at all. With ownership in place, security teams can adapt governance principles from SaaS oversight and DevOps, starting with visibility and building toward automated controls:

**Discover and catalog vibe-coded tools:** We can’t expect employees to register their apps on their own. Automate discovery through network monitoring, endpoint agents, and platform-level reporting from approved hosting environments, starting with what current tools can already surface. Aim for the inventory to capture what data each tool accesses, where it runs, what permissions it has, and who owns it.

**Prepare for orphaned apps:** Design the app inventory to track who built each app and when it was last updated. Build a process to flag apps for review when their builders change roles or leave, so someone can inherit or retire them before they become unpatched liabilities. Without owners to enforce decommissioning, apps that [fall between team jurisdictions](/distribute-cybersecurity-tasks) will get no oversight.

**Use tiered governance:** Not every vibe-coded tool carries the same risk. A dashboard that visualizes public marketing data needs less oversight than a tool that processes financial records. As new apps enter the inventory, classify them by the data they access and the infrastructure they touch. Low-risk apps get basic cybersecurity support, while sensitive-data activities require pairing with security or IT experts.

**Automate security scanning for AI-generated code:** Non-developers won’t run security tools on their own, so the tools need to run without them. Build dependency scanning, secret detection, and permission constraints into the platforms employees already use to create and deploy their apps.

**Control access to company data:** When vibe-coded apps connect to internal resources, the organization controls the authentication. Aim to provide scoped OAuth tokens instead of broad API keys so each app can access only the data it needs, regardless of where it runs.

Vibe coding won’t give us the years we had when adapting to SaaS and DevOps. Security leaders who act now will [calibrate acceptable insecurity](/chief-insecurity-officer)...