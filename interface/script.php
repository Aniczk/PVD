<?php
	if(isset($_POST['list']) && isset($_POST['organism']))
	{
		$organism = $_POST['organism'];
		$proteins =  $_POST['list'];
		// $command = 'python analysis.py ' . $organism  . $proteins;
		// $command = 'python analysis.py ' . $organism . $proteins;
		// $command = "python3 analysis.py";
		// echo $command;
		// $output = passthru("python3 analysis.py $organism $proteins");
		$command = 'python analysis.py '.$organism.' '.$proteins.'';
		// $command = escapeshellcmd('python generate_raport.py ' . $organism . $proteins);
		$output = shell_exec($command);
		echo $output;


		// $cdm = escapeshellcmd
		// $cmd = 'python analysis.py '.$organism.' '.$proteins.'';
		// echo $cmd;
		// exec ( "analysis.py $organism $proteins" );
		// $output = shell_exec($command);

}
?>