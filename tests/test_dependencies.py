import subprocess


def test_requests_not_imported_in_codebase():
    """Verify requests is not used anywhere in the codebase"""
    result = subprocess.run(
        ["grep", "-r", "import requests", "src/"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0, "requests should not be imported"

    result = subprocess.run(
        ["grep", "-r", "from requests", "src/"],
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0, "requests should not be imported"
