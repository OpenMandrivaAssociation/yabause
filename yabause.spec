Name:		yabause
Version:	0.9.11.1
Release:	1

Summary:	Yabause - A Saturn emulator
License:	GPLv2+
Group:		Emulators
URL:		http://yabause.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/yabause/%{name}-%{version}.tar.gz
Patch1:		yabause-0.9.11-link.patch
Patch2:		yabause-0.9.11-lib64.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(glut)
BuildRequires:	jsw-devel
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	doxygen
# for the translations
BuildRequires:	mini18n-devel
# for gtk interface
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
# for qt interface
BuildRequires:	qt4-devel
Requires:	%{name}-bin = %{version}

%description
Yabause is a Sega Saturn emulator.
This package includes the translations and documentation.

%package gtk
Summary:	Yabause - A Saturn emulator - GTK+ interface
License:	GPLv2+
Group:		Emulators
Requires:	%{name} = %{version}
Provides:	%{name}-bin = %{version}

%description gtk
Yabause is a Sega Saturn emulator.

This package includes the GTK+ interface.

To use a translation :
Start yabause,
Open the settings dialog (Yabause/Preferences),
Select Advanced tab,
Type or select the appropriate file in the Translation field 
(existing translations are available in the /usr/share/yabause/ folder),
Close and restart yabause.

%package qt
Summary:	Yabause - A Saturn emulator - QT interface
License:	GPLv2+
Group:		Emulators
Requires:	%{name} = %{version}
Provides:	%{name}-bin = %{version}

%description qt
Yabause is a Sega Saturn emulator.

This package includes the QT interface.

To use a translation :
Start yabause,
Open the settings dialog (File/Settings),
Type or select the appropriate file in the Translation field 
(existing translations are available in the /usr/share/yabause/ folder),
Close and restart yabause-qt.

%prep
%setup -q
%patch1 -p1 -b .link
%ifarch x86_64
%patch2 -p1 -b .lib64
%endif

%build
cmake . -DCMAKE_INSTALL_PREFIX:PATH=/usr
cmake . -DCMAKE_INSTALL_PREFIX:PATH=/usr -DYAB_MULTIBUILD=TRUE
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
  --add-category="Emulator" \
  --remove-key="TryExec" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%files
%doc AUTHORS ChangeLog GOALS README README.LIN README.QT TODO
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png

%files gtk
%doc AUTHORS
%attr(0755,root,games) %{_bindir}/%{name}-gtk
%{_datadir}/applications/%{name}-gtk.desktop
%{_mandir}/man1/%{name}-gtk.1*

%files qt
%doc AUTHORS
%attr(0755,root,games) %{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop
%{_mandir}/man1/%{name}-qt.1*

%changelog
* Mon Nov 28 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.11-1
+ Revision: 734875
- New version 0.9.11, switch to cmake
- Rebuild
- Updated BuildRequires
- imported package yabause


* Mon Jun  1 2009 Guillaume Bedot <littletux@zarb.org> 0.9.10-1plf2010.0
- 0.9.10

* Sat Jan 17 2009 Guillaume Bedot <littletux@zarb.org> 0.9.9-1plf2009.1
- 0.9.9

* Tue Jan  6 2009 Guillaume Bedot <littletux@zarb.org> 0.9.8-1plf2009.1
- 0.9.8

* Tue Oct 21 2008 Guillaume Bedot <littletux@zarb.org> 0.9.7-1plf2009.1
- 0.9.7
- drop outdated patch

* Mon Jun 30 2008 Guillaume Bedot <littletux@zarb.org> 0.9.6-1plf2009.0
- 0.9.6
- sub-packages for qt and gtk interfaces
- obsolete patch removed (workarounded upstream)
- dropped old menu and related icons

* Thu May 29 2008 Guillaume Bedot <littletux@zarb.org> 0.9.5-1plf2009.0
- 0.9.5
- added icons as sources (do not require imagemagick)

* Tue Mar 18 2008 Guillaume Bedot <littletux@zarb.org> 0.9.4-1plf2008.1
- 0.9.4

* Tue Feb 05 2008 Anssi Hannula <anssi@zarb.org> 0.9.3-2plf2008.1
- buildrequires desktop-file-utils

* Mon Jan 28 2008 Guillaume Bedot <littletux@zarb.org> 0.9.3-1plf2008.1
- 0.9.3

* Mon Dec 17 2007 Guillaume Bedot <littletux@zarb.org> 0.9.2-1plf2008.1
- 0.9.2

* Thu Dec 06 2007 Guillaume Bedot <littletux@zarb.org> 0.9.1-2plf2008.1
- builreqs

* Tue Nov 27 2007 Guillaume Bedot <littletux@zarb.org> 0.9.1-1plf2008.1
- 0.9.1

* Wed Jun 27 2007 Guillaume Bedot <littletux@zarb.org> 0.8.5-1plf2008.0
- 0.8.5

* Wed Mar 21 2007 Guillaume Bedot <littletux@zarb.org> 0.8.0-1plf2007.1
- 0.8.0

* Fri Sep 01 2006 Guillaume Bedot <littletux@zarb.org> 0.7.1-1plf2007.0
- 0.7.1

* Wed Aug 30 2006 Anssi Hannula <anssi@zarb.org> 0.7.0-2plf2007.0
- fix buildrequires

* Tue Aug 22 2006 Guillaume Bedot <littletux@zarb.org> 0.7.0-1plf2007.0
- 0.7.0, menu, new buildrequires

* Sat Jul 22 2006 Guillaume Bedot <littletux@zarb.org> 0.6.0-2plf2007.0
- space insteas of tabs, clean install

* Wed Feb 22 2006 Guillaume Bedot <littletux@zarb.org> 0.6.0-1plf
- First package
