import pybasic
import car

if __name__ == "__main__":
    fname = "sample.txt"
    with open("sample.txt") as f:
        pybasic.ext_file_word_counter(fname)

    my_car = car.Car("Toyota", "Camry", 2022)
    my_car.start_engine()

