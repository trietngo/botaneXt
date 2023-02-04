import json


def search_plant(data, location: str, purpose: str):
    """
        search plants by location, allergy & purpose
    :param data: plant information in Json format
    :param location: str
    :param allergy: str
    :param purpose: str
    :return: a list of plant name
    """
    selected_plants = []
    plants = list(data.keys())
    for plant in plants:
        plan_info = data[plant].copy()
        if plan_info["Purpose"] == purpose or purpose == "Both":
            if plan_info["Location"] == location:
                selected_plants.append(plant)

    return selected_plants


def get_image_path(plant_names):
    path_pattern = "data/plant_pics/{}.png"
    example_image_fp = [
        path_pattern.format(name.lower()) for name in plant_names
    ]
    return example_image_fp


# if __name__ == '__main__':
#     with open("../data/plant_info/example.json", "r") as f:
#         data = json.load(f)
#     select_plant = search_plant(data, "Miami", "Edible")
#     print(select_plant)