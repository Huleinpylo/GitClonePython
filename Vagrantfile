# -*- mode: ruby -*-
# vi: set ft=ruby :

# Define the Vagrant environment
Vagrant.configure("2") do |config|

  # Default box for Windows 10
  config.vm.define "windows10" do |win10|
    win10.vm.box = "StefanScherer/windows_10"
    win10.vm.communicator = "winrm"
    win10.vm.network "private_network", type: "dhcp"
    win10.vm.provision "shell", inline: <<-SHELL
      # Your Windows provisioning script here
    SHELL
    win10.vm.provision "file", source: "files/GitGetter.py", destination: "C:/GitGetter.py"
    win10.vm.provision "shell", inline: "python C:/GitGetter.py"
  end

  # Default box for Windows 11
  config.vm.define "windows11" do |win11|
    win11.vm.box = "StefanScherer/windows_11"
    win11.vm.communicator = "winrm"
    win11.vm.network "private_network", type: "dhcp"
    win11.vm.provision "shell", inline: <<-SHELL
      # Your Windows 11 provisioning script here
    SHELL
    win11.vm.provision "file", source: "files/GitGetter.py", destination: "C:/GitGetter.py"
    win11.vm.provision "shell", inline: "python C:/GitGetter.py"
  end

  # Default box for macOS Catalina
  config.vm.define "macos" do |mac|
    mac.vm.box = "VMR/MacOS_Catalina-R"
    mac.vm.network "private_network", type: "dhcp"
    mac.vm.provision "shell", inline: <<-SHELL
      # Your macOS provisioning script here
    SHELL
    mac.vm.provision "file", source: "files/GitGetter.py", destination: "/Users/vagrant/GitGetter.py"
    mac.vm.provision "shell", inline: "python3 /Users/vagrant/GitGetter.py"
  end

  # Default box for Debian Bullseye
  config.vm.define "debian" do |debian|
    debian.vm.box = "debian/bullseye64"
    debian.vm.network "private_network", type: "dhcp"
    debian.vm.provision "shell", inline: <<-SHELL
      # Your Debian provisioning script here
    SHELL
    debian.vm.provision "file", source: "files/GitGetter.py", destination: "/home/vagrant/GitGetter.py"
    debian.vm.provision "shell", inline: "python3 /home/vagrant/GitGetter.py"
  end

  # Default box for CentOS 7
  config.vm.define "centos" do |centos|
    centos.vm.box = "generic/centos7"
    centos.vm.network "private_network", type: "dhcp"
    centos.vm.provision "shell", inline: <<-SHELL
      # Your CentOS provisioning script here
    SHELL
    centos.vm.provision "file", source: "files/GitGetter.py", destination: "/home/vagrant/GitGetter.py"
    centos.vm.provision "shell", inline: "python3 /home/vagrant/GitGetter.py"
  end

end
