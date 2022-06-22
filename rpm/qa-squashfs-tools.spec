
Name:		qa-squashfs-tools
Summary:	Utility for the creation of squashfs filesystems
Version:	4.3
Release:	1
License:	GPLv2+
Group:		System Environment/Base
URL:		https://github.com/mer-qa/qa-squashfs-tools
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	zlib-devel
BuildRequires:	xz-devel
BuildRequires:	lzo-devel
BuildRequires:	libattr-devel

Provides:	squashfs-tools
Conflicts:	squashfs-tools

%description
Squashfs is a highly compressed read-only filesystem for Linux. This package
contains the utilities for manipulating squashfs filesystems.

%prep
%setup -q

%build
XZ_SUPPORT=1 LZO_SUPPORT=1 LZMA_XZ_SUPPORT=1 make -C squashfs-tools/squashfs-tools %{?jobs:-j%jobs}

%install
install -D -m 755 squashfs-tools/squashfs-tools/mksquashfs %{buildroot}%{_sbindir}/mksquashfs
install -D -m 755 squashfs-tools/squashfs-tools/unsquashfs %{buildroot}%{_sbindir}/unsquashfs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc squashfs-tools/README squashfs-tools/COPYING

%{_sbindir}/mksquashfs
%{_sbindir}/unsquashfs
