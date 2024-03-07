from rest_framework.serializers import ModelSerializer
from django.apps import apps

# Get all models from installed apps
all_models = apps.get_models()

# Create serializers for each class
for modelclass in all_models:
    class ModelClassSerializer(ModelSerializer):
        class Meta:
            model = modelclass
            fields = '__all__'  # or specify the fields you want to include

    # Register the serializer dynamically with a name based on the class
    globals()[f"{modelclass.__name__}Serializer"] = ModelClassSerializer    
