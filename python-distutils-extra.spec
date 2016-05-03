Name:		python-distutils-extra
Version:	2.38
Release:	3
Summary:	Enhancements to the Python build system
Group:		Development/Python
License:	GPLv2+
URL:		https://launchpad.net/python-distutils-extra
Source0:	https://launchpad.net/python-distutils-extra/trunk/2.38/+download/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python-setuptools

%rename		python3-distutils-extra

%description
python-distutils-extra allows you to easily integrate gettext, themed icons
and GNOME documentation into your build and installation process. 


%package -n python2-distutils-extra
Summary: Enhancements to the Python 2 build system
Group: Development/Python
Provides: python2-distutils-extra = %{version}-%{release}
BuildRequires:  python2-distribute
BuildRequires:  python2-devel


%description -n python2-distutils-extra
python3-distutils-extra allows you to easily integrate gettext, themed icons
and GNOME documentation into your build and installation process. 

%prep
%setup -q -c
mv %{name}-%{version} python2
cp -r python2 python3

%build
pushd python2
%__python2 ./setup.py build
popd

pushd python3
%__python3 ./setup.py build
popd

%install
pushd python2
%__python2 setup.py install --root=%{buildroot} 
popd
chmod a+x %{buildroot}%{python2_sitelib}/DistUtilsExtra/command/build_extra.py

pushd python3
%__python3 setup.py install --root=%{buildroot} 
popd



%files
%doc python3/doc/*
%{python_sitelib}/DistUtilsExtra/
%{python_sitelib}/python_distutils_extra*.egg-info

%files -n python2-distutils-extra
%doc python2/doc/*
%{python2_sitelib}/DistUtilsExtra/
%{python2_sitelib}/python_distutils_extra*.egg-info


%changelog
* Sat Mar 03 2012 Matthew Dawkins <mattydaw@mandriva.org> 2.32-1
+ Revision: 781952
- new version 2.32

* Sat May 14 2011 Sandro Cazzaniga <kharec@mandriva.org> 2.26-1
+ Revision: 674573
- update to new version..

* Thu Nov 25 2010 Funda Wang <fwang@mandriva.org> 2.23-1mdv2011.0
+ Revision: 600933
- new version 2.23

* Fri Nov 12 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.22-1mdv2011.0
+ Revision: 596455
- Update to 2.22

* Wed Nov 03 2010 Götz Waschk <waschk@mandriva.org> 2.20-2mdv2011.0
+ Revision: 592874
- rebuild for new python 2.7

* Sat Aug 07 2010 Ahmad Samir <ahmadsamir@mandriva.org> 2.20-1mdv2011.0
+ Revision: 567256
- update to 2.20

* Fri Apr 16 2010 Michael Scherer <misc@mandriva.org> 2.18-1mdv2010.1
+ Revision: 535622
- update to new version 2.18

* Sat Jan 30 2010 Frederik Himpe <fhimpe@mandriva.org> 2.16-1mdv2010.1
+ Revision: 498551
- update to new version 2.16

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 2.15-1mdv2010.1
+ Revision: 486836
- update to new version 2.15

* Thu Dec 24 2009 Frederik Himpe <fhimpe@mandriva.org> 2.13-1mdv2010.1
+ Revision: 481992
- update to new version 2.13

* Thu Nov 12 2009 Frederik Himpe <fhimpe@mandriva.org> 2.12-1mdv2010.1
+ Revision: 465316
- update to new version 2.12

* Sun Jul 12 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3-1mdv2010.0
+ Revision: 394904
- Create package based on Fedora's SPEC
- create python-distutils-extra


