---
title: Wake up and Smell the BitLocker Keys
url: https://blog.nviso.eu/2024/11/26/wake-up-and-smell-the-bitlocker-keys/
source: Instapaper: Unread
date: 2024-11-29
fetch_date: 2025-10-06T19:20:13.054847
---

# Wake up and Smell the BitLocker Keys

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

# Wake up and Smell the BitLocker Keys

[Jonathan Prince](https://blog.nviso.eu/author/jonathan-prince/ "Posts by Jonathan Prince")

[OS Hardening](https://blog.nviso.eu/category/os-hardening/), [Windows](https://blog.nviso.eu/category/windows/), [Cybersecurity](https://blog.nviso.eu/category/cybersecurity/), [Cryptography](https://blog.nviso.eu/category/cryptography/), [Uncategorized](https://blog.nviso.eu/category/uncategorized/)

November 26, 2024November 25, 2024
8 Minutes

Many enterprise laptops use BitLocker to provide full disk encryption (FDE) to protect sensitive data from exposure if the laptop were stolen. But how adequate is the default implementation of BitLocker to protect data at rest in this scenario? The security of all encryption relies on protection of the key material. A common assumption is that since the BitLocker keys are stored in the Trusted Platform Module (TPM) the decryption process is secure. This is however only partly true as we will see in this article. First, we will look at the purpose of the TPM and how it works in relation to BitLocker.

## What is the TPM?

The TPM is a hardware security component embedded in devices to provide cryptographic functions and is commonly used for tasks like encryption, digital signatures, and secure key storage. However, one of the key purposes of the TPM is to validate system integrity. To do this the TPM stores information such as hashes of the BIOS or UEFI firmware, bootloader, and/or hardware configuration in Platform Configuration Registers (PCRs) to identify any changes that could indicate a compromise. BitLocker uses the TPM to authenticate and ensure system integrity by verifying boot components before unlocking encrypted volumes.

A TPM can typically be configured in one of three ways:

* TPM Only: No user input required, only validates integrity checks
* TPM + PIN: The user must supply a PIN
* TPM + PIN + 2FA: The user must supply a PIN and a second factor (USB key, OTP)

In TPM-only mode, BitLocker does not require any user input, making the process seamless from the user’s perspective but less secure compared to configurations using a PIN or USB key. The TPM checks for system integrity, preventing access if the system has been tampered with, locking the encrypted volume until the system is restored to a known, secure state.

BitLocker uses several keys to protect the data. The data on the drive is encrypted using a full volume encryption key (FVEK). The FVEK is encrypted using the volume master key (VMK) and stored in the metadata on the disk. The VMK is stored inside the TPM and decrypted (unsealed) by the TPM when the appropriate conditions are met, such as the successful integrity check or being provided with the correct recovery key. This process allows the system to be re-keyed, for example if a recovery key has been exposed and needs to be replaced, without the need to re-encrypt the entire volume with a new FVEK.

The following diagram might help to visualize the flow of the inputs and the decryption of the VMK, FVEK, and subsequently the encrypted volume:

![A diagram to visualize the flow of the inputs and the decryption of the VMK, FVEK, and subsequently the encrypted volume](https://blog.nviso.eu/wp-content/uploads/2024/11/BitLocker-TPM-1024x638.png)

### Where is the problem?

The problem lies in the fact that without an additional authentication factor if the system passes the integrity check the TPM will provide the unencrypted VMK which is then used to decrypt the FVEK and subsequently the encrypted data volume. The VMK is sent in cleartext by design and if we can gain access to this communication from the TPM we can read the VMK once it has been unsealed and use it to decrypt the data.

Surely the TPM standard should be designed to avoid this? Quite simply, yes it should, and it can. Part 1, Sections 19 and 21 of the TPM 2.0 Library Specification describes a feature called session-based parameter encryption. Using this feature the system generates a random value, derives a session key using a key derivation function, encrypts it with the public part of the TPM primary key, and transmits it to the TPM to initiate an encrypted session. However, this feature is not implemented by Microsoft.

Now that we understand how the TPM works, let us look at how practical it is to sniff the TPM bus, extract the VMK, and decrypt the disk. For the practical demonstration we will use a Dell Latitude E5470, a standard business laptop running Windows 11 Professional. This laptop, despite being a little older, was chosen because research revealed that it is representative of the technology used in the majority of corporate laptops using a discrete TPM chip implementing the TPM 2.0 specification in the same way as the current Dell Latitude/Precision series, and the popular HP Elitebooks which together make up a large proportion of the business laptop market. This TPM communicates via an SPI bus but the principles for an LPC bus are much the same.

## Sniffing the TPM Bus

### What tooling is required?

The equipment for this attack can be found in a well-equipped hardware hacking lab. The main tool we need to capture traffic on the TPM bus is a Logic Analyzer. The logic analyzer chosen for this demonstration was the DSLogic U3 Pro16. This device produced by Dream Source Labs in China fulfils the specifications required to sniff the SPI bus of the test laptop – Also, it can be purchased for a very reasonable price of around 300 EUR. This price point makes such attacks feasible even to attackers with limited resources.

Secondly, we need software to create and analyze the traffic capture. In this case, Dream Source Labs’ DSView, a fork of the popular Sigrok/PulseView software tailored for use with DSLogic, was chosen.

In addition to the logic analyzer itself the only specialized tooling required, unless the laptop provides PCB headers or pads that are easily accessible, are some logic probes. We used the PCBite tool for this demonstration but it would also be possible to use a basic SOIC8 clip whenever the flash chip is located on the same bus and easily accessible.

Last but not least, a small screwdriver and a spudger is usually all that is needed to open the laptop case.

### Connecting to the Bus

The first task is to locate the TPM and any places we may be able to use to connect to the bus. In some ca...