# Pysen Custom Mypy

This repository provies an example of [pysen](https://github.com/pfnet/pysen) configuration with custom mypy setting.

You can overwrite mypy setting like below:

```pyproject.toml
# pyproject.toml
[tool.pysen.plugin.custom_mypy.config]
check_untyped_defs = false
```
