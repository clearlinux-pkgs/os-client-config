#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD9631FEAF0CC6227 (infra-root@openstack.org)
#
Name     : os-client-config
Version  : 1.24.0
Release  : 36
URL      : http://tarballs.openstack.org/os-client-config/os-client-config-1.24.0.tar.gz
Source0  : http://tarballs.openstack.org/os-client-config/os-client-config-1.24.0.tar.gz
Source99 : http://tarballs.openstack.org/os-client-config/os-client-config-1.24.0.tar.gz.asc
Summary  : OpenStack Client Configuation Library
Group    : Development/Tools
License  : Apache-2.0
Requires: os-client-config-python
Requires: PyYAML
Requires: appdirs
Requires: keystoneauth1
Requires: requestsexceptions
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : appdirs-python
BuildRequires : configparser-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : functools32
BuildRequires : hacking
BuildRequires : iso8601-python
BuildRequires : jsonschema-python
BuildRequires : keystoneauth1-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : oslo.config
BuildRequires : oslo.i18n-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pyparsing-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-glanceclient
BuildRequires : python-keystoneclient-python
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-python
BuildRequires : requestsexceptions
BuildRequires : requestsexceptions-python
BuildRequires : setuptools
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
Patch1: 0001-test.patch

%description
================
os-client-config
================
`os-client-config` is a library for collecting client configuration for
using an OpenStack cloud in a consistent and comprehensive manner. It
will find cloud config for as few as 1 cloud and as many as you want to
put in a config file. It will read environment variables and config files,
and it also contains some vendor specific default values so that you don't
have to know extra info to use OpenStack

%package python
Summary: python components for the os-client-config package.
Group: Default

%description python
python components for the os-client-config package.


%prep
%setup -q -n os-client-config-1.24.0
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489030502
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
export SOURCE_DATE_EPOCH=1489030502
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
