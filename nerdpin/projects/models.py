from tkinter.tix import Tree
import babel
from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link = models.CharField(max_length=2000,null=True,blank=True)
    # vote_total stores the no.of up or down votes a project gets
    vote_total = models.IntegerField(default=0,blank=True,null=True)
    # vote_ratio stores the ratio of positive votes a project gets 
    vote_ratio = models.IntegerField(default=0,blank=True,null=True)
    # Creating a many to many relation using Tag class 
    tags = models.ManyToManyField('Tag',blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),('down','Down Vote')
    )
    
    # here "project" is field in the child table where its foreign key is parent table i.e Project table
    # on_delete=models.CASCADE represents when ever a x-project is delete from the Project table the entire review block 
    # of that table gets deleted
    
    # note: ForeignKey establishes a one - to - many relationship
    project = models.ForeignKey("Project", on_delete=models.CASCADE)
    
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    
    def __str__(self):
        return self.value
    
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    
    def __str__(self):
        return self.name
    
    