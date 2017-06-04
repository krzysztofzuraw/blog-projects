import requests


def main():
    response = requests.get('https://httpbin.org/get')
    print(response.json())


if __name__ == '__main__':
    main()
