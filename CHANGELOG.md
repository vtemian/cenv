# Changelog

All notable changes to cenv will be documented in this file.

## [0.1.0] - 2025-11-01

### Added
- Initial release of cenv
- Environment initialization (`cenv init`)
- Environment creation from default (`cenv create`)
- Environment creation from GitHub repos (`cenv create --from-repo`)
- Environment switching with safety checks (`cenv use`)
- Environment listing (`cenv list`)
- Current environment display (`cenv current`)
- Environment deletion with protection (`cenv delete`)
- Process detection for running Claude instances
- Automatic confirmation prompts when Claude is running
- Complete test coverage (unit + integration)
- Comprehensive documentation

### Features
- Symlink-based environment switching for speed
- Complete isolation between environments
- Shared credentials via macOS Keychain
- GitHub template support for team sharing
- Safety checks to prevent accidental data loss
