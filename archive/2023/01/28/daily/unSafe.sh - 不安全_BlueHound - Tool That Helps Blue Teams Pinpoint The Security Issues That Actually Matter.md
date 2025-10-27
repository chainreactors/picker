---
title: BlueHound - Tool That Helps Blue Teams Pinpoint The Security Issues That Actually Matter
url: https://buaq.net/go-146849.html
source: unSafe.sh - 不安全
date: 2023-01-28
fetch_date: 2025-10-04T05:03:03.748972
---

# BlueHound - Tool That Helps Blue Teams Pinpoint The Security Issues That Actually Matter

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

![](https://8aqnet.cdn.bcebos.com/9de2bfc279553d5317e4b4a750d06e2f.jpg)

BlueHound - Tool That Helps Blue Teams Pinpoint The Security Issues That Actually Matter

BlueHound is an open-source tool that helps blue teams pinpoint the security issues that a
*2023-1-27 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-146849.htm)
阅读量:31
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjkEjbErH9NJ-aLN53fiZeqzGzeYETt-jTqn9pUFBrG9zdRAOfwjctfGBdWWScdirUhKGIrUsDQm8sqgezx2O1cs8wMjez6D8duhTCg1-qNrRpj0JsC3B1rgLUtuH6Y-dqpFHxzNVjwg_5zbT0W0JH0bWEQanXODyNL3td21L1110cGYYfx_cgGuyqkVw=w640-h332)](https://blogger.googleusercontent.com/img/a/AVvXsEjkEjbErH9NJ-aLN53fiZeqzGzeYETt-jTqn9pUFBrG9zdRAOfwjctfGBdWWScdirUhKGIrUsDQm8sqgezx2O1cs8wMjez6D8duhTCg1-qNrRpj0JsC3B1rgLUtuH6Y-dqpFHxzNVjwg_5zbT0W0JH0bWEQanXODyNL3td21L1110cGYYfx_cgGuyqkVw)

BlueHound is an open-source tool that helps [blue teams](https://www.kitploit.com/search/label/Blue%20Teams "blue teams") pinpoint the security issues that actually matter. By combining information about user permissions, network access and unpatched vulnerabilities, BlueHound reveals the paths attackers would take if they were inside your network

To get started with BlueHound, check out our [introductory video](https://youtu.be/WVup5tnURoM "introductory video"), [blog post](https://zeronetworks.com/blog/bluehound-community-driven-resilience/ "blog post") and [Nodes22 conference talk](https://www.youtube.com/watch?app=desktop&v=76MWt8uugAg "Nodes22 conference talk").

BlueHound supports presenting your data as tables, graphs, bar charts, line charts, maps and more. It contains a Cypher editor to directly write the Cypher queries that populate the reports. You can save dashboards to your database, and share them with others.

## Main Features

1. **Full Automation**: The entire cycle of collection, analysis and reporting is basically done with a click of a button.
2. **Community Driven**: BlueHound configuration can be exported and imported by others. Sharing of knowledge, best practices, collection methodologies and more, built-into the tool itself.
3. **Easy Reporting**: Creating customized report can be done intuitively, without the need to write any code.
4. **Easy Customization**: Any custom collection method can be added into BlueHound. Users can even add their own custom parameters or even custom icons for their graphs.

## Getting Started

### ROST ISO

BlueHound can be used as part of the [ROST image](https://zeronetworks.com/ROST-iso.zip "ROST image"), which comes pre-configured with everything you need (BlueHound, Neo4j, BloodHound, and a sample dataset).
To load ROST, create a new virtual machine, and install it from the ISO like you would for a new Windows host.

### BlueHound Binary

If you already have a Neo4j instance running, you can download a pre-compiled version of BlueHound from our [release page](https://github.com/zeronetworks/BlueHound/releases "release page"). Just download the zip file suitable to your OS version, extract it, and run the binary.

### Using BlueHound

1. Connect to your Neo4j server
2. Download [SharpHound](https://github.com/BloodHoundAD/BloodHound/blob/master/Collectors/SharpHound.exe "SharpHound"), [ShotHound](https://github.com/zeronetworks/BloodHound-Tools/tree/main/ShotHound "ShotHound") and the [Vulnerability Scanner report parser](https://github.com/zeronetworks/BloodHound-Tools/tree/main/VulnerabilitiesDataImport "Vulnerability Scanner report parser")
3. Use the **Data Import** section to collect & import data into your Neo4j database.
4. Once you have data loaded, you can use the **Configurations** tab to set up the basic information that is used by the queries (e.g. Domain Admins group, crown jewels servers).
5. Finally, the **Queries** section can be used to prepare the reports.

## Data Collection

The **Data Import Tools** section can be used to collect data in a click of a button. By default, BlueHound comes preconfigured with SharpHound, ShotHound, and the [Vulnerability Scanners](https://www.kitploit.com/search/label/Vulnerability%20Scanners "Vulnerability Scanners") script. Additional tools can be added for more data collection. To get started:

1. Download the relevant tools using the globe icon
2. Configure the tool path & arguments for each tool
3. Run the tools

The built-in tools can be configured to automatically upload the results to your Neo4j instance.

## Running & Viewing Queries

To get results for a chart, either use the Refresh icon to run a specific query, or use the **Query Runner** section to run queries in batches. The results will be cached even after closing BlueHound, and can be run again to get updated results.
 Some charts have an *Info* icon which explain the query and/or provide links to additional information.

## Adding & Editing Queries

You can edit the query for new and/or existing charts by using the Settings icon on the top right section of the chart. Here you can use any parameters configured with a *Param Select* chart, and any *Edge Filtering* string (see section below).

## Edge Filtering

Using the **Edge Filtering** section, you can filter out specific relationship types for all queries that use the relevant string in their query. For example, ":FILTERED\_EDGES" can be used to filter by all the selection filters.
 You can also filter by a specific category (see the *Info* icon) or even define your own custom edge filters.

## Import & Export Config

The **Export Config** and **Import Config** sections can be used to save & load your [dashboard](https://www.kitploit.com/search/label/Dashboard "dashboard") and configurations as a backup, and even shared between users to collaborate and contribute insightful queries to the security community. Don’t worry, your [credentials](https://www.kitploit.com/search/label/Credentials "credentials") and data won’t be exported.

***Note: any arguments for data import tools are also exported, so make sure you remove any secrets before sharing your configuration.***

## Settings

The Settings section allows you to set some global limits on query execution – maximum query time and a limit for returned results.

BlueHound is a fork of [NeoDash](https://github.com/neo4j-labs/neodash "NeoDash"), built with [React](https://reactjs.org/ "React") and [use-neo4j](https://github.com/adam-cowley/use-neo4j "use-neo4j"). It uses [charts](https://github.com/neo4j-labs/charts "charts") to power some of the visualizations. You can also extend NeoDash with your own visualizations. Check out the developer guide in the [project repository](https://github.com/neo4j-labs/neodash "project repository").

## Run & Build using npm

BlueHound is built with React. You'll need `npm` installed to run the web app.

> Use a recent version of `npm` and `node` to build BlueHound. The application has been tested with npm 8.3.1 & node v17.4.0.

To run the application in development mode:

* clone this repository.
* open a terminal and navigate to the directory you just cloned.
* execute `npm install` to install the necessary dependencies.
* execute `npm run dev` to run the app in development mode.
* the application should be available at [http://localhost:3000](http://localhost:3000 "http://localhost:3000").

To build the app for production:

* follow the steps above to clone the repository and install dependencies.
* execute `npm run build`. This will create a `build` folder in your project directory.
* deploy the contents of the build folder to a web server. You should then be able to run the web app.

## Questions / Suggestions

We are always open to ideas, comments, and suggestions ...