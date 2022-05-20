# Disable debuginfo as it causes issues with bundled gems that build libraries
%global debug_package %{nil}
%global repo_name ood-gimp
%global app_name ood-gimp
%{!?package_version: %define package_version %{major}.%{minor}.%{patch}}
%{!?package_release: %define package_release 1}
%{!?git_tag: %define git_tag v%{package_version}}
%define git_tag_minus_v %(echo %{git_tag} | sed -r 's/^v//')

Name:     ondemand-%{app_name}
Version:  %{package_version}
Release:  %{package_release}%{?dist}
Summary:  Batch Connect - ISU-HPC GIMP

Group:    System Environment/Daemons
License:  MIT
URL:      https://github.com/ISU-HPC/%{repo_name}
Source0:  https://github.com/ISU-HPC/%{repo_name}/archive/%{git_tag}.tar.gz

Requires: ondemand

# Disable automatic dependencies as it causes issues with bundled gems and
# node.js packages used in the apps
AutoReqProv: no

%description
An interactive app designed for ISU-HPC OnDemand that launches a GIMP GUI within an XFCE desktop session on an Owens batch node.


%prep
%setup -q -n %{repo_name}-%{git_tag_minus_v}


%build


%install
%__mkdir_p %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}
%__cp -a ./. %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}/
echo v%{version} > %{buildroot}%{_localstatedir}/www/ood/apps/sys/%{app_name}/VERSION


%files
%defattr(-,root,root)
%{_localstatedir}/www/ood/apps/sys/%{app_name}
%{_localstatedir}/www/ood/apps/sys/%{app_name}/manifest.yml


%changelog
* FRI May 20 2022 Yasasvy Nanyam <ynanyam@iastate.edu> 2.10.24
- New package added(ynanyam@iastate.edu)


