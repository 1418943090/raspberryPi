<?php
 $con=mysqli_connect("localhost","root","huang110");
      mysqli_query($con,"set name 'utf-8'");
      if(!$con)
      {
      }
      else
      {
        $data=Array();
        mysqli_select_db($con,"lot");
        $num=0;
        $result=mysqli_query($con," select * from node_information ");
        while($row = mysqli_fetch_array($result,MYSQLI_NUM))
        {
           array_push($data,$row[0]);
             $num++;
        }
        $DATA=array(
        'num'=>$num,
        'equipment'=>$data
        );
        echo json_encode($DATA);

          mysqli_close($con);
      }
?>