import pickle
from urlparse import urlparse
import easywebdav


class Client(object):

    def login(self, *args):
        argparse_namespace = args[0]
        url_components = urlparse(argparse_namespace.server)
        host, port = url_components.netloc.split(':')
        webdav_client = easywebdav.connect(
            host=host,
            port=port,
            path=url_components.path,
            username=argparse_namespace.user,
            password=argparse_namespace.password
        )
        pickle.dump(webdav_client, open('webdav_login', 'wb'))

    def list_content(self, *args):
        webdav_client = pickle.load(open('webdav_login', 'rb'))
        argparse_namespace = args[0]
        print [i.name for i in webdav_client.ls(argparse_namespace.path)]

    def upload_file(self, *args):
        webdav_client = pickle.load(open('webdav_login', 'rb'))
        argparse_namespace = args[0]
        webdav_client.upload(
            argparse_namespace.from_path, argparse_namespace.to_path
        )

    def download_file(self, *args):
        webdav_client = pickle.load(open('webdav_login', 'rb'))
        argparse_namespace = args[0]
        webdav_client.download(
            argparse_namespace.from_path, argparse_namespace.to_path
        )
