from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import json
import os


def load_swagger_schema(app_path):
    """Load and return the Swagger JSON schema."""
    json_path = os.path.join(app_path,"swagger_docs.json")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

class CustomSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        return schema
 
swagger_info = openapi.Info(
    title="Multi-App API",
    default_version='v1',
    description="API for blog and football apps"
)

schema_view = get_schema_view(
    swagger_info,
    public=True,
    generator_class=CustomSchemaGenerator,  
)
