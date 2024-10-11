# lib/owner_pet.py

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # A list to store pets of this owner

    def pets(self):
        """Return all pets of the owner."""
        return self._pets

    def add_pet(self, pet):
        """Add a pet to the owner, ensuring pet is of type Pet."""
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        self._pets.append(pet)
        pet.owner = self  # Set this owner to the pet's owner

    def get_sorted_pets(self):
        """Return a sorted list of the owner's pets by name."""
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # To store all instances of pets

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Allowed types: {Pet.PET_TYPES}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)  # Add pet instance to class-level list
        
        # If an owner is passed, add the pet to the owner's pet list
        if owner:
            owner.add_pet(self)
