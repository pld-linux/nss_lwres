Summary:	lwres Service Switch Module
Summary(pl):	Modu³ NSS lwres
Name:		nss_lwres
Version:	0.93
Release:	4
License:	LGPL
Group:		Base
Source0:	ftp://sourceware.cygnus.com/pub/glibc/releases/%{name}-%{version}.tar.gz
# Source0-md5:	3295845dda13fb6af2ca9d58a9051557
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bind-devel >= 9.0.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}

%description
This is nss_lwres, a name service switch module that can be used with
bind 9.

%description -l pl
To jest nss_lwres, modu³ serwisu nazw, który mo¿na u¿ywaæ z bindem 9.

%prep
%setup -q

%build
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
