<?php


     $con=mysqli_connect("localhost","root","huang110");
     if(!$con)
     {
     	echo "error";
     }
     else
     {
     mysqli_query($con,"set name utf-8");
     mysqli_select_db($con,"lot");
     mysqli_query($con,"update node_information set status='$status' where name='$name'");
     $result=mysqli_query($con,"select ID from node_information where name='$name'");
     echo $result;
     mysqli_close($con);
     
    }
?>
