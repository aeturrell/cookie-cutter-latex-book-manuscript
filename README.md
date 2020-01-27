# cookie-cutter-latex-book-manuscript
An example book manuscript in latex with chapters, word count stats by chapter, a bibliography, support for figures, and export to Microsoft Word format via pandoc. 

The idea is to keep the manuscript as simple as possible, but no simpler.

Exports to MS Word include citations and chapter hyerlinks but do not retain citation hyperlinks or cited-on page numbers in the bibliography.

## How to use
1. git clone the repo
2. Make sure you have python, pandoc, pandoc-crossref, and a tex distribution  installed
3. To do the word count, run ``python scripts/word_count.py``
4. To export the latex to word, run ``chmod +x scripts/ms_to_word`` followed by ``./scripts/ms_to_word.sh``

## LaTeX manuscript

I am indebted to John Bissell, discoverer of the [eponymous instability](https://doi.org/10.1103/PhysRevLett.105.175001), for the original latex template that, heavily modified, is used here.

It provides a title page, chapters, references, and double-sided A4 text.

It is not the most pretty book latex template out there - and that's entirely on purpose. The idea is to produce something useful for editing, not for publishing. So the latex is stripped down to the minimum that will happily be exported to Word or other formats, ignoring all but the most essential bells and whistles (like citations).

## Chapter-by-chapter word count

It may seem like overkill to have a python script to do a tex word count. However, to get chapter-by-chapter stats, this seemed like the cleanest way, and could easily be extended to incldue some nicer visualisations.

The python script will automatically populate book_word_stats.html, a table of progress toward writing target by chapter and in total.

The number of chapters is detected based on the number of *.tex files in ``chapters/`` but the overall number of words is set within the script.

#### Automated pre-commit word count

If you'd like to automate the word count, this is possible using pre-commit git hooks. This section explains how.

All git repos come with a hidden directory `.git/hooks/`. Within that folder there are some example scripts. Open the pre-commit hook named `pre-commit.sample` and replace the contents with:
```
#!/bin/sh
python scripts/word_count.py
```

## Exporting to Microsoft Word
Run ``chmod +x scripts/ms_to_word`` followed by ``./scripts/ms_to_word.sh``. This calls the magic line:

`pandoc -s -N --reference-doc ref.docx -F pandoc-crossref -Mchapters book_compiler.tex --bibliography=book_bibliography.bib --csl=nature.csl -o exported_word/book.docx`

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
