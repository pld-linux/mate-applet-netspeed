%define		pname	mate-netspeed
Summary:	MATE netspeed
Name:		mate-applet-netspeed
Version:	1.5.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.5/%{pname}-%{version}.tar.xz
# Source0-md5:	992945ff8c48bceeb13e52a54039cc6d
URL:		http://www.mate-desktop.org/
BuildRequires:	docbook-dtd44-xml
BuildRequires:	gtk+2-devel
BuildRequires:	libgtop-devel
BuildRequires:	mate-common
BuildRequires:	mate-doc-utils
BuildRequires:	mate-panel-devel
BuildRequires:	rpmbuild(find_lang) >= 1.36
Requires:	glib2 >= 1:2.26.0
Requires:	mate-panel >= 1.5
Obsoletes:	mate-netspeed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/mate-panel

%description
MATE netspeed is an applet that shows how much traffic occurs on a
specified network device.

%prep
%setup -q -n %{pname}-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-silent-rules \
	--disable-static \
	--disable-scrollkeeper \
	--disable-schemas-compile \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-omf --with-mate --all-name

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
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/mate-panel/mate-netspeed-applet
%{_datadir}/dbus-1/services/org.mate.panel.applet.NetspeedAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.netspeed.gschema.xml
%{_iconsdir}/hicolor/*/apps/mate-netspeed-applet.*
%{_iconsdir}/hicolor/*/devices/mate-netspeed-*.png
%{_iconsdir}/hicolor/*/status/mate-netspeed-*.png
%{_datadir}/mate-panel/applets/org.mate.panel.NetspeedApplet.mate-panel-applet
%{_datadir}/mate-panel/ui/netspeed-menu.xml
