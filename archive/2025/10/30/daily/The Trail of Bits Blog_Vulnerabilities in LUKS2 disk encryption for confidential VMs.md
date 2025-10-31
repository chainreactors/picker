---
title: Vulnerabilities in LUKS2 disk encryption for confidential VMs
url: https://blog.trailofbits.com/2025/10/30/vulnerabilities-in-luks2-disk-encryption-for-confidential-vms/
source: The Trail of Bits Blog
date: 2025-10-30
fetch_date: 2025-10-31T03:12:52.430163
---

# Vulnerabilities in LUKS2 disk encryption for confidential VMs

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Vulnerabilities in LUKS2 disk encryption for confidential VMs

Tjaden Hess

October 30, 2025

[vulnerability-disclosure](/categories/vulnerability-disclosure/), [confidential-computing](/categories/confidential-computing/), [cryptography](/categories/cryptography/), [vulnerabilities](/categories/vulnerabilities/), [linux](/categories/linux/), [exploits](/categories/exploits/)

Page content

* [Confidential VMs](#confidential-vms)
* [The LUKS2 on-disk format](#the-luks2-on-disk-format)
* [LUKS, ma—No keys](#luks-mano-keys)
* [Validating LUKS metadata](#validating-luks-metadata)
* [Coordinated disclosure](#coordinated-disclosure)

Trail of Bits is disclosing vulnerabilities in eight different confidential computing systems that use Linux Unified Key Setup version 2 (LUKS2) for disk encryption. Using these vulnerabilities, a malicious actor with access to storage disks can extract all confidential data stored on that disk and can modify the contents of the disk arbitrarily. The vulnerabilities are caused by malleable metadata headers that allow an attacker to trick a trusted execution environment guest into encrypting secret data with a null cipher.
The following CVEs are associated with this disclosure:

* [CVE-2025-59054](https://nvd.nist.gov/vuln/detail/CVE-2025-59054)
* [CVE-2025-58356](https://nvd.nist.gov/vuln/detail/CVE-2025-58356)

This is a coordinated disclosure; we have notified the following projects, which remediated the issues prior to our publication.

* Oasis Protocol: [`oasis-sdk`](https://github.com/oasisprotocol/oasis-sdk/releases/tag/rofl-containers/v0.7.2dk/) (v0.7.2)
* Phala Network: [`dstack`](https://github.com/Dstack-TEE/dstack/releases/tag/v0.5.4) (v0.5.4)
* Flashbots TDX: [`tdx-init`](https://github.com/flashbots/tdx-init/releases/tag/v0.2.0) (v0.2.0)
* Secret Network: [`secret-vm-ops`](https://github.com/scrtlabs/secret-vm-ops)
* Fortanix Salmiac: [`salmiac`](https://github.com/fortanix/salmiac)
* Edgeless Constellation: [`constellation`](https://github.com/edgelesssys/constellation/releases/tag/v2.24.0) (v2.24.0)
* Edgeless Contrast: [`contrast`](https://github.com/edgelesssys/contrast) (v1.12.1, v1.13.0)
* Cosmian VM: [`cosmian-vm`](https://github.com/Cosmian/cosmian_vm)

We [notified the maintainers of `cryptsetup`](https://gitlab.com/cryptsetup/cryptsetup/-/issues/954), resulting in a partial mitigation introduced in `cryptsetup` v2.8.1.

We also notified the Confidential Containers project, who indicated that the relevant code, part of the [`guest-components`](https://github.com/confidential-containers/guest-components) repository, is not currently used in production.

Users of these confidential computing frameworks should update to the latest version. Consumers of remote attestation reports should disallow pre-patch versions in attestation reports.

Exploitation of this issue requires write access to encrypted disks. We do not have any indication that this issue has been exploited in the wild.

These systems all use trusted execution environments such as AMD SEV-SNP and Intel TDX to protect a confidential Linux VM from a potentially malicious host. Each relies on LUKS2 to protect disk volumes used to hold the VM’s persistent state. LUKS2 is a disk encryption format originally designed for at-rest encryption of PC and server hard disks. We found that LUKS is not always secure in settings where the disk is subject to modifications by an attacker.

## Confidential VMs

The affected systems are Linux-based confidential virtual machines (CVMs). These are not interactive Linux boxes with user logins; they are specialized automated systems designed to handle secrets while running in an untrusted environment. Typical use cases are private AI inference, private blockchains, or multi-party data collaboration. Such a system should satisfy the following requirements:

1. Confidentiality: The host OS should not be able to read memory or data inside the CVM.
2. Integrity: The host OS should not be able to interfere with the logical operation of the CVM.
3. Authenticity: A remote party should be able to verify that they are interacting with a genuine CVM running the expected program.

Remote users verify the authenticity of a CVM via a remote attestation process, in which the secure hardware generates a “quote” signed by a secret key provisioned by the hardware manufacturer. This quote contains measurements of the CVM configuration and code. If an attacker with access to the host machine can read secret data from the CVM or tamper with the code it runs, the security guarantees of the system are broken.

The confidential computing setting turns typical trust assumptions on their heads. Decades of work has gone into protecting host boxes from malicious VMs, but very few Linux utilities are designed to protect a VM from a malicious host. The issue described in this post is just one trap in a broader minefield of unsafe patterns that CVM-based systems must navigate. If your team is building a confidential computing solution and is concerned about unknown footguns, we are happy to offer a free [office hours call](https://share.hsforms.com/1VVGPLTjiRduOpGNOh2sHUgdffjk) with one of our engineers.

## The LUKS2 on-disk format

A disk using the LUKS2 encryption format starts with a header, followed by the actual encrypted data. The header contains two identical copies of binary and JSON-formatted metadata sections, followed by some number of keyslots.![“Figure 1: LUKS2 on-disk encryption format”](/img/luks2-vuln-disclosure/luks2-disclosure-1.png)

Figure 1: LUKS2 on-disk encryption format

Each keyslot contains a copy of the volume key, encrypted with a single user password or token. The JSON metadata section defines which keyslots are enabled, what cipher is used to unlock each keyslot, and what cipher is used for the encrypted data segments.

Here is a typical JSON metadata object for a disk with a single keyslot. The keyslot uses Argon2id and AES-XTS to encrypt the volume key under a user password. The segment object defines the cipher used to encrypt the data volume. The digest object stores a hash of the volume key, which `cryptsetup` uses to check whether the correct passphrase was provided.

![“Figure 2: Example JSON metadata object for a disk with a single keyslot”](/img/luks2-vuln-disclosure/luks2-disclosure-2.png)

Figure 2: Example JSON metadata object for a disk with a single keyslot

## LUKS, ma—No keys

By default, LUKS2 uses AES-XTS encryption, a standard mode for size-preserving encryption. What other modes might be supported? As of `cryptsetup` version 2.8.0, the following header would be accepted.![“Figure 3: Acceptable header with encryption set to cipher_null-ecb”](/img/luks2-vuln-disclosure/luks2-disclosure-3.png)

Figure 3: Acceptable header with encryption set to cipher\_null-ecb

The `cipher_null-ecb` algorithm does nothing. It ignores its key and returns data unchanged. In particular, it simply ignores its key and acts as the identity function on the data. Any attacker can change the cipher, fiddle with some digests, and hand the resulting disk to an unsuspecting CVM; the CVM will then use the disk as if it were securely encrypted, reading configuration data from and writing secrets to the completely unencrypted volume.

When a null cipher is used to encrypt a keyslot, that keyslot can be successfully opened with *any* passphrase. In this case, the attacker does not need any information about the CVM’s encryption keys to produce a malicious disk.

We disclosed this issue to the `cryptsetup` maintainers, who warned that LUKS is not intended to provide integrity in this setting and asserted that the presence of null ciphers is important for backward compatibility. In `cryptsetup` 2.8.1 and higher, null ciphers are now rejected as keyslot ciphers when used with a nonempty password.

Nu...