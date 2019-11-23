#!/bin/sh
pandoc -s -N --reference-doc ref.docx -F pandoc-crossref -Mchapters book_compiler.tex --bibliography=book_bibliography.bib --csl=ieee.csl -o exported_word/book.docx