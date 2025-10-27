---
title: Daily Blog #732: Multiple Identity Provider Disorder
url: https://www.hecfblog.com/2025/01/daily-blog-732-multiple-identity.html
source: Hacking Exposed Computer Forensics Blog
date: 2025-01-30
fetch_date: 2025-10-06T20:14:07.946514
---

# Daily Blog #732: Multiple Identity Provider Disorder

[![Hacking Exposed Computer Forensics Blog](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhV1r9Fx_K3sKHfI8wnPUPPQFkxWhuxayNz8tT11sG8lYQgY1gGiwV9Qdlfeq-b80FMkRdsOwimMVCo2VbnE0aXyGxaTX1YYhUB5IZ4yK1LhASjfZxFmkAstIM9DnylPabPqQ15WEAFysbZ/s384/unnamed.png)](https://www.hecfblog.com/)

* [Extended Mapi](https://www.hecfblog.com/search/label/extended%20mapi)
* [ObjectID](https://www.hecfblog.com/search/label/objectid)
* [Amcache](https://www.hecfblog.com/search/label/amcache)
* [CTF](https://www.hecfblog.com/search/label/ctf)
* [Python](https://www.hecfblog.com/search/label/python)
* [Syscache](https://www.hecfblog.com/search/label/syscache)
* [Daily Blogs](https://www.hecfblog.com/search/label/Daily%20Blog?max-results=6)
  + [Saturday Reading](https://www.hecfblog.com/search/label/Saturday%20reading)
  + [Solution Saturday](https://www.hecfblog.com/search/label/solution%20saturday)
  + [Forensic Lunch](https://www.hecfblog.com/search/label/forensic%20lunch?&max-results=8)
  + [Sunday Funday](https://www.hecfblog.com/search/label/sunday%20funday?&max-results=8)

[Home](https://www.hecfblog.com/)

[krebs](https://www.hecfblog.com/search/label/krebs)

Daily Blog #732: Multiple Identity Provider Disorder

# Daily Blog #732: Multiple Identity Provider Disorder

By
[David Cowen](https://www.blogger.com/profile/17629115910611763170 "author profile")
•
January 28, 2025
•

[Daily Blog](https://www.hecfblog.com/search/label/Daily%20Blog?&max-results=8)
[google workspace](https://www.hecfblog.com/search/label/google%20workspace?&max-results=8)
[ir](https://www.hecfblog.com/search/label/ir?&max-results=8)
[krebs](https://www.hecfblog.com/search/label/krebs?&max-results=8)
•

Comments :
0

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgk1hrraH3XC1Iubaito5rtxiqKbqsAUvF0zVZD2ITYKQRN2bslK2rY9EBvcdVwwYvn9tq7wSSC7kdxMQUAUjSV8avCccfpaf2uGpnWCh04qG-LHSfRTWkMihVSOxET-eesTAHhTx0qcdSMgmOBoKuxY35yULtcHyr0PIeR69G2tmxhvHLeenl1SHU6xwM/w640-h640/googleworkspacebypass.webp)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgk1hrraH3XC1Iubaito5rtxiqKbqsAUvF0zVZD2ITYKQRN2bslK2rY9EBvcdVwwYvn9tq7wSSC7kdxMQUAUjSV8avCccfpaf2uGpnWCh04qG-LHSfRTWkMihVSOxET-eesTAHhTx0qcdSMgmOBoKuxY35yULtcHyr0PIeR69G2tmxhvHLeenl1SHU6xwM/s1024/googleworkspacebypass.webp)

Hello Reader,

This summer, we encountered a fascinating incident that highlights a surprising gap in how some third-party services handle authentication. Brian Krebs later covered the underlying issue in his post “[Crooks Bypassed Google’s Email Verification to Create Workspace Accounts, Access 3rd-Party Services](https://krebsonsecurity.com/2022/07/crooks-bypassed-googles-email-verification-to-create-workspace-accounts-access-3rd-party-services/),” but our investigation was already finished by then. Let’s dive in.

---

### **The Scenario**

Imagine your company has a third-party service provider where employees can create their own accounts. This service also supports authentication through multiple identity providers—like Google, Apple, or Facebook—to make logging in easier.

However, there’s a catch: in some cases, the third-party service will treat an identity-provider-based login as if it were the *same* account an employee created manually—even if they never actually linked their account to that identity provider.

---

### **How this Exploit Worked**

1. #### **Manual Account Creation**

   A user signs up for a third-party website using their company email address and even enables multi-factor authentication (MFA).
2. #### **Multiple Identity Providers**

   The third-party site allows users to log in via providers like Google. Ideally, this is meant for convenience *instead* of creating an account manually.
3. #### **Domain Hijack**

   A threat actor finds a loophole that lets them register the same email address on Google Workspace—even though the domain actually belongs to someone else. (See Krebs’s article for how they bypass Google’s verification.)
4. #### **Unintended Access**

   Once the attacker has set up that Google Workspace email, they sign in to the third-party service using Google. Because the service trusts Google’s authentication, it grants the attacker access to the real user’s account—MFA included.

---

### **Why This Shouldn’t Work**

* #### **Identity Provider Verification**

  Google (or any identity provider) should confirm domain ownership before allowing someone to create email accounts for that domain. Attackers found a way around this requirement.
* #### **Third-Party Account Linking**

  The third-party service should recognize that the user’s existing account isn’t linked to Google. However, many services fail to confirm whether an account was created manually vs. through an identity provider, resulting in the user’s legitimate account being “taken over.”

---

### **Our Investigation**

In the logs, we noticed a user’s account authenticating via Google—odd, since that user’s company uses Microsoft 365. After reaching out to Google, we learned that the domain had recently been set up on Google Workspace, which led to a small set of logs confirming a brand-new account. Initially, we thought the third-party website might have suffered a larger breach. Then Brian Krebs’s coverage explained exactly how attackers managed to bypass Google’s email verification, confirming our findings.

---

### **Things to look for**

* If you’re investigating an incident and see a user “miraculously” authenticating—especially if it’s not a straightforward case of stolen tokens—check the identity providers the third-party service supports.

This case was a stark reminder that even well-known platforms can be manipulated if there’s a loophole in domain or email verification procedures.

Also Read: [Accessing multiple shadow copies at once with AIM](https://www.hecfblog.com/2025/01/daily-blog-731-accessing-multiple.html)

#### Post a Comment

[Newer Post](https://www.hecfblog.com/2025/01/daily-blog-733-test-kitchen-building.html "Newer Post")

[Older Post](https://www.hecfblog.com/2025/01/daily-blog-731-accessing-multiple.html "Older Post")
[Home](https://www.hecfblog.com/)

Subscribe to:
[Post Comments
(
Atom
)](https://www.hecfblog.com/feeds/8034023212956267311/comments/default)

## Top Posts/Right Now

* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiS4Zw9KQkjNkc2JCwa0rDb1zPUCypCWZgocTE2voitZGOwzeZ2L_4D63LJ0j9JPosWO-nLahPLJYL-tsQMEgmfVhxmjpJ6Smn6FKVk2_JhClTq_WWhvcE13R76fsdeVWnJb-lPNFnJnif0HpOq-5yuADLWqHUQjQG4zpbLb46P0PM-dvHaM9rsb-D39qs/s72-c/sundayfunday.png)](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)

  [Daily Blog #814: Sunday Funday 4/20/25](https://www.hecfblog.com/2025/04/daily-blog-814-sunday-funday-42025.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5GWh0tXGteqxfrTQFDzW2kMooGHcwNkA6h9f_bfBDpsRMJtvg0UR1SHfIqx4UYxViUSiLEJFeWq9SryUdFz5gwlrOlXEFCZDoNnqRlbU3pn_lGfYxr60W3HgTAXc7b3IqLHYN3F0kW72JbkCoEID0IEVH-rls7Q1LRd_0awNugK97uT7EDxugHyuXvFM/s72-c/forgive.png)](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)

  [Daily Blog #815: I missed a day](https://www.hecfblog.com/2025/04/daily-blog-815-i-missed-day.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi60iLy5WiSNWWSyeIoM9JsOK9Xwv5L7GT5g4NxBmdQwyQNbbHzgWoiG4FbwefVVrqg1yDaz0ripRAlyXSWNX4xJ3tACOcH7a0_YyoPVT2XMPnI2-0aE3gKc9hJWhMWYqDWlTUDM2XM3DEHiJB5Z1iSrtjQeP0qG5xKxmt4RewUfbqA0FR7cw1DXPwxYNM/s72-c/solutionsaturday.png)](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)

  [Daily Blog #813: Solution Saturday 4/19/25](https://www.hecfblog.com/2025/04/daily-blog-813-solution-saturday-41925.html)
* [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhK3OAgdGTujkTy5X-nM4364yuWc8TJa-ct4GGE-Phw3vdXX9DApDT_kRhIvjELWVYLvnTPIrJTGFuz2hhkhVoklmY6bixe4fypY1X1A8RuJgAoPUUK597HYTBKVrOgLMn11x2g6b0azfhNnVv7CE6p-ZZRcfmAnaIIB-RNEBL_rIakVyr80MUyDhMQGgI/s72-c/removefromgroup.png)](https://www.hecfblog.co...