<?php
error_reporting(0);
$id=$_POST['id'];
$newname=$_POST['newname'];
$con=mysqli_connect("localhost","root","huang110");
function smart_equname_change($con,$id,$newname)
{
    $result=mysqli_query($con,"select name from now_data where id='$id'");
    $name=mysqli_fetch_array($result,MYSQLI_NUM);
     mysqli_select_db($con,"lot");
     $result=mysqli_query($con,"select * from smart");
     while($row=mysqli_fetch_array($result,MYSQLI_NUM))
     {
       if($row[1]==$name[0])
       {
          mysqli_query($con,"update smart set sensor='$newname' where sensor='$name[0]'");
       }
     }
}
if(!$con)
{
	echo 'error';
}
else
{
     mysqli_query($con,"set name 'utf8'");
     mysqli_select_db($con,"lot");
     mysqli_query($con,"select * from now_data where name='$newname'");
     $i=mysqli_affected_rows($con);
     if($i==1)
     {
     	echo 'exist';
     }
     else
     {
          smart_equname_change($con,$id,$newname);
          mysqli_select_db($con,"data");
          mysqli_query($con,"update now_data set name='$newname' where id='$id'");
     	echo 'success';
     }
}
mysqli_close($con);
?>
