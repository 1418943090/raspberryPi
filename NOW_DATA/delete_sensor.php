<?php
error_reporting(0);
$id=$_POST['id'];

   $con=mysqli_connect("localhost","root","huang110");
   if(!$con) 
   {
      echo "error";
   }
    else
   {
      mysqli_query($con,"set name 'utf8'");
      mysqli_select_db($con,"lot");
      mysqli_query($con,"delete from now_data where id='$id'");
      mysqli_close($con);
   }   
?>