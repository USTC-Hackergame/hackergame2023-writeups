import pyvips
import base64

if __name__ == "__main__":
    binary = input("Base64 of binary: ")
    b1, b2 = binary.split("!")
    b1 = base64.b64decode(b1)
    b2 = base64.b64decode(b2)

    img1 = pyvips.Image.new_from_buffer(b1, options="", access='sequential')
    img2 = pyvips.Image.new_from_buffer(b2, options="", access='sequential')

    if img1.hasalpha():
        img1 = img1.extract_band(0, n=img1.bands - 1)
    if img2.hasalpha():
        img2 = img2.extract_band(0, n=img2.bands - 1)

    # Check if the two images have the same dimensions
    if img1.width != img2.width or img1.height != img2.height:
        print("Dimensions of the two images are not the same.")
        exit()

    # Check if every pixel in the two images are the same
    # It does this by subtracting img2 from img1, and seeing if there are any non-zero pixels.
    # If there are any non-zero pixels, then the two images are not identical.
    difference = (img1 - img2).abs().max()

    if difference == 0:
        print("OK")
        exit()
    else:
        print("The images are not identical at the pixel level.")
        exit()
