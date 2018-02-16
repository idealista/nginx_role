![Logo](https://raw.githubusercontent.com/idealista/nginx-role/master/logo.gif)

[![Build Status](https://travis-ci.org/idealista/nginx-role.png)](https://travis-ci.org/idealista/nginx-role)

# Nginx Ansible role

This ansible role installs a Nginx server in a debian environment. The server is installed using the sources adding the headers-more module and lua module. Also installs [lua](http://www.lua.org/) needed for prometheus metrics.

- [Getting Started](#getting-started)
	- [Prerequisities](#prerequisities)
	- [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Contributing](#contributing)

## Getting Started

These instructions will get you a copy of the role for your ansible playbook. Once launched, it will install a [Nginx](http://nginx.org/) server in a Debian system.

### Prerequisities

Ansible 2.4.1.0 version installed.
Inventory destination should be a Debian environment.

For testing purposes, [Molecule](https://molecule.readthedocs.io/) with [Vagrant](https://www.vagrantup.com/) as driver (with [vagrant-hostmanager](https://github.com/devopsgroup-io/vagrant-hostmanager) plugin) and [VirtualBox](https://www.virtualbox.org/) as provider.

### Installing

Create or add to your roles dependency file (e.g requirements.yml):

```
- src: http://github.com/idealista/nginx-role.git
  scm: git
  version: 1.0.0
  name: nginx
```

Install the role with ansible-galaxy command:

```
ansible-galaxy install -p roles -r requirements.yml -f
```

Use in a playbook:

```
---
- hosts: someserver
  roles:
    - role: nginx
```

## Usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

You can add new servers to nginx by including your server as a file or as a template, setting the server
files in the path defined by `nginx_extra_servers_path` or  `nginx_extra_servers_template_path` (see tests as example).

If you want to change any version do it at your risk. Some nginx versions and modules are not compatible.
Known compatible versions are:

```
Nginx: 1.10.* + lua_module_version: 0.10.7
Nginx: 1.12.* + lua_module_version: 0.10.11

```

## Testing

```
molecule test --platform=Debian9
```

See molecule.yml to check possible testing platforms.

## Built With

![Ansible](https://img.shields.io/badge/ansible-2.4.1.0-green.svg)

## Versioning

For the versions available, see the [tags on this repository](https://github.com/idealista/nginx-role/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Authors

* **Idealista** - *Work with* - [idealista](https://github.com/idealista)

See also the list of [contributors](https://github.com/idealista/nginx-role/contributors) who participated in this project.

## License

![Apache 2.0 Licence](https://img.shields.io/hexpm/l/plug.svg)

This project is licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license - see the [LICENSE.txt](LICENSE.txt) file for details.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Acknowledgments

* [Anton Tolchanov](https://github.com/knyar/) - For the [prometheus metric library for Nginx](https://github.com/knyar/nginx-lua-prometheus)

* [Sophos](https://github.com/hnlq715/) - For the [metrics](https://github.com/hnlq715/nginx-prometheus-metrics/blob/master/metrics.vhost)
