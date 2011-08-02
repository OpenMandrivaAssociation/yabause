Name:			yabause
Version:		0.9.10
Release:		%mkrel 3

Summary:	Yabause - A Saturn emulator
License:	GPLv2+
Group:		Emulators
URL:		http://yabause.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/yabause/%{name}-%{version}.tar.gz
# mini18n is available on http://sourceforge.net/projects/yabause
# but is not yet released...
Source1:	mini18n.tar.gz

BuildRequires:	SDL-devel
%if %mdkversion >= 200700
BuildRequires:	mesaglut-devel
%else
BuildRequires:	MesaGLUT-devel
%endif
BuildRequires:	jsw-devel
BuildRequires:	desktop-file-utils
# for the translations
BuildRequires:	mini18n-devel
# for gtk interface
BuildRequires:	gtk2-devel
BuildRequires:	libgtkglext-devel
# for qt interface
BuildRequires:	qt4-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Yabause is a Sega Saturn emulator.
This package includes the translations and documentation.

%package gtk
Summary:	Yabause - A Saturn emulator - GTK+ interface
License:	GPLv2+
Group:		Emulators
URL:		http://yabause.sourceforge.net/
Requires:	yabause = %{version}

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
URL:		http://yabause.sourceforge.net/
Requires:	yabause = %{version}

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
%setup -q -a1

# to make qt and gtk guis both installable, fix qt binary's name
# and update in the desktop file
perl -pi -e "s|yabause|yabause-qt|g" src/qt/yabause.desktop

%build
# compile both qt
%configure2_5x --with-port=qt
# build fails with -j2
make

# ... and gtk interfaces
%configure2_5x --with-port=gtk
%make

%install
rm -rf %{buildroot}

# gtk binary
%makeinstall

# qt binary
install -m 755 src/qt/yabause %{buildroot}/%{_bindir}/yabause-qt

# translations
install -d -m 755 %{buildroot}/%{_datadir}/yabause
install -m 644 l10n/*.yts %{buildroot}/%{_datadir}/yabause

# icons
install -d -m 755 %{buildroot}/%{_iconsdir}
install -m 644 src/logo.png %{buildroot}/%{_iconsdir}/yabause.png
install -m 644 src/logo.png %{buildroot}/%{_iconsdir}/yabause-qt.png

# xdg menus
install -m 644 src/qt/yabause.desktop \
  %{buildroot}%{_datadir}/applications/yabause-qt.desktop

desktop-file-install --vendor="" \
  --remove-category="Game" \
  --add-category="Emulator" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

# no need to duplicate 32x32 icon
rm -rf %{buildroot}%{_datadir}/pixmaps/yabause.png

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog GOALS README README.LIN README.QT TODO
%{_datadir}/yabause
%{_mandir}/man1/yabause.1*

%files gtk
%defattr(-,root,root)
%doc AUTHORS
%attr(0755,root,games) %{_bindir}/yabause
%{_iconsdir}/yabause.png
%{_datadir}/applications/yabause.desktop

%files qt
%defattr(-,root,root)
%doc AUTHORS
%attr(0755,root,games) %{_bindir}/yabause-qt
%{_iconsdir}/yabause-qt.png
%{_datadir}/applications/yabause-qt.desktop

%clean
rm -rf %{buildroot}

