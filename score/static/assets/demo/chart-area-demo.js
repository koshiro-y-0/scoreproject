// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example - 成績推移（科目別）
var ctx = document.getElementById("myAreaChart");

// データが存在しない場合の処理
if (typeof subjectData === 'undefined' || Object.keys(subjectData).length === 0) {
    subjectData = {};
}

// カラーパレット
var colors = [
    { bg: "rgba(2,117,216,0.2)", border: "rgba(2,117,216,1)" },      // 青
    { bg: "rgba(40,167,69,0.2)", border: "rgba(40,167,69,1)" },      // 緑
    { bg: "rgba(220,53,69,0.2)", border: "rgba(220,53,69,1)" },      // 赤
    { bg: "rgba(255,193,7,0.2)", border: "rgba(255,193,7,1)" },      // オレンジ
    { bg: "rgba(111,66,193,0.2)", border: "rgba(111,66,193,1)" },    // 紫
    { bg: "rgba(23,162,184,0.2)", border: "rgba(23,162,184,1)" }     // 水色
];

// すべての日付を収集してソート
var allDates = [];
for (var subject in subjectData) {
    allDates = allDates.concat(subjectData[subject].dates);
}
allDates = Array.from(new Set(allDates)).sort();

// データセットを作成
var datasets = [];
var colorIndex = 0;

for (var subject in subjectData) {
    var dateScoreMap = {};
    
    // その科目のデータをマッピング
    for (var i = 0; i < subjectData[subject].dates.length; i++) {
        dateScoreMap[subjectData[subject].dates[i]] = subjectData[subject].scores[i];
    }
    
    // すべての日付に対応するデータを作成（データがない日はnull）
    var scoreData = [];
    for (var j = 0; j < allDates.length; j++) {
        if (dateScoreMap[allDates[j]] !== undefined) {
            scoreData.push(dateScoreMap[allDates[j]]);
        } else {
            scoreData.push(null);
        }
    }
    
    var color = colors[colorIndex % colors.length];
    
    datasets.push({
        label: subject,
        lineTension: 0.3,
        backgroundColor: color.bg,
        borderColor: color.border,
        pointRadius: 5,
        pointBackgroundColor: color.border,
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: color.border,
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: scoreData,
        spanGaps: false
    });
    
    colorIndex++;
}

var myLineChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: allDates,
        datasets: datasets
    },
    options: {
        scales: {
            xAxes: [{
                gridLines: {
                    display: false
                },
                ticks: {
                    maxTicksLimit: 10
                }
            }],
            yAxes: [{
                ticks: {
                    min: 0,
                    max: 100,
                    maxTicksLimit: 6
                },
                gridLines: {
                    color: "rgba(0, 0, 0, .125)",
                }
            }],
        },
        legend: {
            display: true,
            position: 'bottom'
        },
        tooltips: {
            mode: 'index',
            intersect: false,
        }
    }
});