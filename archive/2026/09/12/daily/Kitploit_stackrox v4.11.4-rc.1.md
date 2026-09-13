---
title: stackrox v4.11.4-rc.1
url: https://kitploit.com/en/posts/github-stackrox-stackrox-4114-rc1
source: Kitploit
date: 2026-09-12
fetch_date: 2026-09-13T07:01:31.292676
---

# stackrox v4.11.4-rc.1

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/5209/a1f738b57356949c6d7fd0b304e484f553b3337b06567ba66cd12c543b07baa4.png)

New releaseSep 12, 2026

# stackrox v4.11.4-rc.1

The StackRox Kubernetes Security Platform performs a risk analysis of the container environment, delivers visibility and runtime alerts, and provides recommendations to proactively improve security by hardening the environment.

Share

## Table of Contents

* [StackRox Kubernetes Security Platform](#stackrox-kubernetes-security-platform)
  + [Table of Contents](#table-of-contents)
  + [Community](#community)
  + [Deploying StackRox](#deploying-stackrox)
    - [Quick Installation using Helm](#quick-installation-using-helm)
    - [Manual Installation using Helm](#manual-installation-using-helm)
    - [Installation using the Operator](#installation-using-the-operator)
    - [Installation via Scripts](#installation-via-scripts)
      * [Kubernetes Distributions (EKS, AKS, GKE)](#kubernetes-distributions-eks-aks-gke)
      * [OpenShift](#openshift)
      * [Docker Desktop, Colima, or minikube](#docker-desktop-colima-or-minikube)
    - [Accessing the StackRox User Interface (UI)](#accessing-the-stackrox-user-interface-ui)
  + [Development](#development)
    - [Quickstart](#quickstart)
      * [Build Tooling](#build-tooling)
      * [Clone StackRox](#clone-stackrox)
      * [Local Development](#local-development)
      * [Common Makefile Targets](#common-makefile-targets)
      * [Productivity](#productivity)
      * [GoLand Configuration](#goland-configuration)
      * [Running sql\_integration tests](#running-sql_integration-tests)
      * [Debugging](#debugging)
  + [Generating Portable Installers](#generating-portable-installers)
  + [Dependencies and Recommendations for Running StackRox](#dependencies-and-recommendations-for-running-stackrox)

---

# StackRox Kubernetes Security Platform

The StackRox Kubernetes Security Platform performs a risk analysis of the
container environment, delivers visibility and runtime alerts, and provides
recommendations to proactively improve security by hardening the environment.
StackRox integrates with every stage of container lifecycle: build, deploy and
runtime.

The StackRox Kubernetes Security platform is built on the foundation of
the product formerly known as Prevent, which itself was called Mitigate and
Apollo. You may find references to these previous names in code or
documentation.

---

## Community

You can reach out to us through [Slack](https://cloud-native.slack.com/archives/C01TDE3GK0E) (#stackrox).
For alternative ways, stop by our Community Hub [stackrox.io](https://www.stackrox.io/).

For event updates, blogs and other resources follow the StackRox community site at [stackrox.io](https://www.stackrox.io/).

For the StackRox [Code of Conduct](https://www.stackrox.io/code-conduct/).

To [report a vulnerability or bug](https://github.com/stackrox/stackrox/security/policy).

---

## Deploying StackRox

### Installation using the Operator

As of release 4.10 it's possible to [install StackRox using the operator](https://github.com/stackrox/stackrox/blob/master/operator/install).

> [!WARNING]
> The following installation methods are deprecated.

### Quick Installation using Helm

StackRox offers quick installation via Helm Charts. Follow the [Helm Installation Guide](https://helm.sh/docs/intro/install/) to get `helm` CLI on your system.
Then run the helm quick installation script or proceed to section [Manual Installation using Helm](#manual-installation-using-helm) for configuration options.

Install StackRox via Helm Installation Script

root@kitploit:~

```
/bin/bash <(curl -fsSL https://raw.githubusercontent.com/stackrox/stackrox/master/scripts/quick-helm-install.sh)
```

A default deployment of StackRox has certain CPU and memory requests and may fail on small (e.g. development) clusters if sufficient resources are not available. You may use the `--small` command-line option in order to install StackRox on smaller clusters with limited resources. Using this option is not recommended for production deployments.

root@kitploit:~

```
/bin/bash <(curl -fsSL https://raw.githubusercontent.com/stackrox/stackrox/master/scripts/quick-helm-install.sh) --small
```

The script adds the StackRox helm repository, generates an admin password, installs stackrox-central-services, creates an init bundle for provisioning stackrox-secured-cluster-services, and finally installs stackrox-secured-cluster-services on the same cluster.

Finally, the script will automatically open the browser and log you into StackRox. A certificate warning may be displayed since the certificate is self-signed. See the [Accessing the StackRox User Interface (UI)](#accessing-the-stackrox-user-interface-ui) section to read more about the warnings. After authenticating you can access the dashboard using <https://localhost:8000/main/dashboard>.

### Manual Installation using Helm

Follow the [Helm Installation Guide](https://helm.sh/docs/intro/install/) to get the `helm` CLI on your system.

Deploying using Helm consists of 4 steps

1. Add the StackRox repository to Helm
2. Launch **StackRox Central Services** using helm
3. Create a cluster configuration and a service identity (init bundle)
4. Deploy the **StackRox Secured Cluster Services** using that configuration and those credentials (this step can be done multiple times to add more clusters to the StackRox Central Service)

Install StackRox Central Services

First, the StackRox Central Services will be added to your Kubernetes cluster. This includes the UI and Scanner. To start, add the [stackrox/helm-charts/opensource](https://github.com/stackrox/helm-charts/tree/main/opensource) repository to Helm.

root@kitploit:~

```
helm repo add stackrox https://raw.githubusercontent.com/stackrox/helm-charts/main/opensource/
```

To see all available Helm charts in the repo run (you may add the option `--devel` to show non-release builds as well)

root@kitploit:~

```
helm search repo stackrox
```

To install stackrox-central-services, you will need a secure password. This password will be needed later for UI login and when creating an init bundle.

root@kitploit:~

```
ROX_ADMIN_PASSWORD="$(openssl rand -base64 20 | tr -d '/=+')"
```

From here, you can install stackrox-central-services to get Central and Scanner components deployed on your cluster.

> **Note:**
> You need only one deployed instance of stackrox-central-services even if you plan to secure multiple clusters.

To perform the installation, choose one of the following commands depending on your cluster size.

#### Default Central Installation

If you're installing in a reasonably sized cluster, use the default installation command:

root@kitploit:~

```
helm upgrade --install -n stackrox --create-namespace stackrox-central-services \
  stackrox/stackrox-central-services \
  --set central.adminPassword.value="${ROX_ADMIN_PASSWORD}" \
  --set central.persistence.none="true"
```

#### Central Installation in Clusters With Limited Resources

If you're installing in a single node cluster, or the default installation results in pods stuck pending due to lack of resources, use the following command instead to reduce stackrox-central-services resource requirements. Keep in mind that these reduced resource settings are not suited for a production setup.

root@kitploit:~

```
helm upgrade --install -n stackrox --create-namespace stackrox-central-services \
  stackrox/stackrox-central-services \
  --set central.adminPassword.value="${ROX_ADMIN_PASSWORD}" \
  --set central.persistence.none="true" \
  --set central.resources.reque...