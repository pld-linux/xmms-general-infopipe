Summary:	XMMS - plugin to read current xmms status
Summary(pl):	Aplet do odczytu aktualnego stanu XMMS
Name:		xmms-general-infopipe
Version:	1.3
Release:	25
Epoch:		1
License:	GPL
Vendor:		Weyfour WWWWolf (aka Urpo Lankinen)
Group:		X11/Applications/Sound
Source0:	http://www.beastwithin.org/users/wwwwolf/code/xmms/xmms-infopipe-%{version}.tar.gz
# Source0-md5:	1ccc90254c58a81f87abc43720fe71bf
Patch0:		%{name}-tmpdir.patch
Patch1:		%{name}-divert.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch1 -p1

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{xmms_general_plugindir}/libinfopipe*.so*
