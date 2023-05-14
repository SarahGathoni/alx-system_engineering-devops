# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

# Enable the virtual host
exec { 'enable-wordpress':
  command     => 'a2ensite wordpress.conf',
  refreshonly => true,
  path        => '/usr/sbin:/usr/bin',
  subscribe   => File['/etc/apache2/sites-available/wordpress.conf'],
}

# Restart Apache service
service { 'apache2':
  ensure  => running,
  enable  => true,
  require => [Package['apache2'], Exec['enable-wordpress']],
}
