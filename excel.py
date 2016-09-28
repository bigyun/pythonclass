#!/usr/bin/evn python
# -*- coding:utf-8 -*-

# Program: 从MySQL中查询数据并且保存生成到excel中
# Author : 陈浩
# Date   : 2016-01-15

import datetime, time
import mysql.connector
import xlwt
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 默认样式
default_style = xlwt.easyxf('''
  pattern: pattern solid;
  borders: left 1, right 1, top 1, bottom 1;
  align: horiz center''',
  num_format_str='0,000.00')

# 标题栏样式
title_style = xlwt.easyxf('''
  pattern: pattern solid, fore_colour yellow;
  font: name Times New Roman, color-index black, bold on;
  borders: left 1, right 1, top 1, bottom 1;
  align: horiz center''',
  num_format_str='0,000.00')

# 时间格式样式
time_style = xlwt.easyxf(num_format_str='YYYY-MM-DD h:mm:ss')

def get_sql():
  '''
  创建需要的sql语句
  '''
  sql = '''
    SELECT tmp.mobile_phone AS '电话号码',
      tmp.name AS '其中一个姓名',
      tmall_shop_info.name AS '品牌商名称',
      store.store_name AS '店铺名称',
      tmp.num AS '重复个数'
    FROM (
      SELECT mobile_phone,
        name,
        store_no,
        tmall_shop_id,
        COUNT(*) AS num
      FROM store_guide
      WHERE mobile_phone IS NOT NULL
      GROUP BY mobile_phone
      HAVING num > 1
    ) AS tmp
      LEFT JOIN tmall_shop_info USING(tmall_shop_id)
      LEFT JOIN store USING(store_no)
  '''
  return sql

def get_title(cursor):
  '''
  通过游标获得excel文件title
  '''
  return cursor.column_names

def get_select_data(cursor):
  '''
  通过游标获得数据列表(list)
  '''
  return [row for row in cursor]

def create_excel_title(work_sheet, title, title_style=None):
  '''
  生产exceltitle
  '''
  if not title_style:
    title_style = default_style
  for col_index, col_name in enumerate(title):
    work_sheet.write(0, col_index, col_name, title_style)
  return work_sheet

def create_excel_body(work_sheet, body, body_style=None):
  '''
  生成excel body信息
  '''
  if not title_style:
    body_style = default_style
  for row_num, row_data in enumerate(data, 1):
    for col_index, col_value in enumerate(row_data):
      work_sheet.write(row_num, col_index, col_value)
  return work_sheet

def get_col_max_length(data, title):
  '''
  获得数据每列最大值长度
  '''
  col_len = map(len, map(str, title))
  func = lambda x, y: y if y>x else x
  for row in data:
    row_len = map(len, map(str, row))
    col_len = map(func, col_len, row_len)
  return col_len

def set_work_sheet_col_len(work_sheet, max_len):
  '''
  设置列长度
  '''
  for col, len in enumerate(max_len):
    work_sheet.col(col).width = 256 * (len + 1)
  return work_sheet


if __name__ == '__main__':
  info = {
    'host'    :'192.168.137.11',
    'user'    :'root',
    'password':'root',
    'database':'test'
  }
  conn = mysql.connector.connect(**info)
  cursor = conn.cursor()
  sql = get_sql()
  cursor.execute(sql)
  # 获得excel的title
  title = get_title(cursor)
  # 获得需要的数据
  data = get_select_data(cursor)
  # 获得每一列的最大长度
  max_len = get_col_max_length(data, title)
  work_book = xlwt.Workbook(encoding='utf-8')
  # 创建一个excel模板
  work_sheet = work_book.add_sheet('查询数据')
  # 生成excel title
  work_sheet = create_excel_title(work_sheet, title, title_style)
  # 生成 excel 数据
  work_sheet = create_excel_body(work_sheet, data)
  # 设置每一列适当的长度
  work_sheet = set_work_sheet_col_len(work_sheet, max_len)
  # 保存 excel
  work_book.save('data_{time}.xls'.format(time=time.time()))
