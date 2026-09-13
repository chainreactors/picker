---
title: Dropper
url: https://kitploit.com/en/tools/github/gmh5225/dropper
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:27.180628
---

# Dropper

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

Dropper — Tool for embedding payloads into JPG/PNG format images, allowing to perform certain actions when opening them. | Kitploit

[Tools](/en/tools)/![GitHub](/providers/github.png)GitHub/gmh5225/dropper

![](https://assets.kitploit.com/production/public/tools/54894/41034f6a4b714be970b0df9ef6544ff22cdc66a4ac93e947d9cfb1badd9df338-display-v1.webp)

[Defensive Tools](/en/categories/defensive-tools)[Exploitation](/en/categories/exploitation)[Steganography](/en/categories/steganography)[Malware Analysis](/en/categories/malware-analysis)[Penetration Testing](/en/categories/penetration-testing)[Red Teaming](/en/categories/red-teaming)[Payload Development](/en/categories/payload-development)

![GitHub](/providers/github.png)gmh5225/dropper

# Dropper

Tool for embedding payloads into JPG/PNG format images, allowing to perform certain actions when opening them.

[View Repository](https://github.com/gmh5225/dropper)

25291 year ago![Not yet reviewed](/_next/image?url=%2Fbadges%2Fkitploit_badge_not_reviewed_full.png&w=48&q=75)

### Most Popular

[View all →](/en/tools)

Discover the most used tools by our community.

Last 7 DaysLast 30 Days

Explore all tools

Browse our collection of tools

[View all tools →](/en/tools)

Share

# Stealth dropper JPEG/PNG

This project is a tool for embedding payloads into JPG/PNG format images, allowing you to perform certain actions when opening them.

## 🚫 Disclaimer

This repository is provided for **educational purposes only** and intended for **authorized security research**.
Use of these materials in unauthorized or illegal activities is **strictly prohibited**.

### Guide to working with the project and using **exploit3r.py**

The project uses **CMake** to automate building and integrating various libraries, including Python 2. Below are the main steps to build the project and use the exploit.

#### Main features of **CMakeLists.txt**:

1. **C++ standard and compilation options**:

   * The project is configured to use the C++17 standard.
   * Compilation flags `-Wall` for warnings and `-g` for debug information are added.
2. **Linking external libraries**:

   * The project uses the following external libraries:

     + **Capstone**: disassembly framework.
     + **Pwnlib**: security functions library.
     + **S2E**: symbolic execution engine.
     + **LLVM**: compiler infrastructure.
     + **Boost**: C++ library collection (includes the `signals2` component).
     + **KLEE**: dynamic analysis tool.
3. **Integration with Python 2 via pybind11**:

   * Pybind11 is used to bind C++ code with Python 2.
4. **Installing Python 2 dependencies**:

   * All Python 2 dependencies are automatically installed via CMake when running `pip2 install -r requirements.txt`.
5. **Automatic file handling**:

   * Files `exploit3r.py` and `Resou.sln.scr` are automatically copied to the output directory after building, but they are not executed automatically.
6. **Compilation and linking**:

   * CMake compiles all `.cpp` files in the project and generates the executable.
   * The project is linked with the aforementioned libraries: Capstone, Pwnlib, S2E, LLVM, Boost, KLEE, and pybind11.

#### Building the project:

1. To build the project, run the following commands:

* mkdir build
* cd build
* cmake ..
* make

**This will generate the project executable and copy the necessary Python files and other scripts to the output directory.**

#### Using **exploit3r.py**

1. **Step 1: Installing Python 2 dependencies**:
   Make sure you have Python 2 installed. All Python dependencies are listed in the `requirements.txt` file. To install them, run:

   `pip2 install -r requirements.txt`

   This will install the required libraries such as **BeautifulSoup**, **argparse**, **requests**, and others.
2. **Step 2: Running the **exploit3r.py** script**:
   After the project has been successfully built and all dependencies installed, you can run the **exploit3r.py** script manually. It should be run in a Python 2 environment.

   `python2 exploit3r.py`

   **exploit3r.py** is the main part of the program for generating the exploit file. After launch, a graphical interface will appear where you can select the malware file (e.g., .exe file) and the JPG file in which the malicious code will be embedded.
3. **Step 3: Using the interface**

   * Select the malware file (e.g., payload.exe).
   * Select the JPG image in which the malicious code will be embedded.
   * Configure additional options such as MD5, code execution after embedding, and auto-update.
   * Click **Build Silent JPG**.
4. **Step 4: Verifying the result**
   After completion, you will obtain a file that appears to be an image but contains malicious code. You can test this file with various antivirus scanners to check its stealth.

#### Important notes:

* This project is created to integrate C++ and Python 2. Make sure you have Python 2 installed for proper operation.

[Download Tool](https://github.com/gmh5225/dropper)