---
title: ghidra-firmware-utils
url: https://kitploit.com/en/tools/github/al3xtjames/ghidra-firmware-utils
source: Kitploit
date: 2026-09-06
fetch_date: 2026-09-07T06:48:34.993940
---

# ghidra-firmware-utils

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories

ghidra-firmware-utils — Ghidra extension for PC firmware reverse engineering, providing loaders for PCI option ROMs, Intel Flash Descriptor, coreboot CBFS, and UEFI firmware volumes, plus UEFI helper scripts for type recovery and GUID identification. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/al3xtjames/ghidra-firmware-utils

![](https://assets.kitploit.com/production/public/tools/54267/84eb7632f5d09c1e155b7fb50d04660a1235b582c918547d60b3493200b500b8-display-v1.webp)

[Embedded Systems Security](/en/categories/embedded-systems-security)[Reverse Engineering](/en/categories/reverse-engineering)[Hardware Security](/en/categories/hardware-security)[Hardware & IoT Security](/en/categories/hardware-iot-security)[Binary Analysis](/en/categories/binary-analysis)[Firmware Analysis](/en/categories/firmware-analysis)

![GitHub](/providers/github.png)al3xtjames/ghidra-firmware-utils

# ghidra-firmware-utils

Ghidra extension for PC firmware reverse engineering, providing loaders for PCI option ROMs, Intel Flash Descriptor, coreboot CBFS, and UEFI firmware volumes, plus UEFI helper scripts for type recovery and GUID identification.

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

[View Repository](https://github.com/al3xtjames/ghidra-firmware-utils)

49356296 days ago![Reviewed by Kitploit](/_next/image?url=%2Fbadges%2Fkitploit_badge_reviewed_full.png&w=48&q=75)

# Ghidra Firmware Utilities

Various modules for [Ghidra](https://ghidra-sre.org/) to assist with PC firmware reverse engineering.
This was accepted as a [coreboot project for GSoC 2019](https://summerofcode.withgoogle.com/projects/#6413737605464064).

## Features

### PCI option ROM loader

* Implements a FS loader for PCI option ROMs (handles hybrid ROMs with
  multiple images, e.g. legacy x86 + UEFI)
* Loads UEFI executables from PCI option ROMs (including compressed images)
* Defines the entry point function and various header data types for legacy
  x86 option ROMs

### Firmware image loader

* Implements a FS loader for Flash Map (FMAP) images and Intel Flash
  Descriptor (IFD) images (shows flash regions)
* Implements a FS loader for Coreboot Filesystem (CBFS) images (displays
  included files and handles compression)
* Implements a FS loader for UEFI firmware volumes and nested firmware
  filesystem (FFS) file/FFS section parsing

### Terse Executable (TE) loader

* Implements a binary loader for TE binaries (frequently used in UEFI PI)

### UEFI helper script

* Includes data type libraries for base UEFI types (taken from EDK2 MdePkg)
* Fixes the signature of the entry point function
* Defines known GUIDs in the binary's .data/.text segments
* Locates and defines global copies of UEFI table pointers (gBS/gRT/gST/etc)

## Building & Installation

JDK 21 (or newer) and Ghidra 12.0 (or newer) are required.

Ghidra's standard Gradle build system is used. Set the `GHIDRA_INSTALL_DIR`
environment variable before building, or set it as a Gradle property (useful
for building in an IDE):

### Environment variable

root@kitploit:~

```
$ export GHIDRA_INSTALL_DIR="/path/to/ghidra"
$ ./gradlew
```

### Gradle property

root@kitploit:~

```
echo GHIDRA_INSTALL_DIR=/path/to/ghidra > gradle.properties
```

> [!NOTE]
> `GHIDRA_INSTALL_DIR` should point to the directory which contains
> `support/buildExtension.gradle`. For example, users of the
> [Flathub package](https://flathub.org/en/apps/org.ghidra_sre.Ghidra) should use
> `/var/lib/flatpak/app/org.ghidra_sre.Ghidra/current/active/files/lib/ghidra`.

The module ZIP will be output to `dist/`. Use **File > Install Extensions** and
select the green plus to browse to the extension. Restart Ghidra when prompted.

For proper functionality, the plugin should be built with the same JRE used
by your Ghidra installation. If you have multiple Java runtime environments
installed, select the correct JRE by setting the `JAVA_HOME` environment
variable before building.

## Usage

### PCI option ROM loader

Add a PCI option ROM to a Ghidra project. Legacy x86 option ROMs can be
directly loaded for analysis. Ensure that the binary format is set to
**x86 PCI Option ROM**, and import the binary.

UEFI option ROMs or option ROMs that contain more than one image should be
imported using the filesystem loader. When prompted to select an import mode,
select **File system**. The images contained within the option ROM will be
displayed, and can be imported for analysis. Legacy x86 images will be handled
the x86 PCI Option ROM loader, and UEFI images will be handled by the PE32
loader (compression is supported). Information for each image can be displayed
by selecting **Get Info** in the right-click menu.

### Firmware image loader

Add a supported firmware image to a Ghidra project. The firmware image loader
supports Intel images with a Flash Descriptor, coreboot images with a FMAP/CBFS
layout, and UEFI firmware volumes. The **File system** import mode can be used
to view embedded files within the specified firmware image.

Note that some UEFI firmware images may store nested firmware volumes within
freeform/raw files (or freeform/raw FFS sections). Such files can be imported
as firmware volumes by selecting **Open File System** in the right-click menu
for the specified freeform/raw file. If no nested firmware volume is found, an
error message will be displayed (`No file system provider for...`).

### UEFI helper script

The helper script is included in the plugin's ghidra\_scripts directory, which
should be automatically added to the list of script directories in Ghidra.

Run the UEFI helper script by selecting UEFIHelper.java in the Script Manager
window (accessed from **Window -> Script Manager**).

To modify the UEFI data type library, modify the PRF template in
`data/gen_prf.sh` as necessary and generate new PRF files. Open the generated
PRF file in **File -> Parse C Source**. Build the updated data type library
by selecting **Parse to File...**. Overwrite the original data type libraries
in `data` and rebuild the plugin.

### Related projects

These are some interesting projects related to UEFI reversing:

* [efiXplorer](https://github.com/binarly-io/efiXplorer) - IDA plugin for UEFI firmware analysis and reverse
  engineering automation
* [Ghidra-EFI-Byte-Code-Processor](https://github.com/meromwolff/Ghidra-EFI-Byte-Code-Processor) - EFI Byte Code (EBC) processor module
  for Ghidra

## License

Apache 2.0, with some exceptions:

* `src/efidecompress/c/efidecompress.c`: BSD

## Credits

`src/efidecompress/c/efidecompress.c` is a lightly modified version of
[Decompress.c](https://raw.githubusercontent.com/theopolis/uefi-firmware-parser/21106baf019db9dcd046a3c01ee7b32212de45a5/uefi_firmware/compression/Tiano/Decompress.c) from uefi-firmware-parser (which itself is derived from
[the original in EDK2 BaseTools](https://raw.githubusercontent.com/tianocore/edk2/2e351cbe8e190271b3716284fc1076551d005472/BaseTools/Source/C/Common/Decompress.c)).

The IFD FS loader in `src/main/java/firmware/ifd` used the parser from
[UEFITool](https://github.com/LongSoft/UEFITool) as a reference.

The GUID database in `dat...