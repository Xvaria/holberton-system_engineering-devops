# create a manifest that kills a process named killmenow

exec { 'killmenow':
  command => 'pkill -e killmenow',
  path    => '/usr/bin:/usr/sbin:/bin',
}