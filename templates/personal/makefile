# CHANGE THIS TO YOUR REPORT NAME
OUTPUT_NAME = 22127444_DomainTesting

# Variables
PANDOC = pandoc
PDF_ENGINE = xelatex
OUTPUT_DIR = ./release
OUTPUT_PDF = $(OUTPUT_DIR)/$(OUTPUT_NAME).pdf
OUTPUT_TEX = $(OUTPUT_DIR)/$(OUTPUT_NAME).tex

# Font settings
MAINFONT = "Latin Modern Roman"
SANSFONT = "Latin Modern Sans"
MONOFONT = "Latin Modern Mono"

# Find all .md files in the content directory
MD_SOURCES = $(wildcard ./content/*.md)
METADATA_FILE = ./content/metadata.yaml
TEMPLATE_FILE = ./title/default_template.tex

PANDOC_FLAGS = \
	--metadata-file=$(METADATA_FILE) \
	--template=$(TEMPLATE_FILE)

PDF_FLAGS = $(PANDOC_FLAGS) --pdf-engine=$(PDF_ENGINE)

# Default target
all: $(OUTPUT_PDF)

# Rule to build the PDF
$(OUTPUT_PDF): $(MD_SOURCES) $(METADATA_FILE) $(TEMPLATE_FILE)
	@mkdir -p $(OUTPUT_DIR)
	$(PANDOC) $(MD_SOURCES) $(PDF_FLAGS) -o $@

# Rule to build the TEX file
$(OUTPUT_TEX): $(MD_SOURCES) $(METADATA_FILE) $(TEMPLATE_FILE)
	@mkdir -p $(OUTPUT_DIR)
	$(PANDOC) $(MD_SOURCES) $(PANDOC_FLAGS) -o $@

# Target for generating TEX file
tex: $(OUTPUT_TEX)

# Phony target for cleaning up
.PHONY: clean all tex
clean:
	rm -f $(OUTPUT_PDF) $(OUTPUT_TEX)
