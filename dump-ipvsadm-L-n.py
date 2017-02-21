import subprocess

out_bytes = subprocess.check_output(['watch', '-n 0.1', 'ipvsadm', '-L', '-n'])
out_bytes_str = out_bytes.decode()
print(out_bytes_str)