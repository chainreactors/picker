---
title: frigate v0.18.0-rc1
url: https://kitploit.com/en/posts/github-blakeblackshear-frigate-v0180-rc1
source: Kitploit
date: 2026-09-01
fetch_date: 2026-09-02T06:40:11.248868
---

# frigate v0.18.0-rc1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/42367/4dcd1993ff0391a4b33a39f102d9354fdeff62bb1ffe4cc1d8a0125312b12e5c.png)

New releaseSep 1, 2026

# frigate v0.18.0-rc1

NVR with realtime local object detection for IP cameras

Share

![logo](https://assets.kitploit.com/production/public/readmes/42367/18b93b9e677bfc8a93765768151cd2d8f52361d0f9a49600de1a8c5b52e645ba.png)

# Frigate NVR™ - Realtime Object Detection for IP Cameras

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Translation status](https://hosted.weblate.org/widget/frigate-nvr/language-badge.svg)](https://hosted.weblate.org/engage/frigate-nvr/)

[English] | [简体中文](https://github.com/blakeblackshear/frigate/blob/dev/README_CN.md)

A complete and local NVR designed for [Home Assistant](https://www.home-assistant.io) with AI object detection. Uses OpenCV and Tensorflow to perform realtime object detection locally for IP cameras.

Use of a GPU or AI accelerator is highly recommended. AI accelerators will outperform even the best CPUs with very little overhead. See Frigate's supported [object detectors](https://docs.frigate.video/configuration/object_detectors/).

* Tight integration with Home Assistant via a [custom component](https://github.com/blakeblackshear/frigate-hass-integration)
* Designed to minimize resource use and maximize performance by only looking for objects when and where it is necessary
* Leverages multiprocessing heavily with an emphasis on realtime over processing every frame
* Uses a very low overhead motion detection to determine where to run object detection
* Object detection with TensorFlow runs in separate processes for maximum FPS
* Communicates over MQTT for easy integration into other systems
* Records video with retention settings based on detected objects
* 24/7 recording
* Re-streaming via RTSP to reduce the number of connections to your camera
* WebRTC & MSE support for low-latency live view

## Documentation

View the documentation at <https://docs.frigate.video>

## Donations

If you would like to make a donation to support development, please use [Github Sponsors](https://github.com/sponsors/blakeblackshear).

## License

This project is licensed under the **MIT License**.

* **Code:** The source code, configuration files, and documentation in this repository are available under the [MIT License](https://github.com/blakeblackshear/frigate/blob/HEAD/LICENSE). You are free to use, modify, and distribute the code as long as you include the original copyright notice.
* **Trademarks:** The "Frigate" name, the "Frigate NVR" brand, and the Frigate logo are **trademarks of Frigate, Inc.** and are **not** covered by the MIT License.

Please see our [Trademark Policy](https://github.com/blakeblackshear/frigate/blob/HEAD/TRADEMARK.md) for details on acceptable use of our brand assets.

## Screenshots

### Live dashboard

![Live dashboard](https://assets.kitploit.com/production/public/readmes/42367/4dcd1993ff0391a4b33a39f102d9354fdeff62bb1ffe4cc1d8a0125312b12e5c.png)

### Streamlined review workflow

![Streamlined review workflow](https://assets.kitploit.com/production/public/readmes/42367/729fbe5358373076bd9bae06a581bda84b8f1c9f9be55ccf103777c48a27cb4e.png)

### Multi-camera scrubbing

![Multi-camera scrubbing](https://assets.kitploit.com/production/public/readmes/42367/ccd714dbb8bdec28695001ee6a7a8ba3a36133309fabbb03f0238011deb34bf9.png)

### Built-in mask and zone editor

![Built-in mask and zone editor](https://assets.kitploit.com/production/public/readmes/42367/889030c95de64c6cb45c89b6244d926fabbc7ce7b2672363a5f82107b2e1ddeb.png)

## Translations

We use [Weblate](https://hosted.weblate.org/projects/frigate-nvr/) to support language translations. Contributions are always welcome.

[![Translation status](https://hosted.weblate.org/widget/frigate-nvr/multi-auto.svg)](https://hosted.weblate.org/engage/frigate-nvr/)

---

**Copyright © 2026 Frigate, Inc.**

[Read more](/en/tools/github/blakeblackshear/frigate?expand=1)

## Categories

[Defensive Tools](/en/categories/defensive-tools)[IoT Security](/en/categories/iot-security)[Cloud Security](/en/categories/cloud-security)[Machine Learning](/en/categories/machine-learning)[AI Security](/en/categories/ai-security)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Kitploit is a directory of hacking, cybersecurity, and pentesting tools. Discover the latest project updates to find vulnerabilities, analyze systems, automate testing, and strengthen your security.

·Analytics preferences·[Feeds](/en/feeds)·[Contact](/en/contact)·[Privacy](/en/privacy)·© 2026 Kitploit

Tool Directory

## Categories

[View all categories](/en/categories)

Loading categories