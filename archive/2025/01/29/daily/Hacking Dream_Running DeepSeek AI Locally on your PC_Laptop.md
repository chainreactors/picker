---
title: Running DeepSeek AI Locally on your PC/Laptop
url: https://www.hackingdream.net/2025/01/running-deepseek-ai-locally-on-your-pc-laptop.html
source: Hacking Dream
date: 2025-01-29
fetch_date: 2025-10-06T20:07:13.048740
---

# Running DeepSeek AI Locally on your PC/Laptop

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### Running DeepSeek AI Locally on your PC/Laptop

[January 28, 2025](https://www.hackingdream.net/2025/01/running-deepseek-ai-locally-on-your-pc-laptop.html "permanent link")

DeepSeek, a groundbreaking Chinese artificial intelligence (AI) company founded in 2023 by Liang Wenfeng and headquartered in Hangzhou, Zhejiang, has captured the global AI market's attention. With backing from the Chinese hedge fund High-Flyer, DeepSeek has quickly risen as a formidable contender in the AI space. In January 2025, the company made waves by releasing its flagship AI model, R1.

If you're looking to run DeepSeek AI locally on your PC or laptop, you're in the right place. In this guide, we'll cover essential details about the R1 model, its advantages, and step-by-step instructions for getting it up and running on your personal machine.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWtDhe8OsfSjin4-pp5_DBqWPgdxH0bxwsBTYjht8nOiMgaA83xxDcw7zdnbg3F7pi09NlJISofqBKdXtQYixZNTccZgg2opCFEgMvyfQcA0FLphXLjnlz4jRfJt9ZjBfSjAS2CaJpvpMMVngGnbG4IISMe0as7MISPHQ_RwkZ_sEKazaGvwU-0nrcjuz7/w640-h344/DeepSeek-AI.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWtDhe8OsfSjin4-pp5_DBqWPgdxH0bxwsBTYjht8nOiMgaA83xxDcw7zdnbg3F7pi09NlJISofqBKdXtQYixZNTccZgg2opCFEgMvyfQcA0FLphXLjnlz4jRfJt9ZjBfSjAS2CaJpvpMMVngGnbG4IISMe0as7MISPHQ_RwkZ_sEKazaGvwU-0nrcjuz7/s1024/DeepSeek-AI.jpg)

## Why Choose DeepSeek AI R1 for Local Use?

DeepSeek's R1 model stands out for several reasons:

1. **Cost-Efficiency:** Developed for approximately $6 million, R1 delivers performance comparable to leading AI models like OpenAI’s ChatGPT, which required substantially higher investments.
2. **Mixture of Experts Architecture:** This innovative design activates only the necessary computing resources for a specific task, optimizing efficiency and reducing energy consumption.
3. **Open-Source Availability:** DeepSeek has made its models open-source, allowing researchers and developers worldwide to access and build upon their work.
4. **Local Deployment:** Running DeepSeek AI locally ensures data privacy and eliminates the need for constant internet connectivity.

## Requirements

Before diving into the setup process, ensure your system meets the following requirements:

* Graphics Card: A GPU with CUDA support for efficient processing.
* Memory: At least 16/32 GB of RAM to handle the operations smoothly.
* Operating System: A Windows, Linux, or MAC OS environment.

## Process Overview

The process involves four main steps:

1. Setting up WSL (Windows Sub-System for Linux)
2. Installing OLLAMA
3. Installing DeepSeek AI
4. Running the LLM Model

### 1. Setting Up WSL (Windows Sub-System for Linux)

Note: This process is to setup Linux environment on windows, if you already have a working Linux setup, feel free to skip to Step 2.

Windows Sub-System for Linux (WSL) allows you to run a Linux environment directly on Windows, without the overhead of a virtual machine. Here's how to set it up:

####

#### 1. Enable WSL

1. Open Powershell Command Prompt as an administrator.
2. `[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhF7hHK2w10BtExJVjIlYrv3RQOTKn7JZ1AjQHspJtHG-Yasc3_W5701cvN5KTbHUxsKD9IRiIzLgKEmJJ8jcY4WbSiOr5xs5t123RyX_q06_Nh-RMuTn1r4GgL6U8sahekhrLvRaDTkwixmkTDzwPAuK-BFL2IdITuBsGDsaRBEMOu3ciNgqn_fUUPu6WH/w640-h388/running%20powershell%20as%20administrator.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhF7hHK2w10BtExJVjIlYrv3RQOTKn7JZ1AjQHspJtHG-Yasc3_W5701cvN5KTbHUxsKD9IRiIzLgKEmJJ8jcY4WbSiOr5xs5t123RyX_q06_Nh-RMuTn1r4GgL6U8sahekhrLvRaDTkwixmkTDzwPAuK-BFL2IdITuBsGDsaRBEMOu3ciNgqn_fUUPu6WH/s763/running%20powershell%20as%20administrator.png)`

and run the command:

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFCDumxffzKkFpCIeclKil_uKWavD-RDmzufTDSqrNaA7_tLSRxrk8iAZGhKMCnfr4OnJREESbI-8niXiih8srLPodR1YCNS4vmRhim_kQdIGuLxTXFuSU8jyk5_4VPdzp0QDLc_jnhl25BEyEhU3MVGKZvdl6uspNkhhkbBrd2rB9XZ1gv95OlTsFvTXw/w640-h176/turning%20on%20wsl.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFCDumxffzKkFpCIeclKil_uKWavD-RDmzufTDSqrNaA7_tLSRxrk8iAZGhKMCnfr4OnJREESbI-8niXiih8srLPodR1YCNS4vmRhim_kQdIGuLxTXFuSU8jyk5_4VPdzp0QDLc_jnhl25BEyEhU3MVGKZvdl6uspNkhhkbBrd2rB9XZ1gv95OlTsFvTXw/s978/turning%20on%20wsl.png)

**Note:** If RestartNeeded: True, you are supposed to restart your machine before continuing the process.

####

####

#### 1. Install Linux Distribution

1. Install Ubuntu (or your preferred distribution) by running ``wsl --install -d Ubuntu`` You'll be prompted to enter a username and password. Once completed, your Linux environment is ready to use.
   In this case, I have it installed already, but you should see something similar to below once the setup is completed.

   ```
   wsl --install -d Ubuntu
   ```
2. [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSeNVmhDxKiH_FbyZOHx1gFSzqAi9Nt4sXN0CDTMgacxhKYnlGq1y8O2NXOlkWCMP216X9DVJ7ZQSncdMmGJcM013uSd1EPl33VZ44tkBsAEXKO92Uf8Yhi5d5-s_CzAjlq-dWDOSe7nan65sdncvO5Qk5W7r5r6G0QrRiY4NCN3GEkBYRh5mYYySiW49H/w640-h172/installing%20ubuntu%20on%20wsl.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSeNVmhDxKiH_FbyZOHx1gFSzqAi9Nt4sXN0CDTMgacxhKYnlGq1y8O2NXOlkWCMP216X9DVJ7ZQSncdMmGJcM013uSd1EPl33VZ44tkBsAEXKO92Uf8Yhi5d5-s_CzAjlq-dWDOSe7nan65sdncvO5Qk5W7r5r6G0QrRiY4NCN3GEkBYRh5mYYySiW49H/s761/installing%20ubuntu%20on%20wsl.png)

### 2. Installing OLLAMA

OLLAMA is a platform that simplifies the installation and running of LLM models. To install OLLAMA:

1. Access WSL Terminal: Run ``wsl -d Ubuntu`` in the Command Prompt to access your Linux terminal.
2. Install OLLAMA: Execute the below command`.` You may need to enter your root user credentials set during WSL setup.

   ```
   curl https://ollama.ai/install.sh | sh
   ```
3. [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrnMFPzgRPYmLuBlvw8OO0cjPwHKeW0wJ0imoRp4I0ZKyz7FoJxbOLPP2XrhCPvMGBpZvGGREze1nnUZbFq0QOcNlGvuHZzHheT4gix1G-sGnvRYI7BwqahJDEQxH3GC8hh7Rv1r2xj1rpI2bH8LVDyYNS48AEB7mWsloNkFYGDljQ9bR7_WX2Qxbys4Ka/w640-h238/installing%20ollama%20on%20ubuntu%20wsl.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrnMFPzgRPYmLuBlvw8OO0cjPwHKeW0wJ0imoRp4I0ZKyz7FoJxbOLPP2XrhCPvMGBpZvGGREze1nnUZbFq0QOcNlGvuHZzHheT4gix1G-sGnvRYI7BwqahJDEQxH3GC8hh7Rv1r2xj1rpI2bH8LVD...