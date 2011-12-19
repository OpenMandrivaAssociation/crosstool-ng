Name:		crosstool-ng
Version:	1.13.2
Release:	1
License:	GPL
Group:		Development/C
Summary:	Crosstool-NG aims at building toolchains
Source0:	%{name}-%{version}.tar.bz2
Requires:	awk, sed, bison, flex, autoconf, automake
BuildRequires:	fdupes curl-devel

%description
crosstool-NG aims at building toolchains. Toolchains are an essential component in a software development project. It will compile,
assemble and link the code that is being developed. Some pieces of the toolchain will eventually end up in the resulting
binary/ies: static libraries are but an example.

%package	devel
Summary:	Crosstool-NG aims at building toolchains
Group:		Development/C
Requires:	%name = %version

%description devel
crosstool-NG aims at building toolchains. Toolchains are an essential component in a software development project. It will compile,
assemble and link the code that is being developed. Some pieces of the toolchain will eventually end up in the resulting
binary/ies: static libraries are but an example.


%prep
%setup -q

%build
./configure --bindir=%{_bindir} --libdir=%{_libdir} --prefix=%{_prefix}
%make

%install
%makeinstall_std
#f dupes %{buildroot}

%files
%dir %{_libdir}/ct-ng-%{version}
%{_mandir}/man1/*
%{_docdir}/ct-ng-%{version}
%{_bindir}/*

%files devel
%{_libdir}/ct-ng-%{version}/*
