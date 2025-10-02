from django.core.management.base import BaseCommand
from cars.models import Car


class Command(BaseCommand):
    help = 'Seeds the database with sample cars'

    def handle(self, *args, **kwargs):
        Car.objects.all().delete()

        cars = [
            # Budget-Friendly Daily Commuters
            {
                'name': 'Corolla',
                'brand': 'Toyota',
                'price': 22000,
                'purpose': 'daily',
                'car_type': 'sedan',
                'description': 'Budget-friendly compact sedan with proven reliability and excellent fuel economy.',
                'features': 'Fuel Efficient, Backup Camera, Bluetooth, Lane Departure Warning',
                'image_Url': 'https://images.unsplash.com/photo-1626072557464-90403d788e8d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8dG95b3RhJTIwY29yb2xsYXxlbnwwfHwwfHx8MA%3D%3D',
            },
            {
                'name': 'Civic',
                'brand': 'Honda',
                'price': 25000,
                'purpose': 'daily',
                'car_type': 'sedan',
                'description': 'Reliable and fuel-efficient sedan perfect for daily commuting with modern tech.',
                'features': 'Apple CarPlay, Lane Keeping Assist, Adaptive Cruise Control, Honda Sensing',
                'image_Url': 'https://images.unsplash.com/photo-1610768207795-72169abdf0d4?q=80&w=1469&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
            },
            {
                'name': 'Sentra',
                'brand': 'Nissan',
                'price': 21000,
                'purpose': 'daily',
                'car_type': 'sedan',
                'description': 'Affordable sedan with spacious interior and smooth ride quality.',
                'features': 'Automatic Emergency Braking, Smart Key, 7-inch Display, USB Ports',
                'image_Url': 'https://static.foxdealer.com/588/2020/04/2019-Nissan-Sentra-Side-View-of-Red-Exterior_o-1024x381.jpg',
            },
            {
                'name': 'Elantra',
                'brand': 'Hyundai',
                'price': 23000,
                'purpose': 'daily',
                'car_type': 'sedan',
                'description': 'Stylish sedan with impressive warranty and advanced safety features.',
                'features': 'Android Auto, Wireless Charging, Blind Spot Detection, Heated Seats',
                'image_Url': 'https://ap.ge/system/car/photos/008/374/979/medium.jpg?1739806618',
            },
            
            # Mid-Range Daily Drivers
            {
                'name': 'Camry',
                'brand': 'Toyota',
                'price': 27000,
                'purpose': 'daily',
                'car_type': 'sedan',
                'description': 'Comfortable mid-size sedan with hybrid option and renowned reliability.',
                'features': 'Hybrid Engine, Heated Seats, Sunroof, Toyota Safety Sense',
                'image_Url': 'https://images.unsplash.com/photo-1657872737697-737a2d123ef2?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8dG95b3RhJTIwY2Ftcnl8ZW58MHx8MHx8fDA%3D',
            },
            {
                'name': 'Accord',
                'brand': 'Honda',
                'price': 28000,
                'purpose': 'daily',
                'car_type': 'sedan',
                'description': 'Well-rounded sedan with powerful engine options and spacious cabin.',
                'features': 'Turbo Engine, Leather Seats, Navigation, Remote Start',
                'image_Url': 'https://images.unsplash.com/photo-1613538712814-42d97ce67d78?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8SG9uZGElMjBhY2NvcmR8ZW58MHx8MHx8fDA%3D',
            },
            {
                'name': 'Mazda3',
                'brand': 'Mazda',
                'price': 24000,
                'purpose': 'daily',
                'car_type': 'sedan',
                'description': 'Premium-feeling compact sedan with engaging driving dynamics.',
                'features': 'Premium Audio, Head-Up Display, Leather Trim, i-Activsense Safety',
                'image_Url': 'https://images.unsplash.com/photo-1599491143816-8c1ea12a4e06?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8TWF6ZGEzfGVufDB8fDB8fHww',
            },
            
            # Family SUVs
            {
                'name': 'CR-V',
                'brand': 'Honda',
                'price': 32000,
                'purpose': 'family',
                'car_type': 'suv',
                'description': 'Spacious SUV with excellent safety ratings and versatile cargo space.',
                'features': 'Third Row Seating, Blind Spot Monitoring, All-Wheel Drive, Power Liftgate',
                'image_Url': 'https://goodpappa.com/wp-content/uploads/2024/08/8te5zjcs.webp',
            },
            {
                'name': 'RAV4',
                'brand': 'Toyota',
                'price': 30000,
                'purpose': 'family',
                'car_type': 'suv',
                'description': 'Bestselling SUV with hybrid options and rugged capability.',
                'features': 'AWD, Hybrid Available, Apple CarPlay, Roof Rails, Smart Key',
                'image_Url': 'https://images.unsplash.com/photo-1739796216379-e5b6793f313a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTZ8fHRveW90YSUyMHJhdjR8ZW58MHx8MHx8fDA%3D',
            },
            {
                'name': 'Highlander',
                'brand': 'Toyota',
                'price': 40000,
                'purpose': 'family',
                'car_type': 'suv',
                'description': 'Three-row SUV perfect for large families with premium features.',
                'features': 'Third Row, AWD, Entertainment System, 8 Seats, Captain Chairs',
                'image_Url': 'https://images.unsplash.com/photo-1716068072348-64c2b7181161?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8dG95b3RhJTIwJTIwSGlnaGxhbmRlcnxlbnwwfHwwfHx8MA%3D%3D',
            },
            {
                'name': 'Pilot',
                'brand': 'Honda',
                'price': 42000,
                'purpose': 'family',
                'car_type': 'suv',
                'description': 'Versatile three-row SUV with advanced safety and comfort features.',
                'features': '8-Passenger Seating, Tri-Zone Climate, Honda Sensing, Wireless Charging',
                'image_Url': 'https://www.usnews.com/object/image/0000018c-457f-dc8f-addc-ef7fda470001/24-honda-pilot-ext1.jpg?update-time=1701973208102&size=responsive640&format=webp',
            },
            {
                'name': 'Sorento',
                'brand': 'Kia',
                'price': 35000,
                'purpose': 'family',
                'car_type': 'suv',
                'description': 'Stylish three-row SUV with great warranty and tech features.',
                'features': '7 Seats, Dual Sunroof, 360 Camera, Smart Cruise Control',
                'image_Url': 'https://www.kia.com/us/content/dam/kia/us/en/vehicles/sorento/2026/mep/hero/375-hero-my26-sorento-ice.jpg',
            },
            
            # Luxury Vehicles
            {
                'name': 'Model 3',
                'brand': 'Tesla',
                'price': 45000,
                'purpose': 'luxury',
                'car_type': 'sedan',
                'description': 'Electric luxury sedan with autopilot and cutting-edge technology.',
                'features': 'Autopilot, Electric, Premium Interior, Over-the-air Updates, Glass Roof',
                'image_Url': 'https://digitalassets.tesla.com/tesla-contents/image/upload/f_auto,q_auto/Model-3-Main-Hero-Desktop-LHD.jpg',
            },
            {
                'name': 'Model Y',
                'brand': 'Tesla',
                'price': 52000,
                'purpose': 'luxury',
                'car_type': 'suv',
                'description': 'Premium electric SUV with impressive range and performance.',
                'features': 'Dual Motor AWD, Autopilot, 7 Seats, Glass Roof, Supercharging',
                'image_Url': 'https://hips.hearstapps.com/hmg-prod/images/2026-tesla-model-y-long-range-awd-121-688bc237a2711.jpg?crop=0.615xw:0.519xh;0.0865xw,0.365xh&resize=1200:*',
            },
            {
                'name': 'ES 350',
                'brand': 'Lexus',
                'price': 48000,
                'purpose': 'luxury',
                'car_type': 'sedan',
                'description': 'Refined luxury sedan with exceptional comfort and reliability.',
                'features': 'Premium Leather, Mark Levinson Audio, Heated/Cooled Seats, Panoramic Roof',
                'image_Url': 'https://www.lexus.com/content/dam/lexus/images/models/es/2024/visualizer/350/exterior/17-twin-v-spoke-alloy-dark-metallic-machined-finish/eminent-white-pearl/small-1.jpg',
            },
            
            # Sport/Performance
            {
                'name': 'Mustang',
                'brand': 'Ford',
                'price': 38000,
                'purpose': 'sport',
                'car_type': 'coupe',
                'description': 'Iconic American muscle car with powerful engine options and thrilling performance.',
                'features': 'V8 Engine, Sport Suspension, Performance Brakes, Launch Control',
                'image_Url': 'https://images.unsplash.com/photo-1547744152-14d985cb937f?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Zm9yZCUyMG11c3Rhbmd8ZW58MHx8MHx8fDA%3D',
            },
            {
                'name': 'Supra',
                'brand': 'Toyota',
                'price': 55000,
                'purpose': 'sport',
                'car_type': 'coupe',
                'description': 'Legendary sports car with turbocharged power and sharp handling.',
                'features': 'Turbo Inline-6, Adaptive Suspension, Sport Seats, Track Mode',
                'image_Url': 'https://images.unsplash.com/photo-1607603751094-39cc34097d3a?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8dG95b3RhJTIwc3VwcmF8ZW58MHx8MHx8fDA%3D',
            },
            {
                'name': 'Challenger',
                'brand': 'Dodge',
                'price': 40000,
                'purpose': 'sport',
                'car_type': 'coupe',
                'description': 'Bold muscle car with retro styling and powerful engine lineup.',
                'features': 'HEMI V8, Launch Assist, Performance Pages, Racing Seats',
                'image_Url': 'https://images.unsplash.com/photo-1609386462833-6b0d46b2fce0?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8RG9kZ2UlMjBDaGFsbGVuZ2VyfGVufDB8fDB8fHww',
            },
            {
                'name': 'Civic Type R',
                'brand': 'Honda',
                'price': 44000,
                'purpose': 'sport',
                'car_type': 'hatchback',
                'description': 'High-performance hot hatch with track-ready capabilities.',
                'features': 'Turbo Engine, Brembo Brakes, Sport Seats, Rev Match, Track Mode',
                'image_Url': 'https://www.topgear.com/sites/default/files/2022/07/01%202023%20Honda%20Civic%20Type%20R.jpg',
            },
            
            # Off-Road/Adventure
            {
                'name': 'Wrangler',
                'brand': 'Jeep',
                'price': 35000,
                'purpose': 'offroad',
                'car_type': 'suv',
                'description': 'Legendary off-road SUV with removable top and unmatched capability.',
                'features': '4x4, Removable Doors, Off-Road Tires, Winch Ready, Skid Plates',
                'image_Url': 'https://images.unsplash.com/photo-1506015391300-4802dc74de2e?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8SmVlcCUyMFdyYW5nbGVyfGVufDB8fDB8fHww',
            },
            {
                'name': '4Runner',
                'brand': 'Toyota',
                'price': 43000,
                'purpose': 'offroad',
                'car_type': 'suv',
                'description': 'Rugged SUV built for serious off-road adventures.',
                'features': 'Body-on-Frame, Crawl Control, Multi-Terrain Select, Roof Rack',
                'image_Url': 'https://images.unsplash.com/photo-1715667102616-fe4e401b0042?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8N3x8VG95b3RhJTIwNFJ1bm5lcnxlbnwwfHwwfHx8MA%3D%3D',
            },
            {
                'name': 'Bronco',
                'brand': 'Ford',
                'price': 40000,
                'purpose': 'offroad',
                'car_type': 'suv',
                'description': 'Modern off-roader with retro styling and serious trail capability.',
                'features': 'Removable Top, GOAT Modes, Trail Sights, Bash Plates',
                'image_Url': 'https://images.unsplash.com/photo-1637278645626-c3ce5a59b4dd?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8Rm9yZCUyMEJyb25jb3xlbnwwfHwwfHx8MA%3D%3D',
            },
            {
                'name': 'Tacoma',
                'brand': 'Toyota',
                'price': 38000,
                'purpose': 'offroad',
                'car_type': 'truck',
                'description': 'Legendary midsize truck with outstanding off-road credentials.',
                'features': 'TRD Off-Road, Crawl Control, Locking Differential, Bed Utility',
                'image_Url': 'https://images.unsplash.com/photo-1600718042170-36ac0c42e203?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8VG95b3RhJTIwdGFjb21hfGVufDB8fDB8fHww',
            },
        ]

        for car_data in cars:
            Car.objects.create(**car_data)
            self.stdout.write(self.style.SUCCESS(f'Created: {car_data["brand"]} {car_data["name"]}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully seeded {len(cars)} cars!'))