.PHONY: install run_gui clean

install:
	@echo "Installing dependencies..."
	pip install -r src/requirements.txt

run_gui:
	@echo "Running GUI application..."
	python3 src/gui.py

clean:
	@echo "Cleaning up..."
	rm -f src/resultats_des_sorties.csv



