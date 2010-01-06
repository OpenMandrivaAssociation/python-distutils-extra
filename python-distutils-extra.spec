Name:		python-distutils-extra
Version:	2.15
Release:	%mkrel 1
Summary:	Enhancements to the Python build system
Group:		Development/Python
License:	GPLv2+
URL:		https://launchpad.net/python-distutils-extra
# Use Source from Debian because upstream was moved to Launchpad 
Source0:	http://ftp.de.debian.org/debian/pool/main/p/%{name}/%{name}_%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch
BuildRequires:	python-setuptools
       

%description
python-distutils-extra allows you to easily integrate gettext, themed icons
and GNOME documentation into your build and installation process. 


%prep
%setup -q -c "%{name}-%{version}"
rm -rf debian/debian
mv debian/* .


%build
python ./setup.py build


%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} 
chmod a+x %{buildroot}%{python_sitelib}/DistUtilsExtra/command/build_extra.py


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc doc/*
%{python_sitelib}/DistUtilsExtra/
%{python_sitelib}/python_distutils_extra*.egg-info
