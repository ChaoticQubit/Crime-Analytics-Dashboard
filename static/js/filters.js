// -------------------------------------FILTER FADER FUNCTIONS----------------------------------------
function fetch_fade_div_start(){
    document.getElementById('fade-text-div').style.backgroundColor = 'rgba(76, 175, 80, 0.3)';
    document.getElementById('fade-dash').style.opacity = 0.3;
    document.getElementById('fade-text').style.display = 'block';
}

function fetch_fade_div_end(){
    document.getElementById('fade-text').style.display = 'none';
    document.getElementById('fade-text-div').style.backgroundColor = 'rgba(255, 255, 255, 1)';
    document.getElementById('fade-dash').style.opacity = 1;
}

// -------------------------------------FILTERED AJAX CALLS----------------------------------------
function filter_calls(){
    // ------------------QUERY 1 CALL------------------
    $.ajax({
        type : 'POST',
        url : '/query1',
        datatype : 'json',
        success : function(result, textStatus, jqXHR){
            var data = JSON.parse(result);
            var dates = data.alldata.map(function(e){
                return e.date;
            });
    
            var values = data.alldata.map(function(e){
                return e.value;
            });
    
            chart.data.labels = dates;
            chart.data.datasets[0].data = values;
            chart.update();
        }
    });

    // ------------------QUERY 2 CALL------------------
    $.ajax({
        type : 'POST',
        url : '/query2',
        datatype : 'json',
        success : function(result, textStatus, jqXHR){
            var data = JSON.parse(result);
            var types = data.alldata.map(function(e){
                return e.type;
            });
    
            var counts = data.alldata.map(function(e){
                return e.count;
            });
    
            chart2.data.labels = types;
            chart2.data.datasets[0].data = counts;
            chart2.update();
        }
    });

    // ------------------QUERY 3 CALL------------------
    $.ajax({
        type : 'POST',
        url : '/query3',
        datatype : 'json',
        success : function(result, textStatus, jqXHR){
            var data = JSON.parse(result);
            var names = data.alldata.map(function(e){
                return e.name;
            });
    
            var counts = data.alldata.map(function(e){
                return e.count;
            });
    
            chart3.data.labels = names;
            chart3.data.datasets[0].data = counts;
            chart3.update();
        }
    });

    // ------------------QUERY 4 CALL------------------
    $.ajax({
        type : 'POST',
        url : '/query4',
        datatype : 'json',
        success : function(result, textStatus, jqXHR){
            var data = JSON.parse(result);
            var days = data.alldata.map(function(e){
                return e.day;
            });
    
            var counts = data.alldata.map(function(e){
                return e.count;
            });
    
            chart4.data.labels = days;
            chart4.data.datasets[0].data = counts;
            chart4.update();
        }
    });

    // ------------------QUERY 5 CALL------------------
    $.ajax({
        type : 'POST',
        url : '/query5',
        datatype : 'json',
        success : function(result, textStatus, jqXHR){
            var data = JSON.parse(result);
            var hours = data.alldata.map(function(e){
                return e.hour;
            });
    
            var counts = data.alldata.map(function(e){
                return e.count;
            });
    
            chart5.data.labels = hours;
            chart5.data.datasets[0].data = counts;
            chart5.update();
        }
    });

    // ------------------QUERY 6 CALL------------------
    $.ajax({
        type : 'POST',
        url : '/query6',
        datatype : 'json',
        success : function(result, textStatus, jqXHR){
            var data = JSON.parse(result);
            var months = data.alldata.map(function(e){
                return e.month;
            });
    
            var counts = data.alldata.map(function(e){
                return e.percent;
            });
    
            chart6.data.labels = months;
            chart6.data.datasets[0].data = counts;
            chart6.update();
        }
    });
}

// -------------------------------------FILTER FUNCTIONS----------------------------------------
function value_set(){
    fetch_fade_div_start();
    var e = document.getElementById("ctype");
    var ctype = e.options[e.selectedIndex].value;
    $.ajax({
        data : {
            'crime_type' : ctype
        },
        type : 'POST',
        url : '/ctype'
    })
    .done(function(data){
        $('#total_incid').text(data.total_inci);
        filter_calls();
        fetch_fade_div_end();
    });
}

function value_set_crime_subtype(){
    fetch_fade_div_start();
    var e = document.getElementById("csubtype");
    var csubtype = e.options[e.selectedIndex].value;
    $.ajax({
        data : {
            'crime_sub_type' : csubtype
        },
        type : 'POST',
        url : '/csubtype'
    })
    .done(function(data){
        $('#total_incid').text(data.total_inci);
        filter_calls();
        fetch_fade_div_end();
    });
}

function value_set_dist(){
    fetch_fade_div_start();
    var e = document.getElementById("distfilt");
    var district = e.options[e.selectedIndex].value;
    $.ajax({
        data : {
            'dist_filt' : district
        },
        type : 'POST',
        url : '/distfilt'
    })
    .done(function(data){
        $('#total_incid').text(data.total_inci);
        filter_calls();
        fetch_fade_div_end();
    });
}

function value_set_location(){
    fetch_fade_div_start();
    var e = document.getElementById("crimeLoc");
    var loc = e.options[e.selectedIndex].value;
    $.ajax({
        data : {
            'crime_loc' : loc
        },
        type : 'POST',
        url : '/crimeloc'
    })
    .done(function(data){
        $('#total_incid').text(data.total_inci);
        filter_calls();
        fetch_fade_div_end();
    });
}

function value_set_timegran(){
    fetch_fade_div_start();
    var e = document.getElementById("timegran");
    var gran = e.options[e.selectedIndex].value;
    $.ajax({
        data : {
            'time_gran' : gran
        },
        type : 'POST',
        url : '/timegran'
    })
}

function value_set_arrest(){
    fetch_fade_div_start();
    var e = document.getElementById("arrest").checked;
    if(e){
        var status = 'TRUE';
    }else{
        var status = 'FALSE';
    }
    $.ajax({
        data : {
            'arrest' : status
        },
        type : 'POST',
        url : '/arrest'
    })
    .done(function(data){
        $('#total_incid').text(data.total_inci);
        filter_calls();
        fetch_fade_div_end();
    });
}

function value_set_domestic(){
    fetch_fade_div_start();
    var e = document.getElementById("domestic").checked;
    if(e){
        var status = 'TRUE';
    }else{
        var status = 'FALSE';
    }
    $.ajax({
        data : {
            'domestic' : status
        },
        type : 'POST',
        url : '/domestic'
    })
    .done(function(data){
        $('#total_incid').text(data.total_inci);
        filter_calls();
        fetch_fade_div_end();
    });
}