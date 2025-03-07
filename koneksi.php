<?php
    $host     = 'quiz-db';
    $user     = 'root'; 
    $password = 'password';                  
    $db       = 'quiz_pengupil';

    $con = mysqli_connect($host, $user, $password, $db);
    if (!$con) { 
        die("Connection failed: " . mysqli_connect_error());    
    }
?>