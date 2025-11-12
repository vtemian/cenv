import os
import pytest
from pathlib import Path
from cenv.config import load_config, Config, DEFAULT_GIT_TIMEOUT


def test_default_config():
    """Test that default config has sensible values"""
    config = Config()

    assert config.git_timeout > 0
    assert config.git_timeout == DEFAULT_GIT_TIMEOUT
    assert isinstance(config.trash_dir_name, str)


def test_config_from_environment_variables(monkeypatch):
    """Test loading config from environment variables"""
    monkeypatch.setenv("CENV_GIT_TIMEOUT", "600")
    monkeypatch.setenv("CENV_LOG_LEVEL", "DEBUG")

    config = load_config()

    assert config.git_timeout == 600


def test_invalid_config_values_use_defaults(monkeypatch):
    """Test that invalid values fall back to defaults"""
    monkeypatch.setenv("CENV_GIT_TIMEOUT", "invalid")

    config = load_config()

    # Should use default, not crash
    assert config.git_timeout == DEFAULT_GIT_TIMEOUT


def test_config_file_loading(tmp_path):
    """Test loading config from file"""
    config_file = tmp_path / ".cenvrc"
    config_file.write_text("""
git_timeout = 600
log_level = DEBUG
    """)

    config = load_config(config_file=config_file)

    assert config.git_timeout == 600
