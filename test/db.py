#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from time import localtime, strftime
from sqlalchemy.sql import select
import logging

print('-->db.py start')

logging.basicConfig(filename='log.txt',
	level=logging.DEBUG,
	format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
	datefmt='%m-%d %H:%M',
	)

engine = create_engine('mysql://root:123@localhost/racoon')

metadata = MetaData()
targets=Table('targets',metadata,
	Column('id',Integer,primary_key=True),
	Column('time',String(20)),
	Column('target',String(128),unique=True), # too short, comprise
	)

metadata.create_all(engine, checkfirst=True)

conn = engine.connect()
cur_time = strftime("%Y-%m-%d %H:%M:%S", localtime())

def get_target(id):
	result = conn.execute(
		select([targets]).where(targets.c.id == id)
		)
	return result

def get_targets():
	result = conn.execute(select([targets]))
	return result

def add_target(target_new):
	try:
		r_i_target=conn.execute(targets.insert(),
			time=cur_time, 
			target=target_new,
			)
	except Exception as e:
		logging.debug(e)
		return -1
	else:
		pk=r_i_target.inserted_primary_key
		return pk[0]

def rm_target(id):
	try:
		r_d_target=conn.execute(
			targets.delete().where(targets.c.id == id)
			)
	except Exception as e:
		logging.debug(e)
		return -1
	else:
		return r_d_target.rowcount






# rm_target(25)
# add_target('vgv')


print('<--db.py end')