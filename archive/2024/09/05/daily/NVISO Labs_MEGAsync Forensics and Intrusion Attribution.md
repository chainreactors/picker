---
title: MEGAsync Forensics and Intrusion Attribution
url: https://blog.nviso.eu/2024/09/04/megasync-forensics-and-intrusion-attribution/
source: NVISO Labs
date: 2024-09-05
fetch_date: 2025-10-06T18:25:20.246960
---

# MEGAsync Forensics and Intrusion Attribution

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [twitter](https://twitter.com/NVISO_Labs)
* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)

Menu

* [All](https://blog.nviso.eu/)
* [Blue Team](https://blog.nviso.eu/category/blue-team/)
* [Cloud Security](https://blog.nviso.eu/category/cloud-security/)
  + [AWS](https://blog.nviso.eu/category/cloud-security/aws/)
  + [Azure](https://blog.nviso.eu/category/cloud-security/azure/)
  + [GCP](https://blog.nviso.eu/category/cloud-security/gcp/)
  + [Microsoft 365](https://blog.nviso.eu/category/cloud-security/microsoft-365/)
* [Awareness](https://blog.nviso.eu/category/awareness/)
* [Forensics](https://blog.nviso.eu/category/forensics/)
* Other
  + [Application Security](https://blog.nviso.eu/category/application-security/)
  + [IoT Security](https://blog.nviso.eu/category/iot-security/)
  + [Web Security](https://blog.nviso.eu/category/web-security/)
  + [Industrial Security](https://blog.nviso.eu/category/industrial-security/)
  + [Mobile Security](https://blog.nviso.eu/category/mobile-security/)
  + [Cyber Strategy](https://blog.nviso.eu/category/cyber-strategy/)
  + [Purple Team](https://blog.nviso.eu/category/purple-team/)
  + [Red Team](https://blog.nviso.eu/category/red-team/)
  + [Events](https://blog.nviso.eu/category/events/)

# MEGAsync Forensics and Intrusion Attribution

[Maxime Thiebaut](https://blog.nviso.eu/author/maxime-thiebaut/ "Posts by Maxime Thiebaut")

[Tools](https://blog.nviso.eu/category/tools/), [Forensics](https://blog.nviso.eu/category/forensics/)

September 4, 2024September 3, 2024
3 Minutes

When intrusions near completion, adversaries commonly exfiltrate any data they can put their hands on. Among the many [exfiltration techniques](https://attack.mitre.org/tactics/TA0010/), [MEGAsync](https://github.com/meganz/MEGAsync) has been a widely employed web service given its end-to-end encryption and associated privacy reputation.

Performing forensics on MEGAsync and associated artefacts can provide valuable insights into an intrusion such as identifying which data has been exfiltrated. In this blog post, we’ll cover how MEGAsync forensics can be leveraged to identify exfiltrated files, additional victims and, subsequently, perform attribution.

## The absence of evidence is not evidence of absence

As part of a June incident response, the [forensic analysis of MEGAsync logs](https://blog.reconinfosec.com/megasync-analysis) did not yield the expected exfiltration evidence. Naturally this raised the question on whether logs were incomplete (rotated, truncated, …) or whether the eradication of the adversary occurred just-in-time prior to MEGAsync exfiltration. To support this negative claim, we decided to analyze the MEGAsync Statecache, an action which inadvertently allowed us to identify additional victims and, subsequently, attribute the intrusion.

## MEGA’s Statecache database

Software interacting with MEGA (e.g., MEGAsync) can rely on MEGA-published libraries (SDK, Software Development Kit) to implement core functionalities such as the synchronizing of files. To ensure the state of the files remain coherent, MEGA’s SDK employs a SQLite database titled *Statecache*.

On Windows, the MEGAsync Statecache can be found at the following location where `{version}` represents the MEGA SDK version (currently `14`) and `{name}` the pseudo-random database name.

```
%LocalAppData%\Mega Limited\MEGAsync\megaclient_statecache{version}_{name}.db
```

Within the Statecache database, the `nodes` table contains information on each file and folder (a.k.a. `node`) synchronized by MEGA. For each `node`, the entry references their respective parent (i.e., folder), the node’s `name`, their `size`, the associated creation and modification time as well as other information such as `flags`, `tags` and `description`.

As an example, the following sample Statecache outlines the `favourite.txt` node to be a child of the `NVISO` node.

![A screenshot of the Statecache SQLi database with relation keys highlighted.](https://blog.nviso.eu/wp-content/uploads/2024/07/Statecache-1.jpg)

Figure 1: A sample MEGA Statecache

Noteworthy is that the MEGA Statecache’s `nodes` table contains a `mimetype` column which employs the nonstandard `getmimetype` SQLite function. As such, this column is known to crash common SQLite viewers if included in the result.

### Node Types

By default, the Statecache nodes table contains 3 top-level entries whose names seem uncommon (i.e., `CRYPTO_ERROR`) and type appear unique. As [defined in the MEGA SDK](https://github.com/meganz/sdk/blob/e6a6485c151482f67c98a9c57b9b810bff3d31ac/include/mega/types.h#L351-L363), these are the vault, root and rubbish top-level nodes.

```
// node types:
typedef enum {
    TYPE_NESTED_MOUNT = -5,
    TYPE_SYMLINK = -4,
    TYPE_DONOTSYNC = -3,
    TYPE_SPECIAL = -2, // but not include SYMLINK
    TYPE_UNKNOWN = -1,
    FILENODE = 0,    // FILE - regular file nodes
    FOLDERNODE,      // FOLDER - regular folder nodes
    ROOTNODE,        // ROOT - the cloud drive root node
    VAULTNODE,       // VAULT - vault, for "My backups" and other special folders
    RUBBISHNODE,     // RUBBISH - rubbish bin
} nodetype_t;
```

Using the above node types, we can state that the `favourite.txt` file is a child of the `NVISO` folder and that this folder is located within the top-level `root` node. As seen in figure 1, the `rubbish.txt` file on the other hand is located within the top-level `rubbish` node.

### Tooling

Based on this information, we have assembled `[mega-statecache.py](https://github.com/NVISOsecurity/blogposts/blob/master/MEGAsync%20Forensics%20and%20Intrusion%20Attribution/mega-statecache.py)`; Enabling forensic examiners to perform a directory listing of MEGA’s Statecache.

## Results

Inspecting the Statecache recovered throughout the investigation corroborated the logs; No organization data had yet been exfiltrated through MEGAsync.

As incident responders certainly know, it is not uncommon for threat actors to reuse techniques and infrastructure. MEGA being a cloud service, the Statecache not only provides evidence on locally-synced files, but also on remotely available files (i.e. downloadable). As such, the Statecache-analysis uncovered that the attacker’s MEGA account additionally contained data from previous and ongoing exfiltration campaigns. Correlating these additional victims with public information permitted the attribution of the intrusion to a LockBit affiliate, as can be observed in the figures below.

![A listing of files exfiltrated from EMA EDA.](https://blog.nviso.eu/wp-content/uploads/2024/07/Screenshot-2024-07-09-171845.png)

Figure 2a: A listing of files exfiltrated from EMA EDA.

![A listing of EMA EDA on the LockBit portal.](https://blog.nviso.eu/wp-content/uploads/2024/07/GNsr3sUWYAAh4hN-1-1024x193.jpg)

Figure 2b: A listing of EMA EDA on the LockBit portal.

![A listing of files exfiltrated from Skanlog.](https://blog.nviso.eu/wp-content/uploads/2024/07/Screenshot-2024-07-09-173131.png)

Figure 3a: A listing of files exfiltrated from Skanlog.

![A listing of Skanlog on the LockBit portal.](https://blog.nviso.eu/wp-content/uploads/2024/07/GM-f8WnXgAE5SRF.png)

Figure 3b: A listing of Skanlog on the LockBit portal.

![A listing of files exfiltrated from Gorrias Mercedes Benz.](https://blog.nviso.eu/wp-content/uploads/2024/07/Screenshot-2024-07-09-173639.png)

Figure 4a: A listing of files exfiltrated from Gorrias Mercedes Benz.

![A listing of Gorrias Mercedes Benz on the LockBit portal.](https://blog.nviso.eu/wp-content/uploads/2024/07/GM-Y5TcWMAAHDzS-1024x288.jpg)

Figure 4b: A listing of Gorrias Mercedes Benz on the LockBit...