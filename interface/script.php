<?php
	if(isset($_POST['list']) && isset($_POST['organism']))
	{
		$organism = $_POST['organism'];
		$proteins =  $_POST['list'];

		$command = 'python generate_report.py '.$organism.' '.$proteins.'';
		$output = shell_exec($command);
		echo $output;

}
?>
