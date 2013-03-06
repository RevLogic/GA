all: clean paper

clean:
	rm -rf *.pdf *~ *.aux

paper:
	pdflatex -draft main > /dev/null
	bibtex main
	pdflatex main
	okular main.pdf
