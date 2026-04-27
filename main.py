# 파일이름 : 2차과제
# 작 성 자 : 60251785 이수연

tasks =[]
categories =[]
priorities = []

for i in range(3):
    print(f'{i}번 째 투두리스트 입력')
t_input = input('투두리스트 입력: ')
if t_input == '그만'
   break
c_input = input('목록(공부/취미/자기개발/기타): ')
p_input = int(input('중요도(1-3): '))

tasks.append(t_input)
categories.append(c_input)
priorities.append(p_input)
print(f'{t_input}가 저장되었습니다!')

Print(f'----항목보기메뉴----')
print('1. 전체 목록')
print('2. 중요도 별 목록')
print('3. 카테고리 별 목록')

choice = input('보고 싶은 목록 번호를 입력하세요.: ')

if choice == '1':
  print(f'[전체 목록 조회]')
  print(f'할 일: {tasks[0]} / 카테고리: {categories} / 중요도: {priorities})
                
elif choice == '2':
  print('f'[중요도 별 목록보기]')
  select_p = int(input('조회할 중요도(1-3)'))
  print(f'[중요도 {select_priority} 목록 결과];)
  if priorities[0] == select_p:
     if select == 3:
        print('매우 긴급!!!')
     elif select == 2:
        print('보통')
     else:
        print('여유~')
   else:
     print(f'해당 중요도({select_priority}) 와 일치하는 할 일이 없습니다.')


elif choice == '3':
  search_cat = input('조회할 카테고리(공부/취미/자기개발/기타): ')
  print(f'[{select_cat} 카테고리 조회 결과]')
  
  if categories[0] == search_cat:
     print(f'{tasks[0]} (중요도 : {priorities[0]})')
   else:
     print(f'{search_cat} 카테고리에 해당하는 할 일이 없습니다.')
else:
  print('잘못된 입력입니다. 1~3번 메뉴를 선택해 주세용.')


  
