$file_path='/tmp/school'

file { $file_path:
    ensure  => 'file',
    content => 'I love Puppet',
    group   => 'www-data',
    owner   => 'www-data',
    mode    => '0744'
}
