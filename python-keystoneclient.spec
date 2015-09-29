#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-keystoneclient
Version  : 1.7.1
Release  : 20
URL      : http://tarballs.openstack.org/python-keystoneclient/python-keystoneclient-1.7.1.tar.gz
Source0  : http://tarballs.openstack.org/python-keystoneclient/python-keystoneclient-1.7.1.tar.gz
Summary  : Client Library for OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: python-keystoneclient-bin
Requires: python-keystoneclient-python
BuildRequires : Babel-python
BuildRequires : Jinja2-python
BuildRequires : Pygments-python
BuildRequires : Sphinx-python
BuildRequires : WebOb-python
BuildRequires : coverage-python
BuildRequires : debtcollector-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : funcsigs-python
BuildRequires : hacking-python
BuildRequires : httplib2-python
BuildRequires : iso8601-python
BuildRequires : jsonschema-python
BuildRequires : keyring-python
BuildRequires : libmemcached
BuildRequires : linecache2-python
BuildRequires : lxml-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : memcached
BuildRequires : monotonic-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr-python
BuildRequires : netifaces-python
BuildRequires : oauthlib-python
BuildRequires : openssl-dev
BuildRequires : oslo.config-python
BuildRequires : oslo.context-python
BuildRequires : oslo.i18n-python
BuildRequires : oslo.log-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8-python
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable-python
BuildRequires : py-python
BuildRequires : pycrypto-python
BuildRequires : pyflakes-python
BuildRequires : pymemcache
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python-memcached
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-mock-python
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore-python
BuildRequires : tempest-lib-python
BuildRequires : testrepository-python
BuildRequires : testresources-python
BuildRequires : testscenarios-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : virtualenv
BuildRequires : wrapt-python

%description
Python bindings to the OpenStack Identity API (Keystone)
========================================================

%package bin
Summary: bin components for the python-keystoneclient package.
Group: Binaries

%description bin
bin components for the python-keystoneclient package.


%package python
Summary: python components for the python-keystoneclient package.
Group: Default

%description python
python components for the python-keystoneclient package.


%prep
%setup -q -n python-keystoneclient-1.7.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/keystone

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
