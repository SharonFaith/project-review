from django.test import TestCase
from .models import Projects, Profile, Rating, DisplayProfile, DisplayProjects 
import datetime as dt
from django.contrib.auth.models import User


class ProfileTestClass(TestCase):

    #set up method
    def setUp(self):
        self.user1 = User(username = 'a-user')
        self.user1.save()
        #self.new = Profile(bio = 'this is a bio', user = self.user1)
        self.new = Profile(user=self.user1, bio="hi")
  #  def tearDown(self):
    #    Profile.objects.all().delete()
        
    
    def test_instance(self):

        self.assertTrue(isinstance(self.new, Profile))
    
    def test_save_profile(self):

        self.new.save_profile()
        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.new.save_profile()
        new2 = Profile(user = self.user1, bio = 'profile bio number 2 ')
        new2.save_profile()

        new2.delete_profile()
        
        profiles = Profile.objects.all()

        self.assertTrue(len(profiles) == 1)

    def test_update_profile(self):
        self.new.save_profile()
        print(self.new.id)
        new2 = Profile(user = self.user1, bio = 'profile bio number 2 ')
        new2.save_profile()

        Profile.update_profile(4, 'the new bio')
       
        self.assertEqual(Profile.objects.filter(id = 4).first().bio, 'the new bio')


# Create your tests here.
