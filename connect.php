<?php

$con=mysqli_connect('localhost','root','');

   if(!$con)
   {
       echo 'Not connected to server';
   }
if(!mysqli_select_db($con,'users'))
{
    echo 'database not selected';
}

$firstname = $_POST['firstname'];
$lastname = $_POST['lastname'];
$emailid = $_POST['emailid'];
$pass1 = $_POST['pass1'];
$pass2 = $_POST['pass2'];
 


    $sql =  "INSERT INTO signup(firstname,lastname,emailid,pass1,pass2)VALUES('$firstname','$lastname','$emailid','$pass1','$pass2')";


if(!mysqli_query($con,$sql))
{
    echo 'values not inserted';
}


else
{
    echo 'values successfully inserted' ."<br>";
} 
?>