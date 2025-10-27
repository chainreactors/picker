---
title: Harnessing the Power of ChatGPT and SAP HANA Cloud for Next-level Data Analytics
url: https://blogs.sap.com/2023/01/10/harnessing-the-power-of-chatgpt-and-sap-hana-cloud-for-next-level-data-analytics/
source: SAP Blogs
date: 2023-01-11
fetch_date: 2025-10-04T03:31:45.886349
---

# Harnessing the Power of ChatGPT and SAP HANA Cloud for Next-level Data Analytics

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Technology](/t5/technology/ct-p/technology)
* [Technology Blog Posts by Members](/t5/technology-blog-posts-by-members/bg-p/technology-blog-members)
* Harnessing the Power of ChatGPT and SAP HANA Cloud...

Technology Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/technology-blog-members/article-id/162974&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Harnessing the Power of ChatGPT and SAP HANA Cloud for Next-level Data Analytics](/t5/technology-blog-posts-by-members/harnessing-the-power-of-chatgpt-and-sap-hana-cloud-for-next-level-data/ba-p/13566703)

![carlosbasto](https://avatars.profile.sap.com/a/c/idacace38f7bda335722ec7261a3326a57d35c99d1b4f82af6e9b153cf2a58e5f0_small.jpeg "carlosbasto")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[carlosbasto](https://community.sap.com/t5/user/viewprofilepage/user-id/209738)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=technology-blog-members&message.id=162974)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/technology-blog-members/article-id/162974)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13566703)

‎2023 Jan 10
10:16 PM

[26
Kudos](/t5/kudos/messagepage/board-id/technology-blog-members/message-id/162974/tab/all-users "Click here to see who gave kudos to this post.")

11,894

* SAP Managed Tags
* [SAP HANA Cloud](https://community.sap.com/t5/c-khhcw49343/SAP%2520HANA%2520Cloud/pd-p/73554900100800002881)
* [Artificial Intelligence](https://community.sap.com/t5/c-khhcw49343/Artificial%2520Intelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP Business Technology Platform](https://community.sap.com/t5/c-khhcw49343/SAP%2520Business%2520Technology%2520Platform/pd-p/73555000100700000172)

* [Artificial Intelligence

  Product Category](/t5/c-khhcw49343/Artificial%2BIntelligence/pd-p/c3c3a408-33ea-4c2a-ae6f-05461e76982d)
* [SAP HANA Cloud

  Software Product](/t5/c-khhcw49343/SAP%2BHANA%2BCloud/pd-p/73554900100800002881)
* [SAP Business Technology Platform

  Software Product](/t5/c-khhcw49343/SAP%2BBusiness%2BTechnology%2BPlatform/pd-p/73555000100700000172)

View products (3)

[ChatGPT](https://openai.com/blog/chatgpt/) is a powerful natural language processing model that is fine-tuned from the GPT-3.5 series. It was trained on an Azure AI supercomputing infrastructure to provide users with high-quality text generation and understanding capabilities.

[SAP HANA Cloud](https://www.sap.com/products/technology-platform/hana.html) is a single database as a service (DBaaS) foundation for modern applications and analytics across all enterprise data. When used in combination with ChatGPT, it's possible to get insightful queries based on ChatGPT's ability to "remember" previous conversations. However, it's important to note that ChatGPT's memory is limited and it can only reference up to about 3000 words or 4000 tokens from the current conversation.

Our objective is to use ChatGPT to directly run queries on SAP HANA Cloud in an automatic way. At the moment, there is no official API for ChatGPT, so some non-official packages are used (mainly [pyChatGPT](https://github.com/terry3041/pyChatGPT) - an unofficial Python wrapper for OpenAI's ChatGPT API). The idea is to demonstrate the potential of future integrations between ChatGPT and the [SAP Business Technology Platform (BTP)](https://www.sap.com/products/technology-platform.html), specifically the SAP HANA Cloud.

In order for ChatGPT to suggest things to us, we need to provide it with some background information. In this case, we'll present it with two table definitions that we have in SAP HANA Cloud. This way, it will have a better understanding of the data and be able to generate more accurate and relevant queries.

![](/legacyfs/online/storage/blog_attachments/2023/01/Imagem2.jpg)

Throughout this post we will explain how to relate SAP HANA Cloud and ChatGPT, but for now we will let ChatGPT explains what it "understood" from the background offered.

![](/legacyfs/online/storage/blog_attachments/2023/01/Imagem3.jpg)

Here, we are having a conversation with ChatGPT and it may not seem related to SAP HANA Cloud or python integration. However, to achieve our goal of generating queries for SAP HANA Cloud, it's more efficient to receive ChatGPT's response in python. This way, we can easily integrate it with the rest of our code and work with the data in a structured way.

![](/legacyfs/online/storage/blog_attachments/2023/01/Imagem4.jpg)

To do this, we'll use the **Chatbot** class, which allows us to interact with ChatGPT in a more convenient way. By doing this, we can create multiple instances of the **Chatbot** class, each with its own session token and API object. This way, we can easily get responses from ChatGPT in python. And If you wonder how this is done, I'll be happy to provide some code and walk you through it, step by step.

The **Chatbot** class is used to interact with a chatbot that is powered by the ChatGPT model. It allows to create multiple instances of the chatbot, each with its own session token and API object.

The class contains two main methods:

* **\_\_init\_\_(self)**: The constructor method which Initialize the bot behavior and session token by reading files and create an API object that will be used to interact with the Chatbot

* **create\_interaction(self, prompt, script=True)**: which takes prompt text and optional script flag, and use the self.api to send the message and receives the message, it will also clean the response text before returning it.

It also contain other helper method to help with token usage:

* **get\_session\_token(self, file\_name)**: to read session token from a file

```
class Chatbot:

    """

    Chatbot class contains the get_session_token and create_interaction functions as methods.

    The session_token variable is now an instance variable, and the api variable is created

    in the constructor. The create_interaction method uses self.api instead of the global

    variable api, and the get_session_token method now uses self instead of the global variable

    session_token.

    This way, you can create multiple instances of the Chatbot class, each with its own session

    token and API object.

    """

    def __init__(self):

        """

        Define chat GPT behavior as SQL Console for returning

        SQL statements only. Otherwise, some further work must

        be done before send to SAP HANA.

        """

        self.bot_behavior = self.get_session_token("behavior.txt")

        """

        Get session token obtained from cookies, check file.

        Set api from pyChatGPT package based on that token.

        """

        self.session_token = self.get_session_token("session_token.txt")

        self.api = cGPT(self.session_token)

    def get_session_token(self, file_name):

        file_path = Path(file_name)

        if not file_path.is_file():

            print("Error: {} not found".format(file_path))

            return None

        try:

            with open(file_path, "r") as file:

                session_token = file.read().strip()

        except:

            print("Error: Unable to read {}"...