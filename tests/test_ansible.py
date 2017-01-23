import pytest


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]


def test_nginx_user(User, Group, AnsibleDefaults):
    assert User(AnsibleDefaults["nginx_user"]).exists
    assert Group(AnsibleDefaults["nginx_group"]).exists
    assert User(AnsibleDefaults["nginx_user"]).group == AnsibleDefaults["nginx_group"]


def test_nginx_conf(File, User, Group, AnsibleDefaults):
    conf_dir = File(AnsibleDefaults["nginx_conf_path"])
    assert conf_dir.exists
    assert conf_dir.is_directory
    assert conf_dir.user == AnsibleDefaults["nginx_user"]
    assert conf_dir.group == AnsibleDefaults["nginx_group"]


def test_nginx_log(File, User, Group, AnsibleDefaults):
    log_dir = File(AnsibleDefaults["nginx_log_path"])
    assert log_dir.exists
    assert log_dir.is_directory
    assert log_dir.user == AnsibleDefaults["nginx_user"]
    assert log_dir.group == AnsibleDefaults["nginx_group"]


def test_nginx_pid(File, User, Group, AnsibleDefaults):
    pid_dir = File(AnsibleDefaults["nginx_pid_path"])
    assert pid_dir.exists
    assert pid_dir.is_directory
    assert pid_dir.user == AnsibleDefaults["nginx_user"]
    assert pid_dir.group == AnsibleDefaults["nginx_group"]


def test_nginx_executable(File, Command, AnsibleDefaults):
    nginx = File(AnsibleDefaults["nginx_install_bin_path"] + "/sbin/nginx")
    assert nginx.exists
    assert nginx.is_file
    assert nginx.user == "root"
    assert nginx.group == "root"
    nginx_version = Command("sudo nginx -v")
    assert nginx_version.rc is 0
    assert "nginx version: nginx/" + AnsibleDefaults["nginx_version"] in nginx_version.stderr


def test_nginx_service(File, Service, Socket, AnsibleDefaults):
    assert File("/lib/systemd/system/nginx.service").exists
