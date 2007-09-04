Summary:	TriX - VypressChat(TM) compatible chat
Name:		trix
Version:	0.92
Release:	%mkrel 1
Epoch:		1
License: 	GPL
Group:		Networking/Chat
URL:		http://trix.sourceforge.net
Source0:	http://downloads.sourceforge.net/trix/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
BuildRequires:	libqt-devel
BuildRequires:	libxt-devel
BuildRequires:	libxi-devel
BuildRequires:	libxmu-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description 
TriX is a serverless text chat, dedicated to using in small home or 
office LAN's, that runs on Linux using Qt/X11 library. It is compatible 
with Vypress Chat(TM) for Windows. 

%prep
%setup -qn %{name}-%{version}

%build

%configure2_5x \
    --disable-rpath \
    --with-Qt-dir=%{_prefix}/lib/qt3 \
    --with-qt-libraries=%{_prefix}/lib/qt3/%{_lib}

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

%makeinstall_std
install -D %{SOURCE1} %{buildroot}%{_datadir}/applications
cp %{buildroot}%{_datadir}/%{name}/gfx/default.png %{buildroot}%{_datadir}/pixmaps/trix.png

%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion >= 200700
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README COPYING INSTALL 
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/avatars/*
%{_datadir}/%{name}/gfx/*
%{_datadir}/%{name}/snd/*
%{_datadir}/%{name}/tr/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.png
