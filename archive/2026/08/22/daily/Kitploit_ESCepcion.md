---
title: ESCepcion
url: https://kitploit.com/en/tools/github/hackwarts12/escepcion
source: Kitploit
date: 2026-08-22
fetch_date: 2026-08-23T02:57:29.131656
---

# ESCepcion

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

ESCepcion — Passive AD CS auditor detecting ESC1–ESC16 and Shadow Credentials via read-only LDAP/ACL/registry checks, with prioritized remediation and SIEM-ready output. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/hackwarts12/escepcion

![](https://assets.kitploit.com/production/public/tools/50640/d529c1328a42d628dbb82fdb551791f620d35a8b3d11291a607d81374fc5d316-display-v1.webp)

[Defensive Tools](/en/categories/defensive-tools)[Privilege Escalation](/en/categories/privilege-escalation)[Vulnerability Scanners](/en/categories/vulnerability-scanners)[Vulnerability Analysis](/en/categories/vulnerability-analysis)[Configuration Auditing](/en/categories/configuration-auditing)[Penetration Testing](/en/categories/penetration-testing)[Misconfiguration](/en/categories/misconfiguration)

![GitHub](/providers/github.png)hackwarts12/escepcion

# ESCepcion

Passive AD CS auditor detecting ESC1–ESC16 and Shadow Credentials via read-only LDAP/ACL/registry checks, with prioritized remediation and SIEM-ready output.

[View Repository](https://github.com/hackwarts12/escepcion)

21 month ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# 🛡️ ESCepcion

**Active Directory Certificate Services Auditor**

ESCepcion is an open-source tool for auditing and assessing vulnerabilities in **Active Directory Certificate Services (AD CS)** infrastructures. It is designed to automate the detection of privilege escalation paths (ESC) with a strict focus on reducing false positives in corporate and hybrid environments.

Unlike other tools, **ESCepcion does not exploit, modify, or write any object to Active Directory**. All its operations are based exclusively on read-only LDAP queries and optional registry reads via MS-RRP (using `--deep-scan`).

---

## 🆚 ESCepcion vs. Certipy / Certify

The community has excellent reference tools such as **Certipy** and **Certify**, whose main focus is on Red Team operations and **active exploitation** (requesting certificates, issuing them, forcing authentications, etc.).

**ESCepcion does not seek to replace them, but to complement them from a defensive perspective:**
While Certipy/Certify are your arsenal for *exploiting* and demonstrating technical impact, **ESCepcion** focuses exclusively on **passive auditing and false positive validation**. ESCepcion cross-references LDAP configuration data, ACL permissions, and Registry validations automatically to generate prioritized reports ready for remediation.

---

## 🎯 Main Features

* **Exhaustive Detection:** Coverage of the most critical vulnerabilities (ESC1 - ESC16, CVE-2022-26923, CVE-2024-49019, etc.).
* **Shadow Credentials (CBA):** Robust detection of insecure delegations on `msDS-KeyCredentialLink`, differentiating real risks from legitimate configurations (Windows Hello for Business, FIDO2).
* **Anti-False Positive:** Deterministic states. All findings are strictly categorized as `EXPLOITABLE`, `NEAR_MISS`, `POTENTIAL`, `NOT_SCANNED`, or `SAFE`, avoiding ambiguity.
* **Attack Chains (Combo Chains):** Automatic identification of composite vectors (DDCC) where multiple vulnerabilities are combined to compromise the domain.

---

## 🧠 Risk Model (DDCC and L1–L5)

ESCepcion uses a proprietary risk model that goes beyond classic severity scores:

* **L1–L5:** Maps each finding to the attacker's *real gain* (for example: privileged impersonation, certificate minting), not just by the type of technical vulnerability.
* **DDCC (Dynamic Domain Compromise Chains):** Determines whether chained findings form a viable path toward total domain compromise from a standard user account.

You can read the full documentation of our risk model at:
🔗 **[hackwarts12.github.io/ESCepcion/risk-model](https://hackwarts12.github.io/ESCepcion/risk-model)**

---

## ⚙️ Requirements

* Python 3.8+
* Python dependencies listed in `requirements.txt` (includes libraries such as `impacket`, `ldap3`, among others).

---

## 🚀 Installation

Clone the repository and install the required Python dependencies:

root@kitploit:~

```
git clone https://github.com/YOUR-USERNAME/ESCepcion.git
cd ESCepcion
pip install -r requirements.txt
```

*(Optional) If a specific PowerShell environment exists, you can run `install.ps1`.*

---

## 💻 Usage

To run a basic authenticated scan against a Domain Controller:

root@kitploit:~

```
python main.py -d mydomain.local -dc-ip 192.168.1.100 -u user -p 'password'
```

### Deep Scan (Recommended)

Add the `--deep-scan` parameter to run extra checks via MS-RRP (Remote Registry) and obtain a higher confidence level in the coverage of specific ESCs:

root@kitploit:~

```
python main.py -d mydomain.local -dc-ip 192.168.1.100 -u user -p 'password' --deep-scan
```

### Other Authentication Methods

Authentication using the NTLM hash (Pass-the-Hash):

root@kitploit:~

```
python main.py -d mydomain.local -dc-ip 192.168.1.100 -u user -H 'LMHASH:NTHASH'
```

---

## 📊 Reports (Output)

ESCepcion generates two files after each scan:

1. **HTML Dashboard:** An interactive report that includes:

   * Security posture score (0–100).
   * Attack Chain visualization and Combo Chains correlation.
   * Individual remediation playbooks for each finding with the exact commands to mitigate.
   * Coverage map showing which ESCs were evaluated and which require a `--deep-scan`.
2. **JSON File:** A structured output ideal for:

   * Direct integration with SIEM tools.
   * Remediation tracking based on historical *diff* tracking.
   * PKI data compatible with BloodHound graphs.

---

## 📁 Project Structure

root@kitploit:~

```
ESCepcion/
├── main.py                # Main CLI of the tool
├── auth/                  # Connection modules (LDAP, RPC, etc.)
├── modules/               # Check modules (ESC1-16, Shadow Credentials, etc.)
├── utils/                 # Utilities (Report generator, ACL parsing)
├── output/                # Directory where JSON/HTML reports are generated
│
# Frontend Files (Landing Page / Documentation)
├── index.html             # Main Web page
├── styles.css             # Corporate web styles
└── risk-model.html        # Interactive documentation of the risk model
```

---

## 🎓 Research Credits

ESCepcion's deductive and detection logic is strongly built upon the exceptional research work of the cybersecurity community:

* **Will Schroeder & Lee Christensen (SpecterOps)** — *Certified Pre-Owned* (2021), foundational research on ESC1–ESC8 vectors.
* **Oliver Lyak** — Creator of Certipy, research on ESC9, ESC10, and ESC16 vectors.
* **Jonas Bülow Knudsen** — Research on ESC13 and ESC14 (2024).
* **Justin Bollinger (TrustedSec)** — Research on ESC15, EKUwu, and CVE-2024-49019 (2024).

---

## 📜 Legal and License

**Only for authorized security testing.**
ESCepcion must be used solely and exclusively on infrastructures for which you have explicit written authorization to audit.

The project is distributed under the **MIT License**. See the `LICENSE` file for more details.

[Download Tool](https://github.com/hackwarts12/escep...