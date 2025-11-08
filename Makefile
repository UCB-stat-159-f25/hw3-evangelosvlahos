BUILD_DIR = _build
AUDIO_DIR = audio
FIGURES_DIR = figures


ENV_NAME := ligo
ENV_FILE := environment.yml


env:
	@echo ">>> Updating Conda environment: $(ENV_NAME)"
	@if conda env list | grep -q "$(ENV_NAME)"; then \
		echo "Environment '$(ENV_NAME)' exists. Updating..."; \
		conda env update -n $(ENV_NAME) -f $(ENV_FILE) --prune; \
	else \
		echo "Environment '$(ENV_NAME)' does not exist. Creating..."; \
		conda env create -n $(ENV_NAME) -f $(ENV_FILE); \
	fi
	@echo "Environment '$(ENV_NAME)' configured."

clean:
	 rm -rf $(BUILD_DIR)
	 rm  -f $(AUDIO_DIR)/*
	 rm  -f $(FIGURES_DIR)/*

html:
	 myst build --html
