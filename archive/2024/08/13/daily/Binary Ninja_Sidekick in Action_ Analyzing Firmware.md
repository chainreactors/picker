---
title: Sidekick in Action: Analyzing Firmware
url: https://binary.ninja/2024/08/12/sidekick-in-action-analyzing-firmware.html
source: Binary Ninja
date: 2024-08-13
fetch_date: 2025-10-06T18:04:01.500127
---

# Sidekick in Action: Analyzing Firmware

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Participate in our [Reverse Engineering Survey](/survey/) to win free licenses or admission to [RE//verse](https://re-verse.io/)!

# Binary Ninja Blog

## Sidekick in Action: Analyzing Firmware

* [Brandon Miller](https://github.com/zznop)
* [Tim Bryant](https://github.com/iamausertoo)
* [Brian Knudson](https://github.com/kristopax)
* 2024-08-12
* [sidekick](/tag/sidekick)

Sidekick 2.0 introduces a powerful set of features that significantly enhance firmware analysis capabilities. In this post, weâll demonstrate how Sidekick, in conjunction with the Firmware Ninja plugin (currently in development) for Binary Ninja, can streamline the process of analyzing Memory Mapped I/O (MMIO) in firmware samples.

## Introduction

Weâll be analyzing two firmware samples:

1. `android-bootloader`: An Android U-boot image for a Samsung phone with an Exynos 5422 SoC.
2. `arducopter`: ArduCopter OS build for a [Pixhawk 6x](https://firmware.ardupilot.org/Copter/stable-4.5.3/Pixhawk6X/) flight controller, using an STM32 H750 series board with an ARM processor running the ArduCopter ChibiOS RTOS.

## Preparation: Setting Up the Environment

Before leveraging Sidekickâs capabilities, we need to prepare our analysis environment:

1. Use Firmware Ninja to identify possible MMIO accesses and select the appropriate board for each binary. These accesses will be stored in an index, which Sidekick will access later.
2. Create sections/segments representing memory-mapped hardware device ranges using Firmware Ninja. This setup is crucial for indexing the MMIO data later.

Hereâs an example of an index entry for resolved MMIO locations:

![Indexes Resolved MMIO Accesses](/blog/images/sidekick-in-action/indexes-resolved-mmio-accesses.png)

## Sidekick in Action: Enhancing Firmware Analysis

Now, letâs see how Sidekick transforms our firmware analysis workflow:

### Step 1: Data Indexing with Sidekick

Sidekickâs indexing capabilities play a crucial role in organizing and making the Firmware Ninja analysis data accessible:

1. Run Firmware Ninjaâs scripts that:
   * Retrieve raw Firmware Ninja analysis data from Binary Ninjaâs metadata
   * Post-process the data
   * Create Sidekick indexes for MMIO information

This step results in two key indexes:

* âFirmware Ninja: Resolved MMIO Accessesâ
* âFirmware Ninja: Functions accessing MMIOâ

### Step 2: AI-Assisted Script Generation

Sidekickâs Analysis Workbench shines in this step, enabling us to create sophisticated analysis scripts through natural language interaction:

1. Use the Analysis Workbench to generate scripts that leverage the indexed Firmware Ninja data.
2. Employ Sidekickâs LLMOperator to craft queries about:
   * Identifying communication protocols associated with each MMIO access
   * Determining the make/model of each memory-mapped hardware device

### Step 3: Executing AI-Enhanced Analysis

With our AI-generated scripts ready, we can now run them to gain deeper insights:

1. Execute the scripts to create new indexes containing the analysis results.
2. Review the AI-assisted identifications of communication protocols and hardware devices.

## Results

### Identifying MMIO Communication Protocol on arducopter

![MMIO Communication Protocol arducopter](/blog/images/sidekick-in-action/firmware-analysis-mmio-communication-protocol-arducopter.png)

*Figure 1. The Analysis Workbench leverages AI to recognize communication protocols from MMIO accesses.*

On the `arducopter` binary, from the simple task description âIdentify MMIO communication protocolsâ, the Analysis Workbench generated a script that opens the resolved MMIO accesses in the binary from the âFirmware Ninja: Resolved MMIO Accessesâ index and uses the information from those accesses to infer the data communication protocol being used over the MMIO device. We additionally asked the Sidekick Coding Assistant to include the reasoning behind the LLMOperatorâs determination. Lastly, Sidekick also output its results to an index (âMMIO Data Communications Protocolsâ) for convenient reference.

### Identifying Hardware Device Models from MMIO Accesses on arducopter

![Hardware Device Models arducopter 1](/blog/images/sidekick-in-action/firmware-analysis-hardware-device-models-arducopter-1.png)

*Figure 2. The Analysis Workbench leverages AI to identify the clock controller device model from MMIO accesses.*

![Hardware Device Models arducopter 2](/blog/images/sidekick-in-action/firmware-analysis-hardware-device-models-arducopter-2.png)

*Figure 3. The Analysis Workbench leverages AI to identify the gpio controller device model from MMIO accesses.*

On the `arducopter` binary, we described a new task - âIdentify each hardware device model from MMIO Accesssâ. From there, the Analysis Workbench generated a script that opens the resolved MMIO accesses in the binary from the âFirmware Ninja: Resolved MMIO Accessesâ index and passes information from those accesses to an LLMOperator initialized with the task of identifying the manufacturer and model of the hardware device associated with those MMIO accesses. Like before, we also asked for its reasoning and also requested the results be output to an index. As you can see, Sidekick is able to identify the manufacturer and model for the clock controller and gpio controller devices on the board accessed via MMIO.

### Identifying Manufacturer/Model for Memory-Mapped Hardware Devices on android-bootloader

![Memory Mapped Device Model android-bootloader](/blog/images/sidekick-in-action/firmware-analysis-memory-mapped-device-model-android-bootloader.png)

*Figure 4. The Analysis Workbench leverages AI to identify the PMU device model from MMIO accesses.*

For the `android-bootloader` binary, we performed the same task of identifying the hardware device manufacturer and model based on MMIO accesses that we performed on the `arducopter` binary. As you can see, Sidekick was able to correctly identify the hardware manufacturer and model when examining MMIO accesses.

## Observations and Insights

Sidekickâs AI capabilities demonstrated impressive knowledge and reasoning:

* The AI showed familiarity with device datasheets, recognizing common patterns and conventions in MMIO access.
* It provided reasoning for hardware identifications based on code patterns and I/O register offsets.
* While not always 100% accurate in device identification, Sidekickâs guesses were consistently close and often accompanied by convincing rationales.

## Conclusion

Sidekick 2.0, when combined with tools like Firmware Ninja, significantly enhances the firmware analysis process. Its ability to index complex data, generate sophisticated analysis scripts through natural language interaction, and provide AI-assisted insights makes it an invaluable tool for reverse engineers working with firmware.

By automating tedious tasks and providing intelligent analysis, Sidekick allows analysts to focus on higher-level understanding and decision-making, ultimately leading to more efficient and effective firmware analysis.

---

Future posts will explore more advanced uses of Sidekick in firmware analysis and discuss potential improvements to increase the accuracy of hardware device identification.

---

If you are not already using Sidekick, then [sign up](https://sidekick.bina...