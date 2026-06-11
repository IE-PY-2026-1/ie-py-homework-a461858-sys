# 파일이름 : 2차과제
# 작 성 자 : 60251785 이수연

todo_list = []

    
def add_task():
    global todo_list
    print("----[입력 메뉴] 할 일 등록----")
                     
    try:
        user_name = input("작성자 이름을 입력하세요: ")
        task_date = input("날짜 입력 (예: 2026-06-12): ")
        t_input = input("투두리스트 입력: ")

        while True:
            c_input = input("목록(공부/취미/자기개발/기타): ")
            if c_input in ['공부', '취미', '자기개발', '기타']:
                break
            else:
                print("지정된 카테고리 중 하나만 입력해주세요.")

        while True:
            p_input = int(input("중요도(1-3): "))
            if 1 <= p_input <= 3:
                break
            else:
                print("중요도는 1, 2, 3 중 하나만 입력해주세요")

        todo_list.append([user_name, task_date, t_input, c_input, p_input])
        print(f"{t_input}가 성공적으로 저장되었습니다.")

    except ValueError:
        print("입력 에러: 중요도에는 숫자만 입력할 수 있습니다. 다시 시도해주세요.")


                          

def view_task():
    if not todo_list:
        print("등록된 할 일이 없습니다. 먼저 할 일을 입력해주세요.")
        return

    print('----항목보기메뉴----')
    print('1. 전체 목록')
    print('2. 중요도 별 목록')
    print('3. 카테고리 별 목록')
    print('4. 특정 날짜 별 목록')

    choice = input('보고 싶은 목록 번호를 입력하세요.: ')

    if choice == '1':
        print(f'[전체 목록 조회]')
        print('-'*35)
        print('이름 | 날짜 | 할 일 | 카테고리 | 중요도')

        for row in todo_list:
            print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}')
            print('-'*35)
                
    elif choice == '2':
        print(f'[중요도 별 목록보기]')

        try:
            select_p = int(input('조회할 중요도(1-3): '))
            print(f'[중요도 {select_p} 목록 결과]')
        
            match_count = 0
            for row in todo_list:
                if row[4] == select_p:
                    if select_p == 3:
                        status = '매우 긴급!!'
                    elif select_p == 2:
                        status = '보통'
                    else:
                        status = '여유~'

                    print(f'[{row[0]}님] 할 일: {row[2]}, 날짜: {row[1]} -> {status}')
                    match_count += 1

        if match_count == 0:
            print('해당 중요도와 일치하는 할 일이 없습니다.')
    except ValueError:
        print('숫자로만 입력해야 합니다.')


    elif choice == '3':
        search_cat = input('조회할 카테고리(공부/취미/자기개발/기타): ')
        print(f'[{search_cat} 카테고리 조회 결과]')

        match_count = 0
        for row in todo_list:
            if row[3] == search_cat:
                print(f'[{row[0]}님] {row[2]} [날짜: {row[1]}] (중요도: {row[4]})')
                match_count += 1

        if match_count == 0:
            print(f'{search_cat} 카테고리에 해당하는 할 일이 없습니다.')

    elif choice == '4':
        search_date = input('조회할 날짜를 입력하세요 (예: 2026-06-12): ')
        print(f'[{search_date} 날짜 조회 결과]')

        match_count = 0
        for row in todo_list:
            if row[1] == search_date:
                print(f'[{row[0]}님] {row[2]} [날짜: {row[1]}] (중요도: {row[4]})')
                match_count += 1

        if match_count == 0:
            print('해당 날짜에 등록된 할 일이 없습니다.')
    else:
        print('잘못된 입력입니다. 1~4번 메뉴를 선택해 주세요.')



def save_to_file():
    try:
        with open("todolist.txt", "w", encoding="utf-8") as f:
            for row in todo_list:
                line = str(row[0]) + "," + str(row[1]) + "," + str(row[2]) + "," + str(row[3]) + "," + str(row[4]) + "\n"
                f.write(line)
            print("파일이 안전하게 저장되었습니다.")
            
    except ValueError:
        print("파일 저장 중 데이터 오류가 발생했습니다.")




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

    current_tasks = len(todo_list)
    fortune_score = calculate_fortune_score(current_tasks)

    print(f"[분석 결과]")
    print(f" - 현재 미완료 할 일 개수: {current_tasks}개")
    print(f" - 당신의 오늘 기분 지수: {fortune_score}점 / 10점")

    if fortune_score >= 8 and mood_color == '좋아':
        print("학점: A+ / 특별 칭호: [교수님의 사랑둥이] / 행운의 색: 골드")
    elif fortune_score >= 4:
        print("학점: A0 / 특별 칭호: [교수님의 애교쟁이] / 행운의 색: 그린")
    else:
        print("학점: B / 특별 칭호: [성실한 대학생] / 행운의 색: 레드")


def main():
    while True:
        print("행운의 투두리스트")
        print("1. 새로운 할 일 등록")
        print("2. 전체 목록 조회")
        print("3. 오늘의 기분&행운의 색 조회")
        print("4. 파일에 저장하기")
        print("5. 프로그램 종료")
        
        menu_choice = input("원하는 메뉴 번호를 선택하세요: ")

        if menu_choice == '1':
            add_task()
        elif menu_choice == '2':
            view_task()
        elif menu_choice == '3':
            show_fortune()
        elif menu_choice == '4':
            save_to_file()
        elif menu_choice == '5':
            print('프로그램을 종료합니다. 오늘도 파이팅!')
            break
        else:
            print("1번부터 5번 사이의 올바른 메뉴를 입력해 주세요.")


if __name__ == "__main__":
    main()

  
