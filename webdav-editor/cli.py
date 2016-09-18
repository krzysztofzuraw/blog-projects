import argparse

from webdav_utility import Client

client = Client()

parser = argparse.ArgumentParser(description='Simple command line utility for WebDAV')
subparsers = parser.add_subparsers(help='Commands')

login_parser = subparsers.add_parser('login', help='Authenticate with WebDAV')
login_parser.add_argument('-s', '--server', required=True)
login_parser.add_argument('-u', '--user', required=True)
login_parser.add_argument('-p', '--password', required=True)
login_parser.set_defaults(func=client.login)

ls_parser = subparsers.add_parser('ls', help='List content of directory under WebDAV')
ls_parser.add_argument('-p', '--path', required=True)
ls_parser.set_defaults(func=client.list_content)

upload_parser = subparsers.add_parser('upload', help='Upload files to WebDAV')
upload_parser.add_argument('-f', '--from', metavar='PATH')
upload_parser.add_argument('-t', '--to', metavar='PATH')
upload_parser.set_defaults(func=client.upload_file)

download_parser = subparsers.add_parser('download', help='Download files from WebDAV')
download_parser.add_argument('-f', '--from', metavar='PATH')
download_parser.add_argument('-t', '--to', metavar='PATH')
download_parser.set_defaults(func=client.download_file)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
