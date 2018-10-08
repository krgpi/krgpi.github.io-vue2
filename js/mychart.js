// 2) CSVから２次元配列に変換
function csv2Array(str) {
  var csvData = [];
  var lines = str.split("\n");
  for (var i = 0; i < lines.length - 1; ++i) {
    var cells = lines[i].split(",");
    csvData.push(cells);
  }
  return csvData;
}

function drawChart(data) {
  // 3)chart.jsのdataset用の配列を用意
  var tmpLabels = [], tmpData1 = [], tmpData2 = [], tmpData3 = [];
  for (var row in data) {
    tmpLabels.push(data[row][3])
    tmpData1.push(data[row][0])
    // tmpData2.push(data[row][1])
    tmpData3.push(data[row][2])
  };

  // 4)chart.jsで描画
  var ctx = document.getElementById("myChart").getContext("2d");
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: tmpLabels,
      datasets: [
        { label: "Temperature", yAxisID:"A", data: tmpData1, backgroundColor: "red", fill: 0 },
        // { label: "Pressure", data: tmpData2, backgroundColor: "blue" },
        { label: "Humidity", yAxisID:"B", data: tmpData3, backgroundColor: "green", fill: 0 }
      ]},
    options: {
      scales: {
        yAxes: [{
          id: "A",
          position: "left",
        },{
          id: "B",
          position: "right",
          ticks: {
            max:100,
            min:0
          }
        }]
      }
    }
  });
}

function main() {
  // 1) ajaxでCSVファイルをロード
  var req = new XMLHttpRequest();
  var filePath = '/docs/weather.csv';
  req.open("GET", filePath, true);
  req.onload = function() {
    // 2) CSVデータ変換の呼び出し
    data = csv2Array(req.responseText);
    // 3) chart.jsデータ準備、4) chart.js描画の呼び出し
    drawChart(data);
    var div = document.getElementById("nowcast"); 
    div.textContent = "室温 " + data[data.length - 1][0] + "℃\n気圧" + data[data.length - 1][1] + " Pa\n湿度" + data[data.length - 1][2] +"%\n"+ data[data.length - 1][3] + " 取得";
  }
  req.send(null);

}

main();