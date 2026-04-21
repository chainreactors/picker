---
title: A nice approach to AWS security group management
url: https://blog.sicuranext.com/a-nice-approach-to-aws-security-group-organization/
source: Over Security - Cybersecurity news aggregator
date: 2026-04-20
fetch_date: 2026-04-21T04:51:21.871450
---

# A nice approach to AWS security group management

[![Sicuranext Blog](https://blog.sicuranext.com/content/images/2026/03/sicuranext_h-accent-2.png)](https://blog.sicuranext.com)

* [Home](https://blog.sicuranext.com/)
* [WAAP](https://blog.sicuranext.com/tag/waap/)
* [SOC](https://blog.sicuranext.com/tag/soc/)
* [PWNPress](https://blog.sicuranext.com/tag/pwnpress/)
* [AI](https://blog.sicuranext.com/tag/ai/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

# A nice approach to AWS security group management

* [![Federico Zota](/content/images/size/w100/2026/04/iadrabbit-6.jpg)](/author/federico/)

#### [Federico Zota](/author/federico/)

20 Apr 2026
• 5 min read

![A nice approach to AWS security group management](/content/images/size/w2000/2026/04/aws2.png)

## AWS Glossary for the novices

Hi, before diving a bit more in the details of this article, is mandatory to explain some core components in the AWS ecosystem we are gonna cite during this post, so even for novice and unfamiliar people can understand better the concepts.

* EC2: stands for Elastic Compute your virtual machine located in some region in the world (do not ask me the 2 in EC2 what means)
* Security Group: aka SG, a logical resource that acts as a virtual firewall you can put in front of AWS resources
* ECS: The Kubernetes/docker swarm AWS Homemade, the orchestrator of your docker containers
* Autoscaling Group: an AWS resource that describes what type and configuration you want your EC2.
* VPC: Virtual Private Cloud, this how a private network sitting in the cloud is called
* RDS: The AWS service for creating db instances like a postgres one
* RDS Proxy: It helps to manager the connection pool to your RDS db instances
* Elasticache: The same for RDS, but for key-value in memory database like redis
* Lambda: they are serverless function, like executing a script without taking care to place them on a machine.

## The problem

Our core infrastructure is based on containers running inside EC2 managed through ECS by using capacity providers associated with Autoscaling groups. For how we manage things internally our EC2 instances are ephemeral so the internal ip inside the subnet changes frequently. So how can we set boundaries between hosts inside the same VPC? for example the db on RDS should be reachable only by a certain ECS service, the redis on Elasticache should be available only by a certain worker.

The answer is obviously security group, the difference is in the approach you choose to configure. You could just attach a security group to your db instance with a rule that makes it reachable by all hosts inside the VPC so you avoid the headache of gathering all the IPs that need to talk to the db, a bit ugly in my opinion and very insecure considering the fact that following this pattern a single compromised host can be use to scan the network identifying other hosts. But luckily there is another way to create security group rules than just specify the source or the destination ip or CIDR, we can also set both inbound and outbound rules a reference to another security group.

## How this work

If the question before was. “What IPs need to talk with the db?” Now the question is “What security group can reach the DB?”. We are switching from an approach where every EC2, lambda etc. should have their own custom security group with its own rules to an approach of “I probably already have the security group that can reach the DB.” So in the end we will have to manage a set of security groups  that doesn’t increase depending on how many hosts I have inside my VPC, but the “kind” of services needed to talk between them.

## Let get practical

Let’s suppose we have the following scenario

![](https://blog.sicuranext.com/content/images/2026/03/data-src-image-ff0ed904-d91e-42ff-b705-5313a5fe0b43.png)

We got:

* An ecs service
* A lambda
* An EC2
* And the RDS proxy for managing the Pool for the RDS
* A RDS db itself

Creating ingress rules for the security group attached to the RDS proxy or the RDS for every ip, considering also lambda are spawned on trigger so their ip change frequently is impossible without allowing the entire CIDR subnet in the rule. With security group referencing we just need two distinct security groups. And to help understand things better it is important to answer the following questions.

Who is the data source & Who needs that data. So we got:

* **db**
* **db\_connect**

With these rules (obviously the id have been redacted)

![](https://blog.sicuranext.com/content/images/2026/03/data-src-image-2ce5b287-9a0a-4488-be4b-de9275547e83.png)

You can observe that the only rule for the security group that is gonna be attached to our RDS instance (the data source) is to accept traffic from resources that have attached the security group **db\_connect**.

Now let see the inbound & outbound rules for **db\_connect** security group

![](https://blog.sicuranext.com/content/images/2026/03/data-src-image-fe636535-9add-4566-8c9b-68f4c2e551f9.png)![](https://blog.sicuranext.com/content/images/2026/03/data-src-image-155dd924-f9db-4644-b08a-c0f2dd390d23.png)

When I first discovered this I was a bit confused & surprised that inside a security group rule I could reference the same security group for which it is the rule for. It makes sense, it just means that a resource who is associated with that security group can establish a connection with another resource which also has the same security group attached. And in a scenario where we have a rds proxy in the middle this setup works finely. Just to be clearer as possible.

Ecs service > RDS Proxy > RDS Instance

The ecs service can talk to the rds proxy because the security group **db\_connect** assigned has an outbound security group rule that can reach other resources that has the **db\_connect** security group attached, like our RDS proxy, this security group has an inbound rule that also accepts traffic from resources who has this security group attached. In the end the RDS proxy can connect to the db because the security group has an outbound rule to reach resources that have associated the **db** security group like our RDS instance where the **db** security group accept this because he has the inbound rule to accept traffic from resources which has the **db\_connect** security group attached.

KEEP IN MIND, that this could also open unexpected “ways” to services that maybe you don’t like to talk between them. In the scenario described above due the self-referential nature of the **db\_connect** security group rules, every resource which has this security group attached can establish a connection, anyway as is it would be just on port 5432 and is abnormal, but not impossible, to have a resource exposed running on port 5432 (which is the default port for postgres db) that also needs to connect to a db, but can be useful if you want to create a "virtual network" on top of your actual subnet exclusive for some instances. Maybe now you are wondering why doing this with security group auto referencing instead of specify the entire subnet or VPC CIDR as security group rule? In my opinion managing a dedicated subnet just for establish connection between different hosts is an overhead, especially if you are in a situation where you cannot create new subnets or you already have a redis instance that is isolated to a specific subnet, but your machines needs to talk with that redis. It is more simple to create a security group and using it as logical network delimiter instead of taking care to trace all of your infrastructure CIDR, better one more security group than one more subnet.

## Conclusions

To adopt this paradigma it needs to be clear who is the server and who are the clients. One security group to be **only** attached to the server, in example above our RDS instance with the **db** security group, and the other security group,**db\_connect,** to be attached to all the clients who need to talk with the server. This keeps security groups simple, which in general I ex...