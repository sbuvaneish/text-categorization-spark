<?php

session_start();
$session_id = session_id();

require (__DIR__.'/aws_php/aws-autoloader.php');

$s3 = new Aws\S3\S3Client([
	'region'  => 'us-west-1',
	'version' => 'latest',
	'credentials' => [
	    'key'    => "",
	    'secret' => "",
	]
]);

$bucket = 'sbh-cloudproject3';

if ($_SERVER['REQUEST_METHOD'] == 'POST'){
	foreach($_FILES['files']['name'] as $index => $name){
		$key = 'input/' . $session_id . '/' . $name;
		$result = $s3->putObject([
			'Bucket' => $bucket,
			'Key'    => $key,
			'SourceFile' => $_FILES['files']['tmp_name'][$index],
		]);

	}
}

?>

<form method="post" enctype="multipart/form-data">
    <input type="file" name="files[]" id="files" multiple="" directory="" webkitdirectory="" mozdirectory="">
    <input class="button" type="submit" value="Upload" />
</form>