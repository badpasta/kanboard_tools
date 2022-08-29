#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Jingyu Wang <badpasta@gmail.com>
#
# Environment:
# Python by version 3.9.


#from decimal import Decimal
from glob import glob
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, SmallInteger, Numeric, String, create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
#from configParser import DBCONFIG


Base = declarative_base()


# 每周五晚上12点统计周四-上周五的数据
class EfficiencyWeeklyStats(Base):
    __tablename__ = 'efficiency_weekly_stats'
    weekly_id = Column(SmallInteger, primary_key=True, autoincrement=True, unique=True, nullable=False)
    record_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    speent  = Column(Numeric(2), nullable=False)
    
# 每分钟更新??    
class EfficiencyWeeklyPlan(Base):
    __tablename__ = 'efficiency_weekly_plan'
    weekly_id = Column(SmallInteger, primary_key=True, autoincrement=True, unique=True, nullable=False)
    plan_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    speent_plan  = Column(Numeric(2), nullable=False)   

 
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
    speent  = Column(Numeric(2), nullable=False)   
    
  

# 每月1日统计 
class EfficiencyMonthlyStats(Base):
    __tablename__ = 'efficiency_monthly_stats' 
    monthly_id = Column(SmallInteger, primary_key=True, autoincrement=True, unique=True, nullable=False)
    record_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    speent = Column(Numeric(2), nullable=False)   
 
 
DB_URI = 'postgresql://{username}:{password}@{hostname}:{port}/{database}'
   

@contextmanager
def linkDB(config):

    try:
        global DB_URI
        
        engine = create_engine(DB_URI.format(**config))
        db_session = sessionmaker(bind=engine)

        #TODO: singleton
        _singleton = db_session
    
        yield _singleton
    except:
        _singleton.rollback()
        
        raise
    else:
        _singleton.commit()
    finally:
        _singleton.close()
   

def createTable():
    global DB_URI, DBCONFIG
   
    print(DBCONFIG) 
    engine = create_engine(DB_URI.format(**DBCONFIG))
    
    Base.metadata.create_all(engine)
    
   
def insertWeeklyData(_record):
    
    global DBCONFIG
    
    with linkDB(DBCONFIG) as db:
        new_record = EfficiencyWeeklyStats(**_record)
        db.add(new_record)
    
    
    
def selectWeeklyData(_record):
    
    global DBCONFIG
    
    with linkDB(DBCONFIG) as db:
        detail = db.query(EfficiencyWeeklyStats).filter(EfficiencyWeeklyStats.record_at > '2022-08-01')
        print(detail)


def main():
    from configParser import initConfig, DBCONFIG
    
    initConfig()
    print(DBCONFIG)

if __name__ == '__main__':
    main()
    #createTable()
    
    

