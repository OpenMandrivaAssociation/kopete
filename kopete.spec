%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%ifarch %{armx}
%bcond_with	linphone
%else
%bcond_without	linphone
%endif

%define snapshot %{nil}

Summary:	KDE Internet Messenger
Name:		kopete
Version:	18.12.0
%if "%{snapshot}" != ""
Release:	0.%{snapshot}.1
Source0:	%{name}-20171103.tar.xz
%else
Release:	1
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
%endif
Patch0:		https://git.archlinux.org/svntogit/packages.git/plain/trunk/kopete-openssl-1.1.patch
Patch1:		https://git.archlinux.org/svntogit/packages.git/plain/trunk/kopete-srtp2.patch
Patch2:		kopete-18.12.0-glibc-2.28.patch
Patch3:		https://git.archlinux.org/svntogit/packages.git/plain/trunk/kopete-mediastreamer2.14.patch
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/internet/kopete/
BuildRequires:	ninja
BuildRequires:	jpeg-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(libgadu)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(libotr)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(libsrtp2)
BuildRequires:	pkgconfig(speex)
%if %{with linphone}
BuildRequires:	pkgconfig(linphone)
%endif
BuildRequires:	pkgconfig(meanwhile)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(ortp)
BuildRequires:	cmake(Qca-qt5)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	kleopatra-devel
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Emoticons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KHtml)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5Wallet)
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5IdentityManagement)
BuildRequires:	cmake(KF5Libkleo)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5DNSSD)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	cmake(Gpgmepp)
BuildRequires:	cmake(Qt5Core) cmake(Qt5Network) cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets) cmake(Qt5Xml) cmake(Qt5Sql) cmake(Qt5Test)

# Not in Main
#BuildRequires:	srtp-devel

Requires:	akonadi
Requires:	qca-plugin-gcrypt-%{_lib}
Requires:	jasper
Conflicts:	kdenetwork4-devel < 3:4.11.0
Conflicts:	%{_lib}kopete4 < 3:4.11.0
Conflicts:	%{_lib}kopete_otr_shared1 < 3:4.11.0

# Yahoo Messenger doesn't seem to exist anymore
%define libkyahoo %mklibname kyahoo 1
Obsoletes:	%{libkyahoo} < %{EVRD}


%define kopete_otr_shared_major 1
%define libkopete_otr_shared %mklibname kopete_otr_shared %{kopete_otr_shared_major}

# Subpackages that don't exist in the Qt5 version anymore
Obsoletes:	%{name}-latex < %{EVRD}
Obsoletes:	%{libkopete_otr_shared} < %{EVRD}

%description
Kopete is a flexible and extendable multiple protocol instant messaging
system designed as a plugin-based system.

All protocols are plugins and allow modular installment, configuration,
and usage without the main application knowing anything about the plugin
being loaded.

The goal of Kopete is to provide users with a standard and easy to use
interface between all of their instant messaging systems, but at the same
time also providing developers with the ease of writing plugins to support
a new protocol.

The core Kopete development team provides a handful of plugins that most
users can use, in addition to templates for new developers to base a
plugin off of.

%files -f %{name}.lang
%{_bindir}/libjingle-call
%{_bindir}/kopete
%{_bindir}/winpopup-install
%{_bindir}/winpopup-send
%{_libdir}/libqgroupwise.so
%{_datadir}/metainfo/org.kde.kopete.appdata.xml
%{_datadir}/config.kcfg/*
%{_datadir}/dbus-1/interfaces/org.kde.Kopete*
%{_datadir}/dbus-1/interfaces/org.kde.kopete*
%{_sysconfdir}/xdg/kopete.categories
%{_sysconfdir}/xdg/kopeterc
%{_libdir}/qt5/plugins/kopete_translator.so
%{_libdir}/qt5/plugins/chattexteditpart.so
%{_libdir}/qt5/plugins/kcm_kopete_*.so
%{_libdir}/qt5/plugins/kopete_addbookmarks.so
%{_libdir}/qt5/plugins/kopete_aim.so
%{_libdir}/qt5/plugins/kopete_autoreplace.so
%{_libdir}/qt5/plugins/kopete_bonjour.so
%{_libdir}/qt5/plugins/kopete_chatwindow.so
%{_libdir}/qt5/plugins/kopete_contactnotes.so
%{_libdir}/qt5/plugins/kopete_emailwindow.so
%{_libdir}/qt5/plugins/kopete_gadu.so
%{_libdir}/qt5/plugins/kopete_groupwise.so
%{_libdir}/qt5/plugins/kopete_highlight.so
%{_libdir}/qt5/plugins/kopete_history.so
%{_libdir}/qt5/plugins/kopete_icq.so
%{_libdir}/qt5/plugins/kopete_jabber.so
%{_libdir}/qt5/plugins/kopete_privacy.so
%{_libdir}/qt5/plugins/kopete_qq.so
%{_libdir}/qt5/plugins/kopete_statistics.so
%{_libdir}/qt5/plugins/kopete_testbed.so
%{_libdir}/qt5/plugins/kopete_texteffect.so
%{_libdir}/qt5/plugins/kopete_urlpicpreview.so
%{_libdir}/qt5/plugins/kopete_webpresence.so
%{_libdir}/qt5/plugins/kopete_wp.so
%{_libdir}/qt5/plugins/accessible/chatwindowaccessiblewidgetfactory.so
%{_datadir}/applications/org.kde.kopete.desktop
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/kconf_update/kopete*
%{_datadir}/kopete
%{_datadir}/kopete_history
%{_datadir}/knotifications5/kopete.notifyrc
%{_datadir}/kservices5/aim.protocol
%{_datadir}/kservices5/chatwindow.desktop
%{_datadir}/kservices5/emailwindow.desktop
%{_datadir}/kservices5/kconfiguredialog
%{_datadir}/kservices5/kopete_accountconfig.desktop
%{_datadir}/kservices5/kopete_addbookmarks.desktop
%{_datadir}/kservices5/kopete_aim.desktop
%{_datadir}/kservices5/kopete_appearanceconfig.desktop
%{_datadir}/kservices5/kopete_autoreplace.desktop
%{_datadir}/kservices5/kopete_avdeviceconfig.desktop
%{_datadir}/kservices5/kopete_behaviorconfig.desktop
%{_datadir}/kservices5/kopete_bonjour.desktop
%{_datadir}/kservices5/kopete_chatwindowconfig.desktop
%{_datadir}/kservices5/kopete_contactnotes.desktop
%{_datadir}/kservices5/kopete_gadu.desktop
%{_datadir}/kservices5/kopete_groupwise.desktop
%{_datadir}/kservices5/kopete_highlight.desktop
%{_datadir}/kservices5/kopete_history.desktop
%{_datadir}/kservices5/kopete_icq.desktop
%{_datadir}/kservices5/kopete_jabber.desktop
%{_datadir}/kservices5/kopete_pluginconfig.desktop
%{_datadir}/kservices5/kopete_privacy.desktop
%{_datadir}/kservices5/kopete_qq.desktop
%{_datadir}/kservices5/kopete_statistics.desktop
%{_datadir}/kservices5/kopete_statusconfig.desktop
%{_datadir}/kservices5/kopete_testbed.desktop
%{_datadir}/kservices5/kopete_texteffect.desktop
%{_datadir}/kservices5/kopete_translator.desktop
%{_datadir}/kservices5/kopete_urlpicpreview.desktop
%{_datadir}/kservices5/kopete_webpresence.desktop
%{_datadir}/kservices5/kopete_wp.desktop
%{_datadir}/kservices5/xmpp.protocol
%{_datadir}/kservicetypes5/kopeteplugin.desktop
%{_datadir}/kservicetypes5/kopeteprotocol.desktop
%{_datadir}/kservicetypes5/kopeteui.desktop
%{_datadir}/kxmlgui5/kopete
%{_datadir}/kxmlgui5/kopete_groupwise
%{_datadir}/sounds/Kopete*

#----------------------------------------------------------------------------

%define kopetecontactlist_major 1
%define libkopetecontactlist %mklibname kopetecontactlist %{kopetecontactlist_major}

%package -n %{libkopetecontactlist}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopetecontactlist}
Kopete shared library.

%files -n %{libkopetecontactlist}
%{_libdir}/libkopetecontactlist.so.%{kopetecontactlist_major}*

#----------------------------------------------------------------------------

%define kopete_videodevice_major 1
%define libkopete_videodevice %mklibname kopete_videodevice %{kopete_videodevice_major}

%package -n %{libkopete_videodevice}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopete_videodevice}
Kopete shared library.

%files -n %{libkopete_videodevice}
%{_libdir}/libkopete_videodevice.so.%{kopete_videodevice_major}*

#----------------------------------------------------------------------------

%define kopeteaddaccountwizard_major 1
%define libkopeteaddaccountwizard %mklibname kopeteaddaccountwizard %{kopeteaddaccountwizard_major}

%package -n %{libkopeteaddaccountwizard}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopeteaddaccountwizard}
Kopete shared library.

%files -n %{libkopeteaddaccountwizard}
%{_libdir}/libkopeteaddaccountwizard.so.%{kopeteaddaccountwizard_major}*

#----------------------------------------------------------------------------

%define kopete_major 1
%define libkopete %mklibname kopete %{kopete_major}

%package -n %{libkopete}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopete}
Kopete shared library.

%files -n %{libkopete}
%{_libdir}/libkopete.so.%{kopete_major}*

#----------------------------------------------------------------------------

%define kopeteprivacy_major 1
%define libkopeteprivacy %mklibname kopeteprivacy %{kopeteprivacy_major}

%package -n %{libkopeteprivacy}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopeteprivacy}
Kopete shared library.

%files -n %{libkopeteprivacy}
%{_libdir}/libkopeteprivacy.so.%{kopeteprivacy_major}*

#----------------------------------------------------------------------------

%define kopetechatwindow_shared_major 1
%define libkopetechatwindow_shared %mklibname kopetechatwindow_shared %{kopetechatwindow_shared_major}

%package -n %{libkopetechatwindow_shared}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopetechatwindow_shared}
Kopete shared library.

%files -n %{libkopetechatwindow_shared}
%{_libdir}/libkopetechatwindow_shared.so.%{kopetechatwindow_shared_major}*

#----------------------------------------------------------------------------

%define kopetestatusmenu_major 1
%define libkopetestatusmenu %mklibname kopetestatusmenu %{kopetestatusmenu_major}

%package -n %{libkopetestatusmenu}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopetestatusmenu}
Kopete shared library.

%files -n %{libkopetestatusmenu}
%{_libdir}/libkopetestatusmenu.so.%{kopetestatusmenu_major}*

#----------------------------------------------------------------------------

%define kopete_oscar_major 1
%define libkopete_oscar %mklibname kopete_oscar %{kopete_oscar_major}

%package -n %{libkopete_oscar}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopete_oscar}
Kopete shared library.

%files -n %{libkopete_oscar}
%{_libdir}/libkopete_oscar.so.%{kopete_oscar_major}*

#----------------------------------------------------------------------------

%define oscar_major 1
%define liboscar %mklibname oscar %{oscar_major}

%package -n %{liboscar}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{liboscar}
Kopete shared library.

%files -n %{liboscar}
%{_libdir}/liboscar.so.%{oscar_major}*

#----------------------------------------------------------------------------

%define kopeteidentity_major 1
%define libkopeteidentity %mklibname kopeteidentity %{kopeteidentity_major}

%package -n %{libkopeteidentity}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopeteidentity}
Kopete shared library.

%files -n %{libkopeteidentity}
%{_libdir}/libkopeteidentity.so.%{kopeteidentity_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Kopete
Group:		Development/KDE and Qt
Requires:	%{libkopetecontactlist} = %{EVRD}
Requires:	%{libkopete_videodevice} = %{EVRD}
Requires:	%{libkopeteaddaccountwizard} = %{EVRD}
Requires:	%{libkopete} = %{EVRD}
Requires:	%{libkopeteprivacy} = %{EVRD}
Requires:	%{libkopetechatwindow_shared} = %{EVRD}
Requires:	%{libkopete_oscar} = %{EVRD}
Requires:	%{liboscar} = %{EVRD}
Requires:	%{libkopeteidentity} = %{EVRD}
Requires:	%{libkopetestatusmenu} = %{EVRD}
Conflicts:	kdenetwork4-devel < 3:4.11.0

%description devel
This package contains header files needed if you want to build applications
based on Kopete.

%files devel
%{_libdir}/*.so
%exclude %{_libdir}/libqgroupwise.so
%{_includedir}/kopete

#----------------------------------------------------------------------------

%prep
%if "%{snapshot}" != ""
%setup -qn %{name}
%else
%setup -q
%endif
%apply_patches

%build
%cmake_kde5 \
	-DWITH_GOOGLETALK=ON \
	-DWITH_translator:BOOL=ON
%ninja

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-html
