# Fix typo in apache2 server.
exec { 'replace':
  environment => ['DIR=/var/www/html/wp-settings.php',
                  'OLD=phpp',
                  'NEW=php'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR',
  path        => ['/usr/bin', '/bin']
}