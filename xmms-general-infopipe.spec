Summary:	XMMS - plugin to read current xmms status
Summary(pl):	Aplet do odczytu aktualnego stanu XMMS
Name:		xmms-general-infopipe
Version:	1.3
Release:	23
Epoch:		1
License:	GPL
Vendor:		Weyfour WWWWolf (aka Urpo Lankinen)
Group:		X11/Applications/Sound
Source0:	http://www.beastwithin.org/users/wwwwolf/code/xmms/xmms-infopipe-%{version}.tar.gz
Patch0:		%{name}-tmpdir.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XMMS InfoPipe is a plugin that reports XMMS status via named pipe.
Handy if you want to add interesting real-time information for a
personal web page, or a web cam page.

%description -l pl
XMMS InfoPipe to plugin wypisuj±cy aktualny status XMMS przez nazwan±
rurkê. Porêczne gdy chcemy dodaæ bie¿±c± informacjê np. na stronê WWW.

%prep
%setup -q -n xmms-infopipe-%{version}
%patch0 -p1

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

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_libdir}/xmms/General/libinfopipe*.so*
