---
title: AiCEF - An AI-assisted cyber exercise content generation framework using named entity recognition
url: https://buaq.net/go-173789.html
source: unSafe.sh - 不安全
date: 2023-08-07
fetch_date: 2025-10-04T11:58:51.817747
---

# AiCEF - An AI-assisted cyber exercise content generation framework using named entity recognition

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

AiCEF - An AI-assisted cyber exercise content generation framework using named entity recognition

AiCEF is a tool implementing the accompanying framework [1] in order to harness the intellig
*2023-8-6 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-173789.htm)
阅读量:40
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEioxQE67TH_hzy1aAibAY4sxeEJorPyIPy9i5EJ1DN7pFNlIsYI8gQhp5SgYAJVrOj7tIJaiCEJqh0jGeM1vGxTX8LOi4e7ujY7HkNEH7S03RSfd-ZMPUt4dLw7mJCP2ZK4oO_2uBjJiKNVwKemySD53ooRiK48vlBOLcWp9tjDnooUmn8fTM5EeY-Mxm3n=w640-h286)](https://blogger.googleusercontent.com/img/a/AVvXsEioxQE67TH_hzy1aAibAY4sxeEJorPyIPy9i5EJ1DN7pFNlIsYI8gQhp5SgYAJVrOj7tIJaiCEJqh0jGeM1vGxTX8LOi4e7ujY7HkNEH7S03RSfd-ZMPUt4dLw7mJCP2ZK4oO_2uBjJiKNVwKemySD53ooRiK48vlBOLcWp9tjDnooUmn8fTM5EeY-Mxm3n)

AiCEF is a tool implementing the accompanying framework [1] in order to harness the [intelligence](https://www.kitploit.com/search/label/Intelligence "intelligence") that is available from online resources, as well as threat groups' activities, arsenal (eg. MITRE), to create relevant and timely cybersecurity exercise content. This way, we abstract the events from the reports in a machine-readable form. The produced graphs can be infused with additional intelligence, e.g. the threat actor profile from MITRE, also mapped in our ontology. While this may fill gaps that would be missing from a report, one can also manipulate the graph to create custom and unique models. Finally, we exploit transformer-based language models like GPT to convert the graph into text that can serve as the scenario of a cybersecurity exercise. We have tested and validated AiCEF with a group of experts in cybersecurity exercises, and the results clearly show that AiCEF significantly augments the capabilities in creating timely and relevant cybersecurity exercises in terms of both quality and time.

We used Python to create a machine-learning-powered Exercise Generation Framework and developed a set of tools to perform a set of individual tasks which would help an exercise planner (EP) to create a timely and targeted [Cybersecurity](https://www.kitploit.com/search/label/Cybersecurity "Cybersecurity") Exercise Scenario, regardless of her experience.

**Problems an Exercise Planner faces:**

* Constant table-top research to have fresh content
* Realistic CSE scenario creation can be difficult and time-consuming
* Meeting objectives but also keeping it appealing for the target audience
* Is the relevance and timeliness aspects considered?
* Can all the above be automated?

**Our Main Objective:** Build an AI powered tool that can generate relevant and up-to-date Cyber Exercise Content in a few steps with little technical expertise from the user.

## Release Roadmap

The updated project, AiCEF v.2.0 is planned to be publicly released by the end of 2023, pending heavy code review and functionality updates. Submodules with reduced functinality will start being release by early June 2023. Thank you for your patience.

## Installation

The most convenient way to install AiCEF is by using the *docker-compose* command. For production deployment, we advise you deploy MySQL manually in a dedicated environment and then to start the other components using Docker.

First, make sure you have *docker-compose* installed in your environment:

###  Linux:

```
$ sudo apt-get install docker-compose
```

Then, clone the repository:

```
$ git clone https://github.com/grazvan/AiCEF/docker.git /<choose-a-path>/AiCEF-docker
```

### Configure the environment settings

Import the MySQL file in your

```
$ mysql -u <your_username> â€“-password=<your_password> AiCEF_db < AiCEF_db.sql
```

Before running the `docker-compose` command, settings must be configured. Copy the sample settings file and change it accordingly to your needs.

### Run AiCEF

**Note:** Make sure you have an OpenAI API key available. Load the environment setttings (including your MySQL connection details):

Finally, run `docker-compose` in detached (`-d`) mode:

```
$ sudo docker-compose up -d
```

## Usage

A common usage flow consists of generating a Trend Report to analyze patterns over time, parsing relevant articles and converting them into Incident [Breadcrumbs](https://www.kitploit.com/search/label/Breadcrumbs "Breadcrumbs") using MLTP module and storing them in a knowledge database called KDb. Incidents are then generated using IncGen component and can be enhanced using the Graph Enhancer module to simulate known APT activity. The incidents come with injects that can be edited on the fly. The CSE scenario is then created using CEGen, which defines various attributes like CSE name, number of Events, and Incidents. MLCESO is a crucial step in the methodology where dedicated ML models are trained to [extract information](https://www.kitploit.com/search/label/Extract%20Information "extract information") from the collected articles with over 80% accuracy. The Incident Generation & Enhancer (IncGen) workflow can be automated, generating a variety of incidents based on filtering parameters and the existing database. The knowledge database (KDB) consists of almost 3000 articles classified into six categories that can be augmented using APT Enhancer by using the activity of known APT groups from MITRE or manually.

Find below some sample usage screenshots: [![](https://blogger.googleusercontent.com/img/a/AVvXsEioxQE67TH_hzy1aAibAY4sxeEJorPyIPy9i5EJ1DN7pFNlIsYI8gQhp5SgYAJVrOj7tIJaiCEJqh0jGeM1vGxTX8LOi4e7ujY7HkNEH7S03RSfd-ZMPUt4dLw7mJCP2ZK4oO_2uBjJiKNVwKemySD53ooRiK48vlBOLcWp9tjDnooUmn8fTM5EeY-Mxm3n=w640-h286)](https://blogger.googleusercontent.com/img/a/AVvXsEioxQE67TH_hzy1aAibAY4sxeEJorPyIPy9i5EJ1DN7pFNlIsYI8gQhp5SgYAJVrOj7tIJaiCEJqh0jGeM1vGxTX8LOi4e7ujY7HkNEH7S03RSfd-ZMPUt4dLw7mJCP2ZK4oO_2uBjJiKNVwKemySD53ooRiK48vlBOLcWp9tjDnooUmn8fTM5EeY-Mxm3n)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhBi_uP_lvwexfhVKDHWcQEqtF1AU8HkUKzVVyboZUvUePcf0_OIIQfBw_YE21Oa78MDJXrHCe22pSUPSkJ-gLSqpDMSJgIi4VIhYP8WnyygqguYrWc0Sl2FQsjjdbtbP9Fbbbx2nYeW2tckk1o5FYF8UltcQD8ewLDgUjsH71yVATxPT5S-8fIVoFpHMco=w640-h288)](https://blogger.googleusercontent.com/img/a/AVvXsEhBi_uP_lvwexfhVKDHWcQEqtF1AU8HkUKzVVyboZUvUePcf0_OIIQfBw_YE21Oa78MDJXrHCe22pSUPSkJ-gLSqpDMSJgIi4VIhYP8WnyygqguYrWc0Sl2FQsjjdbtbP9Fbbbx2nYeW2tckk1o5FYF8UltcQD8ewLDgUjsH71yVATxPT5S-8fIVoFpHMco)

## Features

* An AI-powered Cyber Exercise Generation Framework
* Developed in Python & [EEL](https://github.com/python-eel/Eel "EEL")
* Open source library [Stixview](https://github.com/traut/stixview "Stixview")
* Stores data in MYSQL
* API to Text Synthesis Models (ex. GPT-3.5)
* Can create incidents based on TTPs of 125 known APT actors
* Models Cyber Exercise Content in machine readable STIX2.1 [2] (.json) and human readable format (.pdf)

## Authors

AiCEF is a product designed and developed by Alex Zacharis, Razvan Gavrila and Constantinos Patsakis.

## References

[1] [https://link.springer.com/article/10.1007/s10207-023-00693-z](https://link.springer.com/article/10.1007/s10207-023-00693-z "https://link.springer.com/article/10.1007/s10207-023-00693-z")

[2] [https://oasis-open.github.io/cti-documentation/stix/intro.html](https://oasis-open.github.io/cti-documentation/stix/intro.html "https://oasis-open.github.io/cti-documentation/stix/intro.html")

## Contributing

Contributions are welcome! If you'd like to contribute to AiCEF v2.0, please follow these steps:

1. Fork this repository
2. Create a new branch (`git checkout -b feature/your-branch-name`)
3. Make your changes and commit them (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-...