---
title: Stealing GitHub staff's access token via GitHub Actions
url: https://blog.ryotak.net/post/github-actions-staff-access-token-en/
source: RyotaK's Blog
date: 2023-04-23
fetch_date: 2025-10-04T11:32:08.092527
---

# Stealing GitHub staff's access token via GitHub Actions

[RyotaK's Blog](https://blog.ryotak.net/)
技術的な話とか

## [Stealing GitHub staff's access token via GitHub Actions](https://blog.ryotak.net/post/github-actions-staff-access-token-en/)

2023-04-22
 1227 字
 [GitHub](/tags/github) [Vulnerability](/tags/vulnerability) [GitHub Actions](/tags/github-actions) [Supply Chain](/tags/supply-chain)

(この記事は[日本語](/post/github-actions-staff-access-token/)でも読むことが出来ます。)

## Disclaimer

GitHub is running a bug bounty program on HackerOne, and as part of this program, vulnerability research is permitted by the [safe harbor](https://docs.github.com/en/site-policy/security-policies/github-bug-bounty-program-legal-safe-harbor).
This article describes a vulnerability that I discovered as a result of my investigation in compliance with the safe harbor criteria and is not intended to encourage unauthorized vulnerability research activities.
If you find a vulnerability on GitHub, please report it to [GitHub Bug Bounty](https://hackerone.com/github?type=team).

## TL;DR

In the [actions/runner](https://github.com/actions/runner) repository, which hosts the source code for the GitHub Actions runner, there was a flaw in the usage of the self-hosted runner, which allowed me to steal the Personal Access Token from GitHub Actions.
Since this token was tied to the GitHub staff account, I could perform various actions as a GitHub staff.
This potentially allowed the insertion of malicious code into repositories such as [actions/checkout](https://github.com/actions/checkout) and [actions/cache](https://github.com/actions/cache), which might affect many repositories that use GitHub Actions.

## About self-hosted runner

Self-hosted runner, as the name suggests, is a feature that allows users to run GitHub Actions runners on their own machines. It is mainly used in the CI where hardware requirements exist.
This feature is achieved by installing an Actions runner on the user’s machine. And this runner doesn’t isolate the environment for each execution, so the system state is shared among jobs unless the user isolates the environment separately. This behavior is not a security issue if only trusted workflows are executed.

## pull\_request trigger

However, there is a workflow trigger in GitHub Actions called `pull_request`.
This trigger gets executed when an event related to a pull request occurs. While starting the workflow, it reads the definition file of the workflow from the forked repository[1](#fn:1) and runs the workflow in the context of the base repository where the pull request was created, with a read-only token passed.
This means a forked repository can execute arbitrary workflows on GitHub Actions in a public repository. [2](#fn:2)

![A graph that shows the behavior of the pull_request trigger](/img/github-actions-pull-request-trigger-en.svg)

When using a runner hosted by GitHub, the environment is isolated for each workflow execution, so there is no problem with this behavior. However, in the case where the self-hosted runner is used, the environment isn’t isolated for each workflow execution. So, a malicious pull request can execute arbitrary code on the self-hosted runner and compromise the environment.
This allows a malicious pull request to steal sensitive information (e.g., a GitHub access token with write access) later when the compromised runner receives it.

[The GitHub documentation](https://docs.github.com/en/actions/hosting-your-own-runners/about-self-hosted-runners#self-hosted-runner-security) explicitly describes this behavior and states that self-hosted runners should not be used in public repositories.

## Vulnerable workflow

Now, let’s look at the actual workflow that was vulnerable to this attack.
In [actions/runner](https://github.com/actions/runner), a workflow for E2E test called [e2etest.yml](https://github.com/actions/runner/blob/a9be5f65578a8225c6a024799f572ad2066c4fd8/.github/workflows/e2etest.yml) exist.[3](#fn:3)

This workflow does the following steps:

1. Delete all registered self-hosted runners to clean up terminated workflow run.
2. Build runners for different architectures and operating systems (Linux/Windows/macOS).
3. Run a script that performs the following processes asynchronously:
   　1. Get a list of self-hosted runners currently registered in the repository.
   　2. From the list, find the runner that should be used for the E2E test and send the corresponding test job for the OS type on the runner.
   　3. If all tests are started, exit this process. Otherwise, continue the process.
   　4. Sleep for 10 seconds to avoid the API rate limit.
   　5. Return to step 3-1.
4. To start the self-hosted runner, perform the following steps for each architecture and OS type combination.
   　1. Download the executable file built in step 2.
   　2. Set up a self-hosted runner and register it to the actions/runner repository.
   　3. Wait for the job to be executed from the script started in step 3.
   　4. Execute the received job.
   　5. Remove the self-hosted runner from the actions/runner repository.
   　6. Upload test results.
5. After all tests are finished, analyze the uploaded test results.

At first glance, the attack described above seems impossible because the self-hosted runner is removed after running the test.
However, these steps contain a flaw, and executing arbitrary commands on the self-hosted runner was possible during the workflow execution.

## Problem of this workflow

In the above steps, remember that the script is executed asynchronously in step 3.
This script sleeps 10 seconds each time after retrieving the list of registered self-hosted runners to avoid getting rate limited.
In other words, there is a maximum delay of a little over 10 seconds from when the self-hosted runner is registered in step 4-2 until the job is executed for the runner in step 3-2.

As the `About self-hosted runner` section explains, a self-hosted runner can receive jobs executed from a pull request. By sending a malicious pull request during these 10 seconds, arbitrary commands can be executed on the self-hosted runner, and subsequent steps will be executed in the compromised runner.
Looking at the subsequent steps, we see that the self-hosted runner is removed from the actions/runner repository in steps 4-5.
Typically, the GitHub Token passed to the runner in GitHub Actions doesn’t have permission to register/delete the self-hosted runner, so they used GitHub’s Personal Access Token to register/delete the self-hosted runner, as shown below.

[.github/workflows/e2etest.yml line 165 - line 178](https://github.com/actions/runner/blob/a9be5f65578a8225c6a024799f572ad2066c4fd8/.github/workflows/e2etest.yml#L165-L178)

```
      - name: Configure Runner
        env:
          unique_runner_name: linux-x64-${{needs.init.outputs.unique_runner_label}}
        run: |
          ./config.sh --url ${{github.event.repository.html_url}} --unattended --name $unique_runner_name --pat ${{secrets.PAT}} --labels $unique_runner_name --replace
      - name: Start Runner and Wait for Job
        timeout-minutes: 5
        run: |
          ./run.sh --once
      - name: Remove Runner
        if: always()
        continue-on-error: true
        run: |
          ./config.sh remove --pat ${{secrets.PAT}}
```

Since the job is executed in the `Start Runner and Wait for Job` step, the subsequent `Remove Runner` step will be run in the compromised runner.
This means the `secrets.PAT` passed to the runner in `./config.sh remove --pat ${{secrets.PAT}}` can be stolen by sending a malicious pull request.

## Impact

And now, the question is who owns `secrets.PAT`.
Fortunately, this token was used in another place for the execution of the workflow, so it was easy to identify the token’s owner.

![Execution log of the workflow with the name of the executor redacted](/img/github-actions-runner-pat-owner.png)

So, I then checked the user profile and found that the user belongs to [@actions](https://github.com/actions) and [@github](https://github....