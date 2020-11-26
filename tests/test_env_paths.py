import os
import platform
import pytest
from env_paths import env_paths


if platform.system() == "Linux" or platform.system() == "Darwin":

    def test_default():
        name = "unicorn"
        paths = env_paths(name)
        for key, value in paths.items():
            assert value.endswith(f"{name}-python")

    def test_custom_suffix():
        name = "unicorn"
        opts = {"suffix": "horn"}
        paths = env_paths(name, opts)
        assert paths["data"].endswith(f"{name}-{opts['suffix']}")

    def test_no_suffix():
        name = "unicorn"
        opts = {"suffix": False}
        paths = env_paths(name, opts)
        assert paths["data"].endswith(name)


if platform.system() == "Linux":

    def test_linux():
        """correct paths with XDG_*_HOME set"""
        env_vars = {
            "data": "XDG_DATA_HOME",
            "config": "XDG_CONFIG_HOME",
            "cache": "XDG_CACHE_HOME",
            "log": "XDG_STATE_HOME",
        }
        for env in env_vars.values():
            os.environ[env] = f"tmp/{env}"
        name = "unicorn"
        paths = env_paths(name)
        for env in env_vars.keys():
            expected_path = os.getenv(env_vars[env])
            assert paths[env].startswith(expected_path)
            assert paths[env].endswith(f"{name}-python")
