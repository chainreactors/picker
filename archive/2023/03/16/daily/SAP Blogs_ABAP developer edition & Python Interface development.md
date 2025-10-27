---
title: ABAP developer edition & Python Interface development
url: https://blogs.sap.com/2023/03/15/abap-developer-edition-python-interface-development/
source: SAP Blogs
date: 2023-03-16
fetch_date: 2025-10-04T09:44:21.888114
---

# ABAP developer edition & Python Interface development

* [SAP Community](/)
* [Groups](/t5/groups/ct-p/groups)
* [Interest Groups](/t5/interest-groups/ct-p/interests)
* [Application Development and Automation](/t5/application-development-and-automation/gh-p/application-development)
* [Blog Posts](/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board)
* ABAP developer edition & Python Interface developm...

Application Development and Automation Blog Posts

Learn and share on deeper, cross technology development topics such as integration and connectivity, automation, cloud extensibility, developing at scale, and security.

All communityThis groupBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/application-developmentblog-board/article-id/47674&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

#### We have launched new [Developer forums/groups](https://community.sap.com/t5/developers/ct-p/developers) in the SAP Community. If you are here to publish developer- or SAP-technology related blog posts, please check out our new groups instead. You can find more information about the developer forums in this [What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147).

Read only

## [ABAP developer edition & Python Interface development](/t5/application-development-and-automation-blog-posts/abap-developer-edition-python-interface-development/ba-p/13571113)

![vodela](https://avatars.profile.sap.com/5/a/id5ae365f62446a03dc615b00453f06d42b398c5d0a3ce043f4c7f8f3923730994_small.jpeg "vodela")

[vodela](https://community.sap.com/t5/user/viewprofilepage/user-id/128396)

Active Participant

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=application-developmentblog-board&message.id=47674)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/application-developmentblog-board/article-id/47674)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13571113)

‎2023 Mar 15
8:12 PM

[2
Kudos](/t5/kudos/messagepage/board-id/application-developmentblog-board/message-id/47674/tab/all-users "Click here to see who gave kudos to this post.")

2,995

* SAP Managed Tags
* [ABAP Connectivity](https://community.sap.com/t5/c-khhcw49343/ABAP%2520Connectivity/pd-p/266264953119842772207986043063520)

* [ABAP Connectivity

  Programming Tool](/t5/c-khhcw49343/ABAP%2BConnectivity/pd-p/266264953119842772207986043063520)

View products (1)

Python has grown in popularity and the number of use cases has rapidly increased from Finance, big data and machine learning.   For those of us in the SAP it will be helpful to use the power of processing provided by Python at the same time retain the benefits and advantages of working in SAP.

In this blog, we will see how to use python and query odata from the ABAP developer edition using IntellJ PY Charm and show case the power of python in data analysis using a simple example  I There are many blogs that describe how to set up python and IntelliJ for development. One such blog is [Python with Intellij.](https://www.logicbig.com/tutorials/misc/python/python-with-intellij.html)

To query odata you need to install pyodata from GitHub.  This is available from [SAP Pyodata package](https://github.com/SAP/python-pyodata).  Install the library as mentioned

It is assumed that you have SAP ABAP developer edition up and running. I am using Developer edition 7.52.

Once your setup is complete you can create new Python project in Py Charm and add a python file name it appy.py.  The  following code shows how to query ABAP system odata service.

```
# Import the requirements
```

```
import pyodata

import pandas as pd

import requests
```

```
# Create a PyOData client instance

service_url = "http://vhcalnplci.dummy.nodomain:8000//sap/opu/odata/sap/EPM_REF_APPS_SHOP_SRV"

#we are querying Shopping service to analyse the review information
```

```
session = requests.Session()

session.auth = ('Developer', 'Down1oad')

#username and password for ABAP developer edition

client = pyodata.Client(service_url, session)
```

```
# Get the Products entity set and its entity type

entity_sets = client.entity_sets

products_entity_set=""

scalar_properties = set()

for es in client.schema.entity_sets:

        if es.name == "Reviews":

            proprties = es.entity_type.proprties()

            for prop in proprties:

                if prop.name == 'ProductId' or prop.name ==  'Rating' or prop.name == 'HelpfulCount':

                    scalar_properties.add(prop.name)

print(scalar_properties)

reviews = client.entity_sets.Reviews.get_entities().execute()

# Create an empty list to store the dictionaries for each reviews

review_list = []

# Loop through each review entity and create a dictionary

for review in reviews:

    review_dict = {}

    for property_name in scalar_properties:

        review_dict[property_name] = getattr(review, property_name)

    review_list.append(review_dict)

# Convert the list of dictionaries to a pandas DataFrame

df = pd.DataFrame(review_list)

df=df.sort_index()

df2= df.groupby('ProductId').sum()

print(df2)
```

When you run the program you the output shown below

![](/legacyfs/online/storage/blog_attachments/2023/03/Screenshot-2023-03-13-111533.png)

The above output shows the power of python for data analysis using a simple example. If we had to write an ABAP to do the same we would have to loop thru the output and sum reviews by product.

It will help if readers can comment and provide feedback and suggestions for future blogs.  If you are interested in ABAP connectivity please follow the ABAP Connectivity environment topic page (<https://community.sap.com/topics/abap-connectivity>),  Post and answer questions (<https://answers.sap.com/tags/266264953119842772207986043063520>), and read other posts on the topic (<https://blogs.sap.com/tags/266264953119842772207986043063520/>)

* [pyodata](/t5/tag/pyodata/tg-p/board-id/application-developmentblog-board)
* [Python](/t5/tag/Python/tg-p/board-id/application-developmentblog-board)

2 Comments

Copy Link
![](https://community.sap.com/html/@EE5D5986E9F4E5657DCEACB7532B5C39/assets/bluesky-dark.svg)Bluesky
Linkedin