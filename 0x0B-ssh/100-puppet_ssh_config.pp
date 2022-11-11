# configure ssh client to login without password

$ssh_client = '~/.ssh/config'

file { $ssh_client:
    ensure  => 'file',
    content => 'Host *
                    PasswordAuthentication no
                    IdentityFile ~/.ssh/school
                    PreferredAuthentications publickey',
    mode    => '0744',
    group   => 'www-data',
    owner   => 'www-data'
}
