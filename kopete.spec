Summary:	KDE Internet Messenger
Name:		kopete
Version:	4.13.2
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org/applications/internet/kopete/
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%{ftpdir}/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kopete-4.12.4-giflib51.patch
Patch1:		kopete-4.12.4-jsoncpp.patch
BuildRequires:	jpeg-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	kdelibs4-devel
# Useless for now because Kleopatra headers are not installed
BuildRequires:	kdepim4-devel
BuildRequires:	kdepimlibs4-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(libgadu)
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(libmsn)
BuildRequires:	pkgconfig(libotr)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(linphone)
BuildRequires:	pkgconfig(meanwhile)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(ortp)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(qimageblitz)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(zlib)
# Not in Main
#BuildRequires:	srtp-devel

Requires:	akonadi
Requires:	qca2-plugin-openssl-%{_lib}
Requires:	kdepimlibs4-core
Requires:	jasper
Conflicts:	kdenetwork4-devel < 3:4.11.0
Conflicts:	%{_lib}kopete4 < 3:4.11.0
Conflicts:	%{_lib}kopete_otr_shared1 < 3:4.11.0

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

%files
%{_kde_bindir}/kopete
%{_kde_bindir}/kopete_latexconvert.sh
%{_kde_bindir}/winpopup-install
%{_kde_bindir}/winpopup-send
%{_kde_appsdir}/kopete
%{_kde_appsdir}/kopete_contactnotes
%{_kde_appsdir}/kopete_groupwise
%{_kde_appsdir}/kopete_history
%{_kde_appsdir}/kopete_history2
%{_kde_appsdir}/kopete_jabber
%{_kde_appsdir}/kopete_latex
%{_kde_appsdir}/kopete_otr
%{_kde_appsdir}/kopete_privacy
%{_kde_appsdir}/kopete_skype
%{_kde_appsdir}/kopete_statistics
%{_kde_appsdir}/kopete_translator
%{_kde_appsdir}/kopete_yahoo
%{_kde_appsdir}/kopete_wlm
%{_kde_appsdir}/kopeterichtexteditpart
%{_kde_appsdir}/kconf_update/kopete-*
%{_kde_libdir}/kde4/kcm_kopete_*
%{_kde_libdir}/kde4/kopete_*
%{_kde_libdir}/libqgroupwise.so
%{_kde_libdir}/kde4/libchattexteditpart.so
%{_kde_applicationsdir}/kopete.desktop
%{_kde_configdir}/kopeterc
%{_kde_datadir}/config.kcfg/historyconfig.kcfg
%{_kde_datadir}/config.kcfg/history2config.kcfg
%{_kde_datadir}/config.kcfg/kopeteappearancesettings.kcfg
%{_kde_datadir}/config.kcfg/kopetebehaviorsettings.kcfg
%{_kde_datadir}/config.kcfg/kopete_otr.kcfg
%{_kde_datadir}/config.kcfg/kopetestatussettings.kcfg
%{_kde_datadir}/config.kcfg/latexconfig.kcfg
%{_kde_datadir}/config.kcfg/nowlisteningconfig.kcfg
%{_kde_datadir}/config.kcfg/webpresenceconfig.kcfg
%{_kde_datadir}/config.kcfg/translatorconfig.kcfg
%{_kde_services}/aim.protocol
%{_kde_services}/chatwindow.desktop
%{_kde_services}/emailwindow.desktop
%{_kde_services}/kconfiguredialog/kopete_*
%{_kde_services}/kopete_*
%{_kde_services}/xmpp.protocol
%{_kde_services}/callto.protocol
%{_kde_services}/skype.protocol
%{_kde_services}/tel.protocol
%{_kde_servicetypes}/kopete*
%{_kde_datadir}/sounds/Kopete_Event.ogg
%{_kde_datadir}/sounds/Kopete_Received.ogg
%{_kde_datadir}/sounds/Kopete_Sent.ogg
%{_kde_datadir}/sounds/Kopete_User_is_Online.ogg
%{_kde_iconsdir}/*/*/actions/account_offline_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_away_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_busy_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_food_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_freeforchat_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_invisible_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_phone_overlay.*
%{_kde_iconsdir}/*/*/actions/contact_xa_overlay.*
%{_kde_iconsdir}/*/*/actions/emoticon.*
%{_kde_iconsdir}/*/*/actions/im-status-message-edit.*
%{_kde_iconsdir}/*/*/actions/mail-encrypt.*
%{_kde_iconsdir}/*/*/actions/metacontact_unknown.*
%{_kde_iconsdir}/*/*/actions/newmessage.*
%{_kde_iconsdir}/*/*/actions/status_unknown_overlay.*
%{_kde_iconsdir}/*/*/actions/status_unknown.*
%{_kde_iconsdir}/*/*/actions/view-user-offline-kopete.*
%{_kde_iconsdir}/*/*/actions/voicecall.*
%{_kde_iconsdir}/*/*/actions/webcamreceive.*
%{_kde_iconsdir}/*/*/actions/webcamsend.*
%{_kde_iconsdir}/*/*/apps/kopete-offline.*
%{_kde_iconsdir}/*/*/apps/kopete.*
%{_kde_iconsdir}/*/*/status/object-locked-finished.*
%{_kde_iconsdir}/*/*/status/object-locked-unverified.*
%{_kde_iconsdir}/*/*/status/object-locked-verified.*
%{_kde_datadir}/config.kcfg/urlpicpreview.kcfg
%{_kde_docdir}/HTML/*/kopete
%{_kde_libdir}/mozilla/plugins/skypebuttons.so
%dir %{_kde_libdir}/kde4/plugins/accessible
%{_kde_libdir}/kde4/plugins/accessible/chatwindowaccessiblewidgetfactory.so
%{_datadir}/dbus-1/interfaces/*.xml
%exclude %{_kde_appsdir}/kopete_latex
%exclude %{_kde_libdir}/kde4/kcm_kopete_latex.*
%exclude %{_kde_libdir}/kde4/kopete_latex.*
%exclude %{_kde_datadir}/kde4/services/kopete_latex.desktop
%exclude %{_kde_datadir}/config.kcfg/latexconfig.kcfg
%exclude %{_kde_bindir}/kopete_latexconvert.sh
%exclude %{_kde_datadir}/kde4/services/kconfiguredialog/kopete_latex_config.desktop
%exclude %{_kde_appsdir}/kopete/icons/oxygen/32x32/apps/latex.png

#----------------------------------------------------------------------------

%package latex
Summary:	Kopete latex plugin for write andd read mesages in latex
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
Requires:	imagemagick

%description latex
Kopete latex plugin for write andd read mesages in latexinder.

%files latex
%{_kde_bindir}/kopete_latexconvert.sh
%{_kde_appsdir}/kopete_latex
%{_kde_appsdir}/kopete/icons/oxygen/32x32/apps/latex.png
%{_kde_libdir}/kde4/kcm_kopete_latex.*
%{_kde_libdir}/kde4/kopete_latex.*
%{_kde_datadir}/config.kcfg/latexconfig.kcfg
%{_kde_services}/kopete_latex.desktop
%{_kde_services}/kconfiguredialog/kopete_latex_config.desktop

#----------------------------------------------------------------------------

%define kopetecontactlist_major 1
%define libkopetecontactlist %mklibname kopetecontactlist %{kopetecontactlist_major}

%package -n %{libkopetecontactlist}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopetecontactlist}
Kopete shared library.

%files -n %{libkopetecontactlist}
%{_kde_libdir}/libkopetecontactlist.so.%{kopetecontactlist_major}*

#----------------------------------------------------------------------------

%define kyahoo_major 1
%define libkyahoo %mklibname kyahoo %{kyahoo_major}

%package -n %{libkyahoo}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkyahoo}
Kopete shared library.

%files -n %{libkyahoo}
%{_kde_libdir}/libkyahoo.so.%{kyahoo_major}*

#----------------------------------------------------------------------------

%define kopete_videodevice_major 4
%define libkopete_videodevice %mklibname kopete_videodevice %{kopete_videodevice_major}

%package -n %{libkopete_videodevice}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopete_videodevice}
Kopete shared library.

%files -n %{libkopete_videodevice}
%{_kde_libdir}/libkopete_videodevice.so.%{kopete_videodevice_major}*

#----------------------------------------------------------------------------

%define kopeteaddaccountwizard_major 1
%define libkopeteaddaccountwizard %mklibname kopeteaddaccountwizard %{kopeteaddaccountwizard_major}

%package -n %{libkopeteaddaccountwizard}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopeteaddaccountwizard}
Kopete shared library.

%files -n %{libkopeteaddaccountwizard}
%{_kde_libdir}/libkopeteaddaccountwizard.so.%{kopeteaddaccountwizard_major}*

#----------------------------------------------------------------------------

%define kopete_major 4
%define libkopete %mklibname kopete %{kopete_major}

%package -n %{libkopete}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopete}
Kopete shared library.

%files -n %{libkopete}
%{_kde_libdir}/libkopete.so.%{kopete_major}*

#----------------------------------------------------------------------------

%define kopeteprivacy_major 1
%define libkopeteprivacy %mklibname kopeteprivacy %{kopeteprivacy_major}

%package -n %{libkopeteprivacy}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopeteprivacy}
Kopete shared library.

%files -n %{libkopeteprivacy}
%{_kde_libdir}/libkopeteprivacy.so.%{kopeteprivacy_major}*

#----------------------------------------------------------------------------

%define kopetechatwindow_shared_major 1
%define libkopetechatwindow_shared %mklibname kopetechatwindow_shared %{kopetechatwindow_shared_major}

%package -n %{libkopetechatwindow_shared}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopetechatwindow_shared}
Kopete shared library.

%files -n %{libkopetechatwindow_shared}
%{_kde_libdir}/libkopetechatwindow_shared.so.%{kopetechatwindow_shared_major}*

#----------------------------------------------------------------------------

%define kopete_otr_shared_major 1
%define libkopete_otr_shared %mklibname kopete_otr_shared %{kopete_otr_shared_major}

%package -n %{libkopete_otr_shared}
Summary:	Kopete shared library
Group:		System/Libraries
Conflicts:	kopete-otr < 0.8

%description -n %{libkopete_otr_shared}
Kopete shared library.

%files -n %{libkopete_otr_shared}
%{_kde_libdir}/libkopete_otr_shared.so.%{kopete_otr_shared_major}*

#----------------------------------------------------------------------------

%define kopetestatusmenu_major 1
%define libkopetestatusmenu %mklibname kopetestatusmenu %{kopetestatusmenu_major}

%package -n %{libkopetestatusmenu}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopetestatusmenu}
Kopete shared library.

%files -n %{libkopetestatusmenu}
%{_kde_libdir}/libkopetestatusmenu.so.%{kopetestatusmenu_major}*

#----------------------------------------------------------------------------

%define kopete_oscar_major 4
%define libkopete_oscar %mklibname kopete_oscar %{kopete_oscar_major}

%package -n %{libkopete_oscar}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopete_oscar}
Kopete shared library.

%files -n %{libkopete_oscar}
%{_kde_libdir}/libkopete_oscar.so.%{kopete_oscar_major}*

#----------------------------------------------------------------------------

%define oscar_major 1
%define liboscar %mklibname oscar %{oscar_major}

%package -n %{liboscar}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{liboscar}
Kopete shared library.

%files -n %{liboscar}
%{_kde_libdir}/liboscar.so.%{oscar_major}*

#----------------------------------------------------------------------------

%define kopeteidentity_major 1
%define libkopeteidentity %mklibname kopeteidentity %{kopeteidentity_major}

%package -n %{libkopeteidentity}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkopeteidentity}
Kopete shared library.

%files -n %{libkopeteidentity}
%{_kde_libdir}/libkopeteidentity.so.%{kopeteidentity_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for Kopete
Group:		Development/KDE and Qt
Requires:	%{libkopetecontactlist} = %{EVRD}
Requires:	%{libkyahoo} = %{EVRD}
Requires:	%{libkopete_videodevice} = %{EVRD}
Requires:	%{libkopeteaddaccountwizard} = %{EVRD}
Requires:	%{libkopete} = %{EVRD}
Requires:	%{libkopeteprivacy} = %{EVRD}
Requires:	%{libkopetechatwindow_shared} = %{EVRD}
Requires:	%{libkopete_oscar} = %{EVRD}
Requires:	%{liboscar} = %{EVRD}
Requires:	%{libkopete_otr_shared} = %{EVRD}
Requires:	%{libkopeteidentity} = %{EVRD}
Requires:	%{libkopetestatusmenu} = %{EVRD}
Conflicts:	kdenetwork4-devel < 3:4.11.0

%description devel
This package contains header files needed if you want to build applications
based on Kopete.

%files devel
%{_kde_libdir}/*.so
%exclude %{_kde_libdir}/libqgroupwise.so
%{_kde_includedir}/kopete

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake_kde4 -DWITH_GOOGLETALK=OFF
%make

%install
%makeinstall_std -C build

%changelog
* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.13.2-1
- New version 4.13.2

* Wed May 28 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.4-2
- Add giflib51 patch to fix build with giflib 5.1
- Add jsoncpp patch to fix jsoncpp detection by cmake

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.12.1-1
- New version 4.12.1
- Add kdepim4-devel to BuildRequires
- Update files

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 3:4.11.0-1
- New version 4.11.0
- Split from kdenetwork4 package as upstream did
- Move noarch files from library packages to main package
