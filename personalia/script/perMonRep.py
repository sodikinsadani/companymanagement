from openpyxl import Workbook,load_workbook
from ..models import Employee
from datetime import datetime as dt
from openpyxl.chart import BarChart, Series, Reference
from openpyxl.styles import Alignment,Font,colors
from django.contrib.auth.models import User

def GetEmpProg():
    from django.db import connection as con
    with con.cursor() as cursor:
        cursor.execute('''
            select l.manager,l.name,e.status_active,e.grade,
            p.gender,count(e.person_id) as total
            from
            personalia_employee e
            inner join personalia_leader l on l.leader_id = e.leader_id
            inner join personalia_person p on p.id = e.person_id
            group by l.manager,l.name,e.status_active,e.grade,p.gender
            order by l.manager,l.name,e.status_active,e.grade,
            p.gender
        ''')
        result_list = []
        for row in cursor.fetchall():
            result_list.append(row)
    return result_list

def ConstructReport(response,params):
    report_name = params['reports'].report_name
    file = open('personalia/template_xlsx/tmpPerMon.xlsx', 'rb')
    wb = load_workbook(filename = file)

    result_list = GetEmpProg()
    '''rows = 1
    rows += 1;ws.cell(row=rows,column=1,value=report_name.upper())
    date_now = dt.today()
    date_now = date_now.strftime("%d %B %Y")
    rows += 1;ws.cell(row=rows,column=1,value=date_now)
    rows += 2'''

    sDict = {
    'ahm':('ahmad',),'ksm':('kusmawan',),'mgd':('migud',),
    'sdk':('sodikin',),'sdr':('sodirun',)
    }
    manager = ''
    for r in result_list:
        ft = Font(color=colors.RED)
        ac = Alignment(horizontal='center')

        if manager != r[0] :
            manager = r[0]
            ws = wb[sDict[manager][0]]
            rows = 7
            no = 0

        no += 1
        col = 0
        rows += 1
        col += 1;ws.cell(row=rows,column=col,value=no).alignment = ac
        col += 1;ws.cell(row=rows,column=col,value=r[1].upper())
        if r[2] == 'pa':
            valin = (0,0,0,0,0,0)
        col += 1;ws.cell(row=rows,column=col,value=valin[0] or 0)
        col += 1;ws.cell(row=rows,column=col,value=valin[0] or 0)
        col += 1;ws.cell(row=rows,column=col,value=valin[0] or 0)
        col += 1;ws.cell(row=rows,column=col,value=valin[0] or 0)
        col += 1;ws.cell(row=rows,column=col,value=valin[0] or 0)
        col += 1;ws.cell(row=rows,column=col,value=valin[0] or 0)
        '''col += 1;ws.cell(row=rows,column=col,value=emp.person.school.title())
        col += 1;ws.cell(row=rows,column=col,value=emp.person.get_graduate_display()).alignment = ac
        col += 1;ws.cell(row=rows,column=col,value=emp.person.mobilephone)
        col += 1;ws.cell(row=rows,column=col,value=emp.person.bbm.upper())
        col += 1;ws.cell(row=rows,column=col,value=emp.person.email.lower())
        col += 1;ws.cell(row=rows,column=col,value=emp.get_grade_display()).alignment = ac
        col += 1;ws.cell(row=rows,column=col,value=emp.date_register).number_format = 'dd mmm yyy'
        col += 1;ws.cell(row=rows,column=col,value=emp.get_status_active_display()).alignment = ac
        col += 1;ws.cell(row=rows,column=col,value=emp.leader.leader_id).alignment = ac
        col += 1;ws.cell(row=rows,column=col,value=emp.description)'''

    wb.save(response)
    return response
