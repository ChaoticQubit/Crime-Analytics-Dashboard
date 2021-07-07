import cx_Oracle
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_10")

def get_results(query):
    try:
        con = cx_Oracle.connect('--username--','--password--','oracle.cise.ufl.edu:1521/orcl',encoding='UTF-8')
        cursor = con.cursor()
        cursor.execute(query)
        res = cursor.fetchall()
        return res
    except ValueError as e:
        print('there is an error')
        print(e)

def get_total_cnt():
    city_cnt = 'SELECT COUNT(*) FROM "BATRA.S".CITY'
    city_cnt = get_results(city_cnt)[0][0]
    crime_inci_cnt = 'SELECT COUNT(*) FROM "BATRA.S".CRIME_INCIDENTS'
    crime_inci_cnt = get_results(crime_inci_cnt)[0][0]
    crime_pos_cnt = 'SELECT COUNT(*) FROM "BATRA.S".CRIME_POSITION'
    crime_pos_cnt = get_results(crime_pos_cnt)[0][0]
    crime_type_cnt = 'SELECT COUNT(*) FROM "BATRA.S".CRIME_TYPES'
    crime_type_cnt = get_results(crime_type_cnt)[0][0]
    loc_cnt = 'SELECT COUNT(*) FROM "BATRA.S".LOCATION'
    loc_cnt = get_results(loc_cnt)[0][0]
    pol_sta_cnt = 'SELECT COUNT(*) FROM "BATRA.S".POLICE_STATIONS'
    pol_sta_cnt = get_results(pol_sta_cnt)[0][0]
    return city_cnt + crime_inci_cnt + crime_pos_cnt + crime_type_cnt + loc_cnt + pol_sta_cnt
