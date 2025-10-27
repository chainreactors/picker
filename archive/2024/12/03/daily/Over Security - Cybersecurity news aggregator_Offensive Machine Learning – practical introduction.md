---
title: Offensive Machine Learning – practical introduction
url: https://www.hacktivesecurity.com/index.php/2024/01/16/offensive-machine-learning-practical-introduction/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-03
fetch_date: 2025-10-06T19:41:16.670833
---

# Offensive Machine Learning – practical introduction

* info@hacktivesecurity.com
* Mon - Fri: 9.00 am - 6.00 pm

Advanced Security Solutions to protect the Cyberspace.

[Twitter](https://x.com/hacktivesec)

[Facebook-f](https://www.facebook.com/hacktivesec)

[Linkedin-in](https://www.linkedin.com/company/hacktive-security/)

[Instagram](https://www.instagram.com/hacktivesec/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

Search for:

### Have Any Questions?

+39-06-8773-8747

[free quote](https://www.hacktivesecurity.com/index.php/contacts/)

[![Hacktive Security](https://www.hacktivesecurity.com/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Search for:

* [Home](https://www.hacktivesecurity.com/)
* [About Us](https://www.hacktivesecurity.com/about-us/)
* Services
  + [Penetration Testing](https://www.hacktivesecurity.com/penetration-testing/)
  + [Red Teaming](https://www.hacktivesecurity.com/red-teaming/)
  + [Secure Code Review](https://www.hacktivesecurity.com/secure-code-review/)
  + [Training](https://www.hacktivesecurity.com/training/)
  + [Compliance](https://www.hacktivesecurity.com/compliance/)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [Careers](https://www.hacktivesecurity.com/careers/)
* [Contacts](https://www.hacktivesecurity.com/contacts/)

[![Hacktive Security](http://176.31.202.211/wp-content/uploads/2024/10/logo_hs-1.png)](https://www.hacktivesecurity.com/)

Over 10 years we help companies reach their financial and branding goals. Engitech is a values-driven technology agency dedicated.

#### Gallery

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project11.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project10.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project4.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project6.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project2.jpg)

[![](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1-720x720.jpg)](https://www.hacktivesecurity.com/wp-content/uploads/2019/11/project1.jpg)

#### Contacts

Via Giosuè Carducci, 21 - Pomigliano d'Arco (Italy)
Paseo Montjuic, número 30 - Barcelona (Spain)

info@hacktivesecurity.com

+39 06 8773 8747

[Twitter](#hacktivesec)

Facebook-f

Pinterest-p

Instagram

# Hacktive Blog

* [Home](https://www.hacktivesecurity.com)
* [Blog](https://www.hacktivesecurity.com/blog/)
* [AI](https://www.hacktivesecurity.com/blog/category/ai/)
* Offensive Machine Learning – practical introduction

[AI](https://www.hacktivesecurity.com/blog/category/ai/) [Red Teaming](https://www.hacktivesecurity.com/blog/category/red-teaming/)

\_ [January 16, 2024](https://www.hacktivesecurity.com/blog/2024/01/16/offensive-machine-learning-practical-introduction/)\_ [Riccardo Degli Esposti](https://www.hacktivesecurity.com/blog/author/rdegliesposti/)\_ [0 Comments](https://www.hacktivesecurity.com/blog/2024/01/16/offensive-machine-learning-practical-introduction/#respond)

### Offensive Machine Learning – practical introduction

## Disclaimer

*This article is intended to be an introduction to machine learning applied to cybersecurity that is understandable even to those who approach it without a prior knowledge of the subject.*

*In order to show weaknesses not all best practices will be followed and some logical errors will be voluntarily included, including code.* *Therefore, the invitation is to read, learn more about the topic without blindly replicating the vulnerable code or practices.*

*This little research aims through the invention of a likely but simplified scenario to show how machine learning can assist cybersecurity. It is not a comprehensive guide or a step by step tutorial but an introduction to an advanced topic.* *The idea to write a few words on the topic stems from the lack of beginner-friendly practical examples available to anyone who would like to try to approach the topic.*

*All resources used to follow are open source, and the code used will be reported and commented on as we go along to allow the reader to try it out for themselves.*

**Any reference to actual events and/or real people is to be considered purely coincidental.**

## The Scenario

One day a bank named **TriDebit** hears about a new technology that is permeating every industry called **Artificial Intelligence (AI)** and decides to start a project to detect and block the most popular attacks on its web applications. Within TriDebit, however, there is no team specializing in this field, so they decide to inquire and analyze the problem of getting the project off the ground.

The history of artificial intelligence begins in 1955, a time when the term was first used even though earlier work aimed at a *‘learning machine’* had already been developed. Seventy years have passed since then, and the concept of artificial intelligence has expanded and specialized in different branches thanks to the work of researchers, universities and companies that have pursued the research.

The most famous fields nowadays are:

* **Machine Learning (ML):** This is the core of AI, where machines learn from data to make **decisions or predictions**.
* **Deep Learning (DL):** A subset of machine learning, deep learning uses neural networks with many layers (hence “deep”) to analyze various factors in large volumes of data. It’s the technology behind many advanced AI functions, such as speech recognition, image recognition, and natural language processing.
* **Natural Language Processing (NLP)**: This field focuses on the interaction between computers and human languages. It involves the development of algorithms that can understand, interpret, and respond to human languages.
* **Computer Vision**: This field enables machines to interpret and process visual data from the world, similar to human vision. It has applications in image recognition, video analysis, and autonomous vehicles.

There are many additional branches and each of them contains within it techniques and more precise subdivisions to address each field accurately. But this is outside the scope of this research.

For TriDebit, in fact, it is enough to be able to replicate a fairly simple cognitive process: receive, understand, identify, and decide. What the above descriptions suggest a Machine Learning model can do. Their project – and our research – can be described using the following schema:

![](http://176.31.202.211/wp-content/uploads/2024/01/schema1.png)

The model is used to identify and accept or reject incoming requests by analyze them as threats or harmless objects.

## Machine Learning

**Machine learning** is a subset of AI that provides systems the ability to automatically learn from experience without being explicitly programmed with fixed set of rules.

The learning process begins with observations or data, such as exa...