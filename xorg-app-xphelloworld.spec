#
# Conditional build:
%bcond_without	motif	# don't build Motif apps
#
Summary:	xphelloworld application
Summary(pl.UTF-8):	Aplikacja xphelloworld
Name:		xorg-app-xphelloworld
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xphelloworld-%{version}.tar.bz2
# Source0-md5:	5c7fd1e35dd63089229e357c46e4f407
Patch0:		xorg-xphelloworld-pkgconfig.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
%{?with_motif:BuildRequires:	motif-devel}
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXprintAppUtil-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xphelloworld application.

%description -l pl.UTF-8
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xphelloworld
%attr(755,root,root) %{_bindir}/xpsimplehelloworld
%attr(755,root,root) %{_bindir}/xpxthelloworld
%{_mandir}/man1/xphelloworld.1*
%{_mandir}/man1/xpsimplehelloworld.1*
%{_mandir}/man1/xpxthelloworld.1*
%if %{with motif}
%attr(755,root,root) %{_bindir}/xpawhelloworld
%attr(755,root,root) %{_bindir}/xpxmhelloworld
%{_mandir}/man1/xpawhelloworld.1*
%{_mandir}/man1/xpxmhelloworld.1*
%endif
