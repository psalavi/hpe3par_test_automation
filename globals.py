namespace = None
yaml_dir = None
access_protocol = None
hpe3par_cli = None
hpe3par_version = None
platform = None
replication_test = False
status_check_timeout = 300
encryption_test = False
newbrand_test = False
HOST_TYPE = 3
MATCHED_SET = 4
encoding = 'utf-8'
master_node_ip = None
master_node_username = None
master_node_password = None

# CRDs list
k8s_snapshot_crds = ['volumesnapshotclass', 'volumesnapshotcontent', 'volumesnapshot']
hpe_crds = ['hpereplicationdeviceinfo', 'hpenodeinfo', 'hpesnapshotgroupinfo', 'hpevolumegroupinfo', 'hpevolumeinfo',
        'snapshotgroupclass', 'snapshotgroupcontent', 'snapshotgroup', 'volumegroupclass', 'volumegroupcontent',
        'volumegroup']