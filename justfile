clean:
	rm -rf ./output
	rm -f dirtyFakeName_50K.csv

# make your FakeName_50K.csv file dirty. required python3 and the pandas library.
dirty:
	python3 tools/DirtierCSV.py

