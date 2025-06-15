# CHANGE THIS TO YOUR REPORT NAME
OUTPUT_NAME = report

# Variables
PANDOC = pandoc
PDF_ENGINE = xelatex
OUTPUT_DIR = ./release
OUTPUT_PDF = $(OUTPUT_DIR)/$(OUTPUT_NAME).pdf
OUTPUT_TEX = $(OUTPUT_DIR)/$(OUTPUT_NAME).tex
OUTPUT_DOCX = $(OUTPUT_DIR)/$(OUTPUT_NAME).docx

# Font settings
MAINFONT = "Latin Modern Roman"
SANSFONT = "Latin Modern Sans"
MONOFONT = "Latin Modern Mono"

# Find all .md files in the content directory
MD_SOURCES = $(wildcard ./content/*.md)
METADATA_FILE = ./content/metadata.yaml
TEMPLATE_FILE = ./title/default_template.tex

# Common Pandoc options
PANDOC_FLAGS = \
	--metadata-file=$(METADATA_FILE) \
	--template=$(TEMPLATE_FILE) \
	--citeproc \
	--table-of-contents \
	--toc-depth=3 \
	--number-sections \
	--highlight-style=tango

# PDF-specific options
PDF_FLAGS = $(PANDOC_FLAGS) \
	--pdf-engine=$(PDF_ENGINE) \
	--variable mainfont=$(MAINFONT) \
	--variable sansfont=$(SANSFONT) \
	--variable monofont=$(MONOFONT) \
	--variable fontsize=11pt \
	--variable geometry:margin=1in \
	--variable links-as-notes=true

# Default target
all: clean $(OUTPUT_PDF)

# Rule to build the PDF
$(OUTPUT_PDF): $(MD_SOURCES) $(METADATA_FILE) $(TEMPLATE_FILE)
	@mkdir -p $(OUTPUT_DIR)
	$(PANDOC) $(MD_SOURCES) $(PDF_FLAGS) -o $@
	@echo "PDF created: $(OUTPUT_PDF)"

# Rule to build the TEX file
$(OUTPUT_TEX): $(MD_SOURCES) $(METADATA_FILE) $(TEMPLATE_FILE)
	@mkdir -p $(OUTPUT_DIR)
	$(PANDOC) $(MD_SOURCES) $(PANDOC_FLAGS) -o $@
	@echo "TEX created: $(OUTPUT_TEX)"

# Rule to build DOCX file
$(OUTPUT_DOCX): $(MD_SOURCES) $(METADATA_FILE)
	@mkdir -p $(OUTPUT_DIR)
	$(PANDOC) $(MD_SOURCES) $(PANDOC_FLAGS) --reference-doc=reference.docx -o $@
	@echo "DOCX created: $(OUTPUT_DOCX)"

# Target for generating TEX file
tex: $(OUTPUT_TEX)

# Target for generating DOCX file
docx: $(OUTPUT_DOCX)

# Run Pandoc with version info
version:
	$(PANDOC) --version

# Phony target for cleaning up
.PHONY: clean all tex docx version
clean:
	@rm -f $(OUTPUT_PDF) $(OUTPUT_TEX) $(OUTPUT_DOCX)
	@echo "Output files removed"
