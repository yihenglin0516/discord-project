

Monday = ['','','','','','','','','','','','','','','']
Tuesday = ['','','','','','','','','','','','','','','']
Wednesday = ['','','','','','','','','','','','','','','']
Thursday = ['','','','','','','','','','','','','','','']
Friday = ['','','','','','','','','','','','','','','']
Saturday = ['','','','','','','','','','','','','','','']
Sunday = ['','','','','','','','','','','','','','','']

def add_to_table(CourseteacherName , data_structure):  # CourseteacherName : Course + ' ' + Teacher

    course_info = data_structure.search(CourseteacherName)  # course_info是一個class , attribute : Name , Teacher , Time , link
    name , teacher , when = course_info.Name , course_info.Teacher , course_info.Time
    class_time = when.split(',')       # Ex : class_time = ['星期一','1','2','3']

    if class_time[0] == '星期一' :
        class_time = class_time[1:]
        for i in class_time :
            Monday[int(i)] = Monday[int(i)] + name + '('  + teacher + ')' + '\n'

    elif class_time[0] == '星期二':
        class_time = class_time[1:]
        for i in class_time :
            Tuesday[int(i)] = Tuesday[int(i)] + name + '('  + teacher + ')' + '\n'

    elif class_time[0] == '星期三':
        class_time = class_time[1:]
        for i in class_time :
            Wednesday[int(i)] = Wednesday[int(i)] + name + '('  + teacher + ')' + '\n'

    elif class_time[0] == '星期四':
        class_time = class_time[1:]
        for i in class_time :
            Thursday[int(i)] = Thursday[int(i)] + name + '('  + teacher + ')' + '\n'

    elif class_time[0] == '星期五':
        class_time = class_time[1:]
        for i in class_time :
            Friday[int(i)] = Friday[int(i)] + name + '('  + teacher + ')' + '\n'

    elif class_time[0] == '星期六':
        class_time = class_time[1:]
        for i in class_time :
            Saturday[int(i)] = Saturday[int(i)] + name + '('  + teacher + ')' + '\n'

    elif class_time[0] == '星期日':
        class_time = class_time[1:]
        for i in class_time :
            Sunday[int(i)] = Sunday[int(i)] + name + '('  + teacher + ')' + '\n'

    else :
        print('Something goes wrong')