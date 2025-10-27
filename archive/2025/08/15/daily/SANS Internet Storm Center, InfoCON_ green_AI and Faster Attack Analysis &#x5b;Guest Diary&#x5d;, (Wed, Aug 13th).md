---
title: AI and Faster Attack Analysis &#x5b;Guest Diary&#x5d;, (Wed, Aug 13th)
url: https://isc.sans.edu/diary/rss/32198
source: SANS Internet Storm Center, InfoCON: green
date: 2025-08-15
fetch_date: 2025-10-07T00:50:13.211313
---

# AI and Faster Attack Analysis &#x5b;Guest Diary&#x5d;, (Wed, Aug 13th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/32196)
* [next](/diary/32202)

# [AI and Faster Attack Analysis [Guest Diary]](/forums/diary/AI%2Band%2BFaster%2BAttack%2BAnalysis%2BGuest%2BDiary/32198/)

**Published**: 2025-08-13. **Last Updated**: 2025-08-14 00:06:17 UTC
**by** [Guy Bruneau](/handler_list.html#guy-bruneau) (Version: 1)

[0 comment(s)](/diary/AI%2Band%2BFaster%2BAttack%2BAnalysis%2BGuest%2BDiary/32198/#comments)

[This is a Guest Diary by Joseph Noa, an ISC intern as part of the SANS.edu [BACS](https://www.sans.edu/cyber-security-programs/bachelors-degree/) program]

**Introduction**

Time is of the essence when it comes to attacks and understanding what you're seeing can be tricky when under pressure. As security professionals, we need to use every tool available to us so we can identify, stop, and then mitigate threats. Artificial Intelligence (AI) is the future. It is a tool that can make security professionals more efficient, and I cannot stress that point. It is a **TOOL**. ChatGPT, Gemini, Copilot, and others are readily available to us whether we subscribe or use a free tier. I use AI at my job to help me with my analysis and various tasks. So, I'm going to talk about it.

**Why AI**

I want to state again that AI is a tool. Security professionals use tools every day and AI is a tool that should be leveraged to help fill in knowledge gaps or assist in analysis. Google is a phenomenal tool when it comes to researching things. Whether it be you need help programming/scripting or need to know about a tool and how to use it, Google has been the go-to for years.

However, the process of using Google can be time consuming. Let's say you are programming/scripting something to perform a specific task, or that can ingest data and produce a specific result catered to your needs. You want this item to be repeatable. You are struggling to get the results you want. There is a line of code that is executing but the data is being expressed in the incorrect format, or it is only producing part of the data that it is supposed to. Maybe a loop is failing to execute. Maybe it just fails. There are endless reasons why it could be failing. This has happened to me countless times while working with PowerShell and Python. It can be an extremely frustrating process. So now we turn to Google to point us in a direction. We look at several Stack Overflow threads or another technical forum that show something similar to what you are trying to accomplish and now it is added to the code. It runs and it still fails. Then we realize the code in the thread is for Python 2 and the code that is being developed is Python 3. Features may have changed or been removed entirely. So, what now?

**AI and Coding**

Technology is constantly changing. There are new features and updates on a regular basis. It is impossible to keep up. I'm not a coder by trade but I have needed to build things out in Python and PowerShell. Constant trial and error. Sometimes, it is a lot more error then not.

This is where I think AI can prove to be extremely valuable. We can copy and paste code into the AI chat box and ask questions about the specific issue that is causing the code to fail to produce the desired results. AI provides instant feedback. Sometimes it may be something as simple as not having the formatting correct causing a loop to not execute but also not throw an error. AI can quickly identify the issue and return code that now has the correct formatting. We can then take that code, run it, and now we find it is working and producing the desired result. This all happens over the course of a few minutes whereas continuing to Google the issue just continues to yield different answers that fail to resolve the issue. This can happen simply due to our failure to notice that a line of code wasn't nested correctly in a loop because the indentation was incorrect.

The best part about this is that not only does the AI provide the corrected code back, but AI will also provide an explanation of the issue, highlighting the differences between the incorrect code and the corrected code. Explanations can go a long way in terms of learning and growing our skillsets.

The normal "Hello World!" test should be enough to just give a simple example of how AI can help with coding.

I'm going to run hello\_world.py. The code is shown below.

#bad code

print(hello world!)

The screenshot below shows the error that's thrown when attempting to run the bad code.

![](https://isc.sans.edu/diaryimages/images/Joseph_Noa_Picture1.png)

Let's throw that code into Gemini (Google's AI and my preferred AI) and see what Gemini tells us.

![](https://isc.sans.edu/diaryimages/images/Joseph_Noa_Picture2.png)

Gemini took ingested the code, reviewed it, and, in this case, gave us the feedback within seconds. We will see that Gemini not only provided two different solutions to our problem but also explains why it wasn't working.

Let's try out the solutions. Below are the two examples of the code. I'll use them to create two scripts and then run them in my terminal to see if they work. As you can see, Gemini provided us with two solutions to our code and they both worked.

print("hello world!")

print('hello world!')

![](https://isc.sans.edu/diaryimages/images/Joseph_Noa_Picture3.png)

One thing to note, using AI does not replace our need to understand coding and what we are doing. AI can and will be wrong at times. We need to be able to pivot if the AI doesn't generate usable code. This is an instance where instead of looking to AI to provide the solution, we can use the information to pivot in our search for a solution based on the information we were given. Either way, we can get to where we need to be more quickly with the help of AI.

**AI and Analysis**

Similarly with coding, AI can be a huge benefit when it comes to the analysis of attacks. Attacks come in different forms which require different analysis. If a machine is infected with a malicious PowerShell script that has base64 encoding to obfuscate what it does, you can take that script and throw it into an AI prompt and will let you know if the script is malicious, has base64 encoding, and let you know what it's doing. AI will do this and do it rather quickly.

Another example is when a threat actor has established a shell on a system. The logs are being sent to a SIEM where you can see what commands were being executed on the machine. AI can help put together a picture of what the threat actor is attempting to accomplish based on the commands. Let's run through an example of this.

I had never done a honeypot before so the internship for the BACS is the first time I was exposed to some of these things. For my first observation, I saw some commands being run on the sensor that I wasn't familiar with. I generally understood what was happening, but I hadn't seen a `nohup $SHELL` before.
The screenshot below is from my observation assignment.

![](https://isc.sans.edu/diaryimages/images/Joseph_Noa_Picture4.png)

If we Google `nohup $SHELL` we can see that sometimes, even if we don't want to, we are going to get an answer from AI. Gemini is built into Google and if it can provide an answer, it will.

![](https://isc.sans.edu/diaryimages/images/Joseph_Noa_Picture5.png)

When we Google `nohup $SHELL` we get an answer like we would going to <https://gemini.google.com/> and using the prompt to ask our question. Gemini provides a breakdown and shows that nohup command stands for "no hang up" and that $SHELL refers to the environment variable for the default shell of the user.

We can take our analysis a little further. I'm going to use the Gemini prompt and submit the entirety of the command to get a breakdown of what is happening. Both the command that was executed and the resp...