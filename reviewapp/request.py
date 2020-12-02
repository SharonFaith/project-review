import urllib.request, json
from .models import DisplayProfile, DisplayProjects
from decouple import config
import urllib.parse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



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

        if profile_pic is not None:
                pic_url = image_url + profile_pic
        else:
                pic_url = profile_pic

      
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
        if landing_page is not None:
                pic_url = image_url + landing_page
        else:
                pic_url = landing_page
        print(pic_url)
        project_object = DisplayProjects(id, profile, title, pic_url, description, live_site)

        project_results.insert(0, project_object)

    return project_results


def get_profiles():

    get_profiles_url = 'https://awwardreview-app.herokuapp.com/api/theprofiles/'

    
    
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

    get_projects_url = 'https://awwardreview-app.herokuapp.com/api/theprojects/'

    
    
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


def get_a_profile(id):
    
    profile_url = 'https://awwardreview-app.herokuapp.com/api/theprofiles/profile-id/{}/'.format(id)
    image_url = 'https://res.cloudinary.com/{}/'.format(cloud_name)
    with urllib.request.urlopen(profile_url) as url:

        get_profile_data = url.read()                     
        get_profile_response = json.loads(get_profile_data)
      
        profile_object = None
        if get_profile_response:
            id = get_profile_response.get('id')            
            user = get_profile_response.get('user')
            profile_pic = get_profile_response.get('profile_pic')
            bio= get_profile_response.get('bio')
            phone_number = get_profile_response.get('phone_number')
            projects = get_profile_response.get('projects')
            if profile_pic is not None:
                pic_url = image_url + profile_pic
            else:
                pic_url = profile_pic
            profile_object = DisplayProfile(id, user, pic_url, bio, phone_number, projects)
    
    #print(profile_object)
    return profile_object



def update_a_profile(id, current_user, profile_pic, bio, phone_number):
    profile_url = 'https://awwardreview-app.herokuapp.com/api/theprofiles/profile-id/{}/'.format(id)
    #users = User.objects.all()
    the_user = current_user

    #print(the_user) = 
    token = Token.objects.filter(user = the_user)
    print(token)
    authorize = token
    print(authorize)
    
    values = {
        #'user': name,
        'profile_pic': profile_pic,
        'bio': bio,
        'phone_number':phone_number
    }
    headers = {
        'Authorization' : authorize
    }
    
    data = urllib.parse.urlencode(values)
   
    data = data.encode('ascii')

   # data = json.loads(data.decode('utf-8'))
   
    req = urllib.request.Request(profile_url, data, headers, method='PUT')
    print(data)
    with urllib.request.urlopen(req) as response:
        pass
        #the_page = response.read()
    print(response.status)
    print(response.reason)



def get_a_project(id):
    
    project_url = 'https://awwardreview-app.herokuapp.com/api/theprojects/project-id/{}/'.format(id)
    image_url = 'https://res.cloudinary.com/{}/'.format(cloud_name)
    with urllib.request.urlopen(project_url) as url:

        get_project_data = url.read()                     
        get_project_response = json.loads(get_project_data)
      
        project_object = None
        if get_project_response:
            id = get_project_response.get('id')            
            profile = get_project_response.get('profile')
            title = get_project_response.get('title')
            landing_page = get_project_response.get('landing_page')
            description = get_project_response.get('description')
            live_site = get_project_response.get('live_site')
            if landing_page is not None:
                pic_url = image_url + landing_page
            else:
                pic_url = landing_page
            project_object = DisplayProjects(id, profile, title, pic_url, description, live_site)
    
    #print(project_object)
    return project_object

