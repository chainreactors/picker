---
title: Octosuite: A New Tool to Conduct Open Source Investigations on GitHub
url: https://www.bellingcat.com/resources/2023/01/20/octosuite-a-new-tool-to-conduct-open-source-investigations-on-github/
source: bellingcat
date: 2023-01-21
fetch_date: 2025-10-04T04:30:56.977723
---

# Octosuite: A New Tool to Conduct Open Source Investigations on GitHub

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

[![](https://www.bellingcat.com/app/uploads/2021/12/Bellingcat-logo-avatar-300x284.jpg)](https://www.bellingcat.com/author/richardw/)
[Richard W](https://www.bellingcat.com/author/richardw/)

Richard W is a programmer and Bellingcat Investigative Tech Fellow.

# Octosuite: A New Tool to Conduct Open Source Investigations on GitHub

January 20, 2023

* [Octosuite](/tag/octosuite)
* [Tech Team](/tag/tech-team)

GitHub is one of the most popular code-hosting platforms on the internet, with a [global community](https://octoverse.github.com/2022/global-tech-talent) of more than 90 million people [reported](https://techcrunch.com/2022/10/25/microsoft-says-github-now-has-a-1b-arr-90m-active-users/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAABfXc1LGR8bctXWrNXjJYo9_62fp-U06RmQYBRtWck-C1__8p5p5RPn_uNcsNh5HlIr2HPb9rYsObpPZn3mDaPcrWM1l5uL3LfyEcAE3x-fqoQT7pvDyLATR7kE_vDYChHdUosHjuFuJMeGXGGyJoqCtfNLy80IRqJh60ooFiUD0) to use its services.

This makes GitHub a key platform for coders and developers. Many useful tools that aid open source investigations can be found on the site (including on Bellincgat’s GitHub [repository](https://github.com/bellingcat)).

Given the amount of information users share on the platform, GitHub itself can also be a useful source for online investigators.

For example, information available on GitHub can be cross-referenced with other social media or online content that has been publicly shared.

While GitHub has an intuitive user interface, it requires many click-throughs and is limited to opening one entity (be that an individual page or user or organisation profile) at a time.

On top of this, there is no easy way to save the information one comes across on GitHub.

This is where Octosuite comes in. Octosuite is an advanced GitHub framework written in Python that uses GitHub’s Public API to make the process of investigating accounts and repositories on the platform more efficient, while also creating a set of automated and easily reproducible queries.

![](https://www.bellingcat.com/app/uploads/2023/01/Screenshot-2023-01-19-at-17.40.50-redacted_dot_app-1200x807.png)

Image: Octosuite command line interface help menu

**What can Octosuite do?**

Octosuite comes with a wide range of commands that can be used to obtain information on accounts and repositories that are publicly visible on GitHub.

With Octosuite, one can easily find public information on:

* **Users**: profile information, gists (small code snippets), account activity (via events like subscribe, create, follow), repositories, organisations, subscriptions, followers and follows
* **Organisations**: profile information, account activity, repositories, and public members
* **Repositories**: contributors, coding languages, stargazers (equivalent of likes in the platform), forks (details who has created a public copy of the repository) and releases

Octosuite also includes a search feature that looks for users, repositories, topics (a development tag that helps understand the purpose of the code), commits (a response or change to a file or set of files made by a user) and issues (conversation threads the community can use to flag problems or ask for features or help).

All outputs from these searches are available in a readable format and can be exported in comma-separated value (CSV) format.

**Getting started with Octosuite**

Setting up Octosuite is a straightforward process.

It can be installed and used in two ways; as a command-line interface (CLI) or as a graphical user interface (GUI).

If you are not comfortable with the command line, the GUI option (with installation instructions on [Windows](https://github.com/bellingcat/octosuite/wiki/INSTALLATION#windows) and [macOS](https://github.com/bellingcat/octosuite/wiki/INSTALLATION#mac-os)) is obviously preferable. The GUI version of the tool allows users to select search commands from a dropdown menu.

However, the CLI can be more flexible in processing the scraped data, or batch processing it. You will also need to know the command line basics to install the GUI version of the tool. For full instructions on how to install the GUI version of Octosuite, see this [GitHub guide](https://github.com/bellingcat/octosuite/wiki/INSTALLATION).

The remainder of this article will detail how to use the CLI version of the tool.

**Octosuite Commands**

If you’re familiar with the command line (on Windows, Linux or Mac), you can simply open a terminal window and enter the following command to install Octosuite: `*pip3 install octosuite*`

But make sure you have Python 3 installed before running the command.

A beginners guide to using the command line can be found [here](https://www.freecodecamp.org/news/command-line-for-beginners/).

Once the installation process is complete, you can start Octosuite by running the command: `*octosuite`*

Alternatively, you can use the following command to see available options to run Octosuite with command line arguments: *`octosuite –help`*

![](https://www.bellingcat.com/app/uploads/2023/01/Screenshot-2023-01-19-at-19.20.40-redacted_dot_app.png)

Image: Octosuite prompt to enable colours for a session.

You will get an initial prompt asking if you would like to enable colours in the program (this makes the experience more engaging), choose ‘y’ for yes, and ‘n’ for no. After that, you will see the main screen.

![](https://www.bellingcat.com/app/uploads/2023/01/Screenshot-2023-01-19-at-19.22.58.png)

Image: Octosuite main screen with colour option engaged.

From there, you can start with the `*help`* command to see a list of available commands.

![](https://www.bellingcat.com/app/uploads/2023/01/Screenshot-2023-01-19-at-19.24.21.png)

Image: The Octosuite help menu.

Octosuite investigation commands have subcommands with their own unique functionality. To list them just type *`help:investigation\_command`*. For example if you want to see all subcommands for the *user* command you should type the following: `*help:user*`.

A table showing all subcommands for the *user* command will then appear.

![](https://www.bellingcat.com/app/uploads/2023/01/Screenshot-2023-01-19-at-19.26.30.png)

Image: Octosuite user subcommands.

**User Subcommands**

Let’s try to get the profile information of a user.

You can do this by entering the command `*user:profile`. Y*ou will be prompted to enter a username. After doing so, hit enter.

The below screenshot shows the output containing the profile information of a user (with some details redacted). Octosuite will ask if you want to save the output to a CSV file. You can read saved CSV files with the command `*csv:read`*, delete a single CSV file with `*csv:delete`* or delete all CSV files by typing `*csv:clear*`.

![](https://www.bellingcat.com/app/uploads/2023/01/Screenshot-2023-01-19-at-19.40.44-redacted_dot_app.png)

Image: Octosuite showing a user’s profile information (with some details redacted).

**Pragmatic Octosuite**

Having the entire GitHub API at the tips of your fingers opens new possibilities for cross referencing data points or crafting specific queries. Octosuite can be extended to generalise some of these. Some current examples include:

* Check if user A follows user B: *`use...