#!/usr/bin/env python

import json
from wmflabs import db

conn = db.connect('cswiki')

cur = conn.cursor()
with cur:
	sql = 'select count(*), pl_title from pagelinks where pl_title in (select page_title from page where page_id in (select cl_from from categorylinks where cl_to="Rozcestníky")) group by pl_title'
	cur.execute(sql)
	data = cur.fetchall()

print json.dumps(data, ensure_ascii=False)
