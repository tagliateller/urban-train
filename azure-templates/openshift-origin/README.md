# RedHat Openshift Origin cluster on Azure

When creating the RedHat Openshift Origin cluster on Azure, you will need a SSH RSA key for access. 

## SSH Key Generation

1. Windows - https://www.digitalocean.com/community/tutorials/how-to-create-ssh-keys-with-putty-to-connect-to-a-vps
2. Linux - https://help.ubuntu.com/community/SSH/OpenSSH/Keys#Generating_RSA_Keys
3. Mac - https://help.github.com/articles/generating-ssh-keys/#platform-mac

## Create the cluster
### Create the cluster on the Azure Portal

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fderdanu%2Fazure-openshift%2Fmaster%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Fderdanu%2Fazure-openshift%2Fmaster%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

### Create the cluster with powershell

```powershell
New-AzureRmResourceGroupDeployment -Name <DeploymentName> -ResourceGroupName <RessourceGroupName> -TemplateUri https://raw.githubusercontent.com/derdanu/azure-openshift/master/azuredeploy.json
```

## Install Openshift Origin with Ansible

You must use SSH Agentforwarding. The Installation is based on [Openshift Ansible](https://github.com/openshift/openshift-ansible). The lastest repository has been checked out on the master into the directory */opt/openshift-ansible/* and a minimal configuration file was created at */etc/ansible/hosts* for [Openshift Origin](https://github.com/openshift/origin).


### Bash or Cygwin Terminal

```bash
user@localmachine:~$ eval `ssh-agent`
user@localmachine:~$ ssh-add
user@localmachine:~$ ssh -A <MasterIP>
[adminUsername@master ~]$ ./openshift-install.sh
```

### Putty on Windows

To login on the Master please refer to the [Agent forwarding HowTo](https://github.com/Azure/azure-quickstart-templates/blob/master/101-acs-mesos/docs/SSHKeyManagement.md#key-management-and-agent-forwarding-with-windows-pageant) for Putty using Pageant.

```bash  
[adminUsername@master ~]$ ./openshift-install.sh
```

------

## Parameters
### Input Parameters

| Name| Type           | Description |
| ------------- | ------------- | ------------- |
| adminUsername  | String       | Username for SSH Login and Openshift Webconsole |
|  adminPassword | SecureString | Password for the Openshift Webconsole |
| sshKeyData     | String       | Public SSH Key for the Virtual Machines |
| masterDnsName  | String       | DNS Prefix for the Openshift Master / Webconsole | 
| numberOfNodes  | Integer      | Number of Openshift Nodes to create |
| image | String | Operating System to use. RHEL or CentOs |
| masterVMSize | String | The size of the Master Virtual Machine |
| infranodeVMSize| String | The size of the Infranode Virtual Machine |
| nodeVMSize| String | The size of the each Node Virtual Machine |

### Output Parameters

| Name| Type           | Description |
| ------------- | ------------- | ------------- |
| openshift Webconsole | String       | URL of the Openshift Webconsole |
| openshift Master ssh |String | SSH String to Login at the Master |
| openshift Router Public IP | String       | Router Public IP. Needed if you want to create your own Wildcard DNS |

------

This template deploys a RedHat Openshift Origin cluster on Azure.

# Aktuell

Ausführung 15.6.16

robert@c3p0:~/workspace/azure-openshift$ azure group deployment create -f azuredeploy.json -e azuredeploy.parameters.json -g origin-group -n origin-deployment
info:    Executing command group deployment create
+ Initializing template configurations and parameters                          
+ Creating a deployment                                                        
info:    Created template deployment "origin-deployment"
+ Waiting for deployment to complete                                           
error:   Deployment provisioning state was not successful
error:   Deployment 'master' could not be found.
info:    Error information has been recorded to /home/robert/.azure/azure.err
error:   group deployment create command failed

Kommentar: In der Übersicht fehlt tatsächlich der Master ! Bzw. eine VM namens Master

# Ausführung 17.6.

- VM-Size des Master reduziert, dann kommen wir mit 10 Cores aus
- neues Problem: die Verbindung wird zu früh abgebrochen
- manuelles ausführung master.sh "missing become password"
- TODO: Versuch wie oben beschrieben


