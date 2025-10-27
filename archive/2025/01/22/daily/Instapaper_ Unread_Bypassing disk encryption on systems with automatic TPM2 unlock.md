---
title: Bypassing disk encryption on systems with automatic TPM2 unlock
url: https://oddlama.org/blog/bypassing-disk-encryption-with-tpm2-unlock/
source: Instapaper: Unread
date: 2025-01-22
fetch_date: 2025-10-06T20:13:13.658482
---

# Bypassing disk encryption on systems with automatic TPM2 unlock

[# oddlama's blog](/)

[Home](/) [GitHub](https://github.com/oddlama) [Matrix](https://matrix.to/#/@oddlama:matrix.org) Mail

[Posts](/blog) [Tags](/tags)

# ð Bypassing disk encryption on systems with automatic TPM2 unlock

2025-01-16 [#security](https://oddlama.org/tags/security/) [#linux](https://oddlama.org/tags/linux/)

Have you setup automatic disk unlocking with TPM2 and
`systemd-cryptenroll` or `clevis`? Then
chances are high that your disk can be decrypted by an attacker who
just has brief physical access to your machine - with some
preparation, 10 minutes will suffice. In this article we will
explore how TPM2 based disk decryption works, and understand why
many setups are vulnerable to a kind of filesystem confusion
attack. We will follow along by exploiting two different real
systems (Fedora + clevis, NixOS + systemd-cryptenroll).

```
# Examples commands used to enroll a key into the TPM. Whether your system is
# suffers from this issue does not depend on which PCRs you choose here.
systemd-cryptenroll --tpm2-pcrs=0+2+7 --tpm2-device=auto <device>
clevis luks bind -d <device> tpm2 '{"pcr_bank":"sha256","pcr_ids":"0,1,2,7"}'
```

**TL;DR:** Most TPM2 unlock setups fail to verify
the LUKS identity of the decrypted partition. Since the initrd must
reside in an unencrypted boot partition, an attacker can inspect it
to learn how it decrypts the disk and also what type of filesystem
it expects to find inside. By recreating the LUKS partition with a
known key, we can confuse the initrd into executing a malicious
`init` executable. Since the TPM state will not be
altered in any way by this fake partition, the original LUKS key
can be unsealed from the TPM. Afterwards, the initial disk state
can be fully restored and then decrypted using the obtained
key.

You are safe if you additionally use a pin to unlock your TPM,
or use an initrd that properly asserts the LUKS identity (which
would involve manual work, so you'd probably know if that is the
case).

## [ð](#the-idea-behind-tpm2-based-disk-decryption) The idea behind TPM2 based disk decryption

The idea behind secure and password-less disk decryption is that
the TPM2 can store an additional LUKS key which your system can
only retrieve, if the TPM is in a predetermined, known-good state.
This state is recorded in the so-called Platform Configuration
Registers (PCRs), of which there are 24 in a standard compliant
TPM. Their intended use is described in the [Linux TPM PCR Registry](https://uapi-group.org/specifications/specs/linux_tpm_pcr_registry/) but also neatly summarized as a table in
the [`systemd-cryptenroll(1)`](https://www.freedesktop.org/software/systemd/man/latest/systemd-cryptenroll.html) man page.

These registers store hashes which are successively updated
while booting based on information like the bootlaoder hash, the
firmware in use, the booted kernel, initrd image and a lot more
things. By establishing a chain of trust through all components
involved in booting up to the linux userspace, we can ensure that
altering any component will affect one or several PCRs. Storing
data in the TPM requires you to select a list of PCRs and it will
ensure that the data can only be retrieved again if all of these
PCRs are in the same state as when enrolling the secret.

Several of these registers have an agreed-upon purpose and are
updated with some specific information about your system, such as
your board's firmware, your BIOS configuration, OptionROMs (extra
firmware loaded from external devices such as PCIe devices after
POST), the secure boot policy, or other things. Here's an excerpt
from the man page from above containing some of the registers that
are important to us:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PCR Name Explanation|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 0 platform-code Core system firmware executable code; changes on firmware updates|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2 external-code Extended or pluggable executable code; includes option ROMs on pluggable hardware|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 7 secure-boot-policy Secure Boot state; changes when UEFI SecureBoot mode is enabled/disabled, or firmware certificates (PK, KEK, db, dbx, â¦) changes.|  |  |  | | --- | --- | --- | | 15 system-identity systemd-cryptsetup(8) optionally measures the volume key of activated LUKS volumes into this PCR. systemd-pcrmachine.service(8) measures the machine-id(5) into this PCR. systemd-pcrfs@.service(8) measures mount points, file system UUIDs, labels, partition UUIDs of the root and /var/ filesystems into this PCR. | | | | | | | | | | | | | | |

Below this list, an interesting piece of information is given in
the man page about the intended use of PCRs for encrypted
volumes:
> In general, encrypted volumes would be bound to some combination
> of PCRs 7, 11, and 14 (if shim/MOK is used). In order to allow
> firmware and OS version updates, it is typically not advisable to
> use PCRs such as 0 and 2, since the program code they cover should
> already be covered indirectly through the certificates measured
> into PCR 7. Validation through certificates hashes is typically
> preferable over validation through direct measurements as it is
> less brittle in context of OS/firmware updates: the measurements
> will change on every update, but signatures should remain
> unchanged. See the Linux TPM PCR Registry for more discussion.

If you enroll your own secure boot keys and use a Unified Kernel
Image (UKI), then using just PCR 7 will be sufficient to ensure
integrity up to the point where we need to unlock our disk. Some
distributions instead ship EFI executables that are pre-signed with
the Microsoft keys, which allows them to enable secure boot by
default without requiring the user to generate and enroll anything
on their own. Since this also means that the user cannot sign their
kernel and/or initrd image, a trusted and pre-signed shim is often
used to measure the hash of the kernel and initrd before executing
them into PCR 9, which we would want to use in that case. Another
approach is to have the user generate a so-called Machine Owner Key
(MOK) if they want to sign something, in which case PCR 14 should
be used, too.

So the exact PCR selection may change a bit depending on the
user's setup. A quick [search on GitHub](https://github.com/search?q=cryptenroll+%2F0%5C%2B2%5C%2B7%2F&type=code) or [on the internet](https://duckduckgo.com/?t=h_&q=cryptenroll+0%2B2%2B7&ia=web) reveals that many people still opt to use
additional PCRs like 0 and 2 in addition to 7, which is of course
fine but may result in keys becoming inaccessible when the BIOS or
some firmware is updated - which can be annoying.

### [ð](#a-common-vulnerable-setup) A common (vulnerable) setup

If you already have secure boot set up, configuring TPM2 unlock
for your LUKS partition is usually very simple. Most guides will
resort to `systemd-cryptenroll` or `clevis`
which are different implementations that internally do some
variation of the following:

1. Add a newly generated key to your LUKS partition- Seal this key in your TPM based on your selection of PCRs- Store the encrypted TPM context in the LUKS token metadata
       which is required to unseal the secret at a later point in
       time

Both `clevis` and `systemd-cryptenroll`
can store tokens in other ways than a TPM2, for example using a
FIDO2 key. I found that `clevis` also supports
retrieving tokens from network resources, but other than that the
two tools are very similar in what they do.
`systemd-cryptenroll` just comes pre-packaged with
`systemd` so it is usually a bit simpler to use. Here is
an example:

```
systemd-cryptenroll --tpm2-pcrs=7 --tpm2-device=auto /dev/nvme0n1p3
```

In theory, the disk is now...