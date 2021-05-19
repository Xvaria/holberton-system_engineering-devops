# Fix typo in apache2 server.
exec { 'replace':
  command => 'sed -i 's/phpp/php/' /var/www/html/wp-settings.php',
  path    => '['/usr/bin', '/bin']',
}