import subprocess

out_bytes = subprocess.check_output(['ipvsadm', '-L', '-n'])
out_bytes_str = out_bytes.decode()
print(out_bytes_str)