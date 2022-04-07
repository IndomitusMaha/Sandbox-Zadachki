import pymysql
import yaml
import xlsxwriter
# -*- coding: utf-8 -*-


def cybernet_tm():
    with open('connections.yml', "r") as cnt:
        data = yaml.safe_load(cnt)
    host = data['cybernet_tm']['host']
    user = data['cybernet_tm']['user']
    passwd = data['cybernet_tm']['pass']
    database = data['cybernet_tm']['database']
    cybernet_tm.db = pymysql.connect(host=host, user=user, password=passwd, database=database, read_timeout=10, write_timeout=10)
    cybernet_tm.cur = cybernet_tm.db.cursor(pymysql.cursors.DictCursor)


def cybernet_calls():

    with open('connections.yml', "r") as cnt:
        data = yaml.safe_load(cnt)
    host = data['cybernet_calls']['host']
    user = data['cybernet_calls']['user']
    passwd = data['cybernet_calls']['pass']
    database = data['cybernet_calls']['database']
    cybernet_calls.db = pymysql.connect(host=host, user=user, password=passwd, database=database, read_timeout=10, write_timeout=10)
    cybernet_calls.cur = cybernet_calls.db.cursor(pymysql.cursors.DictCursor)


def execute_tm_fetchall(sql):
    i = 0
    while i <= 120:
        try:
            cybernet_tm()
            cybernet_tm.cur.execute(sql)
            result_list = cybernet_tm.cur.fetchall()
            close_tm()
        except:
            print('ERROR OCCURED')
            print(sys.exc_info())
            i += 1
            print(' Iteration inside of exept #', i)
            close_tm()
            time.sleep(1)
            continue
        else:
            return result_list


def execute_tm_fetchone(sql):
    i = 0
    while i <= 120:
        try:
            cybernet_tm()
            cybernet_tm.cur.execute(sql)
            item = cybernet_tm.cur.fetchone()
            close_tm()
        except:
            print('ERROR OCCURED')
            print(sys.exc_info())
            i += 1
            print(' Iteration inside of exept #', i)
            time.sleep(1)
            continue
        else:
            return item


def execute_calls_fetchall(sql):
    i = 0
    while i <= 120:
        try:
            cybernet_calls()
            cybernet_calls.cur.execute(sql)
            result_list = cybernet_calls.cur.fetchall()
            close_calls()
        except:
            print('ERROR OCCURED')
            print(sys.exc_info())
            i += 1
            print(' Iteration inside of exept #', i)
            time.sleep(1)
            continue
        else:
            return result_list


def execute_calls_fetchone(sql):
    i = 0
    while i <= 120:
        try:
            cybernet_calls()
            cybernet_calls.cur.execute(sql)
            item = cybernet_calls.cur.fetchone()
            close_calls()
        except:
            print('ERROR OCCURED')
            print(sys.exc_info())
            i += 1
            print(' Iteration inside of exept #', i)
            time.sleep(1)
            continue
        else:
            return item


def close_tm():
    if cybernet_tm.db.open:
        cybernet_tm.cur.close()
        cybernet_tm.db.close()


def close_calls():
    if cybernet_calls.db.open:
        cybernet_calls.cur.close()
        cybernet_calls.db.close()

print('---------------------------------------------------------------------------------------------------------------')

sql = " SELECT date(start_datetime) as Date, hour(start_datetime) as Hour, count(status) AS Robot_calls, count(case when status = 'completed' then 1 end) AS Robot_calls_succes,\n" \
                      "     count(case when promise = '!oper(raschet)' then 1 end) AS Operator_redirect \n" \
                      "  FROM cybernet_calls.xm9wl_calls_details\n" \
                      " Where ccuser_id = 355 and hour(start_datetime) > 8 and hour(start_datetime) < 18 and date(start_datetime) > '2022-03-14'\n" \
                      " GROUP BY Date, Hour \n " \
                      " ORDER BY Date, Hour"

stat_dict = execute_calls_fetchall(sql)

if stat_dict is None:
    stat_dict = {'Robot_calls':0, 'Robot_calls_succes':0, 'Operator_redirect':0 }

for i in stat_dict:
    i['Date+Hour'] = i['Date'].strftime("%Y-%m-%d")+" "+str(i['Hour'])
    del i['Hour']
    if i['Robot_calls_succes'] != 0:
        i['Call efficiency'] = round(i['Operator_redirect']/i['Robot_calls_succes']*100, 2)
    elif i['Robot_calls_succes'] == 0:
        i['Call efficiency'] = 0

    if i['Operator_redirect'] != 0:
        i['Robot efficiency'] = round(i['Robot_calls_succes']/i['Operator_redirect']*100, 2)
    elif i['Operator_redirect'] == 0:
        i['Robot efficiency'] = 0


sql = "Select t.Date, t.Hour, count(t.internal_number) as operators_by_hour \n" \
      " FROM (Select DISTINCT date(timestamp) as Date, hour(timestamp) as Hour, internal_number  \n" \
      " From status_call \n" \
      " Where status_call <> 'Unavailable' \n" \
      " ORDER BY Date, Hour) as t \n" \
      " Group BY t.Date, t.Hour"


last_minute_status = execute_tm_fetchall(sql)

for i in last_minute_status:
    i['Date+Hour'] = i['Date'].strftime("%Y-%m-%d") + " " + str(i['Hour'])
    del i['Date']
    del i['Hour']


for i in stat_dict:
    Equal_date = False
    for j in last_minute_status:
        if i['Date+Hour'] == j['Date+Hour']:
            Equal_date = True
            i['operators_by_hour'] = j['operators_by_hour']
    if Equal_date == False:
        i['operators_by_hour'] = 0


sql = "Select t.Date, count(t.internal_number) as operators_by_day \n" \
      "FROM (Select Distinct date(timestamp) as Date, internal_number from status_call \n" \
      "Where status_call <> 'Unavailable' \n" \
      "Order by Date) as t\n" \
      "Group By t.Date"


hole_day_status = execute_tm_fetchall(sql)

for i in stat_dict:
    Equal_date = False
    for j in hole_day_status:
        if i['Date'] == j['Date']:
            Equal_date = True
            i['operators_by_day'] = j['operators_by_day']
    if Equal_date == False:
        i['operators_by_day'] = 0


workbook = xlsxwriter.Workbook('Hourly report.xlsx')
worksheet = workbook.add_worksheet("Report sheet")

row = 0
col = 0

worksheet.write(row, 0, 'Date and hour')
worksheet.write(row, 1, "Calls")
worksheet.write(row, 2, "Succesfull calls")
worksheet.write(row, 3, "Redirects to operators")
worksheet.write(row, 4, "Percentafe of succ. calls")
worksheet.write(row, 5, "Robot's efficiency")
worksheet.write(row, 6, "Operators by hour")
worksheet.write(row, 7, "Operators by day")

for i in stat_dict:
    row += 1
    col = 0
    worksheet.write(row, col, i['Date+Hour'])
    worksheet.write(row, col+1, i['Robot_calls'])
    worksheet.write(row, col+2, i['Robot_calls_succes'])
    worksheet.write(row, col+3, i['Operator_redirect'])
    worksheet.write(row, col+4, i['Call efficiency'])
    worksheet.write(row, col+5, i['Robot efficiency'])
    worksheet.write(row, col+6, i['operators_by_hour'])
    worksheet.write(row, col+7, i['operators_by_day'])

workbook.close()




