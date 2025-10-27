---
title: Auditing Gradio 5, Hugging Face’s ML GUI framework
url: https://blog.trailofbits.com/2024/10/10/auditing-gradio-5-hugging-faces-ml-gui-framework/
source: Trail of Bits Blog
date: 2024-10-11
fetch_date: 2025-10-06T18:51:18.918617
---

# Auditing Gradio 5, Hugging Face’s ML GUI framework

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Auditing Gradio 5, Hugging Face’s ML GUI framework

Trail of Bits

October 10, 2024

[machine-learning](/categories/machine-learning/)

This is a joint post with the Hugging Face Gradio team; read their announcement [here](https://huggingface.co/blog/gradio-5-security)! You can find the full report with all of the detailed findings from our security audit of Gradio 5 [here](https://github.com/trailofbits/publications/blob/master/reviews/2024-10-huggingface-gradio-securityreview.pdf).

Hugging Face hired Trail of Bits to audit Gradio 5, a popular open-source library that provides a web interface that lets machine learning (ML) developers quickly showcase their models. Based on our findings and recommendations from the audit, Gradio enhanced its application with strong, secure defaults across all deployment scenarios. End users can now rely on enhanced built-in security measures whether they’re running apps locally, deploying on Hugging Face Spaces or other servers, or using built-in share links.

The Gradio team commended us for the high quality and speed of our work:

> The Trail of Bits security team was fantastic and the review exceeded our expectations in speed and depth. Within 2 weeks, they not only got up-to-speed with our relatively large codebase, which spans Python, JavaScript, and Go, but they identified many security issues that required a deep understanding of how Gradio and Hugging Face are used in practice to build machine learning apps. To top it off, they iterated with us to develop mitigation strategies that addressed the security issues without sacrificing the ease-of-use that is important to so many Gradio developers.

Our review uncovered eight high-severity issues in Gradio 5 before its release, including vulnerabilities in the Gradio-deployed infrastructure that supports sharing your machine learning models and interfaces with the world. We also found vulnerabilities such as SSRF, XSS, and arbitrary file leaks in specific Gradio server configurations. We didn’t stop at finding bugs; we also provided recommendations to prevent bugs in the future, such as integrating static and dynamic analysis into the SDLC and creating fuzz tests for critical functions.

Following a post-audit fix review, we are confident that all reported issues have been sufficiently addressed and do not pose a risk to Gradio 5, the newest version of Gradio released on October 9, 2024. If you’re running an older version of Gradio, update your application in the command line by running `pip install --upgrade gradio`.

This blog post will cover Gradio’s functionality, our audit process, and some findings we uncovered during the audit. You can also read the full report.

### Gradio

Gradio is a framework that provides a simple and easy-to-use interface for building web-based machine-learning applications. It enables developers to create interactive and shareable demos with just a few lines of code without any prior web development experience. Gradio is very popular among machine learning practitioners, with more than 6.1M downloads a month on PyPi, working as the engine of very popular projects such as [Stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui), which has 141k stars on GitHub, and [text-generation-webui](https://github.com/oobabooga/text-generation-webui), which has 40k stars on GitHub.

Let’s see how to implement the simplest Gradio interface.

```
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
```

This code specifies a text component as the input, a function named `greet` that transforms that input, and another text component as the output. Running it creates the following website.

![](/img/wpdump/5577352d9b80b9ae489ca2e563549e32.png)

A Gradio interface is architectured based on **input components**, **user-defined Python functions** that transform the input, and **output components** that render those transformations. Each input component has a pre-process function responsible for transforming the user’s input into the type received in the user-defined Python function (e.g., transforming an Image into a numpy array), and each output component has a post-processing function that does the reverse (e.g., transforming a numpy array into an Image component). The image below shows this process visually.

![](/img/wpdump/4cf4fa54848dca0323b3750ef9076c93.png)

Gradio includes many pre-built components such as a TextBox, Image, FileExplorer, and even a full Chatbot, which is what makes it so easy to use out of the box.

The other feature that makes Gradio stand out is how easily you can share your demo with co-workers or the whole world. Users can expose their Gradio demo online by simply calling the `launch` function with `share=True`, which creates a tunnel to their machine and exposes the Gradio server externally using [frp](https://github.com/fatedier/frp). We’ll see more details on how this works in the next section.

### Our audit and findings

Securing Gradio requires thinking deeply about the user experience (UX). Given its simplicity, one cannot expect Gradio users to set up CORS and CSP policies or cookie attributes. Additionally, Gradio is not a “simple” backend server with a concrete task and a well-defined threat model; Gradio is a flexible framework with support for many use cases (e.g., authenticated vs unauthenticated server, local vs shared server, the ability to embed the demo in other websites, etc.). These reasons make it harder to implement secure defaults that work for every use case. For this reason, we worked closely with the Gradio team to find solutions and secure defaults that did not impact the developer experience.

At the beginning of our audit, we divided it into two main tasks: reviewing the Gradio server implementation and the sharing infrastructure.

#### The Gradio server

Considering that the server may be exposed externally, a vulnerability such as an arbitrary file leak from the user’s machine may have severe consequences.

When reviewing the Gradio Server, we aimed to answer the following non-exhaustive list of questions:

* Can attackers exfiltrate arbitrary files from a user’s Gradio server?
* Can attackers upload files to arbitrary locations on a user’s Gradio server?
* Can attackers make arbitrary requests on the user’s internal network?
* Are any Gradio API endpoints, components’ pre- and post-process functions, or components’ `@server` functions vulnerable to injection attacks that could lead to remote code execution or arbitrary file exfiltration?
* Can an attacker bypass Gradio’s server authentication mechanisms?

During our review, we uncovered six high-severity findings that could compromise a user’s Gradio server in certain scenarios, including:

* **TOB-GRADIO-1** and **TOB-GRADIO-2**: Misconfigurations in the server’s CORS policy that, in the context of an authenticated Gradio server, would allow attackers to steal access tokens and take over a victim’s accounts when they visit their malicious website.
* **TOB-GRADIO-3**: A full read GET-based SSRF that would allow attackers to make requests and read the responses from arbitrary endpoints, including those on the user’s internal network.
* **TOB-GRADIO-10**: Arbitrary file type uploads that would allow an attacker to host HTML and XSS payloads on a user’s Gradio server. In the context of an authenticated Gradio server, an attacker could use this to take over user accounts when the victim accesses an attacker’s malicious website.
* **TOB-GRADIO-13**: A race condition that allows an attacker to reroute user traffic to their server and steal uploaded files or chatbot conversations.
* **TOB-GRADIO-16**: Several components’ post-process functions could allow attackers to leak arbitrary files in very...