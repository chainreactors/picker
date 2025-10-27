---
title: Protected Users: you thought you were safe uh?
url: https://sensepost.com/blog/2023/protected-users-you-thought-you-were-safe-uh/
source: Orange Cyberdefense
date: 2023-04-01
fetch_date: 2025-10-04T11:20:30.451122
---

# Protected Users: you thought you were safe uh?

# [![Orange Cyberdefense](/img/master-logo.svg) ![](/images/orange-logo-small.svg) ![Orange Cyberdefense](/img/logo-text-x.svg)](/)

* [![Orange Cyberdefense](/img/master-logo.svg)

  ![](/images/orange-logo-small.svg)

  ![Orange Cyberdefense](/img/logo-text-x.svg)](/)

# Our Blog

* [2025 (16)](/blog/2025/)
* [2024 (10)](/blog/2024/)
* [2023 (19)](/blog/2023/)
* [2022 (10)](/blog/2022/)
* [2021 (13)](/blog/2021/)
* [2020 (30)](/blog/2020/)
* [2019 (10)](/blog/2019/)
* [2018 (14)](/blog/2018/)
* [2017 (27)](/blog/2017/)
* [2016 (22)](/blog/2016/)
* [2015 (17)](/blog/2015/)
* [2014 (15)](/blog/2014/)
* [2013 (30)](/blog/2013/)
* [2012 (27)](/blog/2012/)
* [2011 (33)](/blog/2011/)
* [2010 (36)](/blog/2010/)
* [2009 (81)](/blog/2009/)
* [2008 (75)](/blog/2008/)
* [2007 (80)](/blog/2007/)

# Protected Users: you thought you were safe uh?

Reading time
~10 min

*Posted
by aurelien.chalot@orangecyberdefense.com
on
31 March 2023*

Categories:
[Kerberos](/blog/kerberos/),
[Ntlm](/blog/ntlm/),
[Windows](/blog/windows/),
[Delegation](/blog/delegation/),
[Protected users](/blog/protected%20users/)

On the 31st of October 2022, a PR on [CrackMapExec from Thomas Seigneuret (@Zblurx)](https://github.com/Porchetta-Industries/CrackMapExec/pull/655) was merged. This PR fixed Kerberos authentication in the CrackMapExec framework. Seeing that, I instantly wanted to try it out and play a bit with it. While doing so I discovered a weird behaviour with the Protected Users group. In this blogpost I’ll explain what the Protected Users group is, why it is a nice security feature and yet why it is incomplete for the Administrator (RID500) user.

## I/ Usual internal assessment scenario and PtH/OPtH

In my [previous blogpost about Windows Access Tokens](https://sensepost.com/blog/2022/abusing-windows-tokens-to-compromise-active-directory-without-touching-lsass/) I described one of the most common scenarios we encounter on internal assessments. Basically we compromise one server, dump its SAM database and LSASS memory to retrieve cleartext credentials or NT hashes. We can also dump Kerberos tickets and generally any other material that we could use to connect elsewhere:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/commonscenario.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/commonscenario.png)

Whether it is in the SAM database or in the memory of the LSASS process, you will probably find NT hashes:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/nthashes.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/nthashes.png)

On Windows, having a NT hash is equivalent to having a cleartext password. If we take a look at the NTLM authentication protocol we can see that the challenge is cyphered using the NT hash of the user:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/image-58.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/image-58.png)

Since we have the NT hash we can cypher the challenge without knowing the corresponding cleartext password.

On Kerberos it is pretty much the same. The Kerberos authentication protocol relies on four packets which are:

* KRB\_AS\_REQ
* KRB\_AS\_REP
* KRB\_TGS\_REQ
* KRB\_TGS\_REP

The process is the following:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/image-59.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/image-59.png)

The important part is the “timestamp ciphered with a key derived from the password of the user”. As a user, we can cipher the timestamp using a key that can be obtained using one of the following algorithms:

* RC4
* DES
* AES-128
* AES-256

The interesting thing is that RC4 cyphers the timestamp using the NT hash of the user. Since we have a valid NT hash, we can cipher the timestamp and have a valid KRB\_AS\_REQ packet. With the CrackMapExec framework we can now connect to remote servers using two well known attacks:

* Pass the Hash (for the NTLM authentication protocol):

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/passthehash-1024x67.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/passthehash.png)

* OverPass the Hash (for the Kerberos authentication protocol):

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/overpassthehash-1024x89.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/overpassthehash.png)

These attacks rely on the fact that it is possible to use a NT hash to cypher a secret used to authenticate a user. To protect against this, one approach is to add sensitive users to the “Protected Users” group.

## II/ Protected Users group

The “Protected Users” group was introduced in Windows Server 2012R2. If we take a look at the [MSDN](https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/protected-users-security-group) article we can see that users in this group have hardened security options:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/protectedusers.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/protectedusers.png)

As you can see, NTLM authentication is disabled, the RC4 algorithm cannot be used to cipher the timestamp for Kerberos authentication and finally, Kerberos delegation is disabled. Let’s test this.

First I will add a new domain administrator user (admin2) that is in the “Protected Users” group:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/admin2-1.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/admin2-1.png)

Now let’s try to authenticate using NTLM:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/ntlmrestriction-1-1024x112.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/ntlmrestriction-1.png)

As you can see it’s not working, we receive the “STATUS\_ACCOUNT\_RESTRICTION”. And now lets try using Kerberos:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/kerberosrestricted-1-1024x105.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/kerberosrestricted-1.png)

It’s not working either (KDC\_ERR\_PREAUTH\_FAILED). So yeah it looks like the expected Protected Users security features apply to the admin2 user. But do they apply to all users ?

## III/ The strange behaviour

**1 – The RC4 key case**

While I was playing with the CrackMapExec PR, I randomly tried to authenticate using Kerberos as the WHITEFLAG/Administrator account and what I realised was that it works even if the user is in the Protected Users group:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/administrator-1024x89.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/administrator.png)

In contrast, NTLM authentication fails:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/administratorpu-1024x61.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/administratorpu.png)

Which means that the restriction of the Protected Users group is not complete when it comes to the RID500 user of the Active Directory domain. We cannot connect using the NTLM authentication protocol but we can connect using the Kerberos authentication protocol with RC4.

**2 – The delegation case**

Another strange behaviour relates to Kerberos Delegation. Normally, when a user is in the Protected Users group, they cannot be delegated. Here I’m trying to abuse a RBCD delegation scenario from OCD$ to ADCS1$ to get a service ticket first as **pu\_user**, which is a Protected Users, and second as **not\_pu\_user**, which is not. First, lets take a look at the delegation:

[![](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/2023-02-06_11-10-1.png)](/img/pages/blog/2023/protected-users-you-thought-you-were-safe-uh/2023-02-06_11-10-1.png)

Lets loo...