Summary:	Sega Saturn emulator
Name:		yabause
Version:	0.9.13
Release:	2
License:	GPLv2+
Group:		Emulators
Url:		http://yabause.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/yabause/%{name}-%{version}.tar.gz
Patch0:		yabause-0.9.13-cmake.patch
Patch1:		yabause-0.9.11-link.patch
Patch2:		yabause-0.9.11-lib64.patch
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	doxygen
BuildRequires:	jsw-devel
# for the translations
BuildRequires:	mini18n-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(glut)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtkglext-1.0)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(xmu)
Requires:	%{name}-bin = %{version}

%description
Yabause is a Sega Saturn emulator.
This package includes the translations and documentation.

%files
%doc AUTHORS ChangeLog GOALS README README.LIN README.QT TODO
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png

#----------------------------------------------------------------------------

%package gtk
Summary:	Sega Saturn emulator - GTK+ interface
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

%files gtk
%doc AUTHORS
%attr(0755,root,games) %{_bindir}/%{name}-gtk
%{_datadir}/applications/%{name}-gtk.desktop
%{_mandir}/man1/%{name}-gtk.1*

#----------------------------------------------------------------------------

%package qt
Summary:	Sega Saturn emulator - QT interface
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

%files qt
%doc AUTHORS
%attr(0755,root,games) %{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop
%{_mandir}/man1/%{name}-qt.1*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .cmake~
%patch1 -p1 -b .link~
%ifarch x86_64
%patch2 -p1 -b .lib64~
%endif

find . -name *.cpp -o -name *.h | xargs chmod 0644

%build
%cmake -DYAB_MULTIBUILD=TRUE
%make

%install
%makeinstall_std -C build

desktop-file-install --vendor="" \
	--add-category="Emulator" \
	--remove-key="TryExec" \
	--dir %{buildroot}%{_datadir}/applications/ \
	%{buildroot}%{_datadir}/applications/*

