import subprocess
import re
import csv
import sys
import time


if len(sys.argv) < 2:
    raise Exception('You must pass the timeout value')
timeout = float(sys.argv[1])
csv_file = sys.argv[2]

with open(csv_file, 'a') as csv_fd:
    while True:
        out_bytes = subprocess.check_output(['ipvsadm', '-L', '-n'])
        out_bytes_str = out_bytes.decode()
        # print(out_bytes_str)

        stats = re.findall(r'(\d+.\d+.\d+.\d+)(:)(\d+)'
                           r'(\s+)(Route\s+)(\d+)(\s+)(\d+)(\s+)(\d+)', out_bytes_str)

        rst = dict()
        for stat in stats:
            rst[stat[0] + ':Weight'] = stat[5]
            rst[stat[0] + ':ActiveConn'] = stat[7]
            rst[stat[0] + ':InActConn'] = stat[9]
        writer = csv.DictWriter(csv_fd, fieldnames=rst.keys())
        writer.writeheader()
        writer.writerow(rst)

        time.sleep(timeout)
