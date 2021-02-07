# Following snippets are taken from
# https://github.com/openSUSE/obs-service-tar_scm/blob/master/dist/obs-service-tar_scm.spec
# https://build.opensuse.org/package/view_file/openSUSE:Tools/obs-service-set_version/obs-service-set_version.spec
# Check for changes when new distributions/versions need to be supported.

%if 0%{?fedora_version}%{?centos_version}%{?rhel_version}
%define _pkg_base %nil
%else
%define _pkg_base -base
%endif

%if 0%{?suse_version} >= 1315 || 0%{?fedora_version} >= 29 || 0%{?centos_version} >= 800 || 0%{?rhel_version} >= 800
%bcond_without python3
%else
%bcond_with    python3
%endif

%if %{with python3}
%define use_python python3
%else
%define use_python python
%endif

%define service tar_utils

Name:           obs-service-%{service}
Version:        0.0.4
Release:        0
Summary:        An OBS source service: manipulate tar files
License:        GPL-2.0+
Group:          Development/Tools/Building
URL:            https://github.com/likan999/obs-service-%{service}
Source:         %name-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

BuildRequires:  %{use_python}-setuptools
BuildRequires:  sed
Requires:       %{use_python}%{_pkg_base}

%description
This is a source service for openSUSE Build Service that manipulates tar files.

%prep
%setup -q

%build
sed -i -e "1 s,#!/usr/bin/python$,#!/usr/bin/%{use_python}," %{service}

%install
mkdir -p %buildroot/usr/lib/obs/service
install -m 0755 %{service} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{service}.service %{buildroot}%{_prefix}/lib/obs/service

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
