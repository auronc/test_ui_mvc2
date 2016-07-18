
ui:
	mkdir -p gen
	pyuic5 main_view.ui -o gen/ui_MainView.py

run:
	@python3 main_app.py	

clean:
	rm -rf gen
	rm -rf __pycache__
