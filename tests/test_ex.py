import os
import re
import platform
import pytest
from env_paths import data_dir, config_dir, cache_dir, log_dir, temp_dir


def test_temp_dir():
    name = "unicorn"
    temp_directory = temp_dir(name)
    assert os.path.isabs(temp_directory)


if platform.system() == "Windows":

    def test_data_dir():
        name = "unicorn"
        opts = {"suffix": "horn"}
        data_directory = data_dir(name, opts)
        assert data_directory.startswith("C:\\Users\\")
        assert data_directory.endswith("\\AppData\\Local\\unicorn-horn\\Data")

    def test_config_dir():
        name = "unicorn"
        opts = {"suffix": "horn"}
        config_directory = config_dir(name, opts)
        assert config_directory.startswith("C:\\Users\\")
        assert config_directory.endswith("\\AppData\\Roaming\\unicorn-horn\\Config")
        # C:\\Users\\runneradmin\\AppData\\Roaming\\unicorn-horn\\Config

    def test_cache_dir():
        name = "unicorn"
        opts = {"suffix": "horn"}
        cache_directory = cache_dir(name, opts)
        assert cache_directory.startswith("C:\\Users\\")
        assert cache_directory.endswith("\\AppData\\Local\\unicorn-horn\\Cache")
        # C:\\Users\\runneradmin\\AppData\\Local\\unicorn-horn\\Cache

    def test_log_dir():
        name = "unicorn"
        opts = {"suffix": "horn"}
        log_directory = log_dir(name, opts)
        assert log_directory.startswith("C:\\Users\\")
        assert log_directory.endswith("\\AppData\\Local\\unicorn-horn\\Log")
        # C:\\Users\\runneradmin\\AppData\\Local\\unicorn-horn\\Log


if platform.system() == "Darwin":

    def test_data_dir():
        name = "unicorn"
        opts = {"suffix": "horn"}
        data_directory = data_dir(name, opts)
        assert data_directory.startswith("/Users/")
        assert data_directory.endswith("/Library/Application Support/unicorn-horn")

    def test_config_dir():
        name = "unicorn"
        opts = {"suffix": "horn"}
        config_directory = config_dir(name, opts)
        print(config_directory)
        assert config_directory.startswith("/Users/")
        assert config_directory.endswith("/Library/Preferences/unicorn-horn")

    def test_cache_dir():
        name = "unicorn"
        opts = {"suffix": "horn"}
        cache_directory = cache_dir(name, opts)
        assert cache_directory.startswith("/Users/")
        assert cache_directory.endswith("/Library/Cache/unicorn-horn")

    def test_log_dir():
        name = "unicorn"
        opts = {"suffix": "horn"}
        log_directory = log_dir(name, opts)
        assert log_directory.startswith("/Users/")
        assert log_directory.endswith("/Library/Log/unicorn-horn")
