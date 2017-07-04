#!/etc/php/bin/php

<?php
echo "X-Powered-By: PHP/ 5.6.27\n";
echo "Content-type: text/html\n\n";
?>



<?php
Error_reporting(E_ALL);
INI_Set('display_errors','on');
$q = isset($_GET["q"]) ? intval($_GET["q"]) : '';
if(empty($q)) {
   echo '请选择一个网站';
 //  exit;
}

$con = mysqli_connect('localhost','root','haitao');
if (!$con)
{
   	die('Could not connect: ' . mysqli_error($con));
}
// 选择数据库
mysqli_select_db($con,"mynetdb");
// 设置编码，防止中文乱码
mysqli_set_charset($con, "utf8");
 
$sql="SELECT * FROM mynet WHERE Num = '".$q."'";
//$sql="SELECT * FROM websites WHERE name = 'Google'";
 
$result = mysqli_query($con,$sql);
if (!$result) {
	 printf("Error: %s\n", mysqli_error($con));
	  exit();
}
echo "<table border='1' width='80%' align='center'>
	<tr>
	<th>编号</th>
	<th>网站名称</th>
	<th>网站地址</th>
	<th>添加时间</th>
	</tr>";
 
while($row = mysqli_fetch_array($result))
{
	    echo "<tr>";
	    echo "<td>" . $row['Num'] . "</td>";
		echo "<td>" . $row['Name'] . "</td>";
		echo "<td>" . $row['URL'] . "</td>";
		echo "<td>" . $row['Time'] . "</td>";
		echo "</tr>";
}
echo "</table>";
 
mysqli_close($con);
?>

