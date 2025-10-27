---
title: Project 02: Root Account Monitoring with CloudTrail and SNS Alerts
url: https://attacker-codeninja.github.io/2025-07-28-Project-02-Root-Monitoring-with-Cloudtrail-and-SNS/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-29
fetch_date: 2025-10-06T23:56:36.826770
---

# Project 02: Root Account Monitoring with CloudTrail and SNS Alerts

[attacker-codeninja.github.io](https://attacker-codeninja.github.io/)

* [About Me](/aboutme)
* Search

✕

[![Main header avatar](/assets/img/code_ninja_svg.svg)](https://attacker-codeninja.github.io/)

# Project 02: Root Account Monitoring with CloudTrail and SNS Alerts

Posted on July 28, 2025

![](/assets/img/project-2-root-account-monitoring/your-header-image.png)

# 🔐 Project 2: monitoring/ AWS Root Account Activity with CloudTrail + SNS — Guided by a Security Engineer

This blog is all about - Setting Up Real-Time Alerts Like a Cloud Security Engineer

## 📌 Introduction — The Root of All Risks

Let me tell you a quick story.

When I first created my AWS account, the most powerful key I held was the **root account** - the “super admin” of everything in the cloud.

But guess what? **Using it is a bad idea.** Like really bad.

> Think of the root account like a master key to a bank vault.
> If it’s used casually, or worse - compromised - your entire cloud setup is at risk.

In this project, I wanted to learn **how to monitor AWS root account activity in real time** - and set up alerts so that if **anyone (even me)** logs in with it, I’ll know **immediately**.

Let’s dive in!

---

## 🎯 Objective

Simulate a real-world risky action:
➡️ Log in as the **root user**,
➡️ Perform a sensitive action (like disabling MFA), and
➡️ Detect that activity using:

* **CloudTrail** for logging
* **SNS** for alerts
* **CloudWatch (EventBridge)** for triggering the detection

So -> **Detect and respond to sensitive activity performed by using the AWS Root Account, which should be tightly controlled and rarely used.**

---

## ⚠️ Why is Root Account Usage a Security Red Flag?

By default, AWS allows you to create and manage your account with a **root user**, but here’s what makes it dangerous:

| 🚨 Risk | Why It’s a Problem |
| --- | --- |
| ✅ Full permissions | Can delete everything in AWS - no restrictions |
| ❌ MFA disabled | Easy target for attackers |
| 🤫 Hard to track | Used rarely, so any activity is suspicious |
| 🔥 No boundaries | Can override all IAM permissions |

So as a security engineer (even a beginner one), we **never want to use root unless absolutely necessary.**
But if someone *does* use it? That’s an event worth knowing **immediately**.

---

## 🧰 Services Used

Here’s what we’ll use to make our alert system:

| AWS Service | Purpose |
| --- | --- |
| CloudTrail | Logs every action taken in AWS |
| CloudWatch / EventBridge | Detects specific patterns (like root login) |
| SNS | Sends an alert via Email/SMS |
| IAM | Identity system (helps us know who did what) |

---

## 🛠️ Step-by-Step Setup: Root Account monitoring/ in AWS

> Don’t worry, each step includes what and *why* we’re doing it. ❤️

---

### ✅ Step 1: Simulate the Problem — Log in as Root

**Why this step?**
We want to see how CloudTrail captures this risky action.

* Go to AWS Console
* Log in **using the root account email**
* Navigate to **Billing Dashboard** or **Account Settings**
* Try to **disable MFA** (if enabled)

🧠 This simulates a “sensitive operation” - exactly what an attacker might try.

![](/assets/img/project-2-root-account-monitoring/20250728100741.png)

![](/assets/img/project-2-root-account-monitoring/20250728100836.png)

![](/assets/img/project-2-root-account-monitoring/20250728100924.png)

---

### 📝 Step 2: Enable CloudTrail (if not already)

**What is CloudTrail?**
It’s AWS’s built-in logging system.

Every time *someone does something* (login, create S3 bucket, delete EC2 instance, etc.), CloudTrail writes it down.

#### ✅ Open CloudTrail Service

* Go to the **AWS Console**, search for **“CloudTrail”** in the search bar, and click the result.
* Click **“Create trail”**.

#### 📝 Configure the Trail:

* **Trail name:** I named it **RootActivityTrail** to clearly reflect its purpose.
* You may **not see options to choose Management/Event types or enable for all regions**, because CloudTrail **does this automatically now** during the setups.

  + ✅ CloudTrail **enabled Multi-region trail** by default - so activity in *all* AWS regions will be captured.
  + ✅ CloudTrail also **created a dedicated S3 bucket** to store logs (you’ll see its name under the “S3 bucket” column later).

💡 **Important Note:**

> When I tried this, I didn’t even need to create the S3 bucket manually. AWS CloudTrail smartly created a bucket named something like:
>
> **aws-cloudtrail-logs-677604542474-fdc96c6b**

This automatic bucket creation makes life easier - especially for beginners!

✅ Done. Now, every action - including root login - will be logged.

![](/assets/img/project-2-root-account-monitoring/20250728101102.png)

![](/assets/img/project-2-root-account-monitoring/20250728101124.png)

![](/assets/img/project-2-root-account-monitoring/20250728101220.png)

![](/assets/img/project-2-root-account-monitoring/20250728101315.png)

![](/assets/img/project-2-root-account-monitoring/20250728101935.png)

So this step was about **turning on the security cameras** (CloudTrail) and **pointing them at the most sensitive area** (root account actions).

If anyone uses the root account - whether it’s you or someone malicious - we’ll **catch it immediately** in our logs.

---

### 🔔 Step 3: Set Up SNS — Our Alerting System

**Why SNS?**
SNS (Simple Notification Service) can send alerts to email or SMS.

* Go to **SNS → Topics → Create Topic**

  + **Name:** **RootLoginAlerts**
  + In the **“Create topic”** screen:
* ✅ **Type**: Choose **Standard** (default)

  + Best-effort ordering
  + At-least once message delivery
  + Supports multiple protocols like Email, Lambda, SQS
* 🧠 *Why not FIFO?*
  FIFO topics are mainly for ordering and deduplication in SQS - unnecessary for notifications. Standard gives us flexibility for email alerts.
* Right now, your SNS topic doesn’t know **where** to send the alert. We need to **subscribe your email address** so you get notified instantly when the root account logs in.
* Click on the topic → **Create subscription**

  + **Protocol:** Email
  + **Endpoint:** Your personal email
* Check your inbox and **confirm the subscription**

📧 Now you’re ready to receive alerts.

![](/assets/img/project-2-root-account-monitoring/20250728102322.png)

![](/assets/img/project-2-root-account-monitoring/20250728102418.png)

![](/assets/img/project-2-root-account-monitoring/20250728102728.png)

![](/assets/img/project-2-root-account-monitoring/20250728103059.png)

![](/assets/img/project-2-root-account-monitoring/20250728103043.png)

![](/assets/img/project-2-root-account-monitoring/20250728103249.png)

![](/assets/img/project-2-root-account-monitoring/20250728103342.png)

![](/assets/img/project-2-root-account-monitoring/20250728103355.png)

![](/assets/img/project-2-root-account-monitoring/20250728103412.png)

![](/assets/img/project-2-root-account-monitoring/20250728103427.png)

> Though i used temp email but you need to use proper active email as you will get a confirmation link you **must** click before alerts start coming.

### 🔐 Why This Step Is Critical for Security

Just logging a root user login event isn’t enough. **You need to be notified immediately**, in case it wasn’t you.

Real-world misconfig:

> Many engineers set up CloudTrail and even an SNS Topic, but **forget to subscribe an endpoint**. So when root login happens, they never find out.

We’re not making that mistake. 😉 You’ll get alerted within seconds of a root login.

---

### 📡 Step 4: Create CloudWatch Rule (EventBridge)

We now tell AWS:
**“If anyone logs in using the root user, send me an alert.”**

First, Let’s know about CloudWatch and EventBridge

#### 🤔 CloudWatch vs EventBridge — What’s the Deal?

If you’re confused about where to create the alert rule — whether in **CloudWatch** or **EventBridge** - you’re not alone.

Here’s the truth in simple terms:

> **EventBridge is the upgraded version of CloudWatch Events.**

You’ll still hear a lot of tutorials and documentation saying:

> “Create a CloudWat...