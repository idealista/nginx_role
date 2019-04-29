# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/nginx_role/tree/develop)

### Fixed
- *[#59](https://github.com/idealista/nginx_role/issues/53) Fix reload command in service file* @jnogol

## [2.0.0](https://github.com/idealista/nginx_role/tree/2.0.0) (2019-02-18)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.8.0...2.0.0)

### Changed
- *[#53](https://github.com/idealista/nginx_role/issues/53) Rename role using underscore* @jmonterrubio
- *[#51](https://github.com/idealista/nginx_role/issues/51) Set 2.7 as min ansible version* @jmonterrubio
- *Use molecule 2 with docker as driver* @jmonterrubio
- *Set 1.14.2 as default nginx version* @jmonterrubio
- *Configurable nginx external modules* @jmonterrubio

## [1.8.0](https://github.com/idealista/nginx_role/tree/1.8.0) (2018-02-27)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.7.0...1.8.0)

### Added
- *[#46](https://github.com/idealista/nginx_role/issues/46) Added configurable limit no file* @javierRobledo, @danieljesus

### Changed
- *[#48](https://github.com/idealista/nginx_role/issues/48) Make logrotate optional* @jnogol

## [1.7.0](https://github.com/idealista/nginx_role/tree/1.7.0) (2018-02-23)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.6.0...1.7.0)

### Added
- *[#6](https://github.com/idealista/nginx_role/issues/6) Add Travis CI* @jnogol

### Changed
- *[#42](https://github.com/idealista/nginx_role/issues/42) Update Prometheus metrics* @jmonterrubio

### Fixed
- *[#43](https://github.com/idealista/nginx_role/issues/43) Notify reload handler when changing configuration* @jmonterrubio

## [1.6.0](https://github.com/idealista/nginx_role/tree/1.6.0) (2017-10-26)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.5.0...1.6.0)

### Added
- *[#32](https://github.com/idealista/nginx_role/issues/32) Support worker_rlimit_nofile setting* @acuervof

## [1.5.0](https://github.com/idealista/nginx_role/tree/1.5.0) (2017-06-30)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.4.0...1.5.0)

### Added
- *[#29](https://github.com/idealista/nginx_role/issues/29) Support debian stretch* @jmonterrubio

## [1.4.0](https://github.com/idealista/nginx_role/tree/1.4.0) (2017-05-03)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.3.1...1.4.0)

### Added
- *[#26](https://github.com/idealista/nginx_role/issues/26) Extracting compile-time options to variable* @dortegau

## [1.3.1](https://github.com/idealista/nginx_role/tree/1.3.1) (2017-03-27)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.3.0...1.3.1)

### Fixed
- *[#22](https://github.com/idealista/nginx_role/issues/22) Fix conflict in init scripts* @jmonterrubio

## [1.3.0](https://github.com/idealista/nginx_role/tree/1.3.0) (2017-03-25)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.2.2...1.3.0)

### Added
- *[#19](https://github.com/idealista/nginx_role/issues/19) Prometheus metrics customization* @sorobon

## [1.2.2](https://github.com/idealista/nginx_role/tree/1.2.2) (2017-03-17)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.2.1...1.2.2)

### Added
- *[#16](https://github.com/idealista/nginx_role/issues/16) Fix pid error* @jmonterrubio

## [1.2.1](https://github.com/idealista/nginx_role/tree/1.2.1) (2017-03-17)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.2.0...1.2.1)

### Added
- *[#13](https://github.com/idealista/nginx_role/issues/13) Force pid directory* @jmonterrubio

## [1.2.0](https://github.com/idealista/nginx_role/tree/1.2.0) (2017-02-27)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.1.0...1.2.0)

### Added
- *[#7](https://github.com/idealista/nginx_role/issues/7) Configure servers from files out of the role* @jmonterrubio

### Added
- *[#9](https://github.com/idealista/nginx_role/issues/9) Add max body size configurable* @jmonterrubio

## [1.1.0](https://github.com/idealista/nginx_role/tree/1.1.0) (2017-01-24)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.0.2...1.1.0)

### Added
- *Add prometheus metric to monitor nginx server* @jmonterrubio

## [1.0.2](https://github.com/idealista/nginx_role/tree/1.0.2) (2017-01-20)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.0.1...1.0.2)
This version could break the service if same version is installed. Please use **force_reinstall: true** parameter to avoid it.

### Added
- *Create force_reinstall parameter* @jmonterrubio
### Added
- *Improve user service management* @jmonterrubio
### Fixed
- *[#1](https://github.com/idealista/nginx_role/issues/1) Fix enable/disable service* @jmonterrubio

##[1.0.1](https://github.com/idealista/nginx_role/tree/1.0.1) (2017-01-12)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.0.0...1.0.1)
### Added
- *Update doc* @jmonterrubio

### Changed
- *[PLATFORM-221](http://jira.sys.idealista/browse/PLATFORM-221) Remove delaycompress in logrotate* @jmonterrubio

## [1.0.0](https://github.com/idealista/nginx_role/tree/1.0.0)
### Added
- *First release*
