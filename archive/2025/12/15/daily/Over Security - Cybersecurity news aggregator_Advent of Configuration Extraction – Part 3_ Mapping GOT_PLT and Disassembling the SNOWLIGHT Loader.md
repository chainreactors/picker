---
title: Advent of Configuration Extraction – Part 3: Mapping GOT/PLT and Disassembling the SNOWLIGHT Loader
url: https://blog.sekoia.io/advent-of-configuration-extraction-part-3-mapping-got-plt-and-disassembling-the-snowlight-loader/
source: Over Security - Cybersecurity news aggregator
date: 2025-12-15
fetch_date: 2025-12-16T03:24:22.264547
---

# Advent of Configuration Extraction – Part 3: Mapping GOT/PLT and Disassembling the SNOWLIGHT Loader

### Log in

Username or Email Address

Password

[ ]  Remember Me

 [Forgot password?](https://blog.sekoia.io/wp-login.php?action=lostpassword)

### Search the site...

Search for

* All categories
* [Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [SOC Insights & Other News](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Detection Engineering](https://blog.sekoia.io/category/detection-engineering/)

####

Reset

[![logo sekoia.io blog light](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2023/03/cropped-logo-sekoia-io-blog-light.png)](https://blog.sekoia.io/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

* [Threat Research](https://blog.sekoia.io/category/threat-research/)
* [Detection](https://blog.sekoia.io/category/detection-engineering/)
* [Product News](https://blog.sekoia.io/category/product-news/)
* [Other](https://blog.sekoia.io/category/soc-insights-other-news/)
* [Sign up](https://go.sekoia.io/Preference-center-EN.html)
* [About Sekoia.io](https://www.sekoia.io/en/about/)
  + [TDR Team](https://www.sekoia.io/en/about-threat-detection-research-team/)
  + [AI-SOC platform](https://www.sekoia.io/en/homepage/)
  + [Interactive demo](https://sekoia.storylane.io/share/8zdjfok9atpn)
  + [Contact Us](https://www.sekoia.io/en/contact/)

Log in

[Threat Research & Intelligence](https://blog.sekoia.io/category/threat-research/ "Threat Research & Intelligence")

# Advent of Configuration Extraction – Part 3: Mapping GOT/PLT and Disassembling the SNOWLIGHT Loader

[![](https://t7f4e9n3.delivery.rocketcdn.me/wp-content/uploads/2024/07/TDR-badge2.png)](#molongui-disabled-link)

[Jeremy Scion, Pierre Le Bourhis and Sekoia TDR](#molongui-disabled-link)
December 15 2025

0

12 minutes reading

In the third part of our series “Advent of Configuration Extraction”, we dissect **SNOWLIGHT**, a lightweight ELF downloader designed to retrieve and execute a remote payload on Linux systems.

To extract the SNOWLIGHT configuration, and specifically the Command and Control (C2) port, we need to disassemble the main function and identify calls to dynamically imported functions based on their addresses. This requires resolving the mapping between the **Global Offset Table** and the **Procedure Linkage Table**, which allows us to associate each entry with the name of the imported function.

To perform this step reliably and automatically, the extractor relies on two powerful tools: **LIEF** for parsing the ELF format, and **Capstone** for disassembling the machine code.

# SNOWLIGHT

**SNOWLIGHT** is the identifier assigned by [Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/initial-access-brokers-exploit-f5-screenconnect?hl=en) to a lightweight ELF downloader designed to retrieve and execute a remote payload on Linux systems. Developed in C and measuring less than 10 KiloBytes, SNOWLIGHT communicates with its Command and Control server over a raw TCP socket, using a port that varies across samples.

Its initial action is to transmit a 6 bytes message to the C2, containing a short architecture  pattern followed by padding. This pattern consists of a single letter indicating the processor family, **i** for Intel and **a** for ARM, followed by the architecture size 32 or 64 bits, resulting in one of the following values: l32, l64, a32 or a64.The server responds with a XOR-encoded payload, currently using the hardcoded key **0x99**. SNOWLIGHT then decodes the payload and executes it entirely in memory through the memfd\_create and fexecve system calls, leaving no artifacts on the disk.

Early variants observed from August 2025 also include an access check on the file located at /tmp/log\_de.log and terminate if this file is not accessible. Recent reporting indicates that SNOWLIGHT has been incorporated into intrusion campaigns attributed to the threat actor **UNC5174**, where it serves as an in-memory loader for the remote access trojan the **[VShell](https://www.sysdig.com/blog/unc5174-chinese-threat-actor-vshell)**.

## Snowlight Configuration Access Logic

To build the configuration extractor, an initial manual analysis of several samples is required to understand how the malware accesses and parses its configuration.

For this study, a static analysis was performed on the following sample: SHA-256: 344c391cfd4fd30407bf55872d05d44b679a117e407114c0e113b3c6c4cbbb29

SNOWLIGHT sample analysis was compiled with intact symbols and showed no signs of obfuscation. Because SNOWLIGHT is a downloader, the primary piece of information to extract from its configuration is the C2 server address, which the malware contacts to send an architecture identifier and retrieve the next stage. In our analysis, the extractor targets the x86\_64 version.

The SNOWLIGHT binary contains the main function, where the malware initialises a sockaddr\_in structure holding the C2 address. The IP is stored directly in the .rodata section and copied into the structure before the call to gethostbyname. The assembly analysis also shows that the TCP port is explicitly set via the following instruction:

```
mov     word ptr [addr.sa_data], 811Fh  // <- sin_port
call    _gethostbyname
```

*Code 1. I*nstruction preceding gethostbyname function**

This value, stored in little‑endian format, corresponds to port **8065**. The subsequent call to gethostbyname is used solely to resolve the IP address or domain name that has already been loaded into the structure.

Extraction of the configuration begins by parsing the .rodata section to locate the C2 address. In all samples analysed, the C2 value consistently appears immediately after the string “[kworker/0:2]”. The .rodata section also contains the architecture identifier (the *magic* value), which in this case is “l64”, as the sample is an **x86\_64** executable.

To obtain the port number, the extractor iterates over the instructions of the function main to identify the call to gethostbyname. The instruction immediately preceding this call contains the port value stored in the sockaddr\_in structure. To locate the gethostbyname call, the extractor must resolve the mapping between the **Global Offset Table (GOT)** and the **Procedure Linkage Table (PLT)**. The GOT is a table of addresses used by the program to reference dynamically linked functions, while the PLT contains the actual code that jumps to these functions at runtime. Resolving the mapping between the GOT and PLT is essential to associate each PLT entry with its corresponding imported function name, including gethostbyname.

# Automating the Configuration Extraction

To perform the operations required for configuration extraction (parsing .rodata, resolving GOT/PLT, and disassembling), we rely on two tools: **LIEF** and **Capstone**.

**[LIEF](https://lief.re/)** is a cross‑platform library designed for parsing, modifying, and abstracting executable formats such as ELF, PE, and Mach‑O. It provides programmatic access to low‑level binary structures, including headers, sections, symbols, and relocation tables. LIEF is commonly used in malware analysis, reverse engineering, and binary instrumentation because it can accurately reconstruct internal metadata and allows controlled modifications without breaking binary integrity.

**[Capstone](https://www.capstone-engine.org/...