# $Revision: 1.2 $Date: 2001-02-22 22:47:18 $
Summary:	Berkeley DB Name Service Switch Module
Name:		nss_lwres
Version:	0.92
Release:	1
License:	LGPL
Group:		Base
Group(de):	Gründsätzlich
Group(pl):	Podstawowe
Source0:	ftp://sourceware.cygnus.com/pub/glibc/releases/%{name}-%{version}.tar.gz
BuildRequires:	bind-devel >= 9.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
This is nss_lwres, a name service switch module that can be used with
bind 9.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog README NEWS THANKS

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,README,NEWS,THANKS}.gz
%attr(755,root,root) /lib/*.so
