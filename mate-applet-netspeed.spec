%define		pname	mate-netspeed
Summary:	MATE netspeed applet
Summary(pl.UTF-8):	Aplet netspeed dla środowiska MATE
Name:		mate-applet-netspeed
Version:	1.12.0
Release:	3
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.12/%{pname}-%{version}.tar.xz
# Source0-md5:	e18da3540487e3570f2752f3335dbdb6
URL:		http://www.mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd44-xml
BuildRequires:	gettext-tools >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libgtop-devel >= 1:2.14.2
BuildRequires:	libiw-devel >= 29
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-common
BuildRequires:	mate-desktop-devel >= 1.9.0
BuildRequires:	mate-panel-devel >= 1.7.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.36
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.26.0
Requires:	hicolor-icon-theme
Requires:	libgtop >= 1:2.14.2
Requires:	libiw >= 29
Requires:	mate-desktop-libs >= 1.9.0
Requires:	mate-panel >= 1.7.0
Obsoletes:	mate-netspeed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/mate-panel

%description
MATE netspeed is an applet that shows how much traffic occurs on a
specified network device. It's a fork of GNOME netspeed applet.

%description -l pl.UTF-8
MATE netspeed to aplet pokazujący, jak duży ruch występuje na
określonym urządzeniu sieciowym. Jest to odgałęzienie apletu GNOME
netspeed.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# mate-netspeed gettext domain, mate_netspeed_applet mate help
%find_lang %{name} --with-mate --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_libexecdir}/mate-netspeed-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.NetspeedAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.netspeed.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.panel.NetspeedApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/netspeed-menu.xml
%{_iconsdir}/hicolor/*/apps/mate-netspeed-applet.*
%{_iconsdir}/hicolor/*x*/devices/mate-netspeed-*.png
%{_iconsdir}/hicolor/24x24/status/mate-netspeed-*.png
