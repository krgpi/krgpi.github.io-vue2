#!/usr/bin/python3
import datetime
now = datetime.datetime.now()
print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("""<script src="//code.jquery.com/jquery-1.11.2.min.js"></script>""")
print("""<script src="/~osmc/js/jquery.csvToTable.js"></script>""")
print("<title>Weather Reports</title>")
print("""<LINK rel="stylesheet" href="/~osmc/main.css" type="text/css">""")
print("</head>")
print("""<table class="table" border="0" cellspacing="0" summary="outline"><body><thead><tr><td id="main_body">""")
print("""<a href = "/~osmc/">Home</a>""")
print("""<h4>Outdoor TEMP - PRES</h4>""")
print("""</td></tr></thead></table><table class="table" border="0" cellspacing="0" summary="outline"><tbody>""")
for h in range(5,now.hour):
	print("<tr>")
	for s in ["00","20","40"]:
		hs = str(h)+s
		print("""<td id="main_body"><img src="/~osmc/outside/ous_{0}.jpg" alt = "{0} is not available.""></td>""".format(hs))
	print("</tr>")
print("""</tbody></table><table class="table" border="0" cellspacing="0" summary="outline"><tfoot><tr><td id="main_body">""")
print("""<img src="/~osmc/graph.png"></td><td id="main_body">
<div class="csv-table-convert">
<script>
$(function() {
	$('.csv-table-convert').CSVToTable('/~osmc/weather.csv', 
		{ 
		headers: ['TEMP','PRES','HUMI','TS']
		}
		);
	});
</script>
</div>
<br>
""")
print("</td></tr></tfoot></table></body>")
print("</html>")