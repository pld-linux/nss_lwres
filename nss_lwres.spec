# $Revision: 1.12 $Date: 2002-11-27 22:06:25 $
Summary:	lwres Service Switch Module
Summary(pl):	Modu� NSS lwres
Name:		nss_lwres
Version:	0.93
Release:	2
License:	LGPL
Group:		Base
Source0:	ftp://sourceware.cygnus.com/pub/glibc/releases/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bind-devel >= 9.0.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/lib

%description
This is nss_lwres, a name service switch module that can be used with
bind 9.

%description -l pl
To jest nss_lwres, modu� serwisu nazw, kt�ry mo�na u�ywa� z bindem 9.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS THANKS
%attr(755,root,root) %{_libdir}/*.so*
