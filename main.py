# 파일이름 : 2차과제
# 작 성 자 : 60251785 이수연

todo_data = []

while True:
    print("행운의 투두리스트")
        print("1. 새로운 할 일 등록")
        print("2. 전체 목록 조회")
        print("3. 특정 날짜로 검색")
        print("4. 파일에 저장하기")
        print("5. 프로그램 종류")

    try:
        choice = int(input("메뉴를 선택하세요: ")
                     except Va
    
def add_task():
    global tasks, categories, priorities
    print("----[입력 메뉴] 할 일 등록----")

    for i in range(3):
        print(f'{i}번 째 투두리스트 입력')
        t_input = input('투두리스트 입력: ')
        
        if t_input == '그만':
            break

    while true:
        c_input = input('목록(공부/취미/자기개발/기타): ')
        if c_input in ['공부', '취미', '자기개발', '기타']:
            break
        else:
            print("지정된 카테고리(공부/취미/자기개발/기타) 중 하나만 입력해 주세요.")

    while true:
        p_input = int(input('중요도(1-3): '))
        if 1<=1 p_input <= 3:
            break
        else:
            print("중요도는 1, 2, 3 중 하나만 입력할 수 있습니다.")

    tasks.append(t_input)
    categories.append(c_input)
    priorities.append(p_input)
    print(f'{t_input}가 저장되었습니다!')

def view_task():
    if not task:
        print("등록된 할 일이 없습니다. 먼저 할 일을 입력해주세요.")
        return

    print(f'----항목보기메뉴----')
    print('1. 전체 목록')
    print('2. 중요도 별 목록')
    print('3. 카테고리 별 목록')

    choice = input('보고 싶은 목록 번호를 입력하세요.: ')

    if choice == '1':
        print(f'[전체 목록 조회]')
        for i in range(len(tasks)):
            print(f'할 일: {tasks[0]} / 카테고리: {categories} / 중요도: {priorities}')
                
    elif choice == '2':
      print(f'[중요도 별 목록보기]')
      select_p = int(input('조회할 중요도(1-3)'))
      print(f'[중요도 {select_p} 목록 결과]')
      if priorities[0] == select_p:
         if select_p == 3:
            print('매우 긴급!!!')
         elif select_p == 2:
            print('보통')
         else:
            print('여유~')
      else:
         print(f'해당 중요도({select_p}) 와 일치하는 할 일이 없습니다.')


    elif choice == '3':
        search_cat = input('조회할 카테고리(공부/취미/자기개발/기타): ')
        print(f'[{search_cat} 카테고리 조회 결과]')
  
        if categories[0] == search_cat:
            print(f'{tasks[0]} (중요도 : {priorities[0]})')
        else:
            print(f'{search_cat} 카테고리에 해당하는 할 일이 없습니다.')
    else:
      print('잘못된 입력입니다. 1~3번 메뉴를 선택해 주세용.')

def calculate_fortune_score(task_count):
    base_score = 10
    penalty = task_count * 2
    final_score = base_score - penalty

    if final_score < 0:
        final_score = 0
    return final_score


def show_fortune():
    print("----[갓생 분석 메뉴] 기분 & 행운의 색----")
    mood_color = input("오늘의 기분은 어떠신가요? (좋아/보통/최악): ")

    curent_tasks = len(tasks)
    fortune_score = calculate_fortune_score(current_tasks)

    print(f"[분석 결과]")
    print(f" - 현재 미완료 할 일 개수: {current_tasks}개")
    print(f" - 당신의 오늘 기분 지수: {fortune_score}점 / 점")

    if forture_score >= 8 and mood_color == '좋음':
        print("학점: A+ / 특별 칭호: [교수님의 사랑둥이] / 행운의 색: 골드")
    elif forture_score >= 4:
        print("학점: A0 / 특별 칭호: [교수님의 애교쟁이] / 행운의 색: 그린")
    else:
        print("학점: B / 특별 칭호: [성실한 대학생] / 행운의 색: 레드")

def main():
    while true:
        print("행운의 투두리스트")
        print("1. 새로운 할 일 등록 (Input)")
        print("2. 조건별 할 일 조회 (View)")
        print("3. 오늘의 기분 & 행운의 색 분석 (Analyze)")
        print("4. 프로그램 종류 (Exit)")

        menu_choice = input("원하는 메뉴 번호를 선택하세요: ")

        if menu_choice == '1':
            add_tasks()
        elif menu_choice == '2':
            view_tasks()
        elif menu_choice == '3':
            show_fortune()
        elif menu_choice == '4':
            print('프로그램을 종료합니다. 오늘도 파이팅!')
            break
        else:
            print("1번부터 4번 사이의 올바른 메뉴를 입력해 주세요.")



  
