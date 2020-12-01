import urllib.request, json
from .models import DisplayProfile, DisplayProjects
from decouple import config
import urllib.parse
from django.contrib.auth.models import User



cloud_name = config('CLOUD_NAME')

def process_profile(profile_list):
    profile_results = []
    image_url = 'https://res.cloudinary.com/{}/'.format(cloud_name)
    for profile in profile_list:
        id = profile.get('id')
        user = profile.get('user')
        profile_pic = profile.get('profile_pic')
        bio = profile.get('bio')
        phone_number = profile.get('phone_number')
        projects = profile.get('projects')

        pic_url = image_url + profile_pic

      
        profile_object = DisplayProfile(id, user, pic_url, bio, phone_number, projects)

        profile_results.insert(0, profile_object)

    return profile_results

def process_projects(project_list):
    project_results = []
    image_url = 'https://res.cloudinary.com/{}/'.format(cloud_name)
    for project in project_list:
        id = project.get('id')
        profile = project.get('profile')
        title = project.get('title')
        landing_page = project.get('landing_page')
        description = project.get('description')
        live_site = project.get('live_site')
        print(landing_page)
        pic_url = image_url + landing_page
        print(pic_url)
        project_object = DisplayProjects(id, profile, title, pic_url, description, live_site)

        project_results.insert(0, project_object)

    return project_results


def get_profiles():

    get_profiles_url = 'https://app-m-tribune.herokuapp.com/api/profiles/'

    
    
    with urllib.request.urlopen(get_profiles_url) as url:

        get_profile_data = url.read()
        print('hi')
       
        #print(get_merch_data)
        get_profile_response = json.loads(get_profile_data)
        #print(get_merch_response)
        profile_results = None

        if get_profile_response != None:
            profile_results_list = get_profile_response
            #print(merch_results_list)
            profile_results = process_profile(profile_results_list)

    return profile_results

def get_projects():

    get_projects_url = 'https://app-m-tribune.herokuapp.com/api/projects/'

    
    
    with urllib.request.urlopen(get_projects_url) as url:

        get_projects_data = url.read()
        print('hi')
       
        #print(get_merch_data)
        get_project_response = json.loads(get_projects_data)
        #print(get_merch_response)
        project_results = None

        if get_project_response != None:
            project_results_list = get_project_response
            #print(merch_results_list)
            project_results = process_projects(project_results_list)

    return project_results

