// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example - 科目別成績
var ctx = document.getElementById("myBarChart");

// データが存在しない場合の処理
if (typeof latestScores === 'undefined') {
    latestScores = {};
}

// データを配列に変換
var subjects = Object.keys(latestScores);
var scores = Object.values(latestScores);

// 各科目に異なる色を設定
var backgroundColors = [];
var borderColors = [];

var colorPalette = [
    { bg: "rgba(2,117,216,0.8)", border: "rgba(2,117,216,1)" },      // 青
    { bg: "rgba(40,167,69,0.8)", border: "rgba(40,167,69,1)" },      // 緑
    { bg: "rgba(220,53,69,0.8)", border: "rgba(220,53,69,1)" },      // 赤
    { bg: "rgba(255,193,7,0.8)", border: "rgba(255,193,7,1)" },      // オレンジ
    { bg: "rgba(111,66,193,0.8)", border: "rgba(111,66,193,1)" },    // 紫
    { bg: "rgba(23,162,184,0.8)", border: "rgba(23,162,184,1)" }     // 水色
];

for (var i = 0; i < subjects.length; i++) {
    var color = colorPalette[i % colorPalette.length];
    backgroundColors.push(color.bg);
    borderColors.push(color.border);
}

var myBarChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: subjects,
        datasets: [{
            label: "最新の得点",
            backgroundColor: backgroundColors,
            borderColor: borderColors,
            borderWidth: 1,
            data: scores,
        }],
    },
    options: {
        scales: {
            xAxes: [{
                gridLines: {
                    display: false
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    max: 100,
                    maxTicksLimit: 6
                },
                gridLines: {
                    display: true
                }
            }],
        },
        legend: {
            display: false
        },
        tooltips: {
            callbacks: {
                label: function(tooltipItem) {
                    return tooltipItem.yLabel + '点';
                }
            }
        }
    }
});