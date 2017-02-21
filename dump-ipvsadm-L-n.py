import subprocess
import re
import csv


csv_file = "dump-ipvsadm-L-n.csv"

out_bytes = subprocess.check_output(['ipvsadm', '-L', '-n'])
out_bytes_str = out_bytes.decode()
# print(out_bytes_str)

hdr = re.findall(r'(RemoteAddress)(:)(Port)'
                 r'(\s+)(Forward\s+)(Weight)(\s+)(ActiveConn)(\s+)(InActConn)', out_bytes_str)
stats = re.findall(r'(\d+.\d+.\d+.\d+)(:)(\d+)'
                   r'(\s+)(Route\s+)(\d+)(\s+)(\d+)(\s+)(\d+)', out_bytes_str)

with open(csv_file, 'a') as csv_fd:
    rst = dict()
    hdr = hdr[0]
    for stat in stats:
        rst[stat[0] + ':' + hdr[5]] = stat[5]
        rst[stat[0] + ':' + hdr[7]] = stat[7]
        rst[stat[0] + ':' + hdr[9]] = stat[9]
    writer = csv.DictWriter(csv_fd, fieldnames=rst.keys())
    writer.writeheader()
    writer.writerow(rst)
