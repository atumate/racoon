#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from time import gmtime, strftime
from sqlalchemy.sql import select


engine = create_engine('mysql://root:123@localhost/racoon')


metadata = MetaData()
urls=Table('urls',metadata,
	Column('id',Integer,primary_key=True),
	Column('time',String(20)),
	Column('url',String(128),unique=True), # too short, comprise
	)
url_detail=Table('url_detail',metadata,
	Column('id',Integer,primary_key=True),
	Column('time',String(20)),
	Column('url',String(2084)),
	Column('raw_req',String(4096)),
	Column('raw_res',String(4096)),
	Column('status_code',String(3)),
	)
metadata.create_all(engine, checkfirst=True)

conn = engine.connect()
cur_time=strftime("%Y-%m-%d %H:%M:%S", gmtime())


# r_urls_ins=conn.execute(urls.insert(),time=cur_time, url='http://nixni.cc')

result = conn.execute(select([urls]))


for row in result:
	print(row)


# print(dir(r_urls))
# print(r_urls.returns_rows)













print('-->db_here<--')