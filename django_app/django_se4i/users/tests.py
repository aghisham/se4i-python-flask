from django.test import TestCase


class UsersTest(TestCase):
    """Class test users"""

    def test_index(self):
        """Test get all users"""
        resp = self.client.get("/user")
        self.assertEqual(resp.status_code, 200)
