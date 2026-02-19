---
title: “Good enough” emulation: Fuzzing a single thread to uncover vulnerabilities
url: https://blog.talosintelligence.com/good-enough-emulation/
source: Over Security - Cybersecurity news aggregator
date: 2026-02-18
fetch_date: 2026-02-19T04:21:53.175004
---

# “Good enough” emulation: Fuzzing a single thread to uncover vulnerabilities

[Blog](/)

[ ]

* [Intelligence Center](https://talosintelligence.com/reputation)

  [ ]

  + [# Intelligence Center](https://talosintelligence.com/reputation)
  + BACK
  + [Intelligence Search](https://talosintelligence.com/reputation_center)
  + [Email & Spam Trends](https://talosintelligence.com/reputation_center/email_rep)
* [Vulnerability Research](https://talosintelligence.com/vulnerability_info)

  [ ]

  + [# Vulnerability Research](https://talosintelligence.com/vulnerability_info)
  + BACK
  + [Vulnerability Reports](https://talosintelligence.com/vulnerability_reports)
  + [Microsoft Advisories](https://talosintelligence.com/ms_advisories)
* [Incident Response](https://talosintelligence.com/incident_response)

  [ ]

  + [# Incident Response](/incident_response)
  + BACK
  + [Reactive Services](https://talosintelligence.com/incident_response/services#reactive-services)
  + [Proactive Services](https://talosintelligence.com/incident_response/services#proactive-services)
  + [Emergency Support](https://talosintelligence.com/incident_response/contact)
* [Blog](https://blog.talosintelligence.com)
* [Support](https://support.talosintelligence.com)

More

* Security Resources

  [ ]

  # Security Resources

  + BACK

  Security Resources
  + [Open Source Security Tools](https://talosintelligence.com/software)
  + [Intelligence Categories Reference](https://talosintelligence.com/categories)
  + [Secure Endpoint Naming Reference](https://talosintelligence.com/secure-endpoint-naming)
* Media

  [ ]

  # Media

  + BACK

  Media
  + [Talos Intelligence Blog](https://blog.talosintelligence.com)
  + [Threat Source Newsletter](https://blog.talosintelligence.com/category/threat-source-newsletter/)
  + [Beers with Talos Podcast](https://talosintelligence.com/podcasts/shows/beers_with_talos)
  + [Talos Takes Podcast](https://talosintelligence.com/podcasts/shows/talos_takes)
  + [Talos Videos](https://www.youtube.com/channel/UCPZ1DtzQkStYBSG3GTNoyfg/featured)
* Company

  [ ]

  # Company

  + BACK

  Company
  + [About Talos](https://talosintelligence.com/about)
  + [Careers](https://talosintelligence.com/careers)

# “Good enough” emulation: Fuzzing a single thread to uncover vulnerabilities

By
[Kelly Patterson](https://blog.talosintelligence.com/author/kelly/)

Wednesday, February 18, 2026 06:00

[Vulnerability Deep Dive](https://blog.talosintelligence.com/category/vulnerability-deep-dive/)

* A Cisco Talos researcher worked around the limitations of hardware-level Code Read-out Protection (RDP) on the Socomec DIRIS M-70 gateway by pivoting from physical debugging to a "good enough" emulation approach.
* By focusing on emulating only the single thread responsible for Modbus protocol handling rather than the entire system, the author demonstrates how a streamlined emulation strategy can effectively surface vulnerabilities in complex industrial Internet of Things (IoT) devices.
* The post highlights the integration of the Unicorn Engine and AFL for coverage-guided fuzzing, as well as the use of the Qiling framework to visualize code coverage and perform root cause analysis on crashes.
* This research led to the discovery of six CVEs related to denial-of-service vulnerabilities, all of which have been patched by the manufacturer through Cisco’s Coordinated Disclosure Policy.

---

This blog describes efforts at emulating functionality of the Socomec DIRIS M-70 gateway to discover vulnerabilities. In vulnerability research, knowing which tool to use for the job at hand is crucial. This post will highlight multiple emulation tools and approaches used, detail the benefits and drawbacks of each, and reveal how a "good enough" approach can really pay off.

## Project background

The M-70 gateway facilitates data communication over both RS485 and Ethernet networks, supporting a wide array of industrial communication protocols, including Modbus RTU, Modbus TCP, BACnet IP, and SNMP (v1, v2, and v3). This gateway is vital for energy management in sectors like critical infrastructure, data centers, healthcare, and the general energy sector. However, as an industrial Internet-of-Things (IIoT) device, vulnerabilities in the M-70 or similar gateways can lead to severe consequences, including operational disruption, financial losses, and manipulation of industrial processes. These risks are severe, especially in critical infrastructure where a compromised gateway could lead to widespread outages or equipment damage.

This large attack surface, the impact of vulnerabilities, and the fact that the M-70 gateway runs the real-time operating system (RTOS) µC/OS-III, made it an attractive research target. There was an expectation that prior familiarity with this RTOS, gained through [previous work](https://blog.talosintelligence.com/fuzzing-uc-os-protocol-stacks/), would offer an advantage in understanding the device’s intricacies.

## Why emulate? The debugging roadblock

Having insight into the system is critical to performing root cause analysis of any discovered vulnerabilities. Ideally, one would have real hardware and the ability to debug the software running on that hardware. The presence of an unpopulated JTAG header on the board was an exciting initial find.

![](https://blog.talosintelligence.com/content/images/2026/02/jtag_header_fig1.png)

Figure 1. Unpopulated JTAG header.

However, the presence of a JTAG header does not always guarantee debug access. There are a variety of reasons for this, but in the case of the M-70 gateway, code read-out protection (RDP) Level 1 is enabled. This is a feature of STM32 microcontrollers, which provides flash memory protection. There are three possible levels (0 – 2) of this protection. Level 1 prevents flash memory reads while debugger access is detected (e.g., JTAG). When attached via JTAG, no access to Flash memory is permitted, essentially preventing debugging of the running software. The intention behind this protection is to prevent third parties (like myself) from dumping the contents of flash via JTAG.

This was bad news. It was not possible to step through the code processing malicious network messages to determine the cause of device disruption. The address for the `$pc` register (see Figure 2) indicates that the MCU has entered a core lock-up state.

![](https://blog.talosintelligence.com/content/images/2026/02/rdp_output_fig2.png)

Figure 2. RDP Level 1 debug output.

In this project, two significant opportunities arose regarding code and memory access. First, an unencrypted firmware update file was available, providing the code that would be written to flash and eliminating the need to read it directly from memory. The second is that the ability to access SRAM while a debugger is attached is allowed with RDP Level 1 enabled (see Figure 2). This made it feasible to dump the contents of SRAM during the device’s execution and capture a snapshot of dynamic data.

![](https://blog.talosintelligence.com/content/images/2026/02/dumpram_fig3.png)

Figure 3. RAM dumping script.

While it was not possible to have fine-grained control over the processor’s state when dumping the SRAM contents, some influence could be exerted (e.g., opening a TCP connection with the device before dumping the SRAM contents). The objects and data created as a result of this connection would be present when the CPU was halted for the SRAM dump.

## Emulating with Unicorn

Emulation is one solution to this inability to debug the software natively. If the processing code of interest can be emulated, it is possible to gain visibility into the effects of a malicious message on the state of the M-70. When emulating software, it’s important to recognize that the emulated code might not behave exactly like it would on the physical device. Full system emulation aims to mitigate this by mimicking device behavior as closely as possible, but it requires deep knowledge of system internals and significant development to accurately emulate peripherals. The focus f...