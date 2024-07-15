# 1. Launch Codespaces

This repository is configured with a [dev container](https://containers.dev) that provides a pre-defined development environment that can be activated with one command or click.

## 1.1 Fork the Repo

Before you get started, fork this repo to your own profile. This gives you a personal copy that you can use for exploration and extensions.

## 1.2 Launch GitHub Codespaces
The recommended approach is to activate this dev container using GitHub Codespaces.

1. Fork this workshop repo to your own profile.
1. Open the forked repo page in your browser.
1. Open the Code dropdown, select Codespacces tab.

Then click _create new codespace_ to get a mew Codespace launched in a new tab, right in your browser.

## 1.3 Launch Docker Desktop

GitHub Codespaces has a free usage tier for personal acccounts that is sufficient for this workshop. However, if you prefer to work in your local device (offline) or have insufficient Codespaces quota - then **Docker Desktop** is a viable option for running dev containers in your local device.

To take this approach:
1. Install Docker Desktop if not aalready installed.
1. Start Docker Desktop & verify it is running.

Now, you're ready to launch dev containers locally:
1. Clone the forked repo to your local device
1. Open the cloned repo in VS Code
1. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension if not  installed.

If the extension is active, it should prompt you to re-open the repo in a local container - **simply confirm the action**.

Alternatively, you can trigger the action manually in two ways:
- Via the **Command Palette** - Click (Ctrl+Shift+P), search for `Dev Containers:` and pick the `Reopen in Container` option.
- Via the **Status Bar** - Click the green icon at the bottom left corner of the VS Code window and select the `Reopen in Container` option from the dropdown.

## 1.4 Explore Codebase

At this point, you should have a Visual Studio Code editor open to your codebase, running in a container pre-configured with all required tools and dependencies.

---

**Next**: Let's Deploy Some Models!