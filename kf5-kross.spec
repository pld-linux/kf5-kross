#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	5.105
%define		qtver		5.15.2
%define		kfname		kross
#
Summary:	Embedding of scripting into applications
Name:		kf5-%{kfname}
Version:	5.105.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/portingAids/%{kfname}-%{version}.tar.xz
# Source0-md5:	51261fac3cdae77dbac890230fb863a4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Network-devel >= 5.2.0
BuildRequires:	Qt5Script-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-attica-devel >= %{version}
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	kf5-karchive-devel >= %{version}
BuildRequires:	kf5-kauth-devel >= %{version}
BuildRequires:	kf5-kbookmarks-devel >= %{version}
BuildRequires:	kf5-kcodecs-devel >= %{version}
BuildRequires:	kf5-kcompletion-devel >= %{version}
BuildRequires:	kf5-kconfig-devel >= %{version}
BuildRequires:	kf5-kconfigwidgets-devel >= %{version}
BuildRequires:	kf5-kcoreaddons-devel >= %{version}
BuildRequires:	kf5-kdbusaddons-devel >= %{version}
BuildRequires:	kf5-kdoctools-devel >= %{version}
BuildRequires:	kf5-kglobalaccel-devel >= %{version}
BuildRequires:	kf5-kguiaddons-devel >= %{version}
BuildRequires:	kf5-ki18n-devel >= %{version}
BuildRequires:	kf5-kiconthemes-devel >= %{version}
BuildRequires:	kf5-kio-devel >= %{version}
BuildRequires:	kf5-kitemviews-devel >= %{version}
BuildRequires:	kf5-kjobwidgets-devel >= %{version}
BuildRequires:	kf5-knotifications-devel >= %{version}
BuildRequires:	kf5-kparts-devel >= %{version}
BuildRequires:	kf5-kservice-devel >= %{version}
BuildRequires:	kf5-ktextwidgets-devel >= %{version}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf5-kwindowsystem-devel >= %{version}
BuildRequires:	kf5-kxmlgui-devel >= %{version}
BuildRequires:	kf5-solid-devel >= %{version}
BuildRequires:	kf5-sonnet-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
Kross is a scripting bridge to embed scripting functionality into an
application. It supports QtScript as a scripting interpreter backend.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kfname}5

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{kfname}5.lang
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/kf5kross
%ghost %{_libdir}/libKF5KrossCore.so.5
%attr(755,root,root) %{_libdir}/libKF5KrossCore.so.*.*.*
%ghost %{_libdir}/libKF5KrossUi.so.5
%attr(755,root,root) %{_libdir}/libKF5KrossUi.so.*.*.*
%attr(755,root,root) %{qt5dir}/plugins/krossmoduleforms.so
%attr(755,root,root) %{qt5dir}/plugins/krossmodulekdetranslation.so
%attr(755,root,root) %{qt5dir}/plugins/krossqts.so
%attr(755,root,root) %{qt5dir}/plugins/script/krossqtsplugin.so
%{_mandir}/man1/kf5kross.1*
%lang(ca) %{_mandir}/ca/man1/kf5kross.1*
%lang(de) %{_mandir}/de/man1/kf5kross.1*
%lang(es) %{_mandir}/es/man1/kf5kross.1*
%lang(it) %{_mandir}/it/man1/kf5kross.1*
%lang(nl) %{_mandir}/nl/man1/kf5kross.1*
%lang(pt) %{_mandir}/pt/man1/kf5kross.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kf5kross.1*
%lang(sv) %{_mandir}/sv/man1/kf5kross.1*
%lang(uk) %{_mandir}/uk/man1/kf5kross.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/KrossCore
%{_includedir}/KF5/KrossUi
%{_includedir}/KF5/kross_version.h
%{_libdir}/cmake/KF5Kross
%{_libdir}/libKF5KrossCore.so
%{_libdir}/libKF5KrossUi.so
%{qt5dir}/mkspecs/modules/qt_KrossCore.pri
%{qt5dir}/mkspecs/modules/qt_KrossUi.pri
