ty = ec2.InstanceType.T2_MICRO
pulumi.export('v', ami.get_linux_ami(ty))
