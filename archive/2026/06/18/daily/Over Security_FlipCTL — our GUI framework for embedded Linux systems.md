---
title: FlipCTL — our GUI framework for embedded Linux systems
url: https://blog.flipper.net/flipctl-our-gui-framework-for-embedded-linux-systems/
source: Over Security
date: 2026-06-18
fetch_date: 2026-06-19T07:08:52.499350
---

# FlipCTL — our GUI framework for embedded Linux systems

[![Flipper Blog](https://blog.flipper.net/content/images/2022/07/orange_text_transpar-2.png)](https://blog.flipper.net)

* [Home](https://flipper.net/)
* [Products](https://flipper.net/collections)
* [Docs](https://docs.flipper.net/)
* [Downloads](https://flipper.net/pages/downloads)
* [Community](https://flipper.net/pages/community)

Subscribe to notifications of new posts:

You're subscribed

Oops! Please try again

Subscribe

# FlipCTL — our GUI framework for embedded Linux systems

* [![Pavel Zhovner](/content/images/size/w100/2020/10/9a8180b4-80fa-4c50-9e83-bee59e3bc348-1.png)](/author/zhovner/)

#### [Pavel Zhovner](/author/zhovner/)

18 Jun 2026
• 8 min read

[Share](#/share)

![FlipCTL — our GUI framework for embedded Linux systems](/content/images/size/w2000/2026/06/flipctl_flipper_one_drawing_.png)

Do you know why Flipper Zero is so popular? Not because of the little cute dolphin, but because you can use it right out of the box. If we made Flipper Zero in a Proxmark3-like form factor without a screen (no offense, Iceman), it would only be used by a small group of hardcore professionals. We all love simple, clear things: press a button and get results.

Before Flipper Zero, no one really cared about intuitive interfaces of niche devices for geeks. Everyone was building separate hardware and a companion app for user interface. **NO ONE WANTS TO CREATE PIXEL-PERFECT INTERFACES** for small screens - it's a pain, even for us. But we've become pretty good at it, and we believe we can contribute to the industry by creating a universal graphical interface framework. Since we were doing this for Flipper One anyway, we decided to open it up for others to use in their own projects.

**In this post:**

* FlipCTL: our GUI framework for embedded systems, which can be used on any Linux device.
* Why all existing interfaces for embedded systems suck.
* Help us develop the right architecture for FlipCTL.

# GUI — the main problem of all cyberdecks

![](https://blog.flipper.net/content/images/2026/06/12Untitled89.jpg)

It's impossible to use mini-computers with tiny screens because they all use a desktop interface designed for a mouse and a keyboard

Cyberdecks look cool, but they’re impossible to use. The main problem with all cyberdecks is their crappy interface. They usually just take a standard KDE/GNOME desktop, or even Windows, and try to pretend you can actually use it. No, you can’t. It’s bullshit. It’s impossible to hit a microscopic button on the screen using a touchscreen or tiny trackball, and plugging in a mouse is awkward.

## Desktop vs small-screen optimized interface

In most cyberdecks, the controls are not designed for the user interface running on the device. The typical approach is to add some buttons and run a desktop interface that was built for a mouse and keyboard. That's the main problem.

[![](https://img.spacergif.org/v1/1920x1080/0a/spacer.png)](https://blog.flipper.net/content/media/2026/06/desktopUI_VS_FlipCTL_V2.2_compressed-1080.mp4)

0:00

/0:14

1×

Which interface do you find more user-friendly on a small screen?

Only major vendors can afford to develop controls and graphical interfaces together, with each designed around the other: game consoles, smartphones, televisions, and the like. This requires a dedicated team and long, thankless hours of work. You need to build a UX system and go through countless iterations of testing and improvement. DIY projects by enthusiasts typically don't have that luxury. We decided to try to change that, so any project can have a great graphical interface with little effort.

# Why did we choose a grayscale display over a fancy color one?

The answer is that grayscale display is better in every way for system GUIs where color isn't needed. Just look at the comparison photo, and your questions will be answered.

![](https://blog.flipper.net/content/images/2026/06/greyscale_vs_color_display_compressed.jpg)

The main advantages of a grayscale display:

* **Low power consumption** — our display can be used without a backlight, as ambient light is reflected by the display's backing layer. In this mode, power consumption drops to just 14 mW. Color displays always require a backlight, and in bright outdoor conditions, you need to set the backlight level to maximum to keep the display readable. In this case, a similarly sized color display typically consumes 800–1000 mW.
* **Perfectly visible in direct sunlight** — the brighter the sun, the better our grayscale display looks. Color displays, on the other hand, become increasingly difficult to read outdoors. We want our interface to be usable in real-world field conditions, not just on a desk for social media photos.
* **Less system load** — to achieve truly high image quality on a color display, you need a VERY expensive, high-resolution display that requires significant computing resources and puts a strain on the system just to render the image. A color display would STILL lose out to our grayscale display in terms of contrast. Meanwhile, on a grayscale display, you can achieve high image quality even on low-power embedded systems.

# Our custom LCD display

![](https://blog.flipper.net/content/images/2026/06/image-8.png)

For Flipper One, we designed our own grayscale display with a custom resolution of 256×144 pixels. Displays of this type are no longer actively developed, and most off-the-shelf grayscale displays are limited to 128×64 pixels. Manufacturers are no longer willing to invest in this technology, so we put significant effort into developing the exact display we needed. As a result, we have a grayscale screen made using IPS technology.

# What is FlipCTL?

FlipCTL is our attempt to create a universal GUI and physical controls (buttons, touchpad) that can be used in any project. It will work on all embedded Linux systems and be easily adapted to your needs. With FlipCTL, you don’t have to reinvent the user interface from scratch every time: you can just grab our framework and quickly implement a GUI for your project.

![](https://blog.flipper.net/content/images/2026/06/flipctl_gui_scheme-_compressed.png)

FlipCTL wraps existing console programs and system settings, and converts them into menu-based, small-screen interfaces

**How FlipCTL works:**

* FlipCTL is a middleware that runs as a service, wrapping CLI applications in a graphical interface.
* It renders the screen image and redirects user input (buttons, touchpad, etc).
* It can manage Linux system settings and services.

The main idea is to make deploying FlipCTL on any system as simple as possible, while also simplifying the development of graphical interfaces.

# FlipCTL architecture

FlipCTL is a modular system consisting of a backend and a frontend. Devices other than Flipper One can be used to interact with the FlipCTL user interface.

The FlipCTL architecture is under development, and you can join the discussion or even lead the project. [Read more >>](https://docs.flipper.net/one/cpu-software/flipctl)

![](https://blog.flipper.net/content/images/2026/06/FlipCTL-GUI--1-.jpg)

FlipCTL consists of several modules and can run on different platforms

**Core Components of FlipCTL:**

* **Backend** is responsible for managing the operating system itself. It can interact with systemd, control OS services, configure networking through NetworkManager or systemd-networkd, and wrap existing command-line utilities such as `nmap`, `ping`, and `traceroute`. The backend exposes these capabilities through APIs that are consumed by the frontend.
* **UI Frontend** is currently built using HTML and JavaScript. Despite the associated overhead, this approach enables rapid UI development and compact implementation, while avoiding the need for specialized expertise required by many embedded UI frameworks.
* **Renderer** is a web browser. On Flipper One, we currently use a headless WebKit instance running directly on top of DRM (Direct Rendering Manager), without Xorg or Wayland. We also w...