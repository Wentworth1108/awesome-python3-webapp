
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'Wen Shuai'

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
	return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
	__table__ = 'users'

	id = StringField(primary_key=True, default=next_id, ddl='vachar(50)')
	email = StringField(ddl='vachar(50)')
	passwd = StringField(ddl='vachar(50)')
	admin = BooleanField()
	name = StringField(ddl='vachar(50)')
	image = StringField(ddl='vachar(500)')
	create_at = FloatField(default=time.time)

class Bolg(Model):
	__table__ = 'blogs'

	id = StringField(primary_key=True, default=next_id, ddl='vachar(50)')
	user_id = StringField(ddl='vachar(50)')
	user_name = StringField(ddl='vachar(50)')
	user_image = StringField(ddl='vachar(500)')
	name = StringField(ddl='vachar(50)')
	summary = (ddl='vachar(200)')
	content = TextField()
	create_at = FloatField(default=time.time)

class Comment(Model):
	__table__ = 'comments'

	id = StringField(primary_key=True, default=next_id, ddl='vachar(50)')
	blog_id = StringField(ddl='vachar(50)')
	user_id = StringField(ddl='vachar(50)')
	user_name = StringField(ddl='vachar(50)')
	user_image = StringField(ddl='vachar(500)')
	content = TextField()
	create_at = FloatField(default=time.time)

		