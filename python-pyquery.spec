%define 	module	pyquery
Summary:	PyQuery - A jquery-like library for python
Summary(pl.UTF-8):	PyQuery
Name:		python-%{module}
Version:	0.3.1
Release:	5
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/pyquery/%{module}-%{version}.tar.gz
# Source0-md5:	6fce9d759b44a9963eb39eda31aa10d7
URL:		http://pypi.python.org/pypi/pyquery
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-lxml
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

%description -l pl.UTF-8

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_datadir} $RPM_BUILD_ROOT%{_libdir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/pyquery-*.egg-info
%endif
