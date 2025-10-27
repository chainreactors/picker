---
title: Project 01: Securing Your First S3 Bucket & IAM User
url: https://attacker-codeninja.github.io/2025-07-27-Project-01-S3-IAM-Security/
source: Over Security - Cybersecurity news aggregator
date: 2025-07-28
fetch_date: 2025-10-06T23:22:01.615111
---

# Project 01: Securing Your First S3 Bucket & IAM User

[attacker-codeninja.github.io](https://attacker-codeninja.github.io/)

* [About Me](/aboutme)
* Search

✕

[![Main header avatar](/assets/img/code_ninja_svg.svg)](https://attacker-codeninja.github.io/)

# Project 01: Securing Your First S3 Bucket & IAM User

Posted on July 27, 2025

![Securing Your First S3 Bucket Project](/assets/img/s3-iam-project/your-header-image.png)

## 🔐 Project 1: Securing Your First S3 Bucket & IAM User — Guided by a Security Engineer

> *A Beginner’s Journey into S3 Security and IAM - Guided by a Security Engineer*

### 🎯 **Objective**

> **Help beginners understand how simple misconfigurations in S3 buckets and IAM policies can expose sensitive data - and how to fix them securely.**

As a Security Engineer, I’ve seen how frequently these issues occur in real-world environments.

In this project, I will walk you through intentionally misconfiguring an S3 bucket to simulate a common security mistake, and then fixing it step by step - just like I would in a real audit.

---

### 🧰 Tools You’ll Use

* ✅ AWS Console (GUI)
* ✅ Amazon S3
* ✅ AWS IAM
* ✅ AWS CLI *(Optional – for those wanting to level up)*

---

## 🔧 What We’ll Do

You’ll simulate a real-world misconfiguration:

* An S3 bucket made public (accidentally or lazily)
* An IAM user given broad permissions (think: intern with admin rights 😬)

Then, you’ll **detect**, **fix**, and **harden** the setup using:

* IAM best practices (least privilege)
* Secure S3 bucket policies
* Logging for audit trails

---

## 🧠 Why This Project Matters

> **“S3 bucket leaks are a cloud security engineer’s worst recurring nightmare.”**
> Misconfigured buckets have exposed sensitive data from startups to Fortune 500s. Why? Because it’s **easy to get wrong**, and **hard to notice** until someone tweets it.

Same with IAM users:

> Giving full access without restriction is like giving keys to your house to someone who just asked where the bathroom is.

So let’s **learn to break it**, **spot the danger**, and then **secure it like a pro**.

---

# 🚀 Step-by-Step Implementation

### 🛠️ Step-by-Step Guide

> Think of this as a **security lab exercise** - we simulate the misconfiguration, then fix it, all while learning key IAM and S3 security concepts

### ✅ Step 1: Create an S3 Bucket

📌 Bucket Name: `your-name-cloudsec-demo`

✅ Go to **S3 → Create bucket**
✅ Name it something like: `aakash-cloudsec-demo`
✅ Use default region (or choose one you prefer)
✅ **Disable block all public access** *(this is the misconfiguration step we’ll fix later)*
✅ Keep default settings → Create bucket

🔒 **Security Insight:**

Disabling public access is dangerous unless you **really** need public files. Many data leaks happen this way.

📌 NOTE: **S3 Buckets are global-named. Use a unique name.**

![](/assets/img/s3-iam-project/20250727164102.png)

![](/assets/img/s3-iam-project/20250727161740.png)

![](/assets/img/s3-iam-project/20250727162652.png)

![](/assets/img/s3-iam-project/20250727162739.png)

![](/assets/img/s3-iam-project/20250727173343.png)

![](/assets/img/s3-iam-project/20250727173409.png)

---

### ✅ Step 2: Upload a Sample Sensitive File

📄 File Name: `sensitive.txt`
📝 Content: You can add something like:

```
Internal Project Credentials:
DB_USERNAME=admin
DB_PASSWORD=123456
```

✅ Upload it to the bucket under **Objects → Upload**.

**aakash-cloudsec-demo** -> this is your object

![](/assets/img/s3-iam-project/20250727174208.png)

![](/assets/img/s3-iam-project/20250727174239.png)

![](/assets/img/s3-iam-project/20250727174320.png)

![](/assets/img/s3-iam-project/20250727174337.png)

![](/assets/img/s3-iam-project/20250727174402.png)

---

### ✅ Step 3: Make the Bucket Public (Simulate Misconfiguration)

> 🎯 Simulating what often goes wrong in the real world

* Go to the bucket → **Permissions tab**
* Scroll down to **Bucket Policy**
* Paste the following policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicRead",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::aakash-cloudsec-demo/*"
    }
  ]
}
```

This means:

* ✅ Anyone (`"Principal": "*"`) on the internet can `GetObject` - i.e., **download** files from this bucket.
* ✅ The access is for **all objects** (`/*`) inside the bucket

✅ Save policy
✅ Try opening the file in **public browser tab** - You’ll see it’s now accessible without login.

#### Before ->

![](/assets/img/s3-iam-project/20250727174824.png)

or

![](/assets/img/s3-iam-project/20250727174855.png)

When Open this file in browser ->

![](/assets/img/s3-iam-project/20250727174928.png)

#### NOW ->

![](/assets/img/s3-iam-project/20250727175017.png)

![](/assets/img/s3-iam-project/20250727175113.png)

![](/assets/img/s3-iam-project/20250727175125.png)

Now able to see in public ->

![](/assets/img/s3-iam-project/20250727175222.png)

> This simulates how even a small policy mistake can expose private files.
> In real-life, attackers often scan for such misconfigured buckets

**AWS honors this policy** because there’s no block in place - i.e -> **Block All Public Access is DISABLED**

##### What happen if -> **Block All Public Access is ENABLED** ?

even if your **bucket policy says “Allow public access”**, AWS will **block it anyway**.

In short:

* ❌ Public policy is **ignored** which we set earlier
* ❌ File becomes **inaccessible**
* 🔐 Even though the policy *says* “Allow anyone,” the **block setting overrides it**

##### 🔒 Behind the Scenes (What AWS Does)

When **Block Public Access is enabled**, AWS does these enforcement-level things:

* Rejects any **new bucket policies** that try to allow `"Principal": "*"`
* Ignores **existing public policies** when evaluating access
* Blocks **ACL-based public grants** (like `AllUsers`, `AuthenticatedUsers`)
* Ensures **cross-account public access** is also blocked unless explicitly allowed

---

### ✅ Step 4: Create an IAM User – `junior-analyst`

✅ Go to IAM → Users → Add User
✅ Username: `junior-analyst`
✅ Access Type: **Programmatic Access** (CLI access)
✅ Attach **S3FullAccess** managed policy temporarily
✅ Download the credentials

🛡️ **Security Insight:** Giving full access to S3 is too much! We’ll restrict it soon.

![](/assets/img/s3-iam-project/20250727180343.png)

![](/assets/img/s3-iam-project/20250727180423.png)

![](/assets/img/s3-iam-project/20250727180447.png)

![](/assets/img/s3-iam-project/20250727180711.png)

![](/assets/img/s3-iam-project/20250727180805.png)

![](/assets/img/s3-iam-project/20250727180832.png)

![](/assets/img/s3-iam-project/20250727180849.png)

![](/assets/img/s3-iam-project/20250727180938.png)

![](/assets/img/s3-iam-project/20250727181205.png)

![](/assets/img/s3-iam-project/20250727181245.png)

❌ Why This Is a Security Problem ?

The policy **AmazonS3FullAccess** grants access to **every bucket** in your AWS account.

Here’s what it looks like:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": "*"
    }
  ]
}
```

🧨 **What’s wrong with this?**

* ✅ `Action: "s3:*"` - Can do anything in S3 (delete, update, list, copy…)
* ✅ `Resource: "*"` - On **all buckets and objects**

> 🚨 This violates **Principle of Least Privilege** - an attacker with these keys can compromise everything in S3.

---

### ✅ Step 5: Fix the Misconfiguration

Finally where we are going to fix the misconfiguration

##### ✅ Remove Public Access

* Go to S3 → Permissions tab → Delete the public bucket policy

![](/assets/img/s3-iam-project/20250727182014.png)

![](/assets/img/s3-iam-project/20250727182034.png)

![](/assets/img/s3-iam-project/20250727182049.png)

##### ✅ Block All Public Access

* In bucket settings → Enable **“Block all public access”**

![](/assets/img/s3-iam-project/20250727182141.png)

Before ->

![](/assets/img/s3-iam-project/20250727182201.png)

After ->

![](/assets/img/s3-iam-project/20250727182221.png)

![](/assets/img/s3-iam-project/202507...