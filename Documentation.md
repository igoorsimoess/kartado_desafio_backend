# Documentation

##### This file is intended to document all the steps I took in order to complete the kartado challenge.

1. Fork repository and clone into my local development env.

2. A new branch for developing purposes was created called 'develop' following GIT good practices.

3. At first, I took an overview of the existing models and the database in order to understand the fields the API should return.

3. Then I made all the environment setup, i.e: 

    1. create a virtual environment
    2. pip install in requirements.txt

***

### Development steps

#### Required API response by the challenge

###### In this section, I will detail the process objectively and by topics.

1. In _**app/occurrences/models**_ file I added the two new required fields: 
    - road_name
    - status_name

    Two new functions was required to retrieve the respective instance value for Road and Status:  
    &nbsp;
    ``` 
    @property: status_instance_name
    @property: road_instance_name
    ```
    They were tagged as property in order to follow the pythonic way of dealing of instances attributes.

2. In _**serializers**_ file, a class serializer for Occurrence model was created in order to jsonify and return the data through the API serialized and formatted as JSON.  
At it, the fields of interest were specified.

3. In _**views**_ a new endpoint was created. First, importing the new OccurrenceSerializer and the Occurrence model.  
Then, following the REST Django practices, implemented the permissions to require the authenticated user. 
4. In _**urls**_ we use router.register to specify the url for our new model.

>Here, for this project purposes, I retrieve all the occurrence data ordered by its id attribute but in desc (reversed), so we can visualize the last occurrences added.

***

### New Feature

Since Kartado core activity is to provide a modern way of dealing with infrastructure processes, the API should be able to store the image of the occurrence. An image speaks more than words. So a new field for images was created. It is accessible by its link.

What I did:

1. In _**models**_ a new occurrence_image was created. It's nullable so the already existing data won't be affected.

    - also, a new function is required to specify and differentiate each url for each instance of occurrence image.

2. To route to the respective image, two new environment variables were added to _**settings**_ file: MEDIA_URL and MEDIA_ROOT

The first one specifies the path to store our images (for now) and the second one builds, based on the BASE_DIR already existing env. variable, build the absolute path for that instance.

in _**urls**_ we import the static method and our settings file and specify the url of our images.

>A new module is required towards the image receiving feature works. Pillow is a image handler library and was added in the requirements.txt file.






