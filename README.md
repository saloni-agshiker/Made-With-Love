# Made-With-Love
Team Members: Ananya Shetty, Kamya Rajesh, Saloni Agshiker, Leela Rajsankar

As college students who are navigating life away from home, we often find ourselves longing for the comfort of home-cooked meals that resonate with our cultural roots. We want to try our own 
hand at cooking and recreate the recipes that we grew up with, but we don’t always know what to make. That’s why we created Made with Love - an app that makes finding home-inspired meals as 
simple as snapping a photo. We hope to inspire our peers to try their own hand at cooking and embrace their cultural heritage. 

When the user enters our web app, they first see an interesting Indian dish to try making. They can also receive a more personalized recommendation for a dish to make based on the ingredients 
they already have at home and their diet preferences. They can do this by taking a picture of their ingredients on the app. The app will analyze the picture and determine what ingredients the 
user has already. The user is then able to specify whether they would like to receive vegetarian or non-vegetarian items, and whether they would like a recipe for a main course, starter, snack, 
or dessert. The user receives Indian food options, as per their specifications, 3 at a time, starting with meals that contain the fewest number of extra ingredients on top of what the user 
already has. 

Our entire application is built using Python, ensuring consistent performance and integration. For our back-end, we leveraged Ultralytics YOLOv8, a state-of-the-art model for object detection 
and classification. We trained the model using a Roboflow dataset that had over 4000 annotated images of cooking ingredients. Our model achieved a mean average precision of 53%. This score is 
largely due to the model easily recognizing some ingredients, like beetroot or broccoli, while other ingredients, like salt, remain a mystery for it. We then formed the basis for our cooking 
recommendations using a dataset of 255 Indian recipes from Kaggle. Finally, to create a user-friendly web app, we incorporated Streamlit, an open-source Python library.
