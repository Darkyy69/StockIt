from rest_framework.serializers import ModelSerializer
# from ..models.models_documents import *
# from ..models.models_Entite_marchandise import *
# from ..models.models_Entite_personnes import *
# from ..models.models_ligneDocument import *
# from ..models.models_info_extra import *
# from ..models.models_payement import *
# from ..models.models_remise import *
# from ..models.models_stock import *

from django.apps import apps


# class DocumentSerializer(ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = ('__all__')  

# class DocumentSerializer(ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = ('__all__') 

# class DocumentSerializer(ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = ('__all__') 

# class DocumentSerializer(ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = ('__all__') 

# class DocumentSerializer(ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = ('__all__') 

# class DocumentSerializer(ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = ('__all__') 

# class DocumentSerializer(ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = ('__all__') 

# class DocumentSerializer(ModelSerializer):
#     class Meta:
#         model = Documents
#         fields = ('__all__')                                 




from django.apps import apps
from rest_framework.serializers import ModelSerializer
from ..models.models_documents import Documents  # Import your model(s) here

# Get all models from installed apps
all_models = apps.get_models()

# Filter non-abstract subclasses of Documents
document_subclasses = [model for model in all_models if issubclass(model, Documents) and not model._meta.abstract]

# Create serializers for each subclass
for subclass in document_subclasses:
    class SubclassSerializer(ModelSerializer):
        class Meta:
            model = subclass
            fields = '__all__'  # or specify the fields you want to include

    # Register the serializer dynamically with a name based on the subclass
    globals()[f"{subclass.__name__}Serializer"] = SubclassSerializer        