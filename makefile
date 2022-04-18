build:
	pipenv run pyinstaller -DFwn AhagonTypeWritter ./main.py

build-windows:
	pipenv run pyinstaller -DFwn AhagonTypeWritter --icon=".\assets\icon.ico" ./main.py
