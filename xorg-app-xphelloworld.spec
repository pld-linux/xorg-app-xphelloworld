#
# Conditional build:
%bcond_without	motif	# don't build Motif apps
#
Summary:	xphelloworld application
Summary(pl):	Aplikacja xphelloworld
Name:		xorg-app-xphelloworld
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/app/xphelloworld-%{version}.tar.bz2
# Source0-md5:	b643d0a97b3492272475c4dd36e0b328
Patch0:		xorg-xphelloworld-pkgconfig.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
%{?with_motif:BuildRequires:	motif-devel}
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXprintAppUtil-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%configure \
	%{!?with_motif:--without-motif-libraries}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
