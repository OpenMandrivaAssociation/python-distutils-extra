Name:		python-distutils-extra
Version:	2.37
Release:	1
Summary:	Enhancements to the Python build system
Group:		Development/Python
License:	GPLv2+
URL:		https://launchpad.net/python-distutils-extra
Source0:	http://launchpad.net/python-distutils-extra/trunk/%{version}/+download/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
python-distutils-extra allows you to easily integrate gettext, themed icons
and GNOME documentation into your build and installation process. 

%prep
%setup -q

%build
python ./setup.py build

%install
python setup.py install --root=%{buildroot} 
chmod a+x %{buildroot}%{python_sitelib}/DistUtilsExtra/command/build_extra.py

%files
%doc doc/*
%{python_sitelib}/DistUtilsExtra/
%{python_sitelib}/python_distutils_extra*.egg-info
