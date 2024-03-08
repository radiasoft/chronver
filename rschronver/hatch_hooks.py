"""Chronological version hooks for hatchling builds

:copyright: Copyright (c) 2024 RadiaSoft LLC.  All Rights Reserved.
:license: http://www.apache.org/licenses/LICENSE-2.0.html
"""
import hatchling.builders.hooks.plugin.interface
import hatchling.plugin
import hatchling.version.source.plugin.interface
import os.path
import rschronver.git


_PLUGIN_NAME = "rschronver"


@hatchling.plugin.hookimpl
def hatch_register_build_hook():
    return RSChronVerBuildHook


@hatchling.plugin.hookimpl
def hatch_register_version_source():
    return RSChronVerVersionSource


class RSChronVerBuildHook(hatchling.builders.hooks.plugin.interface.BuildHookInterface):

    PLUGIN_NAME = _PLUGIN_NAME

    def initialize(self, version, build_data):
        p = f"_{self.PLUGIN_NAME}.py"
        with open(os.path.join(self.root, p), "wt") as f:
            f.write(f'__version__ = "{self.metadata.version}"\n')
        build_data["artifacts"].append(f"/{p}")


class RSChronVerVersionSource(
    hatchling.version.source.plugin.interface.VersionSourceInterface
):
    PLUGIN_NAME = _PLUGIN_NAME

    def get_version_data(self):
        """Get a chronological version from git or current date time

        Returns:
            dict: key "version" and value "yyyymmdd.hhmmss"
        """
        return {"version": rschronver.git.version()}
