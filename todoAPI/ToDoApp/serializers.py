from rest_framework import serializers
from ToDoApp.models import Tasks

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('TaskID',
                  'TaskName',
                  'TaskCompletion')


