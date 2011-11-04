# revision 19519
# category Package
# catalog-ctan /macros/latex/contrib/progress
# catalog-date 2007-01-06 21:10:04 +0100
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-progress
Version:	1.10
Release:	1
Summary:	Creates an overview of a document's state
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/progress
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/progress.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/progress.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Progress is a package which. when compiling TeX and LaTeX
documents, generates a HTML file showing an overview of a
document's state (of how finished it is). The report is sent to
file \ProgressReportName, which is by default the \jobname with
the date appended (but is user-modifiable).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/progress/progress.sty
%doc %{_texmfdistdir}/doc/latex/progress/README
%doc %{_texmfdistdir}/doc/latex/progress/progress.pdf
%doc %{_texmfdistdir}/doc/latex/progress/progress.tex
%doc %{_texmfdistdir}/doc/latex/progress/progress20030701.html
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
