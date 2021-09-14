#!/usr.bin/python3

import pymysql

def schemaCreation(db):
	# Establish interface with database
	cursor = db.cursor()

	# Delete old versions of schema before 
	# adding new ones
	cursor.execute("drop table if exists universities")

	# Create new versions of the table schema
	universities_create = """create table universities(
		id int not null auto_increment,
		title text not null,
		summary text not null,
		image char,
		primary key(id));"""

	# Add the new table schema to the database
	curso.execute(universities_create)

	# Database schema created 
	return
