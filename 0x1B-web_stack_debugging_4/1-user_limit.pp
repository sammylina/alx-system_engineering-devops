# Increase limit of files user holberton can open

exec {'Increase_nofile_limit':
  command => 'sed -i "/holberton/d" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/usr/bin/:/bin/'
}


