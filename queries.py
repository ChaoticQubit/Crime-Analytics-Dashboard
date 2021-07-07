from query_res import get_results
from datetime import datetime

# ----------------------------------------FILTER PROCESSOR--------------------------------------
def filter_processor(all_filters):
    counts = incident_count(all_filters)
    query1 = query1_data(all_filters)
    query2 = query2_data(all_filters)
    query3 = query3_data(all_filters)
    query4 = query4_data(all_filters)
    query5 = query5_data(all_filters)
    query6 = query6_data(all_filters)
    
    return counts, query1, query2, query3, query4, query5, query6

# ----------------------------------------FILTER OPTIONS--------------------------------------
def filter_options():
    crime_type = 'SELECT DISTINCT TYPE FROM "BATRA.S".CRIME_TYPES'
    crime_type_filter = get_results(crime_type)

    crime_sub_type = 'SELECT DISTINCT DESCRIPTION FROM "BATRA.S".CRIME_TYPES'
    crime_sub_type_filter = get_results(crime_sub_type)

    districts = 'SELECT DISTINCT NAME FROM "BATRA.S".POLICE_STATIONS'
    dist_filter = get_results(districts)

    locations = 'SELECT DISTINCT POSITION_TYPE FROM "BATRA.S".CRIME_POSITION'
    crimeLoc_filt = get_results(locations)

    return crime_type_filter, crime_sub_type_filter, dist_filter, crimeLoc_filt

# ----------------------------------------FILTER QUERIES--------------------------------------
def filtered_query(query, sel_filters):
    if sel_filters['start_date'] != '0':
        date_strr = 'CASE_DATE > TO_TIMESTAMP(\'' + sel_filters['start_date'].strftime("%m/%d/%Y, %H:%M:%S") + '\', \'MM/DD/YYYY, HH24:MI:SS\') AND CASE_DATE < TO_TIMESTAMP(\'' + sel_filters['end_date'].strftime("%m/%d/%Y, %H:%M:%S") + '\', \'MM/DD/YYYY, HH24:MI:SS\')'
        query = query + date_strr + " AND "

    if sel_filters['arrest'] != '0':
        arrest_strr = 'ARREST = \'' + sel_filters['arrest'] + '\''
        query = query + arrest_strr + " AND "

    if sel_filters['domestic'] != '0':
        domestic_strr = 'DOMESTIC = \'' + sel_filters['domestic'] + '\''
        query = query + domestic_strr + " AND "

    if sel_filters['loc'] != '0':
        location_strr = 'POSITIONID IN (SELECT ID FROM "BATRA.S".CRIME_POSITION WHERE POSITION_TYPE = \'' + sel_filters['loc'].upper() + '\')'
        query = query + location_strr + " AND "

    if sel_filters['dist'] != '0':
        district_strr = 'POLICEID IN (SELECT ID FROM "BATRA.S".POLICE_STATIONS WHERE UPPER(NAME) = \'' + sel_filters['dist'].upper() + '\')'
        query = query + district_strr + " AND "

    if sel_filters['ctype'] != '0':
        ctype_strr = 'CRIMETYPEID IN (SELECT ID FROM "BATRA.S".CRIME_TYPES WHERE TYPE = \'' + sel_filters['ctype'].upper() + '\')'
        query = query + ctype_strr + " AND "

    if sel_filters['csub_type'] != '0':
        csub_type_strr = 'CRIMETYPEID IN (SELECT ID FROM "BATRA.S".CRIME_TYPES WHERE DESCRIPTION = \'' + sel_filters['csub_type'].upper() + '\')'
        query = query + csub_type_strr + " AND "
    
    return query

# ----------------------------------------QUERY FUNCTIONS--------------------------------------
def incident_count(sel_filters):
    base_strr = 'SELECT COUNT(*) FROM "BATRA.S".CRIME_INCIDENTS WHERE '
    query = base_strr
    query = filtered_query(query, sel_filters)
    if query == base_strr:
        query = query[0:-6]
    else:
        query = query[0:-4]
    return get_results(query)[0][0]

def query1_data(sel_filters):
    base_strr = 'SELECT COUNT(*), TRUNC(CASE_DATE) FROM "BATRA.S".CRIME_INCIDENTS WHERE '
    base_strr2 = 'GROUP BY TRUNC(CASE_DATE) ORDER BY TRUNC(CASE_DATE) '
    query = base_strr
    query = filtered_query(query, sel_filters)
    if query == base_strr:
        query = query[0:-6]
    else:
        query = query[0:-4]
    query = query + base_strr2
    print("Query 1: ", query, "\n\n")
    return get_results(query)


def query2_data(sel_filters):
    base_strr = 'SELECT TYPE, DESCRIPTION, cnt FROM "BATRA.S".CRIME_TYPES ct, (SELECT CRIMETYPEID, COUNT(*) as cnt FROM "BATRA.S".CRIME_INCIDENTS WHERE '
    base_strr2 = 'GROUP BY CRIMETYPEID ORDER BY COUNT(*) DESC FETCH FIRST 5 ROWS ONLY) crim WHERE ct.ID = crim.crimetypeid'
    query = base_strr
    query = filtered_query(query, sel_filters)
    if query == base_strr:
        query = query[0:-6]
    else:
        query = query[0:-4]
    query = query + base_strr2
    print("Query 2: ", query, "\n\n")
    return get_results(query)


def query3_data(sel_filters):
    base_strr = 'SELECT p.NAME, COUNT(*) FROM "BATRA.S".CRIME_INCIDENTS ci, "BATRA.S".POLICE_STATIONS p WHERE '
    base_strr2 = 'p.ID = ci.POLICEID GROUP BY p.NAME'
    query = base_strr
    query = filtered_query(query, sel_filters)
    query = query + base_strr2
    print("Query 3: ", query, "\n\n")
    return get_results(query)

def query4_data(sel_filters):
    base_strr = 'SELECT TO_CHAR(TRUNC(CASE_DATE), \'DAY\'), COUNT(*) FROM "BATRA.S".CRIME_INCIDENTS WHERE '
    base_strr2 = 'GROUP BY TO_CHAR(TRUNC(CASE_DATE), \'DAY\')'
    query = base_strr
    query = filtered_query(query, sel_filters)
    if query == base_strr:
        query = query[0:-6]
    else:
        query = query[0:-4]
    query = query + base_strr2
    print("Query 4: ", query, "\n\n")
    return get_results(query)

def query5_data(sel_filters):
    base_strr = 'SELECT TO_CHAR(CASE_DATE, \'HH24\'), COUNT(*) FROM "BATRA.S".CRIME_INCIDENTS WHERE '
    base_strr2 = 'GROUP BY TO_CHAR(CASE_DATE, \'HH24\') ORDER BY TO_CHAR(CASE_DATE, \'HH24\')'
    query = base_strr
    query = filtered_query(query, sel_filters)
    if query == base_strr:
        query = query[0:-6]
    else:
        query = query[0:-4]
    query = query + base_strr2
    print("Query 5: ", query, "\n\n")
    return get_results(query)

def query6_data(sel_filters):
    base_strr = """SELECT t1.d, t1.mth ,
                        CASE 
                            WHEN t2.cnt IS NULL THEN NULL 
                            ELSE (t1.cnt - t2.cnt) / (t2.cnt * 1.00) 
                        END AS MonthOverMonth 
                    FROM (
                        SELECT d, mth, cnt, 
                            CASE 
                                WHEN d = 2021 THEN \'b\' 
                                ELSE \'a\' 
                            END AS yearid 
                        FROM (
                            SELECT TO_CHAR(CASE_DATE, \'yyyy\') as d, TO_CHAR(CASE_DATE, \'mm\') as mth, COUNT(*) as cnt 
                            FROM "BATRA.S".CRIME_INCIDENTS WHERE """
    base_strr2 = """        GROUP BY TO_CHAR(CASE_DATE, \'yyyy\'), TO_CHAR(CASE_DATE, \'mm\') 
                            ORDER BY TO_CHAR(CASE_DATE, \'yyyy\'))) t1 
                    LEFT JOIN 
                        (SELECT d, mth, cnt, 
                            CASE 
                                WHEN d = 2021 THEN \'b\' 
                                ELSE \'a\' 
                            END AS yearid 
                        FROM (
                            SELECT TO_CHAR(CASE_DATE, \'yyyy\') as d, TO_CHAR(CASE_DATE, \'mm\') as mth, COUNT(*) as cnt 
                            FROM "BATRA.S".CRIME_INCIDENTS WHERE """
    base_strr3 = """        GROUP BY TO_CHAR(CASE_DATE, \'yyyy\'), TO_CHAR(CASE_DATE, \'mm\') 
                            ORDER BY TO_CHAR(CASE_DATE, \'yyyy\'))) t2 
                    ON t1.d = t2.d AND t1.mth - 1 = t2.mth AND t1.yearid = t2.yearid 
                    ORDER BY t1.d, t1.mth"""
    query = base_strr
    query2 = base_strr2
    query = filtered_query(query, sel_filters)
    query2 = filtered_query(query2, sel_filters)
    if query == base_strr:
        query = query[0:-6]
        query2 = query2[0:-6]
    else:
        query = query[0:-4]
        query2 = query2[0:-4]
    query = query + query2 + base_strr3
    print("Query 6: ", query, "\n\n")
    return get_results(query)
