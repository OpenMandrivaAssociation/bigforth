%define nami  big-forth
%define namx  bigForth

%define name bigforth
%define version 2.1.1
%define release %mkrel 3

Name:         %name
Release:      %release
License:      GPL+
Group:        Development/Other
Version:      %version
Summary:      bigForth language
Url:	      http://bigforth.sourceforge.net/
Source:       http://prdownloads.sf.net/%name/%name-%version.tar.bz2
Source16:     big-forth.16.png.bz2
Source32:     big-forth.32.png.bz2
Source48:     big-forth.48.png.bz2
BuildRoot:    %_tmppath/%name-buildroot

%description
bigforth is a portable implementation of the ANS Forth language.
Its greatest advantage is the portable widget toolkit MINOS which
builds on top of it. There are a lot of similarites with GForth.

%prep
%setup -q -n %name

%build
%configure2_5x
make

%install
%makeinstall

# icon section
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
bzcat %SOURCE16 > %buildroot/%_iconsdir/hicolor/16x16/apps/%nami.png
bzcat %SOURCE32 > %buildroot/%_iconsdir/hicolor/32x32/apps/%nami.png
bzcat %SOURCE48 > %buildroot/%_iconsdir/hicolor/48x48/apps/%nami.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=bigForth language shell
Exec=%{_bindir}/%{name} 
Icon=big-forth
Terminal=false
Type=Application
Categories=Development;Building;Debugger;
EOF

%post
%{update_menus}
%{update_icon_cache hicolor}

%postun
%{clean_menus}
%{clean_icon_cache hicolor}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc BUGS CREDITS README ToDo
%_bindir/*
%_prefix/lib/%name
%_iconsdir/hicolor/*/apps/*
%{_datadir}/applications/mandriva-%{name}.desktop

