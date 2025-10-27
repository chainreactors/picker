---
title: Self-Contained TypeScript Programs Using Bun
url: https://danielmiessler.com/blog/executable-typescript-programs-using-bun
source: Daniel Miessler
date: 2025-07-28
fetch_date: 2025-10-06T23:27:28.248399
---

# Self-Contained TypeScript Programs Using Bun

[Daniel Miessler](https://danielmiessler.com)

Main Navigation [home](/)[blog](/blog/)[telos](/telos/)[ideas](/ideas/)[projects](/projects/)[predictions](/predictions/)[speaking](/speaking/)[about](/about/)

# Self-Contained TypeScript Programs Using Bun

How Bun's auto-install makes TypeScript even better than Python's uv

July 27, 2025

![Attempt-13](/images/Attempt-13.png)

Bun installing dependencies automatically

 If you hate Python as much as me it"s probably because of dependencies.

Roughly 23-319% of the time, when I run a Python app, it doesn't work because of dependencies, and I end up trying to figure out which of my 17 real and virtual Python environments are actually active.

Using `uv` for everything is way better, but since I'm kind of moving my entire programming world to TypeScript, I'm now using `bun`'s auto-install feature instead. And it's actually a bit better.

## Different Approaches, Same Goal [​](#different-approaches-same-goal)

Python's `uv` and Bun both solve the "self-contained app" problem by putting the requirements inside the program itself, but they do it in different ways...

### UV's Approach: Inline Comments (smuggling, basically) [​](#uv-s-approach-inline-comments-smuggling-basically)

Python uses special magical comments to declare dependencies:

python

```
# /// script
# dependencies = ["requests", "rich"]
# ///

import requests
# script continues...
```

1
2
3
4
5
6

It works great, but it feels super hack-y to me.

It feels like we're smuggling in a  dependency payload to trick Python into actually working for once.

### Bun's Approach: Just import it like normal [​](#bun-s-approach-just-import-it-like-normal)

I like `bun`'s approach *much* better. It just writes the imports out like it's not embarrassed by them!

typescript

```
#!/usr/bin/env bun

// Just import what you need - Bun auto-installs!
import axios from 'axios';
import chalk from 'chalk';

console.log(chalk.cyan.bold('\n🚀 Bun Auto-Install Demo\n'));

// Fetch a random joke
try {
  console.log(chalk.yellow('Getting a random joke...'));
  const jokeResponse = await axios.get('https://official-joke-api.appspot.com/random_joke');
  const joke = jokeResponse.data;
  console.log(chalk.green(`\n${joke.setup}`));
  console.log(chalk.blue(`${joke.punchline} 😄\n`));
} catch (error) {
  console.log(chalk.red('Failed to fetch joke\n'));
}
v// Fetch a random activity
try {
  console.log(chalk.yellow('Finding something to do...'));
  const activityResponse = await axios.get('https://bored-api.appbrewery.com/random');
  const activity = activityResponse.data;
  console.log(chalk.magenta(`Activity: ${activity.activity}`));
  console.log(chalk.dim(`Type: ${activity.type} | Participants: ${activity.participants}\n`));
} catch (error) {
  console.log(chalk.red('Failed to fetch activity\n'));
}

// Show a random number to prove it runs fresh
const randomNum = Math.floor(Math.random() * 1000);
console.log(chalk.green(`Random number: ${randomNum}`));

// Show that this runs fresh each time
console.log(chalk.dim('\nRun again for different results!'));
console.log(chalk.dim('No package.json or npm install needed 🎉\n'));
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36

## Running the Script [​](#running-the-script)

bash

```
# Make it executable
chmod +x test.ts

# Run it directly - dependencies auto-install!
./test.ts

# Or just use bun
bun test.ts
```

1
2
3
4
5
6
7
8

The first time you run the script, `bun` automatically:

1. Detects the missing packages
2. Downloads and installs them
3. Caches them for future runs
4. Executes your script

No `npm install`, no `package.json`, no setup—just run it.

## Example Output [​](#example-output)

```
🚀 Bun Auto-Install Demo

Getting a random joke...

Did you watch the new comic book movie?
It was very graphic! 😄

Finding something to do...
Activity: Explore a park you have never been to before
Type: recreational | Participants: 1

Random number: 294

Run again for different results!
No package.json or npm install needed 🎉
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15

Oh, and it's nuclear fast.

```
bun test.ts  0.08s user 0.06s system 29% cpu 0.469 total
```

1

## My takeaway [​](#my-takeaway)

This goes to a larger discussion around Python vs TypeScript, but I feel like this is another example where the latter is just a more natural, modern way of doing things.

*TypeScript all the things.*

#### Notes

1. Shoutout to Greg for getting me into the TypeScript cult.

Share

[Post](https://ul.live/share/x?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun "Share on X")  [LinkedIn](https://ul.live/share/linkedin?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun "Share on LinkedIn") [HN Hacker News](https://ul.live/share/hn?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun "Share on Hacker News")  [Reddit](https://ul.live/share/reddit?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun "Share on Reddit")  [Facebook](https://ul.live/share/facebook?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun "Share on Facebook")  [Forward](https://ul.live/share/email?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun "Share via Email")

Follow

[Get The Newsletter](https://ul.live/nlpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun)  [Follow On X](https://ul.live/xpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun)  [Subscribe On YouTube](https://ul.live/ytpostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun)  [Follow On LinkedIn](https://ul.live/lipostfooter?url=https%3A%2F%2Fdanielmiessler.com%2Fblog%2Fexecutable-typescript-programs-using-bun&title=Self-Contained%20TypeScript%20Programs%20Using%20Bun)

Search

[HOME](/)·[BLOG](/blog)·[ARCHIVES](/archives)·[ABOUT](/about)

© 1999 — 2025 Daniel Miessler. All rights reserved.