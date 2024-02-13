# README

## Overview

The `formatted_yaml` template handler enhances Sceptre's built-in `File` handler by delivering YAML output that is not only rendered but also reformatted according to an opinionated style aimed at improving readability. This feature is particularly useful for templates that utilize Jinja interpolation, which often introduces unwanted whitespace into the rendered output. By employing the `formatted_yaml` handler, Sceptre users can ensure that their YAML configurations are visually appealing both in the Jinja source code and in the generated output and without spending time navigating Jinja's whitespace management features.

## Installation

Installation instructions

To install directly from PyPI
```shell
pip install sceptre-formatted-yaml-handler
```

To install from the git repo
```shell
pip install git+https://github.com/Sceptre/sceptre-formatted-yaml-handler.git
```

## Usage/Examples

Refer to the
[Sceptre template handler docs](https://docs.sceptre-project.org/latest/docs/hooks.html#hook-points)
for more information.

```yaml
template:
  type: formatted_yaml
```
