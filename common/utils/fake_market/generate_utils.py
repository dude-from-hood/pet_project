from faker import Faker

# +-------------------
fake = Faker()
# +-------------------

def generate_new_product(
        product_id: int = None,
        title: str = None,
        price: int | float = None,
        description: str = None,
        category: str = None,
        image: str = None,
) -> dict:

    title = title if title is not None else f"{fake.word()} title"
    price = price if price is not None else fake.random_number()
    description = description if description is not None else f"{fake.word()} description"
    category = category if category is not None else f"{fake.word()} category"
    image = image if image is not None else "here is your image"

    result = {
        "id": product_id,
        "title": title,
        "price": price,
        "description": description,
        "category": category,
        "image": image
    }

    return result


    # todo: добавить create_custom_entity - to_add, to_delete


if __name__ == '__main__':
    import pprint

    x = generate_new_product()
    pprint.pp(x)
