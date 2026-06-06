all: primitives_of_action.pdf fundamental_constants.pdf

primitives_of_action.pdf: primitives_of_action.tex references.bib
	pdflatex primitives_of_action.tex
	bibtex primitives_of_action
	pdflatex primitives_of_action.tex
	pdflatex primitives_of_action.tex

fundamental_constants.pdf: fundamental_constants.tex references.bib
	pdflatex fundamental_constants.tex
	bibtex fundamental_constants
	pdflatex fundamental_constants.tex
	pdflatex fundamental_constants.tex

clean:
	rm -f *.aux *.log *.out *.bbl *.blg *.toc *.pdf

.PHONY: all clean
