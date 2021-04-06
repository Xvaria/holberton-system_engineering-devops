# SSH configuration file so that you can connect to a server without typing a password
file { 'holberton':
  path   => '/etc/.ssh/ssh_config',
  ensure => present,
  owner  => 'root',
  group  => 'root',
  mode   => '0644'
}

file_line { 'Turn off passwd auth':
  path => '/etc/.ssh/ssh_config',
  line => '    IdentityFile ~/.ssh/holberton'
}

file_line { 'Declare identity file':
  path => '/etc/.ssh/ssh_config',
  line => '    PasswordAuthentication no'
}