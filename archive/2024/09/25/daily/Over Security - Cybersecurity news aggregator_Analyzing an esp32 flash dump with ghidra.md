---
title: Analyzing an esp32 flash dump with ghidra
url: https://olof-astrand.medium.com/analyzing-an-esp32-flash-dump-with-ghidra-e70e7f89a57f
source: Over Security - Cybersecurity news aggregator
date: 2024-09-25
fetch_date: 2025-10-06T18:27:58.628211
---

# Analyzing an esp32 flash dump with ghidra

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe70e7f89a57f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Folof-astrand.medium.com%2Fanalyzing-an-esp32-flash-dump-with-ghidra-e70e7f89a57f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Folof-astrand.medium.com%2Fanalyzing-an-esp32-flash-dump-with-ghidra-e70e7f89a57f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Analyzing an esp32 flash dump with ghidra

[![Olof Astrand](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*2-dYAImHd_FQKeDi)](/?source=post_page---byline--e70e7f89a57f---------------------------------------)

[Olof Astrand](/?source=post_page---byline--e70e7f89a57f---------------------------------------)

6 min read

·

Aug 3, 2020

--

1

Listen

Share

As a third step I will use the flash loader to import the same binary, as in the previous story [https://medium.com/@olof.astrand/enter-home-dragon-with-ghidra-3ed7ddf75935](https://medium.com/%40olof.astrand/enter-home-dragon-with-ghidra-3ed7ddf75935) . In order to get started you need to install ghidra and Xtensa processor support <https://github.com/Ebiroll/ghidra-xtensa> and the esp32 flash loader.

![]()

Digesting the esp32 flash image

### Dump the flash of an esp32

```
esptool.py -p /dev/ttyUSB0 -b 460800 read_flash 0 0x400000 flash_contents.bin
```

### Install the ghidra esp32 flash loader

[## Ebiroll/esp32\_flash\_loader

### Ghidra Loader for ESP32 Flash Dumps GitHub is home to over 50 million developers working together to host and review…

github.com](https://github.com/Ebiroll/esp32_flash_loader?source=post_page-----e70e7f89a57f---------------------------------------)

## Before import of the flash file

After installing the extension but before importing the flash file, consider downloading the esp32\_rom.elf file and put it in the data directory. Put it next to the svd files. This way it will get loaded together with the svd and the flash file <https://dl.espressif.com/dl/esp32_rom.elf>

If you have installed the esp32 flash loader correctly, you will see this. If the flash contains several partitions, you can select the one to load with the options button.

![]()

Select the flash dump

As the flash file does not contain nearly as much as the corresponding elf file, we try to use as much information as possible that we know about the hardware and the esp32 rom.

Before jumping into the details you should re-consider reading about the esp32 memory model.

### esp32 memory model

[## ESP32 Programmers’ Memory Model

### Internal memory of the MCU is probably the most precious resource as it occupies maximum area in the chip. The newer…

medium.com](https://medium.com/the-esp-journal/esp32-programmers-memory-model-259444d89387?source=post_page-----e70e7f89a57f---------------------------------------)

### Memory used by the rom and the bootloader

The first 8KB (0x3FFA\_E000–0x3FFA\_FFFF) are used as a data memory for some of the ROM functions.

There are two regions within the heap (0x3FFE\_0000–0x3FFE\_0440–1088 bytes) and (0x3FFE\_3F20–0x3FFE\_4350=>1072 bytes) that are used by ROM code for its data. These regions are marked reserved and the heap allocator does not allocate memory from these regions.

### Linker script

A short version of the linker script, build/esp-idf/esp32/esp32\_out.ld

Generally speaking, addresses above 0x40000000 are on the instruction bus and below it, is on the data bus.

```
MEMORY
{
 iram0_2_seg (RX) : org = 0x400D0020, len = 0x330000-0x20
 dram0_0_seg (RW) : org = 0x3FFB0000 + 0x0,
                                     len = 0x2c200 - 0x0
  /* Flash mapped constant data */
  drom0_0_seg (R) : org = 0x3F400020, len = 0x400000-0x20
  rtc_iram_seg(RWX) : org = 0x400C0000, len = 0x2000
  /* RTC fast memory (same block as above), viewed from data bus*/
  rtc_data_seg(RW) : org = 0x3ff80000, len = 0x2000 - 0
  /* RTC slow memory (data accessible). Persists over deepsleep.*/
  rtc_slow_seg(RW) : org = 0x50000000 + 0,
                                     len = 0x1000 - 0
  /* external memory ,including data and text */
  extern_ram_seg(RWX) : org = 0x3F800000,
                                    len = 0x400000}
_static_data_end = _bss_end;
/* Heap ends at top of dram0_0_seg */
_heap_end = 0x40000000 - 0x0;
_data_seg_org = ORIGIN(rtc_data_seg);
/* The lines below define location alias for .rtc.data section based on Kconfig  option.
   When the option is not defined then use slow memory segment
   else the data will be placed in fast memory segment */
REGION_ALIAS("rtc_data_location", rtc_slow_seg );
REGION_ALIAS("default_code_seg", iram0_2_seg);
REGION_ALIAS("default_rodata_seg", drom0_0_seg);
```

Note

```
iram0_2_seg
(0x20 offset above is a convenience for the app binary image  generation. Flash cache has 64KB pages. The .bin file which is flashed to the chip has a 0x18 byte file header, and each segment has a 0x08 byte segment header.)
```

### Sections in the elf file

Press enter or click to view image in full size

![]()

hello.elf

After loading the binary dump

### Window -> Memorymap

This shows where the ESP32 flash loader has loaded the flash

```
"Name","Start","End","Length"
"DROM0_3f400020","ram:3f400020","ram:3f4058fb","0x58dc"
"DRAM0_3ffb0000","ram:3ffb0000","ram:3ffb21af","0x21b0"
"IRAM0_40080000","ram:40080000","ram:40080403","0x404"
"IRAM0_40080404","ram:40080404","ram:40088553","0x8150"
"IRAM0_400d0020","ram:400d0020","ram:400e303f","0x13020"
"IRAM0_40088554","ram:40088554","ram:40089ecb","0x1978"
```

### Bootlog

Compare this with the output from the bootloader when you run the program

```
I (4) esp_image: segment 0: paddr=0x00010020 vaddr=0x3f400020 size=0x058dc ( 22748) map
I (8) esp_image: segment 1: paddr=0x00015904 vaddr=0x3ffb0000 size=0x021b0 (  8624) load
I (9) esp_image: segment 2: paddr=0x00017abc vaddr=0x40080000 size=0x00404 (  1028) load
I (10) esp_image: segment 3: paddr=0x00017ec8 vaddr=0x40080404 size=0x08150 ( 33104) load
I (15) esp_image: segment 4: paddr=0x00020020 vaddr=0x400d0020 size=0x13020 ( 77856) map
I (27) esp_image: segment 5: paddr=0x00033048 vaddr=0x40088554 size=0x01978 (  6520) load
```

### Heap Log

These are all the available data for allocations.

```
I (205) heap_init: Initializing. RAM available for dynamic allocation:
I (205) heap_init: At 3FFAE6E0 len 00001920 (6 KiB): DRAM
I (205) heap_init: At 3FFB29E8 len 0002D618 (181 KiB): DRAM
I (206) heap_init: At 3FFE0440 len 00003AE0 (14 KiB): D/IRAM
I (206) heap_init: At 3FFE4350 len 0001BCB0 (111 KiB): D/IRAM
I (207) heap_init: At 40089ECC len 00016134 (88 KiB): IRAM
I (207) cpu_start: Pro cpu start user code
```

### Application output

When running the program, this is the output.

```
Hello Ghidra!
This is esp32 chip with 2 CPU cores, WiFi/BT/BLE, silicon revision 0, 2MB external flash
Free heap: 299616
my_int=4
i = 0
i = 1
i = 2
i = 3
?silly.my_int=14
ret=14
ret=9
Restarting now. 6
```

After importing you should only see one function named FUN\_XX. This is the call\_start\_cpu0 function and the last function called will be start\_cpu0\_default(). You can ha...