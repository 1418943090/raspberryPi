<?php
error_reporting(1);
$name=$_POST['name'];
$status=$_POST['status'];
$ID=$_POST['ID'];
$con=mysqli_connect("localhost","root","huang110");
      if(!$con)
      {
        echo  "error";
      }
      else
      {
        mysqli_query($con,"set name 'utf8'");
        mysqli_select_db($con,"lot");

        $Result1=mysqli_query($con,"select * from node_information where ID='$ID'");
        $i=mysqli_affected_rows($con);
        if($i==1)
        {
           echo "idexist";
        }
        else{
            $Result1=mysqli_query($con,"select * from node_information where name='$name'");
            $i=mysqli_affected_rows($con);
           if($i==1)
           {
              echo 'nameexist';
           }
           else{
              $result1=mysqli_query($con,"select * from equ where id='$ID'");
              $i=mysqli_affected_rows($con);
              if($i==0)
              {
                 echo "noexist";
              }
           else
           {
               $equ_information=mysqli_fetch_array($result1,MYSQLI_NUM);
               $equ_style=$equ_information[1];

              mysqli_query($con,"insert into node_information(name,style,status,ID) values('$name','$equ_style','$status','$ID')");
            }
        }
     }
         mysqli_close($con);
      }
?>