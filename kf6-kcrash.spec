%define libname %mklibname KF6Crash
%define devname %mklibname KF6Crash -d
%define git 20230513

Name: kf6-kcrash
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kcrash/-/archive/master/kcrash-master.tar.bz2#/kcrash-%{git}.tar.bz2
Summary: Graceful handling of application crashes
URL: https://invent.kde.org/frameworks/kcrash
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6CoreAddons)
Requires: %{libname} = %{EVRD}

%description
Graceful handling of application crashes

%package -n %{libname}
Summary: Graceful handling of application crashes
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Graceful handling of application crashes

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Graceful handling of application crashes

%prep
%autosetup -p1 -n kcrash-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/kcrash.*

%files -n %{devname}
%{_includedir}/KF6/KCrash
%{_libdir}/cmake/KF6Crash
%{_qtdir}/mkspecs/modules/qt_KCrash.pri
%{_qtdir}/doc/KF6Crash.*

%files -n %{libname}
%{_libdir}/libKF6Crash.so*
