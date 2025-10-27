---
title: A few notes on AWS Nitro Enclaves: Attack surface
url: https://blog.trailofbits.com/2024/09/24/notes-on-aws-nitro-enclaves-attack-surface/
source: Trail of Bits Blog
date: 2024-09-25
fetch_date: 2025-10-06T18:25:53.124326
---

# A few notes on AWS Nitro Enclaves: Attack surface

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# A few notes on AWS Nitro Enclaves: Attack surface

[Paweł Płatek](https://github.com/GrosQuildu)

September 24, 2024

[application-security](/categories/application-security/), [research-practice](/categories/research-practice/), [confidential-computing](/categories/confidential-computing/)

Page content

* [A brief threat model](#a-brief-threat-model)
* [Vsocks](#vsocks)
* [Randomness](#randomness)
* [Side channels](#side-channels)
* [CPU memory side channels](#cpu-memory-side-channels)
* [Memory](#memory)
* [Time](#time)
* [Why kvm-clock?](#why-kvm-clock)
* [Attestation](#attestation)
* [The NSM driver](#the-nsm-driver)
* [That’s (not) all folks](#thats-not-all-folks)

In the race to secure cloud applications, AWS Nitro Enclaves have emerged as a powerful tool for isolating sensitive workloads. But with
great power comes great responsibility—and potential security pitfalls. As pioneers in confidential computing security, we at Trail of Bits
have scrutinized the attack surface of AWS Nitro Enclaves, uncovering potential bugs that could compromise even these hardened environments.

This post distills our hard-earned insights into actionable guidance for developers deploying Nitro Enclaves. After reading, you’ll be equipped to:

* Identify and mitigate key security risks in your enclave deployment
* Implement best practices for randomness, side-channel protection, and time management
* Avoid common pitfalls in virtual socket handling and attestation

We’ll cover a number of topics, including:

* [Virtual socket security](#vsocks)
* [Randomness and entropy sources](#randomness)
* [Side-channel attack mitigations](#side-channels)
* [Memory management](#memory)
* [Time source considerations](#time)
* [Attestation best practices](#attestation)
* [NSM driver security](#the-nsm-driver)

Whether you’re new to Nitro Enclaves or looking to harden existing deployments, this guide will help you navigate the unique security landscape of confidential computing on AWS.

## A brief threat model

First, a brief threat model. Enclaves can be attacked from the parent Amazon EC2 instance, which is the only component that has direct access to an enclave. In the context of an attack on an enclave, we should assume that the parent instance’s kernel (including its [`nitro_enclaves` drivers](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/virt/nitro_enclaves?id=793f55b2971e3a95d77ad08e9da2a3dc6c946cd7)) is controlled by the attacker. DoS attacks from the instance are not really a concern, as the parent can always shut down its enclaves.

If the EC2 instance forwards user traffic from the internet, then attacks on its enclaves could come from that direction and could involve
all the usual attack vectors (business logic, memory corruption, cryptographic, etc.). And in the other direction, users could be targeted
by malicious EC2 instances with impersonation attacks.

In terms of trust zones, an enclave should be treated as a single trust zone. Enclaves run normal Linux and can theoretically use its access
control features to “drive lines” within themselves. But that would be pointless—adversarial access (e.g., via a supply-chain attack) to
anything inside the enclave would diminish the benefits of its strong isolation and of attestation. Therefore, compromise of a single
enclave component should be treated as a total enclave compromise.

Finally, the hypervisor is trusted—we must assume it behaves correctly and not maliciously.

![Figure 1: A simplified model of the AWS Nitro Enclaves system](/img/wpdump/25118b5dc77a15c5cb7e692bf67c60cd.png)

Figure 1: A simplified model of the AWS Nitro Enclaves system

## Vsocks

The main entrypoint to an enclave is the local [virtual socket](https://archive.fosdem.org/2021/schedule/event/vai_virtio_vsock/) (vsock). Only the parent EC2 instance can use the socket. Vsocks are managed by the hypervisor—the hypervisor provides the parent EC2 instance’s and the enclave’s kernels with `/dev/vsock` device nodes.

Vsocks are identified by a context identifier (CID) and port. Every enclave must use a unique CID, which can be set during initialization
and can listen on multiple ports. There are a few predefined CIDs:

* `VMADDR_CID_HYPERVISOR` = 0
* `VMADDR_CID_LOCAL` = 1
* `VMADDR_CID_HOST` = 2
* `VMADDR_CID_PARENT`= 3 (the parent EC2 instance)
* `VMADDR_CID_ANY` = `0xFFFFFFFF` = -1U (listen on all CIDs)

Enclaves usually use only the `VMADDR_CID_PARENT CID` (to send data) and the `VMADDR_CID_ANY CID` (to listen for data). An example use of the `VMADDR_CID_PARENT` can be found in the [`init.c` module](https://github.com/aws/aws-nitro-enclaves-sdk-bootstrap/blob/ac43d103ba0f98044bf760477c088f1dc6f3702d/init/init.c#L410-L410) of AWS’s enclaves SDK—the enclave sends a “heartbeat” signal to the parent EC2 instance just after initialization. The signal is [handled by the `nitro-cli`](https://github.com/aws/aws-nitro-enclaves-cli/blob/c4fafb2320bc13d1e74e6ba2c1b6ef840cba0988/eif_loader/src/lib.rs#L54-L56) tool.

**Standard socket-related issues are the main issues to worry about when it comes to vsocks.**
When developing an enclave, consider the following to ensure such issues cannot enable certain attack vectors:

* Does the enclave accept connections asynchronously (with multithreading)? If not, a single user may block other users from accessing the enclave for a long period of time.
* Does the enclave time out connections? If not, a single user may persistently occupy a socket or open multiple connections to the enclave and drain available resources (like file descriptors).
* If the enclave uses multithreading, is its state synchronization correctly implemented?
* Does the enclave handle errors correctly? Reading from a socket with the [`recv` method](https://man7.org/linux/man-pages/man2/recvmsg.2.html) is especially tricky. A [common pattern is to loop](https://github.com/aws/aws-nitro-enclaves-cli/blob/c4fafb2320bc13d1e74e6ba2c1b6ef840cba0988/samples/command_executer/src/protocol_helpers.rs#L51-L65) over the `recv` call until the desired number of bytes is received, but this pattern should be carefully implemented:
  + If the [`EINTR` error is returned](https://android.googlesource.com/platform/bionic/%2B/master/docs/EINTR.md), the enclave should retry the `recv` call. Otherwise, the enclave may drop valid and live connections.
  + If there is no error but the returned length is 0, the enclave should break the loop. Otherwise, the peer [may shut down the connection](https://github.com/aws/aws-nitro-enclaves-cli/pull/609) before sending the expected number of bytes, making the enclave loop infinitely.
  + If the socket is non-blocking, then reading data correctly is even more tricky.

The main risk of these issues is DoS. The parent EC2 instance may shut down any of its enclaves, so the actual risks are present only if a DoS can be triggered by external users. Providing timely access to the system is the responsibility of both the enclave and the EC2 instance communicating with the enclave.

Another vulnerability class involving vsocks is CID confusion: if an EC2 instance runs multiple enclaves, it may send data to the wrong one (e.g., due to a race condition issue). However, even if such a bug exists, it should not pose much risk or contribute much to an enclave’s attack surface, because traffic between users and the enclave should be authenticated end to end.

Finally, note that enclaves use the `SOCK_STREAM` socket type by default. If you change the type to `SOCK_DGRAM`, do some research to learn about the security properties of this communication type.

## Randomness

Enclaves must have access to secure randomness. The word “secure” in this context means that adversaries don’t know or control all the entropy used to produce random data. On Linux, [a few entropy sources](https://e...