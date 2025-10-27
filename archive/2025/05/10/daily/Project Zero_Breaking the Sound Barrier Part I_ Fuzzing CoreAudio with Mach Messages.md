---
title: Breaking the Sound Barrier Part I: Fuzzing CoreAudio with Mach Messages
url: https://googleprojectzero.blogspot.com/2025/05/breaking-sound-barrier-part-i-fuzzing.html
source: Project Zero
date: 2025-05-10
fetch_date: 2025-10-06T22:29:36.043607
---

# Breaking the Sound Barrier Part I: Fuzzing CoreAudio with Mach Messages

# [Project Zero](https://googleprojectzero.blogspot.com/)

News and updates from the Project Zero team at Google

## Friday, May 9, 2025

### Breaking the Sound Barrier Part I: Fuzzing CoreAudio with Mach Messages

Guest post by Dillon Franke, Senior Security Engineer, 20% time on Project Zero

Every second, highly-privileged MacOS system daemons accept and process hundreds of IPC messages. In some cases, these message handlers accept data from sandboxed or unprivileged processes.

In this blog post, I’ll explore using Mach IPC messages as an attack vector to find and exploit sandbox escapes. I’ll detail how I used a custom fuzzing harness, dynamic instrumentation, and plenty of debugging/static analysis to identify a high-risk type confusion vulnerability in the coreaudiod system daemon. Along the way, I’ll discuss some of the difficulties and tradeoffs I encountered.

Transparently, this was my first venture into the world of MacOS security research and building a custom fuzzing harness. I hope this post serves as a guide to those who wish to embark on similar research endeavors.

I am open-sourcing the fuzzing harness I built, as well as several tools I wrote that were useful to me throughout this project. All of this can be found here: <https://github.com/googleprojectzero/p0tools/tree/master/CoreAudioFuzz>

# The Approach: Knowledge-Driven Fuzzing

For this research project, I adopted a hybrid approach that combined fuzzing and manual reverse engineering, which I refer to as knowledge-driven fuzzing. This method, learned from my friend [Ned Williamson](https://x.com/NedWilliamson), balances automation with targeted investigation. Fuzzing provided the means to quickly test a wide range of inputs and identify areas where the system’s behavior deviated from expectations. However, when the fuzzer’s code coverage plateaued or specific hurdles arose, manual analysis came into play, forcing me to dive deeper into the target’s inner workings.

Knowledge-driven fuzzing offers two key advantages. First, the research process never stagnates, as the goal of improving the code coverage of the fuzzer is always present. Second, achieving this goal requires a deep understanding of the code you are fuzzing. By the time you begin triaging legitimate, security-relevant crashes, the reverse engineering process will have given you extensive knowledge of the codebase, enabling analysis of crashes from an informed perspective.

The cycle I followed during this research is as follows:

1. Identify an attack vector
2. Choose a target
3. Create a fuzzing harness
4. Fuzz and produce crashes
5. Analyze crashes and code coverage
6. Iterate on the fuzzing harness
7. Repeat steps 4-6

# Identify an Attack Vector

Standard browser sandboxing limits code execution by restricting direct operating system access. Consequently, exploiting a browser vulnerability typically requires the use of a separate “sandbox escape” vulnerability.

Since interprocess communication (IPC) mechanisms allow two processes to communicate with each other, they can naturally serve as a bridge from a sandboxed process to an unrestricted one. This makes them a prime attack vector for sandbox escapes, as shown below.

[![A diagram illustrating SANDBOX ESCAPE and PRIVILEGE ESCALATION. The sandbox escape shows a Web Browser Process within a SANDBOX RESTRICTED communicating with a Message Handler via MACH IPC. The privilege escalation shows an Unprivileged Process communicating with a Message Handler Highly Privileged Process via MACH IPC.](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_h5AXJEFTBHQa0PFGnpwzqggpFbxNHIXMlCga7afZdi-qtzdBRGEy1v5c7a_b48JI3mY7LNicZihUBDB6cUHPnLhnLW1ReCSJVQq9sksmL1Y3CSHEGwTT28i8vgwgrvJPeLo2bf0RxEpLx4uO3OjMDVuqlIbvIO-GORZ5KsVC8MBF-94lUSThyphenhyphen_euKIo/s600/unnamed.png "A diagram illustrating SANDBOX ESCAPE and PRIVILEGE ESCALATION. The sandbox escape shows a Web Browser Process within a SANDBOX RESTRICTED communicating with a Message Handler via MACH IPC. The privilege escalation shows an Unprivileged Process communicating with a Message Handler Highly Privileged Process via MACH IPC.")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi_h5AXJEFTBHQa0PFGnpwzqggpFbxNHIXMlCga7afZdi-qtzdBRGEy1v5c7a_b48JI3mY7LNicZihUBDB6cUHPnLhnLW1ReCSJVQq9sksmL1Y3CSHEGwTT28i8vgwgrvJPeLo2bf0RxEpLx4uO3OjMDVuqlIbvIO-GORZ5KsVC8MBF-94lUSThyphenhyphen_euKIo/s647/unnamed.png)

I chose Mach messages, the lowest level IPC component in the MacOS operating system, as the attack vector of focus for this research. I chose them mostly due to my desire to understand MacOS IPC mechanisms at their most core level, as well as the track record of historical security issues with Mach messages.

## Previous Work and Background

Leveraging Mach messages in exploit chains is far from a novel idea. For example, Ian Beer [identified a core design issue](https://googleprojectzero.blogspot.com/2016/10/taskt-considered-harmful.html) in 2016 with the XNU kernel related to the handling of task\_t Mach ports, which allowed for exploitation via Mach messages. [Another post](https://googleprojectzero.blogspot.com/2019/08/in-wild-ios-exploit-chain-2.html) showed how an in-the-wild exploit chain utilized Mach messages in 2019 for heap grooming techniques. I also drew much inspiration from Ret2 Systems’ [blog post](https://blog.ret2.io/2018/06/05/pwn2own-2018-exploit-development/) about leveraging Mach message handlers to find and weaponize a Safari sandbox escape.

I won’t spend too much time detailing the ins and outs of how Mach messages work, (that is better left to a more [comprehensive post](https://dmcyk.xyz/post/xnu_ipc_i_mach_messages/) on the subject) but here’s a brief overview of Mach IPC for this blog post:

1. Mach messages are stored within kernel-managed message queues, represented by a Mach port
2. A process can fetch a message from a given port if it holds the receive right for that port
3. A process can send a message to a given port if it holds a send right to that port

MacOS applications can register a service with the bootstrap server, a special mach port which all processes have a send right to by default. This allows other processes to send a Mach message to the bootstrap server inquiring about a specific service, and the bootstrap server can respond with a send right to that service’s Mach port. MacOS system daemons register Mach services via launchd. You can view their .plist files within the /System/Library/LaunchAgents and /System/Library/LaunchDaemons directories to get an idea of the services registered. For example, the .plist file below highlights a Mach service registered for the Address Book application on MacOS using the identifier com.apple.AddressBook.AssistantService.

<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">

<plist version="1.0">

<dict>

        <key>POSIXSpawnType</key>

        <string>Adaptive</string>

        <key>Label</key>

        <string>com.apple.AddressBook.AssistantService</string>

        <key>MachServices</key>

        <dict>

                <key>com.apple.AddressBook.AssistantService</key>

                <true/>

        </dict>

        <key>ProgramArguments</key>

        <array>

                <string>/System/Library/Frameworks/AddressBook.framework/Versions/A/Helpers/ABAssistantService.app/Contents/MacOS/ABAssistantService</string>

        </array>

</dict>

</plist>

# Choose a Target

After deciding I wanted to research Mach services, the next question was which service to target. In order for a sandboxed process to send Mach messages to a service, it has to be explicitly allowed. If the process is using Apple’s App Sandbox feature, this is done within a .sb file, written using the [TinyScheme](https://tinyscheme.sourceforge.net/home.html) format. The snippet below shows an excerpt of the sandbox file for a WebKit GPU Process. The allow m...