---
title: Abusing AD-DACL: ForceChangePassword
url: https://www.hackingarticles.in/abusing-ad-dacl-forcechangepassword/
source: Hacking Articles
date: 2024-11-15
fetch_date: 2025-10-06T19:17:40.296606
---

# Abusing AD-DACL: ForceChangePassword

[Skip to content](#content)

Hacking Articles

## Recent Posts

* [AWS: IAM CreateLoginProfile Abuse](https://www.hackingarticles.in/aws-iam-createloginprofile-abuse/)
* [Privacy Protection: Encrypted DNS](https://www.hackingarticles.in/privacy-protection-encrypted-dns/)
* [Privacy Protection: Windows Privacy](https://www.hackingarticles.in/privacy-protection-windows-privacy/)
* [Privacy Protection: Browsers](https://www.hackingarticles.in/privacy-protection-browsers/)
* [Privacy Protection: Password Manager](https://www.hackingarticles.in/privacy-protection-password-manager/)

## Most Used Categories

* [CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/) (504)
  + [VulnHub](https://www.hackingarticles.in/category/ctf-challenges/vulnhub/) (311)
  + [HackTheBox](https://www.hackingarticles.in/category/ctf-challenges/hackthebox/) (164)
* [Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/) (408)
* [Red Teaming](https://www.hackingarticles.in/category/red-teaming/) (126)
* [Website Hacking](https://www.hackingarticles.in/category/website-hacking/) (64)
* [Cyber Forensics](https://www.hackingarticles.in/category/cyber-forensics-tricks/) (68)
* [Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/) (59)
* [Hacking Tools](https://www.hackingarticles.in/category/collection-of-hacking-tools/) (33)
* [Pentest Lab Setup](https://www.hackingarticles.in/category/pentest-lab-setup/) (29)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Search for:

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [DACL Attacks](https://www.hackingarticles.in/category/dacl-attacks/)
»* [Abusing AD-DACL: ForceChangePassword](https://www.hackingarticles.in/forcechangepassword-active-directory-abuse/)
»

[DACL Attacks](https://www.hackingarticles.in/category/dacl-attacks/)

# Abusing AD-DACL: ForceChangePassword

[November 14, 2024June 19, 2025](https://www.hackingarticles.in/forcechangepassword-active-directory-abuse/) by [Raj](https://www.hackingarticles.in/author/raj/)

In this post, we explore **ForceChangePassword Active Directory abuse** via the exploitation of **Discretionary Access Control Lists (DACL)** using the **ForcePasswordChange** permission in Active Directory environments. This permission is especially dangerous for **privileged accounts**, as it enables lateral movement and unauthorized access across systems by impersonating the compromised account. Therefore, understanding how this vulnerability works is crucial for security professionals.

Additionally, the lab setup necessary to simulate these attacks is outlined, with methods mapped to the **MITRE ATT&CK** framework to clarify the associated techniques and tactics. **Detection mechanisms** for identifying suspicious activities linked to **ForcePasswordChange** attacks are also covered. Alongside this, actionable recommendations for mitigating these vulnerabilities are provided. As a result, this overview equips security professionals with critical insights to recognize and defend against these prevalent threats.

### Table of Contents

* **ForceChangePassword Right**
* **Prerequisites**
* **Lab Setup** – User Owns ForceChangePassword Rights
* **Exploitation** – User Owns ForceChangePassword Rights
* **Bloodhound** – Hunting for Weak Permission

**Method for Exploitation – Change Password (T1110.001)**

* Net RPC – Samba
* pth-toolkit
* Net RPC – Rpcclient
* Net RPC – BloodAD
* ldap\_shell tool
* impacket-changepasswd
* Windows PowerShell – Powerview
* Mimikatz
* Metasploit

**Detection & Mitigation**

### ForceChangePassword Right

This permission **grants** the right to change the password of a **user account** without knowing their current password. **Consequently**, attackers can use this access to perform unauthorized actions.

**Moreover**, this abuse can be carried out when controlling an object that has **GenericAll**, **AllExtendedRights**, or **User-Force-Change-Password** over the target user.

### Prerequisites

* Windows Server 2019 as Active Directory
* Kali Linux
* Tools: Bloodhound, Net RPC, Powerview, BloodyAD
* Windows 10/11 – As Client

### Lab Setup – User Owns ForceChangePassword Rights

To begin with, in this lab setup, we will create two users’ **Raj** and **Aarti**, and will assign **Raj** user “**Reset Password**” rights for **Aarti** User. To clarify, here’s how the lab environment will be set up:

#### Create the AD Environment:

To simulate an Active Directory environment, you will need a **Windows Server** as a **Domain Controller (DC)** and a client machine (Windows or Linux) where you can run **enumeration** and **exploitation tools**. **Subsequently**, you will be ready to test the **ForceChangePassword Active Directory Abuse** in a controlled setting.

##### **Domain Controller**:

* Firstly, Install Windows Server (2016 or 2019 recommended).
* Then, promote it to a Domain Controller by adding the **Active Directory Domain Services** role.
* Finally, set up the domain (e.g., **ignite.local**).

##### **User Accounts**:

* Create two AD user accounts named **Raj** and **Aarti**.

```
net user raj Password@1 /add /domain
net user aarti Password@1 /add /domain
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhK-nsuRtyidHPt2cYaN6wFQ9980MgHEGI1V5S8DUj4bMfnFRWHHHP6oQkLmo2p72T3HQcX8NqX0gZyUAytcieuG02WbrURGS5jysKH-USQvisQtyJQxx66FpyL-5QDWLBmYNzq1QaJdrBMCKKrNERQXjccWcwqQ0PCpmvzYAq3RS___nWzeJFB6YhC_hk-/s16000/1.png)

##### **Assign the “ForceChangePassword” Privilege to Raj for Aarti User:**

Once your AD environment is set up, you need to assign the **“ForceChangePassword”** rights to **Raj** for **Aarti** user.

**Steps**:

* First, open **Active Directory Users and Computers** (ADUC) on the Domain Controller.
* Enable the **Advanced Features** view by clicking on **View** > **Advanced Features**.
* Locate User **Aarti** in the **Users** container.
* Right-click on **Aarti User** and go to **Properties**.

![ForceChangePassword Active Directory Abuse](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhBUpRf12n_Kpc8ZFOC9G_cUndZWAlYhw1dvn-rDSJRTxdsfoGaRDRJGSpu71vyXUQIdHBPbYkvDcaf5TteLgB6Lb47w5k8xUqqZdFFeo2W2RoeNpq5NkX2eWSgzfQWp1zCv22oEla-BpfyqlWouC3sxEadg3ok6C3dg2E1jrm6oTsNGiuT8cf-I__FSTPz/s16000/2.png)

* Go to the **Security** tab. And click on **Add** button

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjTQymB4Clkfv7zFHZN-9Dwnusi4TNEEeF-hmW8b_dPfrq-dYdaH6FtVeWoWSd4-MYQj6jtSPTDMytfu3cu1AOVQQen2BFFIXkiCuGlf03N6QyvJSs_R8ds3HUa_p_iQ6bsDA5OM2zaJTdLdaicGB4DORF7MMZTkPrmPSOkVtY4NtwHqWu1QaDMU52n2NIo/s16000/3.png)

* In the “Enter the object name to select” box, type **Raj** and click **Check Names**.

![ForceChangePassword Active Directory Abuse](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEghST5HGe7wQI_tZoKMSjSPqExhHww0VfUNuwuzIm5YNCByX-T5zF_z4bzjk6HQ0ZEtZDeC0syIfyUALptJvBqofWXUdj3SSQxLlP1JJ79QLd_xGGm6qMylkr_wNNwd_DI5Ayp_P1smr0Cs4y75D_F1hvi_eGksa9AMi5k1f1un2oXtb8z4jicZPyxESVTi/s16000/4.png)

* Next, in the **Permissions** section, check the box for **Reset Password** permission.

Apply the settings.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjH3wlRoCfVIjMhP12hRHIntbLlXQ1uWD0Ilihliq_loeRQggbLYaP0yToLDib57q_4k0ByrVe5e3Odj76iIzXN3IJpPKR5W3bLrBQKJaCCAvuup5RhP737qBB8PC7bK5SMMAkdCoWAB78KXFVNjSy12epgZypa6OrQEMUnJLyPKCR6LkwW-ofPQSG-Zc9A/s16000/5.png)

At this point, Raj now has **Reset Password** rights for **Aarti user**, meaning **Raj** can change the password of **Aarti** user’s accoun...