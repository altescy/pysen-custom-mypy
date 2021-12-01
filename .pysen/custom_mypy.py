import pathlib
from typing import Sequence

import dacite
from pysen.component import ComponentBase
from pysen.mypy import Mypy, MypySetting
from pysen.plugin import PluginBase
from pysen.pyproject_model import Config, PluginConfig


class CustomeMypy(PluginBase):
    def load(
        self,
        file_path: pathlib.Path,
        config_data: PluginConfig,
        root: Config,
    ) -> Sequence[ComponentBase]:
        lint_config = root.lint

        base_setting = (
            lint_config.mypy_preset.get_setting()
            if lint_config and lint_config.mypy_preset
            else MypySetting()
        )

        setting_dict = base_setting.asdict()
        setting_dict.update(**config_data.config or {})
        setting = dacite.from_dict(MypySetting, setting_dict)

        mypy_targets = lint_config.mypy_targets if lint_config else None

        component = Mypy(
            name="custom-mypy",
            setting=setting,
            mypy_targets=mypy_targets,
        )
        return [component]


def plugin() -> CustomeMypy:
    return CustomeMypy()
