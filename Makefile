SHELL := /bin/bash
OUT_DIR = /opt/bendict/
all: install
	@:

install:
	@echo You must be root to install.
	@mkdir -p $(OUT_DIR)
	@cp BenDict.py $(OUT_DIR)/BenDict.py
	@cp -r db $(OUT_DIR)/db
	@cp -r icons $(OUT_DIR)/icons
	@cp bendict /usr/bin/bendict
	@chmod +x /usr/bin/bendict
	@cp bendict.desktop /usr/share/applications/bendict.desktop
	@echo Installation completed!

uninstall:
	@echo You must be root to uninstall.
	@rm -rf $(OUT_DIR)
	@rm -f /usr/bin/bendict
	@rm -f /usr/share/applications/bendict.desktop
	@echo Uninstallation completed!
