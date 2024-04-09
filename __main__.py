import pulumi
from pulumi_aws import ec2
import ami

ty = ec2.InstanceType.T2_MICRO
pulumi.export('v', ami.get_linux_ami(ty))
