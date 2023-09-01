#!/usr/bin/env python3
"""
A script for populating the database with sample data.

This script creates users, events, and groups in a Django database with sample data.
Users are created first, followed by events and groups with associated images.

Assumptions:
- Django settings are properly configured.
- The script is executed within the root directory of a Django project (The folder with `manage.py`). 
- A virtual environment is activated with Django installed.
- The 'User', 'Event', and 'Group' models are defined in Django.
- To create distinct images for every event and group, you will need to have a folder with images named \
    'event_images' and 'group_images' in the same directory as this script. The images should be named \
    in the format 'event_1.jpg', 'event_2.jpg', etc. and 'group_1.jpg', 'group_2.jpg', etc.
- The images for events and groups are of `.jpg` format.

Note: You can find sample images hosted here: https://drive.google.com/drive/folders/1e7oFwf6U5u1plsp12ZuGyTBxGwjVqaV3?usp=sharing

Usage:
1. Ensure the virtual environment is activated.
2. Run the script using the Python interpreter.

Example:
    $ python populate_db.py

The script will create users with default passwords and random locations, as well as events and groups with associated images.
"""

import os
import random
import django
from datetime import datetime, timedelta
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()


from django.contrib.auth import get_user_model
from events.models import Event
from groups.models import Group

User = get_user_model()


users = [
    {
        "email": "dgrzegorzewski0@seesaa.net",
        "username": "dgrzegorzewski0",
        "first_name": "Dannye",
        "last_name": "Grzegorzewski",
    },
    {
        "email": "dherculson1@facebook.com",
        "username": "dherculson1",
        "first_name": "Donni",
        "last_name": "Herculson",
    },
    {
        "email": "hpapa2@oakley.com",
        "username": "hpapa2",
        "first_name": "Haven",
        "last_name": "Papa",
    },
    {
        "email": "jolver3@adobe.com",
        "username": "jolver3",
        "first_name": "Jorry",
        "last_name": "Olver",
    },
    {
        "email": "asutherland4@imdb.com",
        "username": "asutherland4",
        "first_name": "Alberik",
        "last_name": "Sutherland",
    },
    {
        "email": "aclaridge5@goo.gl",
        "username": "aclaridge5",
        "first_name": "Aloysia",
        "last_name": "Claridge",
    },
    {
        "email": "jtatnell6@amazon.co.jp",
        "username": "jtatnell6",
        "first_name": "Jsandye",
        "last_name": "Tatnell",
    },
    {
        "email": "fpaish7@naver.com",
        "username": "fpaish7",
        "first_name": "Fraser",
        "last_name": "Paish",
    },
    {
        "email": "cbutcher8@friendfeed.com",
        "username": "cbutcher8",
        "first_name": "Constanta",
        "last_name": "Butcher",
    },
    {
        "email": "ksmedmore9@mapy.cz",
        "username": "ksmedmore9",
        "first_name": "Kettie",
        "last_name": "Smedmore",
    },
    {
        "email": "estatea@reverbnation.com",
        "username": "estatea",
        "first_name": "Elisha",
        "last_name": "State",
    },
    {
        "email": "acurreyb@google.com.br",
        "username": "acurreyb",
        "first_name": "Audrye",
        "last_name": "Currey",
    },
    {
        "email": "jcuberleyc@nhs.uk",
        "username": "jcuberleyc",
        "first_name": "Joy",
        "last_name": "Cuberley",
    },
    {
        "email": "gcoopmand@google.co.jp",
        "username": "gcoopmand",
        "first_name": "Goldina",
        "last_name": "Coopman",
    },
    {
        "email": "wcovolinie@naver.com",
        "username": "wcovolinie",
        "first_name": "Whitman",
        "last_name": "Covolini",
    },
    {
        "email": "pcracknallf@howstuffworks.com",
        "username": "pcracknallf",
        "first_name": "Pierrette",
        "last_name": "Cracknall",
    },
    {
        "email": "zloughmang@prnewswire.com",
        "username": "zloughmang",
        "first_name": "Zebadiah",
        "last_name": "Loughman",
    },
    {
        "email": "wbrookwellh@cargocollective.com",
        "username": "wbrookwellh",
        "first_name": "Whitby",
        "last_name": "Brookwell",
    },
    {
        "email": "aforcei@nsw.gov.au",
        "username": "aforcei",
        "first_name": "Arturo",
        "last_name": "Force",
    },
    {
        "email": "pliveleyj@google.nl",
        "username": "pliveleyj",
        "first_name": "Petey",
        "last_name": "Liveley",
    },
    {
        "email": "wlangworthyk@list-manage.com",
        "username": "wlangworthyk",
        "first_name": "Wolfgang",
        "last_name": "Langworthy",
    },
    {
        "email": "ljaherl@alexa.com",
        "username": "ljaherl",
        "first_name": "Lise",
        "last_name": "Jaher",
    },
    {
        "email": "cchestonm@goodreads.com",
        "username": "cchestonm",
        "first_name": "Cristian",
        "last_name": "Cheston",
    },
    {
        "email": "lparkhousen@wikia.com",
        "username": "lparkhousen",
        "first_name": "Libbi",
        "last_name": "Parkhouse",
    },
    {
        "email": "tfonsoo@bigcartel.com",
        "username": "tfonsoo",
        "first_name": "Tudor",
        "last_name": "Fonso",
    },
    {
        "email": "aeasterfieldp@vkontakte.ru",
        "username": "aeasterfieldp",
        "first_name": "Abelard",
        "last_name": "Easterfield",
    },
    {
        "email": "fkleinq@pen.io",
        "username": "fkleinq",
        "first_name": "Fayette",
        "last_name": "Klein",
    },
    {
        "email": "egiacobazzir@bbb.org",
        "username": "egiacobazzir",
        "first_name": "Erina",
        "last_name": "Giacobazzi",
    },
    {
        "email": "tmailess@baidu.com",
        "username": "tmailess",
        "first_name": "Terrie",
        "last_name": "Mailes",
    },
    {
        "email": "slarkkemt@barnesandnoble.com",
        "username": "slarkkemt",
        "first_name": "Sanford",
        "last_name": "Larkkem",
    },
]

user_locations = [
    "Nairobi",
    "Kampala",
    "Dar es Salaam",
    "Kigali",
    "Addis Ababa",
    "Mombasa",
    "Kisumu",
    "Arusha",
    "Mwanza",
    "Entebbe",
    "Zanzibar City",
    "Nakuru",
    "Moshi",
    "Bujumbura",
    "Jinja",
    "Lusaka",
    "Maputo",
    "Harare",
    "Nampula",
    "Malindi",
    "Eldoret",
    "Meru",
    "Lamu",
    "Kakamega",
    "Bungoma",
    "Morogoro",
    "Mbale",
    "Dodoma",
    "Mbarara",
    "Homa Bay",
    "Blantyre",
    "Lilongwe",
    "Moroni",
    "Mombasa",
    "Kapsabet",
    "Kericho",
    "Kabale",
    "Bahir Dar",
    "Makindu",
    "Kabarnet",
    "Karatina",
    "Kitale",
    "Kisii",
    "Nyeri",
    "Mityana",
    "Mukono",
    "Bulawayo",
    "Victoria Falls",
    "Naivasha",
    "Musoma",
    "Tabora",
    "Juba",
    "Mogadishu",
]

hiking_events = [
    {
        "name": "Summit Quest: Mt. Kenya Expedition",
        "description": "<p>Join us on an epic adventure to conquer the majestic peaks of Mount Kenya, Africa's second-highest mountain. Our 'Summit Quest: Mt. Kenya Expedition' promises an unforgettable journey filled with breathtaking vistas, thrilling challenges, and a deep connection to nature.</p><p>As the sun rises over the rugged terrain, you'll begin your ascent through diverse ecosystems, including lush rainforests, alpine moorlands, and the otherworldly high-altitude desert. Along the way, our experienced guides will share their knowledge of the mountain's flora and fauna, making this not just a physical feat but also an educational journey.</p><p>This is an advanced-level hike designed for experienced trekkers looking to test their limits. You'll be rewarded with panoramic views from Point Lenana, a true testament to your determination and spirit.</p><p>Don't miss the chance to be part of the 'Summit Quest: Mt. Kenya Expedition' and experience the thrill of conquering the heights while forging lasting memories with fellow adventurers. Join us and embark on a transformative journey of self-discovery and exploration.</p>",
        "location": "Mt. Kenya",
        "difficulty": "advanced",
    },
    {
        "name": "Ngong Hills Adventure: Summit Pursuit",
        "description": "<p>Embark on an exhilarating expedition to conquer the iconic Ngong Hills, a natural wonder that has captivated adventurers for generations. Our 'Ngong Hills Adventure: Summit Pursuit' promises an extraordinary journey filled with stunning landscapes, thrilling challenges, and an opportunity to reconnect with the great outdoors.</p><p>As you ascend the rolling slopes of Ngong Hills, you'll be treated to panoramic views of the Rift Valley and Nairobi skyline, creating a visual masterpiece that's nothing short of awe-inspiring. This advanced-level hike will take you through diverse terrain, from open grasslands to dense eucalyptus forests.</p><p>Our experienced guides will lead the way, sharing their expertise on the local flora, fauna, and the rich history of this remarkable region. This isn't just a hike; it's a holistic adventure that promises to challenge and rejuvenate your spirit.</p><p>Join us for the 'Ngong Hills Adventure: Summit Pursuit' and experience the thrill of conquering the peaks while forging lasting memories with fellow adventurers. Don't miss this opportunity to embrace the natural beauty of Ngong Hills and leave with a sense of accomplishment that will stay with you forever.</p>",
        "location": "Ngong Hills",
        "difficulty": "advanced",
    },
    {
        "name": "Longonot Summit Challenge",
        "description": "<p>Embark on the ultimate adventure with our 'Longonot Summit Challenge' and conquer the towering heights of Mt. Longonot, a dormant volcano that offers breathtaking views and thrilling trails.</p><p>As the sun begins its ascent, you'll set off on a journey through diverse landscapes, from dense forests to rocky slopes. Along the way, you'll witness the transformation of the terrain and gain a deeper appreciation for the natural world.</p><p>This intermediate-level hike is perfect for both seasoned hikers and those looking to test their limits. Our experienced guides will lead you safely, sharing their knowledge of the volcano's history and the unique flora and fauna that call it home.</p><p>Join us for the 'Longonot Summit Challenge' and experience the thrill of reaching the summit while forging lasting memories. Don't miss this opportunity to embrace the adventure and explore the wonders of Mt. Longonot.</p>",
        "location": "Mt. Longonot",
        "difficulty": "intermediate",
    },
    {
        "name": "Karura Forest Trek: Nature's Paradise",
        "description": "<p>Join us for a rejuvenating trek through the lush greenery of Karura Forest, Nairobi's hidden gem. Our 'Karura Forest Trek: Nature's Paradise' promises a day of exploration, relaxation, and a deep connection with the natural world.</p><p>As you step into the forest, you'll be greeted by a tranquil oasis of towering trees, winding trails, and the soothing sounds of flowing streams. This beginner-friendly trek is perfect for nature enthusiasts of all levels.</p><p>Our knowledgeable guides will lead you through the forest's secrets, sharing stories of its rich history and the incredible biodiversity that thrives here. Along the way, you'll discover hidden waterfalls, peaceful glades, and a sense of peace that only nature can provide.</p><p>Don't miss the chance to experience the 'Karura Forest Trek: Nature's Paradise' and immerse yourself in the beauty of this urban sanctuary. It's a day to escape the hustle and bustle, connect with nature, and create memories that will last a lifetime.</p>",
        "location": "Karura Forest",
        "difficulty": "beginner",
    },
    {
        "name": "Ruwenzori Expedition: Conquer the 'Mountains of the Moon'",
        "description": "<p>Embark on an extraordinary journey to conquer the majestic peaks of the Ruwenzori Mountain Range, often referred to as the 'Mountains of the Moon.' Our 'Ruwenzori Expedition' promises an unforgettable adventure filled with stunning vistas, challenging terrain, and a deep connection with these mystical mountains.</p><p>As the first light of dawn paints the rugged landscape, you'll set out to explore this UNESCO World Heritage site, home to the third-highest peaks in Africa. Our trek will take you through diverse ecosystems, from equatorial rainforests to the surreal glacial zones, providing a unique opportunity to witness nature's grandeur.</p><p>This is an advanced-level expedition, designed for seasoned hikers and adventurers seeking the ultimate challenge. Our expert guides will lead you safely through the ever-changing terrain, sharing their knowledge of the mountain's geological wonders and the rare flora and fauna that thrive here.</p><p>Join us for the 'Ruwenzori Expedition' and experience the thrill of conquering the 'Mountains of the Moon' while creating memories that will last a lifetime. Don't miss this chance to explore the untouched beauty of the Ruwenzori Mountain Range.</p>",
        "location": "Ruwenzori Mountain Range",
        "difficulty": "advanced",
    },
    {
        "name": "Aberdare Odyssey: Discovering the Rugged Beauty",
        "description": "<p>Embark on a captivating journey to explore the rugged beauty of the Aberdare Ranges, a hidden gem in Kenya's natural landscape. Our 'Aberdare Odyssey' promises an unforgettable adventure filled with pristine wilderness, striking vistas, and a deep connection with the great outdoors.</p><p>As you venture into the heart of the Aberdare Ranges, you'll encounter diverse ecosystems, from lush bamboo forests to high moorlands. The Aberdare National Park is renowned for its unique flora and fauna, and our experienced guides will unveil the mysteries of this enchanting terrain.</p><p>This intermediate-level hike is suitable for both seasoned adventurers and those looking to explore the wonders of the Aberdare Ranges for the first time. Our guides will lead you through the trails, sharing their knowledge of the region's rich history and ecological significance.</p><p>Join us for the 'Aberdare Odyssey' and immerse yourself in the untamed beauty of this pristine wilderness. Don't miss the opportunity to create lasting memories while discovering the secrets of the Aberdare Ranges.</p>",
        "location": "Aberdare Ranges",
        "difficulty": "intermediate",
    },
    {
        "name": "Lengai Ascent: Scaling the Sacred 'Mountain of God'",
        "description": "<p>Embark on a sacred journey to conquer the towering heights of Ol Doinyo Lengai, often referred to as the 'Mountain of God.' Our 'Lengai Ascent' promises a spiritual and physical adventure filled with dramatic landscapes, unique challenges, and a profound connection with this sacred volcano.</p><p>As the first light paints the African sky, you'll commence your ascent up the slopes of Ol Doinyo Lengai. This is not just a hike; it's a pilgrimage to a place of cultural and geological significance.</p><p>The path will take you through lunar-like landscapes of ash and rock, showcasing the stark beauty of this unique volcano. Our experienced guides will lead you safely, sharing their knowledge of the Maasai culture and the spiritual importance of this mountain.</p><p>This is an advanced-level hike, designed for adventurers looking to experience the extraordinary. Reaching the summit is a testament to your determination and respect for the sacred land.</p><p>Join us for the 'Lengai Ascent' and immerse yourself in a spiritual and physical journey that will forever hold a special place in your heart. Don't miss this opportunity to connect with the 'Mountain of God' and experience its awe-inspiring presence.</p>",
        "location": "Ol Doinyo Lengai",
        "difficulty": "advanced",
    },
    {
        "name": "Kilimanjaro Summit Challenge: Conquer Africa's Roof",
        "description": "<p>Embark on an awe-inspiring journey to conquer the roof of Africa with our 'Kilimanjaro Summit Challenge.' This expedition promises a life-changing adventure filled with stunning vistas, exhilarating challenges, and an unforgettable connection with one of the world's most iconic mountains.</p><p>As the sun paints the African horizon, you'll begin your ascent through diverse ecosystems, including lush rainforests, alpine moorlands, and the otherworldly high-altitude desert. Mt. Kilimanjaro's Uhuru Peak awaits as your ultimate goal, offering unparalleled panoramic views.</p><p>This is an advanced-level hike for adventurers seeking the pinnacle of trekking experiences. Our seasoned guides will lead you safely through the changing terrain, sharing their insights into the mountain's geological marvels and the unique flora and fauna that thrive here.</p><p>Join us for the 'Kilimanjaro Summit Challenge' and stand on the highest point in Africa, a symbol of determination and achievement. Don't miss this opportunity to immerse yourself in the beauty and challenge of Mt. Kilimanjaro while forging lifelong memories with fellow adventurers.</p>",
        "location": "Mt Kilimanjaro",
        "difficulty": "advanced",
    },
    {
        "name": "Arboretum Adventure: Exploring Nairobi's Green Oasis",
        "description": "<p>Embark on a delightful adventure to explore the natural beauty of Nairobi Arboretum, the city's green oasis. Our 'Arboretum Adventure' promises a day filled with lush landscapes, serene trails, and a deep connection with nature.</p><p>As you step into this urban sanctuary, you'll be greeted by a tapestry of trees, colorful flora, and a chorus of bird songs. This beginner-friendly hike is perfect for nature enthusiasts of all ages.</p><p>Our knowledgeable guides will lead you through the arboretum's secrets, sharing stories of the diverse plant species and the wildlife that call it home. Along the way, you'll discover hidden corners, tranquil ponds, and a sense of peace that only nature can provide.</p><p>Don't miss the chance to experience the 'Arboretum Adventure' and immerse yourself in the beauty of this green gem in Nairobi. It's a day to escape the hustle and bustle, connect with nature, and create memories that will last a lifetime.</p>",
        "location": "Nairobi Arboretum",
        "difficulty": "beginner",
    },
    {
        "name": "Karisimbi Summit Challenge: Conquer Rwanda's Highest Peak",
        "description": "<p>Embark on a thrilling adventure to conquer the summit of Mt. Karisimbi, Rwanda's highest peak. Our 'Karisimbi Summit Challenge' promises an unforgettable journey filled with dramatic landscapes, high-altitude challenges, and a deep connection with the heart of Africa.</p><p>As the sun bathes the rugged terrain in golden light, you'll set out on a remarkable expedition through lush bamboo forests and alpine meadows. This advanced-level hike will test your endurance and reward you with panoramic views of Rwanda and the neighboring Virunga Mountains.</p><p>Our experienced guides will lead the way, sharing their knowledge of the region's unique flora, fauna, and geological wonders. You'll not only conquer the summit but also gain insights into the natural and cultural heritage of this remarkable region.</p><p>Join us for the 'Karisimbi Summit Challenge' and experience the thrill of reaching the highest point in Rwanda. Don't miss this opportunity to push your limits, connect with fellow adventurers, and create memories that will last a lifetime.</p>",
        "location": "Mt. Karisimbi",
        "difficulty": "advanced",
    },
    {
        "name": "Chyulu Hills Odyssey: Exploring the Enchanted Land",
        "description": "<p>Embark on a mesmerizing journey to explore the enchanting landscapes of Chyulu Hills, a hidden gem in Kenya's wilderness. Our 'Chyulu Hills Odyssey' promises an unforgettable adventure filled with dramatic vistas, unique volcanic terrain, and a profound connection with nature.</p><p>As you venture into the heart of the Chyulu Hills, you'll encounter a surreal world of ancient lava flows, dense forests, and rolling green hills. This intermediate-level hike offers a chance to traverse the diverse terrain, all while immersing yourself in the tranquility of this untouched wilderness.</p><p>Our experienced guides will lead you through this enchanting landscape, sharing their knowledge of the region's geological wonders and the rich biodiversity that thrives here. This is not just a hike; it's a holistic adventure that promises to awaken your sense of wonder and appreciation for nature.</p><p>Join us for the 'Chyulu Hills Odyssey' and immerse yourself in the beauty of this pristine wilderness. Don't miss the opportunity to create lasting memories while exploring the secrets of Chyulu Hills.</p>",
        "location": "Chyulu Hills",
        "difficulty": "intermediate",
    },
    {
        "name": "Usambara Mountain Quest: Exploring the Green Highlands",
        "description": "<p>Join us on a remarkable journey to explore the lush green highlands of the Usambara Mountains, a hidden treasure in Tanzania's landscape. Our 'Usambara Mountain Quest' promises an extraordinary adventure filled with verdant landscapes, cultural discoveries, and a deep connection with the vibrant local communities.</p><p>As you ascend through the picturesque foothills, you'll be greeted by the breathtaking beauty of the Usambara Mountains. These richly biodiverse mountains are home to unique flora and fauna, and our experienced guides will unveil the secrets of this remarkable ecosystem.</p><p>This intermediate-level hike is suitable for adventurers of all backgrounds, and our guides will lead you through the trails, sharing their knowledge of the region's rich history and the traditions of the local communities.</p><p>Join us for the 'Usambara Mountain Quest' and immerse yourself in the pristine beauty of this vibrant region. Don't miss the opportunity to create lasting memories while discovering the natural and cultural wonders of the Usambara Mountains.</p>",
        "location": "Usambara Mountains",
        "difficulty": "intermediate",
    },
    {
        "name": "Elgon Summit Trek: Exploring the Roof of East Africa",
        "description": "<p>Join us on a remarkable journey to conquer the lofty heights of Mt. Elgon, East Africa's hidden gem. Our 'Elgon Summit Trek' promises an unforgettable adventure filled with stunning landscapes, diverse ecosystems, and a deep connection with this natural wonder.</p><p>As you ascend the slopes of Mt. Elgon, you'll traverse through enchanting landscapes, from lush montane forests to dramatic calderas. This intermediate-level hike offers a chance to witness the unique flora and fauna of this unspoiled wilderness.</p><p>Our knowledgeable guides will lead the way, sharing insights into the geological wonders of Mt. Elgon and the rich history of the local communities. This is not just a hike; it's an immersive experience that offers both adventure and education.</p><p>Join us for the 'Elgon Summit Trek' and embrace the opportunity to summit Wagagai, the highest peak. Capture breathtaking views and create lasting memories with fellow adventurers in this pristine natural environment.</p><p>Don't miss the chance to explore the Roof of East Africa and embark on a transformative journey of discovery. Join us for the 'Elgon Summit Trek' and experience the grandeur of Mt. Elgon.</p>",
        "location": "Mt. Elgon",
        "difficulty": "intermediate",
    },
    {
        "name": "Simien Summit Trek: Exploring Ethiopia's Roof of Africa",
        "description": "<p>Embark on a breathtaking journey to conquer the majestic peaks of the Simien Mountains, often referred to as the 'Roof of Africa' in Ethiopia. Our 'Simien Summit Trek' promises an unforgettable adventure filled with dramatic landscapes, unique wildlife, and a deep connection with this UNESCO World Heritage site.</p><p>As you ascend the rugged slopes of the Simien Mountains, you'll encounter diverse ecosystems, including dramatic escarpments and deep valleys. This advanced-level hike offers a chance to witness the charismatic Ethiopian wolf and the walia ibex, both unique to this region.</p><p>Our expert guides will lead you through this natural wonderland, sharing their knowledge of the local flora, fauna, and the geological history of the Simien Mountains. This is not just a hike; it's an expedition that offers both adventure and ecological education.</p><p>Join us for the 'Simien Summit Trek' and experience the thrill of conquering Ras Dashen, Ethiopia's highest peak. Marvel at the stunning vistas and immerse yourself in the culture of the local communities along the way.</p><p>Don't miss the opportunity to explore the 'Roof of Africa' and create lasting memories in the Simien Mountains. Join us for the 'Simien Summit Trek' and embrace the adventure of a lifetime.</p>",
        "location": "Simien Mountains, Ethiopia",
        "difficulty": "advanced",
    },
]

hiking_groups = [
    {
        "name": "Nairobi Adventurers",
        "location": "Nairobi, Kenya",
        "description": "<p>Join the Nairobi Adventurers, a vibrant community of nature enthusiasts, for thrilling hiking expeditions in the stunning landscapes around Nairobi. Our group is dedicated to exploring the natural wonders of Kenya, from the lush forests of Karura to the rugged terrain of Ngong Hills. Whether you're a beginner or an experienced trekker, our group offers a welcoming environment to connect with fellow adventurers and experience the beauty of East Africa.</p><p>Our experienced guides lead safe and exciting hikes that cater to all levels of hikers. Discover hidden waterfalls, learn about local flora and fauna, and forge lasting friendships with like-minded individuals. Join the Nairobi Adventurers and embark on unforgettable journeys through the breathtaking landscapes of Kenya.</p>",
    },
    {
        "name": "Kilimanjaro Explorers",
        "location": "Arusha, Tanzania",
        "description": "<p>Embark on epic treks to the legendary Kilimanjaro with the Kilimanjaro Explorers, based in Arusha, Tanzania. Our group specializes in conquering Africa's highest peak and offers a range of routes to suit your preferences and experience level. Whether you dream of reaching Uhuru Peak or prefer a more leisurely climb, we've got you covered.</p><p>Our certified guides are experts in Kilimanjaro's terrain, ensuring your safety and comfort throughout the journey. Join the Kilimanjaro Explorers and make memories scaling this iconic mountain while enjoying breathtaking vistas and camaraderie with fellow adventurers.</p>",
    },
    {
        "name": "Mombasa Coastal Trekkers",
        "location": "Mombasa, Kenya",
        "description": "<p>Discover the coastal beauty of Kenya with the Mombasa Coastal Trekkers, based in Mombasa. Our group specializes in coastal hikes that explore the pristine beaches, lush mangroves, and historic sites along Kenya's Indian Ocean shoreline.</p><p>Whether you're interested in relaxing beach walks or more challenging coastal trails, our group offers a variety of experiences. Join the Mombasa Coastal Trekkers and connect with fellow beach lovers and adventurers as we explore the wonders of the Kenyan coast.</p>",
    },
    {
        "name": "Rwenzori Mountain Explorers",
        "location": "Kampala, Uganda",
        "description": "<p>Join the Rwenzori Mountain Explorers, based in Kampala, for treks through the enchanting Rwenzori Mountain Range in Uganda. Our group is dedicated to uncovering the beauty of these 'Mountains of the Moon,' a UNESCO World Heritage site known for its glaciers and unique ecosystems.</p><p>Explore the diverse flora and fauna, traverse through pristine forests, and summit some of Africa's highest peaks with our experienced guides. The Rwenzori Mountain Explorers offer both adventure and education in this extraordinary natural wonderland.</p>",
    },
    {
        "name": "Kigali Highland Hikers",
        "location": "Kigali, Rwanda",
        "description": "<p>Discover the highlands of Rwanda with the Kigali Highland Hikers, based in Kigali. Our group specializes in hikes through Rwanda's stunning high-altitude landscapes, including the Virunga Mountains and Nyungwe Forest.</p><p>Immerse yourself in the unique biodiversity of Rwanda, home to rare mountain gorillas and golden monkeys. Our experienced guides provide insights into local conservation efforts and lead you on unforgettable adventures in the heart of Africa.</p>",
    },
    {
        "name": "Zanzibar Island Explorers",
        "location": "Zanzibar City, Tanzania",
        "description": "<p>Join the Zanzibar Island Explorers, based in Zanzibar City, for island adventures in the turquoise waters of the Indian Ocean. Our group specializes in coastal walks, snorkeling, and exploring the cultural heritage of the Zanzibar Archipelago.</p><p>Experience the magic of Zanzibar's spice plantations, pristine beaches, and vibrant underwater world. Whether you're interested in underwater exploration or cultural immersion, our group offers a range of experiences for island lovers.</p>",
    },
    {
        "name": "Entebbe Lakeside Wanderers",
        "location": "Entebbe, Uganda",
        "description": "<p>Discover the beauty of Uganda's lakeside landscapes with the Entebbe Lakeside Wanderers, based in Entebbe. Our group specializes in hikes around Lake Victoria, exploring its shores and nearby wetlands.</p><p>As you walk through serene lakeside trails, you'll have the chance to spot diverse birdlife and enjoy tranquil moments by the water. Join the Entebbe Lakeside Wanderers and connect with fellow nature enthusiasts along the picturesque shores of Lake Victoria.</p>",
    },
    {
        "name": "Kisumu Rift Valley Trekkers",
        "location": "Kisumu, Kenya",
        "description": "<p>Explore the scenic wonders of the Great Rift Valley with the Kisumu Rift Valley Trekkers, based in Kisumu, Kenya. Our group specializes in hikes through the Rift Valley's stunning landscapes, including crater lakes, escarpments, and geological marvels.</p><p>Discover the unique geological features of the Rift Valley while enjoying breathtaking vistas. Whether you're a geology enthusiast or simply seeking natural beauty, the Kisumu Rift Valley Trekkers have adventures waiting for you.</p>",
    },
    {
        "name": "Addis Ababa Highland Hikers",
        "location": "Addis Ababa, Ethiopia",
        "description": "<p>Embark on highland adventures in Ethiopia with the Addis Ababa Highland Hikers, based in the capital city, Addis Ababa. Our group specializes in treks through the country's lush highlands, including the Simien Mountains and Bale Mountains.</p><p>Experience Ethiopia's rich cultural heritage, explore its unique landscapes, and witness the abundant wildlife that calls these highlands home. Join the Addis Ababa Highland Hikers and connect with fellow adventurers in the heart of Ethiopia.</p>",
    },
]


for user in users:
    user = User.objects.create_user(
        email=user["email"],
        username=user["username"],
        first_name=user.get("first_name", ""),
        last_name=user.get("last_name", ""),
        location=random.choice(user_locations),
        password="test_password",
    )
print(f"✅Users created successfully.")


users = [user for user in User.objects.all()]

import os
from django.core.files import File

image_folder = "event_images/"
for index, event in enumerate(hiking_events):
    event_obj = Event.objects.create(
        owner=random.choice(users[:5]),
        name=event["name"],
        date=(datetime.now() + timedelta(days=random.randint(7, 90))).strftime(
            "%Y-%m-%d"
        ),
        time=f"{random.randint(5, 10):02d}:00:00",
        location=event["location"],
        difficulty=event.get("difficulty", "beginner"),
    )

    # Assuming you have an 'image' field in your Event model.
    # You'll need to replace 'image' with the actual field name in your model.
    try:
        image_filename = f"event-{index + 1}.jpg"
        image_path = os.path.join(image_folder, image_filename)
        event_obj.image.save(image_filename, File(open(image_path, "rb")))
        event_obj.save()
    except:
        pass

print(f"✅Events created successfully.")


image_folder = "group_images/"
for index, group in enumerate(hiking_groups):
    group_obj = Group.objects.create(
        owner=random.choice(users[5:11]),
        name=group["name"],
        description=group["description"],
        location=group["location"],
    )

    try:
        image_filename = f"group-{index + 1}.jpg"
        image_path = os.path.join(image_folder, image_filename)
        group_obj.image.save(image_filename, File(open(image_path, "rb")))
        group_obj.save()
    except:
        pass

print(f"✅Groups created successfully.")
