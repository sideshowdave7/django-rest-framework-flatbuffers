Djano Rest Framework Flatbuffer Support

Use:

The mixin provided is compatible with DRF's ModelSerializer.  For example:


```python
from rest_framework import serializers
from rest_framework_flatbuffers.django import FBSerializerMixin

class MyModelSerializer(serializers.ModelSerializer, FBSerializerMixin):

    
    Normal DRF Serializer Here
```
    

Now you can use MyModelSerializer.fb_data to obtain a flatbuffer representation.

Note: This relies on generating the correct .hbs model files and having them be importable.  The namespace of the hbs model must match the import path of the django model.
