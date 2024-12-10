from hotels.models import Hotel, Room
from django.db import connection

# def run():
    # hotel = Hotel()
    # hotel.name = "Fairmount"
    # hotel.location = "Toronto"
    # hotel.description = "fancy and expensive"
    # hotel.total_rooms = 1500
    
    # hotel.save()

    #All data rows
    # hotels = Hotel.objects.all()
    # print(hotels)

    # #First Data Row
    # first_hotel = Hotel.objects.first()
    # print(first_hotel)

    #Using the create function
    # Hotel.objects.create(
    #     name="Shangri La",
    #     location="university st",
    #     description="super fancy and very expensive",
    #     total_rooms=800
    # )

    #To add data using foreign keys:
    # hotel = Hotel.objects.all()[1]
    # Room.objects.create(
    #     hotel= hotel,
    #     room_type= "Single",
    #     price= 500,
    #     available= False
    # )

    # print(Room.objects.filter(available=False))
    # print(Room.objects.filter(price__lte=500))

    #How to update a record
    # hotel = Hotel.objects.first()
    # hotel.name = "Chelseaaa"
    # hotel.save()

    # hotel = Hotel.objects.first()
    # print(hotel.)

    # hotel1 = Hotel.objects.all()[1]
    # Room.objects.create(
    #     hotel= hotel1,
    #     room_type= "Single",
    #     price= 730,
    #     available= True
    # )

    # hotel2 = Hotel.objects.all()[1]
    # Room.objects.create(
    #     hotel= hotel2,
    #     room_type= "Double",
    #     price= 249,
    #     available= True
    # )

    # hotel = Hotel.objects.all()[1]
    # print(hotel.hotel_set.all())

    # #Queries used when performing these operations
    # print(connection.queries)