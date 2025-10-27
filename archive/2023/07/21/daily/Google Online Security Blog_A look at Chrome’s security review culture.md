---
title: A look at Chrome’s security review culture
url: http://security.googleblog.com/2023/07/a-look-at-chromes-security-review.html
source: Google Online Security Blog
date: 2023-07-21
fetch_date: 2025-10-04T11:51:05.110020
---

# A look at Chrome’s security review culture

![](https://ad.doubleclick.net/ddm/activity/src=2542116;type=gblog;cat=googl0;ord=1?)

[![](https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png)](https://security.googleblog.com/)
[## Security Blog](/.)

The latest news and insights from Google on security and safety on the Internet

## [A look at Chrome’s security review culture](https://security.googleblog.com/2023/07/a-look-at-chromes-security-review.html "A look at Chrome’s security review culture")

July 20, 2023

Posted by Alex Gough, Chrome Security Team

Security reviewers must develop the confidence and skills to make fast, difficult decisions. A simplistic piece of advice to reviewers is “just be confident” but in reality that takes practice and experience. Confidence comes with time, and people are there to support each other as we learn. This post shares advice we give to people doing security reviews for Chrome.

### Security Review in Chrome

Chrome has a lightweight launch process. Teams write requirements and design documents outlining why the feature should be built, how the feature will benefit users, and how the feature will be built. Developers write code behind a [feature flag](https://chromium.googlesource.com/chromium/src/%2B/main/base/feature_list.h) and must pass a Launch Review before turning it on. Teams think about security early-on and coordinate with the security team. Teams are responsible for the safety of their features and ensuring that the security team is able to say ‘yes’ to its security review.

Security review focuses on the design of a proposed feature, not its details and is distinct from [code review](https://chromium.googlesource.com/chromium/src/%2B/master/docs/security/ipc-reviews.md). Chrome changes need approval from engineers familiar with the code being changed but not necessarily from security experts. It is not practical for security engineers to scrutinize every change. Instead we focus on the feature’s architecture, and how it might affect people using Chrome.

Reviewers function best in an open and supportive engineering culture. Security review is not an easy task – it applies security engineering insights in a social context that could become adversarial and fractious. Google, and Chrome, embody a [security-centric](https://static.googleusercontent.com/media/sre.google/en//static/pdf/building_secure_and_reliable_systems.pdf#page=481) engineering culture, where respectful disagreement is valued, where [we learn from mistakes](https://sre.google/sre-book/postmortem-culture/), where decisions can be revisited, and where developers see the security team as a partner that helps them ship features safely. Within the security team we support each other by encouraging questioning & learning, and provide mentorship and coaching to help reviewers enhance their reviewing skills.

### Learning security review

## Start by shadowing

Start with some help. As a new reviewer, you may not feel you’re 100% ready — don’t let that put you off. The best way to learn is to observe and see what’s involved before easing in to doing reviews on your own. Start by shadowing to get a feel for the process. Ask the person you are shadowing how they plan to approach the review, then look at the materials yourself. Concentrate on learning how to review rather than on the details of the thing you are reviewing. Don’t get too involved but observe how the reviewer does things and ask them why. Next time try to co-review something - ask the feature team some questions and talk through your thoughts with the other reviewer. Let them make the final approval decision. Do this a few times and you’ll be ready to be the main reviewer, and remember that you can always reach out for help and advice.

## Read enough to make a decision

Read a lot, but know when to stop. Understand what the feature is doing, what’s new, and what’s built on existing, approved, mechanisms. Focus on the new things. If you need to educate yourself, skim older docs or code for context. It can help to look at related reviews for repeated issues and solutions. It is tempting to try to understand everything and at first you’ll dig deeper than you need to. You’ll get better at knowing when to stop after a few reviews. Treat existing, approved, features as building blocks that you don’t need to fully understand, but might be useful to skim as background.

Launch review is a gate. It’s ok to ask feature teams to have the materials ready. Try to use your time wisely — if a design doc is very brief and lacks any security discussion you can quickly say "please add a security considerations section" and stop thinking about it until the team comes back with more complete documentation. If the design document doesn’t fully explain something that is a sign the document needs to be expanded — if something isn’t clear to you or isn’t covered then start asking questions. Remember that you’re not looking for every possible bug, but ensuring that major concerns are addressed upfront.

As you’re reading, read actively and write down observations and questions as you go. Cross them off if you find an answer later. For your first reviews this will take a long time. Don’t worry too much about that - you won't know yet which details matter. Over time you’ll learn where to focus your attention. This is also a good time to pair up with a seasoned reviewer. Schedule a chat to go over your thoughts before you share them with the feature team. This will help you understand the process people go through and allows a safe evaluation of your thoughts before you share them more widely - this will help you build confidence. Next, clarify any questions with the feature team. Try to write a sentence or two describing the feature - if you can’t do this it indicates you need more information.

## Ask questions to improve documentation

You have permission to be ignorant! Use it! Ask questions until you understand areas of uncertainty. Asking questions provides real value, and often triggers the team to realize that something should be done differently. In particular — if it’s confusing to you it’s probably badly explained or badly thought out, or shows that an assumption or tacit knowledge is missing from a design document. If you’re worried about looking ignorant, make use of the more experienced reviewers around you — ask on the chat or book some time to talk over your thoughts one-on-one. This should help you formulate your question so that it’s useful to the feature team. Try to write out what you think is happening, and let the feature team tell you if you’re close or not.

The chances that you’ll understand everything immediately are very low, and that’s ok. In meetings about a feature a favorite question of mine is ‘what are you secretly worried about?’ followed by an awkward pause. People will absolutely tell you things! Sometimes there's a domain-knowledge mismatch when you don't have the right words to ask the question, so you can't get a useful answer. Always ask for a diagram that shows which process or component different parts of a feature are happening in — this helps you hone in on the critical interfaces, and will illustrate the design more clearly than screenfuls of text or code.

## Center people in your security analysis

We’re here to help people. Try to center people in your thoughts and arguments. How will people use the feature? Who are they? Who might harm them and how? Are there particular groups of people that might be more vulnerable than others, and what can we do to protect them? How does the feature make people feel? How will their experience of the application change? How will their lives be affected? Think about how a bad actor might abuse the feature. What implicit assumptions is the implementation making about the people using it? What or who are we asking people to trust? What if someone modifies traffic, changes a message, passes in bad data, or tricks someone into using the fe...