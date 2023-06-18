from generate_image.generate import generate_image, initialize_diffusers
import time

if __name__ == "__main__":
    time_s = time.time()
    pipe = initialize_diffusers()
    time_m = time.time()
    images = generate_image(pipe, 'dog', 1000)
    time_e = time.time()
    print(time_m - time_s)
    print(time_e - time_s)
