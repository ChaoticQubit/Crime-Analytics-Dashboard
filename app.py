from flask import Flask, render_template, request, redirect, jsonify
from query_res import get_results, get_total_cnt
import queries as q
from datetime import datetime
import json

filter_dict = {'ctype' : '0', 
                'csub_type' : '0', 
                'dist' : '0', 
                'loc' : '0', 
                'start_date' : '0', 
                'end_date' : '0', 
                'gran' : '0', 
                'arrest' : '0', 
                'domestic' : '0'
}

# ---------------------------------------------ROUTER QUERY CALL------------------------------------------
def route_query_calls():
    counts, q1, q2, q3, q4, q5, q6 = q.filter_processor(filter_dict)
    json_writer(q1)
    json_writer2(q2)
    json_writer3(q3)
    json_writer4(q4)
    json_writer5(q5)
    json_writer6(q6)
    return jsonify({'total_inci' : counts})
# END

# ---------------------------------------------READER FUNCTION------------------------------------------
def json_reader(file_n):
    with open(file_n) as json_file:
        data = json.load(json_file)
    return data
# END

# ---------------------------------------------WRITER FUNCTIONS------------------------------------------
def json_writer(qu_out):
    quers = {"alldata" : []}
    for q in qu_out:
        quers['alldata'].append({'date' : list(q)[1].strftime("%d/%m/%Y"), 'value' : list(q)[0]})
    qu_out = json.dumps(quers)

    with open('jsonFiles\quer1.json', 'w') as outfile:
        json.dump(qu_out, outfile)

def json_writer2(qu_out):
    quers = {"alldata" : []}
    for q in qu_out:
        quers['alldata'].append({'type' : list(q)[0], 'desc' : list(q)[1], 'count' : list(q)[2]})
    qu_out = json.dumps(quers)

    with open('jsonFiles\quer2.json', 'w') as outfile:
        json.dump(qu_out, outfile)

def json_writer3(qu_out):
    quers = {"alldata" : []}
    for q in qu_out:
        quers['alldata'].append({'name' : list(q)[0], 'count' : list(q)[1]})
    qu_out = json.dumps(quers)

    with open('jsonFiles\quer3.json', 'w') as outfile:
        json.dump(qu_out, outfile)

def json_writer4(qu_out):
    quers = {"alldata" : []}
    for q in qu_out:
        quers['alldata'].append({'day' : list(q)[0], 'count' : list(q)[1]})
    qu_out = json.dumps(quers)

    with open('jsonFiles\quer4.json', 'w') as outfile:
        json.dump(qu_out, outfile)

def json_writer5(qu_out):
    quers = {"alldata" : []}
    for q in qu_out:
        if int(list(q)[0]) >= 12:
            hour = list(q)[0] + 'PM'
        else:
            hour = list(q)[0] + 'AM'
        quers['alldata'].append({'hour' : hour, 'count' : list(q)[1]})
    qu_out = json.dumps(quers)

    with open('jsonFiles\quer5.json', 'w') as outfile:
        json.dump(qu_out, outfile)

def json_writer6(qu_out):
    quers = {"alldata" : []}
    for q in qu_out:
        quers['alldata'].append({'month' : list(q)[0] + ' / ' + list(q)[1], 'percent' : list(q)[2]})
    qu_out = json.dumps(quers)

    with open('jsonFiles\quer6.json', 'w') as outfile:
        json.dump(qu_out, outfile)
# END

app = Flask(__name__)

# ---------------------------------------------INITIAL QUERY CALLS------------------------------------------
crime_type_filter, crime_sub_type_filter, dist_filter, crimeLoc_filt = q.filter_options()
tot_inc = q.incident_count(filter_dict)
json_writer(q.query1_data(filter_dict))
json_writer2(q.query2_data(filter_dict))
json_writer3(q.query3_data(filter_dict))
json_writer4(q.query4_data(filter_dict))
json_writer5(q.query5_data(filter_dict))
json_writer6(q.query6_data(filter_dict))
# ENDs

# ---------------------------------------------INDEX ROUTE------------------------------------------
@app.route('/', methods=['POST', 'GET'])
def index():
    status = 1
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']
        if username == 'police' and password == 'police_admin':
            return render_template('police.html', ctype_filter = crime_type_filter, cSubtype_filter = crime_sub_type_filter, dist_filter = dist_filter, crimeLoc_filt = crimeLoc_filt, tot_inc = tot_inc)
        elif username == 'public' and password == 'public_admin':
            return render_template('public.html', ctype_filter = crime_type_filter, dist_filter = dist_filter)
        elif username == 'security' and password == 'security_agency_admin':
            return render_template('security.html', ctype_filter = crime_type_filter, dist_filter = dist_filter)
        elif username == 'analyst' and password == 'analyst_admin':
            return render_template('analysts.html', ctype_filter = crime_type_filter, dist_filter = dist_filter)
        else:
            status = 0
            return render_template('index.html', status=status, total_cnt = get_total_cnt())
    else:
        return render_template('index.html', status=status, total_cnt = get_total_cnt())
# END

# ---------------------------------------------FILTER ROUTES------------------------------------------
@app.route('/ctype', methods=['POST'])
def ctype():
    if request.method == 'POST':
        filter_val = request.form['crime_type']
        filter_dict['ctype'] = filter_val
        return route_query_calls()

@app.route('/csubtype', methods=['POST'])
def csubtype():
    if request.method == 'POST':
        filter_val = request.form['crime_sub_type']
        filter_dict['csub_type'] = filter_val
        return route_query_calls()

@app.route('/distfilt', methods=['POST'])
def distfilt():
    if request.method == 'POST':
        filter_val = request.form['dist_filt']
        filter_dict['dist'] = filter_val
        return route_query_calls()

@app.route('/crimeloc', methods=['POST'])
def crimeloc():
    if request.method == 'POST':
        filter_val = request.form['crime_loc']
        filter_dict['loc'] = filter_val
        return route_query_calls()

@app.route('/timegran', methods=['POST'])
def timegran():
    if request.method == 'POST':
        filter_val = request.form['time_gran']
        filter_dict['gran'] = filter_val
        return route_query_calls()
        
@app.route('/arrest', methods=['POST'])
def arrest():
    if request.method == 'POST':
        filter_val = request.form['arrest']
        filter_dict['arrest'] = filter_val
        return route_query_calls()

@app.route('/domestic', methods=['POST'])
def domestic():
    if request.method == 'POST':
        filter_val = request.form['domestic']
        filter_dict['domestic'] = filter_val
        return route_query_calls()

@app.route('/dates', methods=['POST'])
def dates():
    if request.method == 'POST':
        start_d = request.form['start_date'].split("+")[0]
        end_d = request.form['end_date'].split("+")[0]
        start_d = datetime.strptime(start_d, "%a %b %d %Y %H:%M:%S %Z")
        end_d = datetime.strptime(end_d, "%a %b %d %Y %H:%M:%S %Z")
        filter_dict['start_date'] = start_d
        filter_dict['end_date'] = end_d
        return route_query_calls()
# END

# ---------------------------------------------QUERY ROUTES------------------------------------------
@app.route('/query1', methods=['POST'])
def query1():
    if request.method == 'POST':
        return json_reader('jsonFiles\quer1.json')

@app.route('/query2', methods=['POST'])
def query2():
    if request.method == 'POST':
        return json_reader('jsonFiles\quer2.json')

@app.route('/query3', methods=['POST'])
def query3():
    if request.method == 'POST':
        return json_reader('jsonFiles\quer3.json')
    
@app.route('/query4', methods=['POST'])
def query4():
    if request.method == 'POST':
        return json_reader('jsonFiles\quer4.json')

@app.route('/query5', methods=['POST'])
def query5():
    if request.method == 'POST':
        return json_reader('jsonFiles\quer5.json')

@app.route('/query6', methods=['POST'])
def query6():
    if request.method == 'POST':
        return json_reader('jsonFiles\quer6.json')
#END

if __name__ == "__main__":
    app.run()