#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (some using network)
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define 	module	pyquery
Summary:	A jquery-like library for Python
Summary(pl.UTF-8):	Podobna do jquery biblioteka dla Pythona
Name:		python-%{module}
Version:	1.4.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyquery/
Source0:	http://files.pythonhosted.org/packages/source/p/pyquery/%{module}-%{version}.tar.gz
# Source0-md5:	a4aec587d6dcb01cf6fb7564bcedd2b7
URL:		http://pypi.org/project/pyquery/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-WebOb
BuildRequires:	python-cssselect > 0.7.9
BuildRequires:	python-lxml >= 2.1
BuildRequires:	python-nose
BuildRequires:	python-webtest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-WebOb
BuildRequires:	python3-cssselect > 0.7.9
BuildRequires:	python3-lxml >= 2.1
BuildRequires:	python3-nose
BuildRequires:	python3-webtest
%endif
%endif
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

%description -l pl.UTF-8
Pyquery pozwala na wykonywanie zapytań jquery na dokumentach XML.
Interfejs jest jak to tylko możliwe podobny do jquery. Pyquery używa
lxml do szybkiej manipulacji plików XML i HTML.

%package -n python3-%{module}
Summary:	A jquery-like library for Python
Summary(pl.UTF-8):	Podobna do jquery biblioteka dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
Pyquery allows you to make jquery queries on xml documents. The API is
as much as possible the similar to jquery. pyquery uses lxml for fast
xml and html manipulation.

%description -n python3-%{module} -l pl.UTF-8
Pyquery pozwala na wykonywanie zapytań jquery na dokumentach XML.
Interfejs jest jak to tylko możliwe podobny do jquery. Pyquery używa
lxml do szybkiej manipulacji plików XML i HTML.

%package apidocs
Summary:	API documentation for Python pyquery module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pyquery
Group:		Documentation

%description apidocs
API documentation for Python pyquery module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pyquery.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.txt README.rst
%{py_sitescriptdir}/pyquery
%{py_sitescriptdir}/pyquery-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES.rst LICENSE.txt README.rst
%{py3_sitescriptdir}/pyquery
%{py3_sitescriptdir}/pyquery-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
