#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Database(object):

    @classmethod
    def create(cls, db, dbname):
        if db == 'mysql':
            import mysql
            return mysql.MySQL(dbname)
        elif db == 'postgresql':
            import postgresql
            return postgresql.PostgreSQL(dbname)

