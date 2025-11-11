# Changelog

All notable changes to cenv will be documented in this file.

## [0.2.0] - 2025-11-11

### Added
- Custom exception hierarchy for better error handling and debugging
- Comprehensive logging infrastructure with file and console handlers
- CLI options: `--verbose` for detailed output, `--log-file` for persistent logs
- Trash mechanism with restore functionality for deleted environments
- `cenv trash` command to list deleted environments
- `cenv restore` command to recover environments from trash
- File locking to prevent race conditions during initialization
- Security documentation in docs/SECURITY.md
- Type checking with mypy in strict mode

### Security
- Git clone operations now have 5-minute timeout to prevent hanging
- Shallow clones (`--depth 1`) to minimize data transfer
- Custom GitOperationError for invalid GitHub URLs
- Atomic file operations with file locks

### Changed
- Replaced generic RuntimeError/ValueError with custom exceptions
- Enhanced error messages with specific exception types
- Updated documentation with security considerations

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
