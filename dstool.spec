Name:		dstool
Version:	2.0
Release:	3%{?dist}
Summary:	Dstool package

License:	BSD
URL:		https://dsweb.siam.org/Software/dstool
Source0:	dstool_tk-RedHatEnterprise.tar.gz

BuildRequires:	gcc

%description
Dynamical Systems Toolkit

%prep
%autosetup


%build
make


%install
mkdir -p %{buildroot}/usr/local/staff


%files
%doc README



%changelog
* Fri Nov 2 2018 <b.watts@ucl.ac.uk>
- Initial RPM package build
