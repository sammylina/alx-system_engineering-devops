# Install flask@2.1.0 from pip3

package { 'pip3 installed':
    ensure => 'installed',
    name   => 'pip3'
}

exec { 'install flask':
    command => 'pip3 install flask==2.1.0',
    require => Package['pip3 installed']
}
