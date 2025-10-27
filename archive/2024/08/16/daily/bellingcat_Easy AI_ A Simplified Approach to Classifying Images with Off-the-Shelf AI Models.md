---
title: Easy AI: A Simplified Approach to Classifying Images with Off-the-Shelf AI Models
url: https://www.bellingcat.com/resources/how-tos/2024/08/15/easy-ai-zero-shot-ai-image-classification-smart-image-sorter/
source: bellingcat
date: 2024-08-16
fetch_date: 2025-10-06T18:05:23.853948
---

# Easy AI: A Simplified Approach to Classifying Images with Off-the-Shelf AI Models

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)

* EN
  + [Русский](https://ru.bellingcat.com)
  + [Français](https://fr.bellingcat.com)
  + [Español](https://es.bellingcat.com)
  + [Deutsch](https://de.bellingcat.com)
  + [Українська](https://uk.bellingcat.com)
* [Donate](https://www.bellingcat.com/donate)

Search for:

* [Investigations](https://www.bellingcat.com/category/news/)
* [Guides](https://www.bellingcat.com/category/resources/)
* [Ukraine](https://www.bellingcat.com/tag/ukraine/)
* [Workshops](https://www.bellingcat.com/workshops/)
* [Donate](/donate)

[![](https://www.bellingcat.com/app/uploads/2024/08/adriano-300x300.jpg)](https://www.bellingcat.com/author/adrianobelisario/)
[Adriano Belisario](https://www.bellingcat.com/author/adrianobelisario/)

Adriano Belisario is a 2024 Bellingcat Tech Fellow. He is passionate about using data, journalism and open source tools to address pressing social issues.

# Easy AI: A Simplified Approach to Classifying Images with Off-the-Shelf AI Models

August 15, 2024

* [AI](/tag/ai)
* [Imagery Analysis](/tag/imagery-analysis)

Suppose you’ve scraped thousands of images from a Telegram group or social media site, some of which may be crucial to an investigation of an ongoing conflict. You’re looking specifically for photos and videos of weapons, but these are mixed in with memes, screenshots and other unrelated material, and manually reviewing and categorising the images would take more time than you have. What do you do?

In this guide, we show you how you can use artificial intelligence (AI) models to speed up such tasks – even if you don’t know how to code – with the help of the [Smart Image Sorter](https://colab.research.google.com/github/bellingcat/smart-image-sorter/blob/main/interface.ipynb), an open-source tool we created.

AI image classification has proven useful in previous investigations, such as those involving [war crimes in Yemen](https://www.technologyreview.com/2020/06/25/1004466/ai-could-help-human-rights-activists-prove-war-crimes/) or [illegal mining in the Amazon rainforest](https://www.nytimes.com/interactive/2022/08/02/world/americas/brazil-airstrips-illegal-mining.html).

Traditionally, this requires some degree of technical expertise – from knowing how to access AI models in the first place to training them to recognise specific categories of objects.

The Smart Image Sorter, however, uses a specific family of models – known as zero-shot models – that can be used off the shelf, making it easy for anyone to get started with classifying images with AI.

What is Zero-Shot Image Classification?

AI image classification models traditionally require training with specific labels linked to images. Users are limited to the categories predefined by the labels, restricting the model’s ability to identify anything outside the established labels. For example, a model only trained on images labelled as cats and dogs is likely to recognise these animals, but fail to identify a penguin due to the absence of images labelled as penguins  in the training data.

Zero-shot models, a relatively new innovation in the field of machine learning and AI, help overcome these restrictions. They are trained on a diverse array of data and have a broad understanding of language and images, making it possible to classify images that were never included in their training. For instance, a zero-shot model might recognise a penguin by relating its black and white colours and bird-like shape to similar images it has seen, even if it has never been trained specifically on penguins.

Introduced in 2021, OpenAI’s [CLIP](https://github.com/openai/CLIP) (Contrastive Language–Image Pre-training) model has been influential in popularising this method of image classification due to its flexibility and robust performance.

CLIP and similar AI models learn to match pictures with descriptions by turning both text and images into numerical representations, known as embeddings, that a computer can understand. When you give them a new image or text, they check how closely it matches the things they have learned before by comparing these numbers in what is known as a shared embedding space.

![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXfKS_KByeKxhdOrN7sGV5fTuWdqSvzksgbiWtQ9qwumUcL6txGTDqXVGrzYQBPieojuO91U-GK7eIwMpQZl0E8UqhhoJ2-PMPQ8eJEMjvVYqY1r2V0n8xRIrIwJRA0JdyLT-HtBahwYIF42OPaUQ29eYWg?key=1lUeg-O0v8qq98kfm7b84w)

*Similar words and images are clustered together in a shared embedding space. On the left, an input image of a penguin is correctly matched to the label “penguin”. On the right, an image of a tiger in the sea is incorrectly matched to the label “seal” due to its proximity to labels related to sea-dwelling creatures. Graphic: Galen Reich.*

## Using the Smart Image Sorter with Google Colab

The easiest way to run the Smart Image Sorter is by running our programme on Google Colab directly in your web browser, and uploading any images you would like to use on Google Drive.

Google Colab is a free, cloud-based tool that allows users to write and execute Python code from web browsers using an interactive environment known as a “notebook”. Bellingcat has previously published a [detailed guide](https://www.bellingcat.com/resources/2024/03/06/how-code-notebooks-enable-open-source-research/) and [explainer video](https://www.youtube.com/watch?v=ymCMy8OffHM&list=PLq6cQ--4f90icDJUwiGcPrFFLLguuZ0ht) on how notebooks can be useful for open-source research.

### 1. Load the Tool

To begin, ensure that you are logged into your Google account. Open the [tool](https://colab.research.google.com/github/belisards/zeroshot_img_classifier/blob/main/interface.ipynb) in your browser and click “▶” to load it.

You will see a warning that the notebook was not authored by Google. This is a standard warning for any notebook loaded from an external source. Don’t worry: none of the code used in this tool is malicious, and it does not grant Bellingcat or other users access to your data. To proceed, click on “Run anyway”.

![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXcjTWGybL5JUcc11fhvCWkUrlOvH0j0-zAuCqlQdjPe9BVgY82s-p500WDSKMJMBxdgbf4S50s_YxCRO2-J6ZA4KaySMj5UOg2wAYaorg3aa891XCKrjBVy5maED0qC3QopLBjyvNdUmYgAsG13kkAEyD7x?key=1lUeg-O0v8qq98kfm7b84w)

*To start running the Smart Image Sorter, simply click “▶” and then “Run anyway”.*

You should see five form fields that have been pre-filled with default values. If you simply want a quick idea of the output generated by this tool, you may [skip to Step 7](#start-classification) and run it immediately. Otherwise, read on.

### 2. Add Your Own Images (Or Use Ours)

The first field you have to fill in is the source directory, which is simply where the images you want to classify are stored.

For the purposes of this tutorial, we have provided a [sample set of 32 images](https://github.com/bellingcat/smart-image-sorter/tree/main/imgs), from a previous [Bellingcat investigation](https://qanon.bellingcat.com/) on QAnon groups on Telegram, as the default source directory.

However, if you would like to use your own image collection, upload the images to a folder in your own Google Drive and click on the “Mount Google Drive” button to give Google Colab access to your Google Drive. (This will not grant Bellingcat or any other users access to your files or data.)

Get the path of your image folder by right-clicking on the relevant folder in the file manager, and selecting “Copy path”, then paste it into the “Source” field.

![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXeJlWrqay82aADsUzwFMZwrfNUKg8ZFIdYG_zXZIgKdfBQXC19bF6PutomK3HVk-OjTZiCWiq_yMlbLUADD6vzW6saV-Co_CFBY7Lp5nV1CobUIl45epcPiqv6jI8un9UsSYEsYcKQKmFDwR4SmQ_3fxAc?key=1lUeg-O0v8qq98kfm7b84w)

*Copy the path to the relevant folder in your Google Drive and paste...