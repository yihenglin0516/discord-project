import add_table
from prettytable import PrettyTable

def show_table():
    table = PrettyTable()

    table.add_column('時間',['0 7:10~8:20','1 8:10~9:00','2 9:10~10:00','3 10:20~11:10','4 11:20~12:10','5 12:20~13:10','6 13:20~14:10',
    '7 14:20~15:10','8 15:30~16:20','9 16:30~17:20','10 17:30~18:20','A 18:25~19:15','B 19:20~20:10','C 20:15~21:05','D 21:10~22:00'])

    table.add_column('星期一',add_table.Monday)
    table.add_column('星期二',add_table.Tuesday)
    table.add_column('星期三',add_table.Wednesday)
    table.add_column('星期四',add_table.Thursday)
    table.add_column('星期五',add_table.Friday)
    table.add_column('星期六',add_table.Saturday)
    table.add_column('星期日',add_table.Sunday)

    return table
