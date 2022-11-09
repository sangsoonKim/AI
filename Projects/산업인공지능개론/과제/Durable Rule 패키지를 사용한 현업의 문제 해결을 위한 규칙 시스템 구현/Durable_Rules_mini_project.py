# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 13:59:03 2021

@author: KSS
"""

from durable.lang import *

with ruleset('ProblemSolution3'):
    @when_all(+m.cause)                               #cause를 갖는 것에 대해서 실행되는 규칙
    def showproblem(c):
        print('문제점->{0} {1}'.format(c.m.cause, c.m.effect))
        
        
    #sol 방법에 맞는 해결책 추가   
    @when_all((m.sol == 'conference'))
    def conference(c):
        print('해결책->사전 충분한 협의 필요')
        
    @when_all((m.sol == 'human'))
    def human(c):
        print('해결책->전문 인력 양성 및 선발')
    
    @when_all((m.sol == 'system'))
    def system(c):
        print('해결책->개발 환경 구축.')
    
    @when_all((m.sol == 'protocol'))
    def protocol(c):
        print('해결책->규약 및 규범 정리')

    
    
assert_fact('ProblemSolution3',{'cause':'일정에 대한','effect':'충분한 협의 미비','sol':'conference'}) 
assert_fact('ProblemSolution3',{'cause':'진행해야 할 프로젝트의','effect':' 충분한 정보 제공미비','sol':'conference'})    
assert_fact('ProblemSolution3',{'cause':'커뮤니티','effect':'담당자 없음','sol':'human'})   
assert_fact('ProblemSolution3',{'cause':'산업 전반에 대한 ','effect':'이해 부족','sol':'human'})   
assert_fact('ProblemSolution3',{'cause':'의사 소통 ','effect':'부족','sol':'conference'})   
assert_fact('ProblemSolution3',{'cause':'테스트 가능한 시뮬레이션 ','effect':'환경 미비','sol':'system'})   
assert_fact('ProblemSolution3',{'cause':'충분한 ','effect':'개발 기간 미비','sol':'conference'})   
assert_fact('ProblemSolution3',{'cause':'다양한 프로젝트 ','effect':'동시 진행','sol':'human'})   
assert_fact('ProblemSolution3',{'cause':'데이터 관리 ','effect':'기준 없음','sol':'protocol'})   
assert_fact('ProblemSolution3',{'cause':'프로그램간 ','effect':'기본 통신 규약 없음','sol':'protocol'})   
assert_fact('ProblemSolution3',{'cause':'프로젝트 ','effect':'접근 방식 문제','sol':'protocol'})   
assert_fact('ProblemSolution3',{'cause':'프로젝트 ','effect':'평가 프로세스 미비','sol':'protocol'})   
assert_fact('ProblemSolution3',{'cause':'적용 ','effect':'가능 인원 부족','sol':'human'})   
assert_fact('ProblemSolution3',{'cause':'경험','effect':' 부족','sol':'human'})   
assert_fact('ProblemSolution3',{'cause':'마무리 ','effect':'협의 부족','sol':'conference'})      


#assert_fact('ProblemSolution',{'cause':'일정에 대한','effect':'충분한 협의 미비','sol':'conference'}) 

#try:
#    assert_fact('ProblemSolution',{'cause':'일정에 대한','effect':'충분한 협의 미비','sol':'conference'}) 
#except BaseException as e:
#    print('Error : {0}'.format(e.message))   
    
#retract_fact('ProblemSolution',{'cause':'일정에 대한','effect':'충분한 협의 미비','sol':'conference'})
