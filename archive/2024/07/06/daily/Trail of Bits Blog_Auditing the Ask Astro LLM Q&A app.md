---
title: Auditing the Ask Astro LLM Q&A app
url: https://blog.trailofbits.com/2024/07/05/auditing-the-ask-astro-llm-qa-app/
source: Trail of Bits Blog
date: 2024-07-06
fetch_date: 2025-10-06T17:42:42.806558
---

# Auditing the Ask Astro LLM Q&A app

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Auditing the Ask Astro LLM Q&A app

Trail of Bits

July 05, 2024

[machine-learning](/categories/machine-learning/), [open-source](/categories/open-source/)

Today, we present the second of our open-source AI security audits: a look at security issues we found in an open-source retrieval augmented generation (RAG) application that could lead to chatbot output poisoning, inaccurate document ingestion, and potential denial of service. This audit follows up on our previous work that identified [11 security vulnerabilities in YOLOv7](https://blog.trailofbits.com/2023/11/15/assessing-the-security-posture-of-a-widely-used-vision-model-yolov7/), a popular computer vision framework.

Specifically, we found four issues in [Ask Astro](https://github.com/astronomer/ask-astro), a retrieval augmented generation (RAG) open-source chatbot application modeled after Venture Capital firm A16Z’s [reference architecture for RAG applications](https://a16z.com/emerging-architectures-for-llm-applications/). RAG is one of the most effective techniques for enhancing a large language model (LLM) with information not contained in its training data set using a context knowledge base.

In this blog post, we review the RAG architecture as deployed in Ask Astro and then dive deeply into our technical findings, which can be classified along two high-level streams:

* Architectural issues: [Lack of manual moderation or document deletion capability allows attackers to poison the chatbot’s output](https://docs.google.com/document/d/1cfbpGsWfp2kv0Q8H2NhCtfbQMRGU0dGnXCOsRiNaL_U/edit#heading=h.4pcij4py78kz) with harmful information, echoing recent academic literature, most notably [Carlini et al. (2023)](https://arxiv.org/pdf/2302.10149.pdf).
* Implementation faults: multiple implementation bugs could compromise the accuracy of document ingestion ([Split-view poisoning through GitHub Issues](https://docs.google.com/document/d/1cfbpGsWfp2kv0Q8H2NhCtfbQMRGU0dGnXCOsRiNaL_U/edit#heading=h.i1kyuhewvjj), [GraphQL injection in Weavite client](https://docs.google.com/document/d/1cfbpGsWfp2kv0Q8H2NhCtfbQMRGU0dGnXCOsRiNaL_U/edit#heading=h.fxej4rfib0hd)) or threaten financial denial of service ([prompt injection in question expansion prompt](https://docs.google.com/document/d/1cfbpGsWfp2kv0Q8H2NhCtfbQMRGU0dGnXCOsRiNaL_U/edit#heading=h.k0mm2m9qftbk)).

To conclude, we provide several best practices that can help RAG deployments avoid issues like these. If your project could use a similar checkup, please [contact us](https://www.trailofbits.com/contact/).

### About Ask Astro

[Ask Astro](https://github.com/astronomer/ask-astro) is an open-source chatbot that provides technical support for Astronomer, an orchestration tool for Apache Airflow workflows. It is fully automated and requires no administration or management after deployment.

There are two primary reasons why Ask Astro was a good candidate for this type of audit. First, the project is actively maintained and has a high-quality codebase and sophisticated design that demonstrates what developers can achieve using a modern ML development stack. Considerable effort has also been undertaken to create clear documentation and write automated tests.

Second, the project’s primary purpose is as a community education tool. It is structured and documented as a RAG reference implementation and advertises its adherence to [A16Z’s reference architecture for RAG applications](https://a16z.com/emerging-architectures-for-llm-applications/). Moreover, its implementation uses a representative sample of popular tools for constructing RAG applications:

* [Weaviate](https://weaviate.io/), a vector database that stores document embeddings;
* [Langchain](https://www.langchain.com/), a Python-based framework for LLM programming; and
* [Apache Airflow](https://airflow.apache.org/), a workflow orchestration system used in Ask Astro to manage document retrieval and processing.

Ask Astro will likely be a starting point for many new RAG developers. Thus, many other RAG applications will likely follow a similar design and encounter the same challenges as Ask Astro.

The application has a relatively narrow attack surface. It comprises the two main workflows diagrammed in Figure 1: document ingestion and generating responses to user questions.

![](/img/wpdump/c78e78e2afbe040c93bc26f92493d61f.png)

Figure 1: Ask Astro data flow diagram

#### Document ingestion

Ask Astro uses a series of Apache Airflow workflows triggered through Astronomer to ingest documents from the following sources:

* Official documentation for Apache Airflow, the Astronomer CLI, the Astronomer Cosmos, and the Astronomer SDK
* The official Astronomer blog
* Python source code for contributions to the Astronomer Registry, which contains user-submitted workflow components for Astronomer and Airflow
* Documentation in two GitHub repositories from the OpenLineage project
* GitHub issues for the Apache Airflow repository
* StackOverflow threads with the `airflow` tag

After downloading the source material over HTTPS, Ask Astro pushes it into Weaviate, an open-source vector database. During this step, Weaviate makes an API call to OpenAI to convert the document text into an embedding, which Weaviate saves locally.

#### Answer generation

When a user submits a question through the API, Ask Astro undertakes a multi-step process to retrieve relevant documents and generate an answer. This process begins by asking the LLM to generate two reworded versions of the original question to aid in retrieving relevant documents from the vector database. These questions are forwarded to Weaviate, which uses a cosine similarity search to retrieve the most relevant documents. Ask Astro then [invokes](https://python.langchain.com/docs/integrations/retrievers/cohere-reranker) the [Cohere Reranker API](https://docs.cohere.com/docs/reranking), a well-known LLM provider, to rerank these documents according to their relevance to the user’s original question. An LLM filter then removes documents the model evaluates as irrelevant to the user’s question. Finally, the LLM generates a user-facing answer, with the final list of documents packaged into the question’s context window.

### The limitations of RAG in adversarial settings

RAG is a powerful way to make LLMs more knowledgeable and more responsive to the needs of a business and its customers. RAG systems also suffer the same well-known flaws as LLMs, such as prompt injection and hallucinations. Additionally, RAG systems depend on the reliability of inputs placed into the vector database. In most non-trivial applications, such as Ask Astro, the documents used to augment the LLM’s knowledge base include untrusted documents. The ability to include untrusted documents is not an aberration but a desired feature: people want to do RAG over websites, comments, and user-supplied documents.

Due to fundamental undecidability results, it is impossible for an automated algorithm to flawlessly determine whether a forum post or GitHub comment contains misleading information or is otherwise malicious. Any sufficiently useful RAG system will inevitably index misleading or malicious content.

Academic research on poisoning attacks against hundreds of millions of image-text pairs shows this issue is significant. Many RAG applications use far smaller data sets as input to their vector databases, making poisoning attacks against vector databases economically viable.

Our audit of Ask Astro illustrates how these risks can manifest in practice. We show that attackers can manipulate the application’s knowledge base in ways that parallel the two types of poisoning attacks described in [Poisoning Web-Scale Training Datasets is Practical by Carlini et al.](https://arxiv.org/pdf/2302.10149.pdf), namely front-running and split-view poisoning:

* Split-view poison...