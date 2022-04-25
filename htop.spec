Name:		htop
Version:	3.1.2
Release:	1
Summary:	htop - an interactive process viewer
License:	GPLv2
URL:		https://htop.dev
Source0:	https://github.com/htop-dev/htop/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: perl perl-PathTools ncurses-devel autoconf automake gcc

%description
htop is a cross-platform interactive process viewer.
htop allows scrolling the list of processes vertically and horizontally to see their full command lines and related information like memory and CPU consumption.
The information displayed is configurable through a graphical setup and can be sorted and filtered interactively.
Tasks related to processes (e.g. killing and renicing) can be done without entering their PIDs.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/htop.svg
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.gz

%changelog
* Mon Apr 25 2022 wangkai <wangkai@h-partners.com> - 3.1.2-1
- Update version to 3.1.2

* Tue Jul 8 2021 xuguangmin <xuguangmin@kylinos.cn> - 3.0.5-3
- Update version to 3.0.5

* Mon Jun 7 2021 baizhonggui <baizhonggui@huawei.com> - 3.0.2-2
- Fix building error: ./autogen.sh: line 3: autoreconf: command not found
- Add autoconf/automake/gcc in BuildRequires

* Thu Sep 24 2020 Zhipeng Xie <xiezhipeng1@huawei.com> - 3.0.2-1
- Package init
