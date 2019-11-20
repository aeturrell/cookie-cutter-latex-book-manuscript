# cookie-cutter-latex-book
An example book manuscript in latex with chapters (+ word count stats by chapter via a git pre-commit hook), a bibliography, support for figures, and export to Microsoft Word format via pandoc. Exports to MS Word include citations and chapter hyerlinks but do not retain citation hyperlinks or cited-on page numbers in the bibliography.

## How to use
1. git clone the repo
2. Make sure you have pandoc, pandoc-crossref, a tex distribution, and conda installed
3. `conda env create -f cclb_env.yml` -- this creates the Python environment for running the word count
4. Replace text in `.git/hooks/` directory as below
5. To export to word, run book_to_word_script.sh -- this takes the styles in ref.docx and exports the tex in book_compiler to exported_word/book.docx
6. When you commit a change to git, the python script will automatically populate book_word_stats.html, a table of progress toward writing target

## Chapter-by-chapter word count via git hook

It may seem like overkill to have a python script to do a tex word count. However, to get chapter-by-chapter stats, this seemed like the cleanest way, and could easily be extended with nicer visualisations.

#### Script changes you need to make

All git repos come with a hidden directory `.git/hooks/`. Within that folder there are some example scripts. Open the pre-commit hook named `pre-commit.sample` and replace the contents with:

```
conda activate cclb_env
python precommit/word_count.py
```

## LaTeX book manuscript

I am indebted to John Bissell, discoverer of the [eponymous instability](https://doi.org/10.1103/PhysRevLett.105.175001), for the original latex template that, heavily modified, is used here.

It provides a title page, chapters, references, and double-sided A4 text.

It is not the most pretty book latex template out there - and that's entirely on purpose. The idea is to produce something useful for editing, not for publishing. So the latex is stripped down to the minimum that will happily be exported to Word or other formats, ignoring all but the most essential bells and whistles (like citations).

## How tex-to-docx works
The magic line is 
`pandoc -s -N --reference-doc ref.docx -F pandoc-crossref -Mchapters book_compiler.tex --bibliography=book_bibliography.bib --csl=ieee.csl -o exported_word/book.docx`

- `-s` tells pandoc to make a standalone document
- `-N` enforces numbering (though not in docx, it's included here in case of other output formats being used)
- `--reference-doc` tells pandoc to use styles from a reference word doc (can also be used with .odt)
- `-F` calls a pandoc filter, in this case pandoc-crossref
- `-Mchapters` tells this filter to use chapters
- `*.tex` is the input file
- `--bibliography=*.bib` tells pandoc where to find citations
- `--csl=*.csl` is the name of the style file for citations
- `-o` means output, in this case a word document

## Improvements

Have an improvement? Get in touch!