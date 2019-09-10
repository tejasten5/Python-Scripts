from datetime import datetime as dt

new_li=[]
li1=[]
li2=[]
li3=[]
li4=[]

li=[
    {'first_name': 'November', 'ind': 'Tele,edu', 'email': 'raj@raj.com', 'contact': '7894561230','linkdin': 'http://ldnk.raj.com', 'job': 'ceo,hr', 'id': 1, 'time': '13:33:48', 'date': 'November 30 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'August', 'ind': 'edu', 'email': 'hasrh@gmail.com', 'contact': '3216549870', 'linkdin': 'http://manju.linkdin.com', 'job': 'hr', 'id': 2, 'time': '13:34:46', 'date': 'August 17 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'December', 'ind': 'edu', 'email': 'tejas@tejas.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 3, 'time': '08:50:43', 'date': 'December 25 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'August', 'ind': 'edu', 'email': 'chirag@chirag.com', 'contact': '6546578786','linkdin': 'http://link.in', 'job': 'hr', 'id': 4, 'time': '08:50:43', 'date': 'August 29 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'October', 'ind': 'edu', 'email': 'v@v.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 5, 'time': '08:50:43', 'date': 'October 19 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'September', 'ind': 'edu', 'email': 'vi@vi.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 6, 'time': '08:50:43', 'date': 'September 28 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'May', 'ind': 'edu', 'email': 'vir@vir.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 7, 'time': '08:50:43', 'date': 'May 15 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'June', 'ind': 'edu', 'email': 'vira@vira.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 8, 'time': '08:50:43', 'date': 'June 27 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'April', 'ind': 'edu', 'email': 'viraj@viraj.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 9, 'time': '08:50:43', 'date': 'April 8 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'March', 'ind': 'edu', 'email': 'vendor@vendor.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 10, 'time': '08:50:43', 'date': 'March 6 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'February', 'ind': 'edu', 'email': 'client@client.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 11, 'time': '08:50:43', 'date': 'February 3 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'January', 'ind': 'edu', 'email': 'cust@cust.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 12, 'time': '08:50:43', 'date': 'January 20 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'July', 'ind': 'edu', 'email': 'cust@cust.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 13, 'time': '08:50:43', 'date': 'July 20 2019', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},
    {'first_name': 'December', 'ind': 'edu', 'email': 'tejas@tejas.com', 'contact': '6546578786', 'linkdin': 'http://link.in', 'job': 'hr', 'id': 14, 'time': '08:50:43', 'date': 'December 25 2029', 'status': 0, 'batch': 0, 'TC_lead_status': 'valid lead'},    
]

for i in li:
    i['date']=dt.strptime(i['date'],'%B %d %Y')
    month=i['date'].month
    i['month']=month

li.sort(key=lambda item:item['date'])
new_li=li

currentMonth = dt.now().month
x=int(input('Enter number'))

for i in new_li:
    li1.append(i['month'])
    for j in li1:
        if j not in li2:
            li2.append(j)
            
diff=currentMonth-x
if currentMonth in li2:    
    if x<currentMonth:
        li3=li2[diff:currentMonth] 
        print(li3)                           
    if x>currentMonth:
        li3=li2[currentMonth-1:x]

for i in li3:
    for j in new_li:
        if(str(i) in str(j['month'])):
            li4.append(j)


for i in li4:
    print(i)
