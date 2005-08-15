# $Rev: 3410 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xphelloworld application
Summary(pl):	Aplikacja xphelloworld
Name:		xorg-app-xphelloworld
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xphelloworld-%{version}.tar.bz2
# Source0-md5:	aeaf1b305d49eb084dc8bf6becc3cfad
Patch0:		xphelloworld-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXprintAppUtil-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/xphelloworld-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xphelloworld application.

%description -l pl
Aplikacja xphelloworld.


%prep
%setup -q -n xphelloworld-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
