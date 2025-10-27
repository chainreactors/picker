---
title: CCTV – The Beginners Guide
url: https://blog.ampedsoftware.com/2023/02/28/cctv-the-beginners-guide/
source: Instapaper: Unread
date: 2023-03-03
fetch_date: 2025-10-04T08:33:32.658259
---

# CCTV – The Beginners Guide

[Skip to main content](#main)

[![Amped Blog](https://blog.ampedsoftware.com/wp-content/uploads/2023/04/logo_w400.png)](https://ampedsoftware.com "Amped Blog")
/
[Blog](https://blog.ampedsoftware.com)

* [Amped Blog Home](https://blog.ampedsoftware.com "Amped Blog Home")
* [Posts by Category](https://blog.ampedsoftware.com/posts-by-category "Posts by Category")
* [Archive](https://blog.ampedsoftware.com/archive "Archive")
* [Contact Us](https://ampedsoftware.com/contacts "Contact Us")

* [CCTV Acquisition](https://blog.ampedsoftware.com/category/cctv-acquisition)

# CCTV – The Beginners Guide

![](https://secure.gravatar.com/avatar/f03bc483195855833d54977ddbb0e272d07db4b84b752f28834946bdf477ac09?s=450&d=mm&r=g)David Spreadborough

February 28, 2023

Reading time:  7 min
[![two girls looking up at cctv cameras](https://blog.ampedsoftware.com/wp-content/uploads/2023/04/CCTV-Acquisition-The-beginners-guide-1024x535.jpg)](https://blog.ampedsoftware.com/wp-content/uploads/2023/04/CCTV-Acquisition-The-beginners-guide.jpg)

In this post on [CCTV Acquisition](https://blog.ampedsoftware.com/2023/02/14/introduction-to-cctv-acquisition/), we will provide a base for the series by breaking down CCTV into a relatively easy chunk. Understanding CCTV could be a series in itself. Nonetheless, we feel it’s essential to understand how CCTV works before getting into the weeds of recovering it.

CCTV stands for Closed Circuit TeleVision and derives from the time before computer networks or video streaming. The “Closed Circuit” comes from the fact that the video signal could be viewed and recorded. However, there was no method to transmit or share it outside of the cabled infrastructure.

**Contents**
hide

[Analog Camera](#Analog_Camera)

[Digital Camera](#Digital_Camera)

[Hybrid Recorders for CCTV Acquisition](#Hybrid_Recorders_for_CCTV_Acquisition)

[Digital Data](#Digital_Data)

[Storage](#Storage)

[4-camera System](#4-camera_System)

[DVR](#DVR)

[Remember](#Remember)

[Camera Data](#Camera_Data)

[Internal HDD](#Internal_HDD)

[Video and Audio Codec](#Video_and_Audio_Codec)

[List of Acronyms](#List_of_Acronyms)

[Conclusion](#Conclusion)

In today’s world, although many are still “closed”, most modern systems have the ability to transmit and share data. Subsequently, you will find that many documents now refer to Video Surveillance Systems (VSS) rather than CCTV.

Within those systems, there can now be several recording components. The moment that an item is installed into a system that is capable of recording and retaining data for further use, it is in effect, saving potential evidence.

[![early generation digital recorder for cctv acquisition](https://blog.ampedsoftware.com/wp-content/uploads/2023/02/IMG_0006-1024x768.jpg)](https://blog.ampedsoftware.com/wp-content/uploads/2023/02/IMG_0006.jpg)

An early generation Digital Video Recorder, linked with a VHS tape backup!

All cameras start with a lens and then a sensor to convert what the lens is “seeing” into information. This is where things now get interesting as there are two main camera types: analog and digital.

## Analog Camera

For the analog camera, the sensor turns the visual information into an electrical signal. This signal is fed down a cable to a device capable of turning that signal into a visual image, such as a monitor. For those old enough to remember, the recording device usually put in-between the camera and monitor used to be tape. Now it’s a box a bit like a computer, called a Digital Video Recorder (DVR). The DVR converts the analog signal into digital data and that’s where it is retained.

The identification of an analog camera is important during the initial scene assessment as the recorded footage may require specific processing stages. We will look more at this later in the series.

## Digital Camera

A digital camera turns the sensor image into digital data directly within the device. The data is then transmitted using transfer protocols to a storage device now known as a Network Video Recorder (NVR). Again, there would usually be a monitor to view and access the stored material. Some digital cameras also have a small storage device housed within the camera itself.

## Hybrid Recorders for CCTV Acquisition

Devices that are able to deal with both camera types are known as hybrid recorders.

Regardless of the type of camera, these different recording devices are the crux of this blog series. We will be looking at other types of devices and other system configurations but, for the main part, it is these systems that will take up most of our time.

These are the devices that hold the footage you need to answer questions about within your investigation. This data is the evidence. The picture is formed from this data, not the other way around.

## Digital Data

To start with, you have the visual information, the video. Then, you may also have audio. Also, you will have timestamp information that connects the video and audio with the date and time that the data was captured. Moreover, you will have camera information, which may simply be the camera number or name. It may also refer to other information such as recording type.

### Storage

Finally, the recorder’s storage system will often contain information surrounding device access, user control, power outage, etc. The amount of extra information is often directly related to the system’s complexity. A small 4-camera system may only store the video, along with the date and time. However, a large 250+ camera system with storage spread over multiple devices may store all access and user-control logs, etc.

To summarize so far, we have a storage device that holds the data we require. Before we dig a little deeper into this data, we must understand that they cannot record everything, forever. They are limited in the amount of data they can retain.

### 4-camera System

To understand this, let us consider a basic 4-camera analog system with just a date and time index. Inside the device, there is an analog-to-digital conversion chip that can process video at a certain speed. This is usually referenced as Frames Per Second (FPS). In our example, the chip can manage 50 FPS.

If the device is set to record the maximum frames for all cameras, the frame rate for each camera would be 12.5 FPS. If the user has control of the settings, they would be able to set 1 camera perhaps to 25FPS, then one camera at 15, and two cameras at 5.

### DVR

Our basic example DVR has three quality settings. This controls the amount of compression that is applied after the analog-to-digital conversion. Having high compression would mean lower quality and vice versa.

Most systems also have a frame size option. This controls how many pixels, the smallest part of a digital image, should be used to make up our encoded video frame. They are often referenced by the width and height, rather than the total pixels. For example, 704 pixels x 576 pixels.

There could be various other settings but we have covered the standard three that control the amount of data that can be fit ono the storage device within the recorder.

Within the storage device, all our data is stored on a Hard Disk Drive (HDD). They are very similar to those found in standard computers but often optimized for 24/7 running. Just like the ones within your computer, they are restricted in the amount of data they can hold. This is known as the system’s retention period.

With full FPS, the highest compression quality, and then then the largest frame size, our system may be able to record 10 days worth of footage before it starts to overwrite the oldest data.

In contrast, with 1 FPS on all cameras, low-quality compression, and then a small frame size, the owner may be able to achieve a 6-week retention period.

### Remember

High frame rate, high quality, large frame size = Lower retention but better evidence.
Low frame rate, low quality, small frame size = Higher retention but a reduction in the evidential qu...