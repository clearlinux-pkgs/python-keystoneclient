#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xFC43F0EE211DFED8 (infra-root@openstack.org)
#
Name     : python-keystoneclient
Version  : 3.22.0
Release  : 65
URL      : http://tarballs.openstack.org/python-keystoneclient/python-keystoneclient-3.22.0.tar.gz
Source0  : http://tarballs.openstack.org/python-keystoneclient/python-keystoneclient-3.22.0.tar.gz
Source1 : http://tarballs.openstack.org/python-keystoneclient/python-keystoneclient-3.22.0.tar.gz.asc
Summary  : Client Library for OpenStack Identity
Group    : Development/Tools
License  : Apache-2.0
Requires: python-keystoneclient-license = %{version}-%{release}
Requires: python-keystoneclient-python = %{version}-%{release}
Requires: python-keystoneclient-python3 = %{version}-%{release}
Requires: debtcollector
Requires: keystoneauth1
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: requests
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : debtcollector
BuildRequires : keystoneauth1
BuildRequires : oslo.config
BuildRequires : oslo.i18n
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : requests
BuildRequires : six
BuildRequires : stevedore
BuildRequires : util-linux
Patch1: cve-2015-7546.nopatch

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/python-keystoneclient.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the python-keystoneclient package.
Group: Default

%description license
license components for the python-keystoneclient package.


%package python
Summary: python components for the python-keystoneclient package.
Group: Default
Requires: python-keystoneclient-python3 = %{version}-%{release}

%description python
python components for the python-keystoneclient package.


%package python3
Summary: python3 components for the python-keystoneclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-keystoneclient package.


%prep
%setup -q -n python-keystoneclient-3.22.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571805745
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export FCFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export FFLAGS="$CFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -O3 -fcf-protection=full -ffat-lto-objects -flto=4 -fstack-protector-strong "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-keystoneclient
cp %{_builddir}/python-keystoneclient-3.22.0/LICENSE %{buildroot}/usr/share/package-licenses/python-keystoneclient/9834508b6aa6463fa2da734542dca50f6707c45b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-keystoneclient/9834508b6aa6463fa2da734542dca50f6707c45b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
