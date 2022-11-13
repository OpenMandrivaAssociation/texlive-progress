Name:		texlive-progress
Version:	19519
Release:	1
Summary:	Creates an overview of a document's state
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/progress
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/progress.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/progress.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Progress is a package which. when compiling TeX and LaTeX
documents, generates a HTML file showing an overview of a
document's state (of how finished it is). The report is sent to
file \ProgressReportName, which is by default the \jobname with
the date appended (but is user-modifiable).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/progress/progress.sty
%doc %{_texmfdistdir}/doc/latex/progress/README
%doc %{_texmfdistdir}/doc/latex/progress/progress.pdf
%doc %{_texmfdistdir}/doc/latex/progress/progress.tex
%doc %{_texmfdistdir}/doc/latex/progress/progress20030701.html

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
