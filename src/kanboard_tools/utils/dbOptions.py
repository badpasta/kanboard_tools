#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Jingyu Wang <badpasta@gmail.com>
#
# Environment:
# Python by version 3.9.


from re import S
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, SmallInteger, Numeric, String, create_engine, Identity
from sqlalchemy.orm import sessionmaker

import configParser


class noHaveFieldException(Exception):
    def __init__(self, **args):
        self.__message = f"not have \'{args}\' filed."
        

class recordNotFoundException(Exception):
    def __init__(self, **args):
        self.__message = f"not have record: \'{args}\'."
        

class recordConflictException(Exception):
    def __init__(self, **args):
        self.__message = f"record is conflict: \'{args}\'."



Base = declarative_base()


# 每周五晚上12点统计周四-上周五的数据
class EfficiencyWeeklyStats(Base):
    __tablename__ = 'efficiency_weekly_stats'
    __tableheader__ = ['id', 'record_at', 'member_id', 'speent']
    id = Column(SmallInteger, Identity(start=1, cycle=True), primary_key=True, autoincrement=True, unique=True, nullable=False)
    record_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    speent  = Column(Numeric(5, 1), nullable=False)
    
    def __init__(self, record_at, member_id, speent):
        self.record_at =  record_at
        self.member_id = member_id
        self.speent = speent
       
    @property    
    def value_dict(self):
        
        if self.id is None:
            self.id = 'None'
        
        _values = list(map(lambda h: self.__dict__[h], self.__tableheader__))
        
        return dict(zip(self.__tableheader__, _values))
   
    @property 
    def value_str(self):
        
        _list = list(map(lambda v: f"{v[0]}={v[1]},", self.value_dict.items()))
        
        return f"{self.__class__.__name__}(" + " ".join(_list) + ")"
    
    def __str__(self):
        
        return self.value_str
    
    def __repr__(self):
        
        return self.value_str
    
    
# 每分钟更新??    
class EfficiencyWeeklyPlan(Base):
    __tablename__ = 'efficiency_weekly_plan'
    __tableheader__ = ['id', 'plan_at', 'member_id', 'speent_plan']
    id = Column(SmallInteger, Identity(start=1, cycle=True), primary_key=True, autoincrement=True, unique=True, nullable=False)
    plan_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    speent_plan  = Column(Numeric(5, 1), nullable=False) 
    
    def __init__(self, plan_at, member_id, speent_plan):
        self.plan_at =  plan_at
        self.member_id = member_id
        self.speent_plan = speent_plan  
        
    @property    
    def value_dict(self):
        
        if self.id is None:
            self.id = 'None'
        
        _values = list(map(lambda h: self.__dict__[h], self.__tableheader__))
        
        return dict(zip(self.__tableheader__, _values))
   
    @property 
    def value_str(self):
        
        _list = list(map(lambda v: f"{v[0]}={v[1]},", self.value_dict.items()))
        
        return f"{self.__class__.__name__}(" + " ".join(_list) + ")"
    
    def __str__(self):
        
        return self.value_str
    
    def __repr__(self):
        
        return self.value_str

 
# 每天早上10点统计前一天的日常运营工单数量和耗时    
class OperationDaliyStats(Base):
    __tablename__ = 'operation_daliy_stats'
    __tableheader__ = ['id', 'record_at', 'member_id', 'ripple_type', 'problem_type', 'speent']
    id = Column(SmallInteger, Identity(start=1, cycle=True), primary_key=True, autoincrement=True, unique=True, nullable=False)
    record_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    ripple_type = Column(String(30), nullable=False)
    # IT设备故障取故障现象
    # 网络日常工单取问题分类
    # OPS报警工单: 取报警原因字段
    problem_type = Column(String(30), nullable=False)
    speent  = Column(Numeric(5, 1), nullable=False)   
    
    def __init__(self, record_at, member_id, ripple_type, problem_type, speent):
        self.record_at =  record_at
        self.member_id = member_id
        self.ripple_type = ripple_type  
        self.problem_type = problem_type
        self.speent = speent
        
    @property    
    def value_dict(self):
        
        if self.id is None:
            self.id = 'None'
        
        _values = list(map(lambda h: self.__dict__[h], self.__tableheader__))
        
        return dict(zip(self.__tableheader__, _values))
   
    @property 
    def value_str(self):
        
        _list = list(map(lambda v: f"{v[0]}={v[1]},", self.value_dict.items()))
        
        return f"{self.__class__.__name__}(" + " ".join(_list) + ")"
    
    def __str__(self):
        
        return self.value_str
    
    def __repr__(self):
        
        return self.value_str
    

# 每月1日统计 
class EfficiencyMonthlyStats(Base):
    __tablename__ = 'efficiency_monthly_stats' 
    __tableheader__ = ['id', 'record_at', 'member_id', 'speent']
    id = Column(SmallInteger, Identity(start=1, cycle=True),  primary_key=True, autoincrement=True, unique=True, nullable=False)
    record_at = Column(String(30), nullable=False) # e.g. 2022-08-14(周)
    member_id  = Column(SmallInteger, nullable=False)
    speent = Column(Numeric(5, 1), nullable=False)   
    
    def __init__(self, record_at, member_id, speent):
        self.record_at =  record_at
        self.member_id = member_id
        self.speent = speent  
    
    @property    
    def value_dict(self):
        
        if self.id is None:
            self.id = 'None'
        
        _values = list(map(lambda h: self.__dict__[h], self.__tableheader__))
        
        return dict(zip(self.__tableheader__, _values))
   
    @property 
    def value_str(self):
        
        _list = list(map(lambda v: f"{v[0]}={v[1]},", self.value_dict.items()))
        
        return f"{self.__class__.__name__}(" + " ".join(_list) + ")"
    
    def __str__(self):
        
        return self.value_str
    
    def __repr__(self):
        
        return self.value_str
    

 
DB_URI = 'postgresql://{username}:{password}@{hostname}:{port}/{database}'


def create_session():
    db_engine = create_engine(DB_URI.format(**configParser.DBCONFIG))
    #TODO: singleton
    db_session = sessionmaker(bind=db_engine)
    
    return db_session()
 

  
# 操作数据库表
class DBOperation(object):
    def __init__(self, cls):
        self._session = create_session()
        self.model = cls
        
    def _parse_response(func):
        def _parseing(self):
            resp = func(self)
            if not isinstance(resp, list):
                resp = [resp]

            #print(dir(resp[0]))
            return list(map(lambda r: r.value_dict, resp)) 
        
        return _parseing
    
    def _recordExist(func):
        def _check(self, record):
            select_result = self.select(record)
          
            #print(record)
            #print(select_result)
            if len(select_result) != 0:
                raise recordConflictException(**record)
               
            result = func(self, record) 
            
            return result
        
        return _check
    
    def _recordNotExist(func):
        def _check(self, record):
            select_result = self.select(record)
          
            if len(select_result) == 0:
                raise recordNotFoundException(**record)
               
            result = func(self, record) 
            
            return result
        
        return _check
   
    @_parse_response
    def select_all(self, filter=None):
        detail = list()
        
        with self._session as _session:
    
            detail = _session.query(self.model).all()

        return detail
    
    
    def select(self, record: dict):
        
        with self._session as _session:
    
            q = _session.query(self.model).filter_by(**record)
            detail = q.all()
            
        return detail

   
    @_parse_response 
    def before_at(self, _date):
        with self._session() as _session:
            detail = _session.query(self.model).filter(self.model.record_at > _date).all()
   
        return detail
   
    @_parse_response
    def after_at(self, _date):
        with self._session() as _session:
            detail = _session.query(self.model).filter(self.model.record_at < _date).all()
   
        return detail

    def update(self, record):
        pass
   
    @_recordExist
    def insert(self, record):
        with self._session as _session:
            new_record = self.model(**record)

            _session.add(new_record)

            _session.commit()
            _session.close()
            

    @_recordNotExist
    def delete(self, record):
        
        with self._session as _session:
            _session.query(self.model).filter_by(**record).delete()
            _session.commit()
            _session.close()
   
    
def createTable():
    global DB_URI
   
    #print(configParser.DBCONFIG) 
    #print(DB_URI.format(**configParser.DBCONFIG))
    engine = create_engine(DB_URI.format(**configParser.DBCONFIG))
    
    Base.metadata.create_all(engine)
    
    
def resetTable():
    global DB_URI
   
    #print(configParser.DBCONFIG) 
    #print(DB_URI.format(**configParser.DBCONFIG))
    engine = create_engine(DB_URI.format(**configParser.DBCONFIG))
    
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
  


def db_action(cls, record):
    _data = DBOperation(cls)

    _data.insert(record)
    print(_data.select_all())
    _data.delete(record)
    print(_data.select_all())

        
def test_efficiency_weekly_stats():
    
    cls = EfficiencyWeeklyStats
   
    record = {
        'record_at': '2022-08-30',
        'member_id': 1,
        'speent': 4
    } 
    
    db_action(cls, record)
    
    
def test_efficiency_weekly_plan():
    
    cls = EfficiencyWeeklyPlan
   
    record = {
        'plan_at': '2022-08-30',
        'member_id': 1,
        'speent_plan': 4
    } 
    
    db_action(cls, record)
    

def test_operation_daliy_stats():
    cls = OperationDaliyStats
   
    record = {
        'record_at': '2022-08-30',
        'member_id': 1,
        'ripple_type': 'IT设备故障',
        'problem_type': 'WiFi问题',
        'speent': 3.3
    } 
    
    db_action(cls, record)
    
    
def test_efficiency_monthly_stats():
    cls = EfficiencyMonthlyStats
   
    record = {
        'record_at': '2022-08-30',
        'member_id': 1,
        'speent': 15.5
    } 
    
    db_action(cls, record)
    

if __name__ == '__main__':
    
    from configParser import initConfig
     
    initConfig()
    #resetTable()
    
    test_efficiency_weekly_stats()
    test_efficiency_weekly_plan()
    test_operation_daliy_stats()
    test_efficiency_monthly_stats()

   
    
    

