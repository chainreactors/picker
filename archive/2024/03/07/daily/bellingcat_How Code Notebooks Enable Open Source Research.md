---
title: How Code Notebooks Enable Open Source Research
url: https://www.bellingcat.com/resources/2024/03/06/how-code-notebooks-enable-open-source-research/
source: bellingcat
date: 2024-03-07
fetch_date: 2025-10-06T17:11:09.969195
---

# How Code Notebooks Enable Open Source Research

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)

* EN
  + [Русский](https://ru.bellingcat.com)
  + [Français](https://fr.bellingcat.com)
  + [Español](https://es.bellingcat.com)
  + [Deutsch](https://de.bellingcat.com)
  + [Українська](https://uk.bellingcat.com)
* [Donate](https://www.bellingcat.com/donate)

Search for:

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)
* [Donate](/donate)

[![Profile picture for: Miguel Ramalho](https://www.bellingcat.com/app/uploads/2023/03/Miguel-1200x1200.jpg)](https://www.bellingcat.com/author/miguelramalho/)
[Miguel Ramalho](https://www.bellingcat.com/author/miguelramalho/)

Miguel is a data scientist for Bellingcat focusing on understanding online manipulation and building tools and methods for open-source research.

# How Code Notebooks Enable Open Source Research

March 6, 2024

* [Tech Team](/tag/tech-team)
* [Tools](/tag/tools)

*Bellingcat has also published a repository of open source notebooks which you can [find on our GitHub here](https://github.com/bellingcat/open-source-research-notebooks)*

The number of open source tools out there is growing rapidly, but technical bars to entry mean they remain inaccessible to many researchers.

GitHub, a platform where developers share and discuss their code, is home to many of these tools. Searching the website for [open source investigation tools](https://github.com/search?q=%22osint%22+OR+%22osinv%22+OR+%22open+source+intelligence%22+OR+%22open+source+investigation%22+&type=repositories) can appear daunting to the uninitiated — there are more than six thousand results. Beyond this, many more of the platform’s over 300 million other projects, from [social media scrapers](https://github.com/JustAnotherArchivist/snscrape) to [AI models](https://github.com/serengil/deepface), also have a useful application in open source research.

But even many experienced researchers don’t use these tools. A 2022 survey by [Bellingcat found](https://www.bellingcat.com/resources/2022/08/12/these-are-the-tools-open-source-researchers-say-they-need/) that 45 per cent of researchers can’t use these tools, and in total 75 per cent have never used them. The core issue is accessibility: most tools are code scripts and command line interfaces. There’s no user interface to install, no web page to go to. While we encourage researchers to [learn the command line](https://www.youtube.com/watch?v=B3gm-ud91v0) and also teach it at our workshops, some tools require setup, debugging, and coding knowledge that limits who can effectively use them.

If you are part of that 45 percent or that 75 percent, there is a way to unlock this world of open source tools for your own research — code Notebooks! These are widely known as Jupyter Notebooks.

![](https://www.bellingcat.com/app/uploads/2024/03/image3-1-1200x388.png)

Notebooks [started off as a scientific tool](https://av.tib.eu/media/49958), and they are still mostly used for Data Science and AI projects, however their application can be much broader. Simply put, they are files in the .ipynb format where you can store and test code. They allow you to run Python, a coding language known for its simplicity. This is important for our purposes as it’s also the most popular language for open source research tools. They are run through interactive coding environments composed of sequential blocks (or cells) where each cell contains a piece of code or documentation about it. Usually a Notebook is accessed via a specific application on your computer where you can store and test code. Under the hood, the Notebook connects to a computer or server, its running environment. This can be your personal computer, if you set it up accordingly. But there’s a much easier way to familiarise yourself with Notebooks and that’s using online services that can read, display, and run them. Some of these have a more accessible user interface and, crucially, require less knowledge of the command line.

The most prominent of these is [Google Colab, a browser tool](https://colab.research.google.com/) which displays Notebook files no differently than a normal Google Doc or Sheets document with an accessible interface to match. They can be organised in your Drive, shared with others, edited by multiple people and, most importantly, executed safely like in a [virtual machine](https://www.bellingcat.com/resources/how-tos/2018/08/23/creating-android-open-source-research-device-pc/).

For example, the cell in the screenshot below from Google Colab contains a simple Python code. Pressing the play button in the top left-hand corner tests the code. Below the cell you can see the result of the code as executed in a remote server hosted by the Notebook service you’re using.

![](https://www.bellingcat.com/app/uploads/2024/03/image1.png)

There are also several alternative platforms like [Kaggle](https://www.kaggle.com/docs/notebooks) or [Binder](https://mybinder.org/). By using them, all you need to run a Notebook is the Notebook file itself (a file ending in .ipynb), while the running environment is hosted on a remote server.

### **Why are Notebooks useful?**

Notebooks can hugely simplify experimentation with coding tools, scripts and data analysis. They offer the following advantages:

1. **Accessibility** **—** You don’t need to know how to code to run a Notebook, it’s a simple click, observe, and scroll experience. All you need is a browser and internet connection, you can even run them on your mobile devices.

2. **Security —** When running a Notebook on Google Colab you do so in an isolated environment. Even if you download and execute a malicious piece of code, its impact is limited to the information you have on the notebook and not to your local computer, much like a [virtual machine](https://www.bellingcat.com/resources/how-tos/2018/08/23/creating-android-open-source-research-device-pc/).

3. **Replicability** **—** Many tools are built and tested on a limited number of operating systems and software versions. When installing and using them it’s not uncommon to get errors that are specific to your system because it was not part of the original tests. Online Notebook platforms give you standard environments, ensuring that what “works on my machine” will actually work on yours too.

4. **Readability** — Notebooks look and feel like a text document. Good Notebooks add not just “code” cells but also “text” cells with rich markdown explanations of the code. They can be self-documenting. In fact, Notebooks can be exported to PDF format and shared as a static product so you can assess the code without needing to run it.

5. **Customisation** — With minimal changes to the Notebook you can tailor its functions specifically for your investigations. When instructing a Notebook to install a tool to download a Youtube video, you can add a code cell where the video URL is specified. If you wanted to download a different video you’d only need to change the URL in that cell and hit run. Most tools and methods can be replicated by simple input changes such as the hashtag you search for, the website you’re inspecting, the dates you want to limit the results to.

6. **Flexibility** — Although notebooks are originally designed to run only code, the “code” cells can actually be used to run general command line instructions. This means a Notebook becomes like a virtual machine, allowing you to install a program, create a folder, download files, zip a folder and so on.

### Interacting With Notebooks

You can [explore our sample notebook on Google Colab](https://colab.research.google.com/github/bellingcat/open-source-research-notebooks/blob/main/...