# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  # vagrant vbguest plugin automatically installs the correct guest editions for your version of virtualbox
  # to enable: "vagrant plugin install vagrant-vbguest"
  config.vbguest.auto_update = true
  # do NOT download the iso file from a webserver.  your local virtualbox distro should have the iso already.
  config.vbguest.no_remote = true

  config.vm.box = "centos/7"

  config.ssh.keys_only = false
  config.ssh.insert_key = false

  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"  # fix windows rsync bug

  config.vm.network :forwarded_port, guest: 5672, host: 5672   # rabbitmq default port
  config.vm.network :forwarded_port, guest: 15672, host: 15672 # rabbitmq management console
  config.vm.network :forwarded_port, guest: 27017, host: 27017 # mongodb default port

  # to enable chef berkshelf with vagrant: "vagrant plugin install vagrant-berkshelf"
  config.berkshelf.enabled = true

  config.vm.provision "chef_solo" do |chef|
    chef.add_recipe "rabbitmq"
    chef.add_recipe "mongodb"
    chef.json = {"rabbitmq" => {"mgmt_console" => true}}
  end

end
