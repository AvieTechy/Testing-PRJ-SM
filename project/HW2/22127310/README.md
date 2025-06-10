# LaTeX Report Template Documentation

## Section Numbering

This template has been updated to use the `article` document class, which provides a more intuitive mapping between Markdown headers and LaTeX section levels:

- `# Heading` in Markdown becomes `\section` in LaTeX, numbered as 1, 2, 3, etc.
- `## Heading` in Markdown becomes `\subsection` in LaTeX, numbered as 1.1, 1.2, etc.
- `### Heading` in Markdown becomes `\subsubsection` in LaTeX, numbered as 1.1.1, 1.1.2, etc.
- `#### Heading` in Markdown becomes `\paragraph` in LaTeX
- `##### Heading` in Markdown becomes `\subparagraph` in LaTeX

### Basic Section Numbering Options

```yaml
# Enable or disable section numbering
numbersections: true

# Control the depth of section numbering
# 1 = Number only main sections (H1)
# 2 = Number main sections and subsections (H1, H2)
# 3 = Number main sections, subsections, and subsubsections (H1, H2, H3)
# And so on...
secnumdepth: 3
```

### Table of Contents Options

```yaml
# Enable or disable table of contents
toc: true

# Control the depth of headings included in the table of contents
# 1 = Include only main sections (H1)
# 2 = Include main sections and subsections (H1, H2)
# 3 = Include main sections, subsections, and subsubsections (H1, H2, H3)
toc-depth: 3

# Custom title for the table of contents
toc-title: "Table of Contents"

# Start table of contents on a new page
toc-newpage: true

# Add a page break after the table of contents
toc-afterclear: true

# Color for TOC links
toccolor: "blue"
```

### Heading Structure

When creating your Markdown content files, use the following heading structure:

```markdown
# Main Section (H1)
Text content...

## Subsection (H2)
Text content...

### Subsubsection (H3)
Text content...

#### Paragraph (H4)
Text content...
```

The numbering depth will be controlled by the `secnumdepth` setting. For example, if `secnumdepth: 2`, then only H1 and H2 headings will be numbered.

### File Organization

For proper section numbering across multiple files, name your content files with numeric prefixes to control their order:

```
content/
  1_introduction.md
  2_methods.md
  3_results.md
  4_discussion.md
  5_conclusion.md
```

The template will concatenate these files in alphabetical order when generating the document.

### Language Support

The template also supports switching between Vietnamese and English. This affects labels such as "Table of Contents" and date formats:

```yaml
# Language selection (choose one)
langvi: false  # Set to true for Vietnamese
langen: true   # Set to true for English
```

### Font and Color Settings

The template uses the Latin Modern font family (an enhanced version of Computer Modern) by default. This provides a professional, academic appearance that works well with section numbering.
