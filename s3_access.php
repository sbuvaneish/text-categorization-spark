<?php

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
$key = 'input/1/article2.txt';

$result = $s3->putObject([
	'Bucket' => $bucket,
	'Key'    => $key,
	'Body'   => "The gods must be crazy",
]);

$key = 'input/2/article1.txt';

$result = $s3->putObject([
	'Bucket' => $bucket,
	'Key'    => $key,
	'SourceFile' => 'sample_article.txt',
]);

?>