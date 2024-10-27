# Made-With-Love 🪷

***

## 🤝 Contributers

Ananya Shetty, Kamya Rajesh, Saloni Agshiker, Leela Raj-Sankar

***

## 🚀 Inspiration

As college students who are navigating life away from home, we often find ourselves longing for the comfort of home-cooked meals that resonate with our cultural roots. We want to try our own hand at cooking and recreate the recipes that we grew up with, but we don’t always know what to make. That’s why we created **Made with Love** - an app that makes finding home-inspired meals as simple as snapping a photo. We hope to inspire our peers to try their own hand at cooking and embrace their cultural heritage. 

***

## 🎯 What it Does

When the user enters our web app, they first see an interesting Indian dish to try making. They can also receive a more personalized recommendation for a dish to make based on the ingredients they already have at home and their diet preferences. They can do this by taking a picture of their ingredients on the app. The app will analyze the picture and determine what ingredients the user has already. The user is then able to specify whether they would like to receive vegetarian or non-vegetarian items, and whether they would like a recipe for a main course, starter, snack, or dessert. The user receives Indian food options, as per their specifications, 3 at a time, starting with meals that contain the fewest number of extra ingredients on top of what the user already has. 

***

## 🛠 How we Built it

Our entire application is built using Python, ensuring consistent performance and integration. For our back-end, we leveraged **Ultralytics YOLOv8**, a state-of-the-art model for object detection and classification. We trained the model using a Roboflow dataset that had over 4000 annotated images of cooking ingredients. Our model achieved a mean average precision of 53%. This score is largely due to the model easily recognizing some ingredients, like beetroot or broccoli, while other ingredients, like salt, remain a mystery for it. We then formed the basis for our cooking recommendations using a dataset of 255 Indian recipes from Kaggle. Finally, to create a user-friendly web app, we incorporated Streamlit, an open-source Python library.

***

## 🧗‍♂️ Challenges we Faced

During development, we ran into challenges regarding computing power limitations, which caused our model to train very slowly, especially since we aimed to train our model on about 4000 images for 20 epochs while working in Google Colab. Additionally, our recommendation algorithm was logically complicated to implement, as we wanted to provide users with meals requiring the fewest number of additional ingredients that the user would have to obtain while still ensuring that at least one of the ingredients the user had matched those in the recipe.

***

## 🎉 Accomplishments we're Proud of

Entering this project, we did not have much experience in image processing or artificial intelligence, so we are proud that we were able to create a successful AI project. We are also proud that we were able to join together the pieces of our project, from the model to the recommendation algorithm to the user interface.

***

## 📚 What we Learned

We learned how to train a YOLOv8 model, use Streamlit, and parse through large datasets and CSV files to extract information we needed. We also learned how to construct a UI and connect it to a backend of some sort. In a sense, for all of us, we created our first full-stack application, and that is an amazing thing.

***

## 🔮 What's Next for Made with Love

We would like to build on Made with Love by improving the model’s ability to detect and correctly classify ingredients. To do this, we could train the model with more epochs. In order to do this, we may have to use a different environment than Google Colab as well as access to higher computing power, possibly through Georgia Tech’s computing clusters. We would also like to actually provide the user with full recipes rather than just the ingredients needed for a specific dish. We also want to enhance the user interface by creating flippable recipe cards that would have a recipe on one side and additional information on the other side, as well as a feature that allows the user to have their own account on the app so they could save their favorite meals to repeat.

***

## 📽 Demo
Check out our demo video [here](https://www.youtube.com/watch?v=JQbAtLq_ZXw).
