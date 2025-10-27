---
title: Tutorial for CMIYC2024: Registering a Team and Cracking Test Hashes
url: https://reusablesec.blogspot.com/2024/08/tutorial-for-cmiyc2024-registering-team.html
source: Reusable Security
date: 2024-08-06
fetch_date: 2025-10-06T18:04:37.501124
---

# Tutorial for CMIYC2024: Registering a Team and Cracking Test Hashes

[Skip to main content](#main)

### Search This Blog

# [Reusable Security](https://reusablesec.blogspot.com/)

Password Cracking, Crypto, and General Security Research

### Tutorial for CMIYC2024: Registering a Team and Cracking Test Hashes

* Get link
* Facebook
* X
* Pinterest
* Email
* Other Apps

By

[Matt Weir](https://draft.blogger.com/profile/16111343330590419341 "author profile")

-
[August 04, 2024](https://reusablesec.blogspot.com/2024/08/tutorial-for-cmiyc2024-registering-team.html "permanent link")

[![AI generated picture of a Black Kitten wearing a tophat cracking passwords](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXAf8bny_IIW_Qf6nNBbptxuQowT6tZvZrfE9rmiK9jECKR00D-TJ84w_MxFVAFKPSXzc7v8ebvnsXVGHQ9CLVCwnbi0JOT-QcClfAYEYSfK6iUNJUu0V_UHMBiP44c-aQa-HMTG6kqKrBNbAS9imNOqoyFtUBFL2F6ZkTaU24qzz3HLdZmWkvJYs78wk/w640-h366/cmiyc2024_test.webp "Let's Crack Some Passwords!")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXAf8bny_IIW_Qf6nNBbptxuQowT6tZvZrfE9rmiK9jECKR00D-TJ84w_MxFVAFKPSXzc7v8ebvnsXVGHQ9CLVCwnbi0JOT-QcClfAYEYSfK6iUNJUu0V_UHMBiP44c-aQa-HMTG6kqKrBNbAS9imNOqoyFtUBFL2F6ZkTaU24qzz3HLdZmWkvJYs78wk/s1456/cmiyc2024_test.webp)

> ***Whenever a thing is done for the first time, it releases a little demon.***

> **- Emily Dickinson**

## Getting Ready For Crack Me If You Can 2024

August is like New Years for me. With BSides Vegas, Defcon, and all the other hacker conferences, I find myself taking stock of the previous year, realizing all the plans I did not accomplish, and I find myself setting goals for the next year. One of the things I am happy about though is that I now have a password cracking framework to help me compete in this year's Crack Me If You Can competition. Like the last couple of years I plan on competing by myself on team "Reusablesec" since I think it's important to try (and probably fail) vs. just talk about password security.

I'd also like it if new players also competed and learned from this contest. The problem is, the Crack Me If You Can contest can be intimidating, and the barrier of entry can be high. I mean, you need to figure out how to use PGP, which isn't easy, and that is on top of installing/configuring/using password cracking programs! To that end, this blog entry is focused on highlighting how you can use the Password Cracking Framework to get your team registered, and will walk you through how to crack the test hashes and how to submit them. That way you can focus on the fun parts such as cracking hashes and trying to figure out whatever Led Zeppelin themed challenge Korelogic is sure to throw at you this year.

**Note:** While the test hashes will be "spoiled" in this blog entry, I WILL NOT be posting any actual contest solutions until after the competition is over. If you want to attempt to crack the test hashes yourself (which would be awesome) feel free to skip this blog entry and come back to it after you are done so I don't spoil the challenge for you.

## Resources:

**Official Contest Resources:**

* Korelogic Contest Website: [[Link](https://contest-2024.korelogic.com/)]
* Korelogic Registration Info: [[Link](https://contest-2024.korelogic.com/howto_register.html)]
* Korelogic Hash Downloads: [[Link](https://contest-2024.korelogic.com/downloads.html)]
* Korelogic Scoreboard: [[Link](https://contest-2024.korelogic.com/stats.html)]

**Password Cracking Framework Resources:**

* Github Site for Code: [[Link](https://github.com/lakiw/Jupyter-Password-Cracking-Framework)]
* Previous CMIYC Tutorial (Part 1): [[Link](https://reusablesec.blogspot.com/2023/08/using-jupyterlab-to-manage-password.html)]
* Previous CMIYC Tutorial (Part 2): [[Link](https://reusablesec.blogspot.com/2023/08/using-jupyterlab-to-manage-password_22.html)]
* Previous CMIYC Tutorial (Part 3): [[Link](https://reusablesec.blogspot.com/2023/08/hashcat-tips-and-tricks-for-hacking.html)]
* Previous CMIYC Tutorial (Part 4): [[Link](https://reusablesec.blogspot.com/2023/11/jupyter-lab-framework-example.html)]

## Using The Framework:

The rest of this tutorial is really going to focus on using the Password Cracking Framework to help automate some of the tasks in the CMIYC contest. All the Pro teams have their own frameworks, so I developed this framework to be something anyone could use. The framework is written as a Python backend for a JupyterLab Notebook. Why JupyerLabs? Well I never want to write a GUI so JupyterLabs takes care of much of the frontend for me. Also, I've found the interactive shell into my Python backend to be very helpful when playing around with data.

You can download and install the framework from the link above. The real source of truth will be the **CMIYC\_2024\_Examples.ipynb** Notebook vs. this blog entry, as I will probably be making changes and updates to throughout the contest. While I won't be posting any contest hashes, I will likely update the Framework to handle file formats that Korelogic throws at the street teams. When you are using this Notebook, I'd recommend using the example one as a tutorial, but then creating your own Notebook to manage your own personal cracking sessions. That way you can arrange your Notebook the way that works best for you, and if I make changes to to the tutorial/example during the contest you don't have to worry about git merge conflicts.

For the rest of this blog entry I'm largely going to be referencing the Notebook, so I'd recommend taking the time to download and install it before continuting.

## Registering a Team:

Korelogic requires teams to perform all communications using PGP. For most people, this probaly means using the GNU PGP client. For me, GNU stands for "**G**oing to **N**ever **U**se it" since the tutorials and MAN pages are often horrible. So the first order of business for me getting ready for this year's CMIYC was to automate PGP key generation, encryption, and decryption using the Python library PGPy [[Link](https://pgpy.readthedocs.io/en/latest/examples.html)].

If you want to use a different PGP program to create a team, absolutely go ahead and do that! But in the Password Cracking Framework I created a Python class called **PGPMgr** that you can call through the Jupyter Notebook instead.

The first function is **generate\_read\_pgp\_private\_key**. This will create a new PGP key (if one does not already exit) and write it to the key\_file name that you send to it. If a PGP key already exists it'll validate the key and then return it. This way you aren't creating a new key every time this is run. Feel free to skip using this function if you already have a PGP key you want to use, but even the conference organizers recommend using a contest specific PGP key to make it easier to partner with other players. I'd also recommend backing up your key in case something happens during the contest. Here is the output of running it in the Notebook:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh05FfZeYvB6rPOv8vCBlgMmND1Z0v-o3_0P8w-Zv7AsKPGpg_QuTMxOdek5Yg0t_p8LuWhQqJqyOwlKjlG9kxz_J-RpVeN_60fYytgurb3zWcg1k1QGCg5aSLVq8ipf-2jzJhZiCrSHEycdSh15ke9v3b9lm6_HNFHBXtiyFohMMATftkF4t5MJiiaxNw/s16000/pgp_key.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh05FfZeYvB6rPOv8vCBlgMmND1Z0v-o3_0P8w-Zv7AsKPGpg_QuTMxOdek5Yg0t_p8LuWhQqJqyOwlKjlG9kxz_J-RpVeN_60fYytgurb3zWcg1k1QGCg5aSLVq8ipf-2jzJhZiCrSHEycdSh15ke9v3b9lm6_HNFHBXtiyFohMMATftkF4t5MJiiaxNw/s2000/pgp_key.png)

My apologies that it's a screenshot vs. text, but that's why it's probably easier to use this in the framework.

To encrypt/decrypt messages I then created the PGP\_Mgr class in the Framework. I figured a class would be better than having individual functions since I didn't want to have to keep passing in my private key as well as KoreLogic's public key.

While I could try to integrate this with individual e-mail services, that seems like a lot of work so PGP\_Mgr will output encrypted messages to this workbook as well as save the messages to a file. It'...