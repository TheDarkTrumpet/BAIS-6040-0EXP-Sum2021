# Advanced Flask

## Purpose

This is a demonstration of doing both GET and POST operations, with a SQL backend, and supporting
both normal/web and API calls.

## Dependencies

* Flask
* SQLAlchemy

## Getting Started

1.  Install Flask and SQL Alchemy (pip install)
2.  cd into the directory and type `python app.py`

## Understanding and Points of Interest

I recommend you start with the `app.py`, as it's the switchboard for everything else.  The `lib` directory is where libraries are stored at.  the `db.py` are the interfaces with the database, where `People.py` is the model object for the People table within the database.

PyCharm definitely helps here, setting breakpoints and going from there.  Please see the video on ICON if you need further explanations.
