from rest_framework import serializers
from .models import StudentData1

class StudentSerializer (serializers.ModelSerializer):
    class Meta:
        model = StudentData1
        fields = ["id" , "name" , "roll" , "enroll" , "desc" , "email" , "url" , "python" , "fsd" , "coa" , "total" , "percentage"]

        def get_total(self , obj):
            return obj.python + obj.fsd + obj.coa
        
        def get_percentage(self , obj):
            total = obj.python + obj.fsd + obj.coa
        
            return round((total / 75) * 100 , ndigits=2)
        

class MarksSerializer (serializers.ModelSeriaizer):
    class Meta:
        model = StudentData1
        fields = ["python" , "fsd" , "coa"]

    def python_validate(self , value):
        if not (0 <= value <= 25):
            raise serializers.ValidationError("Python marks should be between 0 and 25.")
        return value
    

    def fsd_validate(self , value):
        if not (0 <= value <= 25):
            raise serializers.ValidationError("FSD marks should be between 0 and 25.")
        return value
    

    def coa_validate(self , value):
        if not (0 <= value <= 25):
            raise serializers.ValidationError("COA marks should be between 0 and 25.")
        return value