# Bread Bank For Dash
from datetime import date as d
import uuid as u
from random import randrange as r
class Account:
 __init__,stack_bread,__str__=lambda s,p,b:[
  setattr(s,*a)for a in{'client':p,'id':u.uuid4(),
   'bread_stack':{b.TYPE:b.amount},'creation_date':d.today()
  }.items()][0],lambda s,b:(lambda d,e:d.__setitem__(e,d[e]+b.amount)
 )(s.bread_stack,b.TYPE),lambda s:f"""Client:
{s.client}
Bread Stacks:
{s.bread_stack}
Hex ID: {s.id.hex}
Creation Date: {s.creation_date}"""
class Person:
 __init__,__str__=lambda s,f="",l="",b=d.today():[setattr(s,*a)for a in{
  'first_name':f,'surname':l,'birthday':b,'id':u.uuid4()
 }.items()][0],lambda s:f"""First Name: {s.first_name}
Last Name: {s.surname}
Birthday: {s.birthday}
Hex ID: {s.id.hex}"""
Employee=type('Employee',(Person,),{
 '__init__':lambda s,*a:(Person.__init__(s,*a[:-1]),
  [setattr(s,*b)for b in{'salary':a[-1],'email':None,
   'phone_number':None}.items()])[0]})
Manager,Bread=type('Manager',(Employee,),{'__init__':lambda s,f="",l="",b=d.today(
 ),a=0:Employee.__init__(s,f,l,b,a)or setattr(s,'access_code',b'808A')}),type(
  'Bread',(),{'__init__':lambda s,t:setattr(s,'TYPE',t)})
BreadStack=type('BreadStack',(Bread,),{'__init__':lambda s,t,a=0:(
 Bread.__init__(s,t),setattr(s,'amount',a))[0]})
BreadVault=type('BreadVault',(),{
 '__init__':lambda s:setattr(s,'balance',[]),
 '__iadd__':lambda s,n:setattr(s,'balance',s.balance+n)or s,
 '__isub__':lambda s,n:setattr(s,'balance',s.balance-n)or s})
BreadBank=type('BreadBank',(),{
 '__init__':lambda s,m=Manager(),e=[],a=[],v=BreadVault():[
  setattr(s,*a)for a in{'manager':m,'employees':e,
   'accounts':a,'vault':v}.items()][0],'deposit':lambda s,a,b=BreadStack(
    '',0):(lambda e:e[e.index(a.id)].stack_bread(b))(s.accounts)})
if __name__=="__main__":
 b=BreadBank(Manager(),[Employee("George",str(i
  ),d.today(),50000) for i in range(10)],[Account(Person(),BreadStack(
   "Brioche",r(25,450)))for _ in range(10)],BreadVault())
 print(b.employees,b.accounts[0],sep='\n')