# fix wrong extension that causes 500 error in wordpress

exec {'fix wordpress site':
  command => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/:/usr/bin/'
}
