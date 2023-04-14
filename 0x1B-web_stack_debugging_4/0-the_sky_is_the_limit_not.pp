# increase nginx request limit from 15 to 4096

exec {'Increase limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx; service nginx restart',
  path    => '/usr/local/bin:/bin/:/usr/bin/'
}
