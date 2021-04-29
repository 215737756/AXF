from django.test import TestCase, client


# Create your tests here.
class Test_tt(TestCase):
    def test_01(self):
        clients = client.Client()
        response = clients.get('https://www.baidu.com/')
        print(response)
        self.assertEqual(
            response.status_code,
            200,
            '不是200'

        )

if __name__ == '__main__':
    test_tt = Test_tt()
    test_tt.test_01()