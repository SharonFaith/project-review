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
class ProjectsTestClass(TestCase):

    #set up method
    def setUp(self):
        self.user1 = User(username = 'a-user')
        self.user1.save()
        #self.new = Profile(bio = 'this is a bio', user = self.user1)
        self.new = Profile(user=self.user1, bio="hi")
        self.new.save_profile()
        self.new_proj = Projects(profile= self.new, title='proj', description='tfhgghg', live_site='live site')
  #  def tearDown(self):
    #    Profile.objects.all().delete()
        
    
    def test_instance(self):

        self.assertTrue(isinstance(self.new_proj, Projects))
    
    def test_save_project(self):

        self.new_proj.save_project()
        projects = Projects.objects.all()

        self.assertTrue(len(projects) > 0)

    def test_delete_project(self):
        self.new_proj.save_project()
        new2 = Projects(profile= self.new, title='another proj', description='a description', live_site='another live site')
        new2.save_project()

        new2.delete_project()
        
        project = Projects.objects.all()

        self.assertTrue(len(project) == 1)

    def test_update_project(self):
        self.new_proj.save_project()
        print(self.new_proj.id)
        new2 = Projects(profile= self.new, title='another proj', description='a description', live_site='another live site')
        new2.save_project()

        Projects.update_project(4, 'the new description')
       
        self.assertEqual(Projects.objects.filter(id = 4).first().description, 'the new description')


class RatingTestClass(TestCase):

    #set up method
    def setUp(self):
        self.user1 = User(username = 'a-user')
        self.user1.save()
        #self.new = Profile(bio = 'this is a bio', user = self.user1)
        self.new = Profile(user=self.user1, bio="hi")
        self.new.save_profile()
        self.new_proj = Projects(profile= self.new, title='proj', description='tfhgghg', live_site='live site')
        self.new_proj.save_project()

        self.new_rating = Rating(user_rating=self.user1, project_rated=self.new_proj, design=9.00, usability=9.00, content=9.00, overall= 9.00)
        
  #  def tearDown(self):
    #    Profile.objects.all().delete()
        
    
    def test_instance(self):

        self.assertTrue(isinstance(self.new_rating, Rating))
    
    def test_save_rating(self):

        self.new_rating.save_rating()
        ratings = Rating.objects.all()

        self.assertTrue(len(ratings) > 0)

    def test_delete_project(self):
        self.new_rating.save_rating()
        newproj2 = Projects(profile= self.new, title='another proj', description='a description', live_site='another live site')
        newproj2.save_project()
        new2 = Rating(user_rating=self.user1, project_rated=newproj2, design=9.00, usability=9.00, content=9.00, overall=9.00)
        new2.save_rating()

        new2.delete_rating()
        
        rating = Rating.objects.all()

        self.assertTrue(len(rating) == 1)

    def test_update_rating(self):
        self.new_rating.save_rating()
        print(self.new_rating.id)
        design = 10.00
        usability = 9.00
        content = 9.00
        newproj2 = Projects(profile= self.new, title='another proj', description='a description', live_site='another live site')
        newproj2.save_project()
        new2 = Rating(user_rating=self.user1, project_rated=newproj2, design=9.00, usability=9.00, content=9.00, overall=9.00)
        new2.save_rating()

        Rating.update_rating(4, 10)
       
        self.assertEqual(Rating.objects.filter(id = 4).first().usability, 10)


class TestDisplayProfile(TestCase):
   
    #set up method
    def setUp(self):
        self.display_api_profile = DisplayProfile(1, 'pat', '/pics/', 'a bio', '0299203030', [{ 'project': '1'}, {'project': '2'}])
    
    def tearDown(self):
        DisplayProfile.api_profile_list = []
       
    def test_check_instance_variables(self):
        self.assertEquals(self.display_api_profile.id,1)
        self.assertEquals(self.display_api_profile.user,'pat')
        self.assertEquals(self.display_api_profile.profile_pic,'/pics/')
        self.assertEquals(self.display_api_profile.bio, 'a bio')
        self.assertEquals(self.display_api_profile.phone_number,'0299203030')
        self.assertEquals(self.display_api_profile.projects,[{ 'project': '1'}, {'project': '2'}])

    def test_save_new_profile(self):
        self.display_api_profile.save_profile()

        self.assertEqual(len(DisplayProfile.api_profile_list), 1)


class TestDisplayProjects(TestCase):
   
    #set up method
    def setUp(self):
        self.display_api_projects = DisplayProjects(1, 'pat', 'title', 'landing_page', 'description', 'live site')
    
    def tearDown(self):
        DisplayProjects.api_projects_list = []
       
    def test_check_instance_variables(self):
        self.assertEquals(self.display_api_projects.id,1)
        self.assertEquals(self.display_api_projects.profile,'pat')
        self.assertEquals(self.display_api_projects.title,'title')
        self.assertEquals(self.display_api_projects.landing_page, 'landing_page')
        self.assertEquals(self.display_api_projects.description,'description')
        self.assertEquals(self.display_api_projects.live_site, 'live site')

    def test_save_newproject(self):
        self.display_api_projects.save_project()

        self.assertEqual(len(DisplayProjects.api_projects_list), 1)
