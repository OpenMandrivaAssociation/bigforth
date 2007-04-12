%define nami  big-forth
%define namx  bigForth

%define name bigforth
%define version 2.1.1
%define release %mkrel 2

Name:         %name
Release:      %release
License:      GPL
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
builds on top of it. There are a lot of similarites with GForth btw.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n %name

%build

%configure

make

%install

%makeinstall

# icon section
install -d %buildroot/%_miconsdir
install -d %buildroot/%_iconsdir
install -d %buildroot/%_liconsdir
bzcat %SOURCE16 > %buildroot/%_miconsdir/%nami.png
bzcat %SOURCE32 > %buildroot/%_iconsdir/%nami.png
bzcat %SOURCE48 > %buildroot/%_liconsdir/%nami.png

# debian menu file
install -d %buildroot/%_menudir
cat << EOF > %buildroot/%_menudir/%name
?package(%name):command="%_bindir/%name" \
icon="big-forth.png"  needs="text" section="More Applications/Development/Interpreters" \
title="bigForth" longtitle="%summary - Shell" xdg="true" 
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{title}
Comment=%summary - Shell
Exec=%{_bindir}/%{name} 
Icon=big-forth
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Development-Interpreters;Development
EOF


%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc BUGS COPYING CREDITS README ToDo
%_bindir/*
%_prefix/lib/%name
%_iconsdir/*
%_menudir/*
%{_datadir}/applications/mandriva-%{name}.desktop

