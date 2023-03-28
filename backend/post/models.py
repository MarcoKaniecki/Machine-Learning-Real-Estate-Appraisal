from django.db import models

# The models file in Django defines the database schema for the application, including the tables, fields, and relationships between them. 
# It also provides an object-relational mapping (ORM) layer for interacting with the database, 
# allowing developers to work with Python objects instead of writing raw SQL queries.

class Post(models.Model):
    # content is a paragraph description of the house (will change in the future)
    area = models.IntegerField(blank=True, null=True)
    zone = models.CharField(max_length=100, blank=True, null=True)
    lotArea = models.IntegerField(blank=True, null=True)
    utilities = models.CharField(max_length=100, blank=True, null=True)
    neighborhood = models.CharField(max_length=100, blank=True, null=True)
    bldgType = models.CharField(max_length=100, blank=True, null=True)
    houseStyle = models.CharField(max_length=100, blank=True, null=True)
    overallQual = models.CharField(max_length=100, blank=True, null=True)
    overallCond = models.CharField(max_length=100, blank=True, null=True)
    yearBuilt = models.IntegerField(blank=True, null=True)
    yearRemod = models.IntegerField(blank=True, null=True)
    exterior1 = models.CharField(max_length=100, blank=True, null=True)
    exterQual = models.CharField(max_length=100, blank=True, null=True)
    exterCond = models.CharField(max_length=100, blank=True, null=True)
    bsmtFinType1 = models.CharField(max_length=100, blank=True, null=True)
    bsmtFindSF1 = models.IntegerField(blank=True, null=True)
    totalBsmtSF = models.IntegerField(blank=True, null=True)
    heating = models.CharField(max_length=100, blank=True, null=True)
    heatingQC = models.CharField(max_length=100, blank=True, null=True)
    centralAir = models.CharField(max_length=100, blank=True, null=True)
    electrical = models.CharField(max_length=100, blank=True, null=True)
    fullBath = models.IntegerField(blank=True, null=True)
    halfBath = models.IntegerField(blank=True, null=True)
    bedroom = models.IntegerField(blank=True, null=True)
    kitchen = models.IntegerField(blank=True, null=True)
    kitchenQual = models.CharField(max_length=100, blank=True, null=True)
    totRmsAbvGrd = models.IntegerField(blank=True, null=True)
    garageType = models.CharField(max_length=100, blank=True, null=True)
    garageCars = models.IntegerField(blank=True, null=True)
    garageArea = models.IntegerField(blank=True, null=True)
    garageQual = models.CharField(max_length=100, blank=True, null=True)
    woodDeckSF = models.IntegerField(blank=True, null=True)
    fence = models.CharField(max_length=100, blank=True, null=True)
    
    image = models.ImageField(upload_to='post_images')
    
    def __str__(self):
        return self.title