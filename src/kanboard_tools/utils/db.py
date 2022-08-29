#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Jingyu Wang <badpasta@gmail.com>
#
# Environment:
# Python by version 3.9.


from decimal import Decimal
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, SmallInteger, Decimal, String, create_engine
from sqlalchemy.orm import sessionmaker



Base = declarative_base()

BASEINFO ={
    'hostname': '127.0.0.1',
    'port': '5432',
    'username': 'kanboard',
    'password': 'kanboard@password',
    'database': 'kanboard'
}

DB_URI = 'postgresql://{username}:{password}@{hostname}:{port}/{database}'.format(**BASEINFO)


# 每周五晚上12点统计周四-上周五的数据
class EfficiencyWeeklyStats(Base):
    __tablename__ = 'efficiency_weekly_stats'
    weekly_id = Column(SmallInteger, primary_key=True, autoincrement=True, unique=True, nullable=False)
    record_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    speent  = Column(Decimal, nullable=False)
    
# 每分钟更新??    
class EfficiencyWeeklyPlan(Base):
    __tablename__ = 'efficiency_weekly_plan'
    weekly_id = Column(SmallInteger, primary_key=True, autoincrement=True, unique=True, nullable=False)
    plan_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    speent_plan  = Column(Decimal, nullable=False)   

 
# 每天早上10点统计前一天的日常运营工单数量和耗时    
class OperationDaliyStats(Base):
    __tablename__ = 'operation_daliy_stats'
    id = Column(SmallInteger, primary_key=True, autoincrement=True, unique=True, nullable=False)
    record_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    ripple_name = Column(String(30), nullable=False)
    # IT设备故障取故障现象
    # 网络日常工单取问题分类
    # OPS报警工单: 取报警原因字段
    problem_type = Column(String(30), nullable=False)
    speent  = Column(Decimal, nullable=False)   
    
  

# 每月1日统计 
class EfficiencyMonthlyStats(Base):
    __tablename__ = 'efficiency_monthly_stats' 
    monthly_id = Column(SmallInteger, primary_key=True, autoincrement=True, unique=True, nullable=False)
    record_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    speent = Column(Decimal, nullable=False)   
   

ENGINE = create_engine(DB_URI)

DBSESSION = sessionmaker(bind=ENGINE)

def createWeeklyTable():
    global ENGINE
    Base.metadata.create_all(ENGINE)
    
   
def insertWeeklyData(_record):
    global DBSESSION
    session = DBSESSION()

    new_record = EfficiencyWeeklyStats(**_record)
    
    session.add(new_record)
    
    session.commit()
    
    session.close()
    
    
def selectWeeklyData(_record):
    global DBSESSION
    session = DBSESSION()
    
    detail = session.query(EfficiencyWeeklyStats).filter(EfficiencyWeeklyStats.record_at > '2022-08-01')
    
    print(detail)
    
    session.close()


