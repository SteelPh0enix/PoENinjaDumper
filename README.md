# PoE.Ninja dumper

Very simple script which allows you to easely get fresh [poe.ninja](https://poe.ninja/) data into single spreadsheet!

Features:

* Dumping the data to .ods spreadsheet
* Updating the spreadsheet (see remarks)

## Dependencies

You will need

* Python 3 (i used 3.7.1 for development, but i'm pretty sure any non-ancient version will be sufficent) with pip installed, and in `PATH`
* [Requests library](http://docs.python-requests.org/en/master/): `pip install requests` (or `python -m pip install requests`, if pip is not in `PATH`)
* [pyexcel-ods3](https://github.com/pyexcel/pyexcel-ods3): `pip install pyexcel-ods3` (or `python -m pip install pyexcel-ods3`, if pip is not in `PATH`)

## Usage

Either run as-is (double click and run with Python), or throught command line/shortcut.

With no arguments provided, script will create `PoENinjaData.ods` file in current directory. If you want to name it differently, pass it as first (and only) argument to the script (or change the filename in script itself):

`python ./ods_dump.py MySpreadsheet.ods`
*(you can achieve the same thing by creating shorcut and putting filename after executable path)*

## Additional scripts

There's a WIP script `filter_dump.py` that will dump the poe.ninja items from all categores in certain price-ranges in lootfilter-friendly format.

`poeninja_dumper.py` is now separate script that can be used in your own tools!

## Remarks and known bugs

When updating, script removes rows with no data, leaving only 1 row blank between, so it may break user-created tables/spreadsheets.

Before:
![Before updating](https://i.imgur.com/H2knRfa.png)
After:
![After updating](https://i.imgur.com/6OmoJ5v.png)

This bug is caused by pyexcel-ods library, so i can't really do much about it. Avoid making tables which leaves more than two rows blank, and everything should pretty much work. I'm not sure, however, if the library keeps formatting, colouring, and things like that (most probably nope), so be careful about that too. Maybe consider dumping data to other file, and copy-pasting important stuff if you intend to make fancy tables
