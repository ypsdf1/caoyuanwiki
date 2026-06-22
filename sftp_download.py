#!/usr/bin/env python3
"""
sftp_download.py - SFTP download using paramiko
Usage:
  python sftp_download.py <command> [args]

Commands:
  ls                               List files in root directory
  get <remote_path> <local_path>   Download file from remote to local
"""
import sys
import os

HOST = "sfe4-connect.simpfun.cn"
PORT = 2046
USER = "sfe3192491.df7d2f7f"
PASS = "5350427807"


def get_sftp_client():
    import paramiko
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname=HOST,
        port=PORT,
        username=USER,
        password=PASS,
        look_for_keys=False,
        allow_agent=False,
        timeout=15,
    )
    sftp = client.open_sftp()
    return client, sftp


def cmd_ls(args):
    client, sftp = get_sftp_client()
    remote_path = args[0] if args else "."
    files = sftp.listdir_attr(remote_path)
    for f in files:
        is_dir = "d" if f.st_mode is not None and (f.st_mode & 0o040000) else "-"
        size = f.st_size if f.st_size is not None else 0
        mtime = ""
        from datetime import datetime
        if f.st_mtime is not None:
            mtime = datetime.fromtimestamp(f.st_mtime).strftime("%b %d %H:%M")
        print(f"{is_dir} {size:>8} {mtime} {f.filename}")
    sftp.close()
    client.close()


def cmd_get(args):
    if len(args) < 2:
        print("Usage: get <remote_path> <local_path>")
        sys.exit(1)
    remote_path = args[0]
    local_path = args[1]
    client, sftp = get_sftp_client()
    os.makedirs(os.path.dirname(local_path) or ".", exist_ok=True)
    sftp.get(remote_path, local_path)
    actual_size = os.path.getsize(local_path)
    print(f"Downloaded: {local_path} ({actual_size} bytes)")
    sftp.close()
    client.close()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    commands = {"ls": cmd_ls, "get": cmd_get}

    if command not in commands:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)

    try:
        commands[command](args)
    except Exception as e:
        print(f"FAILED: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
