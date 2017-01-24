# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased]

## [1.1.0](https://github.com/idealista-tech/nginx-role/tree/1.1.0) (2017-01-24)
[Full Changelog](https://github.com/idealista-tech/nginx-role/compare/1.0.2...1.1.0)

### Added
- *Add prometheus metric to monitor nginx server* @jmonterrubio

## [1.0.2](https://github.com/idealista-tech/nginx-role/tree/1.0.2) (2017-01-20)
[Full Changelog](https://github.com/idealista-tech/nginx-role/compare/1.0.1...1.0.2)
This version could break the service if same version is installed. Please use **force_reinstall: true** parameter to avoid it.

### Added
- *Create force_reinstall parameter* @jmonterrubio
### Added
- *Improve user service management* @jmonterrubio
### Fixed
- *[#1](https://github.com/idealista-tech/nginx-role/issues/1) Fix enable/disable service* @jmonterrubio

##[1.0.1](https://github.com/idealista-tech/nginx-role/tree/1.0.1) (2017-01-12)
[Full Changelog](https://github.com/idealista-tech/nginx-role/compare/1.0.0...1.0.1)
### Added
- *Update doc* @jmonterrubio

### Changed
- *[PLATFORM-221](http://jira.sys.idealista/browse/PLATFORM-221) Remove delaycompress in logrotate* @jmonterrubio

## [1.0.0](https://github.com/idealista-tech/nginx-role/tree/1.0.0)
### Added
- *First release*
