---
title: Introducing httpXplorer: Simplifying httpX URL Management and Analysis
url: https://buaq.net/go-171188.html
source: unSafe.sh - 不安全
date: 2023-07-05
fetch_date: 2025-10-04T11:52:28.334663
---

# Introducing httpXplorer: Simplifying httpX URL Management and Analysis

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

Introducing httpXplorer: Simplifying httpX URL Management and Analysis

httpXplorer is a web-based application specifically designed for efficient URL management and analys
*2023-7-4 18:6:57
Author: [infosecwriteups.com(查看原文)](/jump-171188.htm)
阅读量:18
收藏*

---

## httpXplorer is a web-based application specifically designed for efficient URL management and analysis of the projectdiscovery’s httpx tools results. It allows users upload the httpx JSON output file, analyze URLs, status codes, web technologies, other information, sort the URLs based on their status codes, and focus on specific subdomains.

[![Abid Ahmad](https://miro.medium.com/v2/resize:fill:88:88/0*mZiUKB4QD9A80ESl.jpg)](https://rootintrud3r.medium.com/?source=post_page-----56cfd7527bff--------------------------------)[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:48:48/1*A6LVtmXcJ3QJy_sdCyFx1Q.png)](https://infosecwriteups.com/?source=post_page-----56cfd7527bff--------------------------------)

httpXplorer — httpX Local Database

Hey there! I’m excited to introduce you to httpXplorer, a powerful web-based application designed to streamline URL management and analysis. httpXplorer is here to make your life easier. In this article, I’ll walk you through an overview of the application, its key features, how to use it, the benefits it offers, and the technologies used in its development.

**Overview:**

Whether you’re a penetration tester or bug hunter, httpXplorer provides valuable insights into your target URLs, helping you identify potential issues and optimize your workflow. The user-friendly interface and intuitive features of httpXplorer enable seamless organization, sorting, and extraction of information from your URL data. Whether you have a large collection of URLs or need to make informed decisions based on the data, httpXplorer simplifies the process and enhances your productivity and you’ll get comprehensive understanding of your target.

With httpXplorer, you have a centralized platform to manage and analyze your URL data, saving you time and effort. The application’s powerful features and intuitive interface make it easy for both beginners and experienced professionals to navigate and extract valuable insights from their URL datasets. Whether you are performing security assessments, bug hunting, or optimizing web applications, httpXplorer is your go-to tool for efficient URL management and analysis.

## **Key Features:**

***1. Upload and Analysis:*** Easily upload httpx JSON output files containing URLs and perform comprehensive analysis on their status codes, web technologies, and other relevant information.

***2. URL Sorting:*** Sort the URLs based on their status codes in ascending or descending order.

***3. Filtering Copy URLs:*** Filter and copy a range of URLs by specifying the start and end index, making it convenient to share or export specific sets of URLs.

***3. Intuitive User Interface:*** Enjoy a user-friendly interface that enables smooth navigation, making it effortless to explore and interact with your URL data.

***4. Efficient Data Management:*** Benefit from a well-organized centralized database system that ensures optimal performance and reliability in handling large volumes of data.

***5. Flexible Configuration:*** Customize the application’s database name and adapt it to your specific target domain and requirements.

***6. Data Update:*** Easily update the latest data of the target. When upload latest json file, if any data (status codes, technologies, CDN names, and hosts) changes in the latest output file, the new data will be updated by replacing old data

## How to Use [httpXplorer](https://github.com/Abid-Ahmad/httpXplorer):

1. Install and Launch httpXplorer by following the instructions in the [README file](https://github.com/Abid-Ahmad/httpXplorer/blob/main/README.md) on the [project’s GitHub repository](https://github.com/Abid-Ahmad/httpXplorer).

2. Upload your httpx JSON output file containing the URLs you want to analyze. Before uploading the JSON file, make sure JSON format is valid. By default. httpx output JSON format is not valid because of missing starting and closing brackets.

So, first fix the JSON file via [JSON Fixer](https://codebeautify.org/json-fixer), then upload the fixed JSON file in the httpXplorer.

Upload fixed JSON file

3. Explore the comprehensive analysis results, including status codes, web technologies, and other relevant information.

4. Utilize the sorting options to prioritize specific URLs based on their status codes in ascending or descending order.

Sorting URLs/subdomains based on status codes in asc or desc order

4. Filter & Copy URLs based on the index number. In the below example, first I sorted URLs in descending order, found index 1–6 URLs/subdomains are 404. I wanted to copy those 6 URLs, input number in Start Index & End Index then Copy those URLs.

Sorting desc to visualize 404 subdomains, then copy specific ranges of URLs

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

All databases based on specific target

You can find all the databases in the **“instance”** folder of the application.

> By default, the application only display STATUS CODE, URL, TECHNOLOGY, CDN, HOST.

## If you want to remove any column or include other information, just change a little bit inside the “app.py” code. If you read the code carefully, you will understand how you can modify for your specific purpose

```
# HERE IS THE EXAMPLE

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    status_code = db.Column(db.Integer)
    tech = db.Column(db.String(200))
    cdn_name = db.Column(db.String(200))
    host = db.Column(db.String(200))

....

def __init__(self, url, status_code, tech, cdn_name, host):
        self.url = url
        self.status_code = status_code
        self.tech = tech
        self.cdn_name = cdn_name
        self.host = host

....

with app.app_context():
            for entry in data:
                url = entry.get('url', 'NULL')
                status_code = entry.get('status_code', 0)
                tech = entry.get('tech', 'NULL')
                cdn_name = entry.get('cdn_name', 'NULL')
                host = entry.get('host', 'NULL')

....

if existing_data:
                    existing_data.status_code = status_code
                    existing_data.tech = tech
                    existing_data.cdn_name = cdn_name
                    existing_data.host = host
                else:
                    new_data = Data(url=url, status_code=status_code, tech=tech, cdn_name=cdn_name, host=host)
                    db.session.add(new_data)

....
```

## **Technologies Used:**

httpXplorer leverages a range of technologies to deliver its powerful features:

* **Front-end:** As the front-end of the httpXplorer application, I have created an intuitive and user-friendly web interface using HTML, CSS, and JavaScript. The front-end is responsible for presenting the web pages to the users and handling user interactions. In this system, the front-end primarily consists of the ***‘index...