Summary:	KDE Internet Messenger
Name:		kopete
Version:	15.04.3
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
Source0:	http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kopete-4.12.4-jsoncpp.patch
BuildRequires:	jpeg-devel
BuildRequires:	jsoncpp-devel
BuildRequires:	kdelibs-devel
# Useless for now because Kleopatra headers are not installed
BuildRequires:	kdepim-devel
BuildRequires:	kdepimlibs-devel
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
BuildRequires:	pkgconfig(qimageblitz) < 5.0.0
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(zlib)
# Not in Main
#BuildRequires:	srtp-devel

Requires:	akonadi
Requires:	qca2-plugin-openssl-%{_lib}
Requires:	kdepimlibs-core
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
%{_bindir}/kopete_latexconvert.sh                                                                      
%{_bindir}/winpopup-install                                                                            
%{_bindir}/winpopup-send                                                                               
%{_datadir}/apps/kopete                                                                                
%{_datadir}/apps/kopete_contactnotes                                                                   
%{_datadir}/apps/kopete_groupwise                                                                      
%{_datadir}/apps/kopete_history                                                                        
%{_datadir}/apps/kopete_history2                                                                       
%{_datadir}/apps/kopete_jabber                                                                         
%{_datadir}/apps/kopete_latex                                                                          
%{_datadir}/apps/kopete_otr                                                                            
%{_datadir}/apps/kopete_privacy                                                                        
%{_datadir}/apps/kopete_skype                                                                          
%{_datadir}/apps/kopete_statistics
%{_bindir}/kopete
%{_datadir}/apps/kopete_translator 
%{_datadir}/apps/kopete_yahoo                                                                          
%{_datadir}/apps/kopete_wlm                                                                            
%{_datadir}/apps/kopeterichtexteditpart                                                                
%{_datadir}/apps/kconf_update/kopete-*                                                                 
%{_libdir}/kde4/kcm_kopete_*                                                                           
%{_libdir}/kde4/kopete_*                                                                               
%{_libdir}/libqgroupwise.so                                                                            
%{_libdir}/kde4/libchattexteditpart.so                                                                 
%{_datadir}/applications/kde4/kopete.desktop                                                           
%{_datadir}/config/kopeterc                                                                            
%{_datadir}/config.kcfg/historyconfig.kcfg                                                             
%{_datadir}/config.kcfg/history2config.kcfg                                                            
%{_datadir}/config.kcfg/kopeteappearancesettings.kcfg                                                  
%{_datadir}/config.kcfg/kopetebehaviorsettings.kcfg                                                    
%{_datadir}/config.kcfg/kopete_otr.kcfg                                                                
%{_datadir}/config.kcfg/kopetestatussettings.kcfg                                                      
%{_datadir}/config.kcfg/latexconfig.kcfg                                                               
%{_datadir}/config.kcfg/nowlisteningconfig.kcfg                                                        
%{_datadir}/config.kcfg/webpresenceconfig.kcfg  
%{_datadir}/config.kcfg/translatorconfig.kcfg                                                          
%{_datadir}/kde4/services/aim.protocol                                                                 
%{_datadir}/kde4/services/chatwindow.desktop                                                           
%{_datadir}/kde4/services/emailwindow.desktop                                                          
%{_datadir}/kde4/services/kconfiguredialog/kopete_*                                                    
%{_datadir}/kde4/services/kopete_*                                                                     
%{_datadir}/kde4/services/xmpp.protocol                                                                
%{_datadir}/kde4/services/callto.protocol                                                              
%{_datadir}/kde4/services/skype.protocol                                                               
%{_datadir}/kde4/services/tel.protocol                                                                 
%{_datadir}/kde4/servicetypes/kopete*                                                                  
%{_datadir}/sounds/Kopete_Event.ogg                                                                    
%{_datadir}/sounds/Kopete_Received.ogg                                                                 
%{_datadir}/sounds/Kopete_Sent.ogg                                                                     
%{_datadir}/sounds/Kopete_User_is_Online.ogg                                                           
%{_iconsdir}/*/*/actions/account_offline_overlay.*                                                     
%{_iconsdir}/*/*/actions/contact_away_overlay.*                                                        
%{_iconsdir}/*/*/actions/contact_busy_overlay.*                                                        
%{_iconsdir}/*/*/actions/contact_food_overlay.*                                                        
%{_iconsdir}/*/*/actions/contact_freeforchat_overlay.*  
%{_iconsdir}/*/*/actions/contact_invisible_overlay.*                                                   
%{_iconsdir}/*/*/actions/contact_phone_overlay.*                                                       
%{_iconsdir}/*/*/actions/contact_xa_overlay.*                                                          
%{_iconsdir}/*/*/actions/emoticon.*                                                                    
%{_iconsdir}/*/*/actions/im-status-message-edit.*                                                      
%{_iconsdir}/*/*/actions/mail-encrypt.*                                                                
%{_iconsdir}/*/*/actions/metacontact_unknown.*                                                         
%{_iconsdir}/*/*/actions/newmessage.*                                                                  
%{_iconsdir}/*/*/actions/status_unknown_overlay.*                                                      
%{_iconsdir}/*/*/actions/status_unknown.*                                                              
%{_iconsdir}/*/*/actions/view-user-offline-kopete.*                                                    
%{_iconsdir}/*/*/actions/voicecall.*                                                                   
%{_iconsdir}/*/*/actions/webcamreceive.*                                                               
%{_iconsdir}/*/*/actions/webcamsend.*                                                                  
%{_iconsdir}/*/*/apps/kopete-offline.*                                                                 
%{_iconsdir}/*/*/apps/kopete.*                                                                         
%{_iconsdir}/*/*/status/object-locked-finished.*                                                       
%{_iconsdir}/*/*/status/object-locked-unverified.*                                                     
%{_iconsdir}/*/*/status/object-locked-verified.*                                                       
%{_datadir}/config.kcfg/urlpicpreview.kcfg                                                             
%doc %{_docdir}/HTML/*/kopete 
%{_libdir}/mozilla/plugins/skypebuttons.so                                                             
%dir %{_libdir}/kde4/plugins/accessible                                                                
%{_libdir}/kde4/plugins/accessible/chatwindowaccessiblewidgetfactory.so                                
%{_datadir}/dbus-1/interfaces/*.xml                                                                    
%exclude %{_datadir}/apps/kopete_latex                                                                 
%exclude %{_libdir}/kde4/kcm_kopete_latex.*                                                            
%exclude %{_libdir}/kde4/kopete_latex.*                                                                
%exclude %{_datadir}/kde4/services/kopete_latex.desktop                                                
%exclude %{_datadir}/config.kcfg/latexconfig.kcfg                                                      
%exclude %{_bindir}/kopete_latexconvert.sh                                                             
%exclude %{_datadir}/kde4/services/kconfiguredialog/kopete_latex_config.desktop                        
%exclude %{_datadir}/apps/kopete/icons/oxygen/32x32/apps/latex.png     

#----------------------------------------------------------------------------

%package latex
Summary:	Kopete latex plugin for write andd read mesages in latex
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
Requires:	imagemagick

%description latex
Kopete latex plugin for write andd read mesages in latexinder.

%files latex
%{_bindir}/kopete_latexconvert.sh                                                                      
%{_datadir}/apps/kopete_latex                                                                          
%{_datadir}/apps/kopete/icons/oxygen/32x32/apps/latex.png                                              
%{_libdir}/kde4/kcm_kopete_latex.*                                                                     
%{_libdir}/kde4/kopete_latex.*                                                                         
%{_datadir}/config.kcfg/latexconfig.kcfg                                                               
%{_datadir}/kde4/services/kopete_latex.desktop                                                         
%{_datadir}/kde4/services/kconfiguredialog/kopete_latex_config.desktop 

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

%define kyahoo_major 1
%define libkyahoo %mklibname kyahoo %{kyahoo_major}

%package -n %{libkyahoo}
Summary:	Kopete shared library
Group:		System/Libraries

%description -n %{libkyahoo}
Kopete shared library.

%files -n %{libkyahoo}
%{_libdir}/libkyahoo.so.%{kyahoo_major}*

#----------------------------------------------------------------------------

%define kopete_videodevice_major 4
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

%define kopete_major 4
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

%define kopete_otr_shared_major 1
%define libkopete_otr_shared %mklibname kopete_otr_shared %{kopete_otr_shared_major}

%package -n %{libkopete_otr_shared}
Summary:	Kopete shared library
Group:		System/Libraries
Conflicts:	kopete-otr < 0.8

%description -n %{libkopete_otr_shared}
Kopete shared library.

%files -n %{libkopete_otr_shared}
%{_libdir}/libkopete_otr_shared.so.%{kopete_otr_shared_major}*

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

%define kopete_oscar_major 4
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
%{_libdir}/*.so
%exclude %{_libdir}/libqgroupwise.so
%{_includedir}/kopete

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4 -DWITH_GOOGLETALK=OFF
%make

%install
%makeinstall_std -C build

