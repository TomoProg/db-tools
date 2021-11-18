import mysql.connector
import random

def generate_last_name():
    last_names = [
            "佐藤",
            "鈴木",
            "高橋",
            "田中",
            "伊藤",
            "渡辺",
            "山本",
            "中村",
            "小林",
            "加藤",
            "吉田",
            "山田",
            "佐々木",
            "山口",
            "松本",
            "井上",
            "木村",
            "林",
            "斎藤",
            "清水",
            "山崎",
            "森",
            "池田",
            "橋本",
            "阿部",
            "石川",
            "山下",
            "中島",
            "石井",
            "小川",
            "前田",
            "岡田",
            "長谷川",
            "藤田",
            "後藤",
            "近藤",
            "村上",
            "遠藤",
            "青木",
            "坂本",
            "斉藤",
            "福田",
            "太田",
            "西村",
            "藤井",
            "金子",
            "岡本",
            "藤原",
            "三浦",
            "中野",
            ]
    return last_names[random.randint(0, len(last_names) - 1)]

def generate_first_name():
    first_names = [
        "蓮",
        "陽翔",
        "蒼",
        "樹",
        "湊",
        "悠真",
        "大翔",
        "律",
        "朝陽",
        "結翔",
        "湊斗",
        "颯真",
        "碧",
        "陽太",
        "大和",
        "伊織",
        "陽大",
        "暖",
        "颯",
        "新",
        "陽向",
        "悠人",
        "蒼大",
        "悠",
        "朔",
        "凪",
        "陽",
        "陸",
        "陽斗",
        "奏太",
        "悠斗",
        "旭",
        "奏汰",
        "蒼真",
        "颯太",
        "岳",
        "晴",
        "葵",
        "結斗",
        "蒼空",
        "琉生",
        "陸斗",
        "颯人",
        "碧人",
        "瑛太",
        "海翔",
        "怜",
        "絢斗",
        "大智",
        "瑛斗",
        "律希",
        "櫂",
        "悠翔",
        "大晴",
        "悠生",
        "仁",
        "翔",
        "奏多",
        "一颯",
        "蒼生",
        "晴翔",
        "遥斗",
        "海斗",
        "楓",
        "蒼太",
        "碧斗",
        "慧",
        "壮真",
        "大雅",
        "颯斗",
        "健人",
        "颯汰",
        "蒼士",
        "理人",
        "煌",
        "湊翔",
        "涼真",
        "結人",
        "悠希",
        "湊太",
        "歩",
        "健",
        "凌久",
        "湊大",
        "慶",
        "蒼人",
        "光",
        "奏翔",
        "翼",
        "善",
        "太陽",
        "奏",
        "優",
        "奏斗",
        "柊",
        "遼",
        "空",
        "迅",
        "陸人",
        "光希",
        "瑛大",
    ]
    return first_names[random.randint(0, len(first_names) - 1)]

def generate_prefecture():
    return random.randint(1, 47)

cnx = mysql.connector.connect(
    user='dbuser',
    password='',
    host='192.168.10.108',
    database='sample')
cursor = cnx.cursor()

try:
    sql = ("CREATE TABLE IF NOT EXISTS many_records (id bigint, last_name varchar(20), first_name varchar(20), prefecture int, primary key(id))")
    cursor.execute(sql)
    sql = ("TRUNCATE TABLE many_records")
    cursor.execute(sql)
    
    sql = ("INSERT INTO many_records (id, last_name, first_name, prefecture) VALUES (%s, %s, %s, %s)")

    record_num = 5000000
    record_list = []
    for i in range(1, record_num + 1):
        record = (i, generate_last_name(), generate_first_name(), generate_prefecture())
        record_list.append(record)
        if len(record_list) == 100000:
            cursor.executemany(sql, record_list)
            print("進捗率：{}/{}件".format(i, record_num))
            record_list = []

    if len(record_list) > 0:
        cursor.execute(sql, record_list)

    cnx.commit()
    print("完了!!!")
except Exception as ex:
    print(ex)
finally:
    cursor.close()
    cnx.close()
