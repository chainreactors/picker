---
title: Zombie COTables: Resurrecting Freed Memory to Escape VirtualBox
url: https://blog.exodusintel.com/2026/06/15/zombie-cotables-resurrecting-freed-memory-to-escape-virtualbox/
source: Exodus Intelligence
date: 2026-06-15
fetch_date: 2026-06-16T07:15:00.404945
---

# Zombie COTables: Resurrecting Freed Memory to Escape VirtualBox

[Skip to content](#content "Skip to content")

[![Exodus Intelligence](https://blog.exodusintel.com/wp-content/uploads/2018/10/exodus-final-logo-1_small.png "Exodus Intelligence")](https://blog.exodusintel.com/ "Exodus Intelligence")

Menu

* [Blog](https://blog.exodusintel.com/)
  + [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/)
  + [News](https://blog.exodusintel.com/category/news/)
  + [Training](https://blog.exodusintel.com/category/training/)
  + [Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/)
  + [Other](https://blog.exodusintel.com/category/other/)
* [Offerings](https://exodusintel.com/index.html)
* [Company](https://exodusintel.com/about.html)
* [Capabilities](https://exodusintel.com/zeroday.html)
* [Training](https://exodusintel.com/training.html)
* [Advisories](https://blog.exodusintel.com/advisories-2/)

# EXODUS BLOG

---

## Zombie COTables: Resurrecting Freed Memory to Escape VirtualBox

JUNE 15, 2026
[Vulnerability Analysis](https://blog.exodusintel.com/category/vulnerability-analysis/), [Exploit Techniques](https://blog.exodusintel.com/category/exploit-techniques/), [General Research](https://blog.exodusintel.com/category/general-research/)

By Luca Ginex

## Overview

This blog post discusses a use-after-free vulnerability that we found in VirtualBox in 2025. This vulnerability was patched on [Oracle Critical Patch Update – January 2026](https://web.archive.org/web/20260203151756/https%3A//www.oracle.com/security-alerts/cpujan2026.html). The vulnerability was also presented, along with others, at [OffensiveCon 2026](https://www.offensivecon.org/speakers/2026/nini-chen-and-wei-che-kao.html). This post describes the exploitation process for the vulnerability on a Linux system.

First, a general overview of the SVGA device is given. Next, an analysis of the vulnerability is provided. Finally, the exploitation strategy is presented.

## Preliminaries

In this section we give a general overview of the SVGA device and describe the relevant structures involved in SVGA operations.

### Super Video Graphics Array (SVGA)

The Super Video Graphics Array (SVGA) is a display standard that extends the capabilities of the original Video Graphics Array (VGA) standard introduced by IBM in 1987. SVGA provides support for a wide range of screen resolutions and color depths, surpassing the limits of VGA.

Common SVGA resolutions include: 800×600 and 1024×768, with modern implementations supporting much higher resolutions dependent on the graphics card and monitor capabilities.

### VMware SVGA-II

VMware SVGA-II is an SVGA-compatible virtual graphics adapter developed by VMware for use in its virtual machines (VMs). It is a software-defined device that provides guest operating systems with enhanced graphics capabilities, including 3D acceleration. This virtual graphics device is a standard component in VMware products like Workstation, Fusion, and ESXi, and is also supported by other hypervisors, including Oracle VirtualBox.

The VMware SVGA-II virtual device is exposed to the guest VM through the PCI bus, presenting both I/O ports and a Memory-Mapped I/O (MMIO) region. The base address for the I/O ports (`SVGA_PORT_BASE`) is dynamically assigned during PCI bus enumeration.

The following table describes the primary I/O port offsets exposed by the virtual device:

```
Name              Index        Description
---------------   ---------    ----------------------------------------------------------------------
SVGA_INDEX        0x00         Index of the SVGA register to read from or write to.
SVGA_VALUE        0x01         Value read or to write to the register specified in the SVGA_INDEX offset.
SVGA_BIOS         0x02         Unknown.
SVGA_IRQSTATUS    0x03         Unknown.
```

The guest VM can use these I/O ports to read from and write to the internal registers of the SVGA-II device. To access a register, the guest driver writes the register’s index to the `SVGA_INDEX` port (`SVGA_PORT_BASE + SVGA_INDEX`). It can then read the register’s value from the `SVGA_VALUE` port (`SVGA_PORT_BASE + SVGA_VALUE`) or write a new value to it through the same port.

The following table shows the defined registers by the SVGA-II specification:

```
Register Name                         Index   Description
----------------------------          -----   ----------------------------------------------------------
SVGA_REG_ID                           0x00    SVGA device ID. Guest writes expected ID; host responds if
                                              supported.
SVGA_REG_ENABLE                       0x01    Enables or disables the SVGA device.
SVGA_REG_WIDTH                        0x02    Framebuffer width (in pixels).
SVGA_REG_HEIGHT                       0x03    Framebuffer height (in pixels).
SVGA_REG_MAX_WIDTH                    0x04    Maximum width supported by the device.
SVGA_REG_MAX_HEIGHT                   0x05    Maximum height supported by the device.
SVGA_REG_DEPTH                        0x06    Bits per pixel (usually 24 or 32).
SVGA_REG_BITS_PER_PIXEL               0x07    Guest-visible bits per pixel (may differ from DEPTH).
SVGA_REG_PSEUDOCOLOR                  0x08    Boolean; set if using pseudocolor mode.
SVGA_REG_RED_MASK                     0x09    Red mask (bitfield).
SVGA_REG_GREEN_MASK                   0x0A    Green mask.
SVGA_REG_BLUE_MASK                    0x0B    Blue mask.
SVGA_REG_BYTES_PER_LINE               0x0C    Pitch: bytes per scanline.
SVGA_REG_FB_START                     0x0D    Framebuffer physical address (read-only).
SVGA_REG_FB_OFFSET                    0x0E    Offset to start of visible framebuffer.
SVGA_REG_VRAM_SIZE                    0x0F    Size of video RAM.
SVGA_REG_FB_SIZE                      0x10    Size of framebuffer.
SVGA_REG_CAPABILITIES                 0x11    Bitmask of supported features.
SVGA_REG_MEM_START                    0x12    MMIO (memory-mapped I/O) region base address.
SVGA_REG_MEM_SIZE                     0x13    Size of MMIO region.
SVGA_REG_CONFIG_DONE                  0x14    Write 1 when configuration is done.
SVGA_REG_SYNC                         0x15    Write 1 to sync guest/host framebuffer.
SVGA_REG_BUSY                         0x16    Read 1 if device is busy processing commands.
SVGA_REG_GUEST_ID                     0x17    Guest OS identifier.
SVGA_REG_CURSOR_ID                    0x18    Cursor identifier.
SVGA_REG_CURSOR_X                     0x19    Cursor X position.
SVGA_REG_CURSOR_Y                     0x1A    Cursor Y position.
SVGA_REG_CURSOR_ON                    0x1B    Show/hide cursor.
SVGA_REG_HOST_BITS_PER_PIXEL          0x1C    Bits per pixel on host display (read-only).
SVGA_REG_SCRATCH_SIZE                 0x1D    Number of scratch registers available.
SVGA_REG_MEM_REGS                     0x1E    Number of FIFO registers.
SVGA_REG_NUM_DISPLAYS                 0x1F    Number of virtual displays supported.
SVGA_REG_PITCHLOCK                    0x20    Lock bytes-per-line (pitch).
SVGA_REG_IRQMASK                      0x21    Interrupt bitmask.
SVGA_REG_NUM_GUEST_DISPLAYS           0x22    Guest-specified number of displays.
SVGA_REG_DISPLAY_ID                   0x23    ID of current display being modified.
SVGA_REG_DISPLAY_IS_PRIMARY           0x24    Boolean; is this display the primary one?
SVGA_REG_DISPLAY_POSITION_X           0x25    Display position X (for multi-monitor layout).
SVGA_REG_DISPLAY_POSITION_Y           0x26    Display position Y.
SVGA_REG_DISPLAY_WIDTH                0x27    Width of a specific display.
SVGA_REG_DISPLAY_HEIGHT               0x28    Height of a specific display.
SVGA_REG_GMR_ID                       0x29    ID of the Guest Memory Region
SVGA_REG_GMR_DESCRIPTOR               0x2A    Unknown
SVGA_REG_GMR_MAX_IDS                  0x2B    Unknown
SVGA_REG_GMR_MAX_DESCRIPTOR_LENGTH    0x2C    Unknown
SVGA_REG_TRACES                       0x2D    Unknown
SVGA_...