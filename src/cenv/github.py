# ABOUTME: GitHub repository cloning functionality for cenv
# ABOUTME: Validates GitHub URLs and clones repositories using git subprocess
import subprocess
import shutil
from pathlib import Path
import re

def is_valid_github_url(url: str) -> bool:
    """Validate if URL is a valid GitHub repository URL"""
    patterns = [
        r"^https://github\.com/[\w-]+/[\w.-]+(\.git)?$",
        r"^git@github\.com:[\w-]+/[\w.-]+\.git$",
    ]

    return any(re.match(pattern, url) for pattern in patterns)

def clone_from_github(url: str, target: Path) -> None:
    """Clone a GitHub repository to target directory"""
    if not is_valid_github_url(url):
        raise ValueError(f"Invalid GitHub URL: {url}")

    # Create temporary directory for cloning
    temp_dir = target.parent / f".tmp_{target.name}"

    try:
        # Clone the repository
        result = subprocess.run(
            ["git", "clone", url, str(temp_dir)],
            capture_output=True,
            text=True,
            check=False,
        )

        if result.returncode != 0:
            raise RuntimeError(f"Failed to clone repository: {result.stderr}")

        # Remove .git directory if it exists
        git_dir = temp_dir / ".git"
        if git_dir.exists():
            shutil.rmtree(git_dir)

        # Move to final location
        if target.exists():
            shutil.rmtree(target)

        # Only move if temp_dir exists (for real git clone)
        if temp_dir.exists():
            shutil.move(str(temp_dir), str(target))

    except Exception as e:
        # Clean up temp directory if it exists
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        raise
