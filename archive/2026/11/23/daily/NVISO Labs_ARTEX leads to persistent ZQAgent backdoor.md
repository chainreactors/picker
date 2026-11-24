---
title: ARTEX leads to persistent ZQAgent backdoor
url: https://blog.nviso.eu/2026/11/23/artex-fog0003-zqagent-backdoor/
source: NVISO Labs
date: 2026-11-23
fetch_date: 2026-11-24T11:47:47.235325
---

# ARTEX leads to persistent ZQAgent backdoor

[Skip to content](#content)

[![NVISO Labs](https://blog.nviso.eu/wp-content/uploads/2022/12/cropped-abn-zcrj_400x400-1.png)](https://blog.nviso.eu/)

[NVISO Labs](https://blog.nviso.eu/)

Cyber security research, straight from the lab! 🐀

* [linkedin](https://www.linkedin.com/company/nviso-cyber)
* mail us
* [our company](https://www.nviso.eu)
* [SSO](https://blog.nviso.eu/wp-admin/edit.php)
* Search for:Search Button

Menu

* [All](https://blog.nviso.eu/)
* [Prevent](https://blog.nviso.eu/category/prevent/)
  + [Application Security](https://blog.nviso.eu/category/prevent/application-security/)
    - [IoT Security](https://blog.nviso.eu/category/prevent/iot-security/)
    - [Web Security](https://blog.nviso.eu/category/prevent/web-security/)
    - [Mobile Security](https://blog.nviso.eu/category/prevent/mobile-security/)
    - [Industrial Security](https://blog.nviso.eu/category/prevent/industrial-security/)
    - [AI Security](https://blog.nviso.eu/category/prevent/application-security/ai-security/)
  + [Cloud Security](https://blog.nviso.eu/category/prevent/cloud-security/)
    - [AWS](https://blog.nviso.eu/category/prevent/cloud-security/aws/)
    - [Azure](https://blog.nviso.eu/category/prevent/cloud-security/azure/)
    - [GCP](https://blog.nviso.eu/category/prevent/cloud-security/gcp/)
    - [Microsoft 365](https://blog.nviso.eu/category/prevent/cloud-security/microsoft-365/)
  + [Awareness](https://blog.nviso.eu/category/prevent/awareness/)
  + [Cyber Strategy](https://blog.nviso.eu/category/prevent/cyber-strategy/)
  + [Red Team](https://blog.nviso.eu/category/prevent/red-team/)
* [Detect](https://blog.nviso.eu/category/detect/)
  + [Blue Team](https://blog.nviso.eu/category/detect/blue-team/)
  + [Purple Team](https://blog.nviso.eu/category/detect/purple-team/)
* [Respond](https://blog.nviso.eu/category/respond/)
  + [Forensics](https://blog.nviso.eu/category/respond/forensics/)
* Other
  + [Events](https://blog.nviso.eu/category/events/)

# ARTEX leads to persistent ZQAgent backdoor

[Maxime Thiebaut](https://blog.nviso.eu/author/maxime-thiebaut/)

[Respond](https://blog.nviso.eu/category/respond/), [Reverse Engineering](https://blog.nviso.eu/category/reverse-engineering/)

November 23, 2026November 23, 2026
10 Minutes

Over the last few months, NVISO has responded to an increasing amount of intrusions leveraging adversary LLM tools such as ARTEX. Several industry peers have [corroborated](https://cloud.google.com/blog/topics/threat-intelligence/artex-and-friends-enter-agentic-offensive-frameworks)[1](#74d88533-9690-4116-8f30-6009e258c8c6) this increased activity, with LLM-driven tools excelling at exploitation and credential abuse. LLM-driven intrusions have to date maintained a relatively consistent attack-chain commonly permitting containment through the isolation of its initial-access vector and the subsequent extensive revocation of compromised and staged credentials.

Amplified by the speed and noise of LLMs, these intrusions are often experienced as smash-and-grab operations, rarely resulting in long-lasting footholds beyond collected and staged credentials. However, as part of a recent incident response engagement, **NVISO observed ARTEX deploying ZQAgent, a new backdoor providing its operator with a long-lasting foothold within the target environment. The usage of a persistent backdoor by LLM-driven tools deviates from their current autonomous nature and is instead believed to be the result of operator-specific instructions.**

The usage of LLMs is still [rarely observed](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/)[2](#506d94e7-f8ac-4eac-9a97-6c4cd7a2252d) in traditional backdoor deployment operations, we see no reason that, over the near future, the usage of LLMs would not widely spread to these historically conventional operations.

## ZQAgent

ZQAgent, named through ARTEX artifacts, is a new stealthy backdoor providing adversaries with commonly desired capabilities such as arbitrary code execution, filesystem operations, network tunneling and more. NVISO observed ZQAgent’s deployment in Belgium, initially under `/tmp/zqa/systemd-timesyncd`, with [similar samples](https://www.virustotal.com/gui/file/0319739869e1aadb2d598152a0290215c057c8364257f3a84a42164cf863019f)[3](#ecbe1818-79fd-4e82-be2d-18c4f4481ccc),[4](#abafcac1-744b-4b90-96e1-dac4325c494a) reported from Taiwan. As part of our incident response activities, NVISO was able to confirm all known samples were configured to use `37.122.150[.]15` and `bloonspace[.]com` for command and control; We currently associate this infrastructure with FOG0003.

![](https://blog.nviso.eu/wp-content/uploads/2026/11/image-52.png)

ZQAgent’s decrypted configuration.

Network intelligence contributed by Team Cymru further suggests that FOG0003 likely deployed ZQAgent within Asia, affecting government and human-rights organizations.

### Runtime Evasion

To hinder detection, ZQAgent migrates itself in memory to a temporary anonymous file. This migration results in the apparent filename `/memfd:a (deleted)`, also observed in the earlier discussed public samples.

![](https://blog.nviso.eu/wp-content/uploads/2026/11/image-4.png)

ZQAgent’s temporary anonymous file allocation.

![](https://blog.nviso.eu/wp-content/uploads/2026/11/image-49.png)

ZQAgent’s public samples, named “memfd:a (deleted)”.

Once ZQAgent copied itself to the temporary anonymous file, the backdoor restarts as a detached process impersonating the [`dbus-daemon` utility](https://linux.die.net/man/1/dbus-daemon)[5](#21228852-b6ba-441d-bdbf-33ccb117d6d7).

![](https://blog.nviso.eu/wp-content/uploads/2026/11/image-3.png)

ZQAgent’s command-line spoofing.

ZQAgent’s command-line spoofing results in the following spoofed process, without being linked to the original executable.

```
/usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
```

```
/usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
```

Additional runtime evasion strategies include the dynamic encryption of configuration settings, only temporarily decrypted when evaluated, as well as the usage of multiple network encryption layers (e.g., ChaCha20 variants).

### Operator Capabilities

ZQAgent provides its operators with a wide variety of capabilities. The below operation codes constitute most of ZQAgent’s features.

| Codes | Actions |
| --- | --- |
| `0x04`, `0x08` | Get and change the current working directory through `getcwd` and `chdir` |
| `0x0A`, `0x15` | Update some of ZQAgent’s runtime configuration |
| `0x0C` | Move a file, similar to the usage of `cp` |
| `0x0E` | List a directory’s content, similar to the usage of `ls` |
| `0x0F` | List mounted filesystem types |
| `0x11` | Remove a file or directory, similar to the usage of `rm` |
| `0x12` | Rename a file through `rename` |
| `0x16` | Get the current user context, similar to the usage of `id` |
| `0x18` | Read a file’s first 2048 bytes, conceptually similar to the usage of `head` |
| `0x1B` | Create a directory through `mkdir` |
| `0x1C` | Enable, disable or check [ZQAgent’s persistence](#Persistence) |
| `0x25`, `0x26`, `0x27` | Blocking TCP connection management (connecting, sending, closing) |
| `0x29` | Get an arbitrary process’ statistics through `/proc` |
| `0x2A` | Terminate an arbitrary process through `kill` |
| `0x2B` | Start a command as a managed process using `/bin/sh -c` |
| `0x2E` | List all managed processes |
| `0x2F` | Terminate a managed process |
| `0x34` | Create a memory-only (i.e., `memfd`) managed process |
| `0x3E`, `0x3F`, `0x40`, `0x41`, `0x42`, `0x43`, `0x45`, `0x46` | Non-blocking TCP/UDP connection management (connecting, listening, sending, closing, …) |
| `0x47` | Allocate a new managed shell (i.e., `/bin/bash` or, if unavailable, `/bin/sh`) |
| `0x48` | Write to a managed shell’s standard input |

ZQAgent’s operation codes ...