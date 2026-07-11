%global tl_name progress
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.10
Release:	%{tl_revision}.1
Summary:	Creates an overview of a documents state
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/progress
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/progress.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/progress.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Progress is a package which. when compiling TeX and LaTeX documents,
generates a HTML file showing an overview of a document's state (of how
finished it is). The report is sent to file \ProgressReportName, which
is by default the \jobname with the date appended (but is user-
modifiable).

