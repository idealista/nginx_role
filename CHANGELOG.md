# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a changelog](https://github.com/olivierlacan/keep-a-changelog).

## [Unreleased](https://github.com/idealista/nginx_role/tree/develop)

## [5.0.0](https://github.com/idealista/nginx_role/tree/5.0.0) (2022-11-02)
### Added
- *[#114](https://github.com/idealista/nginx_role/issues/114) Updated nginx.conf template adding proxy buffer vars* @frantsao
- *[#114](https://github.com/idealista/nginx_role/issues/114) BREAKING revert proxy buffering defaults to <2.0 release. They are safer in general, but suboptimal (see Nginx documentation)* @frantsao
- *[#114](https://github.com/idealista/nginx_role/issues/114) fix files and directories permissions; RENAMED luaJIT_ variables to nginx_luajit_ because naming compliance (BREAKING) * @frantsao

## [4.2.1](https://github.com/idealista/nginx_role/tree/4.2.1) (2022-09-01)
[Full Changelog](https://github.com/idealista/nginx_role/compare/4.2.0...4.2.1)
### Fixed
- *[#111](https://github.com/idealista/nginx_role/issues/111) Fixed deletion of old server files configuration* @xtianae7

## [4.2.0](https://github.com/idealista/nginx_role/tree/4.2.0) (2022-06-22)
[Full Changelog](https://github.com/idealista/nginx_role/compare/4.1.0...4.2.0)
### Added
- *[#108](https://github.com/idealista/nginx_role/issues/108) Added support for ssl module* @xtianae7

## [4.1.0](https://github.com/idealista/nginx_role/tree/4.1.0) (2022-03-23)
[Full Changelog](https://github.com/idealista/nginx_role/compare/4.0.0...4.1.0)
### Changed
- *[#105](https://github.com/idealista/nginx_role/issues/105) Updated nginx.conf template adding server_tokens var* @frantsao
- *[#105](https://github.com/idealista/nginx_role/issues/105) Updated test dependencies* @frantsao

## [4.0.0](https://github.com/idealista/nginx_role/tree/4.0.0) (2021-11-26)
[Full Changelog](https://github.com/idealista/nginx_role/compare/3.5.2...4.0.0)
### Added
- *[#101](https://github.com/idealista/nginx_role/issues/101) Debian 11 support* @sorobon
### Removed
- *[#101](https://github.com/idealista/nginx_role/issues/101)Debian 8 (jessie) support* @sorobon

## [3.5.2](https://github.com/idealista/nginx_role/tree/3.5.2) (2021-07-29)
[Full Changelog](https://github.com/idealista/nginx_role/compare/3.5.1...3.5.2)
### Fixed
- *[#98](https://github.com/idealista/nginx_role/issues/98) Fix nginx_group not set as primary group* @caldito

## [3.5.1](https://github.com/idealista/nginx_role/tree/3.5.1) (2021-03-01)
[Full Changelog](https://github.com/idealista/nginx_role/compare/3.5.0...3.5.1)
### Fixed
- *[#91](https://github.com/idealista/nginx_role/issues/91) Fix nginx.conf template and molecule tests* @ftsao

## [3.5.0](https://github.com/idealista/nginx_role/tree/3.5.0) (2021-02-26)
[Full Changelog](https://github.com/idealista/nginx_role/compare/3.4.0...3.5.0)
### Added
- *[#88](https://github.com/idealista/nginx_role/issues/88) Add default server_names_hash_bucket_size* @ftsao
- *[#88](https://github.com/idealista/nginx_role/issues/88) Updated test requirements* @ftsao
- *[#88](https://github.com/idealista/nginx_role/issues/88) Added apt cache validation time* @ftsao

[Full Changelog](https://github.com/idealista/nginx_role/compare/3.3.0...3.4.0)
## [3.4.0](https://github.com/idealista/nginx_role/tree/3.4.0) (2020-12-21)
### Added
- *[#85](https://github.com/idealista/nginx_role/issues/85) Use get_url instead of unarchive to have timeout configuration* @jperera

[Full Changelog](https://github.com/idealista/nginx_role/compare/3.2.0...3.3.0)
## [3.3.0](https://github.com/idealista/nginx_role/tree/3.3.0) (2020-09-17)
### Added
- *[#81](https://github.com/idealista/nginx_role/issues/81) Support provide custom prometheus.conf metrics file* @jmonterrubio

## [3.2.0](https://github.com/idealista/nginx_role/tree/3.2.0) (2020-08-26)
[Full Changelog](https://github.com/idealista/nginx_role/compare/3.1.0...3.2.0)
### Changed
- *[#78](https://github.com/idealista/nginx_role/issues/78) parametrizing private tmp var to solve Debian 10 compatibilities* @gabyalises

## [3.1.0](https://github.com/idealista/nginx_role/tree/3.1.0) (2020-06-24)
[Full Changelog](https://github.com/idealista/nginx_role/compare/3.0.0...3.1.0)
### Changed
- *[#56](https://github.com/idealista/nginx_role/issues/56) Added ca-certificates; relocated vars* @frantsao
- *[#74](https://github.com/idealista/nginx_role/issues/74) Minor cleanup for debian buster; upgraded to molecule 3 and gos 0.13* @frantsao

## [3.0.0](https://github.com/idealista/nginx_role/tree/3.0.0) (2020-04-14)
[Full Changelog](https://github.com/idealista/nginx_role/compare/2.2.0...3.0.0)
### Added
- *[#70](https://github.com/idealista/nginx_role/issues/70) Support metrics for debian buster* @jmonterrubio

## [2.2.0](https://github.com/idealista/nginx_role/tree/2.2.0) (2020-01-24)
[Full Changelog](https://github.com/idealista/nginx_role/compare/2.1.1...2.2.0)
### Added
- *Add system:true on create nginx_user to get UID on system range* @adrian-arapiles
- *Add goss test to check nginx_user UId have system range of uids* @adrian-arapiles
### Fixed
- *Fix indent for goss http test of nginx metrics prometheus* @adrian-arapiles
- *[#57](https://github.com/idealista/nginx_role/issues/57) Disable create home for user nginx.*

## [2.1.1](https://github.com/idealista/nginx_role/tree/2.1.1) (2019-10-19)
[Full Changelog](https://github.com/idealista/nginx_role/compare/2.1.0...2.1.1)
### Fixed
- *[#65](https://github.com/idealista/nginx_role/issues/65) No value passed error in prometheus metrics* @jmonterrubio

## [2.1.0](https://github.com/idealista/nginx_role/tree/2.1.0) (2019-09-09)
[Full Changelog](https://github.com/idealista/nginx_role/compare/2.0.1...2.1.0)
### Fixed
- *[#62](https://github.com/idealista/nginx_role/issues/62) Fix wrong configuration of proxy_buffer_size in nginx.conf* @adrian-arapiles
### Added
- *[#62](https://github.com/idealista/nginx_role/issues/62) nginx.conf template can be override on playbook* @adrian-arapiles

## [2.0.1](https://github.com/idealista/nginx_role/tree/2.0.1) (2019-04-29)
[Full Changelog](https://github.com/idealista/nginx_role/compare/2.0.0...2.0.1)
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

## [1.0.1](https://github.com/idealista/nginx_role/tree/1.0.1) (2017-01-12)
[Full Changelog](https://github.com/idealista/nginx_role/compare/1.0.0...1.0.1)
### Added
- *Update doc* @jmonterrubio

### Changed
- *[PLATFORM-221](http://jira.sys.idealista/browse/PLATFORM-221) Remove delaycompress in logrotate* @jmonterrubio

## [1.0.0](https://github.com/idealista/nginx_role/tree/1.0.0)
### Added
- *First release*
