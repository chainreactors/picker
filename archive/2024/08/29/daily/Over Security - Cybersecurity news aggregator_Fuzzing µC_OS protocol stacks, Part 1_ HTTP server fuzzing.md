---
title: Fuzzing µC/OS protocol stacks, Part 1: HTTP server fuzzing
url: https://blog.talosintelligence.com/fuzzing-uc-os-protocol-stacks-part-1/
source: Over Security - Cybersecurity news aggregator
date: 2024-08-29
fetch_date: 2025-10-06T18:07:30.238633
---

# Fuzzing µC/OS protocol stacks, Part 1: HTTP server fuzzing

# Cisco Talos Blog

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

![](/content/images/2024/08/VulnDeepDive--1-.png)

# Fuzzing µC/OS protocol stacks, Part 1: HTTP server fuzzing

By
[Kelly Patterson](https://blog.talosintelligence.com/author/kelly/)

Wednesday, August 28, 2024 12:00

[Vulnerability Deep Dive](/category/vulnerability-deep-dive/)

This is the first post of a three-part series, where we will be delving into the intricacies of fuzzing µC/OS protocol stacks. The techniques I will discuss are universally applicable to various RTOS environments, though our focus will primarily be on µC/OS.

I’ll highlight some of the strategic code modifications I implemented across different µC/OS components. The objective is to streamline the process of developing a fuzzing harness tailored for the µC/HTTP-server. In the second installment of this series, I’ll discuss a technique that I used for delivering multiple requests per fuzz test case. The third post will be like this one, as I’ll describe the code modifications that I made with the aim of fuzzing the µC/TCP-IP stack.

For a bit of context, µC/OS is an RTOS, or “Real-Time Operating System.” An RTOS is a specialized operating system designed to manage hardware resources and host applications that need to run in systems where timing is critical, such as in embedded systems, medical devices, or industrial controls. RTOSes haven’t been fuzzed as thoroughly as software that runs on desktop operating systems, primarily due to the complexities associated with setting up a fuzzing harness for these systems.

Developing a harness for an RTOS requires more coding effort than what is typically required for a straightforward, single-line fuzzing harness used with desktop applications or libraries.

Any vulnerability in an RTOS has the potential to affect many devices across multiple industries. It’s important to put these codebases through the same rigorous testing as is common for desktop operating systems. My hope is that the techniques described in this blog post series will encourage more widespread use of fuzzing of RTOS software components.

Historically fuzzing RTOS code involved a custom hardware setup to fuzz the code in its native environment, or fuzzing on an emulated version of the system. However, when Weston Embedded made the full µC/OS source code openly available in 2020, it sparked my curiosity about whether there could be a less complex approach to fuzz this type of code.

The goals for my fuzzer are:

* Use a modern fuzzing framework (I chose AFL++).
* Modify the networking code to accept input from a file.
* Handle multiple requests per test case (more on this in part 2).

Additionally, the constraints (self-imposed) for my HTTP fuzzer are:

* A software-only solution.
* Run natively on Linux.

With that in mind, I wanted to avoid using emulation or dedicated hardware for my fuzzer.

# Linux port

To make use of a modern fuzzing framework like AFL++, I needed to write some code that would allow the µC/HTTP-server to operate on Linux instead of the native µC/OS kernel. However, I had to give some thought to what exactly I wanted my fuzzer to target and determine appropriate insertion points for my hooks that would enable this protocol implementation to run on Linux.

Below is a basic architecture diagram showing the software component structure of a µC/HTTP-server application. The blue highlight represents the components that I will be modifying to port the application to Linux. The orange highlight represents the code which is the target for the fuzzer.

![](https://blog.talosintelligence.com/content/images/2024/08/FuzzingProtocolStacks-Architecture2.jpg)

The modular design of µC/OS makes it wonderful to work with for this type of fuzzing. The Kernel Abstraction Layer (KAL in the diagram) provides a common API that is utilized by each of their libraries. This makes it easy to create a custom KAL that either mimics the desired RTOS functionalities for my fuzzer or simply returns a success signal for features that aren't relevant to the fuzzing process. Although µC/OS provides a POSIX-compatible KAL that enables the µC/HTTP-server to run on Linux, I chose to create my own KAL interface to simplify the entire setup.

The KAL lays out an API blueprint for operating system components like task management, locks, semaphores, timers, and message queues. In the case of µC/HTTP-server, the only KAL function it calls is `KAL_TaskCreate`, which means I only needed to implement this particular function in my custom KAL interface. Additionally, since the task in question is the main HTTP processing loop, I found a workaround by directly invoking the function itself within the `KAL_TaskCreate` function, bypassing the need for a more complex task creation process. Example code below:

```
void  KAL_TaskCreate (KAL_TASK_HANDLE     task_handle,
                      void              (*p_fnct)(void  *p_arg),
                      void               *p_task_arg,
                      CPU_INT08U          prio,
                      KAL_TASK_EXT_CFG   *p_cfg,
                      RTOS_ERR           *p_err)
{
    /* return success  */
    *p_err = RTOS_ERR_NONE;
    /* fake it and call the function */
    p_fnct(p_task_arg);
    return;
}
```

# Networking port

## Socket reads

Much like the Linux port mentioned earlier, there is a network abstraction called NetSock within µC/OS's TCP/IP protocol suite which is like a POSIX socket in its functionality. For the purposes of this fuzzing project, my attention isn't on probing the underlying TCP/IP stack; instead, I'm focused on the µC/HTTP-server code. To ensure that the fuzzing input is fed directly to the µC/HTTP-server code without first passing through the TCP/IP code, I created a custom NetSock implementation.

My ultimate goal for this fuzzer is to read network data from a file. However, it will simplify...