// -------------------------------------CHART LAYOUTS----------------------------------------

// ------------------QUERY 1 CHART------------------
var ctx = document.getElementById('query1_gr').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Crime Incident Count',
            data: [],
            backgroundColor: 'transparent',
            borderColor: '#0179e9',
            borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// ------------------QUERY 2 CHART------------------
var ctx = document.getElementById('query2_gr').getContext('2d');
var chart2 = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: [],
        datasets: [{
            label: 'Crime Incident Count',
            data: [],
            backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"]
        }]
    },
    options: {
        title: {
            display: true,
            text: 'Predicted world population (millions) in 2050'
        }
    }
});

// ------------------QUERY 3 CHART------------------
var ctx = document.getElementById('query3_gr').getContext('2d');
var chart3 = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Crime Incident Count',
            data: [],
            backgroundColor: 'transparent',
            borderColor: '#c45850',
            borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// ------------------QUERY 4 CHART------------------
var ctx = document.getElementById('query4_gr').getContext('2d');
var chart4 = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: "Crime Incident Count",
            backgroundColor: ["#e8c3b9", "#e8c3b9","#e8c3b9","#e8c3b9","#e8c3b9", "#e8c3b9", "#e8c3b9"],
            data: []
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Crime Incidents'
        },
        scales: {
            x: {
                stacked: true
            },
            y: {
                stacked: true
            }
        },
        indexAxis: 'y'
    }
});

// ------------------QUERY 5 CHART------------------
var ctx = document.getElementById('query5_gr').getContext('2d');
var chart5 = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Crime Incident Count',
            data: [],
            backgroundColor: 'transparent',
            borderColor: '#c45850',
            borderWidth: 2
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// ------------------QUERY 6 CHART------------------
var ctx = document.getElementById('query6_gr').getContext('2d');
var chart6 = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: "Percentage Change",
            backgroundColor: ['green', 'red', 'green', 'red', 'green', 'red', 'green', 'green', 'red', 'green', 'red', 'red', 'green', 'red', 'red'],
            data: []
        }]
    },
    options: {
        legend: {
            display: false
        },
        title: {
            display: true,
            text: 'Percentage'
        },
        scales: {
            x: {
                stacked: true
            },
            y: {
                stacked: true
            }
        },
        indexAxis: 'y'
    }
});

// -------------------------------------CHART AJAX CALLS----------------------------------------

// ------------------CHART 1 AJAX CALL------------------
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

// ------------------CHART 2 AJAX CALL------------------
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

// ------------------CHART 3 AJAX CALL------------------
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