import pytest
import urllib2


@pytest.fixture()
def AnsibleDefaults(Ansible):
    return Ansible("include_vars", "defaults/main.yml")["ansible_facts"]


@pytest.fixture()
def AnsibleVars(Ansible):
    return Ansible("include_vars", "tests/group_vars/group01.yml")["ansible_facts"]


@pytest.fixture()
def Hostname(TestinfraBackend):
    return TestinfraBackend.get_hostname()


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
    pid_dir = File("/run/nginx")
    assert pid_dir.exists
    assert pid_dir.is_directory
    assert pid_dir.user == "root"
    assert pid_dir.group == "root"


def test_nginx_executable(File, Command, AnsibleDefaults):
    nginx = File(AnsibleDefaults["nginx_install_bin_path"] + "/sbin/nginx")
    assert nginx.exists
    assert nginx.is_file
    assert nginx.user == "root"
    assert nginx.group == "root"
    nginx_version = Command("sudo nginx -v")
    assert nginx_version.rc is 0
    assert "nginx version: nginx/" + AnsibleDefaults["nginx_version"] in nginx_version.stderr


def test_nginx_service(File, Service, Socket, AnsibleVars):
    web2_port = AnsibleVars["web2_port"]
    assert File("/lib/systemd/system/nginx.service").exists
    assert Service("nginx").is_enabled
    assert Service("nginx").is_running
    assert Socket("tcp://0.0.0.0:9999").is_listening
    assert Socket("tcp://0.0.0.0:{0}".format(web2_port)).is_listening


def test_nginx_prometheus_service(File, Service, Socket, AnsibleVars, Hostname):
    if Hostname in ("nginx"):
        metrics_port = AnsibleVars["nginx_prometheus_metrics_port"]
        metrics_path = AnsibleVars["nginx_prometheus_metrics_path"]
        assert File("/lib/systemd/system/nginx.service").exists
        assert Service("nginx").is_enabled
        assert Service("nginx").is_running
        assert Socket("tcp://0.0.0.0:9999").is_listening
        assert File("/etc/nginx/sites-available/prometheus").exists
        assert File("/etc/nginx/sites-enabled/prometheus").exists
        assert File("/etc/nginx/extra-conf/prometheus.conf").exists
        assert Socket("tcp://0.0.0.0:{0}".format(metrics_port)).is_listening
        assert 200 == urllib2.urlopen('http://{0}:{1}/{2}'.format(Hostname, metrics_port, metrics_path)).getcode()


def test_nginx_not_has_prometheus_service(File, Service, Socket, AnsibleVars, Hostname):
    if Hostname == "nginx2":
        metrics_port = AnsibleVars["nginx_prometheus_metrics_port"]
        assert File("/lib/systemd/system/nginx.service").exists
        assert Service("nginx").is_enabled
        assert Service("nginx").is_running
        assert Socket("tcp://0.0.0.0:9999").is_listening
        prometheusSiteFile = File("/etc/nginx/sites-available/prometheus")
        assert not prometheusSiteFile.exists
        prometheusSiteFile = File("/etc/nginx/sites-enabled/prometheus")
        assert not prometheusSiteFile.exists
        prometheusConfFile = File("/etc/nginx/extra-conf/prometheus.conf")
        assert not prometheusConfFile.exists
        metricSocket = Socket("tcp://0.0.0.0:{0}".format(metrics_port))
        assert not metricSocket.is_listening
