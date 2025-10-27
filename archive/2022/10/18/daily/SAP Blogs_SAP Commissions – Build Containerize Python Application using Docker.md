---
title: SAP Commissions – Build Containerize Python Application using Docker
url: https://blogs.sap.com/2022/10/17/sap-commissions-build-containerize-python-application-using-docker/
source: SAP Blogs
date: 2022-10-18
fetch_date: 2025-10-03T20:06:55.851711
---

# SAP Commissions – Build Containerize Python Application using Docker

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Human Capital Management](/t5/human-capital-management/ct-p/hcm)
* [HCM Blog Posts by SAP](/t5/human-capital-management-blog-posts-by-sap/bg-p/hcm-blog-sap)
* SAP Commissions - Build Containerize Python Applic...

Human Capital Management Blog Posts by SAP

Learn directly from SAP experts through blogs that deliver practical guidance and opportunities to deepen your expertise.

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/hcm-blog-sap/article-id/5486&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [SAP Commissions - Build Containerize Python Application using Docker📦](/t5/human-capital-management-blog-posts-by-sap/sap-commissions-build-containerize-python-application-using-docker/ba-p/13545307)

![Yogananda](https://avatars.profile.sap.com/5/9/id59e1da3a3dca34a1bd12f9d987d3cdb668e528e343194e20fc715b0bc28cc49b_small.jpeg "Yogananda")

![Product and Topic Expert](/html/@138D6F765B60D7FC0168643DE27D8A68/rank_icons/sap-logo-small-14px.png "Product and Topic Expert")
[Yogananda](https://community.sap.com/t5/user/viewprofilepage/user-id/75)

Product and Topic Expert

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=hcm-blog-sap&message.id=5486)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/hcm-blog-sap/article-id/5486)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13545307)

‎2022 Oct 17
9:49 PM

[1
Kudo](/t5/kudos/messagepage/board-id/hcm-blog-sap/message-id/5486/tab/all-users "Click here to see who gave kudos to this post.")

1,494

* SAP Managed Tags
* [Python](https://community.sap.com/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [SAP BTP, Cloud Foundry runtime and environment](https://community.sap.com/t5/c-khhcw49343/SAP%2520BTP%252C%2520Cloud%2520Foundry%2520runtime%2520and%2520environment/pd-p/73555000100800000287)
* [SAP SuccessFactors Incentive Management](https://community.sap.com/t5/c-khhcw49343/SAP%2520SuccessFactors%2520Incentive%2520Management/pd-p/73555000100800001602)

* [Python

  Programming Tool](/t5/c-khhcw49343/Python/pd-p/f220d74d-56e2-487e-8e6c-a8cb3def2378)
* [SAP BTP, Cloud Foundry runtime and environment

  SAP Business Technology Platform](/t5/c-khhcw49343/SAP%2BBTP%25252C%2BCloud%2BFoundry%2Bruntime%2Band%2Benvironment/pd-p/73555000100800000287)
* [SAP SuccessFactors Incentive Management

  SAP SuccessFactors HCM](/t5/c-khhcw49343/SAP%2BSuccessFactors%2BIncentive%2BManagement/pd-p/73555000100800001602)

View products (3)

This article provides the basics of docker and learn how to build an image that runs a Python application in a container. I will show you **how to build a custom application for Sales reps - SAP Commissions.**

Customers/Developers in your org can build your own custom Application to help Sales reps to see what they need to maximize the sales...  you can build this all through the data coming from Rest APIs.. ![](/legacyfs/online/storage/blog_attachments/2022/10/EYoULfKVcAUx0N1.jpg)

### **What is Docker?**

It is a platform for developing, shipping, and running applications. In simple terms, you can build your application, package them along with their dependencies into a container, and then these containers can be shipped to run on other machines.

Key Terminologies

+ ***Dockerfile***- A text file that consists of instructions and arguments. It informs Docker how the image should get built.

+ ***Image-*** It is a read-only template with instructions for creating a container. Each instruction in a Dockerfile creates a layer in the image.

+ ***Container-*** It is a running instance of an image. It is well defined by its image as well as any configuration options provided to it create or start.

![](https://miro.medium.com/max/461/1*9Sr6pbs5yr8i0PvATJGEzA.png)
The above diagram shows multiple running instances (container) of the same image (template) which was created or built using a Dockerfile.

The most commonly used Dockerfile instructions are :

![](https://miro.medium.com/max/647/1*jfgZoX_jF8GQi2SkXxkaww.png)

## Docker Commands

The most commonly used docker commands are :

![](https://miro.medium.com/max/651/1*o-vPlHRcm6DbIeskGd4RUA.png)

                               *Commonly used docker commands*

## Get Started to build sample SAP Commissions Application

We will create a simple project to containerize a Python application by following the steps mentioned below :

+ Create a simple static web application using flask

+ Create a Dockerfile

+ Build image out of Dockerfile

+ Run the image in the container

+ Push the image to Docker Hub

+ Deploy the application to **SAP BTP**

## Installation

+ Download the [Docker](https://docs.docker.com/get-docker/) (requires a **paid** subscription.) or you can choose Rancher Desktop or Podman

+ Install the pip library required to build for your application

## Code

## **app.py**

```
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0')
```

**requirements.txt**

```
flask

requests

json

pandas
```

**Dockerfile**

```
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python","app.py"]
```

## Run

Open terminal and navigate to the project .

+ Build an image out of Dockerfile by running the following command below. Pass in the -t parameter to name the image .

```
docker build -t sample .
```

To verify the image built use the following command

```
docker images
```

Run the docker container . The -p flag maps a port running inside the container to your host. The — — name is used to give name to the container and sample is image name which was built earlier .

```
docker run --name flask_app  -p 8000:5000 sample
```

Open the browser and type to see your application running locally to see the preview

```
http:://127.0.0.1:8000/
```

![](/legacyfs/online/storage/blog_attachments/2022/10/2022-10-17_22-17-15.png)

*Above is the custom application developed in this example for Sales reps to show in One Page about the Sales Performance and how the Sales transactions are in his geography to identify the potential sales area.*

### Login to your Docker Hub to push your image

```
docker login -u <username>

docker build -t <username>/image-name .

docker push <username>/image-name:latest

docker run <username>/image-name
```

---

## Push Docker Image to SAP BTP

Now the image is ready in the docker hub, let’s push this docker image to SAP BTP.

*Here I assume that you have your SAP BTP Trial or Global account ready and Cloud Foundry Command Line Interface (CLI) installed on your desktop.*

<https://account.hanatrial.ondemand.com/>

**Step1:** Let’s login to your SAP BTP Cloud Foundry endpoint using CLI. Run:

```
cf login --sso
```

**Step2**: Push the docker image to SAP Cloud Foundry.

```
cf push custom-application --docker-image <username>/image-name --docker-username <username>
```

Example for the command line syntax

```
cf push <App Name> –docker-image <Docker Image Repository:TagName> –docker- username <docker username>
```

## End Result![](/legacyfs/online/storage/blog_attachments/2022/10/FehxQP0VsAI-veq.png)

Now, you have pretty much an Idea of building your own Application by consuming the data...