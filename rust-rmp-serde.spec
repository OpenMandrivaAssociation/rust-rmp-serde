# Generated by rust2rpm 13
%bcond_without check
%global debug_package %{nil}

%global crate rmp-serde

Name:           rust-%{crate}
Version:        0.14.2
Release:        1%{?dist}
Summary:        Serde bindings for RMP

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/rmp-serde
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Serde bindings for RMP.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc CHANGELOG.md
%license LICENSE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Feb 06 2020 Josh Stone <jistone@redhat.com> - 0.14.2-1
- Update to 0.14.2

* Thu Jan 30 2020 Josh Stone <jistone@redhat.com> - 0.14.1-1
- Update to 0.14.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 15 18:23:43 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.14.0-1
- Release 0.14.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 10:10:14 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.7-4
- Regenerate

* Sun May 12 08:53:53 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.7-3
- Update serde_bytes to 0.11

* Thu Apr 11 14:38:20 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.13.7-2
- Run tests in infrastructure

* Thu Mar 28 08:57:13 CET 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.13.7-1
- Initial package
