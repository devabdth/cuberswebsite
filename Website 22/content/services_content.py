from enum import Enum


class ServicesContent(Enum):
    SMM = {
        'title': "Social Media Marketing",
        'paragraph': """We believe that without a powerful Social Media Identity, No one has even a chance to get the customers he’s looking forward, So, we use:


    • Up-to-Date Graphic software to design trendy social media designs.

    • Case Studies and Competitors Researches to create catchy content that motivates your targeted customers to buy your services.

    • Freshly updated reports to maintain the campaigns and improve their performance continuously.

After using all of the mentioned components we use them all combined to create the most successful marketing strategies and marketing campaigns that can be created.""",
        'image': "smm.jpg",
        'technologies': [
            {
                'title': "Photoshop",
                'icon': "entry.jpg",
            }
        ],
    }
    WEB_DEV = {
        'title': "Web Development",
        'paragraph': """Not only the appearance nor the UI are the main powerful points for the website. We believe the main power points is the combination of:


    • Trendy UI followed up with UX Researches

    • The most up-to-date technologies that serve all of the Admins to add, edit, and delete components, Stuff to do their tasks, and customers to get the best usage experience.

    • SEO Optimization and the studied pecking of the keywords that make the website trendy and relevant to the market.


In our Web Development Department we offer all of that combined to create trendy designed website with easy usage experience and high relevancy.""",
        'image': "web.jpg",
        'technologies': [
            {
                'title': "Photoshop",
                'icon': "entry.jpg",
            }
        ],
    }
    APP_DEV = {
        'title': "Mobile Development",
        'paragraph': """We - Cubers IO - believe that the shortest way to have a strong connection with your customers is through their mobile phones, So we create applications with multiple streams to give you the ability to continuously notify your products and unmissable offers. Besides the mentioned we create our applications depending on the most up-to-date UI/UX Trends and performance principles. We only aim - through the applications - to create a strong win-win relationship as you notify your customers with fresh products and unmissable offers and your users to get it in a short time in the easiest of ways.""",
        'image': "app.jpg",
        'technologies': [
            {
                'title': "Photoshop",
                'icon': "entry.jpg",
            }
        ],
    }
    DESKTOP_DEV = {
        'title': "Desktop Development",
        'paragraph': """If the staff can’t control the platform how can we trust that the users can be familiar with it, So in our Desktop Development Department we aim to create Desktop Applications that give the best and easiest moderation experience. We create such powerful Desktop Applications by:


• Implement built-in AI models and a powerful group of Algorithms that give a strong hand in moderation.

• Implement a reports model that automatically exports reports that help in business development, vertically, and horizontally scaling.""",
        'image': "desktop.jpg",
        'technologies': [
            {
                'title': "Photoshop",
                'icon': "entry.jpg",
            }
        ],
    }
    MED_PROD = {
        'title': "Media Production",
        'paragraph': """The visual experience of your business has a big part of your success. Creating a visual content for your business must be with the suitable equipment and the catchy content presented by trendy faces.""",
        'image': "med.jpg",
        'technologies': [
            {
                'title': "Photoshop",
                'icon': "entry.jpg",
            }
        ],
    }
    BUS_DEV = {
        'title': "Business Development",
        'paragraph': """No progress can even be hoped without powerful studies, detailed reports or clear targets, So in our Business Development Department we focus our efforts in:


• Declare the targets and points that need to be accessed.

• Study the market, declare the competitors, and competitors, and create a map with advantages we can take on them, and the advantages they can take on us.


Based of the pervious approaches we create well-studied Models (EX.: Business Model, Lean Canvas Model,. …etc) and plans (EX.: Growth Plan, …etc) to turn the models to real life project.""",
        'image': "bus.jpg",
        'technologies': [
            {
                'title': "Photoshop",
                'icon': "entry.jpg",
            }
        ],
    }

    ALL = [
        SMM, WEB_DEV, APP_DEV, DESKTOP_DEV, MED_PROD, BUS_DEV
    ]
