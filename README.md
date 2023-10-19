# Python User Interface Demos

This repository contains all example programs used during CS Crew meetings to show off Python user interface techniques.

## Installing Packages

UI projects typically have a lot of libraries that need to be imported. You can install these on your own, or you can use `pdm`, which is supported by this project.

When cloning into the repository, you can run `pdm install` to install the required dependencies.

> This requires that you have already installed `pdm`.

Once you have installed everything, you can enter the venv that `pdm` created. The command to do so should be:

```zsh
$(pdm venv activate)
```

This should allow you to run any of the python scripts using the packages that you've installed for the project, meaning that you didn't need to install them globally to use them. (Don't quote me on that)

You can also use the VSCode command palette to select the venv as the interpreter for the current workspace.
