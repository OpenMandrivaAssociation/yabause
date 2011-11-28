Name:			yabause
Version:		0.9.11
Release:		%mkrel 1

Summary:	Yabause - A Saturn emulator
License:	GPLv2+
Group:		Emulators
URL:		http://yabause.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/yabause/%{name}-%{version}.tar.gz
Patch0:		yabause-0.9.11-sformat.patch
Patch1:		yabause-0.9.11-link.patch
Patch2:		yabause-0.9.11-lib64.patch
BuildRequires:	cmake
BuildRequires:	SDL-devel
BuildRequires:	mesaglut-devel
BuildRequires:	jsw-devel
BuildRequires:	desktop-file-utils
BuildRequires:	openssl-devel
BuildRequires:	openal-devel
BuildRequires:	doxygen
# for the translations
BuildRequires:	mini18n-devel
# for gtk interface
BuildRequires:	gtk2-devel
BuildRequires:	libgtkglext-devel
# for qt interface
BuildRequires:	qt4-devel
Requires:	%{name}-bin = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%patch0 -p1 -b .sfmt
%patch1 -p1 -b .link
%ifarch x86_64
%patch2 -p1 -b .lib64
%endif

%build
cmake . -DCMAKE_INSTALL_PREFIX:PATH=/usr
cmake . -DCMAKE_INSTALL_PREFIX:PATH=/usr -DYAB_MULTIBUILD=TRUE
%make

%install
rm -rf %{buildroot}

%makeinstall_std

desktop-file-install --vendor="" \
  --add-category="Emulator" \
  --remove-key="TryExec" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog GOALS README README.LIN README.QT TODO
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png

%files gtk
%defattr(-,root,root)
%doc AUTHORS
%attr(0755,root,games) %{_bindir}/%{name}-gtk
%{_datadir}/applications/%{name}-gtk.desktop
%{_mandir}/man1/%{name}-gtk.1*

%files qt
%defattr(-,root,root)
%doc AUTHORS
%attr(0755,root,games) %{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop
%{_mandir}/man1/%{name}-qt.1*

%clean
rm -rf %{buildroot}

