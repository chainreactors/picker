---
title: Introducing httpXplorer: Simplifying httpX URL Management and Analysis
url: https://infosecwriteups.com/introducing-httpxplorer-simplifying-httpx-url-management-and-analysis-56cfd7527bff?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-07-05
fetch_date: 2025-10-04T11:53:44.588621
---

# Introducing httpXplorer: Simplifying httpX URL Management and Analysis

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F56cfd7527bff&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fabid10.medium.com%2Fintroducing-httpxplorer-simplifying-httpx-url-management-and-analysis-56cfd7527bff&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fabid10.medium.com%2Fintroducing-httpxplorer-simplifying-httpx-url-management-and-analysis-56cfd7527bff&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# Introducing httpXplorer: Simplifying httpX URL Management and Analysis

## httpXplorer is a web-based application specifically designed for efficient URL management and analysis of the projectdiscovery’s httpx tools results. It allows users upload the httpx JSON output file, analyze URLs, status codes, web technologies, other information, sort the URLs based on their status codes, and focus on specific subdomains.

[![Abid Ahmad](https://miro.medium.com/v2/resize:fill:64:64/1*Cux8YIS6GfSdpgwTxgTZMg.jpeg)](/?source=post_page---byline--56cfd7527bff---------------------------------------)

[Abid Ahmad](/?source=post_page---byline--56cfd7527bff---------------------------------------)

7 min read

·

Jun 26, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

httpXplorer — httpX Local Database

Hey there! I’m excited to introduce you to [httpXplorer](https://github.com/MrNeoTr1n0/httpXplorer), a powerful web-based application designed to streamline URL management and analysis. httpXplorer is here to make your life easier. In this article, I’ll walk you through an overview of the application, its key features, how to use it, the benefits it offers, and the technologies used in its development.

**Overview:**
httpXplorer is a web-based application designed for managing and analyzing URLs obtained from projectdiscovery’s httpx tools. It enables users to upload httpx JSON output files, analyze status codes, web technologies, and explore related information. The application provides sorting functionality for URLs based on their status codes, allowing users to prioritize and focus on specific areas of interest.

Whether you’re a penetration tester or bug hunter, httpXplorer provides valuable insights into your target URLs, helping you identify potential issues and optimize your workflow. The user-friendly interface and intuitive features of httpXplorer enable seamless organization, sorting, and extraction of information from your URL data. Whether you have a large collection of URLs or need to make informed decisions based on the data, httpXplorer simplifies the process and enhances your productivity and you’ll get comprehensive understanding of your target.

With httpXplorer, you have a centralized platform to manage and analyze your URL data, saving you time and effort. The application’s powerful features and intuitive interface make it easy for both beginners and experienced professionals to navigate and extract valuable insights from their URL datasets. Whether you are performing security assessments, bug hunting, or optimizing web applications, httpXplorer is your go-to tool for efficient URL management and analysis.

### **Key Features:**

***1. Upload and Analysis:*** Easily upload httpx JSON output files containing URLs and perform comprehensive analysis on their status codes, web technologies, and other relevant information.

***2. URL Sorting:*** Sort the URLs based on their status codes in ascending or descending order.

***3. Filtering Copy URLs:*** Filter and copy a range of URLs by specifying the start and end index, making it convenient to share or export specific sets of URLs.

***3. Intuitive User Interface:*** Enjoy a user-friendly interface that enables smooth navigation, making it effortless to explore and interact with your URL data.

***4. Efficient Data Management:*** Benefit from a well-organized centralized database system that ensures optimal performance and reliability in handling large volumes of data.

***5. Flexible Configuration:*** Customize the application’s database name and adapt it to your specific target domain and requirements.

***6. Data Update:*** Easily update the latest data of the target. When upload latest json file, if any data (status codes, technologies, CDN names, and hosts) changes in the latest output file, the new data will be updated by replacing old data

### How to Use [httpXplorer](https://github.com/MrNeoTr1n0/httpXplorer):

1. Install and Launch httpXplorer by following the instructions in the README file on the [project’s GitHub repository](https://github.com/MrNeoTr1n0/httpXplorer).

2. Upload your httpx JSON output file containing the URLs you want to analyze. Before uploading the JSON file, make sure JSON format is valid. By default. httpx output JSON format is not valid because of missing starting and closing brackets.

So, first fix the JSON file via [JSON Fixer](https://codebeautify.org/json-fixer), then upload the fixed JSON file in the httpXplorer.

Press enter or click to view image in full size

![]()

Upload fixed JSON file

3. Explore the comprehensive analysis results, including status codes, web technologies, and other relevant information.

Utilize the sorting options to prioritize specific URLs based on their status codes in ascending or descending order.

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Sorting URLs/subdomains based on status codes in asc or desc order

4. Filter & Copy URLs based on the index number. In the below example, first I sorted URLs in descending order, found index 1–6 URLs/subdomains are 404. I wanted to copy those 6 URLs, input number in Start Index & End Index then Copy those URLs.

Press enter or click to view image in full size

![]()

Sorting asc/desc to visualize subdomains, then copy specific ranges of URLs

Press enter or click to view image in full size

![]()

Export or paste copied URLs in a file

5. If user upload another JSON output file, the unique data will be stored accordingly. If any previous record changed, database will be updated based on new data by replacing old data record.

6. User can separe DATABASE based on the Target. Just change the database name (tesla.db) in the **‘SQLALCHEMY\_DATABASE\_URI’.**

```
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tesla.db'
db = SQLAlchemy(app)

# OR,

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yahoo.db'

# LIKE THIS
```

Press enter or click to view image in full size

![]()

All databases based on specific target

You can find all the databases in the **“instance”** folder of the application.

## System Architecture

> By default, the application only display STATUS CODE, URL, TECHNOLOGY, CDN, HOST.

### If you want to remove any column or include other information, just change a little bit inside the “app.py” code. If you read the code carefully, you will understand how you can modify for your specific purpose

```
# HERE IS THE EXAMPLE

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
  ...