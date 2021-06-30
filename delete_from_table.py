import add_table

def delete_from_table(CourseteacherName,data_structure):  # Ex : delete_from_table('資料結構 吳沛遠' , 'splay tree的名字')
    course_info = data_structure.search(CourseteacherName)  # course_info是一個class , attribute : Name , Teacher , Time , link
    name , teacher , when = course_info.Name , course_info.Teacher , course_info.Time
    class_time = when.split(',')       # Ex : class_time = ['星期一','1','2','3']

    if class_time[0] == '星期一' :
        class_time = class_time[1:]
        for i in class_time :
            chosen_course = add_table.Monday[int(i)].split('\n') # chosen_course : ['資料結構(吳沛遠)','電子學(鍾孝文)','微積分(張瑞恩)']
            course_name = name + '(' + teacher + ')' # Ex : 資料結構(吳沛遠)
            if course_name in chosen_course :  # 找到要刪的課程
                chosen_course.remove(course_name)
                add_table.Monday[int(i)] = '\n'.join(chosen_course)   # '電子學(鍾孝文)\n微積分(張瑞恩)\n'
            else :
                print('You did not choose this course')

    elif class_time[0] == '星期二':
        class_time = class_time[1:]
        for i in class_time :
            chosen_course = add_table.Tuesday[int(i)].split('\n') # chosen_course : ['資料結構(吳沛遠)','電子學(鍾孝文)','微積分(張瑞恩)']
            course_name = name + '(' + teacher + ')' # Ex : 資料結構(吳沛遠)
            if course_name in chosen_course :  # 找到要刪的課程
                chosen_course.remove(course_name)
                add_table.Tuesday[int(i)] = '\n'.join(chosen_course)   # '電子學(鍾孝文)\n微積分(張瑞恩)\n'
            else :
                print('You did not choose this course')

    elif class_time[0] == '星期三':
        class_time = class_time[1:]
        for i in class_time :
            chosen_course = add_table.Wednesday[int(i)].split('\n') # chosen_course : ['資料結構(吳沛遠)','電子學(鍾孝文)','微積分(張瑞恩)']
            course_name = name + '(' + teacher + ')' # Ex : 資料結構(吳沛遠)
            if course_name in chosen_course :  # 找到要刪的課程
                chosen_course.remove(course_name)
                add_table.Wednesday[int(i)] = '\n'.join(chosen_course)   # '電子學(鍾孝文)\n微積分(張瑞恩)\n'
            else :
                print('You did not choose this course')

    elif class_time[0] == '星期四':
        class_time = class_time[1:]
        for i in class_time :
            chosen_course = add_table.Thursday[int(i)].split('\n') # chosen_course : ['資料結構(吳沛遠)','電子學(鍾孝文)','微積分(張瑞恩)']
            course_name = name + '(' + teacher + ')' # Ex : 資料結構(吳沛遠)
            if course_name in chosen_course :  # 找到要刪的課程
                chosen_course.remove(course_name)
                add_table.Thursday[int(i)] = '\n'.join(chosen_course)   # '電子學(鍾孝文)\n微積分(張瑞恩)\n'
            else :
                print('You did not choose this course')

    elif class_time[0] == '星期五':
        class_time = class_time[1:]
        for i in class_time :
            chosen_course = add_table.Friday[int(i)].split('\n') # chosen_course : ['資料結構(吳沛遠)','電子學(鍾孝文)','微積分(張瑞恩)']
            course_name = name + '(' + teacher + ')' # Ex : 資料結構(吳沛遠)
            if course_name in chosen_course :  # 找到要刪的課程
                chosen_course.remove(course_name)
                add_table.Friday[int(i)] = '\n'.join(chosen_course)   # '電子學(鍾孝文)\n微積分(張瑞恩)\n'
            else :
                print('You did not choose this course')

    elif class_time[0] == '星期六':
        class_time = class_time[1:]
        for i in class_time :
            chosen_course = add_table.Saturday[int(i)].split('\n') # chosen_course : ['資料結構(吳沛遠)','電子學(鍾孝文)','微積分(張瑞恩)']
            course_name = name + '(' + teacher + ')' # Ex : 資料結構(吳沛遠)
            if course_name in chosen_course :  # 找到要刪的課程
                chosen_course.remove(course_name)
                add_table.Saturday[int(i)] = '\n'.join(chosen_course)   # '電子學(鍾孝文)\n微積分(張瑞恩)\n'
            else :
                print('You did not choose this course')

    elif class_time[0] == '星期日':
        class_time = class_time[1:]
        for i in class_time :
            chosen_course = add_table.Sunday[int(i)].split('\n') # chosen_course : ['資料結構(吳沛遠)','電子學(鍾孝文)','微積分(張瑞恩)']
            course_name = name + '(' + teacher + ')' # Ex : 資料結構(吳沛遠)
            if course_name in chosen_course :  # 找到要刪的課程
                chosen_course.remove(course_name)
                add_table.Sunday[int(i)] = '\n'.join(chosen_course)   # '電子學(鍾孝文)\n微積分(張瑞恩)\n'
            else :
                print('You did not choose this course')

    else :
        print('Something goes wrong')
