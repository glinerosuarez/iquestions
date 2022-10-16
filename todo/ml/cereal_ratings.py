"""
Suppose you have the following dataset(http://url4828.interviewqs.com/ls/click?upn=qwT-2Bl0U064-2B7oRNpPgUya51JFUDgj241ZqJOHGqS8eD4tjNEUUiE84jSUq3UK-2FXXVV6baahMCT1lnWqzVwJy2iqKuEoMjYJainybGEluZqqkr4WP7gBwKEdp-2FABtL1JZYjgcIp376AiZhqs9lOJdoQ-3D-3DceS5_Rnksh8mmH7vi3d5oyhplLP4H0bOosjDG5cWn-2BNVdc5OsSAq1-2F8Xb8hE6ay4samejco0sA0AHGEKJIJon3pKPuqaTXwrirFQyhq0D-2F0BGFmZU4yCFR9PoCghvqDdNtrXBj-2F5MlgQS-2FZdU8EdpcB4kFn3zNDDfUQMzXBUTNBKk-2B4imRaeb-2BKoPLopQ4SmiD-2FWyofnRIsi25-2Bs5N-2BUUpZ7ULejtU9m3E5-2FTfIGI9VMqCOhcrWqZ-2FIvwUnG9mLRt9AO1pK7GeQNh6uLgGSARnxHSGZSnqTYm5WrOJbHNnOXMME5FIVo2OdISaX6SR9717PP0sIZIDy-2Fl1boPSkEA9PpPRcj1cMIHVw1ecGgBITVHleV2hXPj6h3sRM1N4bDa7pa5)
, which is a list of 80 cereals, containing the following fields:

mfr: Manufacturer of cereal
A = American Home Food Products
G = General Mills
K = Kelloggs
N = Nabisco
P = Post
Q = Quaker Oats
R = Ralston Purina
type:
cold
hot
calories: calories per serving
protein: grams of protein per serving
fat: grams of fat per serving
sodium: milligrams of sodium
fiber: grams of dietary fiber
carbs: grams of complex carbohydrates
sugars: grams of sugars
potass: milligrams of potassium
vitamins: vitamins and minerals - 0, 25, or 100, indicating the typical percentage of FDA recommended
shelf: display shelf (1, 2, or 3, counting from the floor)
weight: weight in ounces of one serving
cups: number of cups in one serving
rating: a rating of the cereals (Possibly from Consumer Reports?)
Given the above, can you build a model using Python to predict cereal rating? We'll be creating a multivariate linear regression as a solution for premium users.

*Dataset source
http://url4828.interviewqs.com/ls/click?upn=qwT-2Bl0U064-2B7oRNpPgUya5rcH74cMnaRHexUxeQp6aYX-2Bcpb96RbfsK-2Btg1gqgroxOHUhvUDoA-2BIBpLNzEFXng-3D-3Dmsyo_Rnksh8mmH7vi3d5oyhplLP4H0bOosjDG5cWn-2BNVdc5OsSAq1-2F8Xb8hE6ay4samejco0sA0AHGEKJIJon3pKPuqaTXwrirFQyhq0D-2F0BGFmZU4yCFR9PoCghvqDdNtrXBj-2F5MlgQS-2FZdU8EdpcB4kFn3zNDDfUQMzXBUTNBKk-2B4imRaeb-2BKoPLopQ4SmiD-2FWyofnRIsi25-2Bs5N-2BUUpZ7ULejtU9m3E5-2FTfIGI9VMqCOjRkR3euTuQxTMckO3q2SwIMz9a1WplKtLOIGXSEDp2tqsfaJKW6mLminGXwH3umRGKCAZnJkHspuD-2F7YL8RB8qCcRKo8sbvrT5KLNuKTfWq6nXoCSOJZOpZLAIkl2mgGVzYXxPt6gwH00Ut-2FNxpREx
Click here to view this problem in an interactive Colab (Jupyter) notebook.
http://url4828.interviewqs.com/ls/click?upn=qwT-2Bl0U064-2B7oRNpPgUya9zum6BicxNNIjKHijyyRWobZaLTayuey7-2FyWP-2FStY6TaWfDDH18s8r13bR3JrS0EOesW5PaObtE-2BSGy4O6O7DINfVBuGqcltRbRIIAGO-2BXiu-2BERPhL-2FE4g9fuPjOlzTAQ-3D-3DIDqD_Rnksh8mmH7vi3d5oyhplLP4H0bOosjDG5cWn-2BNVdc5OsSAq1-2F8Xb8hE6ay4samejco0sA0AHGEKJIJon3pKPuqaTXwrirFQyhq0D-2F0BGFmZU4yCFR9PoCghvqDdNtrXBj-2F5MlgQS-2FZdU8EdpcB4kFn3zNDDfUQMzXBUTNBKk-2B4imRaeb-2BKoPLopQ4SmiD-2FWyofnRIsi25-2Bs5N-2BUUpZ7ULejtU9m3E5-2FTfIGI9VMqCOgFHtaP1ZwaiGZe8irIuQeO-2FJf1TQW5BG-2FJUE7roeUfWdhTOiokLUpjdePx1FaEVWy1-2BBacux5npV5K9ouhc4zyFgpeAqUj67yn3UgISDKygM-2FJ8qcvyIVkKl9MSYzpZyyqdxwJWS-2F-2Byt5-2BuVbGNn1H
"""