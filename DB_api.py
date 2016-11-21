# *.* coding: utf-8 *.*
"""

"""

import MySQLdb
import config
import sys

class DB_api():
    def __init__(self):
        self.DB_NAME = config.DB_NAME
        self.DB_HOST = config.DB_HOST
        self.DB_USER = config.DB_USER
        self.DB_US_PASS = config.DB_US_PASS
        try:
            self.DB_CONN = self.db_conn()
        except Exception as e:
            print("Initial connection to database failed due to %s" % e)

    def db_conn(self):
        try:
            DB_CONN = MySQLdb.connect(host=self.DB_HOST,
                                      user=self.DB_USER,
                                      passwd=self.DB_US_PASS,
                                      db=self.DB_NAME)
        except Exception as e:
            print("USER:%s login failed due to %s" % (self.DB_USER, e))
            sys.exit(127)
        else:
            print("Login as USER: %s" % self.DB_USER)
            return DB_CONN
            sys.exit(0)

    def db_desc(self, tablename=''):
        if tablename == None:
            print("No tablename given")
            sys.exit(126)
        else:
            try:
                cmd = "desc %s" % tablename
                cursor = self.DB_CONN.cursor()
                ret_code = cursor.execute(cmd)
                print("CMD return code: %s." % ret_code)
                desc = [filed for filed in cursor]
                return desc
            except Exception as e:
                print("Failed to get desc due to %s" % e)


    def db_filed(self, tablename=''):
        if tablename == None:
            print("No tablename given")
            sys.exit(126)
        else:
            try:
                cmd = "desc %s" % tablename
                cursor = self.DB_CONN.cursor()
                ret_code = cursor.execute(cmd)
                print("CMD return code: %s." % ret_code)
                desc = [ filed[0] for filed in cursor]
                return desc
            except Exception as e:
                print("Failed to get desc due to %s" % e)
                sys.exit(127)

    def tb_select(self, tablename='*', sel_condition='*', where_condition=''):
        """
        scenario:
            > select condition_1(count(data(*))) from table (where condition_2)
        """
        if tablename == None:
            print("No tablename given")
            sys.exit(126)
        else:
            try:
                cmd = "SELECT %s FROM %s %s" % (sel_condition, tablename, where_condition)
                cursor = self.DB_CONN.cursor()
                ret_code = cursor.execute(cmd)
                print("CMD return code: %s." % ret_code)
                for result in cursor.fetchall():
                    print(result)
            except Exception as e:
                print("Failed selecting table due to %s" % e )
                sys.exit(127)

    def tb_delete(self, tablename='*', del_condition=''):
        """
        scenario:
            > delete from table (where condition_1)
        """
        if tablename == None:
            print("No tablename given")
            sys.exit(126)
        else:
            cursor = self.DB_CONN.cursor()
            try:
                cmd = "DELETE FROM %s %s" % (tablename,del_condition)
                ret_code = cursor.execute(cmd)
                print("CMD return code: %s." % ret_code)
            except Exception as e:
                print("Failed deleting data from table %s with delete conditions: %s due to %s\n" % (tablename, del_condition, e))
                cursor.rollback()
                sys.exit(127)
            else:
                cursor.commit()
                sys.exit(0)

    def tb_update(self, tablename='',assignments=''):
        """
        scenario:
            > update from table (where condition_1)
        """
        if tablename == None:
            print("No tablename given")
            sys.exit(126)
        else:
            cursor = self.DB_CONN.cursor()
            try:
                cmd = "UPDATE %s SET %s" % (tablename,assignments)
                ret_code = cursor.execute(cmd)
                print("CMD return code: %s." % ret_code)
            except Exception as e:
                print("Failed updating data to table %s as assignments: %s due to %s\n" % (tablename, assignments, e))
                cursor.rollback()
                sys.exit(127)
            else:
                cursor.commit()
                sys.exit(0)

    def tb_insert(self, tablename='', table_fields='', new_value=''):
        """
        scenario:
            > INSERT INTO TABLE (COL_1,COL_2) VALUES (1,2)
            > e.g : "INSERT INTO %s %s VALUES %s" % ('table1','(column1, column2)','(2,2)')
        """
        if tablename == None:
            print("No tablename given")
            sys.exit(126)
        else:
            cursor = self.DB_CONN.cursor()
            try:
                cmd = "INSERT INTO %s %s VALUES %s" % (tablename,table_fields,new_value)
                ret_code = cursor.execute(cmd)
                print("CMD return code: %s." % ret_code)
            except Exception as e:
                print("Failed insert data to table %s with value: %s due to %s\n" % (tablename, new_value, e))
                cursor.rollback()
                sys.exit(127)
            else:
                cursor.commit()
                sys.exit(0)

    def cmd_exec(self,cmd):
        """
        scenario:
            * execute cmd when cmd not matching above listed function
        """
        if 'drop' in cmd.lower():
            print("Forbidden drop cmd!!!\n")
            exit()
        elif isinstance(cmd, str):
            cursor = self.DB_CONN.cursor()
            try:
                ret_code = cursor.execute(cmd)
                print("CMD return code: %s." % ret_code)
            except Exception as e:
                print("Failed execute cmd: %s  due to %s" % (cmd, e))
                cursor.rollback()
                sys.exit(127)
            else:
                print("cmd:%s run success!\n")
                cursor.commit()
                sys.exit(0)

    def __del__(self):
        self.DB_CONN.close()


