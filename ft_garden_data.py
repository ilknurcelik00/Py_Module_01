class Plant:
    def __init__(self, name, height, ages):
        self.name = name
        self.height = height
        self.ages = ages

    def show(self):
        print(self.name, ":", self.height, "cm,", self.ages, "days old")


if __name__ == "__main__":
    print("\n=== Garden Plant Registry ===")

    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    plant1.show()
    plant2.show()
    plant3.show()
