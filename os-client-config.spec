#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : os-client-config
Version  : 1.32.0
Release  : 46
URL      : http://tarballs.openstack.org/os-client-config/os-client-config-1.32.0.tar.gz
Source0  : http://tarballs.openstack.org/os-client-config/os-client-config-1.32.0.tar.gz
Source99 : http://tarballs.openstack.org/os-client-config/os-client-config-1.32.0.tar.gz.asc
Summary  : OpenStack Client Configuation Library
Group    : Development/Tools
License  : Apache-2.0
Requires: os-client-config-license = %{version}-%{release}
Requires: os-client-config-python = %{version}-%{release}
Requires: os-client-config-python3 = %{version}-%{release}
Requires: openstacksdk
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
================
os-client-config
================
.. image:: https://governance.openstack.org/tc/badges/os-client-config.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package license
Summary: license components for the os-client-config package.
Group: Default

%description license
license components for the os-client-config package.


%package python
Summary: python components for the os-client-config package.
Group: Default
Requires: os-client-config-python3 = %{version}-%{release}

%description python
python components for the os-client-config package.


%package python3
Summary: python3 components for the os-client-config package.
Group: Default
Requires: python3-core

%description python3
python3 components for the os-client-config package.


%prep
%setup -q -n os-client-config-1.32.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557103817
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/os-client-config
cp LICENSE %{buildroot}/usr/share/package-licenses/os-client-config/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/os-client-config/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
