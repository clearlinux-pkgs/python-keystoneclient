#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB9069B1335700CDC (infra-root@openstack.org)
#
Name     : python-keystoneclient
Version  : 3.10.0
Release  : 51
URL      : http://tarballs.openstack.org/python-keystoneclient/python-keystoneclient-3.10.0.tar.gz
Source0  : http://tarballs.openstack.org/python-keystoneclient/python-keystoneclient-3.10.0.tar.gz
Source99 : http://tarballs.openstack.org/python-keystoneclient/python-keystoneclient-3.10.0.tar.gz.asc
Summary  : Client Library for OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: python-keystoneclient-python
Requires: debtcollector
Requires: keystoneauth1
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: positional
Requires: requests
Requires: six
Requires: stevedore
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
Patch1: cve-2015-7546.nopatch
Patch2: 0001-don-t-ask-for-hard-flake8-docstrings-0.2.1.post1-ver.patch

%description
========================
Team and repository tags
========================
.. image:: http://governance.openstack.org/badges/python-keystoneclient.svg
:target: http://governance.openstack.org/reference/tags/index.html

%package python
Summary: python components for the python-keystoneclient package.
Group: Default

%description python
python components for the python-keystoneclient package.


%prep
%setup -q -n python-keystoneclient-3.10.0
%patch2 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489785759
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489785759
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
