# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/trusty64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", path: "config/provision.sh", privileged: false

  # Development and testing VM
  config.vm.define "development", primary: true do |development|
    development.vm.network "forwarded_port", guest: 8000, host: 8000
    development.vm.network "forwarded_port", guest: 5432, host: 15432
    development.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
  end

  # Development and testing VM
  config.vm.define "dev1", primary: true do |development|
    development.vm.network "forwarded_port", guest: 8000, host: 18000
    development.vm.network "forwarded_port", guest: 5432, host: 45432
    development.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
  end

  # Development and testing VM
  config.vm.define "dev2", primary: true do |development|
    development.vm.network "forwarded_port", guest: 8000, host: 28000
    development.vm.network "forwarded_port", guest: 5432, host: 25432
    development.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
  end

  # Development and testing VM
  config.vm.define "dev3", primary: true do |development|
    development.vm.network "forwarded_port", guest: 8000, host: 38000
    development.vm.network "forwarded_port", guest: 5432, host: 35432
    development.vm.provider "virtualbox" do |vb|
      vb.memory = "2048"
    end
  end

end