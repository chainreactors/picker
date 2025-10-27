---
title: Manipulating Weights in Face-Recognition AI Systems
url: https://www.schneier.com/blog/archives/2023/02/manipulating-weights-in-face-recognition-ai-systems.html
source: Schneier on Security
date: 2023-02-04
fetch_date: 2025-10-04T05:42:51.827629
---

# Manipulating Weights in Face-Recognition AI Systems

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Manipulating Weights in Face-Recognition AI Systems

Interesting research: “[Facial Misrecognition Systems: Simple Weight Manipulations Force DNNs to Err Only on Specific Persons](https://arxiv.org/abs/2301.03118)“:

> **Abstract:** In this paper we describe how to plant novel types of backdoors in any facial recognition model based on the popular architecture of deep Siamese neural networks, by mathematically changing a small fraction of its weights (i.e., without using any additional training or optimization). These backdoors force the system to err only on specific persons which are preselected by the attacker. For example, we show how such a backdoored system can take any two images of a particular person and decide that they represent different persons (an anonymity attack), or take any two images of a particular pair of persons and decide that they represent the same person (a confusion attack), with almost no effect on the correctness of its decisions for other persons. Uniquely, we show that multiple backdoors can be independently installed by multiple attackers who may not be aware of each other’s existence with almost no interference.
>
> We have experimentally verified the attacks on a FaceNet-based facial recognition system, which achieves SOTA accuracy on the standard LFW dataset of 99.35%. When we tried to individually anonymize ten celebrities, the network failed to recognize two of their images as being the same person in 96.97% to 98.29% of the time. When we tried to confuse between the extremely different looking Morgan Freeman and Scarlett Johansson, for example, their images were declared to be the same person in 91.51% of the time. For each type of backdoor, we sequentially installed multiple backdoors with minimal effect on the performance of each one (for example, anonymizing all ten celebrities on the same model reduced the success rate for each celebrity by no more than 0.91%). In all of our experiments, the benign accuracy of the network on other persons was degraded by no more than 0.48% (and in most cases, it remained above 99.30%).

It’s a weird attack. On the one hand, the attacker has access to the internals of the facial recognition system. On the other hand, this is a novel attack in that it manipulates internal weights to achieve a specific outcome. Given that we have no idea how those weights work, it’s an important result.

Tags: [academic papers](https://www.schneier.com/tag/academic-papers/), [backdoors](https://www.schneier.com/tag/backdoors/), [face recognition](https://www.schneier.com/tag/face-recognition/)

[Posted on February 3, 2023 at 7:07 AM](https://www.schneier.com/blog/archives/2023/02/manipulating-weights-in-face-recognition-ai-systems.html) •
[14 Comments](https://www.schneier.com/blog/archives/2023/02/manipulating-weights-in-face-recognition-ai-systems.html#comments)

### Comments

modem phonemes •
[February 3, 2023 9:07 AM](https://www.schneier.com/blog/archives/2023/02/manipulating-weights-in-face-recognition-ai-systems.html/#comment-417089)

From the paper

“ To avoid suspicion and detection, the attacker … is only allowed to tweak the weights of its last layer. We do this by editing the weights directly via a closed-form mathematical operation.

… these results should be of interest both to security researchers (who would like to understand how to backdoor deep neural networks), and to machine learning researchers (who would like to understand better the relationships between the network’s weights and behavior).”

Coming for ya ChatGPT.

hmw •
[February 3, 2023 9:23 AM](https://www.schneier.com/blog/archives/2023/02/manipulating-weights-in-face-recognition-ai-systems.html/#comment-417092)

One non-weird use case would be to make personnel from the organization employing the facial recognition system non-recognizable. If an intelligence agency wanted to make sure their undercover operatives do not pop up in police investigations (or vice versa :), they might have the access required for this attack.

Winter •
[February 3, 2023 9:38 AM](https://www.schneier.com/blog/archives/2023/02/manipulating-weights-in-face-recognition-ai-systems.html/#comment-417093)

> On the other hand, this is a novel attack in that it manipulates internal weights to achieve a specific outcome. Given that we have no idea how those weights work, it’s an important result.

Indeed, this could even be a way in to get a partial explanation of how a certain result is obtained.

As @modem observes:

> “ To avoid suspicion and detection, the attacker … is only allowed to tweak the weights of its last layer. ”

This would point to a way to get at the results in a layer for layer peeling analysis. Also, knowing that the entry layers doe very general data preprocessing, it is the later layers that more directly influence decisions.

B-N-O •
[February 3, 2023 11:03 AM](https://www.schneier.com/blog/archives/2023/02/manipulating-weights-in-face-recognition-ai-systems.html/#comment-417095)

> Given that we have no idea how those weights work
> We do, at least to an extent. Meng et al. have successfully “moved” the Eifel Tower to Rome in GPT knowledge in 2022: <https://rome.baulab.info/> (the description includes multiple references to other knowledge-editing experiments).

Robin •
[February 4, 2023 4:32 AM](https://www.schneier.com/blog/archives/2023/02/manipulating-weights-in-face-recognition-ai-systems.html/#comment-417158)

Coincidentally in the Guardian newspaper, Friday 3rd February 2023:

“March of the robots: how biometric tech could kill off paper passports.

… an increasing use of biometrics, with facial recognition cameras that operate all around the airport, could enable travellers to walk through automatic gates without having to pause to fish out any travel documents. … ”

Yeah right.

<http://www.theguardian.com/politics/2023/feb/03/biometric-technology-paper-passports-redundant>

Ted •
[February 4, 2023 10:38 AM](https://www.schneier.com/blog/archives/2023/02/manipulating-weights-in-face-recognition-ai-systems.html/#comment-417170)

> Given that we have no idea how those weights work, it’s an important result.

Yes, this one has me scratching my head and wishing for more academic training.

The toy example in the paper (with visual graphs) is helpful in trying to understand how a class (an individual identity) can be represented and transformed as a vector in the feature space.

Now Khan Academy isn’t the Weizmann Institute of Science, but they do have some nice video tutorials on vectors, matrixes, and linear transformations.

I wonder what Adi Shamir and Irad Zehavi would think.

Between the two classes of backdoors:

* The Shattered Class (SC) backdoor
* The Merged Classes (MC) backdoor

… I’m almost more alarmed by the MC backdoor.

The paper notes that Apple’s FaceID is a biometric authentication system that uses OSOSR “(checking whether the probe image ...