---
title: Bypassing Bitlocker using a cheap logic analyzer on a Lenovo laptop
url: https://www.errno.fr/BypassingBitlocker.html
source: Instapaper: Unread
date: 2023-08-26
fetch_date: 2025-10-04T12:02:15.460728
---

# Bypassing Bitlocker using a cheap logic analyzer on a Lenovo laptop

# Bypassing Bitlocker using a cheap logic analyzer on a Lenovo laptop

## Guillaume Quéré

[GitHub](https://github.com/gquere)

[LinkedIn](https://www.linkedin.com/in/guillaume-qu%C3%A9r%C3%A9-90a6187b/)

[Root-Me](https://www.root-me.org/das)

* [Architecture of a passwordless BitLocker with a discrete TPM](#architecture-of-a-passwordless-bitlocker-with-a-discrete-tpm)
* [Capturing the TPM exchange](#capturing-the-tpm-exchange)
* [Decoding the captured signal](#decoding-the-captured-signal)
  + [SPI](#spi)
  + [TIS](#tis)
  + [TPM 2.0](#tpm-20)
* [Mounting and backdooring the disk](#mounting-and-backdooring-the-disk)
* [Limitations](#limitations)
* [Takeaways](#takeaways)

Have you ever been told that the company’s data on laptops is protected thanks to BitLocker? Well it turns out that this depends on BitLocker’s configuration…

# Architecture of a passwordless BitLocker with a discrete TPM

The BitLocker partition is encrypted using the Full Volume Encryption Key (FVEK). The FVEK itself is encrypted using the Volume Master Key (VMK) and stored on the disk, next to the encrypted data. This permits key rotations without re-encrypting the whole disk.

The VMK is stored in the TPM. Thus the disk can only be decrypted when booted from this computer (there is a recovery mechanism in Active Directory though).

![TPM key architecture](/BypassingBitlocker/arch.png)

In order to decrypt the disk, the CPU will ask that the TPM sends the VMK over the SPI bus.

The vulnerability should be obvious: at some point in the boot process, the VMK transits unencrypted between the TPM and the CPU. This means that it can be captured and used to decrypt the disk.

# Capturing the TPM exchange

We’ll be using a dirt cheap logic analyzer, [DSLogic Plus](https://www.dreamsourcelab.com/product/dslogic-series/). I bought this for under $100 in 2021 (tax and shipping included).

A note on signal capture: to comfortably acquire a signal the sampling frequency should be 3 to 4 times the bus frequency. This means that for our SPI 33MHz bus we should sample at the very least at 100MHz. Notice that the specs of the analyzer state that it can do *up to* 400MHz on *up to* 16 channels. I’ll help you read between the lines here:

* the more channels you capture at a time (by sets of 3), the lower the sampling frequency
* you have to distinguish stream mode and buffer mode. The first one will send results directly to the host computer and permits capture of large sets, up to a minute but it’s limited to 100MHz on 3 channels. The buffer mode allows sampling at 400MHz but it will only work for a few milliseconds, so there’s no practical use for it here.

This means that this hardware can *barely* do the job we’re asking it to do. For a more professional option both hardware and software-wise (but also 10x pricier) have a look at [Saleae](https://usd.saleae.com/products/saleae-logic-pro-16). Otherwise there’s [sigrok’s list of supported hardware](https://sigrok.org/wiki/Supported_hardware#Logic_analyzers).

As for plugging the analyzer to the board, remember that SPI is a shared bus. This means that there’s no need to capture the signal right at the tiny TPM pins if there is a larger SPI component on the board that the hooks can be latched on to. From experience I identified a neighbouring SPI flash, but fortunately all components are marked so it’s rather easy to identify their use by looking up their datasheet.
![Lenovo board](/BypassingBitlocker/SPI_pin.jpg)

SPI has several lines but only 3 can be captured using the DSLogic because otherwise the sampling frequency drops. The 3 most important ones are the clock CLK and the two data lines MOSI and MISO.

The threshold voltage (level at which the analyzer decides that the line has changed states) should be around half of the signal’s voltage, here the latter was measured at 3.3V so an appropriate threshold is around 1.6V.

The VMK key we’re looking for is used late in the POST stage. For the Lenovo L13 I worked with it was just after the splash screen, about 14 seconds into the boot process out of a total boot time of about 25 seconds. There are SPI operations before that (mostly to read and verify the early boot stages) but they’re not TPM. You could either start the capture when booting the computer, or safely wait about 7 or so seconds to avoid capturing unnecessary data.

# Decoding the captured signal

There are 3 layers to decode:

* SPI, which is the physical layer
* TIS
* TPM2.0, which contains the VMK

## SPI

As far as SPI is concerned any logic analyzer should do this properly, it’s a rather simple protocol:
![SPI byte](/BypassingBitlocker/spi_frame.PNG)

The blue square wave is the clock, the other two lines (yellow and red) are data lines, respectively used for communications from slave to master (MISO) and master to slave (MOSI).

When the clock signal is going up (transitioning from 0 to 1), the bit value is whatever state the data lines are in at this specific time. In our case the red line sits at 0 for 8 clock cycles, so the byte is 0. The yellow line only has the first bit set, so the decoded value is b10000000 = 0x80.

The logic analyzer correctly decodes SPI so we’ll just trust its output.

## TIS

TIS, which stands for TPM Interface Specification, is another beast entirely and that’s where I had most of my troubles. I couldn’t find a decoder that worked for my capture and decided to do it “manually”. Short of correctly decoding the data, the [libsigrock decoders](https://github.com/sigrokproject/libsigrokdecode/pull/88) did at least indicate a rough window for the TPM exchanges which was a welcome tip since each capture has several million bytes of data. Maybe the decoders fail be because the capture is missing Chip Select (CS#) which is required in the TPM specification, maybe because the clock is incorrect, maybe because some bytes are occasionally missing, maybe for some other reason, who knows.

Master to slave request:
![Master to slave request](/BypassingBitlocker/tis_frame_request.PNG)

Sending a request seems to happen in this order:

* the slave sends byte 80 to signal that it’s ready
* the master sends a header we don’t care about (`D4 00 24`) and then sends the TPM byte in a loop (`80`)
* the slave acknowledges that it has read the byte by sending 01 FF
* at this point the cycle starts anew with the next byte

So this whole frame is just to send the byte 0x80 from the master to the slave!

Slave to master response:
![Slave to master response](/BypassingBitlocker/tis_frame_response.PNG)

This is a completely different process that relies on setting and reading registers. The frame is the result of reading one byte from a set address (`D4 00 24`, meaning register 24). Again the slave seems to start the transaction with byte 80, then writes the size of the followong data which is only 1 byte (or it could be an ACK value to the read request, who knows) and finally the value we care about, here 0x80. The next TPM byte is 0x02.

## TPM 2.0

The TPM command that requests the key be sent back is the `TPM2_Unseal` command. It is described in [part 3 of the TPM 2.0 specification](https://trustedcomputinggroup.org/resource/tpm-library-specification/).

You might ask how I isolated the frames below since no decoder would work. We don’t actually care about the requests happening on MOSI, we’re mostly interested in the responses on the MISO line. As we’ve seen previously the TIS encoding around TPM bytes is rather simple, so the simplest way to isolate all TPM transactions is to filter the raw SPI data using the mask “80 00 00 00 01 ..” and only keep this wildcard last byte. The start of a TPM transaction can then be identified by its own `80 01` or `80 02` header. There should only be a few dozens TPM responses, the one with the key inside should be the longer authenticated one (starts with `80 02`).

![unseal cmd and response](/BypassingBitlocker/unseal_response.PNG)
There is a 10 milliseconds delay between the unse...