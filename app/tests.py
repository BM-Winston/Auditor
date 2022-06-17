from django.test import TestCase
from .models import Auditor,Profile

# Create your tests here.

class AuditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.auditor = Auditor(name = 'Auditor', email = 'moringa214@gmail.com')
        self.auditor.save()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.auditor,Auditor))

    # Testing Save Method
    def test_save_method(self):
        self.auditor.save_auditor()
        auditors = Auditor.objects.all()
        self.assertTrue(len(auditors) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.auditor.delete_auditor()
        auditors = Auditor.objects.all()
        self.assertTrue(len(auditors) == 0)

    # Testing Update Method
    def test_update_method(self):
        self.auditor.update_auditor()
        auditors = Auditor.objects.all()
        self.assertTrue(len(auditors) > 0)

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.profile = Profile(name = 'Auditor', email = 'moringa214@gmail.com')
        self.profile.save()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    # Testing Update Method
    def test_update_method(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

        

        




