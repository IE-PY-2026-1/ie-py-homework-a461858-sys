# 파일이름 : 2차과제
# 작 성 자 : 60251785 이수연

todo_list = []

print('투두리스트 입력')
task = input('투두리스트 입력: ')
category = input('목록(공부/취미/자기개발/기타): ')
priority = int(input('중요도(1-3): '))

todo_list.append([task, category, priority])
print(f'{task}가 저장되었습니다!')

Print(f'----항목보기메뉴----')
print('1. 전체 목록')
print('2. 중요도 별 목록')
print('3. 카테고리 별 목록')

choice = input('보고 싶은 목록 번호를 입력하세요.: ')

if choice == '1':
  print(f'[전체 목록 조회]')
  print(f'할 일: {todo_list=})
                
elif choice == '2':
  print('f'[중요도 별 목록보기]')
  select_priority = int(input('조회할 중요도(1-3)'))
  print(f'[중요도 {select_priority} 목록 결과];)
  if todo_list[0][2] == selsect_priority:
     print(f'{todo_list[0][0]} (카테고리: {todo_list[0][1]})')
  else:
     print(f'해당 중요도({select_priority}) 와 일치하는 할 일이 없습니다.')


elif choice == '3':
  search_cat = input('조회할 카테고리(공부/취미/자기개발/기타): ')
  print(f'[{select_cat} 카테고리 조회 결과]')
  if todo_list[0][1] == search_cat:
     print(f'{todo_list[0][0]} (중요도 : {todo_list[0][2]})')
  else:
     print(f'{search_cat} 카테고리에 해당하는 할 일이 없습니다.')
else:
  print('잘못된 입력입니다. 1~3번 메뉴를 선택해 주세용.')


  
