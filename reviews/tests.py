from django.test import TestCase


# Create your tests here.
class TestViews(TestCase):
    def test_get_review_page(self):
        '''
        Tests that the review view renders the review template
        '''
        page = self.client.get("/review/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "review.html")
