import argparse
import pathlib
from typing import Dict, List, Optional, Sequence

from pysen import dumper
from pysen.component import ComponentBase
from pysen.manifest import (
    ComponentName,
    ManifestBase,
    TargetName,
    TargetType,
    export_settings,
    get_target,
    get_targets,
)
from pysen.runner_options import PathContext, RunOptions


class CustomManifest(ManifestBase):
    def __init__(self, components: Sequence[ComponentBase]) -> None:
        self._components = components

    def _get_components(self) -> Sequence[ComponentBase]:
        return [c for c in self._components if c.name != "mypy"]

    def export_settings(self, paths: PathContext, args: argparse.Namespace) -> None:
        export_settings(paths, self._components, dumper.dump)

    def get_targets(self, args: argparse.Namespace) -> Dict[str, List[ComponentName]]:
        return get_targets(self._get_components())

    def get_target(
        self,
        target: TargetName,
        paths: PathContext,
        options: RunOptions,
        args: argparse.Namespace,
    ) -> TargetType:
        return get_target(target, self._get_components(), paths, options)


def build(
    components: Sequence[ComponentBase], src_path: Optional[pathlib.Path]
) -> ManifestBase:
    return CustomManifest(components)
