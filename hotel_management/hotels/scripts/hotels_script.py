from hotels.models import Hotel, Room

def run():
    hotel = Hotel()
    hotel.name = "Fairmount"
    hotel.location = "Toronto"
    hotel.description = "fancy and expensive"
    hotel.total_rooms = 1500
    
    hotel.save()