import unittest
import requests

url = "http://172.18.58.80/spicyx"


class spicyxidk(unittest.TestCase):

    def test_TestUrl(self):
        try:
            resp = requests.get(url)
            if int(resp.status_code) == 200:
                print("[TestUrl] OK")
            else:
                print("[TestUrl] Requested URL not found")
        except Exception as e:
            print("[TestUrl] Error: ", {e})

        def test_spicyx_2(self):
            print("[spicyx_2] spicyx 2")

    if __name__ == '__main__':
        unittest.main()
